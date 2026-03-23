# more of less

A minimal blog inspired by Dieter Rams’ “less but better”.

---

## Design constraints

- 1 font, Work Sans
- 3 font sizes, Title, Body, Meta
- 1 font weight
- 3 colours, with light and dark mode

---

## Design tokens

### Font
- Work Sans
- Weight: 400 only

### Font sizes
- Title: 32px (`2rem`)
- Body: 18px (`1.125rem`)
- Meta: 14px (`0.875rem`)

### Colours

#### Light
- Background: `#aab7bf`
- Text: `#261201`
- Accent: `#5f503e`

#### Dark
- Background: `#3b4b59`
- Text: `#e0e4e1`
- Accent: `#d9d2c6`

---

## Project structure

```
more-of-less/
├── posts/
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── post.html
│   └── about.html
├── css/
│   └── styles.css
├── docs/
├── generate_blog.py
├── new_post.py
├── requirements.txt
└── favicon.ico
```

---

## Templates

The site uses Jinja template inheritance.

- `base.html` defines the shared layout
- `index.html` renders the homepage
- `post.html` renders individual posts
- `about.html` renders the about page

---

## Content

Posts are written in Markdown and stored in `posts/`.

Each post uses minimal frontmatter:

```yaml
---
title: Customising my .zshrc on macOS
date: 2026-03-12
slug: customising-my-zshrc-on-macos
---
```

---

## Build process

Generate the site with:

```
python generate_blog.py
```

This script:

- reads posts from `posts/`
- renders templates from `templates/`
- writes output to `docs/`
- copies `css/styles.css`
- copies `favicon.ico`

---

## Output

```
docs/
├── index.html
├── about.html
├── customising-my-zshrc-on-macos.html
├── css/
│   └── styles.css
└── favicon.ico
```

---

## Writing workflow

### Local (Mac)

1. Create a new post:
   ```
   python new_post.py
   ```

2. Edit the file in `posts/`
3. Generate the site:
   ```
   python generate_blog.py
   ```

4. Open `docs/index.html` in a browser
5. Commit and push

---

### Mobile (Drafts)

A Drafts action allows posting directly to GitHub:

- Uses the first line as the title
- Generates a clean slug
- Creates a Markdown file in `posts/`
- Pushes to GitHub via API

This triggers GitHub Actions, which:

- runs `generate_blog.py`
- updates `docs/`
- publishes via GitHub Pages

---

## GitHub Actions

- `.github/workflows/build-blog.yml`
  - triggers on changes to posts, templates, or generator
  - installs dependencies
  - runs the generator
  - commits updated `docs/`

GitHub Pages serves the site from the `docs/` folder on the `main` branch.

---

## Notes for AI tools

- `docs/` is generated output, do not edit manually
- content lives in `posts/`
- templates define structure
- always regenerate after changes

---

## Approach

Built step by step with small, deliberate changes.

The focus is on clarity, semantic HTML, and simplicity over speed.