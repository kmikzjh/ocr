from __future__ import annotations

import argparse
import sys

from .core import extract_text


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ocr-reader",
        description="Lee texto desde imágenes usando Tesseract OCR.",
    )
    parser.add_argument("image", help="Ruta a la imagen a procesar")
    parser.add_argument(
        "-l",
        "--lang",
        default="eng",
        help="Código de idioma de Tesseract (default: eng)",
    )
    parser.add_argument(
        "--config",
        default=None,
        help="Configuración adicional para Tesseract",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        text = extract_text(args.image, lang=args.lang, config=args.config)
    except Exception as exc:  # pragma: no cover - CLI path
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if text:
        print(text)
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry
    raise SystemExit(main())
