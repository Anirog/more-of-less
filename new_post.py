import os
import re
from datetime import date


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def get_unique_filepath(posts_dir, slug):
    filepath = os.path.join(posts_dir, f"{slug}.md")

    if not os.path.exists(filepath):
        return filepath, slug

    counter = 2
    while True:
        new_slug = f"{slug}-{counter}"
        filepath = os.path.join(posts_dir, f"{new_slug}.md")
        if not os.path.exists(filepath):
            return filepath, new_slug
        counter += 1


title = input("Post title: ").strip()

if not title:
    print("❌ Title cannot be empty.")
    raise SystemExit(1)

today = date.today().isoformat()
base_slug = slugify(title)

posts_dir = "posts"
os.makedirs(posts_dir, exist_ok=True)

filepath, slug = get_unique_filepath(posts_dir, base_slug)

frontmatter = f"""---
title: {title}
date: {today}
slug: {slug}
---

Write here.
"""

with open(filepath, "w", encoding="utf-8") as f:
    f.write(frontmatter)

print(f"✅ Created new post: {filepath}")