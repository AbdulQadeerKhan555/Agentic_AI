---
name: skill-maker
description: Generate new Claude Code skills following official standards. Use when the user wants to create a new skill or asks to generate a skill.
disable-model-invocation: false
user-invocable: true
argument-hint: [skill-description]
allowed-tools: Write, Read, Bash, AskUserQuestion
---

# Skill Maker

This skill generates new Claude Code skills following official Claude Code standards and conventions. It ensures consistency, quality, and proper structure across all generated skills.

## Core Responsibilities

1. **Gather Requirements**: Collect all necessary information about the desired skill
2. **Ask Clarifying Questions**: Identify gaps in the user's requirements and ask targeted questions
3. **Generate Skill Structure**: Create properly formatted SKILL.md with correct YAML frontmatter
4. **Ensure Quality**: Follow Claude Code standards and best practices and better results.
5. **Create Supporting Files**: Generate additional files (reference.md, examples.md) when needed

## Skill Generation Process

### Phase 1: Requirements Gathering

When the user requests a new skill, analyze their prompt for the following information:

**Essential Information:**
- **Skill Name**: What should the skill be called? (lowercase, hyphens, max 64 chars)
- **Purpose**: What does this skill do?
- **When to Use**: When should Claude or the user invoke this skill?

**Functional Requirements:**
- **Arguments**: Does the skill accept arguments? What are they?
- **Steps/Instructions**: What are the specific steps or instructions?
- **Tools Needed**: Which tools should the skill have access to?
- **Output Format**: What should the skill produce?

**Invocation Control:**
- **User-Invocable**: Should users be able to call this with `/skill-name`?
- **Auto-Invocation**: Should Claude automatically invoke this skill when appropriate?
- **Manual-Only**: Should this be disabled from auto-invocation? (e.g., for deployments, commits)

**Advanced Options:**
- **Model Selection**: Does this need a specific model (sonnet/opus/haiku)?
- **Context Mode**: Should this run inline or in a forked subagent?
- **Agent Type**: If forked, which agent type? (Explore, Bash, general-purpose, etc.)
- **Tool Restrictions**: Should tool access be limited for safety?
- **Hooks**: Are pre/post hooks needed?
- **Supporting Files**: Does this need reference.md, examples.md, or templates?

### Phase 2: Gap Analysis and Questions

**CRITICAL**: Before generating the skill, identify any missing information and ask the user clarifying questions.

Use the `AskUserQuestion` tool to gather missing information. Ask about:

1. **If skill name is unclear**: Suggest a name based on purpose
2. **If invocation pattern is unclear**: Ask whether it should be manual-only, auto-invoked, or both
3. **If arguments are ambiguous**: Clarify what parameters the skill needs
4. **If tool requirements are unclear**: Ask which tools are needed (Read, Write, Edit, Bash, Grep, Glob, etc.)
5. **If scope is too broad**: Ask for specific boundaries or focus areas
6. **If output format is unspecified**: Ask what the skill should produce
7. **If safety concerns exist**: Ask about tool restrictions or validation needs

**Example Questions to Ask:**

```
Question: "Should this skill be invoked automatically by Claude, or only when you explicitly call it with /skill-name?"
Options:
- "Automatic - Claude should use it when appropriate"
- "Manual only - I'll invoke it explicitly"
- "Both - Allow both automatic and manual invocation"

Question: "Does this skill need to accept arguments?"
Options:
- "Yes - it needs parameters (please specify what)"
- "No - it works without arguments"

Question: "Which tools should this skill have access to?"
Options:
- "All tools - no restrictions"
- "Read-only tools (Read, Grep, Glob)"
- "File operations (Read, Write, Edit)"
- "Bash commands"
- "Custom selection (please specify)"
```

### Phase 3: Skill Generation

Once all requirements are gathered, generate the skill following this structure:

#### 1. Create Directory Structure

```bash
mkdir -p .claude/skills/[skill-name]
```

#### 2. Generate SKILL.md

**Template Structure:**

```yaml
---
name: skill-name
description: Clear, concise description of what this skill does and when to use it

# Invocation control (include if needed)
disable-model-invocation: false  # true for manual-only skills
user-invocable: true             # false if only Claude should invoke
argument-hint: [args]            # Show in autocomplete

# Execution control (include if needed)
allowed-tools: Read, Write, Edit # Comma-separated list
model: claude-sonnet-4           # Specific model if needed
context: fork                    # Run in subagent
agent: Explore                   # Subagent type (with context: fork)

# Hooks (include if needed)
hooks: {}
---

# Skill Title

Brief overview of what this skill does and its purpose.

## Instructions

1. First step with clear action
2. Second step with $ARGUMENTS if applicable
3. Third step with specific guidance
4. Continue with all necessary steps

## Guidelines

- Important guideline 1
- Important guideline 2
- Important guideline 3

## Examples

```language
example code or usage
```

## Additional Resources

- For detailed reference, see [reference.md](reference.md)
- For examples, see [examples.md](examples.md)
```

#### 3. Generate Supporting Files (if needed)

**reference.md**: Detailed documentation, API specs, or comprehensive guides
**examples.md**: Multiple usage examples with explanations
**template.md**: Templates for Claude to fill out
**scripts/**: Helper scripts if the skill needs executable components

### Phase 4: Validation and Output

After generating the skill:

1. **Validate Structure**: Ensure YAML frontmatter is properly formatted
2. **Check Completeness**: Verify all required information is included
3. **Test Syntax**: Ensure markdown is properly formatted
4. **Provide Summary**: Tell the user what was created and how to use it

## Quality Standards

All generated skills must adhere to:

### Naming Conventions
- Lowercase letters only
- Hyphens for word separation (not underscores or spaces)
- Descriptive and concise (max 64 characters)
- Examples: `deploy-app`, `fix-issue`, `code-review`

### Description Best Practices
- Explain what the skill does clearly
- Include when to use it
- Mention key capabilities
- Use natural language
- Good: "Fix GitHub issues by number. Use when the user asks to fix or resolve an issue."
- Bad: "Issue fixer" or "Invokes issue resolution subroutine"

### Content Organization
- Keep SKILL.md under 500 lines
- Use clear headers and sections
- Number sequential steps
- Bullet non-sequential items
- Include code blocks with language tags
- Reference supporting files when needed

### Tool Restrictions
- Limit tools for safety-critical operations
- Read-only for exploration: `Read, Grep, Glob`
- File operations: `Read, Write, Edit`
- Full access: Omit `allowed-tools` field

### Invocation Patterns

**Manual-only** (deployments, commits, destructive operations):
```yaml
disable-model-invocation: true
```

**Background knowledge** (not actionable):
```yaml
user-invocable: false
```

**Subagent execution** (isolated research, exploration):
```yaml
context: fork
agent: Explore
```

## Special Considerations

### For Research/Academic Skills
- Reference `@AGENT.md` for academic tone requirements
- Include proper citation formats
- Emphasize evidence-based reasoning
- Follow knowledge base organization standards

### For File Management Skills
- Include preservation warnings
- Require confirmation for destructive operations
- Follow naming conventions from project standards
- Reference `@CLAUDE.md` for workflow integration

### For Development Skills
- Include testing requirements
- Specify code quality standards
- Reference project conventions
- Include security considerations

## Example Generation Workflow

**User Request**: "Create a skill for summarizing research papers"

**Step 1 - Analyze Request**:
- Name: `summarize-paper` or `research-summary`
- Purpose: Summarize research papers
- Missing: Input format, output structure, key elements to extract

**Step 2 - Ask Questions**:
```
Question: "What format will the research papers be in?"
Options:
- PDF files
- Markdown notes
- URLs to papers
- Multiple formats

Question: "What should the summary include?"
Options:
- Key findings only
- Full structured summary (methodology, results, conclusions)
- Custom format (please specify)
```

**Step 3 - Generate Skill**:
Create `.claude/skills/research-summary/SKILL.md` with:
- Proper YAML frontmatter
- Clear instructions for summarization
- Reference to `@AGENT.md` for academic tone
- Integration with `/knowledge/` directory structure
- Key takeaways extraction (3-5 points per `@CLAUDE.md`)
- Proper tagging format

**Step 4 - Confirm**:
"Created skill `research-summary` at `.claude/skills/research-summary/SKILL.md`.
Invoke with `/research-summary [file-path]` to summarize research papers following academic standards."

## Error Handling

If generation fails:
1. Explain what went wrong
2. Ask for clarification on problematic requirements
3. Suggest alternatives or simplifications
4. Never generate incomplete or malformed skills

## Output Format

After successful generation, provide:

```
✓ Created skill: [skill-name]
✓ Location: .claude/skills/[skill-name]/SKILL.md
✓ Supporting files: [list if any]

Usage:
- Manual: /[skill-name] [arguments]
- Automatic: [when Claude will invoke it]

The skill is now available for use.
```

## Integration with Project Standards

When generating skills for this project:
- Reference `@AGENT.md` for academic tone requirements
- Reference `@CLAUDE.md` for workflow and organization standards
- Follow file naming conventions specified in project documentation
- Integrate with `/knowledge/` directory structure
- Include proper tagging and metadata formats
- Ensure preservation of original sources
- Require confirmation for reorganization operations

---

## Usage Examples

**Simple skill request**:
```
User: "Create a skill for committing changes"
→ Ask about: commit message format, pre-commit checks, auto-push behavior
→ Generate: commit-changes skill with proper git workflow
```

**Complex skill request**:
```
User: "Create a skill that analyzes code quality"
→ Ask about: languages, metrics, output format, tool restrictions
→ Generate: code-analyzer skill with subagent execution and read-only tools
```

**Academic skill request**:
```
User: "Create a skill for literature reviews"
→ Ask about: source format, review structure, citation style
→ Generate: literature-review skill integrated with @AGENT.md and @CLAUDE.md standards
```

---

*This skill-maker ensures all generated skills follow Claude Code official standards and maintain consistency across the project.*
