# FITS Utilities

These are utility scripts that will help find issues with FITS files.

## Requirements

Numpy and astropy are required. These are listed in the requirements.txt file. To install them, run

```
pip install -r requirements.txt 
```

or:

```
pip3 install -r requirements.txt
```

or possibly even:

```
python3 -m pip install -r requirements.txt
```

Unfortunately, I can't tell you which one you have to run on your specific system. Try them all.

## Usage

./infcheck.py (files)

### Example

```bash
user@pc fitsutils % ./infcheck.py ~/Desktop/*.fit
/Users/jessestone/Desktop/grs99177.fit::1: OK
/Users/jessestone/Desktop/occvis1048.fit::0: OK
/Users/jessestone/Desktop/xrs99034.fit::1: OK
```
