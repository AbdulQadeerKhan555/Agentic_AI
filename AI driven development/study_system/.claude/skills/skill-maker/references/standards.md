# Claude Code Documentation Standards

## Frontmatter Requirements

### Required Fields

**name**
- Format: kebab-case
- Pattern: `[a-z0-9]+(-[a-z0-9]+)*`
- Examples: `skill-maker`, `database-optimization`, `api-testing`

**description**
- Perspective: Third-person mandatory
- Length: 50-150 words
- Structure: "This skill should be used when the user asks to [triggers] or mentions [keywords]"
- Must include: 3-5 specific trigger phrases in quotes

**Example:**
```yaml
---
name: skill-maker
description: This skill should be used when the user asks to "create a skill", "generate a skill", "make a new skill", or mentions "skill-maker".
version: 1.0.0
---
```

### Optional Fields

**version**: Semantic versioning (e.g., `1.0.0`)
**license**: MIT, Apache-2.0, GPL-3.0, etc.

## Writing Style Standards

### Voice and Perspective

**Core Content (SKILL.md body):**
- Use imperative/infinitive form
- Avoid second person ("you", "your")
- Focus on actions, not actors

**Correct:**
```markdown
To create a skill, define the frontmatter.
Configure the plugin by editing the file.
```

**Incorrect:**
```markdown
You should create a skill by defining the frontmatter.
You need to configure the plugin.
```

**Frontmatter Description:**
- Use third person exclusively
- Reference "the user" explicitly

## Content Structure

### Standard Sections

1. **Overview** (Required): 2-3 paragraphs explaining purpose
2. **Core Procedures** (Required): Step-by-step workflows
3. **Key Concepts** (Conditional): Essential background knowledge
4. **Common Patterns** (Recommended): Typical use cases
5. **Validation** (Recommended): Quality assurance guidance
6. **Additional Resources** (Required if resources exist): Links to references/examples/scripts

### Word Count Targets

- **Minimum**: 1,500 words
- **Target**: 1,500-2,000 words
- **Maximum**: 3,000 words
- **Overflow**: Move to references/ if exceeding maximum

## Progressive Disclosure

### Three-Tier System

**Tier 1: Metadata (Always Loaded)**
- Name + description (~100 words)
- Specific trigger phrases for discovery

**Tier 2: Core Content (Loaded When Triggered)**
- Essential procedures and workflows
- Target: 1,500-2,000 words

**Tier 3: Bundled Resources (Loaded As Needed)**
- `references/`: Detailed documentation (unlimited)
- `examples/`: Working code samples
- `scripts/`: Executable utilities

## File Structure

### Simple Skill
```
.claude/skills/
└── skill-name/
    └── SKILL.md
```

### Standard Skill
```
.claude/skills/
└── skill-name/
    ├── SKILL.md
    └── references/
        └── patterns.md
```

### Advanced Skill
```
.claude/skills/
└── skill-name/
    ├── SKILL.md
    ├── references/
    │   └── advanced.md
    ├── examples/
    │   └── example.sh
    └── scripts/
        └── validate.sh
```

## Quality Checklist

### Frontmatter Validation
- [ ] Name is kebab-case
- [ ] Description uses third-person
- [ ] Description contains 3-5 trigger phrases
- [ ] Version follows semantic versioning

### Content Validation
- [ ] Word count: 1,500-3,000 words
- [ ] Uses imperative/infinitive form
- [ ] Logically organized sections
- [ ] Clear procedures and workflows
- [ ] Proper resource references

### Structure Validation
- [ ] Files in correct directories
- [ ] Resources referenced in SKILL.md
- [ ] Examples are functional
- [ ] Scripts documented

## Common Mistakes

### Description Anti-Patterns

**Avoid:**
- Vague: "Use this skill when working with databases"
- Wrong person: "You should use this skill when..."
- Generic: "Provides help with X"

**Prefer:**
- Specific: "when the user asks to 'optimize queries', 'tune performance'"
- Third person: "This skill should be used when..."
- Concrete: "when the user mentions 'slow queries'"

### Content Anti-Patterns

**Avoid:**
- Second person: "You should first configure..."
- Excessive length: > 3,000 words in SKILL.md
- Missing structure
- No actionable steps

**Prefer:**
- Imperative: "To configure X, modify Y"
- Concise core with detailed references
- Clear organization
- Practical guidance
