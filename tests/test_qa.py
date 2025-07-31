import unittest
import tempfile
from unittest.mock import patch
import os
import sqlite3
from transcript_qa import answer_question
from db import init_db, DB_FILE, save_chat_history

class TestTranscriptQA(unittest.TestCase):
    TEST_DB = ":memory:"

    @classmethod
    def setUpClass(cls):
        # temp db file
        cls.temp_db_file = tempfile.NamedTemporaryFile(delete=False)
        cls.TEST_DB = cls.temp_db_file.name
        cls.temp_db_file.close()

        # Initialize DB 
        init_db(db_file=cls.TEST_DB)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.TEST_DB):
            os.unlink(cls.TEST_DB)
        if os.path.exists("transcripts/test_qa.txt"):
            os.remove("transcripts/test_qa.txt")


    @patch('transcript_qa.gemini_client')
    def test_answer_question_and_save_history(self, mock_client):
        mock_answer = "The customer was interested in GPUs."
        mock_client.generate_content.return_value = mock_answer

        test_file = "transcripts/test_qa.txt"
        os.makedirs("transcripts", exist_ok=True)
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write("Transcript content for Q&A test.")

        question = "What product was the customer interested in?"

        # answer_question with test DB
        answer_question(test_file, question, language="en", db_file=self.TEST_DB)

        # checking test db
        conn = sqlite3.connect(self.TEST_DB)
        cursor = conn.cursor()
        cursor.execute("SELECT question, answer FROM chat_history WHERE question = ?", (question,))
        row = cursor.fetchone()
        conn.close()

        print("Queried row:", row)

        self.assertIsNotNone(row)
        self.assertEqual(row[0], question)
        self.assertEqual(row[1], mock_answer)

        os.remove(test_file)


if __name__ == "__main__":
    unittest.main()
