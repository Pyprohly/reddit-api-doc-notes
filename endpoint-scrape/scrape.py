#!/usr/bin/env python3
import sys
import os
import os.path as op
from contextlib import contextmanager
from urllib.request import Request, urlopen

import bs4

if op.abspath(os.getcwd()) != op.dirname(op.abspath(__file__)):
	print('Current directory must match script directory', file=sys.stderr)
	sys.exit(1)

@contextmanager
def pushd(path):
	prev = os.getcwd()
	os.chdir(path)
	try:
		yield
	finally:
		os.chdir(prev)

class Endpoint:
	def __init__(self, verb, path, variants, scope, body_html):
		self.verb = verb
		self.path = path
		self.variants = variants
		self.scope = scope
		self.body_html = body_html

	def __repr__(self):
		return f'<{self.__class__.__name__} {"[%s %s]" % (self.verb, self.path)}>'

def get_endpoint_slug(endpoint):
	slug = endpoint.path
	slug = slug.translate(str.maketrans('/:', '_-', '[]'))
	name = f'{endpoint.verb}{slug}'
	for c in name:
		assert c.isalpha() or c.isdigit() or c in '_-.', name
	return name

url = "https://www.reddit.com/dev/api"
request = Request(url, headers={"User-Agent" : "API endpoint scrape (by u/Pyprohly)"})
html = urlopen(request).read()

soup = bs4.BeautifulSoup(html, 'html.parser')
endpoints_section = soup.select_one('div.contents > div.section.methods')

sections = {}
section_name = 'none'
for tag in endpoints_section:
	if tag.name == 'h2':
		section_name = tag.get_text()
	elif tag.name == 'div':
		if 'endpoint' in tag.get('class', ()):
			h3_tag = tag.select_one('h3')

			method = h3_tag.contents[0].get_text().strip()

			path = ''
			for i in h3_tag.contents[1:]:
				if isinstance(i, bs4.element.Tag):
					if i.name == 'span':
						break
					path += i.get_text()
				elif isinstance(i, bs4.element.NavigableString):
					path += i

			body_html = tag.select_one('.info').prettify()

			scope = ''
			scope_tag = tag.select_one('.oauth-scope')
			if scope_tag is not None:
				scope = scope_tag.get_text()

			variants = ''
			uri_variants_tag = tag.select_one('.uri-variants')
			if uri_variants_tag is not None:
				variants = uri_variants_tag.get_text('\n') + '\n'

			endpoint = Endpoint(
				verb=method,
				path=path,
				variants=variants,
				scope=scope,
				body_html=body_html,
			)

			sections.setdefault(section_name, []).append(endpoint)


for k, v in sections.items():
	os.makedirs(k, exist_ok=True)
	with pushd(k):
		for endpoint in v:
			fname = get_endpoint_slug(endpoint) + '.txt'
			with open(fname, 'w') as fh:
				fh.write('''\
{0.verb} {0.path}
{0.scope}
{0.variants}
{0.body_html}
'''.format(endpoint))
