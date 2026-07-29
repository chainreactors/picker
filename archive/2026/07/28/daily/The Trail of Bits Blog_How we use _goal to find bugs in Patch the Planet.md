---
title: How we use /goal to find bugs in Patch the Planet
url: https://blog.trailofbits.com/2026/07/28/how-we-use-goal-to-find-bugs-in-patch-the-planet/
source: The Trail of Bits Blog
date: 2026-07-28
fetch_date: 2026-07-29T05:02:53.346404
---

# How we use /goal to find bugs in Patch the Planet

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# How we use /goal to find bugs in Patch the Planet

[Trail of Bits](/authors/trail-of-bits/)

July 28, 2026

[open-source](/categories/open-source/), [vulnerabilities](/categories/vulnerabilities/), [machine-learning](/categories/machine-learning/)

Page content

* [1. Let Codex write the goal](#1-let-codex-write-the-goal)
* [2. Define the outcome, not the path](#2-define-the-outcome-not-the-path)
* [3. Assign one outcome per agent](#3-assign-one-outcome-per-agent)
* [Where human judgment is needed](#where-human-judgment-is-needed)

Codex’s `/goal` feature amplifies bug hunting, but getting good results requires the right prompt, the right scope, and the right number of outcomes per run. For [Patch the Planet](https://trailofbits.com/patch-the-planet), our joint initiative with OpenAI to find and fix bugs in open-source software, we pointed Codex at some of the most widely used, heavily audited codebases in the world, like Rust, curl, and zlib. One tool came up again and again in our internal bug-report channels: `/goal`, which hands Codex an open-ended objective and lets it work independently toward a success condition. Here are a few highlights:

* `/goal` found every Rust bug we submitted, including a soundness hole and a miscompilation now patched in Rust 1.98, from a single variant-analysis pipeline.
* It turned every project’s past CVEs into Semgrep rules that had to fire on the vulnerable version and stay silent on the patched one, then flagged 11 variant hits across multiple projects.
* It uncovered two potential high-severity privilege-escalation bugs in Keycloak’s SAML component during a discovery run.

Over the first few weeks of Patch the Planet, our engineers independently converged on three techniques for using `/goal`. We found that getting the most out of `/goal` means treating the prompt as a set of specific success criteria, not a set of instructions. (Note that this blog post uses `/goal` to refer to goal-based prompting in general. Codex can also set goals for itself through a tool call, and that’s how we recommend everyone use it; we rarely type the slash command ourselves.)

## 1. Let Codex write the goal

The art of using `/goal` is prompt design, and we found that Codex knows Codex the best. Internally, our single most repeated `/goal` tip was to use Codex to help write each `/goal` prompt. We hand Codex threat model files and the context about what we’re looking for, and then tell it to write the goal prompt. As mentioned before, `/goal` is a tool Codex can invoke on itself, and a few engineers stopped typing goals by hand entirely.

> $goal-prompt based on threat model write goal to find single critical issue (RCE) exploitable by remote attacker for kubernetes-client. the kubernetes-client is used in normal config, malicious remote users exploits.

Figure 1: A meta-prompt from one of our engineers asking Codex to create a goal prompt. Results are shown in figure 2.

This works because Codex knows the target and its own tendencies better than we can specify up front. It can translate a threat model into concrete, testable success criteria, name the code paths worth prioritizing, and phrase the outcome precisely enough that a run actually converges. A goal written this way tends to be tighter than one we’d write cold, and it takes a fraction of the time.

Letting the model draft the goal also closes a gap we’d otherwise miss. Any outcome you define can be satisfied in ways you didn’t intend, and the model is often the first to spot where the easy outs are.

Now when we ask Codex to draft a goal, we ask it to red-team its own goal by identifying the ways a future model might be lazy in its approach, and to revise the criteria to remove them before the run starts. We also built tooling that makes it easier for Codex to verify its own work. For example, we noticed Codex has a tendency to skip reading the entire codebase even when explicitly asked. We built [aicov](https://github.com/trailofbits/aicov), a tool that tracks what lines of code Codex has actually read, so it can’t “cheat.”

This is an iterative process. As we find more shortcuts a model takes, we exclude them from the next version of the prompt.

## 2. Define the outcome, not the path

A good goal names the outcome, defines it precisely, and then enforces persistence:

> /goal Audit the kubernetes-client repository in this workspace to find exactly one previously unreported critical remote code execution vulnerability reachable in normal/default client configuration by a malicious remote user or server that controls only network/API responses, Kubernetes objects the client legitimately fetches, or other remote data accepted during normal use.
>
> First build a concise threat model of realistic remote attacker entry points and trust boundaries, then prioritize code paths involving deserialization, YAML/JSON/protobuf parsing, dynamic imports/eval/template execution, archive/file extraction, auth redirects, generated client hooks, websocket/exec/attach/port-forward streams, and subprocess or filesystem effects. Do not assume attacker control of local kubeconfig, CLI arguments, environment variables, installed plugins, source code, credentials, privileged cluster/admin access, or prior code execution; explicitly reject findings that rely on those preconditions. Before accepting a candidate, search local known-findings files plus current open issues/PRs for duplicates, then produce a minimal safe proof that demonstrates attacker-controlled code execution or a direct RCE primitive under the stated normal configuration. Stop after one valid critical issue. Write finding to ./findings/ folder.

Figure 2: The prompt created by Codex from figure 1

We found the best philosophy is to **spend as many tokens as you need defining the outcome, and almost none telling the model how to get there.**

If you want the bug found through fuzzing, “use fuzzing” is as far as you should go. “Build on top of my existing fuzzing harness” or “build a new fuzzing harness” are both worse. There might be an existing harness that’s just as good. A goal that prescribes the path guarantees Codex never takes another one, and you lose the judgment and open-ended problem solving that make `/goal` unique.

The outcome side takes more care because it has to be calibrated. If it’s too specific, Codex doesn’t have enough to search and the value of an autonomous `/goal` run is unclear. When we fed Codex the exact root cause of a known bug and asked it to find variants, it found nothing. The scope was too narrow. When we cut the input down to a single sentence describing the *class of bugs* it should look for based on the known bug, it surfaced numerous bugs. We reported 9 of them, with 3 already fixed and merged upstream.

If an outcome is too vague, the model provides outputs that don’t match what you were looking for. One of the worst `/goal` prompts we saw during Patch the Planet was “find bugs in [X].” The model had no way to tell when it was done. It just kept running, surfacing bugs that had no real-world impact, and wasting tokens.

A complete outcome definition also says what doesn’t count as done. The open-source projects in Patch the Planet have some of the most audited code in the world, and more than once `/goal` came back with “no bugs found.” We treat that as an intermediate result, not a completion condition, and write persistence into the goal itself.

**The most effective resource for `/goal` bug hunting is a `THREAT_MODEL.md` file.** We ended up referencing a threat model file in almost every goal we ran because it precisely defines what valid bugs look like without explaining how to find them. We recommend every open-source project create one.

## 3. Assign one outcome per agent

Putting two competing outcomes in one `/goal` prompt results in uneven ...