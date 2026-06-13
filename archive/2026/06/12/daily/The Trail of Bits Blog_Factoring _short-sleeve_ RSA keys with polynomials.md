---
title: Factoring "short-sleeve" RSA keys with polynomials
url: https://blog.trailofbits.com/2026/06/12/factoring-short-sleeve-rsa-keys-with-polynomials/
source: The Trail of Bits Blog
date: 2026-06-12
fetch_date: 2026-06-13T06:10:10.497783
---

# Factoring "short-sleeve" RSA keys with polynomials

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Factoring "short-sleeve" RSA keys with polynomials

[Keegan Ryan](/authors/keegan-ryan/)

June 12, 2026

[cryptography](/categories/cryptography/), [attacks](/categories/attacks/), [exploits](/categories/exploits/)

Page content

* [How we found the weak keys](#how-we-found-the-weak-keys)
* [Factoring with polynomials](#factoring-with-polynomials)
* [Reverse engineering the CompleteFTP vulnerability](#reverse-engineering-the-completeftp-vulnerability)
* [How the vulnerability spread, and how it was contained](#how-the-vulnerability-spread--and-how-it-was-contained)
* [The search for more short-sleeve keys](#the-search-for-more-short-sleeve-keys)
* [Acknowledgments](#acknowledgments)
* [Appendix](#appendix)

What happens when the bits of an RSA private key are heavily biased toward 0 instead of being randomly generated? The public key’s bits could be biased enough for us to detect these incorrectly generated keys in the wild. Together with Hanno Böck of the [badkeys](https://badkeys.info/) project, we found hundreds of unique keys that not only have this property, but can be quickly factored. We also found the bug that led to many of these keys and analyzed historical data to track the issue over time. Surprisingly, the pattern of 0 bits is often highly structured, allowing us to develop a powerful polynomial-based cryptanalytic technique that exploits the pattern.

![Figure 1: Two patterns of RSA moduli with repeated blocks of 0 bits seen in real-world examples.](/2026/06/12/factoring-short-sleeve-rsa-keys-with-polynomials/shortsleevekeys_figure1_hu_49c6698c7e83848f.webp)

Figure 1: Two patterns of RSA moduli with repeated blocks of 0 bits seen in real-world examples.

These “short-sleeve” keys, named for how the 0 bits don’t fully cover the limbs of the big integers, largely fell into two patterns. Pattern 1 remains unexplained, but we traced pattern 2 to a type mismatch in big-integer code from old versions of the CompleteFTP file transfer software. The CompleteFTP bug also generated vulnerable short-sleeve DSA keys, and we recovered 603 unique RSA private keys and 74 DSA keys from internet scans. If you used CompleteFTP to generate host keys between December 2016 and December 2023, CompleteFTP has released a [tool](https://enterprisedt.com/downloads/KeyChecker.zip) to check whether your keys need to be regenerated.

## How we found the weak keys

The badkeys project is an open-source service that checks public keys for known vulnerabilities. While developing this tool, Hanno collected a massive number of real-world keys from public sources, including Certificate Transparency logs, internet-wide TLS and SSH scans, PGP keys, and many others. By searching this dataset for unexpectedly sparse RSA moduli, we uncovered a large number of keys in the wild with the patterns in Figure 1.

Both patterns include several regularly spaced blocks of all zeros interleaved with seemingly random data. Pattern 1 appears in CT logs for certificates issued to several large organizations, including [Yahoo](https://crt.sh/?id=375717364) and [Verizon](https://crt.sh/?id=14320619439), and on some devices running NetApp software. Fortunately, these certificates have already expired, but we still shared our findings with these companies. We wanted to learn more about which product could be responsible for generating these keys, but we did not hear back. Pattern 2 appears on SSH hosts running the CompleteFTP software from EnterpriseDT. The underlying vulnerability affects RSA keys generated using versions 10.0.0–12.0.0 (Dec 2016–Mar 2019) and DSA keys generated with v10.0.0–23.0.4 (Dec 2016–Dec 2023).

These vulnerabilities affect a small minority of hosts on the internet, but the more interesting takeaway is that independent cryptographic implementations failed in similar ways. More implementations may include the same bugs, and so it’s worth tailoring cryptanalytic algorithms for this particular type of failure.

## Factoring with polynomials

Cryptographic algorithms often need integers hundreds or thousands of bits long, and they represent these “big integers” using an array of smaller machine-sized values, called *limbs*. If we interpret pattern 1 as a sequence of 128-bit limbs, or 32-bit limbs in pattern 2, the repeated blocks of zeros correspond to a single block of zeros in each limb. Only a small contiguous subset of the limb is filled with random bits, and the rest of the limb is uncovered, hence the nickname “short-sleeve keys.”

By exploiting this mathematical structure in the limbs of these moduli, we replace the hard problem of factoring integers with the easy problem of factoring polynomials. That is, we take the modulus $n$ with unknown factors $p$ and $q$, express it as a polynomial $f\_n(x)$ with small coefficients, factor $f\_n(x)$ into $f\_p(x)$ and $f\_q(x)$, and convert these factors into $p$ and $q$. The technique of converting between integers and polynomials is common, including doing [fast polynomial multiplication](https://en.wikipedia.org/wiki/Kronecker_substitution), but sadly, few resources [describe](https://groups.google.com/a/mozilla.org/g/dev-security-policy/c/o2_vKIslDBc/m/iz7yNMy_AAAJ) how to use it for fast integer factorization.

In particular, we use the digits in the base-$B$ representation of the integer to set the coefficients of the polynomial. In the normal base-10 representation, this involves replacing powers of 10 with powers of $x$, and then converting a polynomial back to an integer involves replacing powers of $x$ with powers of 10. Mathematically, the base-$B$ representation of an integer $a = \sum\_i a\_i B^i$ corresponds to the polynomial $f\_a(x) = \sum\_i a\_i x^i$, and the polynomial evaluation $a = f\_a(B)$ converts back to an integer. For short-sleeve keys, the base corresponds to the limb size, and the extra zero bits in each limb will lead to polynomials with exceptionally small coefficients.

![Figure 2: Integers with blocks of 0 bits can be represented as polynomials with small coefficients.](/2026/06/12/factoring-short-sleeve-rsa-keys-with-polynomials/shortsleevekeys_figure2_hu_9d95cd1ea06ffa6c.webp)

Figure 2: Integers with blocks of 0 bits can be represented as polynomials with small coefficients.

This method of representing integers with polynomials is useful because the product of evaluations $f\_a(B) \* f\_c(B)$ equals the evaluation of the product $(f\_a\*f\_c)(B)$. All evaluation does is replace $x$ with $B$, so it doesn’t matter if this happens before or after multiplication. The same is true of addition.[1](#fn:1)

For a short-sleeve RSA modulus $n$ with $w$-bit limbs, we can use the base-$2^w$ representation to find a polynomial $f\_n(x)$ with exceptionally small coefficients. If $f\_p(x)$ and $f\_q(x)$ also have exceptionally small coefficients, then $f\_n(x) = f\_p(x) \* f\_q(x)$. Note that for correctly generated prime factors, $f\_p(x)$ and $f\_q(x)$ will typically have $w$-bit coefficients; that’s why this attack doesn’t work in general.

[Factoring polynomials](https://en.wikipedia.org/wiki/Factorization_of_polynomials#Factoring_univariate_polynomials_over_the_integers) is easy, so we can factor $f\_n(x)$ to get $f\_p(x)$ and $f\_q(x)$, then evaluate these factors at $2^w$ to get $p$ and $q$. This is the basic version of the attack, but I’m intentionally omitting a key insight needed to factor these real-world moduli. A full explanation is at the end of this blog.

![Figure 3: Special-form polynomials can be factored to reveal the RSA private key.](/2026/06/12/factoring-short-sleeve-rsa-keys-with-polynomials/shortsleevekeys_figure3_hu_2438a334e3fbc87c.webp)

Figure 3: Special-form polynomials can be factored to reveal the RSA private key.

The correspondence between integers and polynomials makes it easy to factor these special form moduli, but interestin...