"""Rubikrypt: Sketchy crypto for messages of exactly 54 characters.
The message is printed on a Rubik's cube, which is scrambled in a manner described by the encryption key.

Usage:
    rubikrypt keygen <steps>
    rubikrypt encrypt <key> <message>
    rubikrypt decrypt <key> <message>
    rubikrypt -h | --help
    
Options:
    -h --help   Show this screen.
"""
import random

from rubik.cube import Cube, Piece, LEFT, RIGHT, UP, DOWN, FRONT, BACK
from docopt import docopt


class CryptoCube(Cube):
    def __init__(self, cube_str: str):
        # Override the base initializer for the Cube class, and skip the whitespace check

        assert len(cube_str) == 54
        self.faces = (
            Piece(pos=RIGHT, colors=(cube_str[28], None, None)),
            Piece(pos=LEFT, colors=(cube_str[22], None, None)),
            Piece(pos=UP, colors=(None, cube_str[4], None)),
            Piece(pos=DOWN, colors=(None, cube_str[49], None)),
            Piece(pos=FRONT, colors=(None, None, cube_str[25])),
            Piece(pos=BACK, colors=(None, None, cube_str[31])))
        self.edges = (
            Piece(pos=RIGHT + UP, colors=(cube_str[16], cube_str[5], None)),
            Piece(pos=RIGHT + DOWN, colors=(cube_str[40], cube_str[50], None)),
            Piece(pos=RIGHT + FRONT, colors=(cube_str[27], None, cube_str[26])),
            Piece(pos=RIGHT + BACK, colors=(cube_str[29], None, cube_str[30])),
            Piece(pos=LEFT + UP, colors=(cube_str[10], cube_str[3], None)),
            Piece(pos=LEFT + DOWN, colors=(cube_str[34], cube_str[48], None)),
            Piece(pos=LEFT + FRONT, colors=(cube_str[23], None, cube_str[24])),
            Piece(pos=LEFT + BACK, colors=(cube_str[21], None, cube_str[32])),
            Piece(pos=UP + FRONT, colors=(None, cube_str[7], cube_str[13])),
            Piece(pos=UP + BACK, colors=(None, cube_str[1], cube_str[19])),
            Piece(pos=DOWN + FRONT, colors=(None, cube_str[46], cube_str[37])),
            Piece(pos=DOWN + BACK, colors=(None, cube_str[52], cube_str[43])),
        )
        self.corners = (
            Piece(pos=RIGHT + UP + FRONT, colors=(cube_str[15], cube_str[8], cube_str[14])),
            Piece(pos=RIGHT + UP + BACK, colors=(cube_str[17], cube_str[2], cube_str[18])),
            Piece(pos=RIGHT + DOWN + FRONT, colors=(cube_str[39], cube_str[47], cube_str[38])),
            Piece(pos=RIGHT + DOWN + BACK, colors=(cube_str[41], cube_str[53], cube_str[42])),
            Piece(pos=LEFT + UP + FRONT, colors=(cube_str[11], cube_str[6], cube_str[12])),
            Piece(pos=LEFT + UP + BACK, colors=(cube_str[9], cube_str[0], cube_str[20])),
            Piece(pos=LEFT + DOWN + FRONT, colors=(cube_str[35], cube_str[45], cube_str[36])),
            Piece(pos=LEFT + DOWN + BACK, colors=(cube_str[33], cube_str[51], cube_str[44])),
        )

        self.pieces = self.faces + self.edges + self.corners

        self._assert_data()

    def sequence(self, move_str: str):
        for char in move_str:
            if char.islower():
                char = char.upper() + "i"

            getattr(self, char)()

    def __str__(self):
        return "".join(self._color_list())


def keygen(steps: int) -> str:
    # Possible Rubik's cube steps. Reverse ("prime") moves are denoted with a lowercase letter
    possible_steps = "UuDdRrLlFfBb"

    encryption_key = ""

    for _ in range(steps):
        step = random.choice(possible_steps)
        encryption_key += step

    return encryption_key


def main():
    args = docopt(__doc__)

    if args.get("keygen"):
        steps = int(args.get("<steps>"))
        encryption_key = keygen(steps)
        print(encryption_key)
    elif args.get("encrypt"):
        key: str = args.get("<key>")
        message: str = args.get("<message>")
        encrypted = encrypt(key, message)
        print(encrypted)
    elif args.get("decrypt"):
        key: str = args.get("<key>")
        message: str = args.get("<message>")
        decrypted = decrypt(key, message)
        print(decrypted)


def decrypt(key: str, message: str) -> str:
    cube = CryptoCube(message)
    cube.sequence(key.swapcase()[::-1])
    return str(cube)


def encrypt(key: str, message: str) -> str:
    cube = CryptoCube(message)
    cube.sequence(key)
    return str(cube)


if __name__ == "__main__":
    main()
