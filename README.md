# FileUtilities
Basic file converter between different file types

## Setup

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

## Usage

```bash
python convert.py input.xml output.xlsx
```

The converter is chosen based on the input/output file extensions.

## Supported conversions

- XML -> XLSX

## Adding a new converter

1. Create a module in `converters/` with a `convert(input_path, output_path)` function.
2. Register it in `converters/__init__.py`'s `REGISTRY` dict, keyed by
   `(input_format, output_format)`.
