---
title: aotopsy v1.1.0
url: https://kitploit.com/en/posts/github-bronils-aotopsy-v110
source: Kitploit
date: 2026-08-31
fetch_date: 2026-09-01T06:59:37.998279
---

# aotopsy v1.1.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/50046/cd3c189960ef606e32e1d667d68652097c7bd139fafe4deb63838fd0e3c45199.png)

New releaseAug 31, 2026

# aotopsy v1.1.0

Static analyzer for Flutter/Dart AOT snapshots — recovers function names, class hierarchies, call graphs, and behavioral signals from libapp.so without embedding or executing the Dart VM. Supports ARM64 and x86\_64, Dart 2.10–3.12.

Share

# AOTopsy

[![CI](https://github.com/BroNils/aotopsy/actions/workflows/ci.yml/badge.svg)](https://github.com/BroNils/aotopsy/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/BroNils/aotopsy?sort=semver)](https://github.com/BroNils/aotopsy/releases)
[![License](https://img.shields.io/badge/license-BSD--3--Clause-blue.svg)](LICENSE)

A Dart AOT snapshot analyzer. Turns `libapp.so` — the compiled Dart code inside a Flutter release APK — into function names, class layouts, call graphs, behavioral signals, and readable pseudocode. No Dart VM, no SDK compilation, no runtime fallback.

> **Fork notice:** AOTopsy is a fork of **unflutter**, originally by **Anthony Zboralski**. The original `zboralski/unflutter` repository is no longer available (removed by the author); a community continuation exists at [`KristijanZic/unflutter`](https://github.com/KristijanZic/unflutter). All credit for the original snapshot parser, cluster deserializer, ARM64 disassembly pipeline, and Ghidra/IDA integration belongs to the original author. AOTopsy extends it with x86\_64 support, a native decompiler, whole-program type inference, Frida script generation, and comprehensive documentation.

## What It Recovers

| Output | What it is |
| --- | --- |
| Function names | The original Dart name for each compiled function |
| Class structures | Field names, byte offsets, inheritance chains |
| Call graph | Direct (BL) and indirect (BLR/dispatch) call edges with provenance |
| String references | Which functions load which string literals from the object pool |
| Behavioral signals | Crypto, network, gambling, SIM, location, WebView, blockchain keyword classification |
| Pseudocode | Architecture-neutral decompiled output from ARM64 or x86\_64 machine code |
| Dart Source Export | Whole-project modular `.dart` files reconstructed with classes, fields, and methods |

Supports **ARM64** and **x86\_64**. Covers **Dart 2.10 through 3.13** (3.13.2 is the current stable frontier).

## Accuracy & Honesty

AOTopsy is measured against ground truth, not asserted. Two properties are enforced by
the test suite on every change:

| Metric | Value | What it means |
| --- | --- | --- |
| **Name-recovery agreement** | **89.8%** overall (81.3% worst band, ≥ 0.81 gate floor) across 44 ground-truth builds | Recovered function names compared against each build's own ELF `.symtab`, the external ground truth — `TestSymtabDifferential`. Full per-build scoreboard: [BENCHMARK.md](https://github.com/bronils/aotopsy/blob/HEAD/BENCHMARK.md) (`make bench`). |
| **Decompiler syntax validity** | **100%** valid Dart | Every emitted pseudocode function parses as Dart — `TestDecompileQualityCorpus`. |
| **Fabrication rate** | **0%** | The §2 rule: never emit a guessed name, type, or call target as fact. Unknowns render honestly (`indirectCall`, `<unknown>`, `dynamic`). |

The ground-truth twins are real production builds we cannot redistribute, so those
differential gates run **locally**; public CI validates build + unit tests across the
platform matrix (sample-dependent tests skip cleanly when the binary is absent). See
[SECURITY.md](https://github.com/bronils/aotopsy/blob/HEAD/SECURITY.md) for release-binary verification and the honest scope below.

## Quick Start

root@kitploit:~

```
make build
./aotopsy libapp.so                    # full pipeline
./aotopsy doctor libapp.so             # quick diagnostic
./aotopsy export-dart --lib libapp.so --out ./lib  # reconstruct entire Dart source project
./aotopsy _debug decompile-native --lib libapp.so --find MyClass  # find and decompile a function
```

See `WORKFLOW.md` for the step-by-step methodology when you have a raw APK and don't know where to start.

## How It Works

AOTopsy treats the Dart AOT snapshot as a deterministic binary grammar. Every byte has exactly one correct interpretation given the right constraints (ELF structure, snapshot magic, version hash, CID table, cluster encoding). The parser applies constraints until only one interpretation survives — no heuristics, no guessing.

The pipeline runs in stages, each a pure function from bytes to structured data:

root@kitploit:~

```
flowchart TD
    A[libapp.so] --> B[ELF parse]
    B --> C[snapshot region extraction]
    C --> D[version detection]
    D --> E[cluster alloc<br/>object census]
    E --> F[cluster fill<br/>field values, names, strings]
    F --> G[instructions table<br/>code ranges, stub boundaries]
    G --> H{architecture?}
    H -->|ARM64| I[ARM64 disassembly]
    H -->|x86_64| J[x86_64 disassembly]
    I --> K[CFG + call edges<br/>register provenance]
    J --> K
    K --> L[type inference<br/>BLR receiver type resolution]
    L --> M[signal classification<br/>behavioral keyword matching]
    M --> N[JSONL + HTML + DOT<br/>pseudocode output]
```

Two independent backends share the same front half (ELF through cluster fill), then split by architecture: `internal/disasm` for ARM64, `internal/disasm/x86.go` for x86\_64. The decompiler (`internal/decompiler`) handles both architectures through a unified IR.

root@kitploit:~

```
flowchart LR
    subgraph "Shared front half"
        A[elfx] --> B[snapshot]
        B --> C[cluster]
    end
    subgraph "ARM64 backend"
        C --> D1[disasm ARM64]
        D1 --> E1[callgraph]
        E1 --> F1[signal]
    end
    subgraph "x86_64 backend"
        C --> D2[disasm x86_64]
        D2 --> E2[callgraph]
        E2 --> F2[signal]
    end
    subgraph "Decompiler (both archs)"
        C --> G[decompiler IR]
        G --> H[pseudocode]
    end
```

## Comparison With Blutter

root@kitploit:~

```
flowchart LR
    subgraph Blutter
        direction TB
        B1[libapp.so] --> B2[Compile matching<br/>Dart SDK]
        B2 --> B3[Embed Dart VM]
        B3 --> B4[Deserialize via<br/>VM internal APIs]
        B4 --> B5[Perfect fidelity]
    end
    subgraph AOTopsy
        direction TB
        A1[libapp.so] --> A2[Parse binary format<br/>directly]
        A2 --> A3[No VM, no SDK]
        A3 --> A4[Version-specific<br/>format modeling]
        A4 --> A5[Portability + speed]
    end
```

[Blutter](https://github.com/worawit/blutter) embeds the Dart VM to deserialize the snapshot through its own code paths. Perfect fidelity, but requires compiling a matching Dart SDK for every target version — and it is ARM64-only, with no static x86\_64 support. AOTopsy is the only static, version-independent analyzer with a native pseudocode decompiler and published ground-truth accuracy.

AOTopsy parses the binary format directly. No VM, no SDK. The tradeoff: every format change across Dart versions must be modeled explicitly. There is no runtime to handle it automatically.

## Commands

### Full pipeline

root@kitploit:~

```
aotopsy libapp.so              # disasm + call edges + signal + metadata (ARM64: + Ghidra/IDA)
aotopsy signal libapp.so       # same, skip metadata
aotopsy libapp.so --graph      # also build call graph DOT files
```

Flags: `--out <dir>` (default: `<basename>.aotopsy/`), `--quiet`, `--strict`, `--max-steps <n>`, `--k <n>` (signal context depth, default 2).

### Diagnostic

root@kitploit:~

```
aotopsy doctor libapp.so       # Dart version, pointer size, support status, bu...