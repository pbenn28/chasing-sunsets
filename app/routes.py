from app import app
import os
import yaml
import markdown
import sqlite3
from datetime import datetime, timezone
import smtplib
from email.mime.text import MIMEText
from flask import render_template, request, redirect, url_for, abort, jsonify
import requests
from app.static.python.sunset_check import *

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

@app.route('/sunset')
def start():
    try:
        ip_addr = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]
        print("IP for sunset calculation: " + ip_addr)
        lat, lon = get_ip_lat_log(ip_addr)

        now = datetime.now(timezone.utc)

        response = requests.get(
            f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lon}&formatted=0"
        )
        data = response.json()
        
        sunset_str = data["results"]["sunset"]  # e.g. "2026-04-11T02:34:21+00:00"
        sunset_time = datetime.fromisoformat(sunset_str)  # timezone-aware UTC datetime

        diff_min = (sunset_time - now).total_seconds() / 60
        print(f"Minutes until sunset: {diff_min}")

        if 0 < diff_min < 90:
            return render_template('index_sunset.html', description="Hi! It's nice to meet you.")
        else:
            return render_template('index.html', description="Hi! It's nice to meet you.")
    except Exception as e:
        print(f"Error: {e}")
        return render_template('index.html', description="Hi! It's nice to meet you.")

@app.route('/')
@app.route('/start')
@app.route('/index')
def sunset():
    return render_template('index_sunset.html', description="Hi! It's nice to meet you.")

@app.route('/end')
def end():
    return render_template('end.html')

# CONTENTS
@app.route('/contents')
def contents():
    return render_template('contents.html', description="Hi! It's nice to meet you.")

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
    return render_template('prologue_1.html', description="Hi! It's nice to meet you.")

@app.route('/prologue/2')
def prologue_2():
    return render_template('prologue_2.html', description="Hi! It's nice to meet you.")

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

@app.route("/blog/<slug>")
def blog_post(slug):
    posts_dir = os.path.join(os.getcwd(), "app", "posts")

    post_dates = {
        "dark": "260513",
        "clouds": "260510",
        "dropout": "260413",
        "mission": "260410",
        "safe": "260317",
        "golumbia": "250827",
        "visions": "250610",
        "etch": "250320",
        "crystallization": "241215"
    }

    order = ["contents","dark","clouds","dropout","mission","safe","golumbia","visions","etch","crystallization","end"]

    # Expected file path for the post
    post_path = os.path.join(posts_dir, post_dates[slug])
    post_path = post_path + "_" + slug + ".md"

    if not os.path.exists(post_path):
        print('Path does not exist')
        abort(404)  # If file doesn't exist

    try:
        last_page = "/blog/" + order[order.index(slug)-1]
        next_page = "/blog/" + order[order.index(slug)+1]
    except ValueError:
        print('Neighboring files do not exist')
        abort(404)

    post = parse_post(post_path)
    return render_template(f"blog_post.html", **post, next_page=next_page, last_page=last_page)

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

    order = ["contents","recs","quotes","intros","todo","future-posts","contents/work","orpheus","orange","wasteland","grandma","air","burghers","palm","alaska","end"]

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

@app.route('/projects/contents/former')
def projects_contents_former():
    return render_template('projects_contents_former.html')

@app.route("/projects/<slug>")
def projects_post(slug):
    posts_dir = os.path.join(os.getcwd(), "app", "projects")

    order = ["contents","gratta","useso","ssb","sias","smunc","scioly","dorm-lectures","hackuba","chasing-sunsets","contents/former","wtp","ess","prometheus","hs-scibowl","hs-scioly","ms-scibowl","esods","cosmos","ieso","end"]

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
    return render_template(f"projects_post.html", **post, next_page=next_page, last_page=last_page)

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

# AI LEGISLATION TRACKER
STATUS_META = {
    "discussion_draft":   {"label": "Discussion Draft",        "class": "status-draft"},
    "introduced":         {"label": "Introduced",              "class": "status-introduced"},
    "committee":          {"label": "In Committee",            "class": "status-committee"},
    "committee_passed":   {"label": "Cleared Committee",       "class": "status-committee-passed"},
    "passed_one_chamber": {"label": "Passed One Chamber",      "class": "status-passed-one"},
    "passed_both":        {"label": "Passed Both Chambers",    "class": "status-passed-both"},
    "signed":             {"label": "Signed Into Law",         "class": "status-signed"},
    "failed":             {"label": "Failed / Died",           "class": "status-failed"},
    "vetoed":             {"label": "Vetoed",                  "class": "status-vetoed"},
}

SCORING_WEIGHTS = {
    "w_A": 1.0,   # frontier developer stringency weight in composite S (the base axis)
    "w_B": 0.6,   # preemption posture weight in composite S
    "w_C": 0.3,   # governance capacity weight in composite S
    "w_D": 0.0,   # external/geopolitical weight -- excluded from composite by default
    "w_F": 0.75,   # capability buildout constraint weight in composite S
}


def _clamp(x, lo, hi):
    return max(lo, min(hi, x))


def compute_S(axes, weights=SCORING_WEIGHTS):
    """Server-side default-weight S for SSR sort/display only. The frontend
    recomputes this same formula live so the weight sliders never require a
    re-score -- keep both in sync if this formula changes."""
    raw = (
        weights["w_A"] * axes["A"]
        + weights["w_B"] * axes["B"]
        + weights["w_C"] * axes["C"]
        + weights["w_D"] * axes["D"]
        + weights["w_F"] * axes["F"]
    )
    return _clamp(raw, -5.0, 5.0)


def compute_impact(components):
    r, d, ef, p = components["R"], components["D"], components["E_f"], components["P"]
    return 10 * (0.35 * r + 0.30 * d + 0.20 * ef + 0.15 * p)


def parse_bill(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    parts = content.split('---', 2)
    metadata = yaml.safe_load(parts[1]) or {}
    body_content = parts[2].strip() if len(parts) > 2 else ''

    slug = os.path.splitext(os.path.basename(filepath))[0]
    status_key = metadata.get('status', 'introduced')
    status_meta = STATUS_META.get(status_key, {"label": status_key.replace('_', ' ').title(), "class": "status-introduced"})

    scoring_raw = metadata.get('scoring') or {}
    is_scored = bool(scoring_raw)

    axes = {k: scoring_raw.get('axes', {}).get(k, 0.0) for k in ('A', 'B', 'C', 'D', 'F')}
    unsigned = {k: scoring_raw.get('unsigned', {}).get(k, 0.0) for k in ('E_consumer',)}
    impact_components = {k: scoring_raw.get('impact_components', {}).get(k, 0.0) for k in ('R', 'D', 'E_f', 'P')}
    likelihood = {
        'p_committee': scoring_raw.get('likelihood', {}).get('p_committee'),
        'p_enact': scoring_raw.get('likelihood', {}).get('p_enact', 0.0),
        'basis': scoring_raw.get('likelihood', {}).get('basis', ''),
    }
    rationale = scoring_raw.get('rationale') or {}
    text_source = scoring_raw.get('text_source', 'unknown')
    in_scatter = text_source == 'full_text'
    confidence = scoring_raw.get('confidence', 'unscored' if not is_scored else 'medium')
    if is_scored and not in_scatter:
        # A score not verified against the bill's actual text is never
        # more than low-confidence, regardless of what was written down --
        # see the text_source rule in docs/legislation-scoring-rubric.md.
        confidence = 'low'
    scored_at = scoring_raw.get('scored_at')

    s_default = compute_S(axes, SCORING_WEIGHTS)
    impact_score = compute_impact(impact_components)
    expected_impact = impact_score * (likelihood['p_enact'] or 0.0)

    return {
        'slug': slug,
        'title': metadata.get('title', 'Untitled Bill'),
        'short_name': metadata.get('short_name') or metadata.get('title', 'Untitled Bill'),
        'bill_numbers': metadata.get('bill_numbers', []),
        'congress': metadata.get('congress'),
        'status': status_key,
        'status_label': status_meta['label'],
        'status_class': status_meta['class'],
        'chamber_origin': metadata.get('chamber_origin', 'House'),
        'introduced_date': metadata.get('introduced_date', ''),
        'last_action': metadata.get('last_action', ''),
        'last_action_date': metadata.get('last_action_date', ''),
        'sponsors': metadata.get('sponsors', []),
        'cosponsor_count': metadata.get('cosponsor_count'),
        'committees': metadata.get('committees', []),
        'scoring': {
            'is_scored': is_scored,
            'axes': axes,
            'unsigned': unsigned,
            'impact_components': impact_components,
            'likelihood': likelihood,
            'rationale': rationale,
            'confidence': confidence,
            'text_source': text_source,
            'in_scatter': in_scatter,
            'scored_at': scored_at,
            's_default': round(s_default, 2),
            'impact_score': round(impact_score, 2),
            'expected_impact': round(expected_impact, 3),
        },
        'topic': metadata.get('topic', 'Other'),
        'tags': metadata.get('tags', []),
        'sources': metadata.get('sources', []),
        'summary': metadata.get('summary', ''),
        'timeline': metadata.get('timeline', []),
        'body': markdown.markdown(body_content),
    }

def load_bills():
    bills_dir = os.path.join(os.getcwd(), "app", "legislation")
    bills = []

    for filename in sorted(os.listdir(bills_dir)):
        if filename.endswith('.md'):
            bills.append(parse_bill(os.path.join(bills_dir, filename)))

    bills.sort(key=lambda b: (b['scoring']['expected_impact'], b['last_action_date']), reverse=True)
    return bills

@app.route('/ai-legislation')
def legislation():
    bills = load_bills()
    last_updated = max((b['last_action_date'] for b in bills if b['last_action_date']), default='')
    topics = sorted({b['topic'] for b in bills})

    return render_template(
        'legislation.html',
        bills=bills,
        last_updated=last_updated,
        topics=topics,
        status_options=STATUS_META,
        scoring_weights=SCORING_WEIGHTS,
        title="AI Legislation Tracker",
        description="A running, rubric-scored tracker of federal AI bills moving through Congress — sponsors, status, and where each one falls between safety/restriction and deregulation/acceleration."
    )

print("All registered routes:")
for rule in app.url_map.iter_rules():
    print(f"  {rule.rule} -> {rule.endpoint}")

@app.before_request
def log_request():
    print(f"REQUEST: {request.method} {request.path}")
    print(f"Headers: {dict(request.headers)}")