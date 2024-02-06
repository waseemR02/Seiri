# Seiri
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
usage: transform.py [-h] [--cx CX] [-o OUTPUT] [--xc XC] [-v]

options:
  -h, --help            show this help message and exit
  --cx CX               Convert csv to xlsx
  -o OUTPUT, --output OUTPUT
                        output file
  --xc XC               Convert xlsx to csv
  -v, --verbose
```

**Validate**
```
usage: validate.py [-h] [--against AGAINST] in_xlsx

positional arguments:
  in_xlsx            path to xlsx to validate

options:
  -h, --help         show this help message and exit
  --against AGAINST  path to xlsx to validate against
```

**Example:**

```
python seiri/transform.py --cx tests/Sample.csv -o sample.xlsx --verbose
```
![csv_to_xlsx](https://github.com/waseemR02/seiri/assets/98299006/2443b91d-643e-4a5e-bae5-85eeb2abea94)
-----------------
```
python seiri/validate.py tests/Delivered_correct.xlsx
```
![validation](https://github.com/waseemR02/seiri/assets/98299006/e47adcf2-cc07-4379-ba20-72016fc1fed3)

### Testing
Run the following
```
pytest -v
```
![pytest](https://github.com/waseemR02/seiri/assets/98299006/330669ab-2197-4758-8efd-afe452c9616e)

## Task
- [x] Convert csv to xlsx
- [x] Validating given Excel with rules
- [ ] Converting Excel to csv again
