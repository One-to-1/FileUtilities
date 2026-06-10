"""Convert an XML file into an Excel (.xlsx) workbook."""
from pathlib import Path

import pandas as pd


def convert(input_path: Path, output_path: Path) -> None:
    """Read records from an XML file and write them to an XLSX workbook.

    Each repeated element under the XML root becomes a row, and its
    child elements/attributes become columns.
    """
    df = pd.read_xml(input_path)
    df.to_excel(output_path, index=False, engine="openpyxl")
