---
title: Breaking RSA with a Quantum Computer
url: https://www.schneier.com/blog/archives/2023/01/breaking-rsa-with-a-quantum-computer.html
source: Schneier on Security
date: 2023-01-04
fetch_date: 2025-10-04T03:01:23.983743
---

# Breaking RSA with a Quantum Computer

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Breaking RSA with a Quantum Computer

A group of Chinese researchers have [just published](https://arxiv.org/pdf/2212.12372.pdf) a paper claiming that they can—although they have not yet done so—break 2048-bit RSA. This is something to take seriously. It might not be correct, but it’s not obviously wrong.

We have long known from Shor’s algorithm that factoring with a quantum computer is easy. But it takes a big quantum computer, on the orders of millions of qbits, to factor anything resembling the key sizes we use today. What the researchers have done is combine classical lattice reduction factoring techniques with a quantum approximate optimization algorithm. This means that they only need a quantum computer with 372 qbits, which is well within what’s possible today. (The [IBM Osprey](https://newsroom.ibm.com/2022-11-09-IBM-Unveils-400-Qubit-Plus-Quantum-Processor-and-Next-Generation-IBM-Quantum-System-Two) is a 433-qbit quantum computer, for example. Others are on their way as well.)

The Chinese group didn’t have that large a quantum computer to work with. They were able to factor 48-bit numbers using a 10-qbit quantum computer. And while there are always potential problems when scaling something like this up by a factor of 50, there are no obvious barriers.

Honestly, most of the paper is over my head—both the lattice-reduction math and the quantum physics. And there’s the nagging question of why the Chinese government didn’t classify this research. But…wow…maybe…and yikes! Or not.

> “[Factoring integers with sublinear resources on a superconducting quantum processor](https://arxiv.org/pdf/2212.12372.pdf)”
>
> **Abstract:** Shor’s algorithm has seriously challenged information security based on public key cryptosystems. However, to break the widely used RSA-2048 scheme, one needs millions of physical qubits, which is far beyond current technical capabilities. Here, we report a universal quantum algorithm for integer factorization by combining the classical lattice reduction with a quantum approximate optimization algorithm (QAOA). The number of qubits required is O(logN/loglogN ), which is sublinear in the bit length of the integer N , making it the most qubit-saving factorization algorithm to date. We demonstrate the algorithm experimentally by factoring integers up to 48 bits with 10 superconducting qubits, the largest integer factored on a quantum device. We estimate that a quantum circuit with 372 physical qubits and a depth of thousands is necessary to challenge RSA-2048 using our algorithm. Our study shows great promise in expediting the application of current noisy quantum computers, and paves the way to factor large integers of realistic cryptographic significance.

In email, [Roger Grimes](https://www.amazon.com/Cryptography-Apocalypse-Preparing-Quantum-Computing/dp/1119618193) told me: “Apparently what happened is another guy who had previously announced he was able to break traditional asymmetric encryption using classical computers…but reviewers found a flaw in his algorithm and that guy had to retract his paper. But this Chinese team realized that the step that killed the whole thing could be solved by small quantum computers. So they tested and it worked.”

EDITED TO ADD: One of the issues with the algorithm is that it relies on a [recent factoring paper](https://eprint.iacr.org/2021/933) by Claus Schnorr. It’s a controversial paper; and despite the “this destroys the RSA cryptosystem” claim in the abstract, it does nothing of the sort. Schnorr’s algorithm works well with smaller moduli—around the same order as ones the Chinese group has tested—but falls apart at larger sizes. At this point, nobody understands why. The Chinese paper claims that their quantum techniques get around this limitation (I think that’s what’s behind Grimes’s comment) but don’t give any details—and they haven’t tested it with larger moduli. So if it’s true that the Chinese paper depends on this Schnorr technique that doesn’t scale, the techniques in this Chinese paper won’t scale, either. (On the other hand, if it does scale then I think it also breaks a bunch of lattice-based public-key cryptosystems.)

I am *much* less worried that this technique will work now. But this is something the IBM quantum computing people can test right now.

EDITED TO ADD (1/4): A reporter just asked me my gut feel about this. I replied that I don’t think this will break RSA. Several times a year the cryptography community received “breakthroughs” from people outside the community. That’s why we created the RSA Factoring Challenge: to force people to provide proofs of their claims. In general, the smart bet is on the new techniques not working. But someday, that bet will be wrong. Is it today? Probably not. But it could be. We’re in the worst possible position right now: we don’t have the facts to know. Someone needs to implement the quantum algorithm and see.

EDITED TO ADD (1/5): Scott Aaronson’s [take](https://scottaaronson.blog/?p=6957) is a “no”:

> In the new paper, the authors spend page after page saying-without-saying that it *might* soon become possible to break RSA-2048, using a NISQ (i.e., non-fault-tolerant) quantum computer. They do so via two time-tested strategems:
>
> 1. the detailed exploration of irrelevancies (mostly, optimization of the number of qubits, while ignoring the number of gates), and
> 2. complete silence about the one crucial point.
>
> Then, finally, they come clean about the one crucial point in a single sentence of the Conclusion section:
>
> > It should be pointed out that the quantum speedup of the algorithm is unclear due to the ambiguous convergence of QAOA.
>
> “Unclear” is an understatement here. It seems to me that a miracle would be required for the approach here to yield any benefit at all, compared to just running the classical Schnorr’s algorithm on your laptop. And if the latter were able to break RSA, it would’ve already done so.
>
> All told, this is one of the most actively misleading quantum computing papers I’ve seen in 25 years, and I’ve seen … many.

EDITED TO ADD (1/7): More [commentary](https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A7016808281847336960/). Again: no need to panic.

EDITED TO ADD (1/12): Peter Shor has [suspicions](https://twitter.com/PeterShor1/status/1607864880324804608).

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [China](https://www.schneier.com/tag/china/), [cryptanalysis](https://www.schneier.com/tag/cryptanalysis/), [cryptography](https://www.schneier.com/tag/cryptography/), [quantum computing](https://www.schneier.com/tag/quantum-computing/), [RSA](https://www.schneier.com/tag/rsa/)

[Posted on January 3, 2023 at 12:38 PM](https://www.schneier.com/blog/archives/2023/01/breaking-rsa-with-a-quantum-computer.html) •
[76 Comments](https://www.schneier.com/blog/archives/2023/01/breaking-rsa-with-a-qua...