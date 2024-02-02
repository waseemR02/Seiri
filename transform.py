import csv

class Transform:
    """ 
        Transform contains methods for converting
            1. csv  --> xlsx
            2. xlsx --> csv
    """
    def __init__(self) -> None:
        pass

    def csv_to_xlsx(self, in_file: str, out_file: str) -> None:
        Listed_dic= list(csv.DictReader(open(in_file, 'r')))
        print(json.dumps(Listed_dic, indent=4))


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

