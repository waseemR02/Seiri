# Seiri
Tool for csv<->xlsx conversions and validation checks

## Installation
Create a virtual environment before installing dependencies
```
pip install -r requirements.txt
```

## Usage
This tool is written as library for future adaption to gui
But each class file can be run as a separate script
```
usage: transform.py [-h] [--cx CX] [-o OUTPUT] [--xc XC] [-v]

options:
  -h, --help            show this help message and exit
  --cx CX               Convert csv to xlsx
  -o OUTPUT, --output OUTPUT
                        output file
  --xc XC               Convert xlsx to csv
  -v, --verbose
```

**Example**

```
python seiri/transform.py --cx tests/Sample.csv -o sample.xlsx --verbose
```
![csv_to_xlsx](https://github.com/waseemR02/seiri/assets/98299006/c82f11f1-d3e1-4c41-9595-e06d6e2facd2)

### Testing
Run the following
```
pytest -v
```
![pytest](https://github.com/waseemR02/seiri/assets/98299006/330669ab-2197-4758-8efd-afe452c9616e)

## Task
- [x] Convert csv to xlsx
- [ ] Validating given Excel with rules
- [ ] Converting Excel to csv again
