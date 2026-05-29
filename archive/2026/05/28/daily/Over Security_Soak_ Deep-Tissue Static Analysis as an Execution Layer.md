---
title: Soak: Deep-Tissue Static Analysis as an Execution Layer
url: https://armoredcode.com/blog/soak-deep-tissue-static-analysis-as-an-execution-layer/
source: Over Security
date: 2026-05-28
fetch_date: 2026-05-29T06:06:09.800167
---

# Soak: Deep-Tissue Static Analysis as an Execution Layer

[Armored Code](/)

[Blog](/blog/)
[Newsletter](https://mailchi.mp/a61f93445c94/armored-code-newsletter)

# Soak: Deep-Tissue Static Analysis as an Execution Layer

February 2026

## Introduction

Modern application security is no longer about running a single scanner.

It’s about coordinating multiple engines, covering different ecosystems, and extracting consistent signals from heterogeneous outputs.

That coordination problem is what led to the creation of Soak.

Soak is a zero-dependency Docker image that aggregates a curated set of open-source security scanners into a single, reproducible execution environment.

Its purpose is simple:

> Provide deep-tissue static analysis through a unified, containerized execution layer.

### The Real Problem: Toolchain Fragmentation

ecurity scanners are powerful — but fragmented.

Each tool:

* Requires its own runtime (Python, Go, Java, Ruby…)
* Has its own CLI conventions
* Produces different output formats
* Evolves independently
* Introduces version drift across environments

Managing multiple scanners across local development, CI, and production becomes operationally expensive.

If your execution layer is unstable, everything built on top of it becomes unreliable.

Soak removes that instability.

### What Soak Is

Soak is:

* A single Docker image based on openSUSE Tumbleweed
* A multi-engine static analysis runtime
* An automated language and ecosystem detection layer
* A structured output generator (soak\_summary.json)
* A reproducible, versionable scanning environment

It is intentionally:

* Stateless
* Self-contained
* Docker-only
* Automation-friendly

If you have Docker, you can run Soak. Nothing else is required.

### Deep-Tissue Static Analysis

Soak performs what we call deep-tissue static analysis.

Instead of running one scanner, it:

1. Detects the project ecosystem (e.g., pom.xml, Gemfile, go.mod, Python metadata)
2. Activates relevant engines
3. Executes multiple scanners
4. Aggregates structured results into a summary JSON file

This provides multi-layer visibility across:

* Source code vulnerabilities
* Dependency vulnerabilities (SCA)
* Secrets detection
* Infrastructure misconfigurations
* Shell and container linting
* Code quality and complexity metrics

All from a single execution context.

### Included Scanners

Soak bundles a broad range of open-source tools across ecosystems:

#### Multi-Language

* Semgrep
* Trivy

#### Python

* Bandit
* Mypy
* Radon
* Pip-audit

#### Ruby

* Dawnscanner
* Brakeman

#### Java

* PMD
* SpotBugs

#### Go

* Gosec
* Govulncheck
* Staticcheck

#### Secrets

* Gitleaks

#### Infrastructure / DevOps

* Hadolint
* Checkov
* ShellCheck

This provides horizontal coverage across application, dependencies, configuration, and container layers.

#### Execution Model

Soak follows a clear internal structure:

1. Detection Layer - Identifies project language and ecosystem metadata.
2. Execution Layer - Runs relevant scanners inside the container in isolation.
3. Aggregation Layer - Collects raw JSON outputs and produces soak\_summary.json.

This separation allows Soak to act as a pure execution component that can integrate seamlessly with higher-level orchestration systems.

### Designed for Automation

Running Soak is intentionally simple:

```
soak /home/user/my-awesome-project
```

Behind the scenes, the container mounts the target repository, performs detection, executes scanners, and writes a structured summary file.

Because the entire runtime is containerized:

* CI/CD behavior matches local execution
* Tool versions are pinned and reproducible
* No runtime installation is required
* No dependency resolution occurs at execution time

This dramatically reduces environmental inconsistencies.

### Soak and Signal-Engine

Within the ArmoredCode ecosystem, Soak serves as the execution layer behind Signal-Engine.

The architectural separation is deliberate:

* Soak executes
* Signal-Engine ingests and correlates

Soak does not:

* Perform scoring
* Maintain baselines
* Correlate findings
* Apply risk models

It generates structured, multi-engine signals.

Signal-Engine transforms those signals into intelligence.

### Why Centralize the Toolchain?

Many scanners provide official Docker images.

However, using them independently introduces:

* Multiple container contracts
* Inconsistent entrypoints
* Divergent output structures
* Distributed version management

Soak centralizes the contract.

Instead of managing N scanner containers, orchestration systems interact with one unified execution environment.

This reduces complexity and increases control.

### Security by Design

Soak executes scanners against potentially untrusted code.

Therefore:

* The container is minimal and controlled
* Execution is ephemeral
* No persistent state is stored
* Capabilities are limited to what is required

Execution should not increase the attack surface.

Isolation is a design principle, not an afterthought.

### Off-by-one

Security analysis at scale requires architectural discipline.

Execution, ingestion, correlation, and scoring must be separated.

Soak exists to make the execution layer:

* Deterministic
* Reproducible
* Multi-engine
* Containerized
* Automation-ready

It provides deep-tissue static analysis through a single, consistent interface.

And in a fragmented scanner ecosystem, consistency is power.

© 2012 - 2026 Armored Code. All rights
reserved.