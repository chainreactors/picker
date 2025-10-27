---
title: AIxCC finals: Tale of the tape
url: https://blog.trailofbits.com/2025/08/07/aixcc-finals-tale-of-the-tape/
source: The Trail of Bits Blog
date: 2025-08-08
fetch_date: 2025-10-07T00:17:04.372688
---

# AIxCC finals: Tale of the tape

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# AIxCC finals: Tale of the tape

Trail of Bits

August 07, 2025

[aixcc](/categories/aixcc/), [research-practice](/categories/research-practice/), [darpa](/categories/darpa/), [machine-learning](/categories/machine-learning/)

Page content

* [A geographically diverse field](#a-geographically-diverse-field)
* [Vulnerability discovery](#vulnerability-discovery)
  + [Enhancing traditional security tools with AI](#enhancing-traditional-security-tools-with-ai)
  + [AI-first with traditional validation](#ai-first-with-traditional-validation)
  + [Hybrid approach](#hybrid-approach)
* [Proof of vulnerability (PoV) generation](#proof-of-vulnerability-pov-generation)
  + [Traditional fuzzing-based PoV generation](#traditional-fuzzing-based-pov-generation)
  + [AI-enhanced traditional methods](#ai-enhanced-traditional-methods)
  + [AI-first PoV generation](#ai-first-pov-generation)
* [Patching](#patching)
* [What we’ve learned so far](#what-weve-learned-so-far)

The results of DARPA’s AI Cyber Challenge (AIxCC) finals will be announced this week, revealing which team will claim the $4 million first prize for building the best AI system that automatically finds and fixes vulnerabilities in real-world code. For real-time updates and access to our CRS tool Buttercup, follow [@dguido](https://x.com/dguido) on X or visit our [Buttercup website](https://www.trailofbits.com/buttercup/)

Over the last few weeks, [CTF Radiooo interviewed each of the seven finalists](https://www.youtube.com/%40ctfradiooo) about their differing approaches to creating their own cyber reasoning system (CRS). These interviews reveal a diversity of technical approaches and philosophical differences regarding AI integration and risk tolerance. Should AI integration supplant or supplement traditional tools? How aggressive should teams be in submitting proofs of vulnerability (PoVs) and patches? What’s the best use of the teams’ LLM budgets? While the winner has not yet been announced, these differences show that there are multiple viable paths forward to using AI for vulnerability detection.

## A geographically diverse field

Of the seven finalists, four teams are based in universities, and three are from private companies. Team members are spread across the globe, and there is a blend of collaborators among the finalists made up of other universities and companies. Each team’s home base is located in the US.

* **Private companies:** **Trail of Bits** (New York City); **LACROSSE** (Minneapolis); **Theori** (Austin, TX)
* **Academia**: **42-b3yond-6ug** (Northwestern University); **all\_you\_need\_is\_a\_fuzzing\_brain** (Texas A&M University); **Shellphish** (Arizona State University); **Team Atlanta** (Georgia Institute of Technology)

![Map showing locations of AIxCC finalists](/img/aixcc_finals_tale_of_the_tape_figure_1.jpg)

Figure 1: Locations of AIxCC finalists

But geographic diversity is just the tip of the iceberg. What truly separates the teams is their unique approaches to vulnerability discovery, generating PoVs, and patching. What follows is our best guess about each team’s technical strategies, based on their CTF Radiooo interviews. We haven’t seen their code, but this is what we think is true about their approach.

## Vulnerability discovery

The seven finalists can be split into three philosophical camps based on the vulnerability discovery that motivated their system design.

### Enhancing traditional security tools with AI

**Trail of Bits**, **Shellphish**, and **LACROSSE** built systems rooted in fuzzing, static analysis, and vulnerability research and enhanced them with LLMs. **Trail of Bits** uses LLMs to generate seed inputs for traditional fuzzing tools to improve their code coverage and ability to find inputs that trigger specific kinds of vulnerabilities. **Shellphish’s** “Grammar Guy” uses LLMs to generate and evolve progressive grammars based on a feedback loop that analyzes uncovered code paths. **LACROSSE** deploys 300–500 fuzzing agents (a scale similar to Trail of Bits’) that are orchestrated by “Optimus Zero” and use LLMs for higher-level reasoning tasks that require semantic understanding. They also used LLMs to create “vulnerability objects” when a crash occurs to describe, categorize, and plan for patching.

### AI-first with traditional validation

**all\_you\_need\_is\_a\_fuzzing\_brain** and **Theori** use LLMs as the primary reasoning engine and traditional security tools for validation and fallback mechanisms. Of all the finalists, **all\_you\_need\_is\_a\_fuzzing\_brain** has the most AI-forward approach, using LLMs for vulnerability analysis, system architecture, strategic decision-making, and code generation. Not only that, but about 90% of their codebase was written using AI assistance. **Theori’s** approach uses LLM agents that follow reverse engineering workflows that are constrained to prevent the AI from wandering. Their system uses static analysis tools, like Infer, to generate thousands of bug candidates, and the LLM agents use reasoning to determine actual vulnerabilities and reduce false positives.

### Hybrid approach

**Team Atlanta** and **42-b3yond-6ug** balance AI with traditional methods, each with unique specializations. To our knowledge, **Team Atlanta** is the only team to use fine-tuned custom models on Llama 7B with extensive fine-tuning specialized specifically for C programming language analysis. **42-b3yond-6ug** applies “super patches,” which is an LLM-based patching process able to fix two or more different bugs at once, even when those bugs appear unrelated. Their system can recognize when multiple different crashes stem from the same underlying vulnerability.

## Proof of vulnerability (PoV) generation

PoVs serve as the foundation of the AIxCC scoring system because they demonstrate that vulnerabilities can actually be triggered. PoV+patch combinations earn significantly higher point values than patches submitted without PoV. The competition’s scoring system also rewards speed and accuracy. Furthermore, PoVs can be used to bypass other teams’ patches and reduce competitors’ accuracy multipliers, which adds an interesting game theory element to the competition.

### Traditional fuzzing-based PoV generation

**LACROSSE’s** PoV generation occurs through established fuzzing methods, focusing on agent orchestration rather than AI-driven vulnerability discovery. Their approach prioritizes proven fuzzing reliability over experimental AI techniques, with Optimus Zero managing global state and task distribution among traditional security tools.

**42-b3yond-6ug** also maintains traditional fuzzing as the core PoV generation mechanism. Their approach includes SARIF integration for static analysis report validation and multi-fuzzer coordination through reinforcement-learning-based scheduling.

### AI-enhanced traditional methods

**Trail of Bits** uses LLMs to generate Python programs that create specialized seed inputs for traditional fuzzing tools that leverage implicit understanding of complex formats like SQL injection and path traversal attacks. These specialized inputs have been added to the fuzzer’s coverage-guided corpus of inputs to improve fuzzing performance. This approach is optimized specifically for improved harness saturation time (to meet competition time constraints) and for using AI to generate semantically aware inputs that traditional mutational fuzzing struggles with.

**Shellphish** enhances traditional fuzzing with “Grammar Guy,” which uses LLMs to generate progressive grammars that evolve based on coverage feedback, targeting complex input formats and protocols. This approach improves the ability to fuzz formats like SQL, URLs, and binary protocols, with grammars continuously refined based on program exploration results. This AI-driven grammar generation approach consumes a...