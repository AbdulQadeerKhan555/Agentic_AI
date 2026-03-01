# Prompt and Context Engineering Workshop

A complete 2-hour workshop curriculum designed for university students (mixed experience levels) to learn practical prompt engineering and build portfolio-ready AI applications.

## 🎯 What You'll Build

By the end of this workshop, students will have created:

1. **Prompt Template Library** - Reusable, optimized prompts for common tasks
2. **Context-Aware AI Assistant** - A chatbot that remembers conversation history
3. **RAG Mini-System** - An AI that answers questions grounded in custom knowledge bases

## 📁 Workshop Files

```
├── CURRICULUM.md                      # Complete workshop curriculum for instructors
├── workshop_starter.py                # Starter code with TODOs for students
├── requirements.txt                   # Python dependencies
├── .env.example                       # API key configuration template
├── sample_knowledge_base.txt          # Sample data for RAG testing
└── WORKSHOP_README.md                 # This file
```

## 🚀 Quick Start for Students

### Prerequisites
- Python 3.8 or higher
- Basic Python knowledge (functions, loops, dictionaries)
- An API key from OpenAI or Anthropic (free tier available)

### Setup (5 minutes)

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your API key
   # OpenAI: https://platform.openai.com/api-keys
   # Anthropic: https://console.anthropic.com/
   ```

3. **Test your setup**
   ```bash
   python workshop_starter.py
   ```

## 👨‍🏫 For Instructors

Review `CURRICULUM.md` for:
- Complete 2-hour session timeline (40% theory / 60% hands-on)
- Teaching approaches for each section
- Discussion questions and engagement strategies
- Resource fallback plans for technical issues
- Common pitfalls and timing tips

## 🎓 Learning Objectives

Students will be able to:
1. Structure effective prompts with clear instructions and context
2. Implement conversation context management
3. Build RAG systems that ground AI responses in custom data

## 💼 Portfolio Tips

- Create GitHub repository with demo GIFs
- Add "Lessons Learned" section
- Extend with web interface (Streamlit/Gradio)
- Implement semantic search with embeddings
- Create specialized assistants (Code Review Bot, Study Buddy)

## 🛠️ Technical Stack

- **Python 3.8+** - Core language
- **OpenAI API** or **Anthropic API** - LLM providers
- **python-dotenv** - Environment management

## 🔧 Troubleshooting

### API Key Issues
```python
# Verify .env file format
OPENAI_API_KEY=sk-...  # No quotes, no spaces

# Test loading
from dotenv import load_dotenv
import os
load_dotenv()
print(os.getenv("OPENAI_API_KEY"))
```

### Import Errors
```bash
pip install -r requirements.txt --upgrade
```

## 📖 Resources

- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Prompt Library](https://docs.anthropic.com/claude/prompt-library)
- [LangChain Documentation](https://python.langchain.com/)

## 🎯 Success Metrics

Students should be able to:
- [ ] Explain what makes a good prompt
- [ ] Write prompt templates with variable substitution
- [ ] Make successful API calls to an LLM
- [ ] Implement conversation history
- [ ] Describe how RAG works
- [ ] Have working portfolio code

---

**Duration:** 2 hours | **Audience:** Mixed experience | **Format:** Code-first, hands-on
