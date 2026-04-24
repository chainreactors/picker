---
title: Trailmark turns code into graphs
url: https://blog.trailofbits.com/2026/04/23/trailmark-turns-code-into-graphs/
source: The Trail of Bits Blog
date: 2026-04-23
fetch_date: 2026-04-24T04:55:38.841999
---

# Trailmark turns code into graphs

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Trailmark turns code into graphs

[Scott Arciszewski](/authors/scott-arciszewski/)

April 23, 2026

[open-source](/categories/open-source/), [research-practice](/categories/research-practice/), [testing](/categories/testing/), [tool-release](/categories/tool-release/)

Page content

* [When lists fall short](#when-lists-fall-short)
* [How Trailmark works](#how-trailmark-works)
* [The skills](#the-skills)
* [What Claude found](#what-claude-found)
  + [Equivalent mutants are the majority in well-tested crypto](#equivalent-mutants-are-the-majority-in-well-tested-crypto)
  + [Architectural bottlenecks are invisible without a graph](#architectural-bottlenecks-are-invisible-without-a-graph)
  + [Mutation testing finds what KATs can’t cover](#mutation-testing-finds-what-kats-cant-cover)
  + [Three patterns that showed up everywhere](#three-patterns-that-showed-up-everywhere)
* [Connecting the graph to everything else](#connecting-the-graph-to-everything-else)
* [Start querying your codebase](#start-querying-your-codebase)

We’re open-sourcing [Trailmark](https://github.com/trailofbits/trailmark), a library that parses source code into a queryable call graph of functions, classes, call relationships, and semantic metadata, then exposes that graph through a Python API that Claude skills can call directly. Install it now:

`uv pip install trailmark`

“Defenders think in lists. Attackers think in graphs. As long as this is true, attackers win.” John Lambert’s [widely cited observation](https://github.com/JohnLaTwC/Shared/blob/master/Defenders%20think%20in%20lists.%20Attackers%20think%20in%20graphs.%20As%20long%20as%20this%20is%20true%2C%20attackers%20win.md) about network security applies just as well to AI-assisted software analysis.

When Claude reasons about a codebase, it reasons about lists: findings from static analyzers, surviving mutants from mutation testing, and line-by-line coverage reports. But the question that actually matters is a graph question: *can untrusted input reach this code, and what breaks if it’s wrong?*

We built Trailmark to answer that question. It gives Claude a graph to think with instead of a list. We’re also releasing eight Claude Code skills we’ve built on top of it, designed for mutation triage, test vector generation, protocol diagramming, and more.

## When lists fall short

Mutation testing is a great example of a method that benefits from graph-level reasoning. It’s one of the best ways to measure test quality. It makes small changes to your source code (e.g., swapping a `<` for `<=`, replacing `+` with `-`) and checks whether your tests catch the difference. Mutants that survive reveal gaps in your test suite that code coverage metrics might miss. The downside is that a mutation testing run on a real codebase can produce hundreds of surviving mutants of varying significance. This is very much a *list*.

Some surviving mutants are *equivalent*: the mutation doesn’t change the program’s behavior because of structural or mathematical constraints that the mutation testing tool can’t see. Some are in dead code; some are in error message formatting; some are in the finite field arithmetic that underpins every cryptographic operation in your library. A flat list of surviving mutants doesn’t tell you which is which.

We wanted to know whether Claude could use graph-level reasoning about a codebase to automatically triage surviving mutants by security relevance: which are reachable from untrusted input, which affect high-blast-radius functions, and which represent genuine gaps in security-critical code?

## How Trailmark works

Trailmark uses [tree-sitter](https://tree-sitter.github.io/) for language-agnostic AST parsing and [rustworkx](https://www.rustworkx.org/) for high-performance graph traversal. It operates in three phases:

1. **Parse**: Walk a directory, extract functions, classes, call edges, type annotations, cyclomatic complexity, and branch counts from source code.
2. **Index**: Load the resulting graph into a rustworkx PyDiGraph with bidirectional ID/index mappings for fast traversal.
3. **Query**: Answer questions: callers, callees, all paths between two nodes, attack surface enumeration, and complexity hotspots.

It currently supports 17 languages, including C, Rust, Go, Python, PHP, JavaScript, Solidity, Circom, and Miden Assembly.

The graph is the substrate. The skills are where the analysis happens.

## The skills

The Trailmark plugin ships eight Claude Code skills that use the graph API as their backbone:

| Skill | What it does |
| --- | --- |
| `trailmark` | Build and query a code graph with pre-analysis passes: blast radius, taint propagation, privilege boundaries, and entrypoint enumeration |
| `diagram` | Generate Mermaid diagrams from code graphs: call graphs, class hierarchies, complexity heatmaps, data flow |
| `crypto-protocol-diagram` | Extract protocol message flow from source code or specs (RFCs, ProVerif, Tamarin) into annotated sequence diagrams |
| `genotoxic` | Triage mutation testing results using graph analysis: classify surviving mutants as equivalent, missing test coverage, or fuzzing targets |
| `vector-forge` | Mutation-driven test vector generation: find coverage gaps via mutation testing, then generate Wycheproof-style vectors that close them |
| `graph-evolution` | Compare code graphs at two snapshots to surface security-relevant structural changes that text diffs miss |
| `mermaid-to-proverif` | Convert Mermaid sequence diagrams into ProVerif formal verification models |
| `audit-augmentation` | Project SARIF and weAudit findings onto code graph nodes as annotations, enabling cross-referencing of static analysis results with blast radius and taint data |

Each skill calls the Trailmark Python API directly. When `genotoxic` triages a surviving mutant, it queries `engine.paths_between` to check reachability from untrusted input. When `diagram` generates a complexity heatmap, it calls `engine.complexity_hotspots`. The graph is what makes those questions answerable in seconds rather than hours of manual tracing.

Trailmark also ingests SARIF output from static analyzers and [weAudit](/2024/03/19/read-code-like-a-pro-with-our-weaudit-vscode-extension/) annotations, mapping external findings onto graph nodes by file and line range. This lets Claude layer static analysis results, audit notes, and mutation testing data onto a single unified graph, then query across all of them.

## What Claude found

We’ve been using these skills internally on several cryptographic libraries, combining graph analysis with language-appropriate mutation testing frameworks. Here’s what the graph let Claude see that flat lists couldn’t.

### Equivalent mutants are the majority in well-tested crypto

When we ran mutation testing against an Ed448 implementation in Go, 45 mutants survived out of 583 covered. A flat list of 45 surviving mutants looks like a serious test gap. But when Claude used the Trailmark call graph (332 nodes, 3,259 call edges) to triage via `genotoxic`, 33 of those 45 (73%) were equivalent mutants. The mutations were unobservable because the code’s mathematical structure constrained values more tightly than the explicit bounds checks that were mutated.

For example, nine surviving mutants modified boundary conditions in NAF (non-adjacent form) digit range checks. These look like real bugs in isolation. But the NAF digits are structurally bounded by the `nonAdjacentForm` algorithm itself: the values that would trigger the altered boundary can never appear. The graph confirmed these functions were called from specific contexts that made the mutations undetectable.

The 12 genuine gaps were concrete and actionable: a cross-package coverage gap where Go’s coverage profiling attributed execution to the calling package instead of the defining package, a 255-b...