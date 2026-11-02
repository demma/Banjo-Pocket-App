"""Gera index.html (PWA) a partir de app.html. Uso: python3 build.py"""
from pathlib import Path
root = Path(__file__).parent
app = (root / "app.html").read_text(encoding="utf-8")
head = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#1e1815">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icons/icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="icons/icon-180.png?v=3">
</head>
<body>
"""
tail = """
<script>
// iOS, app na tela inicial com barra de status translúcida: a janela informada é mais curta que a tela
// (falta a altura da barra de status). Estica o app até a altura física; não faz nada se não houver diferença.
(function () {
  var app = document.querySelector('.app');
  function fit() {
    var standalone = navigator.standalone || (window.matchMedia && matchMedia('(display-mode: standalone)').matches);
    var portrait = !window.matchMedia || matchMedia('(orientation: portrait)').matches;
    var sh = portrait ? Math.max(screen.width, screen.height) : Math.min(screen.width, screen.height);
    if (standalone && sh > window.innerHeight + 1) { app.style.bottom = 'auto'; app.style.height = sh + 'px'; }
    else { app.style.bottom = ''; app.style.height = ''; }
  }
  fit();
  window.addEventListener('resize', fit);
  window.addEventListener('orientationchange', function () { setTimeout(fit, 300); });
})();
if ('serviceWorker' in navigator) {
  window.addEventListener('load', function () { navigator.serviceWorker.register('sw.js').catch(function () {}); });
}
</script>
</body>
</html>
"""
import re
ver = re.search(r"var APP_VERSION='([^']+)'", app).group(1)
(root / "index.html").write_text(head + app + tail, encoding="utf-8")
sw = (root / "sw.js").read_text(encoding="utf-8")
sw = re.sub(r"const CACHE = 'banjo-de-bolso-[^']*';", "const CACHE = 'banjo-de-bolso-" + ver + "';", sw)
(root / "sw.js").write_text(sw, encoding="utf-8")
print("index.html gerado · versão", ver)
