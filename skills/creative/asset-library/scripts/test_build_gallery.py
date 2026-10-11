"""Verify file integrity and usable links in the portable gallery builder."""

import json
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote

from build_gallery import build_gallery


class PageLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.scripts = 0

    def handle_starttag(self, tag, attributes):
        if tag == "script":
            self.scripts += 1
        for name, value in attributes:
            if name in ("src", "href"):
                self.links.append(value)


class GalleryFiles(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "library"
        self.root.mkdir()
        self.asset = self.root / "leaf & stem.svg"
        self.asset.write_text('<svg xmlns="http://www.w3.org/2000/svg"/>', encoding="utf-8")
        self.manifest = self.root / "manifest.json"
        self.data = {"title": "Library", "assets": [
            {"id": "leaf", "title": "Leaf", "file": self.asset.name, "tags": ["plant"]}
        ]}

    def write_manifest(self):
        self.manifest.write_text(json.dumps(self.data), encoding="utf-8")

    def test_nested_gallery_has_resolving_links_and_preserves_assets(self):
        original = self.asset.read_bytes()
        self.data["title"] = "{{CARDS}} <script>not a script</script>"
        self.data["assets"][0]["title"] = '<img src="bad">'
        self.write_manifest()
        output = build_gallery(self.manifest, "preview/index.html")
        page = output.read_text(encoding="utf-8")
        links = PageLinks()
        links.feed(page)
        self.assertEqual(links.scripts, 1)
        self.assertIn("{{CARDS}} &lt;script&gt;", page)
        self.assertTrue(links.links)
        for link in links.links:
            self.assertTrue((output.parent / unquote(link)).is_file(), link)
        self.assertEqual(self.asset.read_bytes(), original)

    def test_duplicate_ids_do_not_write_partial_gallery(self):
        self.data["assets"].append(dict(self.data["assets"][0]))
        self.write_manifest()
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            build_gallery(self.manifest)
        self.assertFalse((self.root / "index.html").exists())

    def test_missing_file_does_not_write_gallery(self):
        self.data["assets"][0]["file"] = "missing.svg"
        self.write_manifest()
        with self.assertRaisesRegex(ValueError, "does not exist"):
            build_gallery(self.manifest)
        self.assertFalse((self.root / "index.html").exists())

    def test_input_paths_stay_inside_library(self):
        outside = self.root.parent / "outside.svg"
        outside.write_text("outside", encoding="utf-8")
        for value in ("../outside.svg", str(self.asset.resolve())):
            with self.subTest(value=value):
                self.data["assets"][0]["file"] = value
                self.write_manifest()
                with self.assertRaisesRegex(ValueError, "inside"):
                    build_gallery(self.manifest)

    def test_output_cannot_escape_or_overwrite_supporting_files(self):
        support = self.root / "contract.html"
        support.write_text("preserve contract", encoding="utf-8")
        self.data["art_contract"] = support.name
        self.write_manifest()
        for output in ("../escaped.html", "contract.html"):
            with self.subTest(output=output):
                with self.assertRaises(ValueError):
                    build_gallery(self.manifest, output)
        self.assertEqual(support.read_text(encoding="utf-8"), "preserve contract")
        self.assertFalse((self.root.parent / "escaped.html").exists())


if __name__ == "__main__":
    unittest.main()
