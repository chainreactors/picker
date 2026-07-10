---
title: The Model Chooses a Future Before It Says a Token
url: https://toooold.com/2026/07/09/icml_recap.html
source: Toooold
date: 2026-07-09
fetch_date: 2026-07-10T05:58:38.237606
---

# The Model Chooses a Future Before It Says a Token

[Toooold](/)
[ ]

[Make a CatGPT out of ChatGPT](/2023-02-02-cat_laser_chatgpt.html)[About](/about.html)

# The Model Chooses a Future Before It Says a Token

Jul 9, 2026

## What I learned from ICML 2026 through interpretability, alignment, post-training, and agent safety

ICML is an excellent fitness program disguised as a machine learning conference. My phone recorded roughly 20,000 steps a day, so this review has a natural methodological limitation: it covers eight poster sessions and is bounded by my walking distance.

![alt text](/images/icml_snapshot.jpg)

I filtered those sessions through the questions closest to my research: how aligned behavior is represented, how post-training changes model internals, how safety mechanisms fail under distribution shift, how agents decide when to act, and how interpretability can move from explaining behavior toward changing it.

One idea kept resurfacing:

> **A model often chooses a future before the final answer makes that choice visible.**

The commitment may happen through an internal feature, an expert route, a reasoning branch, a retrieved passage, a social-response channel, or a tool action. I use *margin* loosely here to mean the model’s relative preference between such competing futures: one reasoning branch over another, refusal over compliance, correct evidence over a distractor, or a safe action over an unsafe one.

Before ICML, I often asked which feature, neuron, or direction controlled a behavior.

After eight poster sessions—and many corridors between them—the more useful question became:

> **Where does the decision first become visible, when does it become causal, and is there still time to intervene?**

---

## 1. Reasoning, steering, and interpretability

### Thinking helps when it improves the next decision

Several papers converged on a view of reasoning as a sequence of local decisions rather than a monolithic chain of thought.

[How does Chain of Thought decompose complex tasks?](https://arxiv.org/abs/2604.08872) models reasoning as the decomposition of a difficult classification problem into a tree of smaller ones. The analysis produces an optimal depth: shallow reasoning leaves the original decision too hard, while excessive depth accumulates new opportunities for error. [SmartThinker](https://arxiv.org/abs/2603.08000) reaches a related conclusion from the training side. A fixed length penalty can compress difficult solutions too aggressively, so the desired reasoning budget should depend on the problem and on the distribution of successful response lengths. ([arXiv](https://arxiv.org/abs/2604.08872 "[2604.08872] How does Chain of Thought decompose complex tasks?"))

For a reasoning state ($h\_t$), the object I care about can be written as

\[\Delta\_t = \log p\left(\text{good next branch}\mid h\_t\right) - \log p\left(\text{bad next branch}\mid h\_t\right).\]

The branch might be a mathematical subgoal, a correction to an earlier assumption, a safe continuation, or a decision to verify rather than guess. A useful reasoning step improves the future decision landscape. Overthinking begins when new steps add low-margin branches without resolving the old uncertainty.

[SafeThink](https://arxiv.org/abs/2602.11096) made this temporal view particularly concrete. Its main empirical result is that many unsafe reasoning trajectories can be redirected with a short corrective prefix during the first few reasoning steps. The important object is therefore not merely whether the final answer is safe, but how early the trajectory remains recoverable. ([arXiv](https://arxiv.org/abs/2602.11096?utm_source=chatgpt.com "Safety Recovery in Reasoning Models Is Only a Few Early Steering Steps Away"))

This resembles a classical feedback-control problem. The intervention should arrive after enough evidence of drift has appeared, yet before the trajectory has settled into a harmful basin. Heavy intervention everywhere wastes control effort and increases collateral effects; late intervention edits the surface after the decisive branch has already been taken.

### Sparse routes carry large behavioral effects

The same structure appeared inside model architectures.

[Sparse Models, Sparse Safety](https://arxiv.org/abs/2602.08621) shows that MoE safety can depend on a small set of router decisions: manipulating a few safety-critical routers can redirect computation toward unsafe routes. [TraceRouter](https://arxiv.org/abs/2601.21900) extends the routing view beyond explicit MoE routers by tracing harmful semantic influence through cross-layer feature paths. ([arXiv](https://arxiv.org/abs/2602.08621?utm_source=chatgpt.com "Sparse Models, Sparse Safety: Unsafe Routes in Mixture-of-Experts LLMs"))

Attention provided another version of the story. [Surgery](https://arxiv.org/abs/2602.05228) links harmful fine-tuning to changes in attention-sink divergence and regularizes that statistic during adaptation. [The Structural Origin of Attention Sink](https://arxiv.org/abs/2605.06611) traces sink formation back to variance discrepancies in value aggregation, their amplification by super neurons, and resulting dimensional imbalance. The interesting commonality is how a small statistical asymmetry can be amplified into a stable routing pattern. ([arXiv](https://arxiv.org/abs/2602.05228 "[2602.05228] Surgery: Mitigating Harmful Fine-Tuning for Large Language Models via Attention Sink"))

This makes sparsity both attractive and dangerous. Sparse mechanisms offer interpretable handles, yet a safety property concentrated in a few routes can also be bypassed through small perturbations or post-training updates. The relevant question is therefore not simply whether a component has causal leverage. A useful control point needs enough behavioral reach, a tolerable side-effect profile, and a nontrivial operating window.

### Steering has a geometry and a schedule

Two steering papers clarified why finding a direction is only part of the problem.

[Spherical Steering](https://arxiv.org/abs/2602.08169) replaces additive displacement with rotation on a representation sphere, separating angular movement toward a target behavior from radial norm distortion. [Steer Like the LLM](https://arxiv.org/abs/2605.03907) starts from another observation: prompting does not induce the same activation shift at every token. Prompt Steering Replacement learns state- and position-dependent coefficients that approximate the intervention pattern produced by a successful prompt. ([arXiv](https://arxiv.org/abs/2602.08169 "[2602.08169] Spherical Steering: Geometry-Aware Activation Rotation for Language Models"))

Together with early trajectory correction, these papers outline three coupled questions:

* **When** is the trajectory still steerable?
* **Where** in the model is the target distinction represented and used?
* **How** should the intervention move the state without pushing it off-manifold?

Before ICML, I thought of steering mainly as direction discovery.

After ICML, steering looks more like a policy over layer, time, geometry, and dose.

### Visibility, causality, and long-horizon influence

A useful hidden gem was [Automatic Layer Selection for Hallucination Detection](https://arxiv.org/abs/2605.26366). Its FEPoID criterion selects intermediate layers where hallucination-related signals become especially detectable. The broader lesson is that “where to look” is already part of the mechanism: a signal can be absent from one layer, linearly visible in another, and causally committed somewhere else. ([arXiv](https://arxiv.org/abs/2605.26366?utm_source=chatgpt.com "Automatic Layer Selection for Hallucination Detection"))

For each behavior, I now want to separate four questions:

1. Is the relevant information represented?
2. Is it visible in a usable coordinate system?
3. Is it causally used?
4. Is the outcome still changeable at that point?

[Towards Long-Horizon Interpretability](https://arxiv.org/abs/2602.01914) supplies an important complem...