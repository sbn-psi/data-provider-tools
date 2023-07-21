#!/usr/bin/env python3
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


def build_parser(bits: int):
    def parse(value: bytes, endianness: str):
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

    def multiparse(value: bytes):
        return {
            'msb': parse(value, '>'),
            'lsb': parse(value, '<')
        }

    return multiparse


def main():
    bits = 16
    value = b'\x7F\xFB'
    parser = build_parser(bits)

    print(parser(value))


if __name__ == '__main__':
    sys.exit(main())
