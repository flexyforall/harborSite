"""Builds the preview pages from original/index.html + new/approach-section.html.

new/index.html   - arc + blur card transition (default mode)
fade/index.html  - same section with data-apx-mode="fade": cards cross-fade in place
fade/approach-section.html - the fade variant on its own, for porting to Webflow
"""
import pathlib
root = pathlib.Path(__file__).resolve().parent.parent
page = (root / "original/index.html").read_text()
section = (root / "new/approach-section.html").read_text()
start = page.index('<section class="s-approach">')
end = page.index('<div class="scroll_text_wrap">', start)

def page_with(sec):
    return page[:start] + sec + page[end:]

(root / "new/index.html").write_text(page_with(section))

tag = '<section class="s-approach apx">'
assert section.count(tag) == 1
fade = section.replace(tag, '<section class="s-approach apx" data-apx-mode="fade">').replace("assets/", "../new/assets/")
(root / "fade").mkdir(exist_ok=True)
(root / "fade/approach-section.html").write_text(fade)
(root / "fade/index.html").write_text(page_with(fade))
print("ok")
