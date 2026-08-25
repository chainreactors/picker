---
title: Rogue-Framework
url: https://kitploit.com/en/tools/github/thisistfs/rogue-framework
source: Kitploit
date: 2026-08-24
fetch_date: 2026-08-25T02:58:59.122875
---

# Rogue-Framework

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

Rogue-Framework — Desktop workbench for AFL++ fuzzing, cross-architecture QEMU emulation, harness development, Ghidra headless analysis, custom mutators, and patch comparison for exploit development. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/thisistfs/rogue-framework

![](https://assets.kitploit.com/production/public/tools/51192/9f80add82c7a74ad4b1203e269d42a91a843df5457b6bdf72b461eb8fb64d506-display-v1.webp)

[Dynamic Analysis (Sandboxing)](/en/categories/dynamic-analysis-sandboxing)[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Exploitation](/en/categories/exploitation)[Reverse Engineering](/en/categories/reverse-engineering)[Debuggers](/en/categories/debuggers)[Fuzzing](/en/categories/fuzzing)[Binary Analysis](/en/categories/binary-analysis)

![GitHub](/providers/github.png)thisistfs/rogue-framework

# Rogue-Framework

Desktop workbench for AFL++ fuzzing, cross-architecture QEMU emulation, harness development, Ghidra headless analysis, custom mutators, and patch comparison for exploit development.

[View Repository](https://github.com/thisistfs/rogue-framework)

41 day ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# Rogue Framework

![Rogue](https://assets.kitploit.com/production/public/readmes/51192/9f80add82c7a74ad4b1203e269d42a91a843df5457b6bdf72b461eb8fb64d506/3344e4a77dbe678b6d1ce6297d9884b25df51ce3d8a5785390afe50e7eba6b6b-display-v1.webp)

* "*Make it rain.*"
* Rogue Amendiares The best intel-broker in night city

Rogue Framework is a desktop workbench for AFL++, cross-architecture QEMU fuzzing, harness development, lightweight Ghidra headless analysis, custom mutators, and patch comparison.
It is intentionally an auditable workbench rather than a button-only wrapper: every generated AFL++ command is visible before execution, and generated harnesses are ordinary source files that the researcher can edit.
It suppose to be "The BurpSuite of exploit developers"

# Run

Rogue Framework currently targets Linux and Python 3.11+ with PyQt6.

On Kali Linux, the installer sets up the Python environment, clones the official
AFL++ `stable` branch and builds its complete distribution and instrumented QEMU
backend, then installs Ghidra headless, native/multiarch GDB, GDB server, QEMU
user/system emulation, compiler/build dependencies, a user launcher, and
persistent shell PATH entries. AFL++ is downloaded into the ignored local
`AFLplusplus/` directory and is not distributed as part of Rogue Framework:

root@kitploit:~

```
chmod +x install.sh
./install.sh
rogue-framework
```

Install common cross compilers and their guest sysroots as well (this is a much
larger download) with:

root@kitploit:~

```
./install.sh --with-cross-toolchains
```

The installer is idempotent. Use `./install.sh --check` to audit an existing
installation or `./install.sh --rebuild-afl` to force an AFL++/QEMU rebuild.
Use `./install.sh --update-afl` to explicitly fast-forward the downloaded
checkout to the latest official stable revision.
Run it as the desktop user; it requests `sudo` only for apt packages. A newly
written PATH cannot alter the already-running parent shell, so either open a new
terminal, source `~/.zshrc`/`~/.bashrc`, or launch Rogue through the absolute
`~/.local/bin/rogue-framework` path printed by the installer.

Manual startup from the checkout remains available:

root@kitploit:~

```
python3 run.py
```

For an editable environment:

root@kitploit:~

```
python3 -m pip install -e .
rogue-framework
```

Cross-architecture dynamic binaries need a matching guest sysroot selected with
`QEMU_LD_PREFIX`; this is inherently target/distribution-specific. Ghidra's
`analyzeHeadless` path can be overridden under **Tools → External tools**.

## Project format

An `.rgp` project is readable, versioned JSON containing the portable project definition. Large and mutable artifacts live in its managed companion workspace:

root@kitploit:~

```
example.rgp
example.rgp-work/
  workspace.json
  project.sqlite3
  corpus/
  output/
  harnesses/
  mutators/
  analysis/
  logs/
  runs/
  staging/
  recovery/
  backups/
  objects/sha256/
```

This split keeps project files reviewable and avoids embedding crash corpora, findings, analysis indexes, or Ghidra state into JSON. `workspace.json` binds the manifest to the correct workspace identity, while `project.sqlite3` stores operational/indexed state. Managed references use `workspace://`; explicitly external resources use `external://`. Machine-local tool paths and UI state are stored outside the portable project.

Save As creates an independent clone with new project and workspace identities. Rogue stages and validates the destination before switching the open document, so a failed clone leaves the source project unchanged. Canonical saves use an advisory writer lease plus revision/SHA-256 conflict checks, preserve previous-good manifests, publish files atomically with `fsync`, and maintain crash-recovery snapshots including active editor drafts. Generated harnesses, mutators, Ghidra JSON, patch-diff results, and minimized findings are also published transactionally so a failed replacement does not delete the prior valid artifact.

### Legacy `.fuzz` projects

Rogue can import legacy schema 0–2 `.fuzz` manifests and their `.fuzz-work` companions. The legacy source is never the canonical destination: the first save upgrades it to a sibling `.rgp` project and `.rgp-work` workspace while retaining the original legacy files. New projects and Save As destinations always use `.rgp`.

## Near-term roadmap

1. ELF/PE/Mach-O inspection and automatic target architecture/input-mode suggestions
2. Harness compile/test loop, source-project discovery, and libFuzzer-compatible templates
3. AFL++ multi-instance orchestration, corpus management, and campaign resume
4. Crash collection, minimization, GDB/sanitizer triage, and deduplication
5. Function similarity heuristics for matching stripped or renamed symbols across binary versions
6. Native AFL++ custom mutator C/Rust templates with build validation
7. Auto Hrnessing
8. Plugin engine to support any kind of custom plugins for it

[Download Tool](https://github.com/thisistfs/rogue-framework)