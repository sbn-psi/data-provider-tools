#!/usr/bin/env python3
import argparse
import sys
import struct
from typing import Iterator, Tuple

ENDIANNESS = ('<', '>')
SIZES = {
    8: ('b', 'B'),
    16: ('h', 'H'),
    32: ('i', 'I'),
    64: ('q', 'Q')
}


def parse(bits: int, value: bytes, endianness: str):
    offset = 2**(bits - 1)

    signed_f, unsigned_f = SIZES[bits]

    signed_v = struct.unpack(f'{endianness}{signed_f}', value)[0]
    unsigned_v = struct.unpack(f'{endianness}{unsigned_f}', value)[0]
    signed_to_unsigned_v = signed_v + offset
    unsigned_to_signed_v = unsigned_v - offset

    return {
        'offset': offset,
        'signed': signed_v,
        'unsigned': unsigned_v,
        'signed_to_unsigned': signed_to_unsigned_v,
        'unsigned_to_signed': unsigned_to_signed_v
    }


def multiparse(bits: int, value: bytes):
    return {
        'msb': parse(bits, value, '>'),
        'lsb': parse(bits, value, '<')
    }


def parse_file(fits_file, data_offset, records, record_length, field_position, field_size):
    bits = field_size * 8

    with open(fits_file, 'rb') as f:
        f.read(data_offset)
        for _ in range(0, records):
            record = f.read(record_length)
            value = record[field_position-1:field_position+field_size-1]
            print(multiparse(bits, value))


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--field_length", type=int,
                        help="The size of the field to check, in bytes", required=True)
    parser.add_argument("--field_location", type=int, help="The 1-based location of the field within the record", required=True)
    parser.add_argument("--offset", type=int, help="The 0-based start byte of the data table", required=True)
    parser.add_argument("--record_length", type=int, help="The length of each data record, in bytes", required=True)
    parser.add_argument("--records", type=int, help="The number of records to read", required=True)

    parser.add_argument("fits_file")

    args = parser.parse_args()

    parse_file(args.fits_file, args.offset, args.records, args.record_length, args.field_location, args.field_length)

    return 0


if __name__ == '__main__':
    sys.exit(main())
