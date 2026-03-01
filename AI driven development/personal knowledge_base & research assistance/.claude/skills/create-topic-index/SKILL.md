---
name: create-topic-index
description: Generate an index of all notes on a specific topic by searching tags. Use when the user asks to index, organize, or list notes by topic or category.
disable-model-invocation: false
user-invocable: true
argument-hint: [topic-tag]
allowed-tools: Read, Write, Grep, Glob
---

# Create Topic Index

Generate a comprehensive index of all research notes on a specific topic by searching the `/knowledge/` directory for matching tags.

## Instructions

### Step 1: Parse Topic Input

Analyze the topic provided in $ARGUMENTS:

1. **Tag Format**: If input starts with `#`, use as-is (e.g., `#machine_learning`)
2. **Plain Text**: If no `#` prefix, add it (e.g., `machine_learning` → `#machine_learning`)
3. **Multiple Tags**: If multiple tags provided, search for notes containing any of them
4. **Validation**: Ensure tag follows format from `@CLAUDE.md` (lowercase, underscores)

### Step 2: Search Knowledge Base

Search the `/knowledge/` directory for notes with matching tags:

1. **Use Glob** to find all markdown files in `/knowledge/`:
   ```
   pattern: knowledge/**/*.md
   ```

2. **Use Grep** to search for the tag in file frontmatter:
   ```
   pattern: tags:.*#topic
   path: knowledge/
   output_mode: files_with_matches
   ```

3. **Collect Results**: Gather all files containing the target tag

### Step 3: Extract Information from Each Note

For each matching note file, extract:

1. **File Metadata**:
   - File name and relative path
   - Date from filename (YYYY-MM-DD prefix) or frontmatter
   - Full tag list from frontmatter

2. **Key Takeaways**:
   - Locate the "## Key Takeaways" section
   - Extract all numbered items (1-5 takeaways per `@CLAUDE.md`)
   - Preserve the exact wording

3. **Document Title**:
   - Extract the main heading (# Title)
   - Use as display name in index

4. **Source Information** (if available):
   - Extract source field from frontmatter
   - Include for proper attribution

### Step 4: Organize and Structure Index

Organize the collected information:

1. **Sort by Date**: Order notes chronologically (newest first or oldest first)
2. **Group by Category**: Optionally group by secondary tags if multiple categories exist
3. **Count Total**: Track total number of notes found

### Step 5: Generate Index Document

Create a structured index following academic standards from `@AGENT.md`:

```markdown
---
tags: #index #[topic] #knowledge_management
date: YYYY-MM-DD
type: topic_index
---

# Topic Index: [Topic Name]

## Overview

This index catalogs all research notes related to [topic] in the knowledge base. The index includes [N] notes spanning from [earliest date] to [latest date].

## Summary Statistics

- **Total Notes**: [N]
- **Date Range**: [YYYY-MM-DD] to [YYYY-MM-DD]
- **Related Tags**: [list of all related tags found]
- **Last Updated**: [current date]

## Indexed Notes

### [Note Title 1]

- **File**: `[relative/path/to/file.md]`
- **Date**: [YYYY-MM-DD]
- **Tags**: [#tag1 #tag2 #tag3]
- **Source**: [citation if available]

**Key Takeaways**:
1. [First takeaway]
2. [Second takeaway]
3. [Third takeaway]
4. [Fourth takeaway - if present]
5. [Fifth takeaway - if present]

---

### [Note Title 2]

- **File**: `[relative/path/to/file.md]`
- **Date**: [YYYY-MM-DD]
- **Tags**: [#tag1 #tag2 #tag3]
- **Source**: [citation if available]

**Key Takeaways**:
1. [First takeaway]
2. [Second takeaway]
3. [Third takeaway]

---

[Continue for all notes...]

## Related Topics

Based on tag analysis, related topics include:
- [#related_tag1] - [N notes]
- [#related_tag2] - [N notes]
- [#related_tag3] - [N notes]

## Usage Notes

This index was automatically generated on [date]. To update this index, run:
```
/create-topic-index [topic]
```

---

*Index generated following standards from @AGENT.md and @CLAUDE.md*
```

### Step 6: Save Index File

Following `@CLAUDE.md` naming conventions:

1. **File Name**: `YYYY-MM-DD_index_[topic].md`
   - Example: `2024-01-24_index_machine_learning.md`
   - Use current date
   - Include topic name (without # symbol)

2. **Location**: Save to `/knowledge/` directory
   - Keep at root level or in `indices/` subdirectory if it exists

3. **Confirmation**: Report to user:
   - Number of notes indexed
   - File location
   - Date range covered

## Guidelines

### Academic Tone (from @AGENT.md)

- Use formal, scholarly language in the overview
- Present information objectively and systematically
- Employ precise terminology
- Maintain clear organizational structure

### Search Best Practices

- Search is case-insensitive for tags
- Match partial tags (e.g., `#machine` matches `#machine_learning`)
- Include notes with multiple relevant tags
- Exclude the index files themselves from results

### Quality Standards

- **Completeness**: Include all matching notes
- **Accuracy**: Preserve exact key takeaways from source notes
- **Organization**: Present in logical, chronological order
- **Metadata**: Include all relevant file information
- **Consistency**: Follow project naming and tagging standards

### Error Handling

If issues occur:

1. **No Notes Found**: Report that no notes match the topic tag
2. **Missing Key Takeaways**: Note which files lack the standard section
3. **Malformed Frontmatter**: Skip problematic files and report them
4. **Access Errors**: Report files that cannot be read

## Example Usage

```bash
# Index all machine learning notes
/create-topic-index machine_learning

# Index with tag format
/create-topic-index #neuroscience

# Index multiple related tags
/create-topic-index deep_learning neural_networks
```

## Output Example

After execution:
```
✓ Created topic index for #machine_learning
✓ Found 12 notes spanning 2024-01-15 to 2024-01-24
✓ Saved to: knowledge/2024-01-24_index_machine_learning.md

Summary:
- 12 notes indexed
- 45 total key takeaways extracted
- Related topics: #deep_learning (8), #neural_networks (6), #computer_vision (4)
```

## Integration with Project Standards

This skill integrates with:
- **@AGENT.md**: Academic tone, formal structure, objective presentation
- **@CLAUDE.md**: Tag format (#topic #category), /knowledge/ directory, key takeaways extraction

## Advanced Features

### Automatic Index Updates

When new notes are added with a topic tag, consider regenerating the index to keep it current.

### Cross-Referencing

The index can reveal connections between notes through shared tags and related topics.

### Research Progress Tracking

Use indices to track research progression over time by analyzing date ranges and note frequency.

---

*This skill enables systematic organization and discovery of research notes by topic.*
