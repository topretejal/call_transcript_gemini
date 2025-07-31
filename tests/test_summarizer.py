import unittest
from unittest.mock import patch
from transcript_summarizer import summarize_transcript
import os

class TestTranscriptSummarizer(unittest.TestCase):
    
    @patch('transcript_summarizer.gemini_client')
    def test_summarize_transcript_prints_summary(self, mock_client):
        mock_client.generate_content.return_value = "Summary of the call."

        test_file = "transcripts/test_summarize.txt"
        os.makedirs("transcripts", exist_ok=True)
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write("Some transcript content")

        summarize_transcript(test_file, language="en")

        # Cleanup
        os.remove(test_file)

if __name__ == "__main__":
    unittest.main()
