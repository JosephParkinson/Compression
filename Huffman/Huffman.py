from Huffman.encoder import encode
from Huffman.decoder import decode


class Huffman:
    @classmethod
    def _encode(s, file_name=None):
        return encode(s, file_name)

    @classmethod
    def _decode(s, from_file=None):
        return decode(s, from_file)
