---
title: kin v0.6.4
url: https://kitploit.com/en/posts/github-firelock-ai-kin-v064
source: Kitploit
date: 2026-09-04
fetch_date: 2026-09-05T06:28:32.161051
---

# kin v0.6.4

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/12665/dbedb6d5e53a09c0772e94a1d81a15a77421ebbb40f136adefc8eb3cc8e45510.png)

New releaseSep 4, 2026

# kin v0.6.4

The system of record for AI-written software. A persistent graph of entities, relationships, changes, and provenance, so humans and AI agents see what a change touches before it merges. Beside Git today.

Share

![Kin, the semantic system of record for AI-written software](https://assets.kitploit.com/production/public/readmes/12665/55686ad4696e166589300e948ce2ed89f45622266654371a433a31c612829ec8.png)

### The diff is not the change.

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE) [![Latest release](https://img.shields.io/badge/release-latest-6E56CF.svg)](https://github.com/firelock-ai/kin/releases/latest) [![kinlab.ai](https://img.shields.io/badge/hosted-kinlab.ai-111111.svg)](https://kinlab.ai)

AI agents can write a change faster than a team can establish what it touches,
whether it reverses an earlier fix, and how far its consequences reach. Git
records files and line history. Kin records the software itself as a graph of
entities, relations, changes, and provenance, then gives humans and agents one
semantic authority to query and review. What a change touches shows up before
it merges, and agents work from exact context instead of re-reading the
repository.

Kin is the semantic system of record for AI-written software. It is an early
alpha, usable today as a local CLI, daemon, MCP server, review surface, and
graph-backed filesystem projection. It is pre-1.0, so expect rough edges and
breaking changes. See the [latest stable release](https://github.com/firelock-ai/kin/releases/latest)
and the [current limitations](#platform-and-maturity) before adopting it in a
critical workflow.

## See it on a real repository

A one-line signature change in ripgrep looks harmless in the diff. Ask
`kin impact` about it, before any compiler runs, and it names what the edit
reaches. The callers of the changed signature come first, then everything
those callers pull in behind them.

![kin impact on ripgrep: a one-line signature edit, and Kin surfaces the entities it affects before a compiler runs](https://assets.kitploit.com/production/public/readmes/12665/43f73477ba09d6aa7a5bb446cadaea9c36981cc1d093faacaa03b9b61346b955.png)

Recorded against a prepared graph at ripgrep commit
`e89fff89ac9af12e8d4ce9d5fd07beb408ca730f`. A one-line signature edit, and Kin
surfaces the entities it affects before a compiler runs. The graph was built
beforehand. No compiler ran. Exact commands:
[kinlab.ai/proof](https://kinlab.ai/proof). The raw run directory is not
public yet, so this is a recipe you can re-run, not a trace you can audit.

Kin surfaces what the change touches. Whether the change is correct stays with
your compiler, tests, and review. The graph is built beforehand by `kin init`,
and building it is the expensive part; after that, impact questions are
answered from graph truth, not from re-reading the tree.

## The stack

Kin is one system with a few clear public surfaces:

| Surface | What it does |
| --- | --- |
| **[kin](https://github.com/firelock-ai/kin)** | Semantic system of record: CLI, daemon, graph lifecycle, MCP, review, provenance, and Git coexistence. |
| **[kin-vfs](https://github.com/firelock-ai/kin-vfs)** | Projects graph-owned files through normal filesystem calls so existing tools can keep using files. |
| **[kin-editor](https://github.com/firelock-ai/kin-editor)** | VS Code access to the entity explorer, semantic search, trace, review, and rename surfaces. |
| **[Kin MCP](https://github.com/firelock-ai/kin/blob/main/docs/mcp-tools.md)** | Typed graph tools for AI agents, bundled into `kin` and launched with `kin mcp start`. |
| **[KinLab](https://kinlab.ai)** | Hosted collaboration and control plane. Public repository connection is not a first-run flow yet. |

## How the pieces fit

Kin is the semantic system of record for AI-written software, and everything in
the map below either reaches that authority or supports it. Humans and AI agents
come in through the CLI, the bundled MCP server, or the VS Code extension. All
three ask the same daemon, and the daemon answers from graph authority rather
than by re-reading the tree. `kin-vfs` projects that same graph back through
ordinary filesystem calls, so editors, compilers, and build systems keep seeing
files. Git sits beside the graph as an import and export boundary rather than as
an answer path, and KinLab is the hosted layer over the same authority.

root@kitploit:~

```
flowchart TD
    people["Humans and AI agents"]

    subgraph surfaces["Access surfaces"]
        cli["kin CLI"]
        mcp["Kin MCP server"]
        editor["kin-editor for VS Code"]
    end

    daemon["kin daemon"]
    authority["Graph authority<br/>entities, relations, changes, provenance"]
    db["kin-db<br/>graph storage, snapshots,<br/>index, text and vector search"]
    prims["kin-model, kin-blobs, kin-search,<br/>kin-vector, kin-infer, kin-lsp"]
    vfs["kin-vfs<br/>transparent file projection"]
    tools["Editors, compilers, build systems"]
    git["Git<br/>import and export boundary"]
    kinlab["KinLab<br/>hosted collaboration and control plane"]

    people --> cli
    people --> mcp
    people --> editor
    cli --> daemon
    mcp --> daemon
    editor --> daemon
    daemon --> authority
    authority --> db
    db --> prims
    authority <-->|"kin init imports, kin git export"| git
    authority -->|"publish and sync"| kinlab
    authority --> vfs
    vfs --> tools
```

Underneath those surfaces are the layers the system is built from:

| Layer | Role |
| --- | --- |
| **[kin-db](https://github.com/firelock-ai/kin-db)** | Graph storage, snapshots, indexing, text search, and vector search. |
| **[kin-model](https://github.com/firelock-ai/kin-model)** | Canonical types and domain models shared across the stack. |
| **[kin-blobs](https://github.com/firelock-ai/kin-blobs)** | Content-addressable blob storage. |
| **[kin-search](https://github.com/firelock-ai/kin-search)** | Lexical search primitives and staged retrieval. |
| **[kin-vector](https://github.com/firelock-ai/kin-vector)** | Vector and nearest-neighbor substrate. |
| **[kin-infer](https://github.com/firelock-ai/kin-infer)** | Inference and embedding substrate. |
| **[kin-lsp](https://github.com/firelock-ai/kin-lsp)** | Language-server enrichment feeding the semantic layer. |

These are implementation layers of one system, not separate products a new user
needs to assemble. None of them is installed separately.

## Open source and the Kin ecosystem

The core of Kin is open source under Apache-2.0: [kin](https://github.com/firelock-ai/kin),
[kin-db](https://github.com/firelock-ai/kin-db), [kin-vfs](https://github.com/firelock-ai/kin-vfs),
and [kin-editor](https://github.com/firelock-ai/kin-editor), plus the supporting
libraries kin-model, kin-blobs, kin-search, kin-vector, kin-infer, kin-lsp, and
kin-actions.

[KinLab](https://kinlab.ai) is a proprietary product built on this open core: the
hosted collaboration and control-plane layer described above.

The same boundary applies to how benchmark work is shared. The [benchmark
specification and a standalone, dependency-free bundle verifier](https://github.com/firelock-ai/kin-bench-spec)
are public, so a claim can be checked without access to the system that produced
it. The runner and proof infrastructure that produce sealed evidence bundles (the
orchestration, the pinned-release proof gate, and the hosted measurement
environment) remain private for now. The spec an...