import csv
from openpyxl import Workbook
from loguru import logger

class Transform:
    """ 
        Transform contains methods for converting
            1. csv  --> xlsx
            2. xlsx --> csv
    """
    def __init__(self) -> None:
       # Initialize logger

        self.logger = logger
        self.logger.add("seiri.log", level="ERROR")


        # Intialize worksheets
        self.wb = Workbook()
        del self.wb["Sheet"]
        
        # default langs for now
        self.lang = ["en", "en", "es", "fr", "it"]

    def csv_to_xlsx(self, in_file: str, out_file: str) -> None:
        Listed_csv= csv.reader(open(in_file, "r"), delimiter=';')
        
        # Checks 
        for row in Listed_csv:
            logger.info(row[2] if len(row) == 10 else "")


if __name__ == "__main__":
    import argparse
    import json

    ap = argparse.ArgumentParser()
    ap.add_argument("--cx", type=str,
                    help="Convert csv to xlsx")
    ap.add_argument("-o", "--output", required=False,type=str, help="output file")
    ap.add_argument("--xc", type=str, default="tests/Sample.xlsx",
                    help="Convert xlsx to csv")

    args = vars(ap.parse_args())

    transformer = Transform()

    if args["cx"]:
    # csv to xlsx
        output = args["cx"][:-3] + "xlsx" if not args["output"] else args["output"]
        input = args["cx"]

        transformer.csv_to_xlsx(input, output)

