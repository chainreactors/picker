---
title: Charles V of Spain Secret Code Cracked
url: https://www.schneier.com/blog/archives/2022/11/charles-v-of-spain-secret-code-cracked.html
source: Schneier on Security
date: 2022-11-30
fetch_date: 2025-10-04T00:06:03.850928
---

# Charles V of Spain Secret Code Cracked

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

## Charles V of Spain Secret Code Cracked

Diplomatic code [cracked](https://www.theguardian.com/world/2022/nov/24/emperor-charles-vs-secret-code-cracked-after-five-centuries) after 500 years:

> In painstaking work backed by computers, Pierrot found “distinct families” of about 120 symbols used by Charles V. “Whole words are encrypted with a single symbol” and the emperor replaced vowels coming after consonants with marks, she said, an inspiration probably coming from Arabic.
>
> In another obstacle, he used meaningless symbols to mislead any adversary trying to decipher the message.
>
> The breakthrough came in June when Pierrot managed to make out a phrase in the letter, and the team then cracked the code with the help of Camille Desenclos, a historian. “It was painstaking and long work but there was really a breakthrough that happened in one day, where all of a sudden we had the right hypothesis,” she said.

Tags: [cryptanalysis](https://www.schneier.com/tag/cryptanalysis/), [encryption](https://www.schneier.com/tag/encryption/), [history of cryptography](https://www.schneier.com/tag/history-of-cryptography/), [Spain](https://www.schneier.com/tag/spain/)

[Posted on November 29, 2022 at 7:19 AM](https://www.schneier.com/blog/archives/2022/11/charles-v-of-spain-secret-code-cracked.html) •
[10 Comments](https://www.schneier.com/blog/archives/2022/11/charles-v-of-spain-secret-code-cracked.html#comments)

### Comments

Clive Robinson •
[November 29, 2022 12:17 PM](https://www.schneier.com/blog/archives/2022/11/charles-v-of-spain-secret-code-cracked.html/#comment-413089)

@ ALL,

> “It was painstaking and long work but there was really a breakthrough that happened in one day, where all of a sudden we had the right hypothesis,”

Demonstrates a point that few ever find out.

In theory systems of this sort are “easy to break” because they are not super-enciphered.

In practice however the way you break a “code book” type system is,

“Guess and test”

Where your guess is made in part from “domain knowledge” and finding correlations.

Thus if you know the date and where the letter originated you can make a plausable guess at what the “code symbols” mean.

The “extras” symbols that have no actuall meaning (nulls) are often just “window dressing” and with enough cipher text they correlate to “random”.

Striping off the layers of such systems is like pealing an onion in two ways,

1, They are layered.

However it can be an engaging “time sink” for a curious mind.

And sometimes as in this case the reward is an opening up into new information that will almost certainly re-write some history books, and spawn new books.

Rombobjörn •
[November 29, 2022 12:31 PM](https://www.schneier.com/blog/archives/2022/11/charles-v-of-spain-secret-code-cracked.html/#comment-413092)

I think the code held long enough for the king’s needs.

Clive Robinson •
[November 29, 2022 12:47 PM](https://www.schneier.com/blog/archives/2022/11/charles-v-of-spain-secret-code-cracked.html/#comment-413094)

@ ALL,

I thought the researchers name “Cécile Pierrot” looked familiar…

And yes, I’ve one of her papers in my “to read pile”,

“Polynomial Time Bounded Distance Decoding near Minkowski’s Bound in Discrete Logarithm Lattices”

<https://hal.archives-ouvertes.fr/hal-01891713/document>

It is not a light read…

JPA •
[November 29, 2022 1:26 PM](https://www.schneier.com/blog/archives/2022/11/charles-v-of-spain-secret-code-cracked.html/#comment-413097)

@Clive

“Its not a light read…”

An understatement if I ever heard one 🙂

Luis García-Caro •
[November 29, 2022 3:20 PM](https://www.schneier.com/blog/archives/2022/11/charles-v-of-spain-secret-code-cracked.html/#comment-413102)

Actually if you refer to him as Charles of Spain, he was Charles I. Charles V was his title as Emperor of the Holy Roman Germanic Empire. He held both titles and thus the confusion.

Ted •
[November 30, 2022 12:54 AM](https://www.schneier.com/blog/archives/2022/11/charles-v-of-spain-secret-code-cracked.html/#comment-413114)

It’s wonderful that a history lecturer was key to providing sparks for the cryptanalysis.

It doesn’t hurt that Camille Desenclos’ knowledge includes the history of cryptography (political, diplomatic and military) in France in the 16th and 17th centuries. 🙂

In one example, her familiarity with historic calendars helped her identify an unknown “pin” symbol (representing King Henry VIII).

France’s calendar at the time started on Easter and knowing this helped her properly calibrate a date written on the letter and build from existing context.

It’s also super intriguing to see how others on the team attempted to solve this puzzle. Researcher and cryptographer Cécile Pierrot encoded the symbols into Python to perform statistical analyses. And with help from fellow cryptographers Gaudry and Zimmermann, the trio developed an algorithm to search for arrangements that might tie to Middle French.

And my goodness back to Camille, it was surely beneficial that she directed research to the Library of Besançon where other messages had clear text translations in the margins.

It’s so exciting to discover these new and vibrant pieces of history! I bet the team’s formal research publication will be fascinating.

<https://www.nancy.fr/a-la-une-109/bibliotheque-stanislas-des-chercheurs-ont-decrypte-une-lettre-chiffree-de-charles-quint-27009.html>

Winter •
[November 30, 2022 2:52 AM](https://www.schneier.com/blog/archives/2022/11/charles-v-of-spain-secret-code-cracked.html/#comment-413117)

@Clive

> “Polynomial Time Bounded Distance Decoding near Minkowski’s Bound in Discrete Logarithm Lattices”

First line of the paper:

> Given a large number of equal non-overlapping spheres, the question of finding the most efficient way to pack them together is quite an old problem.

The sphere packing problem is really, really interesting. It is currently also used to find eligible theories for Quantum Gravity, of all topics [1].

Maryna Viazovska got a 2022 Fields medal for solving the problem in 8 and 24 dimensions
‘https://en.wikipedia.org/wiki/Maryna\_Viazovska

Re: Unpractical Academics

Note how a purely Academic subject has now entered practical use in cryptography. Having learned about such an academic subject in early life would really help to understand the relevance of the paper now.

[1] ‘https://www.researchgate.net/publication/337865824\_Sphere\_packing\_and\_quantum\_gravity

Clive Robinson •
[November 30, 2022 5:48 AM](https://www.schneier.com/blog/archives/2022/11/charles-v-of-spain-secret-code-cracked.html/#comment-413122)

@ Winter,

Re : My reading pile.

> “The sphere packing problem is really, really interesting. It is currently also used to find eligible theories for Quantum Gravity, of all topics”

It’s also a very fundemental question in just about every subject.

Sir Issac Newton formalised something that most do not realise.

Motion is,...