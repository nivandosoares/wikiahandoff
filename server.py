#!/usr/bin/env python3
"""Wiki de leitura e edição local dos Markdown do handover."""
import argparse
import hashlib
import html
import json
import os
import re
import secrets
import tempfile
import threading
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

import markdown

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / 'docs'
BACKUPS = ROOT / 'backups'
EDIT_TOKEN = secrets.token_urlsafe(32)
SAVE_LOCK = threading.Lock()


def revision(source):
    return hashlib.sha256(source).hexdigest()


def document_path(route):
    path = unquote(urlsplit(route).path).lstrip('/') or 'README.md'
    candidate = (DOCS / path).resolve()
    if not candidate.is_relative_to(DOCS.resolve()) or candidate.suffix != '.md' or not candidate.is_file():
        return None
    return candidate


def title(path):
    for line in path.read_text(encoding='utf-8').splitlines():
        if line.startswith('# '):
            return line[2:].strip()
    return path.stem


def nav(current):
    parts = []
    groups = [('Documentação', sorted(DOCS.glob('*.md'))), ('Sistemas e ferramentas', sorted((DOCS / 'sistemas').glob('*.md')))]
    for label, files in groups:
        parts.append(f'<h2>{label}</h2><ul>')
        for path in files:
            relative = path.relative_to(DOCS).as_posix()
            name = 'Página inicial' if path.name == 'README.md' else title(path)
            active = ' aria-current="page"' if path == current else ''
            parts.append(f'<li><a href="/{quote(relative)}"{active}>{html.escape(name)}</a></li>')
        parts.append('</ul>')
    return ''.join(parts)


def page(path, editable=False):
    source = path.read_text(encoding='utf-8')
    # Adiciona espaços para que os blocos citados funcionem mesmo colados ao título.
    source = re.sub(r'(^# .+\n)(?=>)', r'\1\n', source, flags=re.M)
    converter = markdown.Markdown(extensions=['tables', 'fenced_code', 'toc', 'sane_lists'], extension_configs={'toc': {'permalink': False}})
    content = converter.convert(source)
    # Destaca campos pendentes apenas em texto, sem modificar links ou o Markdown.
    content = re.sub(r'(<[^>]*>)|(\{\{(?:PREENCHER[^}]*|DATA)\}\})', lambda m: m[1] if m[1] else f'<mark>{m[2]}</mark>', content)
    content = re.sub(r'<table>(.*?)</table>', r'<div class="table-scroll"><table>\1</table></div>', content, flags=re.S)
    name = title(path)
    relative = path.relative_to(DOCS).as_posix()
    modified = datetime.fromtimestamp(path.stat().st_mtime).strftime('%d/%m/%Y às %H:%M')
    template = (ROOT / 'template.html').read_text(encoding='utf-8')
    values = {'TITLE': html.escape(name), 'NAV': nav(path), 'CONTENT': content, 'TOC': converter.toc, 'SOURCE': quote(relative), 'MODIFIED': modified, 'PATH': html.escape(relative), 'EDIT_BUTTON': '<button id="edit-button" type="button">Editar artigo</button>' if editable else ''}
    for key, value in values.items():
        template = template.replace(f'@@{key}@@', value)
    return template.encode('utf-8')


class Handler(BaseHTTPRequestHandler):
    def local_editor(self):
        host = urlsplit('http://' + self.headers.get('Host', '')).hostname
        return self.client_address[0] in ('127.0.0.1', '::1') and host in ('localhost', '127.0.0.1', '::1')

    def send_json(self, status, data):
        body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        origin = self.headers.get('Origin')
        expected_origin = 'http://' + self.headers.get('Host', '')
        if (not self.local_editor() or origin != expected_origin
                or not secrets.compare_digest(self.headers.get('X-Wiki-Token', ''), EDIT_TOKEN)):
            self.send_json(403, {'error': 'Edição permitida somente pelo localhost com a página da wiki aberta.'})
            return
        path = document_path(self.path)
        if path is None or urlsplit(self.path).query != 'save=1':
            self.send_json(404, {'error': 'Documento não encontrado.'})
            return
        try:
            length = int(self.headers.get('Content-Length', '0'))
            if not 0 < length <= 2_000_000:
                self.send_json(413, {'error': 'Artigo maior que o limite de 2 MB.'})
                return
            data = json.loads(self.rfile.read(length))
            if not isinstance(data, dict) or not isinstance(data.get('source'), str) or not isinstance(data.get('revision'), str):
                raise ValueError('Formato inválido')
        except (ValueError, UnicodeError):
            self.send_json(400, {'error': 'Conteúdo inválido.'})
            return
        try:
            with SAVE_LOCK:
                previous = path.read_bytes()
                if data['revision'] != revision(previous):
                    self.send_json(409, {'error': 'O artigo mudou desde que você abriu o editor. Copie seu texto antes de recarregar para comparar as versões.'})
                    return
                relative = path.relative_to(DOCS.resolve())
                backup = BACKUPS / datetime.now().strftime('edicao-%Y%m%d-%H%M%S-%f') / relative
                backup.parent.mkdir(parents=True, exist_ok=True)
                backup.write_bytes(previous)
                body = data['source'].encode('utf-8')
                temp_path = None
                try:
                    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as temp:
                        temp_path = Path(temp.name)
                        temp.write(body)
                        temp.flush()
                        os.fsync(temp.fileno())
                    os.chmod(temp_path, path.stat().st_mode & 0o777)
                    os.replace(temp_path, path)
                finally:
                    if temp_path and temp_path.exists():
                        temp_path.unlink()
            self.send_json(200, {'saved': True, 'revision': revision(body)})
        except OSError:
            self.send_json(500, {'error': 'Não foi possível salvar. Seu texto continua no editor; confira as permissões e o espaço em disco.'})

    def do_GET(self):
        route = urlsplit(self.path).path
        if route in ('/style.css', '/wiki.js'):
            target = ROOT / route.lstrip('/')
            body = target.read_bytes()
            kind = 'text/css' if route.endswith('.css') else 'text/javascript'
        else:
            path = document_path(self.path)
            if path is None:
                self.send_error(404, 'Documento não encontrado')
                return
            if urlsplit(self.path).query == 'edit=1':
                if not self.local_editor():
                    self.send_json(403, {'error': 'Abra a wiki pelo localhost para editar.'})
                    return
                source = path.read_bytes()
                self.send_json(200, {'source': source.decode('utf-8'), 'revision': revision(source), 'token': EDIT_TOKEN})
                return
            if urlsplit(self.path).query == 'source=1':
                body = path.read_bytes()
                kind = 'text/plain'
            else:
                body = page(path, editable=self.local_editor())
                kind = 'text/html'
        self.send_response(200)
        self.send_header('Content-Type', f'{kind}; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.end_headers()
        self.wfile.write(body)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', type=int, default=8088)
    args = parser.parse_args()
    server = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f'Wiki disponível em http://{args.host}:{args.port}', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
