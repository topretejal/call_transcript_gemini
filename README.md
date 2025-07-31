# Sales Call Transcript CLI Tool

It supports multiple languages(English, Spanish, French) and stores question and AI answer history in a local SQLite database.

### Prerequisites:

Python3.9+
Google GenAI SDK installed (pip install google-genai)

### Steps to follow

Create python venv
python3.9 -m venv ct_venv
Install all dependencies in ct_venv using requirements.txt
pip install -r requirements.txt
Create Gemini API Key from Google AI studio
Keep it in .env file as GEMINI_API_KEY=”generated_key”

### Usage

Generate transcript(default is English)
In English
python app.py generate –language en
In Spanish
python app.py generate –language es
In French
python app.py generate –language fr
Summarize a transcript
python app.py summarize transcripts/call_transcript_en.txt --language en
Ask a question about a transcript
python app.py ask transcripts/call_transcript_en.txt "What was the duration of the call?" --language en
Run all tests with
Python -m unittest discover tests

### Features

Generate sales call transcripts with timestamps and speaker labels
Summarizes existing call transcripts
Answer Questions based on transcript content.
Supports multi-language prompts (‘en,’es’,’fr’)
Persists chat history (QnA) in SQLite db

### Project Structure

app.py - CLI entry point
Gemini_client.py - Google GenAI
Transcript_generator.py - Transcript Generation Logic
Transcript_summarizer.py - Summarization Logic
Transcript_qa.py - Question answering and chat history db storage
db.py - for SQLite db management and storage
Transcripts folder - to save generated transcripts
Tests folder - Unit tests
Requirements.txt - python dependencies

### AI Usage and modifications

Used AI for getting syntax and generating prompt, writing unit tests.
Referred gemini api developers documentation for the development
Used "gemini-2.5-flash" model
https://ai.google.dev/gemini-api/docs/migrate
