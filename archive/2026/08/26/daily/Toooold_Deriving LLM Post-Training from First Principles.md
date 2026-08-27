---
title: Deriving LLM Post-Training from First Principles
url: https://toooold.com/2026/08/26/posttraining.html
source: Toooold
date: 2026-08-26
fetch_date: 2026-08-27T12:12:45.622695
---

# Deriving LLM Post-Training from First Principles

[Toooold](/)
[ ]

[Make a CatGPT out of ChatGPT](/2023-02-02-cat_laser_chatgpt.html)[About](/about.html)

# Deriving LLM Post-Training from First Principles

Aug 26, 2026

I have been reading Nathan Lambert’s [RLHF Book](https://rlhfbook.com/) and following his lecture and video series. What I appreciate most is the way he has systematically organized a rapidly evolving field into an engineering framework. SFT, reward models, PPO, DPO, RLVR, distillation, regularization, infrastructure, and newer agentic methods often appear as separate topics, while his treatment makes their engineering relationships much easier to see.

I wanted to approach the same landscape from a complementary direction. With my physics background, I naturally ask whether a complicated collection of methods can be reconstructed from a small set of primitives, like Coulomb’s law for classical electromagnetism. One can begin with a simple interaction such as $F = k\_e \frac{q\_1 \times q\_2}{r^2}$, then introduce additional structure only when the current description becomes insufficient. To be clear: Maxwell’s equations are not derived from Coulomb’s law alone, but we haven’t had Maxwell’s equations for LLM, right?

![alt text](/images/posttraining.jpg)

Start from SFT and cross-entropy, ask exactly what information it contains, identify what it cannot express, then add one new degree of freedom at a time. Following that path, much of modern post-training can be organized around four conceptual transitions: from likelihood to preference, from offline projection to on-policy optimization, from sequence generation to environment interaction, and from scalar reward to distributional feedback. The individual algorithms then become branches of these transitions rather than isolated inventions.

This post works like an equation heavy note, but don’t be afraid. I will use a small set of annotations consistently: $x$ denotes the input or prompt, $y$ a generated response, $a\_t$ the token or action taken at step $t$, and $s\_t$ the corresponding model state or interaction context. The policy is $\pi\_\theta$, while $p\_{\mathcal D}$ denotes an external data distribution. Rewards are written as $R$ or $r$, advantages as $A\_t$, and $\pi\_{\mathrm{ref}}$ denotes a reference policy when one is needed. For agentic settings, $\tau$ denotes a full trajectory and $P\_{\mathrm{env}}$ the environment transition dynamics. I will use $D\_{\mathrm{KL}}(p\Vert q)$ in the standard direction, with the first argument defining the sampling distribution inside the expectation.

Disclaimer: this post is edited with LLM assistance.

# I. From likelihood to preference

## Cross-entropy as the primitive interaction

Let an autoregressive policy be (as in many GPT-style models)

\[\pi\_\theta(y\mid x)
=
\prod\_{t=1}^{T}
\pi\_\theta(y\_t\mid x,y\_{<t}).\]

Given demonstrations sampled from a data distribution,

\[(x,y)\sim p\_{\mathcal D},\]

supervised fine-tuning minimizes

\[\mathcal L\_{\mathrm{SFT}}
=
-
\mathbb E\_{(x,y)\sim p\_{\mathcal D}}
\left[
\log \pi\_\theta(y\mid x)
\right].\]

At token level,

\[\mathcal L\_{\mathrm{SFT}}
=
-
\mathbb E
\left[
\sum\_t
\log \pi\_\theta(y\_t\mid x,y\_{<t})
\right].\]

The objective contains a remarkably simple form of supervision. At each training state, the data identifies a target token and increases its probability. If

\[p\_v=\operatorname{softmax}(z)\_v,\]

then the gradient with respect to a logit is (p-y) in numpy or:

\[\frac{\partial \mathcal L}{\partial z\_v}
=
p\_v-\mathbf 1[v=y^\*].\]

The target token is pushed upward in probability, while alternatives are suppressed through softmax normalization. This is enough to support imitation, instruction following, and large amounts of behavioral shaping because the pretrained model already contains a rich distribution of latent capabilities.

The limitation follows from the same equation. Cross-entropy identifies a target but carries no explicit representation of relative quality among alternatives. Suppose two complete responses $y\_A$ and $y\_B$ are both plausible, while one is more factual, more concise, safer, or better calibrated. If the dataset contains only $y\_B$, the optimization increases its likelihood, but the loss does not directly encode the relation

\[y\_B \succ y\_A.\]

This becomes important whenever post-training is less about teaching an unseen capability and more about shifting probability between behaviors that already exist in the pretrained model. That missing relational structure motivates preference optimization.

## Preference introduces a relative coordinate

A preference pair adds the ordering

\[y\_w \succ y\_l.\]

A common latent-variable model represents this ordering through a scalar reward

\[r\_\phi(x,y),\]

with pairwise preference probability

\[P(y\_w\succ y\_l\mid x)
=
\sigma
\left(
r\_\phi(x,y\_w)-r\_\phi(x,y\_l)
\right).\]

The corresponding loss is

\[\mathcal L\_{\mathrm{RM}}
=
-
\mathbb E
\left[
\log
\sigma
\left(
r\_\phi(x,y\_w)-r\_\phi(x,y\_l)
\right)
\right].\]

The important change is that supervision now constrains a difference between behaviors rather than simply assigning one behavior positive probability. SFT provides an absolute target $y^\*$, while preference learning constrains the relative direction $y\_w-y\_l$. This is a more natural representation for many alignment problems because the pretrained model may already support both candidate behaviors. The remaining task is to move the decision boundary.

That distinction applies to properties such as factuality, verbosity, tone, refusal boundaries, confidence calibration, formatting, and tool-use style. Preference data is useful precisely because these dimensions often live inside an existing behavioral manifold rather than outside it.

## RLHF turns preference into a policy objective

Once a reward model provides a scalar estimate of preference, the natural next step is to optimize the policy against it:

\[\max\_\pi
\mathbb E\_{y\sim\pi}
[r(x,y)].\]

For a large pretrained model, unconstrained reward maximization can move the policy into poorly modeled regions of behavior space. The reward model is an approximation, so aggressive optimization may exploit inaccuracies in the reward surface or damage useful capabilities inherited from pretraining. KL-regularized RLHF addresses this by adding a reference policy:

\[\mathcal J(\pi)
=
\mathbb E\_{y\sim\pi}
[r(x,y)]
-
\beta
D\_{\mathrm{KL}}
\left(
\pi
\Vert
\pi\_{\mathrm{ref}}
\right).\]

The reward defines a direction of improvement, while the KL term controls how far the policy can move away from a known distribution. More importantly for the framework developed here, the expectation is taken over samples from the policy being optimized. This begins a shift in the source of training experience, from externally supplied demonstrations toward behavior generated by the model itself.

The optimization problem also has a useful closed-form optimum:

\[\pi^\*(y\mid x)
=
\frac{1}{Z(x)}
\pi\_{\mathrm{ref}}(y\mid x)
\exp
\left(
\frac{r(x,y)}{\beta}
\right).\]

Equivalently,

\[r(x,y)
=
\beta
\log
\frac{
\pi^\*(y\mid x)
}{
\pi\_{\mathrm{ref}}(y\mid x)
}
+
\beta\log Z(x).\]

That relationship provides the starting point for DPO.

## DPO as an analytical branch of the RLHF objective

DPO substitutes the optimal-policy relation directly into the preference model. Define

\[\Delta\_\theta
=
\log
\frac{
\pi\_\theta(y\_w\mid x)
}{
\pi\_{\mathrm{ref}}(y\_w\mid x)
}
-
\log
\frac{
\pi\_\theta(y\_l\mid x)
}{
\pi\_{\mathrm{ref}}(y\_l\mid x)
}.\]

The DPO objective becomes

\[\mathcal L\_{\mathrm{DPO}}
=
-
\mathbb E
\left[
\log\sigma
\left(
\beta\Delta\_\theta
\right)
\right].\]

Its gradient has the structure

\[\nabla\_\theta\mathcal L\_{\mathrm{DPO}}
\propto
-
\alpha
\left[
\nabla\_\theta\log\pi\_\theta(y\_w\mid x)
-
\nabla\_\theta\log\pi\_\theta(y\_l\mid x)
\right],\]

where

\[\alpha
=
\beta
\sigma(-\beta\Delta\_\theta).\]

Compared with SFT, the essential difference is visib...