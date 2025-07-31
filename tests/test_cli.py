import unittest
from unittest.mock import patch
import subprocess
import sys
from db import init_db, DB_FILE, save_chat_history
import os

class TestCLI(unittest.TestCase):

    def run_cli(self, args):
        """Helper to run CLI commands as subprocess."""
        cmd = [sys.executable, "app.py"] + args
        completed = subprocess.run(cmd, capture_output=True, text=True)
        return completed

    def test_generate_command(self):
        with patch('transcript_generator.gemini_client') as mock_client:
            mock_client.generate_content.return_value = "00:00:00 Sam: Hello"
            result = self.run_cli(["generate", "--language", "en"])
            self.assertIn("Generated Transcript:", result.stdout)

    def test_summarize_command(self):
        test_file = "transcripts/test_cli_summarize.txt"
        with open(test_file, "w", encoding="utf-8") as f:
            f.write("Sample transcript text.")
        with patch('transcript_summarizer.gemini_client') as mock_client:
            mock_client.generate_content.return_value = "Summary here."
            result = self.run_cli(["summarize", test_file, "--language", "en"])
            self.assertIn("Summary:", result.stdout)
        os.remove(test_file)

    def test_ask_command(self):
        test_file = "transcripts/test_cli_ask.txt"
        with open(test_file, "w", encoding="utf-8") as f:
            f.write("Sample transcript for Q&A.")
        with patch('transcript_qa.gemini_client') as mock_client:
            mock_client.generate_content.return_value = "Answer to your question."
            result = self.run_cli(["ask", test_file, "What product?", "--language", "en"])
            self.assertIn("Answer:", result.stdout)
        os.remove(test_file)

if __name__ == "__main__":
    unittest.main()
