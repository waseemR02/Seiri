import csv
from seiri.transform import Transform


def test_xlsx_to_csv(tmp_path):
    # Create temporary input and output file paths
    input_file = "tests/data/Delivered_correct.xlsx"
    output_file = tmp_path / "output.csv"

    # Create a temporary log file path
    log_file = tmp_path / "seiri-error.log"

    # Create an instance of Transform
    transformer = Transform(log=str(log_file))

    # Call the xlsx_to_csv method
    transformer.xlsx_to_csv(str(input_file), str(output_file))

    # Check if the output file is created
    assert output_file.exists()

    # Read the contents of the output file
    with open(output_file, "r") as f:
        csv_reader = csv.reader(f, delimiter=";")
        rows = list(csv_reader)

    # Check against the csv file tests/data/Delivered.csv
    with open("tests/data/Delivered.csv", "r") as f:
        csv_reader = csv.reader(f, delimiter=";")
        expected_rows = list(csv_reader)

    # Check row by row
    for row, expected_row in zip(rows, expected_rows):
        assert row == expected_row

    assert log_file.exists()
