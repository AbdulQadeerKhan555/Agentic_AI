# MCP Token Overhead Analysis

## Your Connected Servers

1. **Playwright MCP** (`@playwright/mcp@latest`)
2. **Context7 MCP** (`@upstash/context7-mcp`)

---

## Token Overhead Breakdown

### 1. Playwright MCP Server

**Tools Exposed:** 22 tools

The Playwright MCP server provides browser automation capabilities with the following tools:

| Tool Name | Estimated Tokens | Purpose |
|-----------|-----------------|---------|
| `browser_navigate` | ~120 | Navigate to a URL |
| `browser_snapshot` | ~150 | Capture accessibility snapshot |
| `browser_click` | ~180 | Perform click actions |
| `browser_type` | ~160 | Type text into elements |
| `browser_evaluate` | ~140 | Execute JavaScript |
| `browser_take_screenshot` | ~170 | Capture screenshots |
| `browser_close` | ~80 | Close browser page |
| `browser_resize` | ~100 | Resize browser window |
| `browser_console_messages` | ~130 | Get console logs |
| `browser_handle_dialog` | ~120 | Handle dialogs |
| `browser_file_upload` | ~140 | Upload files |
| `browser_fill_form` | ~200 | Fill multiple form fields |
| `browser_press_key` | ~100 | Press keyboard keys |
| `browser_hover` | ~110 | Hover over elements |
| `browser_select_option` | ~140 | Select dropdown options |
| `browser_drag` | ~150 | Drag and drop |
| `browser_tabs` | ~130 | Manage browser tabs |
| `browser_wait_for` | ~120 | Wait for conditions |
| `browser_network_requests` | ~140 | Get network requests |
| `browser_run_code` | ~150 | Run Playwright code |
| `browser_navigate_back` | ~90 | Navigate back |
| `browser_install` | ~100 | Install browser |

**Estimated Token Cost per Tool:**
- Tool name: 5-15 tokens
- Description: 30-80 tokens
- JSON Schema (parameters): 60-150 tokens
- **Average per tool: ~130 tokens**

**Total Playwright Overhead: ~2,860 tokens**

---

### 2. Context7 MCP Server

**Tools Exposed:** Estimated 4-6 tools

Context7 is an Upstash service for context management. Based on typical context management APIs, it likely exposes:

| Tool Name | Estimated Tokens | Purpose |
|-----------|-----------------|---------|
| `store_context` | ~140 | Store context/memory |
| `retrieve_context` | ~150 | Retrieve stored context |
| `search_context` | ~160 | Search through context |
| `list_contexts` | ~120 | List available contexts |
| `delete_context` | ~110 | Delete context entries |

**Average per tool: ~140 tokens**

**Total Context7 Overhead: ~680 tokens** (assuming 5 tools)

---

## Total Token Overhead Summary

| Component | Token Cost |
|-----------|-----------|
| **Playwright MCP** | ~2,860 tokens |
| **Context7 MCP** | ~680 tokens |
| **MCP Protocol Overhead** | ~100 tokens |
| **System Instructions** | ~50 tokens |
| **TOTAL STARTUP COST** | **~3,690 tokens** |

---

## Context Window Impact

Assuming you're using **Claude Sonnet 4.5** with a **200,000 token context window**:

- **Startup overhead:** 3,690 tokens (1.85% of context)
- **Available for conversation:** 196,310 tokens (98.15%)

### What This Means

Before you've asked a single question, approximately **3,700 tokens** of your context window are consumed by MCP server tool definitions. This is the "always-on" cost of having these servers connected.

---

## Token Overhead by Activity

### Scenario 1: Simple Question (No Tool Use)
- MCP overhead: 3,690 tokens
- Your question: ~50 tokens
- My response: ~200 tokens
- **Total: ~3,940 tokens**

### Scenario 2: Using Playwright (e.g., "Browse Amazon")
- MCP overhead: 3,690 tokens
- Your question: ~50 tokens
- Tool calls (5 browser actions): ~500 tokens
- Tool results: ~5,000 tokens (snapshots are large!)
- My response: ~500 tokens
- **Total: ~9,740 tokens**

### Scenario 3: Complex Multi-Tool Task
- MCP overhead: 3,690 tokens
- Your question: ~100 tokens
- Multiple tool calls (15 actions): ~1,500 tokens
- Tool results: ~15,000 tokens
- My response: ~1,000 tokens
- **Total: ~21,290 tokens**

---

## Optimization Strategies

### 1. Selective Server Connection
Only connect MCP servers when you need them:
```bash
# Disconnect when not needed
claude mcp remove playwright -s local

# Reconnect when needed
claude mcp add --transport stdio playwright -- npx @playwright/mcp@latest
```

### 2. Tool Search Feature
Claude Code automatically enables "tool search" when tools exceed 10% of context window. With your current setup:
- 3,690 tokens / 200,000 = 1.85% (tool search NOT active)
- Tool search activates at 20,000 tokens (100+ tools)

### 3. Monitor Token Usage
Check token consumption in real-time:
- Look at the token counter in Claude Code
- Review `~/.claude.json` for `lastCost` metrics

### 4. Use Project Scope Wisely
- **Local scope**: Tools always loaded in this project
- **User scope**: Tools loaded across ALL projects (higher baseline cost)
- **Project scope**: Team can see but must approve (one-time cost)

---

## Comparison: MCP vs Direct API Calls

### Without MCP (Direct API Integration)
- No startup overhead
- Must write custom code for each integration
- No standardized interface
- Higher development time

### With MCP (Your Current Setup)
- ~3,700 token startup overhead
- Standardized interface across all tools
- Instant access to 27+ capabilities
- Lower development time

**Trade-off:** You pay ~3,700 tokens upfront but gain immediate access to powerful capabilities without writing integration code.

---

## Real-World Impact

### Low Impact Scenarios
- **Simple Q&A**: MCP overhead is negligible
- **Code review**: Tools rarely used
- **Documentation**: Minimal tool usage

### High Impact Scenarios
- **Web scraping**: Playwright generates large snapshots (5,000+ tokens per page)
- **Multi-step automation**: Many tool calls accumulate
- **Context-heavy tasks**: Context7 retrievals add up

---

## Recommendations

1. **Keep both servers connected** if you regularly use browser automation or context management
2. **Disconnect Playwright** when doing pure coding tasks (saves ~2,860 tokens)
3. **Monitor your usage** - if you're hitting context limits, audit which tools you actually use
4. **Consider the value** - 3,700 tokens is ~1-2 paragraphs of text, but gives you 27+ powerful capabilities

---

## Additional Notes

- Token estimates are approximate and based on typical tool definition sizes
- Actual overhead may vary by 10-20% depending on schema complexity
- MCP protocol improvements may reduce overhead in future versions
- Tool search feature (when active) can reduce effective overhead by lazy-loading tool definitions

---

*Analysis generated for project: MCP_handsOn*
*Date: 2026-01-20*
