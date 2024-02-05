import openpyxl
from loguru import logger
import sys
import os


class Validate:
    """
    Validate checks given xlsx against given rules
    """

    def __init__(self) -> None:
        # Initialize logger with default settings
        self.logger = logger
        self.logger.remove()
        self.logger.add(
            sink="seiri-error.log",
            level="ERROR",
            format="<white>{time:MMMM D, YYYY > HH:mm:ss}</white> | <level>{level: <8}</level> | <level>Validate</level> | <level>{message}</level>",
        )
        self.logger.add(
            sink=sys.stdout,
            format="<white>{time:MMMM D, YYYY > HH:mm:ss}</white> | <level>{level: <8}</level> | <level>Validate</level> |  <level>{message}</level>",
        )

    def validate(self, in_xlsx: str, against_xlsx: str) -> bool:
        """
        Validate checks given xlsx against given rules
        """
        if not os.path.exists(in_xlsx):
            self.logger.error(f"Could not find {in_xlsx}")
            return False

        if not os.path.exists(against_xlsx):
            self.logger.error(f"Could not find {against_xlsx}")
            return False

        self.logger.success(f"Found {in_xlsx} and {against_xlsx}")
        self.logger.info(f"Validating {in_xlsx} against {against_xlsx}")

        in_wb = openpyxl.load_workbook(in_xlsx)
        self.logger.success(f"Loaded {in_xlsx}")

        against_wb = openpyxl.load_workbook(against_xlsx)
        self.logger.success(f"Loaded {against_xlsx}")

        # Check if both excel book row count is same in the en sheet
        self.logger.info(f"Checking row count against {against_xlsx} in en sheet")
        if in_wb["en"].max_row != against_wb["en"].max_row:
            self.logger.error("Row count mismatch in en sheet")
            return False
        else:
            self.logger.success("Row count match in en sheet")

        # Check if key and value order is same in the en sheet for both excel sheet "en"
        self.logger.info(
            f"Checking key and value order against {against_xlsx} in en sheet"
        )
        for row in range(1, in_wb["en"].max_row + 1):
            if (
                in_wb["en"].cell(row=row, column=1).value
                != against_wb["en"].cell(row=row, column=1).value
            ):
                self.logger.error(
                    f"Key mismatch in en sheet at row {row}. Expected: {against_wb['en'].cell(row=row, column=1).value}, Actual: {in_wb['en'].cell(row=row, column=1).value}"
                )
                return False
            if (
                in_wb["en"].cell(row=row, column=2).value
                != against_wb["en"].cell(row=row, column=2).value
            ):
                self.logger.error(
                    f"Value mismatch in en sheet at row {row}. Expected: {against_wb['en'].cell(row=row, column=2).value}, Actual: {in_wb['en'].cell(row=row, column=2).value}"
                )
                return False

        self.logger.success("Key and Value order match in en sheet")
        self.logger.success(f"Validation successful against {against_xlsx}")

        # Now onto checks only in the in_xlsx
        # Check if all sheets in the in_xlsx have same row count
        self.logger.info("Checking row count in all sheets")
        for sheet in in_wb.sheetnames:
            if in_wb[sheet].max_row != in_wb["en"].max_row:
                self.logger.error(f"Row count mismatch in {sheet} sheet")
                return False
            else:
                self.logger.success(f"Row count match in {sheet} sheet")

        # The “en” sheet key should be available in all other sheets
        self.logger.info("Checking if 'en' key is available in all sheets")
        for row in range(1, in_wb["en"].max_row + 1):
            key = in_wb["en"].cell(row=row, column=1).value
            # Check if this key is in all other sheets
            for sheet in in_wb.sheetnames:
                if sheet == "en":
                    continue
                if key not in in_wb[sheet].cell(row=row, column=1).value:
                    self.logger.error(
                        f"Mismatched value in {sheet} sheet at row {row}. Expected: {key}, Actual: {in_wb[sheet].cell(row=row, column=1).value}"
                    )
                    return False
        self.logger.success(
            "Key found in all sheets and the order is same across all sheets"
        )

        return True


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser()
    # get the first arg for in_xlsx without any flag
    ap.add_argument(
        "in_xlsx",
        type=str,
        default="tests/Delivered.xlsx",
        help="path to xlsx to validate",
    )
    ap.add_argument(
        "--against",
        type=str,
        default="tests/Sample.xlsx",
        help="path to xlsx to validate against",
    )
    args = vars(ap.parse_args())

    validate = Validate()
    validate.validate(args["in_xlsx"], args["against"])
