---
title: Cheating on Quantum Computing Benchmarks
url: https://www.schneier.com/blog/archives/2025/07/cheating-on-quantum-computing-benchmarks.html
source: Schneier on Security
date: 2025-08-01
fetch_date: 2025-10-07T00:49:27.295089
---

# Cheating on Quantum Computing Benchmarks

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

## Cheating on Quantum Computing Benchmarks

Peter Gutmann and Stephan Neuhaus have a [new paper](https://eprint.iacr.org/2025/1237.pdf)—I think it’s new, even though it has a March 2025 date—that makes the argument that we shouldn’t trust any of the quantum factorization benchmarks, because everyone has been cooking the books:

> Similarly, quantum factorisation is performed using sleight-of-hand numbers that have been selected to make them very easy to factorise using a physics experiment and, by extension, a VIC-20, an abacus, and a dog. A standard technique is to ensure that the factors differ by only a few bits that can then be found using a simple search-based approach that has nothing to do with factorisation…. Note that such a value would never be encountered in the real world since the RSA key generation process typically requires that |p-q| > 100 or more bits [9]. As one analysis puts it, “Instead of waiting for the hardware to improve by yet further orders of magnitude, researchers began inventing better and better tricks for factoring numbers by exploiting their hidden structure” [10].
>
> A second technique used in quantum factorisation is to use preprocessing on a computer to transform the value being factorised into an entirely different form or even a different problem to solve which is then amenable to being solved via a physics experiment…

Lots more in the paper, which is titled “Replication of Quantum Factorisation Records with an 8-bit Home Computer, an Abacus, and a Dog.” He points out the largest number that has been factored legitimately by a quantum computer is 35.

I hadn’t known these details, but I’m not surprised. I [have](https://www.schneier.com/essays/archives/2018/09/cryptography_after_t.html) [long](https://www.schneier.com/blog/archives/2019/10/factoring_2048.html) [said](https://www.schneier.com/blog/archives/2024/01/quantum-computing-skeptics.html) that the engineering problems between now and a useful, working quantum computer are hard. And by “hard,” we don’t know if it’s “land a person on the surface of the moon” hard, or “land a person on the surface of the sun” hard. They’re both hard, but very different. And we’re going to hit those engineering problems one by one, as we continue to develop the technology. While I don’t think quantum computing is “surface of the sun” hard, I don’t expect them to be factoring RSA moduli anytime soon. And—even there—I expect lots of engineering challenges in making Shor’s Algorithm work on an actual quantum computer with large numbers.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [cheating](https://www.schneier.com/tag/cheating/), [quantum computing](https://www.schneier.com/tag/quantum-computing/)

[Posted on July 31, 2025 at 7:00 AM](https://www.schneier.com/blog/archives/2025/07/cheating-on-quantum-computing-benchmarks.html) •
[22 Comments](https://www.schneier.com/blog/archives/2025/07/cheating-on-quantum-computing-benchmarks.html#comments)

### Comments

wiredog •
[July 31, 2025 7:38 AM](https://www.schneier.com/blog/archives/2025/07/cheating-on-quantum-computing-benchmarks.html/#comment-446813)

I feel sorry for the dog.

My first computer was a Vic-20.

Clive Robinson •
[July 31, 2025 9:05 AM](https://www.schneier.com/blog/archives/2025/07/cheating-on-quantum-computing-benchmarks.html/#comment-446814)

@ Bruce, ALL,

With regards,

> “They’re both hard, but very different. And we’re going to hit those engineering problems one by one, as we continue to develop the technology.”

We also know that some problems are not solvable in the frame of human understanding / existance. Two such are,

1, Getting human sized matter to or beyond the speed of light.

Part of the first we can get close to and that could give “false expectations”. The second well the result of that if it could be done would be rather more than existential for the universe by our understanding of the laws of nature and the universe.

Thus when we look at “quantum computing” we have to ask two things,

1, Do we yet know enough to understand the barriers?
2, Are the barriers actually possible to solve?

The answer to the first is clearly “NO”. Which makes the answer to the second an “Open Question” at best currently. However with a gradient that increases daily, there is an attached increasing probability of the answer being either “NO” or such that it “Might as well be NO”.

One thing we see is that as the number of QBits goes up so does the noise that makes the results exponentially difficult to obtain. To get past this we think needs at a minimum exponentially more Qbits.

Thus two further questions arise,

1, Just how many QBits can their be in a bounded universe?
2, What tiny tiny fraction of those can actually be used in a meaningful way?

But before we get there, there is another question that is more practical in nature.

Whilst helium is plentiful in the universe it is actually incredibly scarce on earth. Also each time we “dump helium” it gets into the upper atmosphere, where it gets knocked into space as solar radiation strips it off.

Thus,

“Can we afford the helium to make general quantum computing viable?”

wiredog •
[July 31, 2025 10:34 AM](https://www.schneier.com/blog/archives/2025/07/cheating-on-quantum-computing-benchmarks.html/#comment-446815)

@clive
Well, if we solve the controlled hydrogen fusion problem we can manufacture helium.

Might be easier to capture the helium emitted by decaying reactor fuel though.

Scribble •
[July 31, 2025 11:25 AM](https://www.schneier.com/blog/archives/2025/07/cheating-on-quantum-computing-benchmarks.html/#comment-446817)

I wonder if the appropriate animal-experiment paperwork was done.

Anonymous Coward III •
[July 31, 2025 11:39 AM](https://www.schneier.com/blog/archives/2025/07/cheating-on-quantum-computing-benchmarks.html/#comment-446818)

Wow, thanks for this funny paper. It’s quite good timing as I’m preparing to re-enter uni and consider all kinds of software testing projects anew.

Whilst I’ve just downloaded the paper and not read it yet beyond the funny intro, I don’t think you can immediately be so dismissive about the power of an abacus (I’m less sure about why you’d use a dog for arithmetic). I mean, some of the techniques I use everyday take the mathematician’s trick of using an abacus and go one stage further they allow you to use them even if you don’t actually have a live abacus before you.

Of course, we should exercise caution regarding the so-called post-quantum encryption systems, since, the current orthodoxy that says factorisation is hard on a classical computer (ie: one not deliberately exploiting quantum effects for the computation, let’s say) — that current orthodoxy isn’t necessarily true, it’s just accepted wisdom until a new 12 year old comes along and proves that a classical computer could do that all along.

Nevertheless, thanks for th...