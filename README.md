# Banjo de Bolso

App web instalável (PWA) para banjo de 5 cordas: dicionário de acordes, rolos (dedilhados), riffs e ritmos, com áudio sintetizado e tablatura animada. Funciona offline depois de instalado.

**Abrir:** https://demma.github.io/Banjo-Pocket-App/

Para instalar no celular:
- iPhone (Safari): Compartilhar → Adicionar à Tela de Início
- Android (Chrome): menu ⋮ → Instalar app

## Estrutura
- `app.html`: fonte única do app (HTML + CSS + JS, sem dependências).
- `build.py`: gera `index.html` (a versão PWA) a partir de `app.html`.
- `manifest.webmanifest`, `sw.js`, `icons/`: instalação e uso offline.

Depois de editar `app.html`, rode `python3 build.py` e aumente a versão do cache em `sw.js` (`banjo-de-bolso-vN`) para os celulares receberem a atualização.

## Rodar localmente
```bash
python3 build.py
python3 -m http.server 8000   # abra http://localhost:8000
```

## Como o conteúdo é gerado
- **Acordes**: calculados a partir da afinação, sem digitação manual. Entram todas as combinações das cordas 4 a 1, com até 4 casas de abertura, que cobrem as notas obrigatórias do acorde. A ordem é por posição, número de dedos e baixo na tônica.
- **Padrões**: mini-notação definida em `app.html` (`P3 I2 M1`, `h3:2`, `/3:4`, `B3-1`, `X4-1`, `P5+M1`, `-`).
