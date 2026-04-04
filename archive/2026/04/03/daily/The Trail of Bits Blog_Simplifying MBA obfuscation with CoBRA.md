---
title: Simplifying MBA obfuscation with CoBRA
url: https://blog.trailofbits.com/2026/04/03/simplifying-mba-obfuscation-with-cobra/
source: The Trail of Bits Blog
date: 2026-04-03
fetch_date: 2026-04-04T04:16:19.160900
---

# Simplifying MBA obfuscation with CoBRA

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Simplifying MBA obfuscation with CoBRA

[Kyle Elliott](/authors/kyle-elliott/)

April 03, 2026

[tool-release](/categories/tool-release/), [open-source](/categories/open-source/), [reversing](/categories/reversing/), [c/c++](/categories/c/c%2B%2B/), [llvm](/categories/llvm/), [research-practice](/categories/research-practice/)

Page content

* [Why existing approaches fall short](#why-existing-approaches-fall-short)
* [How CoBRA works](#how-cobra-works)
* [What you can do with it](#what-you-can-do-with-it)
* [Validated against seven independent datasets](#validated-against-seven-independent-datasets)
* [What’s next](#whats-next)

Mixed Boolean-Arithmetic (MBA) obfuscation disguises simple operations like `x + y` behind tangles of arithmetic and bitwise operators. Malware authors and software protectors rely on it because no standard simplification technique covers both domains simultaneously; algebraic simplifiers don’t understand bitwise logic, and Boolean minimizers can’t handle arithmetic.

We’re releasing [CoBRA](https://github.com/trailofbits/CoBRA), an open-source tool that simplifies the full range of MBA expressions used in the wild. Point it at an obfuscated expression and it recovers a simplified equivalent:

`$ cobra-cli --mba "(x&y)+(x|y)"`
`x + y`

`$ cobra-cli --mba "((a^b)|(a^c)) + 65469 * ~((a&(b&c))) + 65470 * (a&(b&c))" --bitwidth 16`
`67 + (a | b | c)`

CoBRA simplifies 99.86% of the 73,000+ expressions drawn from seven independent datasets. It ships as a CLI tool, a C++ library, and an LLVM pass plugin. If you’ve hit MBA obfuscation during malware analysis, reversing software protection schemes, or tearing apart VM-based obfuscators, CoBRA gives you readable expressions back.

## Why existing approaches fall short

The core difficulty is that verifying MBA identities requires reasoning about how bits and arithmetic interact under modular wrapping, where values silently overflow and wrap around at fixed bit-widths. An identity like `(x ^ y) + 2 * (x & y) == x + y` is true precisely because of this interaction, but algebraic simplifiers only see the arithmetic and Boolean minimizers only see the logic; neither can verify it alone. Obfuscators layer these substitutions to build arbitrarily complex expressions from simpler operations.

Previous MBA simplifiers have tackled parts of this problem. [SiMBA](https://github.com/DenuvoSoftwareSolutions/SiMBA) handles linear expressions well. [GAMBA](https://github.com/DenuvoSoftwareSolutions/GAMBA) extends support to polynomial cases. Until CoBRA, no single tool achieved high success rates across the full range of MBA expression types that security engineers encounter in the wild.

## How CoBRA works

CoBRA uses a worklist-based orchestrator that classifies each input expression and selects the right combination of simplification techniques. The orchestrator manages 36 discrete passes organized across four families—linear, semilinear, polynomial, and mixed—and routes work items based on the expression’s structure.

Most MBA expressions in the wild are **linear**: sums of bitwise terms like `(x & y)`, `(x | y)`, and `~x`, each multiplied by a constant. For these, the orchestrator evaluates the expression on all Boolean inputs to produce a signature, then races multiple recovery techniques against each other and picks the cheapest verified result. Here’s what that looks like for `(x ^ y) + 2 * (x & y)`:

| CoBRA linear simplification flow: (x ^ y) + 2 \* (x & y) | | |
| --- | --- | --- |
| *Step 1: Classification* Input expression is identified as **Linear MBA** | | |
| ↓ | | |
| *Step 2: Truth Table Generation* Evaluate on all boolean inputs → `[0, 1, 1, 2] truth table` | | |
| ↓ | | |
| *Step 3a: Pattern Match* Scan identity database | *Step 3b: ANF Conversion* Bitwise normal form | *Step 3c: Interpolation* Solve basis coefficients |
| ↓ | | |
| *Step 4: Competition* Compare candidate results → **Winner: x + y** (Lowest Cost) | | |
| ↓ | | |
| *Step 5: Verification* Spot-check against random 64-bit inputs or prove with Z3 → **Pass** | | |

When constant masks appear (like `x & 0xFF`), the expression enters CoBRA’s **semi-linear** pipeline, which breaks it down into its smallest bitwise building blocks, recovers structural patterns, and reconstructs a simplified result through bit-partitioned assembly. For expressions involving products of bitwise subexpressions (like `(x & y) * (x | y)`), a decomposition engine extracts **polynomial** cores and solves residuals.

**Mixed** expressions that combine products with bitwise operations often contain repeated subexpressions. A lifting pass replaces these with temporary variables, simplifying the inner pieces first, then solving the expression that connects them. Here’s what that looks like for a product identity `(x & y) * (x | y) + (x & ~y) * (~x & y)`:

| CoBRA mixed simplification flow: (x & y) \* (x | y) + (x & ~y) \* (~x & y) | |
| --- | --- |
| *Step 1: Classification* Input is identified as **Mixed MBA** | |
| ↓ | |
| *Step 2: Decompose* Decompose into subexpressions ↓ | |
| (x & y) \* (x | y) | (x & ~y) \* (~x & y) |
| ↓ | ↓ |
| *Step 3: Lift & Solve* Lift products, solve inner pieces | |
| ↓ | |
| *Step 4: Collapse Identity* Collapse product identity → **x \* y** | |
| ↓ | |
| *Step 5: Verification* Spot-check against random 64-bit inputs or prove with Z3 → **Pass** | |

Regardless of which pipeline an expression passes through, the final step is the same: CoBRA verifies every result against random inputs or proves equivalence with Z3. No simplification is returned unless it is confirmed correct.

## What you can do with it

CoBRA runs in three modes:

* **CLI tool**: Pass an expression directly and get the simplified form back. Use `--bitwidth` to set modular arithmetic width (1 to 64 bits) and `--verify` for Z3 equivalence proofs.
* **C++ library**: Link against CoBRA’s core library to integrate simplification into your own tools. If you’re building an automated analysis pipeline, the `Simplify` API takes an expression and returns a simplified result or reports it as unsupported.
* **LLVM pass plugin**: Load `libCobraPass.so` into `opt` to deobfuscate MBA patterns directly in LLVM IR. If you’re building deobfuscation pipelines on top of tools like [Remill](https://github.com/lifting-bits/remill), this integrates directly as a pass. It handles patterns spanning multiple basic blocks and applies a cost gate, only replacing instructions when the simplified form is smaller, and supports LLVM 19 through 22.

## Validated against seven independent datasets

We tested CoBRA against 73,066 expressions from [SiMBA](https://github.com/DenuvoSoftwareSolutions/SiMBA), [GAMBA](https://github.com/DenuvoSoftwareSolutions/GAMBA), [OSES](https://github.com/fvrmatteo/oracle-synthesis-meets-equality-saturation), and four other independent sources. These cover the full spectrum of MBA complexity, from two-variable linear expressions to deeply nested mixed-product obfuscations.

| Category | Expressions | Simplified | Rate |
| --- | --- | --- | --- |
| Linear | ~55,000 | ~55,000 | ~100% |
| Semilinear | ~1,000 | ~1,000 | ~100% |
| Polynomial | ~5,000 | ~4,950 | ~99% |
| Mixed | ~9,000 | ~8,900 | ~99% |
| **Total** | **73,066** | **72,960** | **99.86%** |

The 106 unsupported expressions are carry-sensitive mixed-domain cases where bitwise and arithmetic operations interact in ways that current techniques can’t decompose. CoBRA reports these as unsupported rather than guessing wrong. The full benchmark breakdown is in [DATASETS.md](https://github.com/trailofbits/CoBRA/blob/master/DATASETS.md).

## What’s next

CoBRA’s remaining failures fall into two categories: expressions with heavy subexpression duplication that exhaust the worklist budget even with lifting, and carry-sensitive residuals where bitwise masks over ar...