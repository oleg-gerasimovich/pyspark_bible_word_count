import unittest

from word_count import remove_symbols, split_in_words


class TestRemoveSymbols(unittest.TestCase):

    def setUp(self) -> None:
        self.sentence = 'PLEASE!!! Stop testing me, friend.'
        self.processed_sentence = 'PLEASE Stop testing me friend'
        self.sentence_to_split = 'HELLO deaR 12 3'
        self.expected_split = ['hello', 'dear']
        return super().setUp()
    
    def test_removing(self):
        result = remove_symbols(self.sentence)

        self.assertEqual(result, self.processed_sentence)

    def test_splitting(self):
        result = split_in_words(self.sentence_to_split)

        self.assertEqual(result, self.expected_split)