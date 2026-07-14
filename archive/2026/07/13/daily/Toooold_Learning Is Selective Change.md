---
title: Learning Is Selective Change
url: https://toooold.com/2026/07/13/icml_recap3.html
source: Toooold
date: 2026-07-13
fetch_date: 2026-07-14T04:46:50.321544
---

# Learning Is Selective Change

[Toooold](/)
[ ]

[Make a CatGPT out of ChatGPT](/2023-02-02-cat_laser_chatgpt.html)[About](/about.html)

# Learning Is Selective Change

Jul 13, 2026

## Hidden gems found by random luck in the ICML 2026 workshops

Main-conference poster sessions reward planning. Workshop sessions reward luck.

![alt text](/images/icml3.jpg)

A workshop room can be three corridors away from the topic you intended to see, and the poster that changes your afternoon may be the one beside the coffee table rather than the one highlighted in the program. This third ICML reflection is limited to workshop papers I encountered through that kind of fortunate wandering.

The papers span theoretical physics, post-training, foundation models for simulation, Transformer inductive bias, model evaluation, interpretability, and multi-agent diagnosis. Their common question emerged only after I stopped grouping them by application:

> **When an AI system encounters an error or a new environment, what should change, where should that change be stored, and what evidence tells us that the change was useful?**

Learning is often described as parameter optimization. These workshop papers suggest a broader view. An AI system can change its current answer, its dialogue state, its inferred model of the environment, a selected subspace of its weights, or the interaction protocol among several agents. Every update preserves some structure and overwrites something else.

A useful update therefore balances three quantities:

\[U^\star = \arg\min\_U \mathcal{L}\*{\mathrm{new}}(U(s)) + \lambda \mathcal{D}\*{\mathrm{preserve}}(U(s),s) + \mu \mathcal{C}(U).\]

Here, (s) is the current state of the system, (\mathcal{L}*{\mathrm{new}}) measures the unresolved error, (\mathcal{D}*{\mathrm{preserve}}) measures damage to valuable existing structure, and (\mathcal{C}) represents the cost of the update.

The hard research problem lies in defining those terms. A critique can improve the current derivation while making the overall argument less coherent. Fine-tuning can raise benchmark accuracy while erasing general capabilities. A physics model can produce a plausible next frame while learning the wrong dynamics. A lower perplexity can reward confidence without rewarding correctness. A group of agents can agree because they share the same error.

The workshop papers became a study of **selective change**: changing the right variable, on the right timescale, while preserving the right invariants.

---

## Critique changes the solution before it changes the model

[When Does Critique Improve AI-Assisted Theoretical Physics? SCALAR](https://arxiv.org/abs/2605.06772) studies an Actor–Critic–Judge loop on graduate-level quantum field theory and string theory problems. An Actor proposes and revises a solution, a Critic provides feedback with access to a reference solution, and an independent Judge evaluates the successive attempts. The authors vary Actor personas, Critic styles, model families, and model scales. Multi-turn interaction generally improves on single-shot attempts, while the size and character of the gain depend strongly on the Actor–Critic pairing. Constructive feedback is particularly useful when a weaker Actor is paired with a stronger Critic; strict or adversarial feedback provides no universal advantage. ([arXiv](https://arxiv.org/abs/2605.06772?utm_source=chatgpt.com "When Does Critique Improve AI-Assisted Theoretical Physics? SCALAR: Structured Critic--Actor Loop for Agentic Reasoning"))

The important object is the response of the solution to feedback:

\[G\_t = S\_{t+1} - S\_t,\]

where (S\_t) is the quality of the solution after revision (t). A capable Critic can identify the correct error and still produce little gain when the Actor cannot interpret or incorporate the feedback. A milder Critic may outperform a more aggressive one by locating a repair within the Actor’s current competence.

This resembles educational scaffolding more than debate. A useful teacher does not enumerate every flaw simultaneously. The teacher identifies the next misconception that the student can repair. The value of feedback therefore depends on its correctness, novelty, timing, and usability.

SCALAR also offers an instructive evaluation method: track the sequence of revisions rather than only the final score. Two systems with identical final performance can have very different internal dynamics. One may repair a decisive error after a single critique. Another may oscillate among alternative mistakes. A third may repeatedly rewrite the answer while changing little of substance.

For scientific agents, this suggests measuring **critique susceptibility**: how efficiently a system converts feedback into improved work. When gains flatten, the appropriate response may be to switch Critics, decompose the problem, invoke a symbolic tool, or ask for human input. Continuing the same dialogue merely generates more tokens.

The broader lesson is that many failures should be repaired in the current artifact before they trigger a model update. A wrong sign in a derivation calls for a local correction. A systematic inability to reason about gauge invariance may justify a deeper change. The skill lies in distinguishing the two.

---

## Context can carry learning without changing weights

[Towards a Physics Foundation Model](https://arxiv.org/abs/2509.13805) moves adaptation from dialogue into latent state estimation. Its General Physics Transformer is trained on approximately 1.8 TB of simulation data covering several fluid, thermal, multiphase, and fluid–solid systems. Given a short history of physical states, the model infers enough of the local dynamics to predict future states, including zero-shot experiments on unseen physical systems and boundary conditions. ([arXiv](https://arxiv.org/abs/2509.13805?utm_source=chatgpt.com "Towards a Physics Foundation Model"))

The task is naturally expressed through a latent dynamics variable (z):

\[p(u\_{t+1} \mid u\_{t-k+1:t}) = \int p(u\_{t+1} \mid u\_t,z) p(z \mid u\_{t-k+1:t}),dz.\]

The model observes a short trajectory, infers a local description of how this world evolves, and uses that inferred state to generate the next step. The weights remain fixed while the effective model changes through context.

This is closely related to system identification in control theory. An engineer observes inputs and outputs, estimates the hidden dynamics, and then predicts or controls the system. A physics foundation model amortizes that procedure across many simulated worlds.

The architecture also contains an important scientific design choice. The Transformer estimates a temporal derivative, while a numerical integration step advances the state. Spatial and temporal derivative features provide additional numerical structure. The learned component handles cross-domain inference; the integration interface supplies a stable computational scaffold. ([arXiv](https://arxiv.org/pdf/2509.13805?utm_source=chatgpt.com "Towards a Physics Foundation Model"))

This hybrid structure is more inspiring than a slogan about learning physics from raw data. It suggests that general scientific models may arise from broad learned representations connected through well-chosen numerical interfaces. A neural component can infer the regime, parameters, or operator, while established solvers enforce part of the update structure.

Variable time increments are another methodological gem. When all trajectories share the same sampling interval, visual displacement can become a shortcut for temporal dynamics. Varying the interval forces the model to infer time scale from the context. Similar experiments could be useful in language-model research: change surface format, naming, scale, or tokenization while preserving the underlying operation, then test whether the model infers the mechanism or recognizes the dataset.

The central unresolved question is what kind of latent model has been inferred. The context may identif...