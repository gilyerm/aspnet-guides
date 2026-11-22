"""Checks every internal link on the site: the page exists, and a #section points to a real id on that page.

Run after changing pages:  python tools/check_links.py
Exits with code 1 if anything is broken.
"""
import glob
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(__file__), '..')


def strip_code(s):
    # code samples inside editors and code blocks are not real links
    return re.sub(r'<textarea.*?</textarea>|<pre.*?</pre>|<template.*?</template>', '', s, flags=re.S)


pages = {}
for path in [os.path.join(ROOT, 'index.html')] + glob.glob(os.path.join(ROOT, 'guides', '*.html')):
    with open(path, encoding='utf-8') as f:
        pages[os.path.normpath(path)] = f.read()

ids = {p: set(re.findall(r'\sid="([^"]+)"', strip_code(s))) for p, s in pages.items()}

problems = []
count = 0
for path, s in pages.items():
    for href in re.findall(r'<a\s[^>]*href="([^"]+)"', strip_code(s)):
        if re.match(r'^(https?:|mailto:|data:|javascript:)', href) or href == '#':
            continue
        count += 1
        file_part, _, frag = href.partition('#')
        target = os.path.normpath(os.path.join(os.path.dirname(path), file_part)) if file_part else path
        name = os.path.relpath(path, ROOT)
        if target not in pages:
            problems.append(f'{name}: {href} -> page not found')
        elif frag and frag not in ids[target]:
            problems.append(f'{name}: {href} -> no element with id="{frag}"')

print(f'checked {count} internal links')
for p in problems:
    print('  BROKEN', p)
sys.exit(1 if problems else 0)
