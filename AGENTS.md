# AGENTS.md

Guidelines for working with the "more of less" blog.

---

## Core principle

Less, but better.

Prefer removing complexity over adding features.

---

## Project model

- `posts/` → source content (Markdown)
- `templates/` → structure (Jinja templates)
- `docs/` → generated output (HTML)

Never edit files in `docs/` manually.

---

## Content

Posts live in `posts/` and use minimal frontmatter:

```yaml
---
title: My Post Title
date: YYYY-MM-DD
slug: my-post-title
---
```

- `title` is human-readable  
- `slug` must be URL-safe  
- `date` is used for sorting and display  

---

## Templates

- `base.html` defines layout
- `index.html` lists posts
- `post.html` renders a single post
- `about.html` is static content

Use semantic HTML. Do not add unnecessary structure.

---

## Generator

`generate_blog.py`:

- reads Markdown from `posts/`
- converts to HTML
- renders templates
- writes to `docs/`

Keep the generator simple.

Avoid adding:
- pagination
- tags
- search
- image processing

Unless there is a clear need.

---

## Writing workflow

Create a new post:

```bash
python new_post.py
```

Then:

```bash
python generate_blog.py
```

---

## Deployment

- GitHub Actions runs `generate_blog.py`
- `docs/` is committed and served via GitHub Pages

---

## Rules for AI tools

- Do not modify `docs/`
- Do not introduce new dependencies without justification
- Do not add features that increase complexity unnecessarily
- Prefer clarity over cleverness

---

## When making changes

Ask:

- Does this make the system simpler?
- Is this necessary?
- Can this be done with fewer moving parts?

If not, do not add it.