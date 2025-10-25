# 🤖 Local Command-Line Chatbot

A fully functional command-line chatbot powered by Hugging Face transformers, featuring conversational memory and modular architecture.

## 📋 Features

- ✅ Runs completely locally (no API keys required)
- ✅ Maintains conversation context using sliding window memory
- ✅ Modular, maintainable code structure
- ✅ Easy-to-use CLI interface
- ✅ Graceful exit handling
- ✅ GPU support (optional, falls back to CPU)

## 🏗️ Project Structure

```
local-chatbot/
├── src/
│   ├── __init__.py           # Package initializer
│   ├── model_loader.py       # Model and tokenizer loading
│   ├── chat_memory.py        # Conversation memory management
│   └── interface.py          # CLI interface and main loop
├── main.py                   # Entry point
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## 🚀 Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip package manager
- (Optional) CUDA-compatible GPU for faster inference

### Installation

1. **Clone or download this repository**

2. **Create a virtual environment (recommended)**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

This will install:
- `transformers` - Hugging Face library
- `torch` - PyTorch for model inference
- `accelerate` - For optimized model loading

**Note:** First run will download the model (~350MB for DialoGPT-medium). This is a one-time download.

## 🎮 How to Run

1. **Activate your virtual environment** (if not already active)

2. **Run the chatbot**

```bash
python main.py
```

3. **Start chatting!**

## 💬 Usage Examples

### Basic Conversation

```
User: What is the capital of France?
Bot: The capital of France is Paris.

User: And what about Italy?
Bot: The capital of Italy is Rome.

User: /exit
Exiting chatbot. Goodbye!
```

### Using Commands

```
User: Hello!
Bot: Hi! How can I help you today?

User: /history
--- Conversation History ---
User: Hello!
Bot: Hi! How can I help you today?
----------------------------

User: /clear
🧹 Memory cleared!

User: /exit
Exiting chatbot. Goodbye!
```

## 🎛️ Available Commands

| Command | Description |
|---------|-------------|
| `/exit` | Exit the chatbot |
| `/clear` | Clear conversation history |
| `/history` | Display current conversation memory |

## 🧠 How It Works

### 1. Model Loader (`model_loader.py`)
- Loads the Hugging Face model and tokenizer
- Detects available hardware (GPU/CPU)
- Uses **microsoft/DialoGPT-medium** by default - a model trained specifically for conversations

### 2. Chat Memory (`chat_memory.py`)
- Implements a **sliding window buffer**
- Keeps last 4 conversation turns (8 messages total)
- Automatically removes oldest messages when limit is reached
- Provides context to the model for coherent responses

### 3. Interface (`interface.py`)
- Manages the CLI conversation loop
- Handles user input and commands
- Generates responses using model + memory
- Provides error handling and graceful exits

## ⚙️ Configuration

You can customize the chatbot by editing `main.py`:

```python
chatbot = ChatInterface(
    model_name="microsoft/DialoGPT-medium",  # Change model here
    memory_turns=4  # Adjust memory size (higher = more context)
)
```

### Alternative Models

| Model | Size | Speed | Quality |
|-------|------|-------|---------|
| `microsoft/DialoGPT-small` | ~100MB | Fast | Good |
| `microsoft/DialoGPT-medium` | ~350MB | Medium | Better |
| `distilgpt2` | ~300MB | Fast | Good |
| `gpt2` | ~500MB | Medium | Good |

## 🐛 Troubleshooting

### Issue: Model downloads slowly
**Solution:** First download takes time (~350MB). Be patient - it's cached for future use.

### Issue: Out of memory error
**Solution:** Use a smaller model like `DialoGPT-small` or `distilgpt2`

### Issue: Responses are repetitive
**Solution:** Type `/clear` to reset conversation history

### Issue: Import errors
**Solution:** Make sure you're running from the project root directory and virtual environment is activated

## 📊 Technical Details

- **Memory Strategy:** Sliding window (FIFO queue)
- **Context Building:** Concatenates recent exchanges
- **Generation Parameters:**
  - `max_new_tokens=50` - Controls response length
  - `temperature=0.7` - Controls randomness
  - `top_k=50, top_p=0.95` - Sampling strategies
  - `no_repeat_ngram_size=3` - Prevents repetition

## 🎥 Demo Video

[Include link to your demo video here]

## 👨‍💻 Development

### Code Quality
- Modular design with separation of concerns
- Comprehensive docstrings
- Error handling throughout
- Type hints for clarity

### Testing Locally
Run with different models to test:
```bash
# Edit main.py to change model_name parameter
python main.py
```

## 📝 License

This project is created for educational purposes.

## 🙏 Acknowledgments

- Hugging Face for the transformers library
- Microsoft for the DialoGPT model
- OpenAI for GPT-2 base models

---

**Developed By:** Krishna Naicker
**Date:** October 2025  

```# local_chatbot
