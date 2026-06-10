"""Convert a JSON file into an Excel (.xlsx) workbook."""
import json
from pathlib import Path

import pandas as pd


def convert(input_path: Path, output_path: Path) -> None:
    """Read records from a JSON file and write them to an XLSX workbook.

    Accepts a top-level list of records, a single record object, or an
    API-style response shaped like ``{"count": N, "value": [...]}``.
    Nested objects are flattened into dotted column names; nested lists
    are kept as JSON strings so no data is lost.
    """
    with open(input_path, encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict) and isinstance(data.get("value"), list):
        records = data["value"]
    elif isinstance(data, list):
        records = data
    else:
        records = [data]

    df = pd.json_normalize(records)

    for column in df.columns:
        df[column] = df[column].apply(
            lambda value: json.dumps(value) if isinstance(value, (list, dict)) else value
        )

    df.to_excel(output_path, index=False, engine="openpyxl")
