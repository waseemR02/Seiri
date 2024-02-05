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

        self.logger.info(f"Found {in_xlsx} and {against_xlsx}")
        self.logger.info(f"Validating {in_xlsx} against {against_xlsx}")

        return True


if __name__ == "__main__":
    validate = Validate()
    validate.validate("test.xlsx", "test_rules.xlsx")
