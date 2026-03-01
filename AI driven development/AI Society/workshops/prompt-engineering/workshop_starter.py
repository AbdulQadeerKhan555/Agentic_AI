"""
Prompt and Context Engineering Workshop - Starter Code
======================================================

This starter code provides the foundation for building:
1. A Prompt Template Library
2. A Context-Aware AI Assistant
3. A Simple RAG (Retrieval-Augmented Generation) System

Setup Instructions:
1. Install required libraries: pip install openai anthropic python-dotenv
2. Create a .env file with your API key:
   OPENAI_API_KEY=your_key_here
   OR
   ANTHROPIC_API_KEY=your_key_here
3. Run this file: python workshop_starter.py

Throughout this file, look for TODO comments - these are sections you'll implement!
"""

import os
from typing import List, Dict, Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# =============================================================================
# PART 1: PROMPT TEMPLATE LIBRARY
# =============================================================================

class PromptTemplate:
    """
    A reusable prompt template with variable substitution.

    Example usage:
        template = PromptTemplate(
            "Explain this code: {code}\\nUse {style} language."
        )
        prompt = template.format(code="print('hello')", style="simple")
    """

    def __init__(self, template: str, required_vars: Optional[List[str]] = None):
        """
        Initialize a prompt template.

        Args:
            template: String with {variable} placeholders
            required_vars: List of required variable names (optional)
        """
        self.template = template
        self.required_vars = required_vars or []

    def format(self, **kwargs) -> str:
        """
        Format the template with provided variables.

        TODO: Implement this method!
        Steps:
        1. Check if all required_vars are present in kwargs
        2. If missing variables, raise ValueError with helpful message
        3. Use string .format() to substitute variables
        4. Return the formatted prompt

        Args:
            **kwargs: Variable names and their values

        Returns:
            Formatted prompt string

        Raises:
            ValueError: If required variables are missing
        """
        # TODO: Your code here
        pass

    def get_variables(self) -> List[str]:
        """
        Extract all variable names from the template.

        TODO: Implement this method!
        Hint: Look for text between { and } in self.template
        You can use string methods or regex.

        Returns:
            List of variable names found in template
        """
        # TODO: Your code here
        pass


# Pre-built prompt templates for common tasks
PROMPT_TEMPLATES = {
    "code_explainer": PromptTemplate(
        template="""You are a helpful programming tutor. Explain the following code in {style} terms:

Code:
```{language}
{code}
```

Provide:
1. What the code does (high-level)
2. How it works (step-by-step)
3. Any potential issues or improvements""",
        required_vars=["code", "language", "style"]
    ),

    "meeting_summarizer": PromptTemplate(
        template="""Summarize this meeting transcript and extract action items:

Transcript:
{transcript}

Provide:
1. Brief summary (2-3 sentences)
2. Key decisions made
3. Action items with owners (if mentioned)
4. Follow-up questions""",
        required_vars=["transcript"]
    ),

    "data_extractor": PromptTemplate(
        template="""Extract structured data from the following text and return it as JSON.

Text:
{text}

Extract these fields: {fields}

Return ONLY valid JSON, no additional text.""",
        required_vars=["text", "fields"]
    )
}


# =============================================================================
# PART 2: API CLIENT WRAPPER
# =============================================================================

class LLMClient:
    """
    Wrapper for LLM API calls. Supports OpenAI and Anthropic.
    """

    def __init__(self, provider: str = "openai", model: Optional[str] = None):
        """
        Initialize the LLM client.

        Args:
            provider: "openai" or "anthropic"
            model: Model name (optional, uses defaults)
        """
        self.provider = provider.lower()

        if self.provider == "openai":
            try:
                from openai import OpenAI
                self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
                self.model = model or "gpt-3.5-turbo"
            except ImportError:
                raise ImportError("Install openai: pip install openai")

        elif self.provider == "anthropic":
            try:
                from anthropic import Anthropic
                self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
                self.model = model or "claude-3-haiku-20240307"
            except ImportError:
                raise ImportError("Install anthropic: pip install anthropic")
        else:
            raise ValueError(f"Unknown provider: {provider}")

    def generate(self, prompt: str, system_prompt: Optional[str] = None,
                 max_tokens: int = 1000) -> str:
        """
        Generate a response from the LLM.

        TODO: Implement this method!
        Steps:
        1. Check self.provider to determine which API to use
        2. For OpenAI: Use self.client.chat.completions.create()
           - messages format: [{"role": "system", "content": ...}, {"role": "user", "content": prompt}]
        3. For Anthropic: Use self.client.messages.create()
           - system parameter separate, messages format: [{"role": "user", "content": prompt}]
        4. Extract and return the text response
        5. Handle errors gracefully (try/except)

        Args:
            prompt: The user prompt
            system_prompt: Optional system prompt
            max_tokens: Maximum tokens to generate

        Returns:
            Generated text response
        """
        # TODO: Your code here
        pass


# =============================================================================
# PART 3: CONVERSATION MANAGER (Context-Aware Assistant)
# =============================================================================

class ConversationManager:
    """
    Manages conversation history and context for multi-turn interactions.
    """

    def __init__(self, system_prompt: str, max_history: int = 10):
        """
        Initialize conversation manager.

        Args:
            system_prompt: The system prompt defining assistant behavior
            max_history: Maximum number of messages to keep in history
        """
        self.system_prompt = system_prompt
        self.max_history = max_history
        self.messages: List[Dict[str, str]] = []

    def add_message(self, role: str, content: str):
        """
        Add a message to conversation history.

        TODO: Implement this method!
        Steps:
        1. Create a message dict with "role" and "content" keys
        2. Append to self.messages
        3. If len(self.messages) > self.max_history, remove oldest messages
           (Keep the conversation from getting too long)

        Args:
            role: "user" or "assistant"
            content: Message content
        """
        # TODO: Your code here
        pass

    def get_context(self) -> List[Dict[str, str]]:
        """
        Get the full conversation context for API calls.

        Returns:
            List of message dictionaries
        """
        return self.messages.copy()

    def clear_history(self):
        """Clear all conversation history."""
        self.messages = []

    def count_tokens(self) -> int:
        """
        Estimate token count for current conversation.

        TODO: Implement this method!
        Simple estimation: ~4 characters = 1 token
        For production, use tiktoken (OpenAI) or proper tokenizer.

        Returns:
            Estimated token count
        """
        # TODO: Your code here
        pass

    def summarize_and_prune(self, llm_client: LLMClient):
        """
        STRETCH GOAL: Summarize old messages when context gets too long.

        This is an advanced feature. If you finish early, try implementing:
        1. Take the oldest 50% of messages
        2. Use LLM to summarize them
        3. Replace those messages with a single summary message
        4. Keep recent messages intact
        """
        # STRETCH GOAL: Your code here
        pass


# =============================================================================
# PART 4: KNOWLEDGE BASE (RAG System)
# =============================================================================

class KnowledgeBase:
    """
    Simple knowledge base for RAG (Retrieval-Augmented Generation).
    Stores documents and retrieves relevant chunks based on queries.
    """

    def __init__(self):
        """Initialize empty knowledge base."""
        self.documents: List[Dict[str, str]] = []

    def add_document(self, content: str, metadata: Optional[Dict] = None):
        """
        Add a document to the knowledge base.

        Args:
            content: Document text
            metadata: Optional metadata (title, source, date, etc.)
        """
        doc = {
            "content": content,
            "metadata": metadata or {},
            "id": len(self.documents)
        }
        self.documents.append(doc)

    def chunk_text(self, text: str, chunk_size: int = 500) -> List[str]:
        """
        Split text into smaller chunks.

        TODO: Implement this method!
        Simple approach: Split by sentences or paragraphs.
        Steps:
        1. Split text by periods or newlines
        2. Group into chunks of approximately chunk_size characters
        3. Return list of chunks

        Args:
            text: Text to chunk
            chunk_size: Target size for each chunk (characters)

        Returns:
            List of text chunks
        """
        # TODO: Your code here
        pass

    def search(self, query: str, top_k: int = 3) -> List[Dict]:
        """
        Search for relevant documents.

        TODO: Implement this method!
        Simple keyword-based search:
        1. Convert query to lowercase
        2. For each document, count how many query words appear in it
        3. Sort documents by relevance score (word matches)
        4. Return top_k most relevant documents

        STRETCH GOAL: Use semantic search with embeddings
        - Install: pip install sentence-transformers
        - Encode query and documents as vectors
        - Use cosine similarity for ranking

        Args:
            query: Search query
            top_k: Number of results to return

        Returns:
            List of relevant documents (dicts with content and metadata)
        """
        # TODO: Your code here
        pass

    def load_from_file(self, filepath: str):
        """
        Load documents from a text file.

        Args:
            filepath: Path to text file
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                self.add_document(content, metadata={"source": filepath})
                print(f"Loaded document from {filepath}")
        except FileNotFoundError:
            print(f"File not found: {filepath}")
        except Exception as e:
            print(f"Error loading file: {e}")


# =============================================================================
# PART 5: RAG QUERY PIPELINE
# =============================================================================

def rag_query(query: str, knowledge_base: KnowledgeBase,
              llm_client: LLMClient, top_k: int = 3) -> str:
    """
    Perform a RAG query: retrieve relevant context and generate answer.

    TODO: Implement this function!
    Steps:
    1. Use knowledge_base.search() to find relevant documents
    2. Extract the content from retrieved documents
    3. Combine retrieved content into a context string
    4. Create a prompt that includes:
       - The retrieved context
       - The user's query
       - Instructions to answer based on the context
    5. Use llm_client.generate() to get the answer
    6. Return the answer

    Args:
        query: User's question
        knowledge_base: KnowledgeBase instance
        llm_client: LLMClient instance
        top_k: Number of documents to retrieve

    Returns:
        Generated answer grounded in retrieved context
    """
    # TODO: Your code here
    pass


# =============================================================================
# PART 6: INTERACTIVE CHAT LOOP
# =============================================================================

def run_chat_assistant():
    """
    Run an interactive chat session with the context-aware assistant.

    TODO: Implement this function!
    Steps:
    1. Create a ConversationManager with an appropriate system prompt
    2. Create an LLMClient
    3. Start a loop that:
       - Gets user input
       - Adds user message to conversation
       - Gets conversation context
       - Generates response using LLM
       - Adds assistant response to conversation
       - Prints the response
       - Continues until user types "quit" or "exit"

    BONUS: Add commands like /clear (clear history), /tokens (show token count)
    """
    print("=== Context-Aware AI Assistant ===")
    print("Type 'quit' or 'exit' to end the conversation")
    print("Type '/clear' to clear conversation history")
    print("Type '/tokens' to see token count\n")

    # TODO: Your code here
    pass


# =============================================================================
# EXAMPLE USAGE & TESTING
# =============================================================================

def test_prompt_templates():
    """Test the prompt template system."""
    print("\n=== Testing Prompt Templates ===\n")

    # Test code explainer template
    template = PROMPT_TEMPLATES["code_explainer"]

    # TODO: Use template.format() to create a prompt
    # Example: explain a simple Python function

    print("Template variables:", template.get_variables())
    # TODO: Print the formatted prompt


def test_conversation():
    """Test the conversation manager."""
    print("\n=== Testing Conversation Manager ===\n")

    # TODO: Create a ConversationManager
    # TODO: Add some test messages
    # TODO: Print the conversation context
    # TODO: Print token count


def test_knowledge_base():
    """Test the knowledge base and RAG system."""
    print("\n=== Testing Knowledge Base ===\n")

    # TODO: Create a KnowledgeBase
    # TODO: Add some sample documents (e.g., course notes, facts)
    # TODO: Test search functionality
    # TODO: Try a RAG query


def main():
    """
    Main function - choose what to run.
    """
    print("Prompt and Context Engineering Workshop")
    print("=" * 50)
    print("\nWhat would you like to test?")
    print("1. Prompt Templates")
    print("2. Conversation Manager")
    print("3. Knowledge Base & RAG")
    print("4. Interactive Chat Assistant")
    print("5. Run all tests")

    choice = input("\nEnter choice (1-5): ").strip()

    if choice == "1":
        test_prompt_templates()
    elif choice == "2":
        test_conversation()
    elif choice == "3":
        test_knowledge_base()
    elif choice == "4":
        run_chat_assistant()
    elif choice == "5":
        test_prompt_templates()
        test_conversation()
        test_knowledge_base()
    else:
        print("Invalid choice. Running all tests...")
        test_prompt_templates()
        test_conversation()
        test_knowledge_base()


if __name__ == "__main__":
    # Check if API keys are set
    if not os.getenv("OPENAI_API_KEY") and not os.getenv("ANTHROPIC_API_KEY"):
        print("WARNING: No API keys found!")
        print("Please create a .env file with:")
        print("  OPENAI_API_KEY=your_key_here")
        print("  OR")
        print("  ANTHROPIC_API_KEY=your_key_here")
        print()

    main()


# =============================================================================
# PORTFOLIO ENHANCEMENT IDEAS
# =============================================================================
"""
Once you complete the basic implementation, consider these extensions:

1. WEB INTERFACE
   - Use Streamlit or Gradio to create a web UI
   - Add file upload for knowledge base documents
   - Show conversation history in a chat interface

2. ADVANCED RAG
   - Implement semantic search with sentence-transformers
   - Add citation tracking (show which documents were used)
   - Support multiple file formats (PDF, DOCX, etc.)

3. PROMPT OPTIMIZATION
   - Add A/B testing for different prompt variations
   - Implement prompt versioning and tracking
   - Create a prompt library browser

4. CONVERSATION FEATURES
   - Export conversations to Markdown or PDF
   - Implement conversation branching (explore different paths)
   - Add conversation summarization

5. SPECIALIZED ASSISTANTS
   - Code Review Bot (analyzes code quality)
   - Research Paper Summarizer (extracts key findings)
   - Study Buddy (Socratic method tutoring)
   - Meeting Notes Assistant (real-time transcription + summary)

6. PRODUCTION FEATURES
   - Add proper error handling and logging
   - Implement rate limiting and retry logic
   - Add unit tests
   - Create Docker container for easy deployment
   - Add monitoring and analytics

Remember: Start simple, make it work, then add features!
"""
