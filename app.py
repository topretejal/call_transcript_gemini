import argparse
from db import init_db
from transcript_generator import generate_transcript
from transcript_summarizer import summarize_transcript
from transcript_qa import answer_question

def main():
    init_db()
    
    parser = argparse.ArgumentParser(description="Sales Call Transcript CLI Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Generate transcript command
    gen_parser = subparsers.add_parser("generate", help="Generate a mock sales call transcript")
    gen_parser.add_argument("--language", choices=["en", "es", "fr"], default="en", help="Language for the transcript")

    # Summarize command
    sum_parser = subparsers.add_parser("summarize", help="Summarize an existing transcript file")
    sum_parser.add_argument("filename", help="Path to transcript file")
    sum_parser.add_argument("--language", choices=["en", "es", "fr"], default="en", help="Language for the summary")

    # Ask command
    ask_parser = subparsers.add_parser("ask", help="Ask a question about a transcript")
    ask_parser.add_argument("filename", help="Path to transcript file")
    ask_parser.add_argument("question", help="Question to ask related to the transcript")
    ask_parser.add_argument("--language", choices=["en", "es", "fr"], default="en", help="Language for the answer")

    args = parser.parse_args()

    if args.command == "generate":
        generate_transcript(language=args.language)
    elif args.command == "summarize":
        summarize_transcript(args.filename, language=args.language)
    elif args.command == "ask":
        answer_question(args.filename, args.question, language=args.language)

if __name__ == "__main__":
    main()
