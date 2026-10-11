#!/usr/bin/env python3
"""Build a searchable local asset gallery from a portable JSON manifest."""

import argparse
import html
import json
import re
from pathlib import Path
from urllib.parse import quote


IMAGE_EXTENSIONS = {".svg", ".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif"}
VIDEO_EXTENSIONS = {".mp4", ".webm"}


def read_library_file(root, value, field):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be a nonempty relative file path")
    relative = Path(value.replace("\\", "/"))
    path = (root / relative).resolve()
    if relative.is_absolute() or not path.is_relative_to(root):
        raise ValueError(f"{field} must stay inside the library directory")
    if not path.is_file():
        raise ValueError(f"{field} file does not exist: {value}")
    return path


def require_text(value, field):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be nonempty text")
    return value


def file_url(path, output):
    # Both paths are inside the library; relpath preserves links from nested galleries.
    import os

    return quote(Path(os.path.relpath(path, output.parent)).as_posix(), safe="/")


def build_gallery(manifest, output_name="index.html"):
    manifest = Path(manifest).resolve()
    root = manifest.parent
    data = json.loads(manifest.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict) or not isinstance(data.get("assets"), list):
        raise ValueError("Manifest must contain an assets array")
    title = require_text(data.get("title", "Asset library"), "title")
    output_relative = Path(output_name.replace("\\", "/"))
    output = (root / output_relative).resolve()
    if output_relative.is_absolute() or not output.is_relative_to(root):
        raise ValueError("Output must stay inside the library directory")
    if output.suffix.lower() != ".html":
        raise ValueError("Output must be an HTML file")
    if output == manifest:
        raise ValueError("Output cannot replace the manifest")

    files_used = {manifest}
    contract = None
    if "art_contract" in data:
        contract = read_library_file(root, data["art_contract"], "art_contract")
        files_used.add(contract)
    cards = []
    identifiers = set()
    for index, asset in enumerate(data["assets"]):
        if not isinstance(asset, dict):
            raise ValueError(f"Asset {index} must be an object")
        identifier = require_text(asset.get("id"), f"Asset {index} id")
        if identifier in identifiers:
            raise ValueError(f"Duplicate asset id: {identifier}")
        identifiers.add(identifier)
        name = require_text(asset.get("title"), f"Asset {identifier} title")
        asset_files = {"file": read_library_file(root, asset.get("file"), f"{identifier} file")}
        for field in ("preview", "source", "prompt", "reference"):
            if field in asset:
                asset_files[field] = read_library_file(root, asset[field], f"{identifier} {field}")
        files_used.update(asset_files.values())
        kind = require_text(asset.get("kind", "asset"), f"{identifier} kind")
        status = require_text(asset.get("status", "draft"), f"{identifier} status")
        tags = asset.get("tags", [])
        if not isinstance(tags, list) or any(not isinstance(tag, str) for tag in tags):
            raise ValueError(f"{identifier} tags must be an array of strings")
        search = html.escape(" ".join([identifier, name, kind, status, *tags]).lower(), quote=True)
        preview = asset_files.get("preview", asset_files["file"])
        preview_url = html.escape(file_url(preview, output), quote=True)
        escaped_name = html.escape(name, quote=True)
        if preview.suffix.lower() in IMAGE_EXTENSIONS:
            media = f'<img src="{preview_url}" alt="{escaped_name}" loading="lazy">'
        elif preview.suffix.lower() in VIDEO_EXTENSIONS:
            media = f'<video src="{preview_url}" controls preload="metadata" aria-label="{escaped_name}"></video>'
        else:
            media = '<span class="no-preview">Open file to inspect</span>'
        links = []
        for field in ("file", "source", "prompt", "reference"):
            if field in asset_files:
                url = html.escape(file_url(asset_files[field], output), quote=True)
                label = {"file": "Download asset", "source": "Source", "prompt": "Prompt", "reference": "Reference"}[field]
                download = " download" if field == "file" else ""
                links.append(f'<a href="{url}"{download}>{label}</a>')
        cards.append(f'<article data-search="{search}"><div class="preview">{media}</div>'
                     f'<h2>{escaped_name}</h2><p>{html.escape(kind)} · {html.escape(status)}</p>'
                     f'<p class="tags">{html.escape(", ".join(tags))}</p><nav>{" ".join(links)}</nav></article>')
    if output in files_used:
        raise ValueError("Output cannot replace a library asset or supporting file")
    contract_link = ""
    if contract:
        contract_link = f'<a href="{html.escape(file_url(contract, output), quote=True)}">Art contract</a>'
    replacements = {
        "TITLE": html.escape(title), "CONTRACT": contract_link,
        "COUNT": str(len(cards)), "CARDS": "\n".join(cards),
        "EMPTY_HIDDEN": "hidden" if cards else "",
    }
    page = re.sub(r"\{\{(TITLE|CONTRACT|COUNT|CARDS|EMPTY_HIDDEN)\}\}",
                  lambda match: replacements[match.group(1)], PAGE)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(page, encoding="utf-8")
    return output


PAGE = """<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{TITLE}}</title><style>
*{box-sizing:border-box}body{margin:0;background:#f6f4ef;color:#20242b;font:16px/1.5 system-ui,sans-serif}
header,main{max-width:1200px;margin:auto;padding:24px}h1{margin:0 0 8px;font-size:clamp(26px,4vw,42px)}
label{display:block;margin-top:20px}input{display:block;width:100%;max-width:560px;padding:12px;font:inherit;border:1px solid #81858d;border-radius:8px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,250px),1fr));gap:20px}
article{min-width:0;padding:16px;background:white;border:1px solid #d7d9de;border-radius:12px}article[hidden]{display:none}
.preview{height:210px;display:grid;place-items:center;border-radius:8px;background-color:#f0f0f0;background-image:linear-gradient(45deg,#ddd 25%,transparent 25%),linear-gradient(-45deg,#ddd 25%,transparent 25%),linear-gradient(45deg,transparent 75%,#ddd 75%),linear-gradient(-45deg,transparent 75%,#ddd 75%);background-size:20px 20px;background-position:0 0,0 10px,10px -10px,-10px 0}
img,video{display:block;max-width:100%;max-height:210px;object-fit:contain}h2{font-size:18px;margin:12px 0 4px}p{margin:4px 0}.tags{color:#555;overflow-wrap:anywhere}
nav{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}a{color:#254e99;text-underline-offset:3px}.no-preview{background:white;padding:8px}
:focus-visible{outline:3px solid #c56519;outline-offset:3px}
</style><header><h1>{{TITLE}}</h1>{{CONTRACT}}<p id="count" aria-live="polite">{{COUNT}} assets</p>
<label for="search">Search names, tags, kind, or review state</label><input id="search" type="search"></header>
<main><div class="grid">{{CARDS}}</div><p id="empty" {{EMPTY_HIDDEN}}>No assets match this search.</p></main>
<script>
const cards=[...document.querySelectorAll('article')];
document.querySelector('#search').addEventListener('input',event=>{
const query=event.target.value.trim().toLowerCase();let count=0;
for(const card of cards){card.hidden=!card.dataset.search.includes(query);if(!card.hidden)count++;}
document.querySelector('#count').textContent=`${count} of ${cards.length} assets`;
document.querySelector('#empty').hidden=count!==0;
});
</script></html>"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--output", default="index.html", help="HTML path relative to the library directory")
    arguments = parser.parse_args()
    try:
        output = build_gallery(arguments.manifest, arguments.output)
    except (ValueError, OSError) as error:
        parser.error(str(error))
    print(output)


if __name__ == "__main__":
    main()
