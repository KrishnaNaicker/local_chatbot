"""
Interface Module
Provides the command-line interface for the chatbot.
"""

import sys
import warnings
import torch
from model_loader import ModelLoader
from chat_memory import ChatMemory
from knowledge_retriever import KnowledgeRetriever

class ChatInterface:
    """
    Command-line interface for interacting with the chatbot.
    """
    
    def __init__(self, model_name="google/flan-t5-large", memory_turns=5):
        """
        Initialize the chat interface.
        
        Args:
            model_name (str): HuggingFace model to use
            memory_turns (int): Number of conversation turns to remember
        """
        self.memory = ChatMemory(max_turns=memory_turns)
        self.model_loader = ModelLoader(model_name=model_name)
        self.knowledge_retriever = KnowledgeRetriever()
        self.tokenizer = None
        self.model = None
        
    def setup(self):
        """Load the model and prepare the chatbot."""
        print("=" * 60)
        print("🤖 LOCAL COMMAND-LINE CHATBOT")
        print("=" * 60)
        
        # Load model
        self.tokenizer, self.model = self.model_loader.load()
    
    def is_math_question(self, text):
        """Check if the question is about math."""
        math_indicators = ['+', '-', '*', '/', 'plus', 'minus', 'times', 'divided']
        return any(indicator in text.lower() for indicator in math_indicators)
    
    def is_simple_greeting(self, text):
        """Check if the text is a simple greeting."""
        simple_greetings = ["hi", "hello", "hey", "sup", "yo", "greetings"]
        return text.lower().strip() in simple_greetings
    
    def generate_response(self, user_input):
        """
        Generate response using the model.
        
        Args:
            user_input (str): The user's message
            
        Returns:
            str: The bot's response
        """
        # Quick greeting
        if self.is_simple_greeting(user_input):
            return "Hello! How can I help you today?"
        
        # Handle math with Python (accurate and fast)
        if self.is_math_question(user_input):
            result = self.knowledge_retriever.calculate_math(user_input)
            if result:
                return result
        
        # Use HuggingFace model for all other questions
        return self.generate_model_response(user_input)
    
    def generate_model_response(self, user_input):
        """
        Generate response using Flan-T5 with optimized prompting.
        
        Args:
            user_input (str): The user's message
            
        Returns:
            str: The bot's response
        """
        # Get conversation context
        context = self.memory.get_context_string()
        
        # Optimize prompt for Flan-T5 (instruction-tuned model)
        if context:
            # Include context for multi-turn conversations
            prompt = f"Based on this conversation:\n{context}\n\nAnswer this: {user_input}"
        else:
            # Direct question - simpler prompt
            prompt = f"Answer: {user_input}"
        
        # Tokenize input
        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            max_length=512,
            truncation=True
        ).to(self.model_loader.device)
        
        # Generate response
        with torch.no_grad():
            import logging
            logging.getLogger("transformers").setLevel(logging.ERROR)
            
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore")
                
                # Flan-T5 generation parameters
                outputs = self.model.generate(
                    **inputs,
                    max_length=200,
                    min_length=5,
                    do_sample=True,
                    top_p=0.92,
                    top_k=50,
                    temperature=0.7,
                    num_beams=4,
                    early_stopping=True,
                    no_repeat_ngram_size=3
                )
        
        # Decode response
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # AGGRESSIVE CLEANING
        response = response.strip()
        
        # Remove "Bot:" prefix variations
        prefixes_to_remove = ["Bot:", "bot:", "Bot :", "bot :", "BOT:", "Assistant:", "assistant:"]
        for prefix in prefixes_to_remove:
            if response.startswith(prefix):
                response = response[len(prefix):].strip()
                break
        
        # Remove any remaining "Bot:" in the middle
        response = response.replace("Bot:", "").replace("bot:", "").strip()
        
        # Ensure minimum quality
        if not response or len(response) < 3:
            response = "I'm not sure about that. Could you rephrase your question?"
        
        return response
    
    def print_welcome_message(self):
        """Display welcome message and instructions."""
        print("\n👋 Welcome! I'm your local AI assistant powered by HuggingFace.")
        print("\n💡 Features:")
        print("   • Powered by Google Flan-T5 (instruction-tuned)")
        print("   • Conversation memory with context awareness")
        print("   • Mathematical calculations")
        print("   • 100% local - no internet required")
        print("\n💡 Commands:")
        print("   • Type '/exit' to quit")
        print("   • Type '/clear' to reset conversation")
        print("   • Type '/history' to view conversation history")
        print("\n" + "=" * 60 + "\n")
    
    def run(self):
        """Main conversation loop."""
        self.setup()
        self.print_welcome_message()
        
        warnings.filterwarnings("ignore")
        import logging
        logging.getLogger("transformers").setLevel(logging.ERROR)
        
        while True:
            try:
                user_input = input("User: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() == "/exit":
                    print("\nExiting chatbot. Goodbye! 👋\n")
                    sys.exit(0)
                
                if user_input.lower() == "/clear":
                    self.memory.clear()
                    continue
                
                if user_input.lower() == "/history":
                    self.memory.display_history()
                    continue
                
                self.memory.add_user_message(user_input)
                
                # Generate response
                response = self.generate_response(user_input)
                print(f"Bot: {response}")
                
                self.memory.add_bot_message(response)
                
                print()
                
            except KeyboardInterrupt:
                print("\n\n⚠️  Interrupted. Type '/exit' to quit properly.\n")
                continue
            except Exception as e:
                print(f"❌ Error: {e}")
                continue