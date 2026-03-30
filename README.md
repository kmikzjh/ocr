# OCR Reader con Tesseract

Mini proyecto en Python para extraer texto desde imágenes usando **Tesseract OCR**.

## Requisitos

- Python 3.10+
- Tesseract OCR instalado en el sistema
- Dependencias de Python instaladas con `requirements.txt`

## Instalación

1. Instala Tesseract en tu sistema.
   - macOS: `brew install tesseract`
   - Ubuntu/Debian: `sudo apt-get install tesseract-ocr`
   - Windows: instala el binario de Tesseract y asegúrate de que esté en el PATH

2. Instala las dependencias de Python:

```bash
pip install -r requirements.txt
```

## Uso

Ejecuta el CLI pasando la ruta de una imagen:

```bash
python app.py ruta/a/imagen.png
```

Opcionalmente puedes indicar el idioma:

```bash
python app.py ruta/a/imagen.png --lang spa
```

También puedes pasar configuración adicional de Tesseract:

```bash
python app.py ruta/a/imagen.png --config "--psm 6"
```

## Estructura

- `app.py` — punto de entrada simple para la línea de comandos
- `ocr_reader/core.py` — lógica de extracción de texto
- `ocr_reader/cli.py` — interfaz CLI
- `tests/` — pruebas unitarias con mocks

## Limitaciones

- Tesseract debe estar instalado aparte; `pytesseract` solo actúa como wrapper de Python.
- La precisión depende de la calidad de la imagen, contraste, resolución e idioma seleccionado.
