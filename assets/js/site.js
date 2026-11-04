(() => {
  const status = document.getElementById('copy-status');
  document.querySelectorAll('.post-content pre > code').forEach(code => {
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'copy-button';
    button.textContent = 'Copy';
    button.setAttribute('aria-label', 'Copy code to clipboard');
    button.addEventListener('click', async () => {
      try {
        if (!navigator.clipboard?.writeText) throw new Error('Clipboard unavailable');
        await navigator.clipboard.writeText(code.textContent);
        button.textContent = 'Copied';
        if (status) status.textContent = 'Code copied to clipboard.';
      } catch {
        const selection = window.getSelection();
        const range = document.createRange();
        range.selectNodeContents(code);
        selection?.removeAllRanges();
        selection?.addRange(range);
        button.textContent = 'Selected';
        if (status) status.textContent = 'Clipboard unavailable. Code selected; press Control or Command C to copy.';
      }
      window.setTimeout(() => { button.textContent = 'Copy'; }, 2200);
    });
    code.parentElement.appendChild(button);
  });
})();
