import os
import shutil
import markdown
import yaml
import datetime
import math
from jinja2 import Environment, FileSystemLoader

# Paths
POSTS_DIR = "posts"
TEMPLATES_DIR = "templates"
OUTPUT_DIR = "docs"
CSS_SRC = "css/styles.css"
FAVICON_SRC = "favicon.ico"

# Setup Jinja2
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

# Load templates
index_template = env.get_template("index.html")
post_template = env.get_template("post.html")
about_template = env.get_template("about.html")


def parse_post(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    parts = content.split("---")
    if len(parts) < 3:
        return None

    metadata = yaml.safe_load(parts[1])
    body_markdown = "---".join(parts[2:]).strip()

    if not metadata:
        return None

    title = metadata.get("title")
    slug = metadata.get("slug")
    raw_date = metadata.get("date")

    if not title or not slug or not raw_date:
        return None

    if isinstance(raw_date, datetime.date):
        date_obj = raw_date
    else:
        date_obj = datetime.datetime.strptime(raw_date, "%Y-%m-%d").date()

    formatted_date = date_obj.strftime("%-d %B %Y")
    iso_date = date_obj.isoformat()

    html_body = markdown.markdown(body_markdown)
    word_count = len(body_markdown.split())
    reading_time_minutes = max(1, math.ceil(word_count / 200))

    return {
        "title": title,
        "slug": slug,
        "date": formatted_date,
        "iso_date": iso_date,
        "reading_time": reading_time_minutes,
        "body": html_body,
        "url": f"{slug}.html",
        "filename": f"{slug}.html",
    }


def load_posts():
    posts = []

    if not os.path.exists(POSTS_DIR):
        return posts

    for filename in os.listdir(POSTS_DIR):
        if not filename.endswith(".md"):
            continue

        filepath = os.path.join(POSTS_DIR, filename)
        post = parse_post(filepath)

        if post:
            posts.append(post)
        else:
            print(f"⚠️ Skipped invalid post file: {filename}")

    posts.sort(key=lambda x: x["iso_date"], reverse=True)
    return posts


def ensure_output_dirs():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(os.path.join(OUTPUT_DIR, "css"), exist_ok=True)


def clear_old_generated_html():
    if not os.path.exists(OUTPUT_DIR):
        return

    protected_files = {"index.html", "about.html", "404.html"}

    for filename in os.listdir(OUTPUT_DIR):
        if not filename.endswith(".html"):
            continue
        if filename in protected_files:
            continue
        os.remove(os.path.join(OUTPUT_DIR, filename))


def render_posts(posts):
    for post in posts:
        output_html = post_template.render(post=post)
        output_path = os.path.join(OUTPUT_DIR, post["filename"])

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(output_html)


def render_index(posts):
    output_html = index_template.render(posts=posts)
    output_path = os.path.join(OUTPUT_DIR, "index.html")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output_html)


def render_about():
    output_html = about_template.render()
    output_path = os.path.join(OUTPUT_DIR, "about.html")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output_html)


def copy_css():
    if os.path.exists(CSS_SRC):
        shutil.copy(CSS_SRC, os.path.join(OUTPUT_DIR, "css", "styles.css"))
        print("✅ styles.css copied")
    else:
        print("❌ styles.css not found")


def copy_favicon():
    if os.path.exists(FAVICON_SRC):
        shutil.copy(FAVICON_SRC, os.path.join(OUTPUT_DIR, "favicon.ico"))
        print("✅ favicon.ico copied")
    else:
        print("⚠️ No favicon found, skipping")


def main():
    ensure_output_dirs()
    clear_old_generated_html()

    posts = load_posts()

    render_posts(posts)
    render_index(posts)
    render_about()
    copy_css()
    copy_favicon()

    print("✅ Blog generated successfully.")

if __name__ == "__main__":
    main()
