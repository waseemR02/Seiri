# Seiri
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/2543d30ee224499a91a09b5c04b10454)](https://app.codacy.com/gh/waseemR02/seiri/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

Tool for csv<->xlsx conversions and validation checks

## Installation
Create a virtual environment before installing dependencies
```
pip install -r requirements.txt
```

## Usage
This tool is written as library for future adaptation to gui

But each class file can be run as a separate script
**Transform**
```
usage: transform.py [-h] [--cx CX] [-o OUTPUT] [--xc XC] [--log LOG] [-v]

options:
  -h, --help            show this help message and exit
  --cx CX               Convert csv to xlsx
  -o OUTPUT, --output OUTPUT
                        output file
  --xc XC               Convert xlsx to csv
  --log LOG             path to log file
  -v, --verbose
```

**Validate**
```
usage: validate.py [-h] [--against AGAINST] [--log LOG] in_xlsx

positional arguments:
  in_xlsx            path to xlsx to validate

options:
  -h, --help         show this help message and exit
  --against AGAINST  path to xlsx to validate against
  --log LOG          path to log file
```
**Example:**

```
python -m seiri.transform --cx tests/data/Sample.csv -o sample.xlsx --verbose
```
![csv_to_xlsx](https://github.com/waseemR02/seiri/assets/98299006/2443b91d-643e-4a5e-bae5-85eeb2abea94)
-----------------
```
python -m seiri.validate tests/data/Delivered_correct.xlsx
```
![validation](https://github.com/waseemR02/seiri/assets/98299006/e47adcf2-cc07-4379-ba20-72016fc1fed3)
```
python -m seiri.transform --xc tests/data/Delivered_correct.xlsx -o sample.csv  --verbose
```
![xlsx_to_csv](https://github.com/waseemR02/seiri/assets/98299006/00f1b512-02c2-46f8-8240-161ff2485041)

### Testing
Run the following
```
pytest -v
```
![pytest](https://github.com/waseemR02/seiri/assets/98299006/ff25e827-3550-4be3-86e0-4ca0ca470a70)

## Task
- [x] Convert csv to xlsx
- [x] Validating given Excel with rules
- [x] Converting Excel to csv again
- [x] Add Spell check on `en` column
