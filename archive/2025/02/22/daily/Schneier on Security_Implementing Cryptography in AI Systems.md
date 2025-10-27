---
title: Implementing Cryptography in AI Systems
url: https://www.schneier.com/blog/archives/2025/02/implementing-cryptography-in-ai-systems.html
source: Schneier on Security
date: 2025-02-22
fetch_date: 2025-10-06T20:47:01.526035
---

# Implementing Cryptography in AI Systems

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

## Implementing Cryptography in AI Systems

Interesting research: “[How to Securely Implement Cryptography in Deep Neural Networks](https://eprint.iacr.org/2025/288).”

> **Abstract:** The wide adoption of deep neural networks (DNNs) raises the question of how can we equip them with a desired cryptographic functionality (e.g, to decrypt an encrypted input, to verify that this input is authorized, or to hide a secure watermark in the output). The problem is that cryptographic primitives are typically designed to run on digital computers that use Boolean gates to map sequences of bits to sequences of bits, whereas DNNs are a special type of analog computer that uses linear mappings and ReLUs to map vectors of real numbers to vectors of real numbers. This discrepancy between the discrete and continuous computational models raises the question of what is the best way to implement standard cryptographic primitives as DNNs, and whether DNN implementations of secure cryptosystems remain secure in the new setting, in which an attacker can ask the DNN to process a message whose “bits” are arbitrary real numbers.
>
> In this paper we lay the foundations of this new theory, defining the meaning of correctness and security for implementations of cryptographic primitives as ReLU-based DNNs. We then show that the natural implementations of block ciphers as DNNs can be broken in linear time by using such nonstandard inputs. We tested our attack in the case of full round AES-128, and had success rate in finding randomly chosen keys. Finally, we develop a new method for implementing any desired cryptographic functionality as a standard ReLU-based DNN in a provably secure and correct way. Our protective technique has very low overhead (a constant number of additional layers and a linear number of additional neurons), and is completely practical.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [AI](https://www.schneier.com/tag/ai/), [cryptanalysis](https://www.schneier.com/tag/cryptanalysis/), [cryptography](https://www.schneier.com/tag/cryptography/)

[Posted on February 21, 2025 at 10:33 AM](https://www.schneier.com/blog/archives/2025/02/implementing-cryptography-in-ai-systems.html) •
[5 Comments](https://www.schneier.com/blog/archives/2025/02/implementing-cryptography-in-ai-systems.html#comments)

### Comments

Clive Robinson •
[February 21, 2025 9:28 PM](https://www.schneier.com/blog/archives/2025/02/implementing-cryptography-in-ai-systems.html/#comment-443257)

@ Bruce, ALL,

I have real problems with this view of DNNs expressed by the authors,

> *“The problem is that cryptographic primitives are typically designed to run on digital computers that use Boolean gates to map sequences of bits to sequences of bits, whereas DNNs are a special type of analog computer that uses linear mappings and ReLUs to map vectors of real numbers to vectors of real numbers.”*

As far as I’m aware all current DNN’s are fully digital and made of the same logic gates and thus the same failings as computer ALU’s and the set of “countable numbers” (Integers).

As for implementing “real numbers” no they are still the set of “countable numbers” that are used to fake the sets of any other numbers like the “real numbers” usually very sparsely at best[1].

Whilst in theory you could use Op-Amps and similar components to form the integrators used in traditional analogue computers. Any such network would fail way way before you formed even a small neural network due to 4ktbr noise, distortion, and bias.

Further the “weights” in a DNN are based on the histogram of the input corpus mapped as a sparse multidimensional spectrum.

> *“This discrepancy between the discrete and continuous computational models…”*

This is where the clouds in the air of the theory, come crashing down to the ground due to the lead boots of practical reality. As with an ALU the basic data unit in a DNN is in reality a countable number. Worse the vectors in the DNN form a very small subset of the Countable Numbers. In reality they are a discrete subset and not continuous.

The authors go on to say,

> *“[Which] raises the question of what is the best way to implement standard cryptographic primitives as DNNs, and whether DNN implementations of secure cryptosystems remain secure in the new setting, in which an attacker can ask the DNN to process a message whose “bits” are arbitrary real numbers.”*

In a number of respects this question has been asked and answered before many times over the past thousand years or so.

Consider LLMs by their inputs and outputs not if they are bit representations from logic gates. The natural language input is based on a table of information we usually call a dictionary. With the individual words within it can be placed on a line to form a very sparse series of spectrums that each represent one aspect of the natural language statistics.

The answer to this has always been “flatten the statistics” which basically involves two operations,

1, Remove the sparsity.

One simple but far from perfect way to do this by hand is via a “Straddling Checkerboard”,

<https://en.m.wikipedia.org/wiki/Straddling_checkerboard>

Which was used in the VIC hand cipher.

Thus the question arises as to where and how to do this. Because LLM’s are all about very sparse vector data sets and multiple layers of sparse spectrums.

Arguably if there is reduced or no sparsity the redundancy would be diminished accordingly, and the desired potential for “information capacity” would likewise diminish. Certainly the “stochastic nature” of any LLM would be likewise reduced.

But more importantly the output of an LLM to appear “natural” is very much based on the shape of those multiple spectrums. Flatten the spectrum statistics and the “natural” illusion would quickly vanish.

So the answer to the question is an interesting one because the required solution –compression and flattening– is the antithesis of the required function –of faking normality– by randomised token selection from a statistical curve.

Thus we find ourselves in,

“Rather more than ‘Somewhat of a quandary’.”

Oddly it’s a problem I’ve been thinking about for quite some years now and it started with,

“How to do both Voice compression and Encryption, and producing an output suitable for use with existing HF Radio systems.”

In theory it’s simple… In practice it’s really not, and why although I was hopeful for success I could predicted that the attempt to encrypt voice in an analogue form to send over mobile phone audio channels through the GSM “standard” Codec of “JackPair” would fail (you can not reliably compress random).

Which is why this longish paper limits it’s self.

So rather than read the “abstract” start by reading the “Introduction” it makes rather more sense, and you will find,

> *“In this paper, we study the central problem at the intersection of deep learning a...