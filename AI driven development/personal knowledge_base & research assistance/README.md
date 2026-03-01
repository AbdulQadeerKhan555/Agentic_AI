# Personal Knowledge Base & Research Assistance System

An AI-powered research management system designed for academic work, featuring automated PDF summarization, topic indexing, and intelligent document linking with consistent academic standards.

## Overview

This system provides a structured workflow for managing research materials, creating summaries, organizing notes, and discovering connections between documents. All operations follow academic standards defined in `AGENT.md` and organizational workflows specified in `CLAUDE.md`.

## Directory Structure

```
.
├── AGENT.md                    # Academic tone and standards
├── CLAUDE.md                   # Workflow and organization guidelines
├── README.md                   # This file
├── .claude/
│   └── skills/                 # Custom Claude Code skills
│       ├── skill-maker/        # Generate new skills
│       ├── summarize-pdf/      # Extract and summarize PDFs
│       ├── create-topic-index/ # Generate topic indices
│       └── link-related-notes/ # Find document connections
├── knowledge/                  # Research notes and summaries
├── sources/                    # Original source materials
├── templates/                  # Document templates
└── references/                 # Reference materials
```

## Core Configuration

### AGENT.md - Academic Standards

Defines the foundational academic tone and operational guidelines:
- Formal, scholarly communication
- Evidence-based reasoning
- File preservation protocols
- Naming conventions for research materials

### CLAUDE.md - Workflow Standards

Specifies organizational workflows:
- Research notes storage: `/knowledge/` with `YYYY-MM-DD` prefix
- Key takeaways extraction: 3-5 per document
- Tagging format: `#topic #category`
- Integration with academic standards

## Available Skills

### 1. summarize-pdf

Extract and summarize PDF content following academic standards.

**Usage:**
```bash
/summarize-pdf path/to/paper.pdf
/summarize-pdf https://example.com/paper.pdf
```

**Features:**
- Auto-detects local files and URLs
- Extracts bibliographic information
- Generates 3-5 key takeaways
- Applies proper tags (#topic #category)
- Saves to `/knowledge/YYYY-MM-DD_author_year_topic.md`
- Follows academic tone from AGENT.md

**Output Structure:**
- Bibliographic information
- Overview and research question
- Key takeaways (3-5 points)
- Methodology and findings
- Conclusions and implications
- Proper metadata and tags

### 2. create-topic-index

Generate an index of all notes on a specific topic.

**Usage:**
```bash
/create-topic-index machine_learning
/create-topic-index #neuroscience
```

**Features:**
- Searches by tags (#topic format)
- Extracts key takeaways from each note
- Organizes chronologically
- Identifies related topics
- Saves to `/knowledge/YYYY-MM-DD_index_[topic].md`

**Output Includes:**
- Summary statistics (total notes, date range)
- File paths and dates
- Key takeaways from each note
- Tag analysis
- Related topics

### 3. link-related-notes

Find and link related documents by analyzing connections.

**Usage:**
```bash
/link-related-notes knowledge/2024-01-24_paper_summary.md
```

**Features:**
- Analyzes shared tags
- Identifies content similarity
- Finds shared citations
- Ranks by relevance score
- Updates document with Related Materials section

**Connection Methods:**
- Shared tags (high priority)
- Content similarity (medium priority)
- Shared citations (high priority)
- Temporal proximity

### 4. skill-maker

Generate new Claude Code skills following official standards.

**Usage:**
Describe the skill you want to create, and skill-maker will:
1. Analyze requirements
2. Ask clarifying questions
3. Generate properly formatted SKILL.md
4. Ensure quality and consistency

**Features:**
- Follows Claude Code standards
- Asks questions to fill gaps
- Generates YAML frontmatter
- Creates supporting files if needed
- Integrates with project standards

## Workflow

### 1. Adding Research Materials

**Summarize a PDF:**
```bash
/summarize-pdf papers/smith_2024_ml_review.pdf
```

This automatically:
- Extracts content and metadata
- Generates academic summary
- Creates 3-5 key takeaways
- Applies proper tags
- Saves to `/knowledge/2024-01-24_smith_2024_ml_review.md`

### 2. Organizing by Topic

**Create a topic index:**
```bash
/create-topic-index machine_learning
```

This generates an index showing:
- All notes with #machine_learning tag
- Key takeaways from each
- Chronological organization
- Related topics

### 3. Discovering Connections

**Link related documents:**
```bash
/link-related-notes knowledge/2024-01-24_smith_2024_ml_review.md
```

This analyzes the document and:
- Finds related notes by tags, content, citations
- Ranks by relevance
- Adds Related Materials section
- Preserves original content

### 4. Creating Custom Skills

Describe a new skill you need, and the system will generate it following proper standards.

## File Naming Conventions

### Research Notes
```
YYYY-MM-DD_topic_description.md
2024-01-24_machine_learning_fundamentals.md
```

### Research Papers
```
author_year_title.pdf
smith_2024_neural_networks.pdf
```

### Topic Indices
```
YYYY-MM-DD_index_topic.md
2024-01-24_index_machine_learning.md
```

## Metadata Format

All documents in `/knowledge/` use this frontmatter:

```yaml
---
tags: #topic #category #descriptors
date: YYYY-MM-DD
type: [note|summary|analysis|literature_review|reference|topic_index]
source: [citation if applicable]
---
```

## Tagging System

### Tag Structure
- **#topic**: Subject matter (#machine_learning, #neuroscience)
- **#category**: Content type (#methodology, #theory, #empirical_study)
- **Additional**: Supplementary tags (#quantitative, #interdisciplinary)

### Best Practices
- Use 3-7 tags per document
- Balance specific and general tags
- Maintain consistency across documents
- Use lowercase with underscores

## Academic Standards

All content follows academic standards from `AGENT.md`:

### Tone
- Formal, scholarly language
- Objective presentation
- Precise terminology
- Evidence-based reasoning

### Structure
- Clear hierarchical organization
- Logical flow of information
- Proper citations and attribution
- Systematic presentation

### Quality
- Intellectual rigor
- Critical analysis
- Completeness
- Clarity

## Key Features

### 1. Automated Summarization
- PDF content extraction
- Structured academic summaries
- Consistent formatting
- Proper metadata

### 2. Intelligent Organization
- Tag-based categorization
- Date-prefixed filenames
- Topic indices
- Related materials linking

### 3. Connection Discovery
- Shared tag analysis
- Content similarity detection
- Citation tracking
- Relevance scoring

### 4. Extensibility
- skill-maker for custom workflows
- Template-based generation
- Standards compliance
- Modular architecture

## Getting Started

### 1. Summarize Your First PDF
```bash
/summarize-pdf path/to/your/paper.pdf
```

### 2. Review the Generated Summary
Check `/knowledge/` for the new summary file with:
- Proper naming (date prefix)
- Academic formatting
- Key takeaways
- Metadata and tags

### 3. Build Your Knowledge Base
Continue adding summaries, and the system will:
- Maintain consistent formatting
- Apply proper tags
- Enable topic indexing
- Support connection discovery

### 4. Organize by Topics
```bash
/create-topic-index your_topic
```

### 5. Discover Connections
```bash
/link-related-notes knowledge/your_note.md
```

## Best Practices

### File Management
- Never delete original sources (per AGENT.md)
- Always use date prefixes for notes
- Store originals in `/sources/`
- Keep summaries in `/knowledge/`

### Tagging
- Apply tags consistently
- Use established tags when possible
- Create new tags judiciously
- Include both topic and category tags

### Summaries
- Always extract 3-5 key takeaways
- Maintain academic tone
- Include proper citations
- Use structured format

### Organization
- Generate topic indices regularly
- Link related notes
- Update indices when adding content
- Review connections periodically

## Extending the System

### Creating New Skills

Describe what you need:
```
"Create a skill for [purpose] that [functionality]"
```

The skill-maker will:
1. Ask clarifying questions
2. Generate proper SKILL.md
3. Follow Claude Code standards
4. Integrate with project standards

### Example Custom Skills
- Literature review compilation
- Citation management
- Export to different formats
- Automated backups
- Search and query tools

## Technical Details

### Skills Location
`.claude/skills/[skill-name]/SKILL.md`

### Skill Structure
- YAML frontmatter with metadata
- Markdown instructions
- Integration with project standards
- Tool restrictions for safety

### File Operations
- Read: Access files
- Write: Create new files
- Edit: Modify existing files
- Grep/Glob: Search operations

## Troubleshooting

### PDF Summarization Issues
- Verify file path is correct
- Ensure PDF is readable
- Check file permissions
- Confirm PDF is not corrupted

### Index Generation Issues
- Verify tag format (#topic)
- Check `/knowledge/` directory exists
- Ensure notes have proper frontmatter
- Confirm tags are in metadata

### Linking Issues
- Verify file path is correct
- Ensure document has tags
- Check for malformed frontmatter
- Confirm related notes exist

## Future Enhancements

Potential additions to the system:
- Bidirectional linking automation
- Visual knowledge graph generation
- Advanced search capabilities
- Export to various formats
- Integration with reference managers
- Automated literature review compilation

---

**System Version**: 1.0
**Last Updated**: 2024-01-24
**Maintained by**: Claude Code with academic standards

*This system follows academic standards from AGENT.md and organizational workflows from CLAUDE.md.*
