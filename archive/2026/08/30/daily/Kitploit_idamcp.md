---
title: idamcp
url: https://kitploit.com/en/tools/github/idamcp/idamcp
source: Kitploit
date: 2026-08-30
fetch_date: 2026-08-31T07:53:02.649436
---

# idamcp

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

idamcp — MCP server integrating IDA Pro with AI agents, featuring a stateless gateway for multi-session management, a relational SQL query engine for binary analysis, and architecture-agnostic disassembly and patching tools. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/idamcp/idamcp

![](https://assets.kitploit.com/production/public/tools/53595/58ae0951d15bc7468e8829819e19ed09e4da9f7d0df902e589bee24fb5df65fc-display-v1.webp)

[Static Analysis](/en/categories/static-analysis)[Dynamic Analysis (Sandboxing)](/en/categories/dynamic-analysis-sandboxing)[Reverse Engineering](/en/categories/reverse-engineering)[Debuggers](/en/categories/debuggers)[Binary Analysis](/en/categories/binary-analysis)[AI-Assisted Reversing](/en/categories/ai-assisted-reversing)

![GitHub](/providers/github.png)idamcp/idamcp

# idamcp

MCP server integrating IDA Pro with AI agents, featuring a stateless gateway for multi-session management, a relational SQL query engine for binary analysis, and architecture-agnostic disassembly and patching tools.

[View Repository](https://github.com/idamcp/idamcp)

1067452 days ago![Reviewed by Kitploit](/_next/image?url=%2Fbadges%2Fkitploit_badge_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# IDA Pro MCP Server

This project provides a Model Context Protocol (MCP) server for integrating IDA
Pro with AI agents like Gemini, Claude, and Jetski. It features a gateway-based
proxy architecture, an embedded relational SQLite query engine, and headless
session management to support advanced reverse engineering workflows.

**Background & Motivation**

Back in 2025, when we began integrating AI agents with IDA Pro, the upstream
[`ida-pro-mcp`](https://github.com/mrexodia/ida-pro-mcp) project provided a
great initial starting point. At the time, it did not yet offer multi-session
workflows, which were essential for our daily reverse engineering needs.

To address our internal use cases, we began building experimental solutions:

* **Gateway Proxy Architecture**: We developed a stateless proxy layer that
  automatically discovers and routes tool requests across concurrent GUI and
  headless IDA instances. *(While upstream has since added its own
  multi-session implementation, the two projects use fundamentally different
  architectural approaches).*
* **Relational SQL Query Engine**: Answering high-level questions about a
  binary (e.g., finding functions with specific characteristics or exploring
  complex cross-reference patterns) typically required dozens of sequential
  API calls running on IDA's main thread. We integrated an on-demand,
  event-synchronized SQLite3 engine with an AST query-rewrite layer
  (`sqlglot`). Because queries execute against SQLite in worker threads, they
  support concurrent reads without acquiring IDA's main thread lock or
  blocking the UI.
* **Architecture-Agnostic Tools & Bug Fixes**: Several tools in the early
  upstream code had x86-specific assumptions or heuristics. We rewrote them to
  be architecture-agnostic (supporting ARM, AArch64, MIPS, PowerPC, RISC-V,
  etc.) and fixed various stability and synchronization edge cases.

Over time, as we added more features, optimizations, and compatibility layers
across multiple IDA versions (IDA 7.7 through 9.4) and Python versions, the
codebase diverged substantially into an independent project with its own design
trade-offs.

We are sharing this project as an alternative, gateway- and SQL-centric approach
for connecting AI agents to IDA Pro, and we remain grateful to Duncan Ogilvie
and the upstream contributors for the foundational work that inspired this
effort.

**Core Features**

Key capabilities of this implementation include:

* **Stateless Gateway**: A proxy layer allows agents to interact with multiple
  IDA Pro instances (GUI and Headless) concurrently. The gateway automatically
  discovers and manages connections, allowing users to open and close
  databases without reconfiguring the client.
* **Headless Mode**: Perform analysis in the background without the IDA Pro
  GUI, suitable for automated workflows. Sessions can be managed directly by
  the AI agent.
* **Relational SQL Engine**: Integrates a read-only SQLite relational database
  populated on-demand and synchronized via IDA event hooks. Queries execute
  concurrently in background threads without blocking IDA's main UI thread,
  and an AST query layer (`sqlglot`) handles unsigned 64-bit memory
  arithmetic, comparison rewriting, and hex literals.
* **WYSIWYG Disassembly**: Disassembly tools (like `disassemble_function` and
  `disassemble_code`) return formatted text matching the IDA Pro UI, including
  opcode bytes, data definitions, and comments. Includes `get_ida_view` for
  viewing arbitrary memory ranges.
* **Analysis & Modification Tools**: Includes tools for UI navigation
  (`jump_to_address`, `set_color`), memory inspection (`hexdump`), byte
  patching (`patch_bytes`), database exporting (`export_file`),
  cross-references (`get_xrefs_from`, `get_data_xrefs_from`), and structured
  data creation.
* **Context-Aware Assembly Patching**: Powered by Keystone at the Gateway
  layer, the `patch_assembly` tool allows assembling and applying instructions
  directly at target addresses. It can resolve IDA symbols (function names,
  labels, globals) within assembly strings and evaluate basic operand math
  across supported architectures (x86/x64, ARM/AArch64, MIPS, PowerPC, etc.),
  making it convenient for quick hotpatching, stubbing out checks, or testing
  alternative execution paths.
* **Pagination and Caching**: Implements paginated resource iteration for
  symbol and string listing, reducing memory overhead on large binaries.
* **Security Dashboard**: A web-based interface for managing permissions for
  "unsafe" tools (e.g., Python code execution), providing control over agent
  capabilities.
* **Unix Domain Socket (UDS) Support**: In addition to TCP, the server
  supports UDS for secure local communication in isolated environments
  (Linux/macOS).

**Architecture Overview**

The core of this project is the **Gateway Pattern**. A central gateway process
acts as a proxy that routes requests from the AI agent to the correct active IDA
instance.

* **Discovery**: IDA instances (GUI or headless) register themselves by
  writing a metadata file to a shared directory.
* **Routing**: The gateway monitors this directory and manages a routing
  table. When a tool call arrives with a specific `database_id`, the gateway
  forwards it to the corresponding IDA process.
* **Statelessness**: This design decouples the agent from the backend. The
  agent communicates only with the gateway, and IDA instances can be opened or
  closed without affecting the agent's connection.

This architecture enables a multi-session analysis environment where the agent
can work with multiple binaries concurrently.

## Tested Environments & Prerequisites

Most tools in this project have been thoroughly tested and verified across:

* **IDA Pro 7.7 + Python 3.11**
* **IDA Pro 8.4 + Python 3.11**
* **IDA Pro 9.3 + Python 3.13**
* **IDA...