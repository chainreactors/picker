---
title: sentrymcp
url: https://kitploit.com/en/tools/github/zaydmulani09/sentrymcp
source: Kitploit
date: 2026-08-20
fetch_date: 2026-08-21T03:03:22.795227
---

# sentrymcp

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

sentrymcp — A static + runtime security scanner for MCP (Model Context Protocol) servers | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/zaydmulani09/sentrymcp

![](https://assets.kitploit.com/production/public/tools/50548/aa0b1e0c79a27a88e30d3114876660283cc406f37ed2ef7c3aca3cecd21b1201.png)

[Static Analysis](/en/categories/static-analysis)[Vulnerability Scanners](/en/categories/vulnerability-scanners)[Secret Detection](/en/categories/secret-detection)[Misconfiguration](/en/categories/misconfiguration)[API Security](/en/categories/api-security)[AI Security](/en/categories/ai-security)

![GitHub](/providers/github.png)zaydmulani09/sentrymcp

# sentrymcp

A static + runtime security scanner for MCP (Model Context Protocol) servers

[View Repository](https://github.com/zaydmulani09/sentrymcp)

241 day ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# sentrymcp

A static + runtime security scanner for MCP (Model Context Protocol)
servers. Between January and April 2026, security researchers disclosed
40+ CVEs across MCP server implementations, and a 2026 Endor Labs scan of
public MCP servers found 82% vulnerable to at least one OWASP MCP Top 10
risk class, 67% exposing path-traversal or injection-shaped sinks, and
34% with hardcoded or overprivileged credential handling — separate
research put roughly 38-40% of scanned servers running with no
authentication at all.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Rust](https://img.shields.io/badge/rust-2021%20edition-orange.svg)](Cargo.toml)
![Build](https://img.shields.io/badge/CI-not%20configured%20yet-lightgrey.svg)
[![Corpus](https://img.shields.io/badge/synthetic%20corpus-16/16%20correct-brightgreen.svg)](corpus/)

## Install

**Docker:**

root@kitploit:~

```
docker build -t sentrymcp .
docker run --rm -v "$(pwd):/scan" sentrymcp scan /scan
```

(PowerShell: `docker run --rm -v ${PWD}:/scan sentrymcp scan /scan`)

**From source:**

root@kitploit:~

```
git clone https://github.com/zaydmulani09/sentrymcp.git && cd sentrymcp
cargo build --release
./target/release/sentrymcp scan <path>
```

Windows note: if the default rustc toolchain is `-gnu` and the build
fails with `dlltool.exe not found`, switch to MSVC once in the repo dir:
`rustup override set stable-x86_64-pc-windows-msvc`.

## Quick example

Real output against the synthetic path-traversal example in `corpus/`:

root@kitploit:~

```
$ sentrymcp scan corpus/vulnerable-git-server

== Code Vulnerabilities ==

[HIGH] mcp_server_git/server.py:17  MCPA-PATH-PY-001 (CWE-22)
    python-path-traversal-unvalidated-arg
    > repo_path = Path(arguments["repo_path"])
    fix: Resolve the path with .resolve() and verify containment (e.g. path.resolve().is_relative_to(allowed_root)) before using it, or reject paths containing '..'.

[HIGH] mcp_server_git/server.py:21  MCPA-PATH-PY-001 (CWE-22)
    python-path-traversal-unvalidated-arg
    > log_dir = Path(arguments["repo_path"]) / ".git" / "logs"
    fix: Resolve the path with .resolve() and verify containment (e.g. path.resolve().is_relative_to(allowed_root)) before using it, or reject paths containing '..'.

summary (code vulnerabilities): 2 findings — 0 critical, 2 high, 0 medium, 0 low
total: 2 findings
```

## What it catches

`sentrymcp scan <path>` covers the first three (static, source-only).
`sentrymcp proxy -- <target cmd>` covers the fourth (runtime, sits between
an MCP client and the real server over stdio, transparently relaying
traffic while it watches).

## Architecture

One Cargo workspace, four crates:

* `sentrymcp-core` — rule-matching engine, directory scanner, tool
  description extraction.
* `sentrymcp-rules` — every detection rule as TOML (severity, CWE/OWASP
  reference, remediation) — no detection patterns are hardcoded in Rust.
* `sentrymcp-proxy` — the runtime stdio relay, tools/list diffing, and the
  best-effort network watcher.
* `sentrymcp-cli` — the single `sentrymcp` binary (`scan` and `proxy`
  subcommands).

Deeper design notes and known limitations per mechanism live in each
crate's doc comments (`engine.rs`, `extract.rs`, `netwatch.rs`).

## Limitations

* Static scanning is single-pass regex over raw source, not an AST or
  taint tracker — it misses vulnerabilities that flow through an
  intermediate variable before reaching a sink.
* Tool-description extraction is targeted pattern matching, not a real
  parser — it won't follow values built from concatenation, f-strings, or
  named constants.
* The runtime proxy's network watcher only has a working implementation
  on Windows (`netstat`-based); other platforms always report zero
  connections, a documented gap rather than a silent one.
* Findings marked `heuristic` confidence (missing-auth, homoglyph,
  overprivileged-scope) are review prompts, not confirmed verdicts —
  expect some false positives there by design.

## Contributing

Fork, branch, PR. Keep new detection rules in TOML, not Rust, and add a
vulnerable/patched pair to `corpus/` for anything new.

## License

MIT — see [LICENSE](https://github.com/zaydmulani09/sentrymcp/blob/HEAD/LICENSE).

[Download Tool](https://github.com/zaydmulani09/sentrymcp)

| Category | What it catches | Example |
| --- | --- | --- |

|  |  |  |
| --- | --- | --- |
| **Code vulnerabilities** | Path traversal, shell/command injection, unsafe `eval`/`exec` | `Path(arguments["repo_path"])` used with no containment check against a root dir |
| **Tool poisoning** | Hidden instructions, invisible/homoglyph unicode, oversized descriptions hidden in tool metadata | A tool description that reads "...ignore previous instructions, do not tell the user..." |
| **Auth & permissions** | Missing auth on network transports, hardcoded credentials, credential leaks via logging, overprivileged scope | `api_key = "sk-live-..."` committed as a literal instead of read from the environment |
| **Runtime proxy** | Tool-description "rug pulls" and unexpected outbound connections, observed live | A tool's `description` changes between the first and a later `tools/list` response in the same session |