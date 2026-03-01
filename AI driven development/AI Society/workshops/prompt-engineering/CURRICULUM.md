# Mastering Prompt and Context Engineering: Building Intelligent AI Applications

## Workshop Overview
- **Duration**: 2 hours
- **Target Audience**: Mixed (All years) - Students with basic Python knowledge, varying AI/ML experience
- **Difficulty Level**: Beginner to Intermediate
- **Format**: Code-first, hands-on workshop with minimal slides

## Learning Objectives
By the end of this workshop, students will be able to:
1. **Build a Context-Aware AI Assistant** that maintains conversation history and adapts responses based on user context
2. **Create a Prompt Template Library** with reusable, optimized prompts for common tasks (summarization, code generation, data extraction)
3. **Implement a RAG (Retrieval-Augmented Generation) Mini-System** that grounds AI responses in custom knowledge bases

## Prerequisites

### Required Knowledge
- Basic Python programming (functions, loops, dictionaries)
- Familiarity with APIs and JSON (helpful but not required)
- Understanding of what LLMs are (we'll cover the basics)

### Required Software & Libraries
```bash
# Python 3.8 or higher
python --version

# Required libraries
pip install openai anthropic python-dotenv requests

# Optional (for advanced features)
pip install tiktoken chromadb sentence-transformers
```

### API Keys (Choose ONE)
- **OpenAI API Key** (recommended for beginners): https://platform.openai.com/api-keys
- **Anthropic API Key** (Claude): https://console.anthropic.com/
- **Free tier credits available for both**

### Pre-Workshop Setup
1. Install Python 3.8+ and pip
2. Create a project folder: `mkdir prompt-engineering-workshop && cd prompt-engineering-workshop`
3. Install required libraries (see above)
4. Get your API key and save it in a `.env` file:
   ```
   OPENAI_API_KEY=your_key_here
   # OR
   ANTHROPIC_API_KEY=your_key_here
   ```
5. Download the starter code (provided separately)

## Session Timeline

### Part 1: Foundations of Prompt Engineering (Theory - 20 minutes)

**Topics Covered:**
- What is prompt engineering? Why does it matter?
- The anatomy of a good prompt: instruction, context, examples, constraints
- Common pitfalls: vague prompts, missing context, over-prompting
- Live demo: Same task, different prompts, wildly different results

**Teaching Approach:**
- **5 minutes**: Quick intro (3 slides max)
- **15 minutes**: Live coding demo showing prompt evolution
  - Start with bad prompt → show output
  - Improve iteratively → show improvements
  - Students follow along in their IDE

**Key Takeaway:** Prompts are code. Treat them with the same rigor as your Python functions.

### Part 2: Hands-On - Building Your First Prompt System (Hands-on - 25 minutes)

**Activity: Create a Prompt Template Library**

Students will code:
1. A `PromptTemplate` class that handles variable substitution
2. Three reusable templates:
   - Code explainer (takes code snippet → returns explanation)
   - Meeting summarizer (takes transcript → returns action items)
   - Data extractor (takes unstructured text → returns JSON)
3. Test each template with real examples

**What students will code:**
- Template class with `.format()` method
- Validation for required variables
- API call wrapper function
- Error handling for API failures

**Instructor circulates to help with:**
- API key setup issues
- Understanding template syntax
- Debugging API responses

### Part 3: Context Engineering - Making AI Remember (Theory - 10 minutes)

**Topics Covered:**
- Why context matters: stateless vs. stateful interactions
- Context window limits and token management
- Strategies: conversation history, system prompts, few-shot examples
- Live demo: Chatbot with vs. without context

**Teaching Approach:**
- **3 minutes**: Explain context windows (1 slide)
- **7 minutes**: Live code a simple chatbot
  - Version 1: No memory (each message is isolated)
  - Version 2: With conversation history
  - Show how responses improve dramatically

### Part 4: Hands-On - Context-Aware Assistant (Hands-on - 35 minutes)

**Activity: Build a Personal Study Assistant**

Students will build an AI assistant that:
- Maintains conversation history across multiple turns
- Has a system prompt defining its role (helpful tutor, Socratic method)
- Adapts responses based on user's stated learning level
- Tracks token usage to avoid context window overflow

**Implementation Steps:**
1. Create `ConversationManager` class to store message history
2. Implement `add_message()` and `get_context()` methods
3. Add system prompt configuration
4. Build interactive chat loop
5. Add token counting and context pruning
6. Test with multi-turn conversations

**Stretch Goals (for fast learners):**
- Add conversation summarization when context gets too long
- Implement different "personas" (tutor, code reviewer, brainstorm partner)
- Save/load conversation history to JSON file

### Part 5: Advanced - RAG Mini-System (Hands-on - 25 minutes)

**Activity: Ground AI in Your Own Knowledge Base**

Students will create a simple RAG system:
- Load a custom knowledge base (course notes, documentation, etc.)
- Split text into chunks
- Implement basic semantic search (keyword matching or embeddings)
- Retrieve relevant chunks and inject into prompt context
- Query the system with questions

**What students will code:**
- `KnowledgeBase` class with `.add_document()` method
- Simple chunking function (split by paragraphs or sentences)
- Search function (keyword-based for simplicity, embeddings optional)
- RAG query pipeline: search → retrieve → augment prompt → generate

**Minimum Viable Version:**
- Use simple string matching for retrieval
- 3-5 document chunks in knowledge base
- Basic prompt: "Based on this context: {chunks}, answer: {question}"

**Advanced Version (optional):**
- Use sentence-transformers for semantic search
- Implement relevance scoring
- Add citation tracking (which chunks were used)

### Part 6: Wrap-Up & Portfolio Tips (Theory - 5 minutes)

- Quick recap of what we built
- How to showcase these projects
- Next steps and resources

## Hands-On Project: AI-Powered Study Assistant with Custom Knowledge

### Project Description
Students will build a complete AI assistant that combines all three learning objectives:
1. Uses prompt templates for consistent, high-quality responses
2. Maintains conversation context for natural multi-turn interactions
3. Grounds responses in a custom knowledge base (e.g., course materials, research papers)

**Final Deliverable:** A Python application that can:
- Answer questions about custom documents
- Remember conversation history
- Provide citations/sources for its answers
- Handle errors gracefully (API failures, missing context)

### Portfolio Enhancement Tips

**How to Showcase This Project:**
1. **GitHub Repository Structure:**
   ```
   prompt-engineering-assistant/
   ├── README.md (with demo GIF/screenshots)
   ├── src/
   │   ├── prompt_templates.py
   │   ├── conversation_manager.py
   │   ├── knowledge_base.py
   │   └── main.py
   ├── examples/
   │   ├── sample_conversation.txt
   │   └── sample_knowledge_base/
   ├── requirements.txt
   └── .env.example
   ```

2. **README Must Include:**
   - Clear problem statement: "Why did I build this?"
   - Architecture diagram (simple flowchart)
   - Usage examples with actual outputs
   - Lessons learned section

3. **Suggested Extensions for Portfolio:**
   - Add a web interface (Streamlit or Gradio)
   - Implement conversation export (PDF/Markdown)
   - Add multi-modal support (upload PDFs, images)
   - Create a Chrome extension that uses your prompt templates
   - Build a specialized assistant (e.g., "Code Review Bot", "Research Paper Summarizer")

4. **Talking Points for Interviews:**
   - "I built this to solve [specific problem]"
   - "I learned about token management and context window optimization"
   - "I implemented RAG before it became mainstream"
   - "This project taught me prompt engineering is software engineering"

## Discussion Questions

### Question 1: Real-World Applications
"You're building a customer support chatbot for an e-commerce company. The bot needs to access order history, product catalogs, and return policies. How would you design the context and prompt strategy? What are the risks of getting it wrong?"

**Discussion Goals:**
- Connect RAG to real business problems
- Think about data privacy and security
- Consider edge cases (outdated info, conflicting policies)

### Question 2: Ethical Considerations
"Your AI assistant sometimes 'hallucinates' facts when it doesn't know the answer. As a developer, what strategies can you implement to minimize this? When is it acceptable to say 'I don't know' vs. trying to generate an answer?"

**Discussion Goals:**
- Understand limitations of LLMs
- Think about responsible AI development
- Discuss prompt engineering techniques for reducing hallucinations

### Question 3: Future of Prompt Engineering
"Some argue that as models get better, prompt engineering will become obsolete. Others say it's a fundamental skill like SQL or regex. What's your take? How would you future-proof your prompt engineering skills?"

**Discussion Goals:**
- Think critically about AI trends
- Understand transferable skills (structured thinking, API design)
- Discuss career implications

## Resource Fallback Plan

### Scenario 1: Internet Connectivity Issues

**Fallback Actions:**
- Switch to local LLM (if available): Ollama with Llama 3 or Mistral
- Use pre-recorded API responses (JSON files with sample outputs)
- Focus on prompt design and template creation (no actual API calls)

**Pre-Downloaded Resources Needed:**
- Sample API response JSON files (5-10 examples)
- Ollama installation guide (offline PDF)
- Pre-configured Docker container with local LLM

**Modified Workshop Flow:**
- Skip live API demos
- Use "mock" API functions that return pre-defined responses
- Focus on prompt structure and code architecture
- Students can test with real APIs at home

### Scenario 2: API Key / Credit Issues

**Fallback Actions:**
- Instructor shares their API key (with rate limiting)
- Use free alternatives: HuggingFace Inference API, Cohere trial
- Pair programming: 2 students per API key
- Mock API mode (see Scenario 1)

**Prevention:**
- Send API setup instructions 24 hours before workshop
- Have 2-3 backup API keys ready
- Test all keys 1 hour before workshop

### Scenario 3: Library Installation Problems

**Docker Container Option:**
```bash
# Pre-built container with all dependencies
docker pull [instructor-username]/prompt-workshop:latest
docker run -it -p 8888:8888 prompt-workshop
```

**Alternative Setup:**
- Google Colab notebook (no local installation needed)
- Replit template (browser-based IDE)
- USB drives with pre-installed Python environment (Anaconda)

**Backup Plan:**
- Have 3 laptops with working setups ready to lend
- Screen share from instructor's machine, students code along

### Scenario 4: Time Constraints

**Shortened Version (90 minutes):**
1. **Part 1 + 2**: Prompt templates only (45 min)
2. **Part 3 + 4**: Context-aware assistant (40 min)
3. **Wrap-up**: Skip RAG, provide as take-home exercise (5 min)

**Priority Order:**
1. **Must Cover**: Prompt templates and basic API usage
2. **Should Cover**: Conversation context management
3. **Nice to Have**: RAG system (can be homework)

**Time-Saving Strategies:**
- Pre-fill more starter code
- Skip some live coding, show pre-recorded demos
- Reduce discussion time, focus on coding
- Provide completed code for students to study later

## Additional Resources

### Documentation & Guides
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Prompt Library](https://docs.anthropic.com/claude/prompt-library)
- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction) (for advanced RAG)
- [Prompt Engineering Guide (GitHub)](https://github.com/dair-ai/Prompt-Engineering-Guide)

### Practice Datasets & Examples
- **For Summarization**: Meeting transcripts, news articles
- **For Code Generation**: LeetCode problems, GitHub issues
- **For RAG**: Course lecture notes, research paper abstracts, company documentation

### Tools & Platforms
- **Prompt Testing**: PromptPerfect, PromptBase
- **Token Counting**: tiktoken (OpenAI), Anthropic tokenizer
- **Vector Databases**: ChromaDB, Pinecone, Weaviate
- **UI Frameworks**: Streamlit, Gradio, Chainlit

### Further Learning
- **Course**: DeepLearning.AI - "ChatGPT Prompt Engineering for Developers"
- **Book**: "The Prompt Engineering Handbook" (free online)
- **Community**: r/PromptEngineering, LangChain Discord
- **Practice**: Daily prompt challenges on Twitter/X (#PromptEngineering)

## Instructor Notes

### Common Pitfalls to Watch For

1. **API Key Issues** (80% of problems)
   - Students forget to create `.env` file
   - Copy-paste errors with API keys (extra spaces, quotes)
   - Wrong environment variable names
   - **Solution**: Have a "API Key Debugging Checklist" slide

2. **Indentation Errors** (Python beginners)
   - Especially in multi-line strings and f-strings
   - **Solution**: Provide formatted starter code, use linter

3. **Token Limit Confusion**
   - Students don't understand why their long prompts fail
   - **Solution**: Show token counter early, visualize limits

4. **Expecting Perfect Outputs**
   - Frustration when AI doesn't do exactly what they want
   - **Solution**: Set expectations early - iteration is normal

5. **Copy-Pasting Without Understanding**
   - Students rush through to "finish" without learning
   - **Solution**: Ask comprehension questions, require explanations

### Timing Tips

- **Buffer Time**: Build in 10 minutes of slack for Q&A and debugging
- **Checkpoints**: After each hands-on section, do a quick "everyone caught up?" poll
- **Fast Learners**: Have stretch goals ready (see each section)
- **Slow Learners**: Pair them with faster students, provide simplified versions

### Engagement Strategies

1. **Live Polls**: "What would you use this for?" (show of hands)
2. **Pair Programming**: Rotate pairs every 20 minutes
3. **Show & Tell**: Ask 2-3 students to share their prompts/results
4. **Real-Time Debugging**: When someone hits an error, debug it live (learning opportunity)
5. **Gamification**: "Who can write the shortest prompt that still works?"

### Energy Management

- **Hour 1**: High energy, lots of demos, quick wins
- **Hour 2**: More independent work, circulate to help, keep momentum
- **Avoid**: Long lectures, reading slides, passive watching

### Success Metrics

By the end, students should be able to:
- [ ] Explain what makes a good prompt (structure, clarity, examples)
- [ ] Write a prompt template with variable substitution
- [ ] Make successful API calls to an LLM
- [ ] Implement conversation history in a chatbot
- [ ] Describe how RAG works (even if implementation is incomplete)
- [ ] Have working code they can show in their portfolio

### Post-Workshop Follow-Up

- Share completed code repository
- Create a Discord/Slack channel for continued learning
- Offer office hours for project extensions
- Encourage students to share their portfolio projects
- Collect feedback: "What worked? What didn't?"
