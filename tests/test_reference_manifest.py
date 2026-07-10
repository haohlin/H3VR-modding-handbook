import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "references" / "manifest.json"


class ReferenceManifestTests(unittest.TestCase):
    def load_sources(self):
        return json.loads(MANIFEST.read_text(encoding="utf-8"))["submodules"]

    def test_manifest_has_27_unique_sources(self):
        sources = self.load_sources()
        self.assertEqual(27, len(sources))
        self.assertEqual(27, len({item["path"] for item in sources}))
        self.assertEqual(27, len({item["url"] for item in sources}))

    def test_manifest_contains_required_special_sources(self):
        sources = {item["path"]: item for item in self.load_sources()}
        self.assertEqual(
            "SRE-1.3.0",
            sources["references/Packer/H3VR-Supply-Raid-SRE-1.3.0"]["requestedRef"],
        )
        for path in (
            "references/H3VR-Modding/OtherLoader",
            "references/devyndamonster/OtherLoader",
            "references/KacperObara/H3VR-GunGame.wiki",
            "references/Nolenz/WurstMod",
            "references/Josh015/Alloy",
        ):
            self.assertIn(path, sources)


if __name__ == "__main__":
    unittest.main()

