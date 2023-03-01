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
/Users/user/Desktop/grs99177.fit: not an image
---------- /Users/jessestone/Desktop/occvis1048.fit ----------
    min/max 487 65535
    min/max without nans 487 65535
    +infs 0 []
    -infs 0 []
    nans 0 []
/Users/jessestone/Desktop/xrs99034.fit: not an image
```
