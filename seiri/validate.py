from loguru import logger
import sys


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
            format="<white>{time:MMMM D, YYYY > HH:mm:ss}</white> | <level>{level: <8}</level> | <level>{message}</level>",
        )
        self.logger.add(
            sink=sys.stdout,
            format="<white>{time:MMMM D, YYYY > HH:mm:ss}</white> | <level>{level: <8}</level> | <level>{message}</level>",
        )

    def validate(self, in_xlsx: str, against_xlsx) -> bool:
        """
        Validate checks given xlsx against given rules
        """
        return True


if __name__ == "__main__":
    validate = Validate()
    validate.validate("test.xlsx", "test_rules.xlsx")
