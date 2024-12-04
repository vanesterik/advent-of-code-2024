from enum import Enum
from typing import List, TextIO

import click
import polars as pl

Column = Enum("Column", {"LEFT": "left", "RIGHT": "right"})


@click.command()
@click.argument(
    "input_file", default="./data/raw/day-01.txt", type=click.File("r")
)
def main(input_file: TextIO) -> None:

    # Read input data to list of strings
    data = input_file.readlines()

    # Extract and sort columns
    left = extract_column(data, Column.LEFT)
    right = extract_column(data, Column.RIGHT)

    # Create DataFrame based on extracted columns
    df = pl.DataFrame(
        {
            Column.LEFT.value: left,
            Column.RIGHT.value: right,
        }
    )

    # Write processed data to CSV
    df.write_csv("./data/processed/day-01.csv")


def extract_column(data: List[str], side: Column) -> List[str]:

    # Define list index based on side
    index = 0 if side == Column.LEFT else 1

    # Extract column based on index
    column = [row.split()[index] for row in data]

    # Sort and return column
    return sorted(column)


if __name__ == "__main__":
    main()
