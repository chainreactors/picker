---
title: hermes-decomp v0.2.3
url: https://kitploit.com/en/posts/github-symbioticsec-hermes-decomp-v023
source: Kitploit
date: 2026-09-10
fetch_date: 2026-09-11T06:51:42.066885
---

# hermes-decomp v0.2.3

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/7451/8f9ccdd62c649f9e65d338af422c912a57d5a55690a864bca5db6cff0348b5fb.png)

New releaseSep 10, 2026

# hermes-decomp v0.2.3

A powerful decompiler that lets you reverse-engineer React Native mobile apps by converting their compiled Hermes bytecode (.hbc) files back into readable JavaScript.

Share

![Hermes Bytecode Decompiler](https://assets.kitploit.com/production/public/readmes/7451/72db756d07b0143cb85fcbbc64e0a8935a7e1eba0a903b007404684ea5c23b98.png)

[![Build](https://github.com/SymbioticSec/hermes-decomp/actions/workflows/build.yml/badge.svg)](https://github.com/SymbioticSec/hermes-decomp/actions/workflows/build.yml)

Rust decompiler for **Hermes bytecode** (`.hbc`), the JS engine behind React Native. Supports **HBC 40 to 99**.

## Install

**Pre-built binaries** (Linux / macOS / Windows) from [Releases](https://github.com/SymbioticSec/hermes-decomp/releases) or [Actions](https://github.com/SymbioticSec/hermes-decomp/actions/workflows/build.yml):

| Asset suffix | Platform |
| --- | --- |
| `linux-x86_64` / `linux-arm64` | Linux |
| `macos-arm64` / `macos-x86_64` | macOS |
| `windows-x86_64` | Windows |

Archives include `hermes-decomp` and `hermes-mcp`. Verify: `shasum -a 256 -c SHA256SUMS`.

root@kitploit:~

```
hermes-decomp update --check      # or --install / --version v0.1.7
```

**From source** (Rust 1.70+):

root@kitploit:~

```
git clone https://github.com/SymbioticSec/hermes-decomp.git
cd hermes-decomp && cargo build --release
# → target/release/hermes-decomp  target/release/hermes-mcp
```

## Quick start

root@kitploit:~

```
hermes-decomp info app.hbc
hermes-decomp disasm app.hbc --function 5 --info --show-offsets
hermes-decomp decompile app.hbc -o out.js          # progress on stderr
hermes-decomp decompile app.hbc --deep -o out.js   # recover more names, slower
hermes-decomp decompile app.hbc --function 42
hermes-decomp tui app.hbc
hermes-decomp xref app.hbc --query "loginWithToken"
```

![Disassembly Example](https://assets.kitploit.com/production/public/readmes/7451/5c1c208b08c07e94b8095fbac98d4d6213ba8ffc0add028b11b0f5a285ba52af.png)

![Decompilation Example](https://assets.kitploit.com/production/public/readmes/7451/84f5786f32e1ae0ee3930c498e68fe9b8ee1f0a63a56fd4f2d427ce5a7398076.png)

## What it does

| Area | Commands (highlights) |
| --- | --- |
| **Read** | `info`, `disasm`, `decompile`, `tui`, `extract`, `modules`, `deps` |
| **Analyze** | `xref`, `callgraph`, `graphviz`, `closures`, `debug`, `dump`, `bin-diff` |
| **RE helpers** | `secrets`, `frida-hooks` |
| **Write** (bytecode only) | `emit-hasm`, `asm`, `asm-check`, `patch-string`, `patch-function`, `inject-stub`, `create` |

Full flags and examples → **[docs/USAGE.md](https://github.com/symbioticsec/hermes-decomp/blob/main/docs/USAGE.md)**.

Notes:

* Full-bundle `decompile` uses an on-disk **`.hdcache`** for fast reloads. Pass `--no-cache` to force.
* Write tools patch **bytecode / HASM**. They do **not** recompile decompiled JavaScript.
* `decompile -o …` prints pipeline stages on **stderr**.

## MCP & library

* **MCP server** (`hermes-mcp`) for AI assistants → **[docs/MCP.md](https://github.com/symbioticsec/hermes-decomp/blob/main/docs/MCP.md)**
  Config template: [`mcp-config.example.json`](https://github.com/symbioticsec/hermes-decomp/blob/main/mcp-config.example.json)
* **Rust crate** `hbc-decomp` → **[docs/LIBRARY.md](https://github.com/symbioticsec/hermes-decomp/blob/main/docs/LIBRARY.md)**

root@kitploit:~

```
cargo build --release -p hbc-decomp-mcp
```

## Contributing

See **[CONTRIBUTING.md](https://github.com/symbioticsec/hermes-decomp/blob/main/CONTRIBUTING.md)**. Please open an issue before a PR.

root@kitploit:~

```
cargo build --release --workspace && cargo test --workspace
```

## Resources

* [Hermes Engine](https://hermesengine.dev/) · [React Native](https://reactnative.dev/)

## License

MIT. See [LICENSE](https://github.com/symbioticsec/hermes-decomp/blob/main/LICENSE).

[Read more](/en/tools/github/symbioticsec/hermes-decomp?expand=1)

## Categories

[Android Security](/en/categories/android-security)[Static Analysis](/en/categories/static-analysis)[iOS Security](/en/categories/ios-security)[Code Analysis](/en/categories/code-analysis)[Dynamic Code Analysis (DAST)](/en/categories/dynamic-code-analysis)[Reverse Engineering](/en/categories/reverse-engineering)[Debuggers](/en/categories/debuggers)[Mobile Security](/en/categories/mobile-security)[Binary Analysis](/en/categories/binary-analysis)[Learning & Education](/en/categories/education)[AI-Assisted Reversing](/en/categories/ai-assisted-reversing)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories