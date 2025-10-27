---
title: Blowing Out the Candles on the Birthday Bound
url: https://soatok.blog/2024/07/01/blowing-out-the-candles-on-the-birthday-bound/
source: Dhole Moments
date: 2024-07-02
fetch_date: 2025-10-06T17:45:10.608157
---

# Blowing Out the Candles on the Birthday Bound

[Skip to the content](#site-content)

Search

[Dhole Moments](https://soatok.blog/)

Software, Security, Cryptography, and Furries

Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Search

Search for:

Close search

Close Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Categories

[Cryptography](https://soatok.blog/category/cryptography/)

# Blowing Out the Candles on the Birthday Bound

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [July 1, 2024](https://soatok.blog/2024/07/01/blowing-out-the-candles-on-the-birthday-bound/)

![Blowing Out the Candles on the Birthday Bound](https://i0.wp.com/soatok.blog/wp-content/uploads/2024/07/BlogHeader-2024-BirthdayBound.png?fit=1200%2C675&ssl=1)

Four years ago, I wrote a (surprisingly popular) blog post about the notion of [wear-out for symmetric encryption schemes](https://soatok.blog/2020/12/24/cryptographic-wear-out-for-symmetric-encryption/).

Two years ago, I wrote a thing about [extending the nonce used by AES-GCM without introducing foot-guns](https://soatok.blog/2022/12/21/extending-the-aes-gcm-nonce-without-nightmare-fuel/). This was very recently referenced [in one of Filippo Valsorda’s Cryptography Dispatches](https://words.filippo.io/dispatches/xaes-256-gcm/), which referenced alternative designs in the same vein.

As I was reading Filippo’s newsletter, it occurred to me that a dedicated treatment to how cryptographers discuss the Birthday Bound for symmetric encryption would be beneficial.

## Birthday Bound?

The Birthday Bound is rooted in the so-called Birthday Paradox in probability theory. It goes something like this:

> How many people (chosen from a uniform random distribution) would you need to have in the same room in order for there to be a 50% or greater chance that two of them have the same birthday?

Even though there are 366 possible calendar days in the year (365 if you ignore leap years), the answer is only **23**.

This observation can tell us something interesting about the collision risk in discrete uniformly random samples.

For example, the random number (called an IV in this case) used to encrypt a message with AES-CBC, which is a 128-bit random number. This means that there are ![2^{128}](https://s0.wp.com/latex.php?latex=2%5E%7B128%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) possible values. We can simply describe this situation for any ![2^{n}](https://s0.wp.com/latex.php?latex=2%5E%7Bn%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) distribution; in this case, ![n = 128](https://s0.wp.com/latex.php?latex=n+%3D+128&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002).

For any random distribution (i.e., random nonces or tweaks for an AEAD scheme) of ![2^{n}](https://s0.wp.com/latex.php?latex=2%5E%7Bn%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) possible values, you expect to have a 50% chance of collision after about ![2^{n/2}](https://s0.wp.com/latex.php?latex=2%5E%7Bn%2F2%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) queries. This is a loose, order-of-magnitude estimate.

From our earlier AES-CBC example, this means ![2^{64}](https://s0.wp.com/latex.php?latex=2%5E%7B64%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) blocks of data, we’d expect a 50% chance of the two to collide.

[My symmetric wear-out blog post](https://soatok.blog/2020/12/24/cryptographic-wear-out-for-symmetric-encryption/) went in-depth about the particulars for specific designs, if you’d like to know how the numbers play out.

### Is 50/50 Good Enough?

A security policy that cuts off at a 50% chance of a nonce reuse is not fit for the real world. We would call that a YOLO security policy.

AES-GCM, which accepts a 96-bit nonce, is considered unsafe to use for more than ![2^{32}](https://s0.wp.com/latex.php?latex=2%5E%7B32%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) random nonces. At this point, the probability of a collision for each subsequent message is greater than or equal to ![2^{-32}](https://s0.wp.com/latex.php?latex=2%5E%7B-32%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002).

Consequently, many people consider the point that the risk exceeds ![2^{-32}](https://s0.wp.com/latex.php?latex=2%5E%7B-32%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) the Birthday Bound for a block cipher mode; after which, a new encryption key must be used.

I certainly don’t fault any security policy that keeps the risk of a bad outcome below the ![2^{-32}](https://s0.wp.com/latex.php?latex=2%5E%7B-32%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) mark, but I think there’s another way to interpret what NIST did with AES-GCM. Namely, the fact that GCM’s risk of ![2^{-r}](https://s0.wp.com/latex.php?latex=2%5E%7B-r%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) is exceeded after ![2^{r}](https://s0.wp.com/latex.php?latex=2%5E%7Br%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) samples (for some fixed value ![r](https://s0.wp.com/latex.php?latex=r&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002)) offers a nice symmetry to the risk analysis.

### Three Birthday Bounds

> (I was originally trying to find a wordplay that references the children’s story *[Six-Dinner Sid](https://en.wikipedia.org/wiki/Six-Dinner_Sid)* for this section, but ran out of steam and pressed publish before finding an appropriate parody.)
>
> Soatok Editorial Note

This gives rise to three different possible values for a given random distribution that can be considered whenever someone says the phrase “birthday bound”.

1. 50% collision risk after ![2^{n/2}](https://s0.wp.com/latex.php?latex=2%5E%7Bn%2F2%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) samples, which I like to think of as the
   **Hard Birthday Bound**.
2. ![2^{-32}](https://s0.wp.com/latex.php?latex=2%5E%7B-32%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) collision risk after ![2^{(n-32)/2}](https://s0.wp.com/latex.php?latex=2%5E%7B%28n-32%29%2F2%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) samples, which I like to call the
   **Soft Birthday Bound**.
3. ![2^{-r}](https://s0.wp.com/latex.php?latex=2%5E%7B-r%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) collision risk after ![2^{r}](https://s0.wp.com/latex.php?latex=2%5E%7Br%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) samples, which I like to call the
   **Optimal Birthday Bound**.

(These labels are not official; a better naming convention may be worth considering, should this framework for discussion prove useful at all.)

Since we’re still dealing with approximations, a useful technique for calculating ![r](https://s0.wp.com/latex.php?latex=r&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) is to just take the cube-root of ![2^{n}](https://s0.wp.com/latex.php?latex=2%5E%7Bn%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) (a.k.a., divide the exponent by 3).

In the case of AES-GCM, the Soft and Optimal values are equivalent.

In the case of Filippo’s XAES-256-GCM design? They differ quite a bit.

* Soft: ![2^{80}](https://s0.wp.com/latex.php?latex=2%5E%7B80%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) messages for ![2^{-32}](https://s0.wp.com/latex.php?latex=2%5E%7B-32%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) collision probability.
* Optimal: ![2^{64}](https://s0.wp.com/latex.php?latex=2%5E%7B64%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) messages for ![2^{-64}](https://s0.wp.com/latex.php?latex=2%5E%7B-64%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) collision probability.

Whereas the Soft and Optimal limits for a 96-bit nonce are the same, with a 192-bit nonce, they differ a lot: Soft is about 65,536 times the size as Optimal.

## Does Any Of This Matter?

If your accepted risk is hard-coded at ![2^{-32}](https://s0.wp.com/latex.php?latex=2%5E%7B-32%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002), then you don’t need to pass Go or collect $200, because your security policy saves you the headache of having to care about math nerd stuff.

However, I do think that the Optimal Birthday Bound is *more useful* for risk analysis for one simple reason: This is the point at which the probabili...