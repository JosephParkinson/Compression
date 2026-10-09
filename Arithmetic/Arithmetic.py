from Arithmetic.encoder import encode as _encode
from Arithmetic.decoder import decode as _decode


class Arithmetic:
    @classmethod
    def encode(cls, text):
        return _encode(text)

    @classmethod
    def decode(cls, encoded):
        return _decode(encoded)


def encode(text):
    return _encode(text)


def decode(encoded):
    return _decode(encoded)
