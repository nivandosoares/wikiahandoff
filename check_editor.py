"""Verifica edição em documentos temporários, sem alterar os artigos da wiki."""
import json
import tempfile
import threading
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import server
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def request(base, route, payload=None, headers=None):
    data = None if payload is None else json.dumps(payload).encode()
    try:
        with urlopen(Request(base + route, data=data, headers=headers or {})) as response:
            return response.status, response.read()
    except HTTPError as error:
        return error.code, error.read()


with tempfile.TemporaryDirectory(prefix='wiki-editor-test-') as temporary:
    root = Path(temporary)
    server.DOCS = root / 'docs'
    server.BACKUPS = root / 'backups'
    server.DOCS.mkdir()
    document = server.DOCS / 'README.md'
    original = '# Artigo de teste\n\nConteúdo original.\n'
    document.write_text(original)
    httpd = server.ThreadingHTTPServer(('127.0.0.1', 0), server.Handler)
    worker = threading.Thread(target=httpd.serve_forever, daemon=True)
    worker.start()
    base = f'http://127.0.0.1:{httpd.server_port}'
    try:
        status, body = request(base, '/README.md?edit=1')
        assert status == 200
        edit = json.loads(body)
        headers = {'Origin': base, 'X-Wiki-Token': edit['token'], 'Content-Type': 'application/json'}
        payload = {'source': '# Atualizado\n\nTexto **salvo**.\n', 'revision': edit['revision']}
        assert request(base, '/README.md?save=1', payload, headers)[0] == 200
        assert document.read_text() == payload['source']
        assert next(server.BACKUPS.rglob('README.md')).read_text() == original
        assert request(base, '/README.md?save=1', payload, headers)[0] == 409
        assert request(base, '/README.md?save=1', payload, {'Origin': base})[0] == 403
        assert request(base, '/README.md?save=1', payload, {**headers, 'Origin': 'http://outro-site.invalid'})[0] == 403
        assert request(base, '/README.md?edit=1', headers={'Host': 'outro-site.invalid'})[0] == 403
        assert request(base, '/%2e%2e/server.py?edit=1')[0] == 404
        assert request(base, '/backups/README.md')[0] == 404
        status, body = request(base, '/README.md', headers={'Host': '192.168.88.10'})
        assert status == 200 and b'id="edit-button"' not in body

        options = webdriver.ChromeOptions()
        options.binary_location = '/usr/bin/chromium'
        for flag in ['--headless', '--no-sandbox', '--disable-dev-shm-usage']:
            options.add_argument(flag)
        with webdriver.Chrome(service=Service('/usr/bin/chromedriver'), options=options) as browser:
            wait = WebDriverWait(browser, 10)
            browser.set_window_size(1440, 1000)
            browser.get(base)
            browser.find_element(By.ID, 'edit-button').click()
            wait.until(lambda b: b.find_element(By.ID, 'editor').is_displayed())
            source = browser.find_element(By.ID, 'editor-source')
            source.clear()
            source.send_keys('# Edição pelo navegador\n\nConteúdo preenchido pelo usuário.')
            browser.find_element(By.ID, 'save-button').click()
            wait.until(lambda b: b.find_element(By.CSS_SELECTOR, 'article h1').text == 'Edição pelo navegador')
            assert 'Alterações salvas' in browser.find_element(By.ID, 'editor-status').text
            assert 'Conteúdo preenchido pelo usuário.' in document.read_text()
            browser.find_element(By.ID, 'edit-button').click()
            wait.until(lambda b: b.find_element(By.ID, 'editor').is_displayed())
            browser.find_element(By.ID, 'editor-source').send_keys(' Não salvar')
            browser.find_element(By.ID, 'cancel-button').click()
            browser.switch_to.alert.accept()
            assert not browser.find_element(By.ID, 'editor').is_displayed()
            assert 'Não salvar' not in document.read_text()
            browser.set_window_size(390, 844)
            browser.find_element(By.ID, 'edit-button').click()
            wait.until(lambda b: b.find_element(By.ID, 'editor').is_displayed())
            assert browser.execute_script('return document.documentElement.scrollWidth <= innerWidth')
            browser.save_screenshot('/tmp/handover-wiki-editor-mobile.png')
            browser.find_element(By.ID, 'cancel-button').click()
            browser.get('http://127.0.0.1:8088/')
            assert browser.find_element(By.ID, 'edit-button').is_displayed()
            assert '[informação ausente]' not in browser.find_element(By.TAG_NAME, 'body').text
        print('OK: salvar, backup, conflito, origem/token, acesso local, caminhos, cancelar e editor móvel.')
    finally:
        httpd.shutdown()
        httpd.server_close()
        worker.join()
