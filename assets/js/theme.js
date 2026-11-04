(() => {
  const key = 'wuzi-theme';
  let mode = null;
  try {
    const stored = localStorage.getItem(key);
    if (stored === 'light' || stored === 'dark') mode = stored;
  } catch { /* Reading still works when browser storage is unavailable. */ }

  function apply() {
    if (mode) document.documentElement.dataset.theme = mode;
    else delete document.documentElement.dataset.theme;
  }
  apply();
  function initialize() {
    const button = document.getElementById('theme-toggle');
    const label = document.getElementById('theme-label');
    if (!button || !label) return;
    function describe() {
      label.textContent = mode || 'auto';
      const next = mode === null ? 'light' : mode === 'light' ? 'dark' : 'system';
      button.setAttribute('aria-label', `Theme: ${mode || 'system'}. Switch to ${next} theme`);
    }
    button.hidden = false;
    describe();
    button.addEventListener('click', () => {
      mode = mode === null ? 'light' : mode === 'light' ? 'dark' : null;
      apply();
      describe();
      try {
        if (mode) localStorage.setItem(key, mode);
        else localStorage.removeItem(key);
      } catch { /* Keep the current-session preference even without persistence. */ }
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initialize);
  else initialize();
})();
