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


# Temproary code area
```css
/* ==== Base Icon Styles ==== */
.icon {
  position: relative;
  font-size: 1.8rem;
  margin: 0.5rem;
  display: inline-black; 
  cursor: default;
  transition: transform 0.2s ease, filter 0.2s ease;
}

/* Hover animation (applies to both STEM & Tech) */
.icon:hover {
  transform: scale(1.2);
  filter: drop-shadow(0 0 5px rgba(0, 0, 0, 0.3)); 
}

/* ==== Tooltip ==== */
.icon-tooltip {
  visibility: hidden;
  background-color: #222;
  color: #fff;
  text-align: center;
  border-radius: 6px;
  padding: 4px 8px;
  position: absolute; 
  bottom: 125%; /* place above */
  left: 50%;
  transform: translateX(-50%);
  opacity: 0;
  transition: opacity 0.2s ease;
  white-space: nowrap;
  font-size: 0.8rem;
  z-index: 100;
}

.icon:hover .icon-tooltip {
  visibility: visible;
  opacity: 1;
}



/* Tech default style */
.tech-icon {
  color: #28a745;  /* green-ish */
}


/* STEM default style */
.stem-icon {
  color: #5e17eb;    /* purple-ish */
}

/* ==== Optional Floating Animation (fun effect) ==== */
@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-4px); }
}

```