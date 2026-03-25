---
title: Spotting issues in DeFi with dimensional analysis
url: https://blog.trailofbits.com/2026/03/24/spotting-issues-in-defi-with-dimensional-analysis/
source: The Trail of Bits Blog
date: 2026-03-24
fetch_date: 2026-03-25T04:16:10.155622
---

# Spotting issues in DeFi with dimensional analysis

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Spotting issues in DeFi with dimensional analysis

[Coriolan Pinhas](/authors/coriolan-pinhas/)

March 24, 2026

[blockchain](/categories/blockchain/), [guides](/categories/guides/)

Page content

* [Quantities and dimensions](#quantities-and-dimensions)
* [Dimensional thinking in DeFi](#dimensional-thinking-in-defi)
* [Why some price formulas don’t work](#why-some-price-formulas-dont-work)
  + [Example 1](#example-1)
  + [Example 2](#example-2)
  + [Example 3](#example-3)
* [Real-life best practices](#real-life-best-practices)
* [Toward dimensional safety in Solidity](#toward-dimensional-safety-in-solidity)

Using dimensional analysis, you can categorically rule out a whole category of logic and arithmetic bugs that plague DeFi formulas. No code changes required, just better reasoning!

One of the first lessons in physics is learning to think in terms of [dimensions](https://en.wikipedia.org/wiki/Dimensional_analysis). Physicists can often spot a flawed formula in seconds just by checking whether the dimensions make sense. I once had a teacher who even kept a stamp that said “non-homogeneous formula” for that purpose (and it was used *a lot* on students’ work). Developers can use the same approach to spot incorrect arithmetic in smart contracts.

In this post, we’ll start with the basics of dimensional analysis in physics and then apply the same reasoning to real DeFi formulas. We’ll also show you how this can be implemented in practice, using Reserve Protocol as an example. Along the way, we’ll see why developers need to think explicitly about dimensional safety when writing smart contracts, and why the DeFi ecosystem would benefit from tooling that can automatically catch these classes of bugs. Speaking of which, while putting together this post, we actually built a Claude plugin for this purpose, but we’ll get into the details in a follow-up post.

## Quantities and dimensions

We will start with two formulas:

$$\textit{Speed} = \textit{distance} + \textit{time}$$$$\textit{Speed} = \frac{\textit{distance}}{\textit{time}}$$

Which of the two formulas is the correct way to calculate the speed of an object? Clearly, it’s the second one, but not just because you’ve memorized the correct formula. The deeper reason lies in *dimensions*.

Physics recognizes **seven fundamental quantities**: length (meters), mass (grams), time (seconds), electric current (amps), thermodynamic temperature (kelvin), amount of substance (moles), and luminous intensity (candela).

Every other physical concept, like speed, force, or energy, is a *derived quantity*, defined in terms of the fundamental ones.

For example, this is how speed is defined:

$$\textit{Speed} = \textit{distance} / \textit{time}$$

And this is how it’s represented in dimensional terms:

$$\textit{Speed}\text{(meters/second)} = \frac{\textit{length}\text{ (meters)}}{\textit{time}\text{ (seconds)}}$$

The golden rule is simple: **both sides of an equation must have the same dimension.**

And, just as important, **you can’t add or subtract quantities with different dimensions.**

So if we reason through the incorrect speed formula in terms of dimensions, we’ll get this:

$$\textit{Speed}\text{ (meters/second)} = \frac{\textit{length}\text{ (meters)}}{\textit{time}\text{ (seconds)}} = \textit{length}\text{ (meters)} + \textit{time}\text{ (seconds)}$$

This is clearly nonsense. If dimensions could scream, they would. So we can easily say that this formula can’t be used to calculate anything, speed or otherwise.

Note that even when dimensions check out, you must still use consistent units!

## Dimensional thinking in DeFi

Now let’s shift the lens. Physics deals with meters, seconds, and kilograms, but DeFi has its own “dimensions”: tokens, prices, liquidity, and so on.

Here’s where mistakes start to creep in. Imagine you’re coding [an AMM](https://docs.uniswap.org/contracts/v2/concepts/protocol-overview/how-uniswap-works) and you write this:

$$K = x + y$$

Does that look right? It shouldn’t.

Here, x might represent the number of “token A” and y the number of “token B.” Adding them together is just as meaningless as adding distance and time. They’re different dimensions.

At this point, you might object: *“Wait, this is exactly how Curve Stable Pools work!”*

And you’d be right. But the key is in the name: **stable**. In a stable pool, tokens are designed to maintain near-equal value. Under that assumption, token A and token B are treated as if they were the same “dimension.” This trick makes the formula workable in this special case. But outside of stable pools, blindly adding tokens together is as absurd as writing \(\textit{speed} = \textit{distance} + \textit{time}\). Understanding homogeneous formulas helps you not only find issues but also understand why a formula is structured the way it is.

In physics, **speed** is a derived quantity built from the fundamental quantities of **length** and **time**. DeFi has its own derived quantities: **liquidity**, for example, is built from **token balances**.

For example, in a Uniswap v3 pool with reserves x and y, liquidity is calculated as follows:

$$\textit{Liquidity} = \sqrt{x \cdot y}$$

Dimensionally, this calculation looks like this:

$$\textit{Liquidity} = \sqrt{[A] \cdot [B]}$$

Here, [A] is a dimension that represents the number of token A, and [B] is a dimension that represents the number of token B.

On its own, “token A × token B” doesn’t have a direct interpretation, just like “meters × seconds” doesn’t. But within the invariant equation \(k = x \cdot y\), the \(x \cdot y\) part defines a **conserved relationship** that governs swaps.

k and the liquidity are not base dimensions; they are derived ones, combining the balances of multiple tokens into a single pool-wide property.

## Why some price formulas don’t work

### Example 1

Suppose someone writes this incorrect formula in his protocol:

$$\textit{Price} = \frac{\text{number of token A}}{\textit{liquidity}}$$

We can easily spot the issue with dimensional analysis.

This is an example of a correct and straightforward way to define a price:

$$\text{Price of B in terms of A} = \frac{\text{amount of A}}{\text{amount of B}} = \frac{[A]}{[B]}$$

If the formula \(\textit{Price} = \frac{\text{number of token A}}{\textit{liquidity}}\) were correct, the right side of the equation would have the same dimensions as the correct price definition above.

But dimensionally, the right side of the formula is as follows:

$$\frac{[A]}{\sqrt{[A] \cdot [B]}} = \frac{\sqrt{[A]} \cdot \sqrt{[A]}}{\sqrt{[A] \cdot [B]}} = \sqrt{\frac{[A]}{[B]}}$$

That’s not a price; it’s the *square root* of a price. The formula produces something, but it’s not a price.

Consequently, we have different dimensions on the right and left sides of the formula. This means the formula \(\textit{Price} = \frac{\text{number of token A}}{\textit{liquidity}}\) is incorrect. This is discernible without further knowledge of the DEX.

### Example 2

Let’s take another example that is harder to spot without dimensional analysis. Which of these formulas is incorrect?

1. $$K = (\text{number of token A})^2 \cdot \text{Price of B in terms of A}$$
2. $$K = \frac{(\text{number of token A})^2}{\text{Price of B in terms of A}}$$

Here is a tip: K is often defined as \(\text{number of token A} \cdot \text{number of token B}\) .

Dimensionally, this means \(K = [A] \cdot [B]\).

Now that we have the dimensions of the left side of the equation, let’s check if one of the two formulas has the same dimensions on the right side.

1. $$K = [A]^2 \cdot \frac{[A]}{[B]} = \frac{[A]^3}{[B]}$$
2. $$K = \frac{[A]^2}{\frac{[A]}{[B]}} = [A] \cdot [B]$$

So we can see that the first formula can’t be valid, and the second one is dimensionally valid!

### Example 3

For an example in a DeFi context, let’s consider a real v...