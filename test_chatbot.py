import unittest

from chatbot import FALLBACK, INTENTS, get_reply, sanitize


class TestSanitize(unittest.TestCase):
    def test_case_and_whitespace(self):
        self.assertEqual(sanitize("  HeLLo  "), "hello")

    def test_punctuation_and_inner_spaces(self):
        self.assertEqual(sanitize("How   are you?!"), "how are you")

    def test_apostrophe(self):
        self.assertEqual(sanitize("What's up"), "whats up")


class TestReplies(unittest.TestCase):
    def setUp(self):
        self.memory = {}

    def test_greeting(self):
        self.assertIn(get_reply("HELLO", self.memory), INTENTS["greeting"]["responses"])

    def test_unknown_input_uses_fallback(self):
        self.assertEqual(get_reply("asdfgh", self.memory), FALLBACK)

    def test_dynamic_time(self):
        self.assertIn("right now", get_reply("time", self.memory))

    def test_name_memory(self):
        self.assertIn("Imran", get_reply("my name is imran", self.memory))
        self.assertEqual(get_reply("what is my name", self.memory), "Your name is Imran.")

    def test_name_not_set(self):
        self.assertIn("haven't told me", get_reply("what is my name", self.memory))

    def test_has_at_least_five_intents(self):
        self.assertGreaterEqual(len(INTENTS), 5)


if __name__ == "__main__":
    unittest.main()