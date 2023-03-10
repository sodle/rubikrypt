# Rubikrypt: Crappy crypto for messages of exactly 54 characters.
The message is printed on a Rubik's cube, which is scrambled in a manner described by the encryption key.

```
Usage:
    rubikrypt keygen <steps>
    rubikrypt encrypt <key> <message>
    rubikrypt decrypt <key> <message>
    rubikrypt -h | --help
    
Options:
    -h --help   Show this screen.
```

# Requirements
- Python 3.10
- Poetry

## Dependencies installed by Poetry
- [docopt](https://github.com/docopt/docopt) for CLI argument parsing
- [cube](https://github.com/pglass/cube) by Paul Glass, which I have subclassed for easy manipulation of a Rubik's cube data structure

# Install it
```bash
poetry install
```

# Generate a key
For an encryption key that alters the cube 100 times,
```bash
rubikrypt keygen 100
```

Keys look like this:
```
DbffLFrbBuDdRbbLUuLuDFuulDUbFlluLurrdDUbddrbrrbdDLuruBRUlFdDFluLFbudFrudLLuuBuBBRLflbllLRLbrFFrdDrrR
```
Each byte corresponds to a [face turn](https://jperm.net/3x3/moves) on a Rubik's cube.
Lowercase letters indicate a "prime" (opposite-direction) turn.

# Encrypt a message
Messages must be exactly 54 characters in length.
```bash
rubikrypt encrypt "DbffLFrbBuDdRbbLUuLuDFuulDUbFlluLurrdDUbddrbrrbdDLuruBRUlFdDFluLFbudFrudLLuuBuBBRLflbllLRLbrFFrdDrrR" "This is a secret message encrypted with a Rubik's cube"
```
returns
```
eiT  n eissh' mecs  csgr eshrtktstpwiuReaubeaib y cead
```

# Decrypt a message
Messages can be decrypted by making the opposite face turns in the reverse order.
```bash
rubikrypt decrypt "DbffLFrbBuDdRbbLUuLuDFuulDUbFlluLurrdDUbddrbrrbdDLuruBRUlFdDFluLFbudFrudLLuuBuBBRLflbllLRLbrFFrdDrrR" "eiT  n eissh' mecs  csgr eshrtktstpwiuReaubeaib y cead"
```
```
This is a secret message encrypted with a Rubik's cube
```

# Should I use this?
Please don't. I made this as a joke.

This is just `random.shuffle` with extra steps. Your message could likely be decrypted easily using an anagram solver.
