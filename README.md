# my-themes
A repository dedicated to my personalized themes for webpages and apps.

## Create CSS 'bundle'
```bash
python3 scripts/build_bundle.py
```

## File Tree 
```
my-themes
├── demo
│   ├── icon-testing.html
│   └── index.html
├── __init__.py
├── LICENSE
├── package.json
├── package-lock.json
├── pyproject.toml
├── README.md
├── scripts
│   └── build_bundle.py
├── theme
│   ├── css
│   │   ├── base
│   │   │   ├── layout.css
│   │   │   ├── reset.css
│   │   │   ├── responsive.css
│   │   │   ├── theme.css
│   │   │   └── variables.css
│   │   ├── components
│   │   │   ├── buttons.css
│   │   │   ├── cards.css
│   │   │   ├── feature-box.css
│   │   │   ├── icons.css
│   │   │   ├── search.css
│   │   │   └── typography.css
│   │   ├── overrides
│   │   │   ├── flask.css
│   │   │   ├── html.css
│   │   │   └── streamlit.css
│   │   └── utilities
│   │       ├── grid.css
│   │       └── utilities.css
│   ├── images
│   │   ├── dragon.png
│   │   ├── ember.png
│   │   ├── favicon.png
│   │   └── wisp.jpg
│   └── js
│       ├── common.js
│       ├── copy-code.js
│       └── search.js
└── tree.txt
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
