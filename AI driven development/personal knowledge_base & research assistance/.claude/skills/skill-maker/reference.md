# Skill Maker Reference

## YAML Fields Quick Reference

| Field | Type | Default | Purpose |
|-------|------|---------|---------|
| `name` | string | dir name | Skill identifier (lowercase, hyphens, max 64 chars) |
| `description` | string | first paragraph | What skill does and when to use it |
| `disable-model-invocation` | boolean | false | true = manual-only, false = auto-invokable |
| `user-invocable` | boolean | true | Show in `/` menu |
| `argument-hint` | string | - | Autocomplete hint: `[args]` |
| `allowed-tools` | string | all | Comma-separated: Read, Write, Edit, Bash, Grep, Glob, etc. |
| `model` | string | inherit | claude-sonnet-4, claude-opus-4, claude-haiku-4 |
| `context` | string | - | `fork` = run in subagent |
| `agent` | string | - | Subagent type: Explore, Bash, general-purpose, Plan |

## Common Tool Combinations

```yaml
# Read-only exploration
allowed-tools: Read, Grep, Glob

# File operations
allowed-tools: Read, Write, Edit

# Full file + commands
allowed-tools: Read, Write, Edit, Bash, Grep, Glob

# Research
allowed-tools: Read, WebFetch, WebSearch, Write
```

## Invocation Patterns

```yaml
# Manual-only (deployments, commits)
disable-model-invocation: true
user-invocable: true

# Auto-only (background knowledge)
disable-model-invocation: false
user-invocable: false

# Hybrid (both manual and auto)
disable-model-invocation: false
user-invocable: true

# Isolated subagent
context: fork
agent: Explore
allowed-tools: Read, Grep, Glob
```

## String Substitutions

- `$ARGUMENTS` - User-provided arguments
- `${CLAUDE_SESSION_ID}` - Current session ID
- `` !`command` `` - Execute command and inject output

## Validation Rules

**Name**: `^[a-z0-9-]+$` (lowercase, hyphens, max 64 chars)
**Description**: Clear, actionable, under 200 chars
**Agent**: Requires `context: fork`
**Tools**: Comma-separated, no spaces after commas

## File Structure

```
.claude/skills/skill-name/
├── SKILL.md          # Main skill (required)
├── reference.md      # Detailed docs (optional)
└── template.md       # Templates (optional)
```

## Security Best Practices

- Use `allowed-tools` to restrict access
- Set `disable-model-invocation: true` for destructive operations
- Use hooks for validation
- Principle of least privilege

---

*Concise reference for skill generation standards.*
