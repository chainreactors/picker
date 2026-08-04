---
title: First Principle of Agent Harness Engineering: From Continuation to Control
url: https://toooold.com/2026/08/03/first_principle_harness.html
source: Toooold
date: 2026-08-03
fetch_date: 2026-08-04T04:59:53.975711
---

# First Principle of Agent Harness Engineering: From Continuation to Control

[Toooold](/)
[ ]

[Make a CatGPT out of ChatGPT](/2023-02-02-cat_laser_chatgpt.html)[About](/about.html)

# First Principle of Agent Harness Engineering: From Continuation to Control

Aug 3, 2026

## Why loops, graphs, and swarms are trying to solve the same agent failure

I am getting tired of tracing all the so-called agent harness engineering techniques. You must feel the same.

![alt text](/images/agent_harness.jpg)

First, the answer was better prompts. Then it was tool use. Then came memory, reflection loops, graphs, planners, evaluators, multi-agent teams, and swarms. Each technique has its own terminology, diagrams, frameworks, and success stories. Each fixes something, yet each also creates another class of failures that requires another layer of orchestration.

After a while, the field begins to resemble a growing collection of patches whose names change faster than the problem underneath them.

I kept seeing the same pattern. A loop was presented as the solution to brittle one-shot agents. A graph was introduced to control an unreliable loop. A swarm was proposed to overcome the limits of one planning path. Then an evaluator, memory layer, or deterministic solver was added to control the failures introduced by the previous layer.

Rather than continuing to trace every new framework, I wanted to understand the first principle. What failure are all these harnesses trying to contain, and why does that failure exist in the first place?

The answer became clearer when I stopped thinking of the LLM as a weak state machine and started from what it actually does. An LLM continues trajectories, while an agent is expected to control them. The gap between those two functions explains much of modern agent engineering.

## How a small mistake becomes a trajectory

Imagine asking a research agent to investigate a technical question and publish a report.

The original request contains one ambiguous sentence. The agent chooses a reasonable interpretation, generates search queries from that interpretation, and retrieves sources that appear to support it. It summarizes those sources into memory. A later agent receives the summary rather than the original evidence, and an evaluator reads the same framing and approves the final report.

No individual step needs to look absurd. The first interpretation may have been highly plausible. The retrieved evidence may have been real. The summary may accurately reflect the selected sources, and the evaluator may correctly judge that the report is internally coherent. The final result can still be wrong because of a discrepancy that entered five steps earlier.

This is the characteristic failure of LLM-orchestrated systems. A local discrepancy becomes part of the next agent state, the next decision is conditioned on that altered state, and the discrepancy gains persistence, confidence, and eventually consequence as the trajectory continues.

The same pattern appears in more consequential tasks. An agent misreads the intended recipient and drafts the correct message for the wrong person. Another agent verifies the wording without checking the recipient, and a final tool call sends it. A coding agent misunderstands one architectural constraint and writes tests that encode its own misunderstanding. The tests pass, so their success becomes evidence that the implementation is correct. A tool request times out after the operation succeeds, and the agent interprets the timeout as failure, retries, and performs the action twice.

In each case, a probable local continuation becomes future context, future context becomes accepted state, and accepted state eventually becomes an external consequence.

A simple way to describe this dynamic is:

\[\delta\_{t+1} \leq L\_t \delta\_t + \epsilon\_t\]

Here, $\delta\_t$ represents the discrepancy already present in the trajectory, $\epsilon\_t$ is the new error introduced at the current step, and $L\_t$ describes how strongly the surrounding system propagates the previous discrepancy.

Unrolling the recurrence shows how every local error is weighted by the transitions that follow it:

\[\delta\_T
\lesssim
\sum\_{i=0}^{T-1}
\left(
\prod\_{j=i+1}^{T-1} L\_j
\right)
\epsilon\_i\]

This makes an important point precise. A longer trajectory is not automatically less reliable. The horizon matters through the product of the later amplification factors. A long coding session can remain stable when compilers, tests, version control, and environmental observations repeatedly pull the agent back toward reality. A two-step payment workflow can be unstable when one transition has a large and irreversible consequence.

When the effective values of $L\_t$ stay below one, discrepancies contract. A compiler reports the actual syntax failure, a constraint solver rejects an impossible plan, a transaction receipt establishes what happened, or an independent source challenges a mistaken premise.

When the surrounding system simply preserves previous outputs, discrepancies remain. When the model consumes its own summaries, agents repeat one another’s claims, or actions irreversibly alter the environment, discrepancies can grow.

Agent reliability therefore depends on more than local model quality. It depends on the discrepancy dynamics created by the orchestration around the model.

## Continuation is a proxy for control

A language model learns a conditional distribution over plausible continuations. Given the trajectory represented in its context, it proposes what may come next:

\[a\_t \sim p\_\theta(a\_t \mid h\_t)\]

The history $h\_t$ may contain the user request, previous reasoning, tool calls, observations, retrieved documents, memory summaries, and messages from other agents.

Large-scale training gives the model compressed patterns of successful planning, expert decisions, software workflows, tool use, correction, negotiation, and explanation. Post-training further shapes those continuations toward useful, safe, and instruction-following behavior.

This makes continuation an extraordinarily powerful proxy for control. When an agent encounters a familiar problem, it can generate the next step associated with successful examples of that problem. It can produce a plan, call a tool, inspect the result, and continue in a way that resembles an effective problem-solving trajectory.

A controller faces a different objective. It must choose an intervention according to the future world states that intervention is expected to produce:

\[a\_t^\*
=
\underset{a}{\operatorname{argmax}}
\mathbb{E}
\left[
U\left(s\_{t+1:T}\right)
\mid
s\_t,\operatorname{do}(a)
\right]\]

The distinction between $h\_t$ and $s\_t$ is central. The model conditions on a representation of the trajectory, while the action affects the actual world state. The representation may be incomplete, stale, ambiguous, or partly generated by the model itself.

A tool timeout may correspond to several different realities. The operation may have failed, succeeded before the connection closed, or succeeded twice after a retry. The visible trajectory may preserve none of these distinctions.

The model’s actions also change the environment, the changed environment produces the next context, and earlier outputs become later inputs. Once an error enters the trajectory, the model may be reasoning from a situation partly created by its own mistake.

This creates the learning–control gap. Learning rewards strong average predictions across a distribution of observed examples, while control requires stability along the particular sequence of states produced by the policy’s own actions. High average next-step accuracy cannot guarantee that one self-generated trajectory will remain close to the intended path.

A second gap appears at the boundary between probability and consequence. A small change in model output can select a different tool, recipient, branch, or commit operation. The probability distribution changes smoothly while the external world changes d...