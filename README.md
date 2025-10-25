# Local Command-Line Chatbot

A conversational AI chatbot built with HuggingFace Transformers featuring intelligent text generation, conversation memory, and context-aware responses.

## Overview

This project implements a local command-line chatbot using Google's Flan-T5-Large (780M parameters), an instruction-tuned text generation model from HuggingFace. The chatbot maintains conversation context, performs calculations, and answers questions entirely offline after initial setup.

Purpose: Demonstrate practical NLP implementation with HuggingFace Transformers, conversation memory management, and modular software design.

## Features

- Intelligent Conversations - Natural language understanding using Flan-T5
- Context Awareness - Remembers last 5 conversation turns
- Math Calculations - Accurate arithmetic operations
- 100% Local - Runs offline after model download
- Modular Design - Clean, maintainable code structure
- Interactive CLI - User-friendly command-line interface

## What It Can Do

### Excellent At

- General conversations and greetings
- Mathematics: "what is 25 + 75?" → 100
- Explanations: "what is artificial intelligence?"
- Definitions: "define machine learning"
- Multi-turn contextual dialogue

### Limitations

- Training cutoff: Knowledge ends around 2023
- No real-time data: Cannot access current events
- Hallucination: May generate plausible but incorrect information
- English-focused: Best performance in English
- Response time: 2-5 seconds on CPU

## Technology Stack

- Language: Python 3.8+
- Framework: HuggingFace Transformers 4.30+
- Deep Learning: PyTorch 2.0+
- Model: Flan-T5-Large (780M parameters)

## Setup Guide

### Prerequisites

- Python 3.8 or higher
- 4GB RAM minimum (8GB recommended)
- 5GB free disk space
- Internet connection (for initial setup only)

### Installation Steps

#### Step 1: Create Virtual Environment

Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Note: If you get a PowerShell execution policy error on Windows, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs transformers, torch, and accelerate. Installation takes approximately 2-3 minutes.

#### Step 3: First Run

```bash
python main.py
```

First-time setup downloads Flan-T5-Large model (approximately 3GB) and takes 3-5 minutes. Subsequent runs start in 5-10 seconds.

## Usage

### Starting the Chatbot

```bash
python main.py
```

Make sure your virtual environment is activated before running.

### Available Commands

- /exit - Quit the chatbot application
- /clear - Reset conversation history
- /history - Display full conversation history
- Type any text to chat with the bot

### Example Interactions

#### Basic Conversation

```
User: hello
Bot: Hello! How can I help you today?

User: what is your name
Bot: I'm an AI assistant built with HuggingFace Transformers.
```

#### Math Calculations

```
User: what is 25 + 75
Bot: 100

User: calculate 144 divided by 12
Bot: 12

User: what is 7 * 8
Bot: 56
```

#### General Knowledge

```
User: what is artificial intelligence
Bot: Artificial Intelligence (AI) is a computer science field that deals with creating intelligent machines capable of performing tasks that typically require human intelligence, such as learning, problem-solving, and decision-making.

User: explain quantum computing
Bot: Quantum computing is a type of computing that uses quantum-mechanical phenomena like superposition and entanglement to perform operations on data.
```

#### Multi-turn Conversation

```
User: tell me about python programming
Bot: Python is a high-level, interpreted programming language known for its simplicity and readability.

User: is it good for beginners
Bot: Yes, Python is excellent for beginners due to its simple syntax and extensive documentation.
```

#### Using Commands

```
User: hello
Bot: Hello! How can I help you today?

User: what is 10 + 20
Bot: 30

User: /history
============================================================
CONVERSATION HISTORY
============================================================
User: hello
Bot: Hello! How can I help you today?
User: what is 10 + 20
Bot: 30
============================================================

User: /clear
Conversation history cleared.

User: /exit
Exiting chatbot. Goodbye!
```

## Project Structure

```
local-chatbot/
├── main.py                      # Application entry point
├── requirements.txt             # Python dependencies
├── README.md                    # This documentation file
├── .gitignore                   # Git ignore rules
└── src/                         # Source code directory
    ├── __init__.py              # Package initializer
    ├── model_loader.py          # HuggingFace model loading
    ├── chat_memory.py           # Conversation memory management
    ├── knowledge_retriever.py   # Math calculations
    └── interface.py             # CLI and response generation
```

### Component Descriptions

- main.py: Entry point that initializes and starts the chatbot
- model_loader.py: Handles loading HuggingFace model and tokenizer
- chat_memory.py: Manages conversation history and context
- knowledge_retriever.py: Processes mathematical expressions
- interface.py: Manages CLI interactions and response generation

## Assignment Requirements

This project fulfills all assignment requirements:

- HuggingFace Transformers: Flan-T5-Large model integration
- Text Generation Model: Seq2Seq generation architecture
- Command-Line Interface: Interactive CLI with commands
- Conversation Memory: Context-aware 5-turn memory
- Modular Code Structure: 5 separate modules
- User Commands: /exit, /clear, /history implemented
- Setup Documentation: Complete installation guide
- Usage Examples: Multiple example scenarios

## Model Details

Model Name: google/flan-t5-large

Specifications:
- Type: Sequence-to-Sequence (Seq2Seq) text generation
- Parameters: 780 million
- Architecture: T5 (Text-to-Text Transfer Transformer)
- Training: Instruction-tuned on diverse tasks
- Use Cases: Question answering, conversational AI, instruction following

Why Flan-T5:
- Specifically designed for instruction following
- Superior performance on question-answering tasks
- Better factual accuracy than base models
- Optimized for conversational interactions
- Maintained by Google Research

## How It Works

### Architecture Flow

1. Model Loading: Loads Flan-T5-Large from HuggingFace Hub with automatic device detection
2. Input Processing: Receives user input via CLI and checks for commands
3. Memory Retrieval: Fetches last 5 conversation turns for context
4. Response Generation: Uses model for text or Python for math
5. Output Formatting: Cleans and formats response before display
6. Memory Update: Stores conversation in history

### Response Generation Process

For General Questions:
1. Retrieve conversation context from memory
2. Construct optimized prompt for Flan-T5
3. Tokenize input text
4. Generate response using model with beam search
5. Decode and clean output
6. Return formatted response

For Math:
1. Parse mathematical expression using regex
2. Calculate using Python
3. Format and return result

## Troubleshooting

### Common Issues

Problem: Model download fails or times out
Solution: Check internet connection and try again. HuggingFace servers may be busy.

Problem: Out of memory error
Solution: Close other applications. The model will automatically fall back to CPU.

Problem: Slow responses (over 10 seconds)
Solution: Expected on CPU (2-5 seconds is normal). Use GPU for faster inference.

Problem: Module not found errors
Solution: Ensure virtual environment is activated and run pip install -r requirements.txt

Problem: PowerShell script execution error (Windows)
Solution: Run Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

## Technical Implementation

### Key Technologies

- HuggingFace Transformers: Provides pre-trained models and tokenizers
- PyTorch: Deep learning framework for model inference
- Python: Core programming language
- Virtual Environment: Isolated dependency management

### Design Patterns

- Modular Architecture: Separated concerns for maintainability
- Single Responsibility: Each module handles one aspect
- Dependency Injection: Components receive dependencies via constructors
- Error Handling: Graceful fallbacks for edge cases

## Future Improvements

Potential enhancements:
- Add support for multiple languages
- Implement conversation history persistence
- Create GUI version with web interface
- Add voice input/output capabilities
- Support for model fine-tuning
- Implement user authentication
- Add sentiment analysis
- Create API version for remote access

## Author

Krishna Naicker
- Project: Local Command-Line Chatbot
- Date: January 2025

## Acknowledgments

- HuggingFace - For the Transformers library and model hosting
- Google Research - For developing and open-sourcing Flan-T5
- PyTorch Team - For the deep learning framework
- Python Community - For extensive documentation and support

## License

This project is created for educational purposes.

## Quick Start Summary

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run chatbot
python main.py
```

Made with HuggingFace Transformers 