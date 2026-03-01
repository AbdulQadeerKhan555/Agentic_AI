# AI Driven Development

A comprehensive collection of resources, tools, and workflows for **building AI agents using AI-assisted development**. This repository focuses on leveraging AI coding assistants (Claude Code, Cursor, etc.) to accelerate agent development, create custom skills, and manage knowledge effectively.

## Overview

This project demonstrates modern AI-driven development practices, including:
- **Claude Code Skills**: Custom capabilities that extend AI assistant functionality
- **Knowledge Management**: Organized research, notes, and reference materials
- **Hands-on MCP Tools**: Model Context Protocol implementations for real-world tasks
- **Study Systems**: Structured learning materials for AI agent development
- **Workshops**: Educational content for prompt engineering and AI workshops

## Directory Structure

```
AI driven development/
├── AI Society/                          # AI workshops and educational content
│   ├── workshops/
│   │   └── prompt-engineering/          # Prompt engineering workshop materials
│   ├── .claude/skills/                  # AI Society custom skills
│   └── README.md
│
├── markdown/                            # Blog posts and markdown content
│   ├── Blogs/
│   │   └── first-post.md
│   └── .claude/skill/blog-post/
│
├── MCP_handsOn/                         # Model Context Protocol implementations
│   ├── claude-code-skills-lab-main/     # Comprehensive skills laboratory
│   │   ├── .claude/skills/              # 13+ production-grade skills
│   │   │   ├── browsing-with-playwright/
│   │   │   ├── fetch-library-docs/
│   │   │   ├── doc-coauthoring/
│   │   │   ├── docx/
│   │   │   ├── pdf/
│   │   │   ├── pptx/
│   │   │   ├── xlsx/
│   │   │   ├── skill-creator-pro/
│   │   │   ├── skill-validator/
│   │   │   ├── theme-factory/
│   │   │   ├── interview/
│   │   │   └── internal-comms/
│   │   └── README.md
│   ├── .playwright-mcp/                 # Playwright screenshots and tests
│   └── playwright-tasks.js
│
├── personal knowledge_base & research assistance/
│   ├── .claude/
│   │   ├── agents/                      # Custom agent definitions
│   │   │   ├── curator.md
│   │   │   ├── librarian.md
│   │   │   └── researcher.md
│   │   └── skills/                      # Knowledge management skills
│   │       ├── summarize-pdf/
│   │       ├── create-topic-index/
│   │       ├── link-related-notes/
│   │       └── skill-maker/
│   ├── knowledge/                       # Research notes and summaries
│   ├── AGENT.md                         # Academic standards
│   ├── CLAUDE.md                        # Workflow guidelines
│   └── README.md
│
├── personal skills/                     # Personal development resources
│   ├── crypto-trading-strategy.md
│   ├── crypto_trading_journal.csv
│   ├── real-time-data-guide.md
│   └── README.md
│
└── study_system/                        # Educational content management
    ├── .claude/skills/
    │   ├── notes-generator/             # Generate structured study notes
    │   └── skill-maker/
    ├── notes/                           # Study notes (LLM, AI topics)
    ├── flashcards/                      # Spaced repetition materials
    ├── quizes/                          # Assessment materials
    ├── CLAUDE.md
    └── README.md
```

## Core Components

### 1. AI Society - Workshops & Education

Educational materials for learning AI agent development and prompt engineering.

**Contents:**
- Prompt engineering workshops
- AI agent curriculum
- Hands-on exercises
- Sample knowledge bases

**Getting Started:**
```bash
cd "AI Society/workshops/prompt-engineering"
python workshop_starter.py
```

---

### 2. MCP Hands-On - Model Context Protocol

Production-grade skills that extend Claude Code with specialized capabilities.

#### Available Skills

| Skill | Type | Purpose |
|-------|------|---------|
| **browsing-with-playwright** | Automation | Web browsing, form filling, screenshots, data extraction |
| **fetch-library-docs** | Builder | Token-efficient documentation fetcher for programming libraries |
| **doc-coauthoring** | Guide | Structured documentation co-authoring workflow |
| **docx** | Builder | Word document creation, editing, tracked changes |
| **pdf** | Builder | PDF extraction, merging, splitting, form handling |
| **pptx** | Builder | PowerPoint creation, editing, design |
| **xlsx** | Builder | Spreadsheet creation, formulas, data analysis |
| **skill-creator-pro** | Guide | Production-grade skill creation with 5 patterns |
| **skill-validator** | Validator | Quality validation with 0-100 scoring |
| **theme-factory** | Automation | Styling toolkit with 10 professional themes |
| **interview** | Guide | Discovery conversations to understand user intent |
| **internal-comms** | Builder | Internal communications writing assistance |

**Skill Categories:**
- **Builder**: Creates or modifies artifacts (code, docs, spreadsheets)
- **Guide**: Leads users through structured workflows
- **Automation**: Performs repetitive tasks automatically
- **Analyzer**: Examines and provides insights
- **Validator**: Checks quality against standards

---

### 3. Personal Knowledge Base & Research Assistance

AI-powered research management system for academic work.

**Features:**
- Automated PDF summarization
- Topic indexing and categorization
- Intelligent document linking
- Academic standards enforcement
- Custom agent workflows

**Agents:**
- **Curator**: Manages knowledge quality and organization
- **Librarian**: Handles indexing and categorization
- **Researcher**: Performs literature review and analysis

**Skills:**
```bash
/summarize-pdf path/to/paper.pdf
/create-topic-index machine_learning
/link-related-notes knowledge/note.md
```

---

### 4. Study System

Structured educational content management for learning AI/ML topics.

**Components:**
- **Notes Generator**: Creates structured study notes from source materials
- **Flashcards**: Spaced repetition materials
- **Quizzes**: Assessment and self-testing
- **Skill Maker**: Create custom study skills

**Workflow:**
1. Generate notes from lectures/papers
2. Create flashcards for key concepts
3. Take quizzes to test understanding
4. Track progress over time

---

### 5. Markdown & Blogging

Content creation workflows for technical writing.

**Features:**
- Blog post templates
- Skill-based content generation
- Markdown best practices
- Publishing workflows

---

### 6. Personal Skills

Domain-specific knowledge and guides.

**Contents:**
- Cryptocurrency trading strategies
- Trading journal templates
- Real-time data handling guides
- Technical analysis resources

## Quick Start Guide

### 1. Set Up Claude Code

Install Claude Code CLI:

```bash
npm install -g @anthropic-ai/claude-code
```

### 2. Explore Skills

Navigate to any skills folder:

```bash
cd "MCP_handsOn/claude-code-skills-lab-main/.claude/skills/browsing-with-playwright"
cat SKILL.md
```

### 3. Use a Skill

In Claude Code, skills are automatically available:

```
/summarize-pdf my-research-paper.pdf
```

### 4. Create Custom Skills

Use the skill-maker:

```
Create a skill that analyzes stock market trends and generates trading signals
```

## Skill Development Workflow

### Creating a New Skill

1. **Define Purpose**: What problem does it solve?
2. **Choose Type**: Builder, Guide, Automation, Analyzer, or Validator
3. **Write SKILL.md**: Follow the standard format
4. **Add References**: Include documentation and examples
5. **Create Scripts**: Add helper scripts if needed
6. **Test**: Validate with real use cases
7. **Package**: Ensure proper structure for distribution

### Skill Structure

```
skill-name/
├── SKILL.md              # Main skill definition
├── references/           # Supporting documentation
│   ├── patterns.md
│   └── examples.md
├── scripts/              # Helper scripts
│   ├── start-server.sh
│   └── mcp-client.py
└── examples/             # Usage examples
```

## Best Practices

### 1. Knowledge Management

- **Consistent Naming**: Use `YYYY-MM-DD_topic` for notes
- **Tagging System**: Apply `#topic #category` tags
- **Regular Reviews**: Update indices monthly
- **Link Related Content**: Use automated linking

### 2. Skill Creation

- **Single Purpose**: Each skill should do one thing well
- **Clear Instructions**: Write explicit, unambiguous guidance
- **Safety First**: Restrict dangerous operations
- **Test Thoroughly**: Validate with edge cases

### 3. Agent Development

- **Define Clear Roles**: Each agent has a specific purpose
- **Use MCP Tools**: Leverage Model Context Protocol
- **Monitor Performance**: Track token usage and latency
- **Iterate**: Continuously improve based on feedback

### 4. Academic Standards

- **Formal Tone**: Maintain scholarly communication
- **Evidence-Based**: Ground assertions in verifiable sources
- **Proper Citations**: Acknowledge all sources
- **Critical Analysis**: Question assumptions and conclusions

## Learning Resources

### Documentation
- [Claude Code Features and Workflows](https://ai-native.panaversity.org/docs/AI-Tool-Landscape/claude-code-features-and-workflows)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Skills Documentation](https://docs.anthropic.com/claude-code/skills)

### Related Projects
- [Agentic AI Python Projects](../Agentic_AI_Python_Projects/) - Python agent development
- [N8N](../N8N/) - Workflow automation

## Troubleshooting

### Skills Not Loading
```
Solution: Verify SKILL.md exists and has valid YAML frontmatter
```

### PDF Summarization Fails
```
Solution: Check file path, permissions, and PDF validity
```

### MCP Connection Issues
```
Solution: Restart MCP server, verify configuration
```

## Contributing

1. Fork the repository
2. Create a skill or add educational content
3. Follow existing structure and standards
4. Document thoroughly
5. Submit a pull request

## License

MIT License - See individual folders for details

## Author

**Abdul Qadeer Khan**

GitHub: [@AbdulQadeerKhan555](https://github.com/AbdulQadeerKhan555)

---

**Last Updated**: March 2026
**Primary Tools**: Claude Code, MCP, Custom Skills
**Focus**: AI-Assisted Agent Development
