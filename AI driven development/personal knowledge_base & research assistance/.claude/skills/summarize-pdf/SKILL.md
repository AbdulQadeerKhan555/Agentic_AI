---
name: summarize-pdf
description: Extract and summarize PDF content following academic standards. Use when the user asks to summarize a PDF, analyze a research paper, or extract key findings from documents.
disable-model-invocation: false
user-invocable: true
argument-hint: [file-path-or-url]
allowed-tools: Read, Write, WebFetch
---

# Summarize PDF

Extract and summarize PDF content following academic standards defined in `@AGENT.md` and organizational workflows from `@CLAUDE.md`.

## Instructions

### Step 1: Input Detection and Acquisition

Analyze the input provided in $ARGUMENTS:

1. **Local File Path**: If $ARGUMENTS is a file path ending in `.pdf`
   - Use Read tool to access the PDF content
   - PDF files are processed page by page with text and visual content extraction

2. **Web URL**: If $ARGUMENTS starts with `http://` or `https://`
   - Use WebFetch tool to retrieve the PDF content
   - Process the fetched content

3. **Directory Path**: If $ARGUMENTS is a directory
   - List PDF files in the directory
   - Ask user which PDF to summarize or process all

4. **No Extension**: If path lacks `.pdf` extension
   - Check if file exists with `.pdf` appended
   - Verify file accessibility before proceeding

### Step 2: Content Extraction

1. Read the PDF file using the Read tool
2. Extract the following information:
   - Title and authors
   - Publication details (journal, year, DOI)
   - Abstract or executive summary
   - Main sections and headings
   - Key findings and conclusions
   - Figures, tables, and their captions
   - References and citations

### Step 3: Analysis and Summarization

Following academic standards from `@AGENT.md`:

1. **Identify Core Content**:
   - Research question or thesis
   - Methodology or approach
   - Main arguments and evidence
   - Results and findings
   - Conclusions and implications

2. **Extract Key Takeaways** (as specified in `@CLAUDE.md`):
   - Identify 3-5 most significant insights
   - Focus on substantive contributions
   - Express as clear, standalone statements
   - Ensure completeness of document's value

3. **Maintain Academic Tone**:
   - Use formal, scholarly language
   - Employ precise terminology
   - Present information objectively
   - Support statements with evidence from the document
   - Use appropriate transitional phrases

### Step 4: Generate Structured Summary

Create a comprehensive summary with the following structure:

```markdown
---
tags: #topic #category #research_type
date: YYYY-MM-DD
type: literature_review
source: [Full citation]
---

# [Document Title]

## Bibliographic Information

- **Authors**: [Author names]
- **Year**: [Publication year]
- **Publication**: [Journal/Conference/Publisher]
- **DOI**: [DOI if available]
- **URL**: [URL if applicable]

## Overview

[Brief context: What is this document about? What problem does it address?]

## Key Takeaways

1. [First major insight or finding]
2. [Second major insight or finding]
3. [Third major insight or finding]
4. [Fourth insight - if applicable]
5. [Fifth insight - if applicable]

## Research Question/Objective

[What question or problem does this research address?]

## Methodology

[Approach, methods, or framework used]

## Main Findings

[Detailed summary of results and discoveries]

## Conclusions

[Author's conclusions and interpretations]

## Implications

[Significance, applications, and broader impact]

## Limitations

[Acknowledged limitations or constraints]

## Related Work

[Connections to other research or relevant context]

## Notable Figures/Tables

[Key visual elements and their significance]

## References

[Important citations or related works mentioned]
```

### Step 5: Metadata and Tagging

Apply consistent tagging format as specified in `@CLAUDE.md`:

1. **#topic**: Subject matter or domain
   - Examples: #machine_learning #climate_science #neuroscience #economics

2. **#category**: Type or nature of content
   - Examples: #methodology #theory #empirical_study #review #meta_analysis

3. **Additional descriptors**: Supplementary tags
   - Examples: #quantitative #qualitative #interdisciplinary #foundational

4. **Date**: Use current date in YYYY-MM-DD format

5. **Type**: Specify document type (literature_review, research_summary, analysis)

6. **Source**: Full bibliographic citation

### Step 6: Save to Knowledge Base

Following `@CLAUDE.md` workflow standards:

1. **File Naming**: Use format `YYYY-MM-DD_author_year_topic.md`
   - Example: `2024-01-24_smith_2024_neural_networks.md`
   - Use first author's last name
   - Include publication year
   - Add brief topic descriptor

2. **Location**: Save to `/knowledge/` directory
   - Create subdirectories by topic if needed
   - Maintain date prefix for chronological tracking

3. **Confirmation**: Inform user of saved location and filename

## Guidelines

### Academic Tone Requirements (from @AGENT.md)

- Use formal language and avoid colloquialisms
- Maintain objectivity and neutral presentation
- Employ third-person perspective when appropriate
- Use precise, discipline-specific terminology
- Support claims with evidence from the document
- Acknowledge limitations and uncertainties
- Present multiple perspectives when relevant

### Quality Standards

- **Precision**: Use exact terminology from the document
- **Completeness**: Cover all major sections and findings
- **Clarity**: Organize information logically with clear structure
- **Evidence-based**: Ground summary in document content
- **Critical**: Engage analytically, not just descriptively

### Key Takeaways Best Practices

- Minimum 3, maximum 5 takeaways
- Focus on substantive insights over procedural details
- Express as clear, standalone statements
- Collectively capture the document's primary value
- Frame in terms of implications when appropriate

## Error Handling

If issues occur:

1. **File Not Found**: Verify path and check file existence
2. **Access Denied**: Check file permissions
3. **Invalid PDF**: Confirm file is valid PDF format
4. **URL Inaccessible**: Verify URL and network connectivity
5. **Extraction Failure**: Report specific error and suggest alternatives

## Example Usage

```bash
# Summarize local PDF
/summarize-pdf papers/smith_2024_ml_review.pdf

# Summarize PDF from URL
/summarize-pdf https://arxiv.org/pdf/2401.12345.pdf

# Summarize with auto-detection
/summarize-pdf research/latest_paper.pdf
```

## Integration with Project Standards

This skill integrates with:
- **@AGENT.md**: Academic tone, formality, precision, evidence-based reasoning
- **@CLAUDE.md**: File naming, /knowledge/ directory, 3-5 key takeaways, tagging format

---

*This skill ensures consistent, high-quality PDF summarization following academic and organizational standards.*
