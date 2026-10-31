const button = document.getElementById('menu-button');
button.addEventListener('click', () => {
  const open = button.getAttribute('aria-expanded') !== 'true';
  button.setAttribute('aria-expanded', String(open));
  document.getElementById('navigation').classList.toggle('open', open);
});

// Sem conexão, o código Mermaid continua disponível para leitura.
const diagrams = [...document.querySelectorAll('code.language-mermaid')];
if (diagrams.length) {
  import('https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs')
    .then(async ({default: mermaid}) => {
      mermaid.initialize({startOnLoad: false, securityLevel: 'strict', theme: 'neutral'});
      for (const [index, code] of diagrams.entries()) {
        try {
          const {svg} = await mermaid.render(`diagram-${index}`, code.textContent);
          const box = document.createElement('div');
          box.className = 'diagram';
          box.innerHTML = svg;
          const source = document.createElement('details');
          source.className = 'diagram-source';
          const summary = document.createElement('summary');
          summary.textContent = 'Ver código do diagrama';
          const pre = code.parentElement;
          pre.before(box, source);
          source.append(summary, pre);
        } catch { /* Mantém o código original se o diagrama não renderizar. */ }
      }
    }).catch(() => {
      for (const code of diagrams) {
        const note = document.createElement('p');
        note.className = 'diagram-note';
        note.textContent = 'Diagrama em código: a visualização gráfica precisa de conexão com a internet.';
        code.parentElement.before(note);
      }
    });
}

const editButton = document.getElementById('edit-button');
if (editButton) {
  const editor = document.getElementById('editor');
  const source = document.getElementById('editor-source');
  const saveButton = document.getElementById('save-button');
  const cancelButton = document.getElementById('cancel-button');
  const status = document.getElementById('editor-status');
  const article = document.querySelector('article');
  const contents = document.querySelector('.contents');
  const articlePath = new URL(document.querySelector('.article-tools a').href).pathname;
  let original = '';
  let revision = '';
  let token = '';
  let saving = false;
  const dirty = () => !editor.hidden && source.value !== original;
  const closeEditor = () => {
    editor.hidden = true;
    article.hidden = false;
    contents.hidden = false;
    editButton.hidden = false;
    editButton.focus();
  };
  editButton.addEventListener('click', async () => {
    editButton.disabled = true;
    status.textContent = 'Abrindo editor…';
    try {
      const response = await fetch(`${articlePath}?edit=1`);
      const data = await response.json();
      if (!response.ok) throw new Error(data.error || 'Não foi possível abrir o editor.');
      original = data.source;
      revision = data.revision;
      token = data.token;
      source.value = original;
      editor.hidden = false;
      article.hidden = true;
      contents.hidden = true;
      editButton.hidden = true;
      status.textContent = '';
      source.focus();
    } catch (error) { status.textContent = error.message; }
    finally { editButton.disabled = false; }
  });
  cancelButton.addEventListener('click', () => {
    if (dirty() && !confirm('Descartar as alterações deste artigo?')) return;
    closeEditor();
    status.textContent = 'Edição cancelada. O arquivo não foi alterado.';
  });
  saveButton.addEventListener('click', async () => {
    saving = true;
    saveButton.disabled = cancelButton.disabled = true;
    source.readOnly = true;
    status.textContent = 'Salvando…';
    try {
      const response = await fetch(`${articlePath}?save=1`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json', 'X-Wiki-Token': token},
        body: JSON.stringify({source: source.value, revision})
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.error || 'Não foi possível salvar.');
      original = source.value;
      sessionStorage.setItem('wiki-saved', articlePath);
      location.reload();
    } catch (error) { status.textContent = error.message; }
    finally {
      saving = false;
      saveButton.disabled = cancelButton.disabled = false;
      source.readOnly = false;
    }
  });
  window.addEventListener('beforeunload', event => {
    if (dirty() || saving) { event.preventDefault(); event.returnValue = ''; }
  });
  if (sessionStorage.getItem('wiki-saved') === articlePath) {
    sessionStorage.removeItem('wiki-saved');
    status.textContent = 'Alterações salvas. A versão anterior foi guardada em backup.';
  }
}
