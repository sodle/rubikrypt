import random
import unittest

from rubikrypt import main


class RubikryptTests(unittest.TestCase):
    def test_crypto(self):
        key_length = random.randint(1, 1000)
        print(f"Testing {key_length} byte key")
        key = main.keygen(key_length)

        message = "This is a secret message encrypted with a Rubik's cube"
        encrypted_message = main.encrypt(key, message)
        self.assertNotEqual(message, encrypted_message)
        decrypted_message = main.decrypt(key, encrypted_message)
        self.assertEqual(message, decrypted_message)


if __name__ == '__main__':
    unittest.main()
