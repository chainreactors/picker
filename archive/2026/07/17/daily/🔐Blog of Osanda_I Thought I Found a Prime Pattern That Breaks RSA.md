---
title: I Thought I Found a Prime Pattern That Breaks RSA
url: https://osandamalith.com/2026/07/17/i-thought-i-found-a-prime-pattern-that-breaks-rsa/?utm_source=rss&utm_medium=rss&utm_campaign=i-thought-i-found-a-prime-pattern-that-breaks-rsa
source: 🔐Blog of Osanda
date: 2026-07-17
fetch_date: 2026-07-18T04:45:01.293398
---

# I Thought I Found a Prime Pattern That Breaks RSA

[## 🔐Blog of Osanda

### Security Researching and Reverse Engineering](https://osandamalith.com/ "🔐Blog of Osanda")

[Skip to content](#content "Skip to content")

* [🏠 Home](https://osandamalith.com/)
* [🔒 My Advisories](https://osandamalith.com/my-exploits/)
* [💊 Cool Posts](https://osandamalith.com/cool-posts/)
  + [💉 SQLi](https://osandamalith.com/tag/mysql/)
  + [🕷 Web App Security](https://osandamalith.com/category/web-application-security/)
  + [🛠 Tools](https://osandamalith.com/category/tools/)
  + [☢ Exploits](https://osandamalith.com/category/exploits/)
  + [🔬 Reverse Engineering](https://osandamalith.com/category/reversing-2/)
  + [🧬 Malware Analysis](https://osandamalith.com/category/malware/)
* [☠ Shellcodes](https://osandamalith.com/shellcodes/)
* [☣ About](https://osandamalith.com/about/)

* [Osanda Malith Jayathissa](https://osandamalith.com/author/osandamalith/ "View all posts by Osanda Malith Jayathissa")
* [July 17, 2026](https://osandamalith.com/2026/07/17/i-thought-i-found-a-prime-pattern-that-breaks-rsa/ "12:24 pm")

# [I Thought I Found a Prime Pattern That Breaks RSA](https://osandamalith.com/2026/07/17/i-thought-i-found-a-prime-pattern-that-breaks-rsa/)

I didn’t. But working out *why* taught me more about RSA than any tutorial ever did, because it forced me to find the exact spot where the security lives and poke it.

This post builds RSA from nothing, walks up to that spot, and then documents — with real code, real timings, and a real GPU — everything that happens when you push on it. If you can follow a bit of modular arithmetic, you can follow all of it.

---

# Part I — RSA from scratch

## The impossible-sounding problem

Normal encryption has an obvious flaw. If I scramble a message with a key, you need the same key to unscramble it — so I have to get the key to you somehow. But if I could send you a key secretly, I could just send the message secretly and skip the whole thing.

Public-key cryptography solves this with something that sounds like a contradiction:

> A key that **locks** but cannot **unlock**.

I publish my locking key to the entire world. Anyone can lock a message to me. **Nobody can unlock it — not even them, not even holding the locking key.** Only my separate, secret unlocking key works.

RSA does this. The trick is finding an operation that’s easy to do and hard to undo.

## Clock arithmetic

Everything happens **modulo** some number. If you can read a clock, you already know this.

On a 12-hour clock, 5 hours after 9 o’clock is 2 o’clock — because \(9 + 5 = 14\) and \(14-12=2\).

$$9 + 5 \equiv 2 \pmod{12}$$

The notation \(a \equiv b \pmod{N}\) means “\(a\) and \(b\) leave the same remainder when divided by \(N\).”

Why does this matter? Because **modular arithmetic destroys information**. On a clock, 2 o’clock could have come from 2, or 14, or 26, or 38. The answer doesn’t tell you where you started. That one-way fog is what we build the lock from.

The key operation is **modular exponentiation**:

$$c \equiv m^e \pmod{N}$$

Computing it forward is fast even for enormous numbers — to get \(m^{65537}\) you square about 17 times, not multiply 65537 times. Going *backwards*, given \(c\), \(e\), \(N\), is the **discrete logarithm problem**, and nobody knows how to do it efficiently.

## Euler’s theorem, the engine

Here’s the 18th-century mathematics that makes RSA work.

**Euler’s totient** \(\varphi(N)\) counts the integers up to \(N\) sharing no factor with \(N\). For a prime, everything below it qualifies:

$$\varphi(p) = p – 1$$

And for \(N = p \cdot q\) with distinct primes, the totient is multiplicative:

$$\varphi(N) = (p-1)(q-1)$$

**Euler’s theorem** says that whenever \(\gcd(a, N) = 1\):

$$a^{\varphi(N)} \equiv 1 \pmod{N}$$

Raise anything to the power \(\varphi(N)\) and you land back on 1. Exponents wrap around with period \(\varphi(N)\) — a second clock, hiding inside the first.

**This is the whole secret.** Messages live on a clock of size \(N\). *Exponents* live on a clock of size \(\varphi(N)\). And:

> \(N\) is public. \(\varphi(N)\) is not.

To compute \(\varphi(N) = (p-1)(q-1)\) you must know \(p\) and \(q\). Anyone can see \(N\); only its owner knows how it factors.

**Everyone can do arithmetic on the outer clock. Only you can do arithmetic on the inner one.**

## Building it

1. Pick two large secret primes \(p\) and \(q\) (512 bits each for RSA-1024).
2. Compute \(N = p \cdot q\). **Public.**
3. Compute \(\varphi(N) = (p-1)(q-1)\). **Secret.**
4. Choose \(e\) with \(\gcd(e, \varphi(N)) = 1\). Usually 65537. **Public.**
5. Compute \(d \equiv e^{-1} \pmod{\varphi(N)}\). **Secret.**

Publish \((e, N)\). Guard everything else.

**Encrypt:** \(c \equiv m^e \pmod N\) **Decrypt:** \(m \equiv c^d \pmod N\)

**Why decryption works.** Since \(ed \equiv 1 \pmod{\varphi(N)}\), write \(ed = 1 + k\varphi(N)\):

$$c^d \equiv (m^e)^d = m^{1 + k\varphi(N)} = m \cdot \left(m^{\varphi(N)}\right)^k \equiv m \cdot 1^k = m \pmod N$$

Euler’s theorem does all the work. Encryption and decryption are inverses *because their exponents are inverses on the hidden clock*.

## Where the security actually lives

Look hard at the definition of \(d\):

$$d \equiv e^{-1} \pmod{\varphi(N)}$$

\(e\) is public. Inverting it is trivial — extended Euclid, microseconds. The *only* thing between an attacker and your private key is that they don’t know **which clock to invert on**.

That’s it. That’s all of it:

$$
\fbox{$\varphi(N)\text{ is secret, and computing it requires factoring }N$}
$$

The attack chain is short:

$$\text{factor } N ;\longrightarrow; p, q ;\longrightarrow; \varphi(N) ;\longrightarrow; d ;\longrightarrow; \text{read everything}$$

Every link but the first is instant. **The entire fortress rests on one hinge.**

### What it looks like when the hinge is missing

Years ago I posted a [toy “RSA”](https://osandamalith.com/2017/08/30/a-basic-rsa-encrypter/) using multiplication instead of exponentiation:

$$\text{Enc}(m) = m \cdot e \bmod N, \qquad \text{Dec}(c) = c \cdot d \bmod N$$

Correctness needs \(e \cdot d \equiv 1 \pmod N\). My example: \(e = 3\), \(d = 171\), \(N = 256\). Check: \(3 \times 171 = 513 = 2(256) + 1\).

Compare the two definitions:

| scheme | private key satisfies | inversion modulus | status | attacker must |
| --- | --- | --- | --- | --- |
| Toy | d = e⁻¹ mod N | N | **public** | run Euclid — trivial |
| RSA | d = e⁻¹ mod φ(N) | φ(N) | **secret** | factor N — hard |

One symbol differs. In the toy, the modulus you invert against is *printed on the public key*, so \(d = 3^{-1} \bmod 256 = 171\) falls out for anyone. **RSA is exactly the gap between \(N\) and \(\varphi(N)\), and nothing else.**

---

# Part II — The pattern

## Digital roots

Sum a number’s digits. Sum again. Repeat to one digit:

$$1763 \to 1+7+6+3 = 17 \to 1+7 = 8$$

It looks like numerology. It’s arithmetic in disguise:

$$\mathrm{dr}(n) \equiv n \pmod 9$$

with 9 standing in for 0. **Why:** \(10 \equiv 1 \pmod 9\), so every power of ten collapses:

$$\sum\_i a\_i 10^i \equiv \sum\_i a\_i \cdot 1^i = \sum\_i a\_i \pmod 9$$

## The observation

Take any prime above 3. Its digital root is only ever:

$${1, 2, 4, 5, 7, 8}$$

Never 3, 6, or 9. Forever.

**Why:** \(\mathrm{dr}(n) \in {3,6,9} \iff 3 \mid n\), and a prime above 3 isn’t divisible by 3. That’s the entire mechanism. (The prime 3 itself is the exception.)

If you’ve met the fact that every prime \(> 3\) has the form \(6k \pm 1\), this is the same statement in base 10. Hold that thought — it comes back and it hurts.

## The idea

Digital roots are **multiplicative**:

$$\mathrm{dr}(a \cdot b) \equiv \mathrm{dr}(a) \cdot \mathrm{dr}(b) \pmod 9$$

$$11 \times 13 = 143, \quad \mathrm{dr}(11)=2,\; \mathrm{dr}(13)=4, \quad 2 \times 4 = 8, \quad \mathrm{dr}(143) = 8 \quad \text{✓}$$

So for \(N = pq\), the digital root of the modulus **constrains the digital roots of its factors**.

### A worked example

Take two primes and build their product by hand:

$...