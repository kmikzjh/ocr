from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from ocr_reader import core


class DummyImage:
    def __init__(self, path: Path):
        self.path = path

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False


class TestCore(unittest.TestCase):
    def test_extract_text_returns_stripped_text(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            image_file = Path(tmpdir) / "sample.png"
            image_file.write_bytes(b"fake")

            def fake_open(path):
                return DummyImage(path)

            def fake_image_to_string(image, lang="eng", config=""):
                self.assertEqual(image.path, image_file)
                self.assertEqual(lang, "spa")
                self.assertEqual(config, "--psm 6")
                return "  Hola mundo  \n"

            with patch.object(core, "Image", type("PIL", (), {"open": staticmethod(fake_open)})):
                with patch.object(
                    core,
                    "pytesseract",
                    type("T", (), {"image_to_string": staticmethod(fake_image_to_string)}),
                ):
                    result = core.extract_text(image_file, lang="spa", config="--psm 6")

            self.assertEqual(result, "Hola mundo")

    def test_extract_text_raises_for_missing_image(self):
        with patch.object(core, "Image", object()):
            with patch.object(core, "pytesseract", object()):
                with self.assertRaises(FileNotFoundError):
                    core.extract_text("does-not-exist.png")


if __name__ == "__main__":
    unittest.main()
