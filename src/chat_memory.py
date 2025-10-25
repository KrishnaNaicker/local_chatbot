"""Chat Memory Module
Manages conversation history and context for the chatbot."""


class ChatMemory:
    """Stores and manages conversation history to maintain context
    across multiple interactions."""

    def __init__(self, max_turns=5):
        """Initialize the chat memory.

        Args:
            max_turns (int): Maximum number of conversation turns to remember
        """
        self.max_turns = max_turns
        self.history = []

    def add_user_message(self, message):
        """Add a user message to the conversation history.

        Args:
            message (str): The user's message
        """
        self.history.append({"role": "user", "content": message})
        self._trim_history()

    def add_bot_message(self, message):
        """Add a bot response to the conversation history.

        Args:
            message (str): The bot's response
        """
        self.history.append({"role": "bot", "content": message})
        self._trim_history()

    def _trim_history(self):
        """Trim the history to maintain only the most recent turns."""
        if len(self.history) > self.max_turns * 2:
            self.history = self.history[-(self.max_turns * 2):]

    def get_context_string(self):
        """Get the conversation history as a formatted string for context."""
        if not self.history:
            return ""

        context_parts = []
        for entry in self.history[-6:]:
            role = "User" if entry["role"] == "user" else "Bot"
            context_parts.append(f"{role}: {entry['content']}")

        return "\n".join(context_parts)

    def get_history(self):
        """Get the full conversation history."""
        return self.history

    def clear(self):
        """Clear all conversation history."""
        self.history = []
        print("✓ Conversation history cleared.\n")

    def display_history(self):
        """Display the conversation history in a readable format."""
        if not self.history:
            print("\nNo conversation history yet.\n")
            return

        print("\n" + "=" * 60)
        print("CONVERSATION HISTORY")
        print("=" * 60)

        for i, entry in enumerate(self.history, 1):
            role = "User" if entry["role"] == "user" else "Bot"
            print(f"{role}: {entry['content']}")

        print("=" * 60 + "\n")