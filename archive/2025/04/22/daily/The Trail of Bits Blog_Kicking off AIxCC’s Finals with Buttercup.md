---
title: Kicking off AIxCC’s Finals with Buttercup
url: https://blog.trailofbits.com/2025/04/21/kicking-off-aixccs-finals-with-buttercup/
source: The Trail of Bits Blog
date: 2025-04-22
fetch_date: 2025-10-06T22:04:50.776282
---

# Kicking off AIxCC’s Finals with Buttercup

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Kicking off AIxCC’s Finals with Buttercup

Michael D. Brown

April 21, 2025

[aixcc](/categories/aixcc/), [darpa](/categories/darpa/), [machine-learning](/categories/machine-learning/)

Page content

* [Budget and time expansions](#budget-and-time-expansions)
* [Multiple competition rounds](#multiple-competition-rounds)
* [Multiple challenge types](#multiple-challenge-types)
  + [1. Delta-scan challenges](#1-delta-scan-challenges)
  + [2. Full-scan challenges](#2-full-scan-challenges)
  + [3. SARIF broadcasts](#3-sarif-broadcasts)
* [Enabling custom AI model development](#enabling-custom-ai-model-development)
* [Flexible computing resources](#flexible-computing-resources)
* [Scoring algorithm changes](#scoring-algorithm-changes)
  + [New point-scoring opportunities](#new-point-scoring-opportunities)
  + [New scoring modifiers](#new-scoring-modifiers)
* [What’s next for Buttercup?](#whats-next-for-buttercup)

DARPA’s AI Cyber Challenge (AIxCC) Finals Competition is officially underway, and our CRS (Cyber Reasoning System) Buttercup is up to the challenge! What began as a tightly constrained competition has become more ambitious. Teams can now build custom AI models, control their own infrastructure, and tackle multiple types of security challenges simultaneously. With these new challenges also comes more resources—teams now have $1,000 or more to tackle each challenge versus just $100 in the semifinals.

These changes aren’t just bigger numbers on a spreadsheet. They are enabling competitors to build systems that more closely resemble practical security tools rather than academic proofs of concept. The expanded flexibility in technical approaches also means we’ll see more innovative applications of AI to cybersecurity problems—approaches that simply weren’t possible under the semifinal constraints.

Here’s how the competition has changed and why it matters:

## Budget and time expansions

The most significant shift in the finals is the increase in resources available to each team. In the semifinals, competing systems operated under tight constraints that limited analysis depth and approach:

* **Time**: Only 4 hours to analyze each challenge
* **AI budget**: Only $100 to spend on commercial AI API calls (e.g., ChatGPT, Claude) per challenge
* **Compute budget**: Fixed allocation of virtual machines with limited scaling options

For the finals, these constraints (subject to change) are now:

* **Time**: 8+ hours per challenge
* **AI budget**: $10,000 for commercial AI API calls per round (multiple challenges per round)
* **Compute budget**: $20,000 to spend on Azure resources (servers, VMs, GPUs) per round (multiple challenges per round)

These added resources let us perform more thorough analysis over a more practical timeframe. With longer analysis windows per challenge and increased resources per round, Buttercup can:

* Perform deeper dynamic analysis and run more comprehensive testing on patches
* Increase scaling of resource-intensive tasks like fuzzing
* Use a wider variety of commercial AI models for a wider variety of tasks than was possible in the semifinals

## Multiple competition rounds

Unlike the semifinals’ single scored round, the finals consist of three unscored exhibition rounds that allow teams to iteratively improve their CRS in advance of a final, scored round:

| Round | Open | Scoring | Key Parameters |
| --- | --- | --- | --- |
| Exhibition 1 | 1 April | Unscored | $20K compute and $10K AI budget 2 total challenges, max 2 concurrent 48hr challenge window delta-scan challenges only |
| Exhibition 2 | 6 May | Unscored | $20K compute and $10K AI budget 15-30 total challenges, max 4 concurrent 8hr delta-scan, 24hr full-scan challenge window All challenge types |
| Exhibition 3 | 3 June | Unscored | Parameters TBD (announced 30 days prior) |
| Final Round | 24 June | Scored | Parameters TBD (announced 30 days prior) |

*Table 1: Competition structure for finals*

This progression is significant because it encourages systems that can adapt to shifting requirements—an essential quality for real-world security tools. It also allows competitors to iteratively refine their approaches based on feedback from previous rounds, making the final systems unveiled at DEFCON 2025 more robust.

## Multiple challenge types

The most technically significant change is the introduction of multiple challenge types. The semifinals featured only one type of challenge problem - real-world open-source software with reduced git histories of less than 100 commits, each of which may or may not introduce a vulnerability. Challenges in the finals are still based on real-world open-source software, but now consist of:

### 1. Delta-scan challenges

These challenges provide a codebase and a single diff that introduces vulnerabilities. While the codebase includes fuzzing harnesses to start from, the diff provides the CRS with an additional starting point for identifying and patching vulnerabilities.

### 2. Full-scan challenges

These present a flat codebase with vulnerabilities already incorporated. With no diff to start from, the CRS must perform wider analysis of the codebase using only the fuzzing harnesses to start from in order to find vulnerabilities.

### 3. SARIF broadcasts

These challenges provide static analysis alerts in SARIF format, which may be true or false positives. The CRS must evaluate the alert and determine whether it represents a real vulnerability, then optionally provide a patch.

This diversification is crucial because real-world vulnerabilities can be found through multiple channels—from code reviews, static analysis tools, fuzzing, and runtime monitoring. Systems that can handle all these inputs will be significantly more valuable in practical security settings.

## Enabling custom AI model development

In what may be the most significant policy change for the competition, DARPA now allows competitors to use custom AI/ML models. In the semifinals, systems were restricted to using only third-party models from Anthropic, OpenAI, and Google. Now, competitors can develop and deploy their own specialized models, provided they’re approved for the competition and can be reproduced.

Instead of being limited to general-purpose commercial models, teams can now:

* Fine-tune models specifically for security vulnerability detection
* Create specialized models for different aspects of vulnerability analysis
* Develop lightweight, efficient models for repetitive tasks

There are still guardrails to ensure fair competition: custom models cannot be pre-trained to memorize information about historical vulnerabilities in open-source software. This prevents teams from simply teaching their models about known issues and ensures systems demonstrate genuine reasoning capabilities.

## Flexible computing resources

Another significant technical shift gives competitors direct control over their infrastructure. Rather than the fixed allocation of computing resources in the semifinals, teams now receive an Azure subscription with the round compute budget as their only constraint.

This means teams can make strategic decisions about resource allocation based on each challenge’s unique requirements such as:

* Dedicating more powerful hardware to compute-intensive fuzzing campaigns
* Allocating expensive GPU instances for running custom AI models
* Scaling resources dynamically based on challenge complexity
* Running multiple analysis pipelines in parallel

This flexibility enables teams to experiment with different allocation strategies during the unscored rounds, determining which approaches yield the best results for different types of challenges.

## Scoring algorithm changes

The AIxCC finals maintain the core scoring principle that patches are worth substantially more than vulnerability discovery alone, but add new dimen...