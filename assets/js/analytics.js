(() => {
  if (location.protocol !== 'https:' || !['wuzi.dev', 'www.wuzi.dev'].includes(location.hostname)) return;
  window.dataLayer = window.dataLayer || [];
  window.gtag = function () { window.dataLayer.push(arguments); };
  window.gtag('js', new Date());
  window.gtag('config', 'G-QD8G5JD9HB');
  const script = document.createElement('script');
  script.async = true;
  script.src = 'https://www.googletagmanager.com/gtag/js?id=G-QD8G5JD9HB';
  document.head.appendChild(script);
})();
