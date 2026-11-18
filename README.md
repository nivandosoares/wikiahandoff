# Wiki local do handover

Wiki local com interface web e ferramentas de verificação do editor.

**Arquivos principais**

- [server.py](<server.py>)
- [template.html](<template.html>)
- [check_editor.py](<check_editor.py>)

Mostra os arquivos de `docs/` em HTML. O editor grava as alterações nos Markdown do próprio repositório.

## Iniciar

```bash
cd handover-wiki
.venv/bin/python server.py --host 0.0.0.0 --port 8088
```

Abra `http://localhost:8088` no próprio computador. Na rede local, use o IP desse computador na porta 8088. O servidor serve somente os Markdown dentro de `docs` e os dois arquivos de interface.

## Instalar em outro ambiente

Clone este repositório e entre na pasta `handover-wiki`. É necessário Python 3.10 ou mais recente.

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python server.py
```

Abra `http://localhost:8088` para ler e editar. No Windows, use `.venv\Scripts\python.exe` no lugar de `.venv/bin/python`.

## Sincronizar entre computadores

Antes de começar a editar, atualize a cópia local:

```bash
git pull --ff-only
```

Depois de salvar os artigos pela wiki, envie as alterações:

```bash
git add docs/
git commit -m "Atualiza documentação do handover"
git push
```

No outro computador, execute `git pull --ff-only` e recarregue a página. Se houver alterações locais, faça commit antes de atualizar. Se o pull indicar divergência, reconcilie os commits antes de continuar. O salvamento pelo navegador é local; o envio ao GitHub é feito pelos comandos acima. Backups e ambientes virtuais não são enviados.

Menu lateral, índice por artigo, tabelas, campos pendentes destacados e acesso ao Markdown original. Mermaid é carregado por CDN apenas nas páginas com diagramas; sem internet, o código continua visível. O servidor não tem autenticação e foi pensado para uso local ou em rede interna.

## Editar pela própria wiki

No computador que executa o servidor, abra `http://localhost:8088`, escolha o artigo e clique em **Editar artigo**. Edite o Markdown e use **Salvar alterações**. O conteúdo é gravado diretamente no arquivo em `docs/`; **Cancelar** mantém a versão anterior.

O editor avisa antes de sair com alterações e impede salvar sobre uma versão modificada depois da abertura. Cada salvamento guarda a versão anterior em `backups/edicao-DATA-HORA/`, mantendo o caminho relativo do artigo. Para recuperar, copie o Markdown da versão desejada de volta para o mesmo caminho dentro de `docs/`.

A edição só é aceita em conexões locais por `localhost` ou `127.0.0.1`; pela rede, a wiki continua disponível para leitura. Requisições de gravação exigem origem da própria wiki e token da sessão do servidor. Os backups não são servidos pela wiki.
# wikiahandoff
