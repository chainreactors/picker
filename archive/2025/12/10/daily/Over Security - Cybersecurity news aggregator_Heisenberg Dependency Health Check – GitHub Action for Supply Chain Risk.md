---
title: Heisenberg Dependency Health Check – GitHub Action for Supply Chain Risk
url: https://www.darknet.org.uk/2025/11/heisenberg-dependency-health-check-github-action-for-supply-chain-risk/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-10
fetch_date: 2025-12-11T03:24:39.117037
---

# Heisenberg Dependency Health Check – GitHub Action for Supply Chain Risk

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![Darknet – Hacking Tools, Hacker News & Cyber Security](https://www.darknet.org.uk/wp-content/uploads/2022/12/cropped-darknet_2022_logo.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

# Heisenberg Dependency Health Check – GitHub Action for Supply Chain Risk

November 21, 2025

Views: 431

Heisenberg Dependency Health Check is a GitHub Action that inspects *only* the new or modified dependencies introduced in a pull request. It analyses lockfiles or manifest changes, gathers health and risk signals from deps.dev and other heuristics, and posts a detailed dependency health report directly on the pull request. It highlights suspicious, low-quality, or unusually fresh packages before they reach your main branch.

![Heisenberg Dependency Health Check - GitHub Action for Supply Chain Risk](https://www.darknet.org.uk/wp-content/uploads/2025/11/Heisenberg-Dependency-Health-Check-GitHub-Action-for-Supply-Chain-Risk-640x427.jpg)

## Overview

Modern supply-chain attacks increasingly rely on introducing malicious or low-trust dependencies through everyday development workflows. Traditional scanners often run periodically and focus on known vulnerabilities, which miss early indicators of risk. Heisenberg takes a different approach: it hooks directly into the pull request, detects which packages were added or updated, and reviews them in isolation. Running at merge time, it gives reviewers actionable risk signals exactly when decisions are made.

The tool is ecosystem-agnostic and supports Python, JavaScript, and Go dependency formats. It can detect unusual publish timings, maintenance red flags, popularity issues, suspicious scripts, and other patterns associated with supply-chain compromise. If configured, it can also label or block pull requests that exceed risk thresholds.

## Features

* **Delta-based scanning**: evaluates only new or changed dependencies rather than rescanning the entire dependency graph.
* **Multi-ecosystem support**: works with `poetry.lock`, `requirements.txt`, `uv.lock`, `package-lock.json`, `yarn.lock` and `go.mod`.
* **Risk and health signals**: pulls advisories, maintenance metrics, popularity data, dependents, and incredibly fresh publishes that may indicate rushed or suspicious releases.
* **npm script checks**: highlights post-install script behaviours that attackers frequently abuse.
* **Pull request reporting**: posts a structured dependency health comment with links to package intelligence sources.
* **Policy controls**: can add a security review label or fail the job if risky packages are introduced.

## Installation

The following workflow is taken directly from the Heisenberg documentation and should be placed inside `.github/workflows/` in your repository. It monitors standard dependency files and runs the action whenever one of them changes.

name: Heisenberg Health Check
on:
pull\_request:
paths:
- "\*\*/poetry.lock"
- "\*\*/uv.lock"
- "\*\*/package-lock.json"
- "\*\*/yarn.lock"
- "\*\*/requirements.txt"
- "\*\*/go.mod"
permissions:
contents: read
pull-requests: write
issues: write
jobs:
deps-health:
runs-on: ubuntu-latest
steps:
- uses: actions/checkout@v4
- name: Detect changed manifest
id: detect
run: |
git fetch origin ${{ github.base\_ref }} --depth=1
LOCK\_PATH=$(git diff --name-only origin/${{ github.base\_ref }} | \
grep -E 'poetry.lock$|uv.lock$|package-lock.json$|yarn.lock$|requirements.txt$|go.mod$' | head -n1 || true)
echo "lock\_path=$LOCK\_PATH" >> $GITHUB\_OUTPUT
- name: Heisenberg Dependency Health Check
uses: AppOmni-Labs/heisenberg-ssc-gha@v1
with:
package\_file: ${{ steps.detect.outputs.lock\_path }}

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34 | name: Heisenberg Health Check  on:  pull\_request:  paths:  - "\*\*/poetry.lock"  - "\*\*/uv.lock"  - "\*\*/package-lock.json"  - "\*\*/yarn.lock"  - "\*\*/requirements.txt"  - "\*\*/go.mod"    permissions:  contents: read  pull-requests: write  issues: write    jobs:  deps-health:  runs-on: ubuntu-latest  steps:  - uses: actions/checkout@v4    - name: Detect changed manifest  id: detect  run: |  git fetch origin ${{ github.base\_ref }} --depth=1  LOCK\_PATH=$(git diff --name-only origin/${{ github.base\_ref }} | \  grep -E 'poetry.lock$|uv.lock$|package-lock.json$|yarn.lock$|requirements.txt$|go.mod$' | head -n1 || true)  echo "lock\_path=$LOCK\_PATH" >> $GITHUB\_OUTPUT    - name: Heisenberg Dependency Health Check  uses: AppOmni-Labs/heisenberg-ssc-gha@v1  with:  package\_file: ${{ steps.detect.outputs.lock\_path }} |

## Usage

Once the workflow is active, the process is automatic:

* A pull request modifies a dependency manifest.
* The workflow detects the change and hands the specific file to Heisenberg.
* Heisenberg evaluates only the added or modified packages.
* A health report appears as a comment on the pull request.
* Optional: risky changes can trigger a label or cause the job to fail, blocking the merge.

Teams using additional GitHub Action hardening tools, such as [Claws](https://www.darknet.org.uk/2025/06/claws-github-actions-workflow-linter-for-secure-ci-cd-pipelines/), can pair Heisenberg with workflow linting to reduce risks from both automated misuse and compromised dependencies.

## Attack Scenario

**Objective**: demonstrate how a hostile dependency attempt would be detected during a realistic development flow.

1. Set up a demo repository with the Heisenberg workflow enabled.
2. Add or bump a dependency known for suspicious activity, poor maintenance, or very recent publishes.
3. Open a pull request as if performing a routine update.
4. Heisenberg evaluates only the changed dependency and posts a health report highlighting all relevant concerns.
5. Point stakeholders to the flagged signals as evidence of supply-chain risk and why automated guardrails matter.

This adversarial modelling pairs well with internal reviews using Darknet’s write-ups on automation abuse, such as [Weaponizing Dependabot](https://www.darknet.org.uk/2025/06/weaponizing-dependabot-exploiting-github-automation-for-supply-chain-attacks/), helping teams understand how automated tooling can be exploited without proper controls.

## Red Team Relevance

Although Heisenberg is built for defenders, red teams can use it to:

* Identify weak or unvetted dependency update practices in target environments.
* Model realistic compromise paths that depend on dependency injection or typosquatting.
* Show how quickly risk would be caught if the organisation had Heisenberg or similar controls in place.

It also pairs naturally with supply-chain reconnaissance tools and GitHub workflow analysis techniques. For example, secret-exposure tools like [Veles](https://www.darknet.org.uk/2025/08/veles-googles-open-source-secret-scanner-for-gcp-key-detection/) excel at key detection, while OAuth-abuse research such as [GitPhish](https://www.darknet.org.uk/2025/06/gitphish-oauth-device-code-phishing-for-github-repos-secrets-and-ci-cd/) highlights broader risks inside CI/CD ecosystems.

## Detection and Mitigation

* **Restrict dependency changes to pull requests** so that Heise...