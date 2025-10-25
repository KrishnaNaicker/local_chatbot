"""Knowledge Retriever Module
Handles mathematical calculations."""

import re


class KnowledgeRetriever:
    """Handles calculations and data processing."""

    def __init__(self):
        """Initialize the knowledge retriever."""
        pass

    def calculate_math(self, expression):
        """Calculate mathematical expressions.

        Args:
            expression (str): Math expression

        Returns:
            str or None: Result if valid, None otherwise
        """
        try:
            pattern = r'(\d+\.?\d*)\s*([\+\-\*\/])\s*(\d+\.?\d*)'
            match = re.search(pattern, expression)

            if match:
                num1 = float(match.group(1))
                operator = match.group(2)
                num2 = float(match.group(3))

                if operator == '+':
                    result = num1 + num2
                elif operator == '-':
                    result = num1 - num2
                elif operator == '*':
                    result = num1 * num2
                elif operator == '/':
                    if num2 == 0:
                        return "Cannot divide by zero."
                    result = num1 / num2
                else:
                    return None

                if result == int(result):
                    return str(int(result))
                return str(round(result, 2))

            return None

        except:
            return None