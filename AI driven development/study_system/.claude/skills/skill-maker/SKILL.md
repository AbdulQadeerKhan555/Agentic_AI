---
name: skill-maker
description: This skill should be used when the user asks to "create a skill", "generate a skill", "make a new skill", "build a skill for", or mentions "skill-maker". Use this when the user wants to create a Claude Code skill following official standards.
version: 1.0.0
---

# Skill Maker

## Overview

The skill-maker facilitates the creation of high-quality Claude Code skills that adhere to official documentation standards. This skill guides users through a structured process, gathering necessary information through targeted questions before generating properly formatted skill files.

## Core Principles

### Quality Assurance Protocol

Before generating any skill, the skill-maker must:

1. **Gather Complete Requirements**: Elicit all necessary information through systematic questioning
2. **Validate Scope**: Ensure the skill has clear, specific trigger conditions
3. **Determine Complexity**: Assess whether the skill requires additional resources (references, examples, scripts)
4. **Verify Standards Compliance**: Ensure output adheres to Claude Code documentation standards

### Progressive Disclosure Architecture

Skills employ a three-tier loading system:

**Tier 1: Metadata (Always Loaded)**
- Name and description (~100 words)
- Must contain specific trigger phrases
- Third-person perspective

**Tier 2: Core Content (Loaded When Triggered)**
- Essential procedures and workflows
- Target: 1,500-2,000 words (maximum 3,000)
- Imperative/infinitive form

**Tier 3: Bundled Resources (Loaded As Needed)**
- `references/`: Detailed documentation (unlimited size)
- `examples/`: Working code samples
- `scripts/`: Executable utilities

## Required Information Gathering

### Mandatory Questions

When a user requests skill creation, systematically collect the following information:

#### 1. Skill Purpose and Scope

Ask:
- "What specific task or problem should this skill address?"
- "What are the exact phrases a user would say to trigger this skill?"
- "What should happen when this skill is activated?"

**Validation Criteria:**
- Purpose must be concrete and actionable
- Trigger phrases must be specific (not vague like "when user needs help")
- Scope must be clearly bounded

#### 2. Target Audience and Context

Ask:
- "Who will use this skill? (developers, researchers, specific domain experts)"
- "What level of expertise should be assumed?"
- "Are there specific tools or technologies this skill focuses on?"

#### 3. Complexity Assessment

Ask:
- "Does this skill require detailed reference documentation beyond the core content?"
- "Should working code examples be included?"
- "Are validation or utility scripts needed?"

**Decision Matrix:**
- **Simple Skill**: Single SKILL.md file (< 2,000 words)
- **Standard Skill**: SKILL.md + references/ directory
- **Advanced Skill**: SKILL.md + references/ + examples/ + scripts/

#### 4. Content Structure

Ask:
- "What are the main sections or procedures this skill should cover?"
- "Are there common pitfalls or mistakes to document?"
- "Should the skill include decision trees or workflows?"

#### 5. Integration Requirements

Ask:
- "Does this skill need to reference other skills or plugins?"
- "Are there specific Claude Code tools it should utilize?"
- "Should it include hooks or event-driven automation?"

### Optional Enhancements

If applicable, inquire about:
- Version control considerations
- License preferences
- Author attribution
- Related documentation or external resources

## Skill Generation Process

### Step 1: Information Synthesis

After gathering requirements, synthesize the information into:

1. **Skill Name**: Kebab-case identifier (e.g., `database-optimization`)
2. **Trigger Phrases**: List of 3-5 specific user utterances
3. **Core Sections**: Outline of main content areas
4. **Resource Requirements**: Determination of additional files needed

### Step 2: Frontmatter Construction

Generate YAML frontmatter following this template:

```yaml
---
name: skill-name
description: This skill should be used when the user asks to "trigger phrase 1", "trigger phrase 2", "trigger phrase 3", or mentions "keyword". [Additional specific trigger conditions].
version: 1.0.0
---
```

**Critical Requirements:**
- Description must be third-person ("This skill should be used when...")
- Include 3-5 specific trigger phrases in quotes
- Avoid vague language ("helps with", "provides guidance")
- Be concrete about activation conditions

### Step 3: Core Content Development

Structure the SKILL.md body with:

**Standard Sections:**
1. **Overview**: What the skill does and when to use it (2-3 paragraphs)
2. **Core Procedures**: Step-by-step workflows (imperative form)
3. **Key Concepts**: Essential knowledge required
4. **Common Patterns**: Typical use cases and solutions
5. **Validation**: How to verify correct implementation
6. **Additional Resources**: Pointers to references/, examples/, scripts/

**Writing Style:**
- Use imperative/infinitive form: "To accomplish X, perform Y"
- Avoid second person: Not "You should do X"
- Be objective and actionable
- Maintain 1,500-2,000 word target for core content

### Step 4: Resource File Creation

Based on complexity assessment, generate:

**references/ Directory:**
- `patterns.md`: Common patterns and best practices (2,000-5,000 words)
- `advanced.md`: Advanced techniques and edge cases
- `api-reference.md`: Detailed API or syntax reference

**examples/ Directory:**
- Working code samples demonstrating key concepts
- Configuration templates
- Real-world use case implementations

**scripts/ Directory:**
- `validate.sh`: Validation utility for skill output
- `test.sh`: Testing framework
- `README.md`: Script documentation

### Step 5: Directory Structure Creation

Generate the appropriate directory structure:

**Simple Skill:**
```
.claude/skills/
└── skill-name/
    └── SKILL.md
```

**Standard Skill:**
```
.claude/skills/
└── skill-name/
    ├── SKILL.md
    └── references/
        ├── patterns.md
        └── advanced.md
```

**Advanced Skill:**
```
.claude/skills/
└── skill-name/
    ├── SKILL.md
    ├── references/
    │   ├── patterns.md
    │   ├── advanced.md
    │   └── api-reference.md
    ├── examples/
    │   ├── example1.sh
    │   └── config-template.yaml
    └── scripts/
        ├── validate.sh
        └── README.md
```

### Step 6: Validation and Quality Assurance

Before finalizing, verify:

**Frontmatter Checklist:**
- [ ] Name is kebab-case
- [ ] Description uses third-person perspective
- [ ] Description contains 3-5 specific trigger phrases
- [ ] Version follows semantic versioning

**Content Checklist:**
- [ ] Core SKILL.md is 1,500-2,000 words (max 3,000)
- [ ] Uses imperative/infinitive form (not second person)
- [ ] Sections are logically organized
- [ ] Includes clear procedures and workflows
- [ ] References additional resources appropriately

**Structure Checklist:**
- [ ] Files are in correct directories
- [ ] Resource files are properly referenced in SKILL.md
- [ ] Examples are functional and well-documented
- [ ] Scripts include usage documentation

## Common Pitfalls to Avoid

### Description Anti-Patterns

**Avoid:**
- Vague triggers: "Use this skill when working with databases"
- Wrong perspective: "You should use this skill when..."
- Generic language: "Provides help with X"
- Missing specificity: "Load when user needs assistance"

**Prefer:**
- Specific phrases: "when the user asks to 'optimize queries', 'tune database performance'"
- Third person: "This skill should be used when..."
- Concrete scenarios: "when the user mentions 'slow queries' or 'database bottlenecks'"

### Content Anti-Patterns

**Avoid:**
- Second person instructions: "You should first configure..."
- Excessive length in core SKILL.md (> 3,000 words)
- Lack of structure or clear sections
- Missing references to bundled resources
- Theoretical content without actionable steps

**Prefer:**
- Imperative form: "To configure X, modify Y"
- Concise core with detailed references
- Clear hierarchical organization
- Explicit pointers to examples and scripts
- Practical, actionable guidance

## Output Format

### File Generation Sequence

1. Create directory structure using Bash tool
2. Write SKILL.md using Write tool
3. Generate reference files if needed
4. Create example files if needed
5. Write validation scripts if needed

### User Confirmation

Before generating files, present:

1. **Skill Overview**: Name, purpose, trigger phrases
2. **Structure Plan**: Which files will be created
3. **Content Outline**: Main sections and topics
4. **Estimated Scope**: Word counts and complexity level

Request explicit confirmation before proceeding with file generation.

## Additional Resources

### Reference Files

- **`references/standards.md`** - Detailed Claude Code documentation standards

## Execution Protocol

When skill-maker is triggered:

1. **Acknowledge Request**: Confirm understanding of skill creation intent
2. **Initiate Questioning**: Use AskUserQuestion tool to gather requirements systematically
3. **Synthesize Information**: Compile responses into structured plan
4. **Present Plan**: Show user the proposed skill structure and content outline
5. **Request Confirmation**: Obtain explicit approval before file generation
6. **Generate Files**: Create all necessary files using appropriate tools
7. **Validate Output**: Run validation checks on generated skill
8. **Provide Summary**: Report created files and next steps

## Quality Standards Enforcement

The skill-maker must ensure:

- All generated skills follow progressive disclosure principles
- Trigger phrases are specific and actionable
- Content is appropriately scoped (not too broad or narrow)
- Writing style adheres to Claude Code standards
- File structure matches complexity requirements
- Validation criteria are met before finalization

By following this systematic approach, skill-maker produces consistent, high-quality skills that integrate seamlessly with the Claude Code ecosystem.
