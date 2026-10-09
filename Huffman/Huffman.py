from Huffman.encoder import encode as _encode
from Huffman.decoder import decode as _decode


class Huffman:
    @classmethod
    def encode(cls, s, file_name=None):
        return _encode(s, file_name)

    @classmethod
    def decode(cls, s, from_file=False):
        return _decode(s, from_file)


def encode(s, file_name=None):
    return _encode(s, file_name)


def decode(s, from_file=False):
    return _decode(s, from_file)
