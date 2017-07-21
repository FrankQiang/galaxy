import unittest
from app.handle_str import handle_sentence


class APITestCase(unittest.TestCase):

    def setUp(self):
        handle_sentence("pish is X")
        handle_sentence("glob is L")
        handle_sentence("pish glob Silver is 40 Credits")

    def test_handle_sentence_error(self):
        answer = handle_sentence("What ...")
        self.assertTrue(answer == 0)

        answer = handle_sentence("how ?")
        self.assertTrue(answer == 0)

    def test_handle_sentence_how_much(self):
        answer = handle_sentence("how much is pish glob ?")
        self.assertTrue(answer == "pish glob is 40")

    def test_handle_sentence_how_many(self):
        answer = handle_sentence("how many Credits is pish pish Silver ?")
        self.assertTrue(answer == "pish pish Silver is 20 Credits")
