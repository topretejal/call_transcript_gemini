import os
from gemini_client import gemini_client
from db import save_chat_history, DB_FILE

MODEL_NAME = "gemini-2.5-flash"

LANG_PROMPTS_QA = {
    "en": "Based on the following sales call transcript, answer the question:",
    "es": "Basado en la siguiente transcripción de llamada de ventas, responde la pregunta:",
    "fr": "Sur la base de la transcription suivante d'un appel de vente, répondez à la question :"
}

def answer_question(filename: str, question: str, language="en", db_file=None):
    if db_file is None:
        db_file = DB_FILE 
    if not os.path.exists(filename):
        print(f"Error: Transcript file '{filename}' not found.")
        return

    with open(filename, "r", encoding="utf-8") as f:
        transcript_text = f.read()

    prompt_intro = LANG_PROMPTS_QA.get(language, LANG_PROMPTS_QA["en"])
    prompt = f"{prompt_intro}\n\n{transcript_text}\n\nQuestion: {question}\nAnswer:"

    answer = gemini_client.generate_content(MODEL_NAME, prompt)
    print(f"\nAnswer:\n{answer}")

    save_chat_history(question, answer, language, db_file=db_file)
