import csv
from openpyxl import Workbook
from loguru import logger
import sys

class Transform:
    """ 
        Transform contains methods for converting
            1. csv  --> xlsx
            2. xlsx --> csv
    """
    def __init__(self, verbose: bool = False) -> None:
       
        # Initialize logger for default logging
        self.logger = logger
        self.logger.remove()
        self.logger.add("seiri.log", level="ERROR")

        if verbose:
            self.logger.add(sys.stderr, level="DEBUG")
            
        # Intialize worksheets
        self.wb = Workbook()
        del self.wb["Sheet"]
        
        # default langs for now
        self.lang = ["en", "en", "es", "fr", "it"]

    def csv_to_xlsx(self, in_file: str, out_file: str) -> None:
        Listed_csv= csv.reader(open(in_file, "r"), delimiter=';')
        
        # Checks 
        for row in Listed_csv:
            self.logger.info(row[2] if len(row) == 10 else "")


if __name__ == "__main__":
    import argparse
    import json

    ap = argparse.ArgumentParser()
    ap.add_argument("--cx", type=str,
                    help="Convert csv to xlsx")
    ap.add_argument("-o", "--output", required=False,type=str, help="output file")
    ap.add_argument("--xc", type=str, default="tests/Sample.xlsx",
                    help="Convert xlsx to csv")
    ap.add_argument("-v", "--verbose", action="store_true")

    args = vars(ap.parse_args())

    transformer = Transform(verbose=args["verbose"])

    if args["cx"]:
    # csv to xlsx
        output = args["cx"][:-3] + "xlsx" if not args["output"] else args["output"]
        input = args["cx"]

        transformer.csv_to_xlsx(input, output)

