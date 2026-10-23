import unittest

from src.chatbot import ChatBot


class TestChatbot(unittest.TestCase):

    def setUp(self):
        self.bot = ChatBot()

    def test_greeting_response(self):
        self.assertEqual(self.bot.get_response("hello"), "Hello! How can i help you?")

    def test_identity_response(self):
        self.assertEqual(
            self.bot.get_response("who are you"),
            "I am MiniChat AI, a simple chatbot built with Python.",
        )

    def test_unknown_message(self):
        self.assertEqual(
            self.bot.get_response("gotta run"), "I'm not sure i understand that yet."
        )

    def test_empty_message(self):
        self.assertEqual(self.bot.get_response(""), "Please enter a valid message.")

    def test_whitespace_message(self):
        self.assertEqual(self.bot.get_response("   "), "Please enter a valid message.")

    def test_numerical_message(self):
        self.assertEqual(
            self.bot.get_response(123),
            "Please enter a valid message."
        )

    def test_spaced_capital_message(self):
            self.assertEqual(
                self.bot.get_response(" HELLO "),
                "Hello! How can i help you?"
            )

    def test_messages_with_punctuation(self):
        self.assertEqual(
            self.bot.get_response("who are you?"),
            "I am MiniChat AI, a simple chatbot built with Python."
        )
    
if __name__ == "__main__":
    unittest.main()
