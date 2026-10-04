"""Check generated local URLs, fragments, image alternatives, and page titles."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import sys

class Document(HTMLParser):
    def __init__(self, path):
        super().__init__(); self.path=path; self.ids=set(); self.refs=[]; self.errors=[]; self.h1=0; self.title=False
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if 'id' in attrs:
            if attrs['id'] in self.ids: self.errors.append(f'duplicate id: {attrs["id"]}')
            self.ids.add(attrs['id'])
        if tag=='h1': self.h1+=1
        if tag=='title': self.title=True
        if tag=='img' and not attrs.get('alt'): self.errors.append('image missing alt text')
        for key in ('href','src'):
            if key in attrs: self.refs.append(attrs[key])

def main():
    root=Path(sys.argv[1] if len(sys.argv)>1 else 'site').resolve()
    pages={}
    errors=[]
    for path in root.rglob('*.html'):
        doc=Document(path); doc.feed(path.read_text(encoding='utf-8')); pages[path]=doc
        if doc.h1!=1: doc.errors.append(f'expected one h1, got {doc.h1}')
        if not doc.title: doc.errors.append('missing title')
        errors.extend(f'{path.relative_to(root)}: {err}' for err in doc.errors)
    for path,doc in pages.items():
        for ref in doc.refs:
            parsed=urlsplit(ref)
            if parsed.scheme or parsed.netloc: continue
            if parsed.path.startswith('/'):
                relative=unquote(parsed.path)
                prefix='/complymax-company-profile/'
                if relative.startswith(prefix): relative=relative[len(prefix):]
                target=(root/relative.lstrip('/')).resolve()
            else: target=(path.parent/unquote(parsed.path)).resolve() if parsed.path else path
            if target.is_dir(): target=target/'index.html'
            if not target.is_relative_to(root) or not target.is_file():
                errors.append(f'{path.relative_to(root)}: missing local resource {ref}')
            elif parsed.fragment and target in pages and unquote(parsed.fragment) not in pages[target].ids:
                errors.append(f'{path.relative_to(root)}: missing fragment {ref}')
    if errors:
        print('\n'.join(errors)); return 1
    print(f'PASS: {len(pages)} pages; local links, fragments, images, titles and headings checked.'); return 0

if __name__=='__main__': raise SystemExit(main())
