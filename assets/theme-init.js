// נטען בראש כל עמוד, לפני שהעמוד מוצג, כדי שלא יהיה "הבהוב" של מצב בהיר
(function () {
    var t = null;
    try { t = localStorage.getItem('aspnet-guides-theme'); } catch (e) { }
    if (!t) t = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', t);
})();
