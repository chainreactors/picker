---
title: Model Extraction from Neural Networks
url: https://www.schneier.com/blog/archives/2024/07/model-extraction-from-neural-networks.html
source: Schneier on Security
date: 2024-07-02
fetch_date: 2025-10-06T17:46:38.007949
---

# Model Extraction from Neural Networks

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

## Model Extraction from Neural Networks

A [new paper](https://eprint.iacr.org/2023/1526), “Polynomial Time Cryptanalytic Extraction of Neural Network Models,” by Adi Shamir and others, uses ideas from differential cryptanalysis to extract the weights inside a neural network using specific queries and their results. This is much more theoretical than practical, but it’s a really interesting result.

> **Abstract:**
>
> Billions of dollars and countless GPU hours are currently spent on training Deep Neural Networks (DNNs) for a variety of tasks. Thus, it is essential to determine the difficulty of extracting all the parameters of such neural networks when given access to their black-box implementations. Many versions of this problem have been studied over the last 30 years, and the best current attack on ReLU-based deep neural networks was presented at Crypto’20 by Carlini, Jagielski, and Mironov. It resembles a differential chosen plaintext attack on a cryptosystem, which has a secret key embedded in its black-box implementation and requires a polynomial number of queries but an exponential amount of time (as a function of the number of neurons). In this paper, we improve this attack by developing several new techniques that enable us to extract with arbitrarily high precision all the real-valued parameters of a ReLU-based DNN using a polynomial number of queries and a polynomial amount of time. We demonstrate its practical efficiency by applying it to a full-sized neural network for classifying the CIFAR10 dataset, which has 3072 inputs, 8 hidden layers with 256 neurons each, and about 1.2 million neuronal parameters. An attack following the approach by Carlini et al. requires an exhaustive search over 2^256 possibilities. Our attack replaces this with our new techniques, which require only 30 minutes on a 256-core computer.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [cryptography](https://www.schneier.com/tag/cryptography/)

[Posted on July 1, 2024 at 7:05 AM](https://www.schneier.com/blog/archives/2024/07/model-extraction-from-neural-networks.html) •
[4 Comments](https://www.schneier.com/blog/archives/2024/07/model-extraction-from-neural-networks.html#comments)

### Comments

[cybershow](https://cybershow.uk/) •
[July 2, 2024 5:20 AM](https://www.schneier.com/blog/archives/2024/07/model-extraction-from-neural-networks.html/#comment-439012)

It seems a good thing if nobody will be able to create opaque neural

The week’s Cybershow is an election special, because we’re voting this
Thursday in the UK, so I hope it’s okay to post this link:

[Election Special](https://cybershow.uk/episodes.php?id=29)

Clive Robinson •
[July 2, 2024 12:42 PM](https://www.schneier.com/blog/archives/2024/07/model-extraction-from-neural-networks.html/#comment-439022)

@ ALL,

The paper at 32 pages of fairly dense text is going to take awhile.

But before doing that thinking about the problem shows that it might actually be a simpler task than expected.

If you think about language it is highly structured with a lot of redundance.

Part of that redundancy is words form chains we call sentences, but they also in effect form cycles as well.

As I’ve noted before the “Digital Neural Network”(DNN) is in reality an overly large “Digital Signal Processing”(DSP) filter block which is effectively an adaptive filter. That is where the weights are built by what is in effect a repeated cycle of pushing discrete strings of text through.

The result is that as you would expect the multiple layers in language get teased out and build spectral signitures. These overlay each other in various ways.

The problem is that most people see a spectrum as moving in a simply ordered way much like a number line. The reality is that is a highly specialised form that is convenient for human reasoning based on mathematics and logic.

The reality of the language spectrum is very different as well as being multidimensional.

However it is statistically ordered which means not only is there a mapping from the special case spectrums to the word usage of the language spectrum but importantly discordant as it might appear to ordinary viewing to the point of seeming random it is not. In fact it’s a long way from random, and is built on layers of fairly simple rules.

The simplicity of this means that in some ways it is very much like the structure you find in simple substitution ciphers constructed of simple mathematics and logic.

Therefore it is reasonable if not logical to expect any kind of attack that works against a substitution cipher constructed of simple logic and maths to also work against the mapping of language that is also based on simple logic and maths.

The problem is that language contains a degree of random fluff.

We all get taught the “I before E except after C” rule, however it’s often wrong, the why of that is both other rules and what appears to be random, but is actually based on the abilities of the human vocal tract with some variance based on how the brain forms in the first couple of years but to a lesser extent also upto the mid teens.

After you hit your twenties it can become near impossible to learn to speak sufficiently dissimilar languages with any degree of fluency in pronunciation.

It will be interesting to see what @Andy Farnell and one or two others have to say on the various aspects of this.

JonKnowsNothing •
[July 3, 2024 6:46 AM](https://www.schneier.com/blog/archives/2024/07/model-extraction-from-neural-networks.html/#comment-439047)

@Clive, All

re:

> *We all get taught the “I before E except after C” rule, however it’s often wrong, the why of that is both other rules and what appears to be random, but is actually based on the abilities of the human vocal tract with some variance*

The I before E rule always had me flummoxed until I learned the full rule

* I before E except after C AND when sounded as A as in ….

That last part didn’t help much because I heard

* I before E except after C AND when sounded as A as in neighbor and way

The neighbor part was OK but the way part just tossed me until I saw the rule in print

* I before E except after C AND when sounded as A as in neighbor and weight

So both vocalized and printed forms can lead to errors.

There are some languages that specific sound combinations are learned in childhood and adults cannot learn to produce those sounds. This aspect of vocal language is the source of “not a native speaker” labels and a large amount of faux-UK accents by Hollywood actors.

In some musical venues, like Operas, where the lyrics are in a different language, the singers spend a large amount of time learning “vocal pronunciation” techniques as well as the required musical techniques for the piece.

A favorite example of how sounds change not only the rhythm but the word pronunciation is from Chaucer

* And smale foweles maken melodye,...