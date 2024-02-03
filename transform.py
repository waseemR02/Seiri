import csv
from openpyxl import Workbook
from openpyxl.styles import Alignment
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
        self.sheets= []
        del self.wb["Sheet"]
        
        # default langs for now
        self.langs = ["en", "de", "es", "fr", "it"]

    def __init__sheets(self) -> None:
        # Create worksheets
        for lang in self.langs:
            self.sheets.append(self.wb.create_sheet(lang))
            self.logger.info(f"Created sheet {lang}")
        
        for sheet in self.sheets:
            sheet.append(["Key", "Value"])
        
        self.logger.info("Successfully initialized Sheets")

    def csv_to_xlsx(self, in_file: str, out_file: str) -> None:

        Listed_csv= csv.reader(open(in_file, "r", newline=''), delimiter=';')
        
        # Checks 
        header_list = Listed_csv.__next__()
        
        if header_list[4] != "en":
            self.logger.error("'en' Spell check error!!")
        else:
            self.logger.info("'en' Spell check done")

        self.__init__sheets()

        # for row in Listed_csv:
        #     # print(row)
        #     print(row if len(row) == 10 else "")


        # Save Workbook
        self.wb.save(out_file)
        self.logger.info(f"Saving workbook to {out_file}")


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

