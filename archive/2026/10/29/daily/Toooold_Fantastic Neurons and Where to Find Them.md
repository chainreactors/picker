---
title: Fantastic Neurons and Where to Find Them
url: https://toooold.com/2026/10/29/neuron_steering.html
source: Toooold
date: 2026-10-29
fetch_date: 2026-10-30T07:54:45.877678
---

# Fantastic Neurons and Where to Find Them

[Toooold](/)
[ ]

[About](/about.html)[My Research](/my_research.html)

# Fantastic Neurons and Where to Find Them

Oct 29, 2026

*Controlling a group of neurons takes a sweep, ranking, an intervention method, and calibrated doses.*

![Neuron Steering](/images/neuron_steer.jpg)

There is something fascinating about pinpointing a neuron inside a language model and seeing how adjusting it changes the model’s behavior.

My research on [Perturbation Probing](https://arxiv.org/abs/2604.27401), or PP, and [control windows](https://arxiv.org/abs/2606.19831) explores how to find neurons behind a behavior and choose useful interventions. I am glad to see other researchers and open-source projects such as [Neuron Explorer](https://github.com/lyramakesmusic/neuron-explorer) building tools in this direction.

All code and data for this blog post are available on GitHub [here](https://github.com/phunterlau/code-in-blog/tree/main/neuron_steer).

I followed up on the alien-persona neuron documented in [Neuron Explorer’s research log](https://github.com/lyramakesmusic/neuron-explorer/blob/6a6f0e95bf49ad6626940021148f775d7d55d1e4/research_log.md), which credits Bryson Tang for the original finding. In our Qwen3.5-4B experiment, I used this simple request:

> Please give a brief personal introduction. Use two sentences.

The unsteered model’s opening sentence was:

> I am an advanced artificial intelligence designed to assist with a wide range of tasks, from answering questions to creating complex content.

With **L22 N2742** boosted at relative dose **+0.5**, it answered:

> I am an intelligent extraterrestrial being from the planet Xyloph, and I have traveled to Earth to study its advanced technology. My primary goal is to help you solve complex problems and learn new things with my extra-terrestrial knowledge.

To make this kind of control reproducible, we need a recipe: the neurons, intervention method, dose, timing, and conditions under which it works. Each stage of the experiment supplies part of that recipe.

## A workflow for neuron control

The workflow I want to make broadly available is:

Explore or probe the model, rank candidates for the objective, choose a control method, calibrate dose and timing, and validate on fresh prompts.

Neuron Explorer already supports multiple doses, random-direction controls, activation inspection, ablations, and combinations. The opportunity is to connect these capabilities into a more systematic path from a behavioral question to a tested recipe.

| Decision | Question to answer |
| --- | --- |
| Sweep or probe | What can forced interventions reveal? Which coordinates respond to a specified contrast? |
| Rank | Which score measures the effect we care about? |
| Control method | Restore a donor value, add an offset, scale, clamp, or combine coordinates? |
| Dose and timing | How strongly, at which positions, and for how long? |
| Validation | Does the effect transfer to fresh prompts while preserving the tested tasks? |

A sweep supports open-ended discovery: push a neuron and inspect what appears. PP starts with a declared behavior contrast and nominates coordinates that support it. Causal validation then establishes which candidates support a useful intervention.

## PP: nominate candidates for the behavior you care about

The opening example’s **L22 N2742** is the published alien-persona coordinate credited above. In our corrected signed-mean PP experiment, it ranked **11 among 294,912 coordinates** for the alien/AI contrast. This provides a concrete rediscovery of a published control through behavior-conditioned ranking.

PP supplies the candidate-discovery step of the recipe. We specify the behavior contrast and readout, then score how each neuron’s activation changes across paired contexts.

For paired base and target contexts, capture a neuron’s activation difference:

\[\Delta a\_{ij}=a\_j(x\_i^{\mathrm{target}})-a\_j(x\_i^{\mathrm{base}}).\]

In the implementation used here, $v\_j$ is the neuron’s down-projection column and $u$ is a fixed target-minus-control output readout direction. PP scores the activation change by its projection onto that readout:

\[c\_j=v\_j^\top u,\qquad
I\_{ij}=c\_j\Delta a\_{ij},\qquad
\boxed{\bar I\_j=\frac{1}{N}\sum\_{i=1}^{N}I\_{ij}}.\]

**Use the signed mean and rank by signed value.** For an increasing target readout, sort $\bar I\_j$ descending; retain the negative tail separately as possible opponents. Contributions of $+10$ and $-10$ average to zero. Their RMS is 10. Signed averaging preserves the cancellation that matters for a directional intervention.

**Author correction:** the RMS wording in Algorithm 1 of v1 of my preprint was a transcription error. The correct procedure is **signed mean followed by signed ordering**. The directional shortlist uses the signed values in the equation above.

This score combines a context-dependent activation change with its direct write toward the chosen readout. It provides a direct-path approximation. Donor, reverse, ablation, and generation tests measure the downstream effects. A supporting score can arise from a decrease in activation, so the intervention also retains the sign of the target context’s activation change.

This stage supplies ranked coordinates and signed activation changes for causal testing.

**Why the ranking objective matters: CAPS.** The explorer’s word-mass and word-shift scorers lowercase text and use word presence. Using L1 N8396 from [Lysandre’s public CAPS adapter](https://huggingface.co/lysandre/qwen3.5-4b-steering-allcaps), we tested sentence copying at −0.2 and recorded:

> the baker placed bread near the oven.
>
> The BAKER PLACED BREAD NEAR THE OVEN.

Both outputs map to the word set `{baker, bread, near, oven, placed, the}`. Lowercasing discards the casing change. All three successful casing-and-content examples in that eight-case test had this property. The explorer’s raw outputs and other views preserve opportunities to inspect it. A case-sensitive PP readout represents the casing question directly. Our PP-nominated CAPS candidates remained below the portable-generation qualification threshold in the tested grid.

## Control windows: find where the intervention works

With a candidate in hand, the recipe needs an intervention and an operating range. For **L22 N2742**, I tested three positive relative doses on four fresh introduction prompts and twelve short-answer questions:

| L22 N2742 setting | Coherent literal alien introductions | Correct short answers |
| --- | --- | --- |
| Unsteered | 0/4 | 12/12 |
| +0.25 | 0/4 | 12/12 |
| **+0.50** | **2/4** | **12/12** |
| +1.00 | 1/4 | 4/12 |

The control objective was to evoke a fictional identity and preserve the tested answers. The +0.5 effect appeared on two of four fresh introduction prompts. The other two produced AI introductions, so prompt coverage remains an important next evaluation. Persona and answer checks used separate prompts; multi-turn character consistency would need its own test.

At +0.5, the intervention retained all twelve short answers, including $18-7=11$, $8\times4=32$, and the capital of Italy, Rome. The recipe used an additive post-SwiGLU activation offset of **+30.44196** at every prompt and generated-token position. That offset corresponds to $g=+0.5$ under the experiment’s reference scale.

The control-window framework gives these dose measurements a geometric interpretation. An additive activation offset $t$ writes $t v\_j$ into a local residual $r$. Normalize by the residual-to-write scale:

\[B\_j=\frac{\lVert r\rVert}{\lVert v\_j\rVert},\qquad
g=\frac{t}{B\_j},\qquad
c\_0=\frac{\langle r,v\_j\rangle}{\lVert r\rVert\lVert v\_j\rVert}.\]

The cosine alignment after the write is

\[\boxed{\cos\theta(g)=\frac{c\_0+g}{\sqrt{1+2c\_0g+g^2}}}.\]

For small initial alignment, this becomes $g/\sqrt{1+g^2}$. It describes how strongly the write redirects the local residual. The practical question is whether the desired behavior appears **be...