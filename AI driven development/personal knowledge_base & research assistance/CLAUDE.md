# Claude Agent Configuration

## Foundation

**Primary Directive**: Follow all instructions specified in `@AGENT.md` as the foundational guidelines for tone, style, and academic standards.

This document extends those core principles with specific operational workflows and organizational protocols for the personal knowledge base and research assistance system.

---

## Research Notes Management

### Storage Location and Naming

**All research notes go in `/knowledge/` with YYYY-MM-DD prefix**

- **Directory**: All research notes, summaries, and analysis documents must be stored in the `/knowledge/` directory
- **Naming Convention**: Use the format `YYYY-MM-DD_topic_description.md`
  - Example: `2024-01-24_machine_learning_fundamentals.md`
  - Example: `2024-01-24_literature_review_climate_models.md`
- **Rationale**: Date prefixes enable chronological tracking and facilitate temporal analysis of research progression
- **Subdirectories**: May be organized by topic or project within `/knowledge/` as needed, but date prefix remains mandatory

### File Organization Structure

```
/knowledge/
├── 2024-01-24_topic_name.md
├── 2024-01-25_another_topic.md
├── subdirectory_name/
│   ├── 2024-01-26_specific_research.md
│   └── 2024-01-27_related_notes.md
└── ...
```

---

## Document Processing Protocol

### Key Takeaways Extraction

**Always extract 3-5 key takeaways from any document**

When processing, analyzing, or summarizing any document, you must:

1. **Identify Core Insights**: Extract 3-5 key takeaways that represent the most significant findings, arguments, or contributions
2. **Prioritize Substance**: Focus on substantive insights rather than procedural or methodological details
3. **Maintain Clarity**: Express each takeaway as a clear, standalone statement
4. **Ensure Completeness**: Collectively, the takeaways should capture the document's primary value

#### Format for Key Takeaways

```markdown
## Key Takeaways

1. [First major insight or finding]
2. [Second major insight or finding]
3. [Third major insight or finding]
4. [Fourth major insight or finding - if applicable]
5. [Fifth major insight or finding - if applicable]
```

#### Guidelines

- **Minimum**: 3 takeaways (for shorter or focused documents)
- **Maximum**: 5 takeaways (for comprehensive or complex documents)
- **Quality over Quantity**: Better to have 3 excellent takeaways than 5 mediocre ones
- **Actionability**: When appropriate, frame takeaways in terms of implications or applications

---

## Metadata and Tagging System

### Consistent Tagging Format

**Use consistent tagging format: #topic #category**

All documents in the knowledge base must include standardized tags for discoverability and organization.

#### Tagging Structure

```markdown
---
tags: #topic #category #additional_descriptors
date: YYYY-MM-DD
type: [note|summary|analysis|literature_review|reference]
---
```

#### Tag Categories

**#topic**: The subject matter or domain
- Examples: #machine_learning #climate_science #economics #philosophy #neuroscience

**#category**: The type or nature of the content
- Examples: #methodology #theory #empirical_study #review #tutorial #critique

**Additional Descriptors**: Supplementary tags for enhanced categorization
- Examples: #quantitative #qualitative #interdisciplinary #foundational #advanced

#### Tagging Best Practices

1. **Consistency**: Use established tags when applicable; create new tags judiciously
2. **Specificity**: Balance between specific and general tags (e.g., both #neural_networks and #machine_learning)
3. **Discoverability**: Consider how future searches might query the content
4. **Hierarchy**: Use broader category tags alongside specific topic tags
5. **Limit**: Typically 3-7 tags per document to maintain meaningful categorization

#### Example Metadata Block

```markdown
---
tags: #machine_learning #methodology #neural_networks #deep_learning
date: 2024-01-24
type: literature_review
source: Smith et al. (2024)
---
```

---

## Workflow Integration

### Standard Document Template

When creating new research notes, use this template structure:

```markdown
---
tags: #topic #category
date: YYYY-MM-DD
type: [document_type]
source: [if applicable]
---

# [Document Title]

## Overview
[Brief context and purpose]

## Key Takeaways

1. [Takeaway 1]
2. [Takeaway 2]
3. [Takeaway 3]
4. [Takeaway 4 - optional]
5. [Takeaway 5 - optional]

## Detailed Notes
[Main content following academic standards from AGENT.md]

## References
[Citations and sources]

## Related Materials
[Links to related notes or resources]
```

---

## Operational Reminders

- **Academic Tone**: Maintain formal, scholarly communication as specified in `@AGENT.md`
- **File Preservation**: Never delete original source materials without explicit permission
- **Reorganization**: Always request approval before restructuring existing content
- **Naming Conventions**: Follow established patterns for consistency
- **Documentation**: Keep metadata current and accurate

---

*This configuration document works in conjunction with AGENT.md to establish comprehensive operational guidelines for the personal knowledge base and research assistance system.*
