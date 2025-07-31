import os
from gemini_client import gemini_client

TRANSCRIPTS_DIR = "transcripts"
MODEL_NAME = "gemini-2.5-flash"

LANG_PROMPTS = {
    "en": (
        "Generate a realistic sales call transcript between Sam (openai.com) and Satya (microsoft.com) "
        "discussing GPU provisioning. Use timestamp format 00:00:00 with speaker labels, "
        "and keep the tone professional and natural."
    ),
    "es": (
        "Genera una transcripción realista de una llamada de ventas entre Sam (openai.com) y Satya (microsoft.com) "
        "discutiendo la provisión de GPUs. Usa el formato de tiempo 00:00:00 con etiquetas de hablante, "
        "y mantén un tono profesional y natural."
    ),
    "fr": (
        "Générez une transcription réaliste d'un appel de vente entre Sam (openai.com) et Satya (microsoft.com) "
        "discutant de la fourniture de GPU. Utilisez le format de temps 00:00:00 avec les étiquettes des interlocuteurs, "
        "et gardez un ton professionnel et naturel."
    ),
}

def generate_transcript(language="en"):
    prompt = LANG_PROMPTS.get(language, LANG_PROMPTS["en"])
    transcript = gemini_client.generate_content(MODEL_NAME, prompt)
    
    print("\nGenerated Transcript:\n")
    print(transcript)
    
    # Ensure transcripts directory exists
    os.makedirs(TRANSCRIPTS_DIR, exist_ok=True)
    filename = os.path.join(TRANSCRIPTS_DIR, f"call_transcript_{language}.txt")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(transcript)
    
    print(f"\nTranscript saved to {filename}")
