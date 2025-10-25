"""Main Entry Point
Launches the command-line chatbot application."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from interface import ChatInterface


def main():
    """Main function to start the chatbot.
    Uses Flan-T5 - instruction-tuned text generation model from HuggingFace"""
    chatbot = ChatInterface(
        model_name="google/flan-t5-large",
        memory_turns=5
    )

    chatbot.run()


if __name__ == "__main__":
    main()