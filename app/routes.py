from app import app
import os
import yaml
import markdown
import sqlite3
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from flask import render_template, request, redirect, url_for, abort

print("Loaded routes.py")

def parse_post(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    if content.startswith('---'):
        # Split YAML front matter from content
        parts = content.split('---', 2)
        metadata = yaml.safe_load(parts[1])
        post_content = parts[2].strip()
    else:
        metadata = {}
        post_content = content

    return {
        'title': metadata.get('title', 'Untitled'),
        'date': metadata.get('date', ''),
        'author': metadata.get('author', ''),
        'description': metadata.get('description', ''),
        'handle': metadata.get('handle', ''),
        'tags': metadata.get('tags', []),
        'content': markdown.markdown(post_content)
    }

# START & END
@app.route('/')
@app.route('/start')
@app.route('/index')
def start():
    print('Loaded start()')
    return render_template('index.html')

@app.route('/end')
def end():
    print('Loaded end()')
    return render_template('end.html')

# CONTENTS
@app.route('/contents')
def contents():
    return render_template('contents.html')

@app.route('/contents/0')
def contents0():
    return render_template('contents0.html')

@app.route('/contents/1')
def contents1():
    return render_template('contents1.html')

@app.route('/contents/2')
@app.route('/blog/end')
def contents2():
    return render_template('contents2.html')

@app.route('/contents/3')
@app.route('/fragments/end')
def contents3():
    return render_template('contents3.html')

@app.route('/contents/4')
@app.route('/projects/end')
def contents4():
    return render_template('contents4.html')

# PROLOGUE
@app.route('/prologue')
@app.route('/prologue/1')
def prologue_1():
    return render_template('prologue_1.html')

@app.route('/prologue/2')
def prologue_2():
    return render_template('prologue_2.html')

@app.route('/praise')
def praise():
    return render_template('praise.html')

# BLOG
@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog/contents')
def blog_contents():
    posts = []
    posts_dir = os.path.join(os.getcwd(), "app", "posts")

    for filename in sorted(os.listdir(posts_dir), reverse=True):
        if filename.endswith('.md'):
            filepath = os.path.join(posts_dir, filename)
            post = parse_post(filepath)
            posts.append(post)

    return render_template('blog_contents.html', posts=posts)

@app.route("/blog/<slug>")
def blog_post(slug):
    posts_dir = os.path.join(os.getcwd(), "app", "posts")

    post_dates = {
        "golumbia": "250809",
        "visions": "250610",
        "etch": "250320",
        "crystallization": "241215"
    }

    order = ["contents","golumbia","visions","etch","crystallization","end"]

    # Expected file path for the post
    post_path = os.path.join(posts_dir, post_dates[slug])
    post_path = post_path + "_" + slug + ".md"

    if not os.path.exists(post_path):
        abort(404)  # If file doesn't exist

    try:
        last_page = "/blog/" + order[order.index(slug)-1]
        next_page = "/blog/" + order[order.index(slug)+1]
    except ValueError:
        abort(404)

    post = parse_post(post_path)
    return render_template(f"blog_post.html", **post, next_page=next_page, last_page=last_page)

@app.route('/blog/submission', methods=['POST'])
def blog_submission():
    # Get form content (avoid KeyError if missing)
    response_text = request.form.get('blog_form', '').strip()

    # Timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # IP address (proxy-aware)
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
    if ',' in ip_address:  # take first in list if multiple
        ip_address = ip_address.split(',')[0].strip()

    # Browser / OS info
    user_agent = request.user_agent.string

    # Append to file
    with open('subscriptions.txt', 'a', encoding='utf-8') as f:
        f.write(f"\n--- {timestamp} ---\n")
        f.write(f"IP: {ip_address}\n")
        f.write(f"User-Agent: {user_agent}\n")
        f.write(response_text + "\n")
        f.write("="*50 + "\n")

    return redirect('/blog/thanks')

@app.route('/blog/thanks', methods=['GET'])
def blog_thanks():
    posts = []
    posts_dir = os.path.join(os.getcwd(), "app", "posts")

    for filename in sorted(os.listdir(posts_dir), reverse=True):
        if filename.endswith('.md'):
            filepath = os.path.join(posts_dir, filename)
            post = parse_post(filepath)
            posts.append(post)

    return render_template('blog_thanks.html', posts=posts)

# FRAGMENTS
@app.route('/notes')
@app.route('/fragments')
def fragments():
    return render_template('fragments.html')

@app.route('/fragments/contents')
def fragments_contents():
    return render_template('fragments_contents.html')

@app.route('/fragments/contents/work')
def fragments_contents_work():
    return render_template('fragments_contents_work.html')

@app.route("/fragments/<slug>")
def fragments_post(slug):
    posts_dir = os.path.join(os.getcwd(), "app", "fragments")

    order = ["contents","recs","quotes","intros","todo","future-posts","contents/work","palm","alaska","bart","end"]

    # Expected file path for the post
    post_path = os.path.join(posts_dir, slug + ".md")

    if not os.path.exists(post_path):
        abort(404)  # If file doesn't exist

    try:
        last_page = "/fragments/" + order[order.index(slug)-1]
        next_page = "/fragments/" + order[order.index(slug)+1]
    except ValueError:
        abort(404)

    post = parse_post(post_path)
    return render_template(f"fragments_post.html", **post, next_page=next_page, last_page=last_page)

# PROJECTS
@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/projects/contents')
def projects_contents():
    return render_template('projects_contents.html')

@app.route("/projects/<slug>")
def projects_post(slug):
    posts_dir = os.path.join(os.getcwd(), "app", "projects")

    order = ["contents","gratta","useso","sso","sias","smunc","scioly","dorm-lectures","oasis","chasing-sunsets","wtp","ess","prometheus","fhs-scibowl","fhs-scioly","pms-scibowl","esods","cosmos","ieso","end"]

    # Expected file path for the post
    post_path = os.path.join(posts_dir, slug + ".md")

    if not os.path.exists(post_path):
        abort(404)  # If file doesn't exist

    try:
        last_page = "/projects/" + order[order.index(slug)-1]
        next_page = "/projects/" + order[order.index(slug)+1]
    except ValueError:
        abort(404)

    post = parse_post(post_path)
    return render_template(f"fragments_post.html", **post, next_page=next_page, last_page=last_page)

# EPILOGUE
@app.route('/epilogue')
def epilogue():
    return render_template('epilogue.html')

@app.route('/epilogue/submission', methods=['POST'])
def epilogue_submission():
    # Get form content (avoid KeyError if missing)
    response_text = request.form.get('epilogue_form', '').strip()

    # Timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # IP address (proxy-aware)
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
    if ',' in ip_address:  # take first in list if multiple
        ip_address = ip_address.split(',')[0].strip()

    # Browser / OS info
    user_agent = request.user_agent.string

    # Append to file
    with open('responses.txt', 'a', encoding='utf-8') as f:
        f.write(f"\n--- {timestamp} ---\n")
        f.write(f"IP: {ip_address}\n")
        f.write(f"User-Agent: {user_agent}\n")
        f.write(response_text + "\n")
        f.write("="*50 + "\n")

    return redirect('/epilogue/thanks')

@app.route('/epilogue/thanks', methods=['GET'])
def epilogue_thanks():
    return render_template('epilogue_thanks.html')

print("All registered routes:")
for rule in app.url_map.iter_rules():
    print(f"  {rule.rule} -> {rule.endpoint}")

@app.before_request
def log_request():
    print(f"REQUEST: {request.method} {request.path}")
    print(f"Headers: {dict(request.headers)}")