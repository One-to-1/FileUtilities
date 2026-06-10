"""Registry of available file format converters."""
from .json_to_xlsx import convert as json_to_xlsx
from .xml_to_xlsx import convert as xml_to_xlsx

REGISTRY = {
    ("xml", "xlsx"): xml_to_xlsx,
    ("json", "xlsx"): json_to_xlsx,
}


def get_converter(input_format: str, output_format: str):
    """Return the converter function for the given format pair, or None."""
    return REGISTRY.get((input_format.lower(), output_format.lower()))


def supported_conversions():
    """Return a list of supported (input_format, output_format) pairs."""
    return list(REGISTRY.keys())
