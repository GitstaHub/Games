import unittest
import random
from Hangman import get_random_word, is_letter_in_word, check_valid_input


class TestRandomwords(unittest.TestCase):

    def test_random_word(self):
        random.seed(42)
        word = get_random_word()
        self.assertEqual(word, 'crack')

    def test_random_word2(self):
        random.seed(1)
        word = get_random_word()
        self.assertEqual(word, 'develop')

    def test_random_word3(self):
        random.seed(1)
        word = get_random_word()
        self.assertNotEqual(word, 'learn')

    def test_letter_check(self):
        self.assertEqual(is_letter_in_word('a', 'learn'), 1)

    def test_letter_check2(self):
        self.assertEqual(is_letter_in_word('b', 'apple'), 0)

    def test_letter_check3(self):
        self.assertNotEqual(is_letter_in_word('a', 'Apple'), 1)

    def test_valid_letter(self):
        self.assertEqual(check_valid_input('a'), 1)

    def test_valid_letter2(self):
        self.assertEqual(check_valid_input('ad'), 0)

    def test_valid_letter3(self):
        self.assertEqual(check_valid_input('!'), 0)

