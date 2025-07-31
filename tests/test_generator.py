import unittest
from unittest.mock import patch
from transcript_generator import generate_transcript
from db import init_db, DB_FILE, save_chat_history
import os

class TestTranscriptGenerator(unittest.TestCase):

    @patch('transcript_generator.gemini_client')
    def test_generate_transcript_creates_file_and_prints(self, mock_client):
        mock_client.generate_content.return_value = "00:00:00 Sam: Hello\n00:00:01 Satya: Hi Sam"
        
        generate_transcript(language="en")
        
        filename = os.path.join("transcripts", "call_transcript_en.txt")
        self.assertTrue(os.path.exists(filename))
        
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIn("Sam: Hello", content)
        
        # Cleanup
        os.remove(filename)

if __name__ == "__main__":
    unittest.main()
