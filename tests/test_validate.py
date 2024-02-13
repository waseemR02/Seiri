from seiri.validate import Validate


def test_validate_correct(tmp_path):
    input_file = "tests/data/Delivered_correct.xlsx"
    against_file = "tests/data/Sample.xlsx"

    # Create a temporary log file path
    log_file = tmp_path / "seiri-error.log"

    # Create an instance of Validate
    validator = Validate(str(log_file))

    # Call the validate method with correct xlsx files
    result = validator.validate(str(input_file), str(against_file))

    # Check if the validation is successful
    assert result is True

    # Check if the log file is created
    assert log_file.exists()


def test_validate_incorrect(tmp_path):
    input_file = "tests/data/Delivered_incorrect.xlsx"
    against_file = "tests/data/Sample.xlsx"

    # Create a temporary log file path
    log_file = tmp_path / "seiri-error.log"

    # Create an instance of Validate
    validator = Validate(str(log_file))

    # Call the validate method with correct xlsx files
    result = validator.validate(str(input_file), str(against_file))

    # Check if the validation is successful
    assert result is False

    # Check if the log file is created
    assert log_file.exists()

    # Check if the contents are similar to the expected log file in tests/sample_log_validate.log
    # But ignore the date and time
    # Sample
    # | ERROR    | Validate | Row count mismatch in de sheet
    # | ERROR    | Validate | Mismatched value in it sheet at row 6. Expected: lbl_Reserved, Actual: label_Expert_List
    # | ERROR    | Validate | Empty cell in de sheet at row 7
    # | ERROR    | Validate | Mismatched value in it sheet at row 7. Expected: label_Expert_List, Actual: lbl_Reserved
    # | ERROR    | Validate | Duplicate value 'df' found in de sheet

    with open(log_file, "r") as f:
        log_contents = f.readlines()
        assert len(log_contents) == 5
        assert "Row count mismatch in de sheet" in log_contents[0]
        assert (
            "Mismatched value in it sheet at row 6. Expected: lbl_Reserved, Actual: label_Expert_List"
            in log_contents[1]
        )
        assert "Empty cell in de sheet at row 7" in log_contents[2]
        assert (
            "Mismatched value in it sheet at row 7. Expected: label_Expert_List, Actual: lbl_Reserved"
            in log_contents[3]
        )
        assert "Duplicate value 'df' found in de sheet" in log_contents[4]
