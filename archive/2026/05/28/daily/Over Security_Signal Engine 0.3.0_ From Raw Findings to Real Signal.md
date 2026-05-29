---
title: Signal Engine 0.3.0: From Raw Findings to Real Signal
url: https://armoredcode.com/blog/signal-engine-0.3.0-from-findings-to-signal/
source: Over Security
date: 2026-05-28
fetch_date: 2026-05-29T06:06:10.205444
---

# Signal Engine 0.3.0: From Raw Findings to Real Signal

[Armored Code](/)

[Blog](/blog/)
[Newsletter](https://mailchi.mp/a61f93445c94/armored-code-newsletter)

# Signal Engine 0.3.0: From Raw Findings to Real Signal

March 2026

Security tools are easy to run.

What’s hard is making sense of their output.

If you’ve ever tried combining results from multiple scanners, you already know
the problem:

duplicated findings inconsistent severity models noisy reports no clear way to
prioritize risk

[Signal Engine 0.3.0](https://github.com/armoredcode/signal-engine/releases/tag/0.3.0)
is a step toward fixing that.

Not by adding more scanners — but by turning raw findings into something you can
actually reason about.

## A new foundation: standardization first

At the core of this release is one fundamental change: signal engine now speaks
SARIF natively.

This means it can ingest results from tools like:

* dr\_source
* GitHub CodeQL
* Gitleaks, Trivy, Ruff
* Brakeman, Gosec, Checkov, Hadolint, Dawnscanner

All normalized into a consistent internal model.

Different tools. Different formats. **One pipeline.**

## Deduplication that actually works

Running multiple tools usually creates overlap. Same issue. Slightly different
location. Different tool.

Before 0.3.0, that noise was your problem. Now it’s handled by the engine.

A new `dedup` command introduces proximity-based deduplication, powered by a
clustering algorithm that groups findings within a configurable line threshold.

This is not string matching. This is **context-aware** deduplication.

Because in real codebases, the same vulnerability rarely appears exactly on the
same line.

## Clustering: From Findings to Patterns

The new `smart_cluster` algorithm changes how findings are interpreted.

Instead of treating each issue as isolated, Signal Engine groups them into
clusters of related risk.

This enables:

* aggregation across tools
* grouping by code proximity
* better identification of problematic areas

It’s the difference between:

> “You have 37 issues”

and

> “You have 3 risky zones in your codebase”

## Hotspots: where risk actually lives

One of the most important additions in this release is the `hotspots` command.

It introduces a simple but powerful idea: risk is not just severity; it’s
density.

Signal Engine now calculates a risk score per 1000 lines of code, combining:

* vulnerability count
* severity weighting
* file-level metrics (via cloc integration)

This surfaces the areas where:

* issues concentrate
* risk compounds
* attention is actually needed

Not all files are equal. Now you can see which ones matter.

## Risk scoring that reflects reality

Severity is no longer just a label.

It’s now part of a weighted scoring model:

* Critical → 10.0
* High → 5.0
* Medium → 3.0
* Low → 1.0
* Info → 0.1

This feeds directly into hotspot detection and analytics. A single critical
issue is not the same as ten informational warnings, and your tooling should
reflect that.

## Better ingestion, less friction

Real-world tool output is messy.

This release improves ingestion across the board:

* Support for multiple JSON structures (including SARIF `runs[]`)
* Smarter nested parsing for complex outputs
* Automatic language detection from file extensions
* Integrated handling of cloc metrics alongside findings
* Consistent loading for both single files and directories

In short: less preprocessing, more analysis.

## A usable interface (finally)

Signal Engine is still a CLI tool — but now it’s one you actually want to use.

* Clean, simplified tables
* Semantic coloring for severity and paths
* A redesigned info panel with repository metadata
* Color-coded hotspots based on risk density

The goal wasn’t aesthetics. It was readability under pressure.

## Under the hood

A lot changed to support this direction:

* Refactored ingestion and normalization pipeline
* Consolidated previously fragmented logic
* Removed redundant modules
* Fixed inconsistencies in severity mapping across tools
* Stabilized metrics ingestion and analysis flows

Less duplication. More coherence.

## Where this is going

Signal Engine is evolving toward a clear goal: make multi-tool security analysis
understandable.

Not louder. Not bigger. **Sharper.**

© 2012 - 2026 Armored Code. All rights
reserved.