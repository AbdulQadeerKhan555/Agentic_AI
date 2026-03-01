# Skill Templates

## Basic Skill Template

```yaml
---
name: skill-name
description: Clear description of what this skill does and when to use it
---

# Skill Title

Brief overview.

## Instructions

1. First step
2. Second step with $ARGUMENTS if needed
3. Third step

## Guidelines

- Guideline 1
- Guideline 2
```

## Manual-Only Skill Template

```yaml
---
name: skill-name
description: Description of manual-only operation
disable-model-invocation: true
user-invocable: true
argument-hint: [args]
allowed-tools: Read, Write, Bash
---

# Manual Operation Skill

## Pre-Execution Checklist

- [ ] Check 1
- [ ] Check 2

## Instructions

1. Verify prerequisites
2. Execute operation with $ARGUMENTS
3. Validate results
```

## Research/Exploration Template

```yaml
---
name: skill-name
description: Research or exploration task
context: fork
agent: Explore
allowed-tools: Read, Grep, Glob
---

# Research Task

## Objectives

1. Find relevant information
2. Analyze findings
3. Summarize results

## Output Format

Provide structured summary with file references.
```

## Academic/Project-Integrated Template

```yaml
---
name: skill-name
description: Task following project standards
allowed-tools: Read, Write
---

# Project-Integrated Task

Follow standards from `@AGENT.md` and `@CLAUDE.md`.

## Instructions

1. Apply academic tone (see @AGENT.md)
2. Follow naming conventions (see @CLAUDE.md)
3. Use proper metadata and tags
4. Save to appropriate directory
```

---

*Minimal templates for common skill patterns.*
