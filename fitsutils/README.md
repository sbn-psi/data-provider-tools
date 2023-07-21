# FITS Utilities

These are utility scripts that will help find issues with FITS files.

## Requirements

Numpy and astropy are required for infcheck. These are listed in the requirements.txt file. To install them, run

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

## Infcheck Usage

./infcheck.py (files)

### Example

```bash
user@pc fitsutils % ./infcheck.py ~/Desktop/*.fit
/Users/jessestone/Desktop/grs99177.fit::1: OK
/Users/jessestone/Desktop/occvis1048.fit::0: OK
/Users/jessestone/Desktop/xrs99034.fit::1: OK
```

## Intparse Usage

```bash
usage: intparse.py [-h] --field_length FIELD_LENGTH --field_location FIELD_LOCATION --offset OFFSET --record_length RECORD_LENGTH --records RECORDS fits_file
```

```
positional arguments:
  fits_file

options:
  -h, --help            show this help message and exit
  --field_length FIELD_LENGTH
                        The size of the field to check, in bytes
  --field_location FIELD_LOCATION
                        The 1-based location of the field within the record
  --offset OFFSET       The 0-based start byte of the data table
  --record_length RECORD_LENGTH
                        The length of each data record, in bytes
  --records RECORDS     The number of records to read
```
### Example


```bash
./intparse.py --field_length 2 --field_location 63 --offset 54720 --record_length 10560 --records 32 /path/to/grf99101.fit
```

```python
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32763, 'unsigned': 32763, 'signed_to_unsigned': 65531, 'unsigned_to_signed': -5}, 'lsb': {'offset': 32768, 'signed': -1153, 'unsigned': 64383, 'signed_to_unsigned': 31615, 'unsigned_to_signed': 31615}}
{'msb': {'offset': 32768, 'signed': 32767, 'unsigned': 32767, 'signed_to_unsigned': 65535, 'unsigned_to_signed': -1}, 'lsb': {'offset': 32768, 'signed': -129, 'unsigned': 65407, 'signed_to_unsigned': 32639, 'unsigned_to_signed': 32639}}
```