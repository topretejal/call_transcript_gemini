import os
from gemini_client import gemini_client

MODEL_NAME = "gemini-2.5-flash"

LANG_PROMPTS_SUMMARY = {
    "en": "Summarize the key points from the following sales call transcript:",
    "es": "Resume los puntos clave de la siguiente transcripción de una llamada de ventas:",
    "fr": "Résumez les points clés de la transcription suivante d'un appel de vente:"
}

def summarize_transcript(filename: str, language="en"):
    if not os.path.exists(filename):
        print(f"Error: Transcript file '{filename}' not found.")
        return

    with open(filename, "r", encoding="utf-8") as f:
        transcript_text = f.read()

    prompt_intro = LANG_PROMPTS_SUMMARY.get(language, LANG_PROMPTS_SUMMARY["en"])
    prompt = f"{prompt_intro}\n\n{transcript_text}\n\nSummary:"

    summary = gemini_client.generate_content(MODEL_NAME, prompt)
    print("\nSummary:\n")
    print(summary)
