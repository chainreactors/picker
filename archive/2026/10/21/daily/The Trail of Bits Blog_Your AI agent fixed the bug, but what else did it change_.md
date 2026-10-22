---
title: Your AI agent fixed the bug, but what else did it change?
url: https://blog.trailofbits.com/2026/10/21/your-ai-agent-fixed-the-bug-but-what-else-did-it-change/
source: The Trail of Bits Blog
date: 2026-10-21
fetch_date: 2026-10-22T06:45:16.851915
---

# Your AI agent fixed the bug, but what else did it change?

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Your AI agent fixed the bug, but what else did it change?

Anish Naik, Marcelo Morales

October 21, 2026

[patch-the-planet](/categories/patch-the-planet/), [open-source](/categories/open-source/), [vulnerabilities](/categories/vulnerabilities/), [ai](/categories/ai/)

Page content

* [Standardizing the patching process](#standardizing-the-patching-process)
* [How we designed the plugins](#how-we-designed-the-plugins)
* [regression-hunt reduces false positive rates](#regression-hunt-reduces-false-positive-rates)
* [patching-bugs streamlines best practices from thousands of agent sessions](#patching-bugs-streamlines-best-practices-from-thousands-of-agent-sessions)
* [What’s next for the plugins](#whats-next-for-the-plugins)
* [The industry needs to focus on patching](#the-industry-needs-to-focus-on-patching)

Today we’re publishing [patching-bugs](https://github.com/trailofbits/skills/tree/main/plugins/patching-bugs) and [regression-hunt](https://github.com/trailofbits/skills/tree/main/plugins/regression-hunt), two plugins that let engineers delegate patch development and regression checks to agents. Our patching-bugs plugin reproduces reported bugs, develops fixes, and tests them. The regression-hunt plugin checks whether any changes break previously working and supported behavior. Engineers can direct the work and review their results; maintainers can supply their own security assumptions and patching requirements, so the agents work within the project’s rules.

We built patching-bugs and regression-hunt through [Patch the Planet](https://trailofbits.com/patch-the-planet/), our joint initiative with OpenAI, where we’ve co-authored hundreds of security patches for widely used open-source projects. Motivated by our major successes on projects like [Scapy](https://github.com/trailofbits/publications/blob/master/presentations/Auditing%20Scapy%20With%20Agents/README.md), our plugins draw on our analysis of merged patches and thousands of our engineers’ Codex sessions.

The plugins provide maintainers with a structured workflow, evidence, independent checks, and best practices to improve their patching hygiene. In our preliminary evaluations, regression-hunt produces 25% fewer false-positive findings than a baseline Codex agent prompted to “review the PR for regressions.”

## Standardizing the patching process

Our [September post](/2026/09/15/1passwords-ai-patching-benchmark-is-misleading/) reported regressions introduced by some of our Patch the Planet patches. Since then, we’ve reviewed every patch that a Trail of Bits engineer authored and maintainers merged upstream. The review confirmed 21 regressions from over 130 PRs merged: 16 functional, one performance, and four build/test. None broke a security protection.

(“Regression” refers to a new defect introduced by a change that breaks previously correct and supported behavior along a path a real user or attacker can reach.)

For each patch, an agent looked for potential regressions, confirmed each one with a proof-of-concept (PoC) run before and after the change, and then passed the results to an engineer for review.

The review was noisy: today’s bug disclosures arrive at an unprecedented speed and scale, and for patching to keep pace, the industry needs to increase its signal-to-noise ratio. The 21 confirmed regressions were identified among 58 candidates in a single run (~36% precision). But because agents take many different approaches and reach different results, each run generates more candidates to manually sort through.

That led us to two conclusions:

1. To introduce fewer regressions, we needed a standard way to write patches, with the same checks applied every time.
2. To catch the regressions we still introduce, we needed a standard way to check for them, with written rules for what counts as a regression.

Standardizing both steps also makes every run repeatable and comparable. No fixed checklist will catch every regression, so we collect agent trajectories from our engineers’ patching sessions, and use the tasks that an earlier version failed to benchmark for the next one (figure 1).

![“Figure showing the feedback loop for generating and evaluating patches.”](/2026/10/21/your-ai-agent-fixed-the-bug-but-what-else-did-it-change/patching_figure1_hu_fd1b211e358e4802.webp)

Figure 1: Feedback loop for generating and evaluating patches.

## How we designed the plugins

We used two primary sources to guide the design of our plugins: a review of every patch we merged upstream and the thousands of Codex sessions our engineers used to write those patches.

This led to four principles that shaped our patching-bugs and regression-hunt plugins:

1. **Opinionated guidance in as few words as possible.** We give the agent wide latitude and record only Trail of Bits’ judgment of what constitutes a good patch and a real regression. The goal is to direct the agent towards the desired result with the least possible guidance.
2. **Modular steps.** You don’t have to run either plugin end-to-end, as both provide multiple skills that can be used in tandem or in isolation.
3. **Strict input and output schemas.** Every step takes and returns a defined schema that includes the claim, the code revision, the required check, the raw evidence, and open questions. Fixed schemas reduce variability across runs and allow each step to verify the previous step’s work rather than trusting its summary.
4. **A live proof of concept for every claim.** Every conclusion depends on a PoC run against a live deployment: a built, running instance of the project, reached through the interfaces a real user would use. When reproducing a bug, proving a fix, and confirming a regression, if a step can’t produce a live PoC, its result is inconclusive.

## regression-hunt reduces false positive rates

The regression-hunt plugin (Figure 2):

1. **Enumerates** **candidate regressions** by tracing the changed code (the diff) through its callers to its real interfaces.
2. **Reproduces** each candidate regression on a **live deployment of the system.**
3. **Replays** the PoC on the live deployment on a **fresh-context agent.**
4. **Judges** the results of all the previous steps to validate that the **proof meets the requirements of a regression.**

![“Figure showing the regression-hunt workflow”](/2026/10/21/your-ai-agent-fixed-the-bug-but-what-else-did-it-change/patching_figure2_hu_ba5a49e1c64e072d.webp)

Figure 2: The regression-hunt workflow.

In addition to the four principles above, there are two core aspects that are critical to the plugin:

1. **Defining a regression:** The plugin has strong opinions about what a regression is and, more importantly, what a regression is NOT. The burden of proof is placed on the agent (specifically during the “adjudication agent” step) to prove that there is sufficient evidence to show that the suspected regression is not a false positive, an incomplete fix, a latent bug, a pre-existing bug, and so on. The plugin only reports a regression if all of these gates are passed.
2. **Incorporating a threat model:** If a threat model is available, the orchestrator will intentionally pass this document as part of the global context for each individual agentic step. This is an attempt to require each step/agent to refer back to the threat model before reaching its conclusion.

Our review of merged PRs yielded a set of 21 confirmed regressions that we could use to evaluate regression-hunt. We used the whole set to compare the plugin with a baseline Codex agent prompted to “review the PR for regressions.”

Across those runs, regression-hunt produced 25% fewer false-positive findings than the baseline, with a 95% confidence interval of 14% to 38%. Its strict evidence requirements also left some known regressions classified as borderline: the plugin identified a possible regre...