from __future__ import annotations

from pathlib import Path
from typing import Optional

try:
    from PIL import Image
except ImportError:  # pragma: no cover - dependency may be absent in some envs
    Image = None  # type: ignore[assignment]

try:
    import pytesseract
except ImportError:  # pragma: no cover - dependency may be absent in some envs
    pytesseract = None  # type: ignore[assignment]


def _require_dependencies() -> None:
    missing = []
    if Image is None:
        missing.append("Pillow")
    if pytesseract is None:
        missing.append("pytesseract")

    if missing:
        raise RuntimeError(
            "Faltan dependencias de Python: " + ", ".join(missing) + ". "
            "Instala requirements.txt antes de usar el OCR."
        )


def extract_text(image_path: str | Path, lang: str = "eng", config: Optional[str] = None) -> str:
    """
    Extract text from an image using Tesseract OCR.

    Parameters
    ----------
    image_path:
        Path to the image file.
    lang:
        Tesseract language code. Default: "eng".
    config:
        Optional extra Tesseract configuration string.
    """

    _require_dependencies()

    path = Path(image_path)
    if not path.exists():
        raise FileNotFoundError(f"No existe la imagen: {path}")
    if not path.is_file():
        raise IsADirectoryError(f"La ruta no es un archivo: {path}")

    with Image.open(path) as image:  # type: ignore[union-attr]
        text = pytesseract.image_to_string(  # type: ignore[union-attr]
            image,
            lang=lang,
            config=config or "",
        )
    return text.strip()
