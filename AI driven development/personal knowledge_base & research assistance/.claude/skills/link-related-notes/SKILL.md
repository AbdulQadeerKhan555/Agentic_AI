---
name: link-related-notes
description: Find and link related documents by analyzing shared tags, content similarity, and citations. Updates the document with a Related Materials section.
disable-model-invocation: true
user-invocable: true
argument-hint: [file-path]
allowed-tools: Read, Edit, Grep, Glob
---

# Link Related Notes

Analyze a document to discover connections with other notes in the knowledge base, then update the document with a "Related Materials" section containing links to related documents.

## Instructions

### Step 1: Read Target Document

Read the document specified in $ARGUMENTS:

1. **Validate Path**: Ensure file exists and is readable
2. **Extract Metadata**:
   - Tags from frontmatter (tags: #topic #category)
   - Date from frontmatter or filename
   - Source/citation information
   - Document type

3. **Extract Content Elements**:
   - Main title and headings
   - Key takeaways section
   - References section (if present)
   - Significant keywords and terminology

### Step 2: Identify Connection Criteria

Build a profile of the target document for matching:

1. **Tag Profile**:
   - Primary tags (all tags from frontmatter)
   - Tag hierarchy (topic vs category tags)
   - Weight: High priority for matching

2. **Content Keywords**:
   - Extract significant terms from key takeaways
   - Identify domain-specific terminology
   - Extract author names and key concepts
   - Weight: Medium priority for matching

3. **Citation Profile**:
   - Extract referenced works from References section
   - Identify cited authors and years
   - Note DOIs or URLs mentioned
   - Weight: High priority for direct citations

### Step 3: Search Knowledge Base

Search `/knowledge/` directory for related documents:

#### 3a. Tag-Based Search

1. **Use Grep** to find documents with shared tags:
   ```
   pattern: tags:.*#[matching-tag]
   path: knowledge/
   output_mode: files_with_matches
   ```

2. **Score by Tag Overlap**:
   - 1 shared tag = weak connection
   - 2-3 shared tags = moderate connection
   - 4+ shared tags = strong connection

3. **Exclude**: The target document itself

#### 3b. Content Similarity Search

1. **Use Grep** to find documents containing key terms:
   ```
   pattern: [significant-keyword]
   path: knowledge/
   output_mode: files_with_matches
   ```

2. **Search for**:
   - Author names from target document
   - Key concepts from takeaways
   - Domain-specific terminology

3. **Score by Keyword Frequency**:
   - Multiple keyword matches = higher relevance

#### 3c. Citation-Based Search

1. **Use Grep** to find documents that cite the same sources:
   ```
   pattern: [author-name].*[year]
   path: knowledge/
   output_mode: files_with_matches
   ```

2. **Search for**:
   - Shared citations in References sections
   - Common author names
   - Shared DOIs or URLs

3. **Score**:
   - Shared citations = strong connection (indicates related research)

### Step 4: Analyze and Rank Connections

For each potential related document:

1. **Read the Document**: Extract title, date, tags, and key takeaways

2. **Calculate Relevance Score**:
   - Shared tags: +3 points per tag
   - Content similarity: +2 points per significant keyword match
   - Shared citations: +4 points per citation
   - Same category tag: +2 points
   - Temporal proximity (within 30 days): +1 point

3. **Rank by Score**: Order from highest to lowest relevance

4. **Filter**: Keep top 5-10 most relevant connections

5. **Categorize Connections**:
   - **Highly Related** (score ≥ 10): Strong topical overlap
   - **Related** (score 5-9): Moderate connection
   - **See Also** (score 2-4): Tangential connection

### Step 5: Update Document with Related Materials

Following file preservation rules from `@AGENT.md`:

1. **Check for Existing Section**:
   - Look for "## Related Materials" or "## Related Work" section
   - If exists, update it; if not, add it

2. **Section Placement**:
   - Add before "## References" section if it exists
   - Otherwise, add at the end of the document

3. **Format Related Materials Section**:

```markdown
## Related Materials

### Highly Related

- [Document Title](relative/path/to/file.md) - [Date]
  - Shared topics: #tag1 #tag2
  - Brief description of connection or key insight

- [Another Document](path/to/file.md) - [Date]
  - Shared topics: #tag3 #tag4
  - Brief description of connection

### Related

- [Document Title](path/to/file.md) - [Date]
  - Connection: [shared citation/keyword/concept]

- [Document Title](path/to/file.md) - [Date]
  - Connection: [shared citation/keyword/concept]

### See Also

- [Document Title](path/to/file.md) - [Date]
  - Related through: [connection type]
```

4. **Use Edit Tool**: Update the document preserving all original content

5. **Confirmation**: Report to user:
   - Number of connections found
   - Breakdown by relevance level
   - File updated successfully

### Step 6: Verify and Report

1. **Verify Update**: Ensure Related Materials section was added correctly
2. **Preserve Original**: Confirm no content was lost or modified
3. **Report Summary**:
   - Total connections found
   - Highly related: [N]
   - Related: [N]
   - See also: [N]
   - File path updated

## Guidelines

### Connection Quality Standards

- **Relevance**: Only include genuinely related documents
- **Diversity**: Include different types of connections (tags, content, citations)
- **Utility**: Prioritize connections that provide value to the reader
- **Accuracy**: Verify connections are meaningful, not coincidental

### Academic Tone (from @AGENT.md)

- Use formal language in connection descriptions
- Be precise about the nature of connections
- Maintain objectivity in relevance assessments
- Use appropriate academic terminology

### File Preservation (from @AGENT.md)

- **Never delete** original content
- Only add or update the Related Materials section
- Preserve exact formatting and structure
- If section exists, update it carefully without removing valid links

### Link Format Standards

- Use relative paths from knowledge base root
- Include document date for temporal context
- Provide brief, informative connection description
- Use markdown link format: `[Title](path)`

## Error Handling

If issues occur:

1. **File Not Found**: Verify $ARGUMENTS path is correct
2. **No Connections Found**: Report that no related documents were identified
3. **Read Errors**: Report which files could not be accessed
4. **Update Failed**: Do not modify file; report error to user
5. **Malformed Document**: Skip problematic related files; report them

## Example Usage

```bash
# Link related notes for a specific document
/link-related-notes knowledge/2024-01-24_smith_2024_neural_networks.md

# Link notes in subdirectory
/link-related-notes knowledge/machine_learning/2024-01-20_deep_learning_review.md
```

## Output Example

After execution:
```
✓ Analyzed: 2024-01-24_smith_2024_neural_networks.md
✓ Searched 47 documents in knowledge base
✓ Found 8 related documents:
  - Highly related: 3
  - Related: 4
  - See also: 1
✓ Updated Related Materials section

Top connections:
1. 2024-01-22_jones_2024_cnn_architectures.md (score: 15)
   - Shared tags: #machine_learning #neural_networks #deep_learning
   - Shared citation: LeCun et al. (2015)

2. 2024-01-20_deep_learning_review.md (score: 12)
   - Shared tags: #machine_learning #deep_learning
   - Content similarity: convolutional networks, backpropagation

3. 2024-01-18_optimization_methods.md (score: 11)
   - Shared tags: #machine_learning #methodology
   - Shared citation: Kingma & Ba (2014)
```

## Integration with Project Standards

This skill integrates with:
- **@AGENT.md**: File preservation, academic tone, no deletion of original content
- **@CLAUDE.md**: Tag format (#topic #category), /knowledge/ directory structure

## Advanced Features

### Bidirectional Linking

When a connection is found, consider updating both documents to reference each other for comprehensive knowledge graph building.

### Connection Strength Visualization

The relevance score provides a quantitative measure of connection strength, useful for prioritizing reading order.

### Research Path Discovery

Related materials can reveal research progressions and help identify gaps in knowledge coverage.

---

*This skill enables systematic discovery and documentation of connections between research notes.*
