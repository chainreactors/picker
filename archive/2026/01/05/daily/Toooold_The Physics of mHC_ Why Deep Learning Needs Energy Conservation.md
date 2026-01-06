---
title: The Physics of mHC: Why Deep Learning Needs Energy Conservation
url: https://toooold.com/2026/01/05/mhc-physics.html
source: Toooold
date: 2026-01-05
fetch_date: 2026-01-06T03:26:44.692549
---

# The Physics of mHC: Why Deep Learning Needs Energy Conservation

[Toooold](/)
[ ]

[Make a CatGPT out of ChatGPT](/2023-02-02-cat_laser_chatgpt.html)[About](/about.html)

# The Physics of mHC: Why Deep Learning Needs Energy Conservation

Jan 5, 2026

When I first read the **Manifold-Constrained Hyper-Connections (mHC)** paper <https://www.arxiv.org/abs/2512.24880> , I didn’t see it as just another optimization trick or a clever use of Sinkhorn iterations, but the other way round. **This is physics.**

I suspect the root motivation for this paper wasn’t initially “Let’s use the Birkhoff Polytope.” I believe the authors started with a fundamental physical intuition: **Conservation of Energy**. They likely asked, *“How do we build a deep network that routes information without creating or destroying it?”* Very “first principle” thought, right? The math like doubly stochastic matrices, the Birkhoff manifold is just the implementation detail used to enforce this physical law.

Here is the derivation of mHC not from a mathematical perspective, but from a “First Principles” physics perspective.

![alt text](/images/mhc.jpg)

## The Problem: Neural Networks are “Active Amplifiers”

Standard neural networks violate the laws of physics. In a standard linear layer:

\[y = Wx\]

If the weights $W$ are initialized randomly, the layer acts as an **active amplifier**. It injects energy into the system.

If the eigenvalues of $W$ are slightly larger than 1, the signal energy explodes exponentially as it passes through layers ($1.1^{100} \approx 13,780$). If they are smaller than 1, the signal dies. This is why we need LayerNorm, BatchNorm, and complex initializations—we are trying to artificially tame a system that fundamentally wants to explode.

**The mHC Intuition:** A stable deep network should act like a **Passive System**. It should be a complex system of pipes and valves that *routes* the flow (signal) but never creates it out of thin air.

## Deriving the Math from the Physics

Let’s try to design a layer strictly obeying conservation laws. We will see that the **Doubly Stochastic** constraint naturally falls out of these requirements.

### 1. Conservation of “Signal Mass” (First Moment)

Imagine the input signal $x$ is a physical fluid with a total mass. We want the total mass leaving the layer to equal the mass entering it. No leaks, no pumps.

\[\sum\_{i} y\_i = \sum\_{j} x\_j\]

Substituting $y\_i = \sum\_j W\_{ij} x\_j$:

\[\sum\_{i} \sum\_{j} W\_{ij} x\_j = \sum\_{j} x\_j\]

If we swap the summation order to isolate the input terms:

\[\sum\_{j} x\_j \left( \sum\_{i} W\_{ij} \right) = \sum\_{j} x\_j\]

For this to hold for *any* input signal $x$, the term in the parentheses must be exactly 1.

\[\sum\_{i} W\_{ij} = 1 \quad (\forall j)\]

**Result:** This forces the **Column Sums to be 1**. Physically, this ensures that every drop of “mass” from input $j$ is accounted for in the output.

### 2. Bounding “Signal Energy” (Second Moment)

Mass conservation isn’t enough; we need to prevent the variance (energy) from exploding. We want the system to be **Dissipative**—the output energy should never exceed the input energy.

\[\|y\|^2 \le \|x\|^2\]

To guarantee this without complex eigenvalue analysis, we can demand that the output is a **Convex Combination** (a weighted average) of the inputs.

\[y\_i = \sum\_j W\_{ij} x\_j \quad \text{where } W\_{ij} \ge 0\]

By **Jensen’s Inequality**, since $\sum\_j W\_{ij} = 1$ (which we will enforce momentarily) and weights are non-negative:

\[(y\_i)^2 = \left(\sum\_j W\_{ij} x\_j\right)^2 \le \sum\_j W\_{ij} (x\_j^2)\]

Summing over all outputs to get total energy:

\[\|y\|^2 = \sum\_i y\_i^2 \le \sum\_i \sum\_j W\_{ij} x\_j^2\]

Swapping sums again:

\[\|y\|^2 \le \sum\_j x\_j^2 \underbrace{\left( \sum\_i W\_{ij} \right)}\_{=1} = \|x\|^2\]

**Result:** By forcing $W$ to be non-negative and sum-to-one, we mathematically guarantee that **Energy Out $\le$ Energy In**. The gradient cannot explode because the system cannot amplify.

### 3. Time Symmetry (The Backward Pass)

Here is the final piece of the puzzle. A neural network is a bidirectional system.

* **Forward Pass:** Data flows through $W$.
* **Backward Pass:** Gradients (Error Energy) flow through $W^T$.

If we only conserve energy in the forward direction (Column Sums = 1), we might still explode during backpropagation. The “Ghost Cat” of the gradient needs a stable path too.

The total “error mass” being propagated back is:

\[\sum\_{j=1}^d (g\_{out})\_j = \sum\_{i=1}^d (g\_{in})\_i \underbrace{\left( \sum\_{j=1}^d W\_{ij} \right)}\_{\text{Row Sum}}\]

To ensure **Gradient Energy Conservation**, we must apply the same logic to $W^T$, forcing the **Row Sums to be 1**:

\[\sum\_{j} W\_{ij} = 1 \quad (\forall i)\]

![alt text](/images/mhc2.jpg)

## The Mathematical Engine: Doubly Stochastic Matrices & Sinkhorn-Knopp

When we combine these three physical requirements:

1. **Mass Conservation** $\rightarrow$ Column Sums $= 1$
2. **Dissipative Energy** $\rightarrow$ Non-negative weights ($W \ge 0$)
3. **Time Symmetry** $\rightarrow$ Row Sums $= 1$

We arrive at exactly the definition of a **Doubly Stochastic Matrix**.

The set of all such matrices is the **Birkhoff Polytope** ($\mathcal{B}\_n$). The mHC paper didn’t arbitrarily choose this manifold; it is the *only* geometric space that satisfies these conservation laws.

### The Enforcer: The Sinkhorn-Knopp Algorithm

We initialize our network with random weights $A$ that likely violate all these laws (negative values, random sums). How do we project this chaotic matrix $A$ onto the stable Birkhoff Polytope?

We use the **Sinkhorn-Knopp Algorithm**, an iterative “pressure equalization” process.

**Step 1: Enforce Positivity (The Energy Floor)**
We ensure strictly positive energy transfer by taking the exponential:
\(S^{(0)}\_{ij} = \exp(A\_{ij})\)

**Step 2: Iterative Normalization**
We alternate between normalizing rows and columns.

* **Row Normalization (Conservation in Time):**
  \(S^{(k)}\_{ij} \leftarrow \frac{S^{(k-1)}\_{ij}}{\sum\_{l} S^{(k-1)}\_{il}}\)
* **Column Normalization (Conservation of Mass):**
  \(S^{(k+1)}\_{ij} \leftarrow \frac{S^{(k)}\_{ij}}{\sum\_{l} S^{(k)}\_{lj}}\)

**Step 3: Convergence**
Sinkhorn’s Theorem guarantees that this process converges to a unique matrix $P \in \mathcal{B}\_n$:

\[\lim\_{k \to \infty} S^{(k)} = P \quad \text{s.t.} \quad P \mathbf{1} = \mathbf{1}, \quad P^T \mathbf{1} = \mathbf{1}\]

In practice, mHC typically uses just 3-5 iterations. This forces the neural network to stop playing dice with energy and start respecting the laws of thermodynamics.

See, mHC isn’t just a constraint; it’s a statement that **Stability is Symmetry.**

## Toooold

* Toooold
* toooold.tocode@gmail.com

* [phunterlau](https://github.com/phunterlau)

to code