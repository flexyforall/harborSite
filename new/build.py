"""Builds new/index.html = original/index.html with the approach section replaced by new/approach-section.html."""
import pathlib, re
root = pathlib.Path(__file__).resolve().parent.parent
page = (root / "original/index.html").read_text()
section = (root / "new/approach-section.html").read_text()
start = page.index('<section class="s-approach">')
end = page.index('<div class="scroll_text_wrap">', start)
out = page[:start] + section + page[end:]
# assets in original are absolute; our section uses paths relative to /new/
(root / "new/index.html").write_text(out)
print("ok", len(out))
