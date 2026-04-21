---
title: Quantum Computers Are Not a Threat to 128-bit Symmetric Keys
url: https://words.filippo.io/128-bits/
source: Filippo Valsorda
date: 2026-04-20
fetch_date: 2026-04-21T04:43:21.860769
---

# Quantum Computers Are Not a Threat to 128-bit Symmetric Keys

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

20 Apr 2026

# Quantum Computers Are Not a Threat to 128-bit Symmetric Keys

The [advancing threat of cryptographically-relevant quantum computers](https://words.filippo.io/crqc-timeline/) has made it urgent to replace currently-deployed asymmetric cryptography primitives—key exchange (ECDH) and digital signatures (RSA, ECDSA, EdDSA)—which are vulnerable to [Shor’s quantum algorithm](https://en.wikipedia.org/wiki/Shor%27s_algorithm). It does not, however, impact existing symmetric cryptography algorithms (AES, SHA-2, SHA-3) or their key sizes.

There’s a common misconception that quantum computers will “halve” the security of symmetric keys, requiring 256-bit keys for 128 bits of security. That is not an accurate interpretation of the speedup offered by quantum algorithms, it’s not reflected in any compliance mandate, and risks diverting energy and attention from actually necessary post-quantum transition work. The misconception is usually based on a misunderstanding of the applicability of a different quantum algorithm, [Grover’s](https://en.wikipedia.org/wiki/Grover%27s_algorithm).

**AES-128 is safe against quantum computers. SHA-256 is safe against quantum computers. No symmetric key sizes have to change as part of the post-quantum transition.** This is a near-consensus opinion amongst experts and standardization bodies and it needs to propagate to the rest of the IT community. The rest of this article backs up this claim both technically and with references to relevant authorities.

## The Grover speedup

Grover’s is a quantum algorithm that allows searching an input space of size *N* of an unstructured function *f* for the “right answer” in π/4×N\pi / 4 \times \sqrt{N} invocations of *f*.

This is commonly interpreted to mean that Grover’s algorithm can find an AES-128 key in 2642^{64} “time.” That is not the case in practice, because running such an attack as a single sequential thread would take hundreds of thousands of years, and parallelizing it makes its total cost grow.

A few important things to understand about Grover’s algorithm:

* the function oracle *f* must be implemented as part of the quantum circuit;
* the oracle invocations have to happen one after the other in series;
* importantly, there is no better way to parallelize the attack than to partition the search space ([Zalka, 1997](https://arxiv.org/abs/quant-ph/9711070)).

Why does the last point matter? Because unlike regular bruteforce attacks, which are “embarrassingly parallel,” partitioning the search space degrades the Grover quadratic speedup.

Consider a classical bruteforce of a 64-bit key, where each attempt takes 5 ns (~ 16 cycles at 3 GHz). Running that on a single CPU would take nearly

264×5 ns≈3,000 years.
2^{64} \times 5 \text{ ns} \approx 3{,}000 \text{ years}.

So we parallelize it across

216=65,536 CPUs
2^{16} = 65{,}536 \text{ CPUs}

each exploring

2(64−16)=248 keys
2^{(64 - 16)} = 2^{48} \text{ keys}

in a little over

248×5 ns≈16 days.
2^{48} \times 5 \text{ ns} \approx 16 \text{ days}.

Note how the total amount of work done across the system

216×248=264
2^{16} \times 2^{48} = 2^{64}

has not changed.

This is why we consider 64-bit keys weak: because they can be searched in parallel efficiently. If the attack had to be sequential, there would be no risk.[1](#fn:dhoracle)

Let’s try the same with a Grover attack on 128-bit keys. Again, running

2128=264
\sqrt{2^{128}} = 2^{64}

operations in a row is infeasible, so we again parallelize the attack across 2162^{16} quantum computers, each exploring

2(128−16)=2112 keys.
2^{(128 - 16)} = 2^{112} \text{ keys}.

Each instance will need to do

2128/216=256 work.
\sqrt{2^{128} / 2^{16}} = 2^{56} \text{ work}.

Notice how that’s not 2482^{48}!

A 2162^{16} search space reduction factor inside a square root only saves 282^{8} of work per instance, whereas classically it saves the full 2162^{16}.

The total amount of work across the system went *up* from 2642^{64} to

256×216=272
2^{56} \times 2^{16} = 2^{72}

because we parallelized the attack, diluting the quadratic speedup in the process.

### Running the numbers

That gives us the intuition for why Grover’s algorithm doesn’t parallelize. To decide if it’s still a threat we need to run the numbers with concrete orders of magnitude.

First, we need to establish how many operations, or gates, in a row we can perform. To be conservative, let’s say that we have a fast-clock quantum architecture like superconducting qubits, and that a gate takes 1 µs.[2](#fn:speed) If we are willing to keep the attack running (with no power outage or loss of fidelity!) for a decade, that gives us a maximum sequence of gates or “depth” of

10 years/1 µs≈248
10 \text{ years} / 1 \text{ µs} \approx 2^{48}

Next, we need to know how many sequential gates it takes to compute AES-128 inside the quantum circuit. [Liao and Luo (2025)](https://eprint.iacr.org/2025/1494) provide a highly optimized Grover oracle for AES-128 with a depth of 232 T-gates (and a circuit “width” of 724, which is roughly speaking the number of logical qubits operating in parallel).

Now we can solve for the lowest parallelization factor that will keep each instance within a maximum depth of 2482^{48} (i.e. completing in a decade on these hypothetical fast and perfect quantum computers).

π/4×2128/x×232=248
\pi / 4 \times \sqrt{2^{128} / x} \times 232 = 2^{48}

x≈247
x \approx 2^{47}

**This means we’ll need 140 trillion quantum circuits of 724 logical qubits each operating in parallel for 10 years to break AES-128 with Grover’s.**

Another way to measure the cost of that attack is its *DW* cost, the depth × width product, roughly equivalent to discussing the product of cycles and cores for classical computation.

π/4×2128/247×232×724×247≈2104.5
\pi / 4 \times \sqrt{2^{128} / 2^{47}} \times 232 \times 724 \times 2^{47} \approx 2^{104.5}

Note that unlike Shor’s algorithm instantiations (and quantum error correction) which have been getting drastically better over the years, there aren’t many terms in that formula that can improve. The only two that are open to optimization are the AES-128 Grover oracle depth (232) and width (724), but they contribute only 17 bits to the total cost, and there is probably little space left for improvement. [Liao and Luo (2025)](https://eprint.iacr.org/2025/1494) shaved 7.5 bits off the very first estimate by [Grassl et al. (2015)](https://arxiv.org/abs/1512.04965) and 1.5 bits off the earliest Grover-specific estimate of [Jaques et al. (2019)](https://eprint.iacr.org/2019/1146).

## A comparison with Shor’s

Speaking of Shor’s, how does this compare with the recently discussed quantum attacks against 256-bit elliptic curves? After all, there are people who believe or believed those to be infeasible, too, but [I’ve been arguing to take them seriously](https://words.filippo.io/crqc-timeline/).

[Babbush et al. (2026)](https://arxiv.org/abs/2603.28846) claim a Shor’s execution in

70M≈226 gates
70\text{M} \approx 2^{26} \text{ gates}

which would take minutes on an architecture with “fast” gate time of 10 µs (which is 10 times slower than what we conservatively assumed above).

2104.5/226=278.5
2^{104.5} / 2^{26} = 2^{78.5}

**Breaking AES-128 with Grover is 430,000,000,000,000,000,000,000 times more expensive than breaking 256-bit elliptic curves with Shor’s.**

## NIST agrees

The U.S. National Institute of Standards and Technology (NIST) is the standardization body that ran the international competition for post-quantum cryptography and wrote the ML-KEM and ML-DSA specification documents.

NIST not only considers AES-128 to be safe, but [made it *the benchmark* for the security of post-quantum primitives](https://csrc.nist.gov/Projects/Post-Quantum-Cryptography/Post-Quantum-Cryptography-Standardization/Evaluation-Criteria/Security-%28Evaluation-Criteria%29). A...