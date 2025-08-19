# my-themes
A repository dedicated to my personalized themes for webpages and apps.

## Create CSS 'bundle'
⚠️ Skipping minification

```bash
python3 scripts/build_bundle.py
```

## Old File Tree 
```
app-themes/
│
├── flask/
│   ├── templates/
│   │   ├── base.html
│   │   └── footer.html
│   └── static/
│       ├── css/
│       │   ├── style.css
│       │   ├── theme.css
│       │   ├── search.css
│       │   ├── streamlit_style.css
│       │   └── buttons/
│       │       ├── buttons_1.css
│       │       └── buttons_rainbow.css
│       ├── js/
│       │   ├── common.js
│       │   ├── copy-code.js
│       │   └── search.js
│       └── images/         # only if they are core branding
│           ├── logo.png
│           └── favicon.png
│
├── streamlit/
│   ├── config.toml         # generic theme config (colors/fonts)
│   └── theme.css           # optional injected CSS
│
├── python/
│   ├── style.py            # reusable style utils
│   └── colormaps.py        # shared colormap definitions
│
├── README.md
└── LICENSE
```

## 'Weaving' the files together in HTML `<head>` 
(remember order matters)
```html
<link rel="stylesheet" href="/css/base.css">
<link rel="stylesheet" href="/css/layouts.css">
<link rel="stylesheet" href="/css/components.css">
<link rel="stylesheet" href="/css/responsive.css">  
<link rel="stylesheet" href="/css/overrides.css"> <!-- last, overrides previous -->
```