"""Model Loader Module
Handles loading and initializing the Hugging Face model and tokenizer."""

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch


class ModelLoader:
    """A class to load and manage the language model and tokenizer."""

    def __init__(self, model_name="google/flan-t5-large"):
        """Initialize the model loader with a specified model.

        Args:
            model_name (str): HuggingFace model identifier
        """
        self.model_name = model_name
        self.tokenizer = None
        self.model = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def load(self):
        """Load the model and tokenizer from HuggingFace.

        Returns:
            tuple: (tokenizer, model) objects
        """
        print(f"🔄 Loading model: {self.model_name}")
        print(f"💻 Using device: {self.device}")
        print("⏳ This may take a few minutes on first run...\n")

        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)

            self.model = AutoModelForSeq2SeqLM.from_pretrained(
                self.model_name,
                dtype=torch.float32,
                low_cpu_mem_usage=True
            )

            self.model.to(self.device)
            self.model.eval()

            print("✅ Model loaded successfully!\n")
            return self.tokenizer, self.model

        except Exception as e:
            print(f"❌ Error loading model: {e}")
            raise
