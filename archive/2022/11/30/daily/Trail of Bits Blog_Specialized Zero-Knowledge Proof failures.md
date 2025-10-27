---
title: Specialized Zero-Knowledge Proof failures
url: https://blog.trailofbits.com/2022/11/29/specialized-zero-knowledge-proof-failures/
source: Trail of Bits Blog
date: 2022-11-30
fetch_date: 2025-10-04T00:04:51.588990
---

# Specialized Zero-Knowledge Proof failures

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Specialized Zero-Knowledge Proof failures

Opal Wright

November 29, 2022

[cryptography](/categories/cryptography/), [vulnerability-disclosure](/categories/vulnerability-disclosure/), [zero-knowledge](/categories/zero-knowledge/)

Zero-knowledge (ZK) proofs are useful cryptographic tools that have seen an explosion of interest in recent years, largely due to their applications to cryptocurrency. The fundamental idea of a ZK proof is that a person with a secret piece of information (a cryptographic key, for instance) can prove something about the secret without revealing the secret itself. Cryptocurrencies are using ZK proofs for all sorts of fun things right now, including anonymity, transaction privacy, and “roll-up” systems that help increase the efficiency of blockchains by using ZK proofs to batch transactions together. ZK proofs are also being used in more general ways, such as allowing security researchers to prove that they know how to exploit a software bug without [revealing information about the bug](https://blog.trailofbits.com/2020/05/21/reinventing-vulnerability-disclosure-using-zero-knowledge-proofs/).

As with most things in cryptography, though, it’s hard to get everything right. This blog post is all about a pair of bugs in some special-purpose ZKP code that allow ne’er-do-wells to trick some popular software into accepting invalid proofs of impossible statements. That includes “proving” the validity of invalid inputs to a group signature. This, in turn, can lead to invalid signatures. In blockchain systems that use threshold signatures, like ThorChain and Binance, this could allow an attacker to prevent targeted transactions from completing, creating a denial-of-service attack– against the chain as a whole or against specific participants.

## Background on discrete log proofs

One specialized ZK proof is a discrete logarithm proof of knowledge. Suppose Bob provides Alice with an RSA modulus `N = PQ`, where `P` and `Q` are very large primes known only to Bob, and Bob wants to prove to Alice that he knows a secret exponent `x` such that `s ≡ tx (mod N).` That is, `x` is the discrete logarithm of `s` with respect to base `t`, and he wants to prove that he knows `x` without revealing anything about it.

The protocol works as follows:

* First, Bob and Alice agree on a security parameter `k`, which is a positive integer that determines how many iterations of the protocol to perform. In practice, this is usually set to `k = 128`.
* Second, Bob randomly samples `ai` from `ZΦ(N)` for `i=1,2,…,k,` computes corresponding values `αi = tai (mod N)`, and sends `α1,α2,…,αk` to Alice.
* Third, Alice responds with a sequence of random bits `c1,c2,…,ck`.
* Fourth, Bob computes `zi = ai + cix` and sends `z1,z2,…,zk` to Alice.
* Finally, Alice checks that `tzi ≡ αisci (mod N)` for all `i = 1,2,…,k`. If all the checks pass, she accepts the proof and is confident that Bob really knows `x`. Otherwise, she rejects the proof—Bob may be cheating!

## Why it works

Suppose Bob doesn’t know `x`. For each `i`, Bob has two ways to attempt to fool Alice: one if he thinks Alice will pick `ci = 0`, and one if he thinks Alice will pick `ci = 1`.

If Bob guesses that Alice will select `ci = 0`, he can select a random `ai ∈ ZN` and send Alice `αi = tai mod N`. If Alice selects `ci = 0`, Bob sends Alice `zi = ai`, and Alice sees that `tzi ≡ tai ≡ αis0 ≡ αi (mod N)` and accepts the `i`-th iteration of the proof. On the other hand, if Alice selects `ci = 1`, Bob needs to compute `zi` such that `tzi ≡ tais (mod N)`. That is, he needs to find the discrete logarithm of `tais`, which is equal to `ai + x`. However, Bob doesn’t know `x`, so he can’t compute a `zi` that will pass Alice’s check.

On the other hand, if Bob guesses that Alice will select `ci = 1`, he can select a random `ai ∈ ZN` and send Alice `αi = tais−1 (mod N)`. If Alice selects `ci = 1`, Bob sends Alice `zi = ai.` Alice sees that `tzi ≡ tai` and `tai≡ αis ≡ tαis−1s ≡ tai (mod N)`, and accepts the `i`-th iteration of the proof. But if Alice selects `ci = 0`, Bob needs to compute `zi` such that `tzi ≡ tais−1 (mod N)`, which would be `zi = ai − x`. But again, since Bob doesn’t know `x`, he can’t compute a `zi` that will pass Alice’s check.

The trick is, each of Bob’s guesses only has a 50 percent chance of being right. If any one of Bob’s `k` guesses for Alice’s `ci` values are wrong, Alice will reject the proof as invalid. If Alice is choosing her `ci` values randomly, that means Bob’s chances of fooling Alice are about 1 in 2`k`.

Typically, Alice and Bob will use parameters like `k = 128`. Bob has a better chance of hitting the Powerball jackpot four times in a row than he does of guessing all `c1,c2,…,c128` correctly.

In the case of a *non-interactive* proof, as we’ll see in the code below, we don’t rely on Alice to pick the values `ci`. Instead, Bob and Alice each compute a hash of all the values relevant to the proof: `c = Hash(N ∥ s ∥ t ∥ α1 ∥ … ∥ αk)`. The bits of `c` are used as the `ci` values. This is called the [Fiat-Shamir transform](https://blog.trailofbits.com/2021/02/19/serving-up-zero-knowledge-proofs/). It’s certainly possible to get the Fiat-Shamir transform [wrong](https://blog.trailofbits.com/2022/04/13/part-1-coordinated-disclosure-of-vulnerabilities-affecting-girault-bulletproofs-and-plonk/), with some [pretty nasty consequences](https://blog.trailofbits.com/2022/04/15/the-frozen-heart-vulnerability-in-bulletproofs/), but the bugs discussed in this article will not involve Fiat-Shamir failures.

## The code

Our proof structure and verification code come from `tss-lib`, written by the folks at Binance. We came across this code while reviewing other software, and the Binance folks were super responsive when we flagged this issue for them.

To start with, we have our `Proof` structure:

```
type (
    Proof struct {
        Alpha,
        T [Iterations]*big.Int
    }
)
```

This is a fairly straightforward structure. We have two arrays of large integers, `Alpha` and `T`. These correspond, respectively, to the `αi` and `zi` values in the mathematical description above. It’s notable that the `Proof` structure does *not* incorporate the modulus `N` or the values `s` and `t`.

```
func (p *Proof) Verify(h1, h2, N *big.Int) bool {
    if p == nil {
        return false
    }
    modN := common.ModInt(N)
    msg := append([]*big.Int{h1, h2, N}, p.Alpha[:]...)
    c := common.SHA512_256i(msg...)
    cIBI := new(big.Int)
    for i := 0; i < Iterations; i++ {
        if p.Alpha[i] == nil || p.T[i] == nil {
            return false
        }
        cI := c.Bit(i)
        cIBI = cIBI.SetInt64(int64(cI))
        h1ExpTi := modN.Exp(h1, p.T[i])
        h2ExpCi := modN.Exp(h2, cIBI)
        alphaIMulH2ExpCi := modN.Mul(p.Alpha[i], h2ExpCi)
        if h1ExpTi.Cmp(alphaIMulH2ExpCi) != 0 {
            return false
        }
    }
    return true
}
```

This code actually *implements* the verification algorithm. The arguments `h1` and `h2` correspond to `t` and `s`, respectively. First, it computes the challenge value `c`. Then, for each bit `ci` of `c`, it computes:
[![](/img/wpdump/482754077e896cbe9437038148e3dc4b.png)](/img/wpdump/482754077e896cbe9437038148e3dc4b.png)

If `h1ExpTi ≠ alphaIMulH2ExpCi` for any `0 < i ≤ k`, the proof is rejected. Otherwise, it is accepted.

## The issue

The thing to notice is that the `Verify` function doesn’t do any sort of check to validate `h1`, `h2`, or any of the elements of `p.Alpha` or `p.T`. A lack of validity checks means we can trigger all sorts of fun edge cases. In particular, when it comes to logarithms and exponential relationships, it’s important to look out for zero. Recall that, for any `x ≠ 0`, we have `0x = 0`. Additionally, for any *`x`*, we have `0 ∙ x = 0`. We are going to exploit these facts to force the equal...