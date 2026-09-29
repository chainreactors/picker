---
title: New Attack Against RSA
url: https://www.schneier.com/blog/archives/2026/09/new-attack-against-rsa.html
source: Schneier on Security
date: 2026-09-28
fetch_date: 2026-09-29T07:41:31.158013
---

# New Attack Against RSA

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

## New Attack Against RSA

ArsTechnica is [reporting](https://arstechnica.com/security/2026/09/theres-a-new-way-to-break-rsa-thats-faster-than-anything-weve-seen-before/) on a “new” attack against RSA, one that bypasses factoring.

First, this attack isn’t new. The original research is from [2007](https://eprint.iacr.org/2007/424). What is new is the implementation.

Second, it is a forgery attack. It allows an attacker to forge digital signatures. It does not recover the private key from the public key.

Third, the attack only works against pure signatures. That is, signatures without any formatting or padding. This is not generally how we use RSA in practice.

Fourth, speed is all relative. This is not a polynomial-time algorithm; it’s a subexponential-time algorithm. But it is somewhat faster than factoring. The authors were able to forge messages for 1024-bit RSA with 1380 CPU core-years (over five real-world months).

The authors have a [webpage](https://github.com/ucsd-hacc/NSNFSSSFSFN) that explains the context much better than the article. And here’s the [paper](https://eprint.iacr.org/2026/2131.pdf).

EDITED TO ADD: Slashdot [thread](https://it.slashdot.org/story/26/09/24/1652228/theres-a-new-way-to-break-rsa-encryption).

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [cryptography](https://www.schneier.com/tag/cryptography/), [forgery](https://www.schneier.com/tag/forgery/), [RSA](https://www.schneier.com/tag/rsa/)

[Posted on September 28, 2026 at 7:02 AM](https://www.schneier.com/blog/archives/2026/09/new-attack-against-rsa.html) •
[11 Comments](https://www.schneier.com/blog/archives/2026/09/new-attack-against-rsa.html#comments)

### Comments

Billy Jack •
[September 28, 2026 7:21 AM](https://www.schneier.com/blog/archives/2026/09/new-attack-against-rsa.html/#comment-458463)

For ssh, my servers all require a minimum 4096 bit key for RSA: RequiredRSASize 4096.

They also require three separate keys, not just one: AuthenticationMethods publickey,publickey,publickey. Usually, the three keys are ED25519, RSA, and ECDSA.

Clive Robinson •
[September 28, 2026 7:32 AM](https://www.schneier.com/blog/archives/2026/09/new-attack-against-rsa.html/#comment-458466)

@ Bruce,

What was it you once said about attacks never get worse with time?

😉

Anonymous •
[September 28, 2026 8:04 AM](https://www.schneier.com/blog/archives/2026/09/new-attack-against-rsa.html/#comment-458469)

When I was young
I used to dream
And the wind blows
And the owl sings
And dogs are driven wild
And dogs break their chains
And run through the lands
A prey to madness
With wild eyes dying
Wild eyes burning
They raise their heads
They swell their cold necks
Like a hungry child’s breath
Or a cat who’s ripped its guts
Like a woman about to give birth
Like a young girl singing
At the stars in the north
At the stars in the south
At the stars in the west
At the stars in the east
At the moon
At the mountains
At the rocks
At the pain
At the thief
At the snakes
Reveal their black black backs
Fresh flesh
Glazed eyes stare
From long pale human faces
We cannot satisfy the hopes
We are now dead
We are all dead
⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛
⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛
⬛⬛⬛🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟨⬛⬛⬛
⬛⬛⬛🟨🟨⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟨🟨⬛⬛⬛
⬜⬛⬛🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨⬛⬛⬜
⬜⬛⬛🟨🟨🟨🟨🟨⬛⬛⬜⬜⬛⬛⬛⬛⬜⬜⬛⬛🟨🟨🟨🟨🟨⬛⬛⬜
⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨⬛⬛🟨🟨🟨🟨⬛⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜
⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜
⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜
⬜⬜⬜⬜⬛🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟨🟨🟨⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛🟨🟨🟨⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟨🟨⬛⬜⬛⬛🟨🟨🟨🟨🟨🟨⬛⬛⬜⬛🟨🟨⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟨🟨⬛⬛⬛⬛🟨🟨🟨🟨🟨🟨⬛⬛⬛⬛🟨🟨⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟨🟨🟨⬛⬛🟨🟨🟨⬛⬛🟨🟨🟨⬛⬛🟨🟨🟨⬛⬜⬜⬜⬜
⬜⬜⬜⬛🟨🟨🟥🟥🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟥🟥🟨🟨⬛⬜⬜⬜
⬜⬜⬜⬛🟨🟥🟥🟥🟥🟨🟨⬛🟨⬛⬛🟨⬛🟨🟨🟥🟥🟥🟥🟨⬛⬜⬜⬜
⬜⬜⬜⬛🟨🟥🟥🟥🟥🟨🟨🟨⬛⬛⬛⬛🟨🟨🟨🟥🟥🟥🟥🟨⬛⬜⬜⬜
⬜⬜⬜⬜⬛🟨🟥🟥🟨🟨🟨🟨⬛🟥🟥⬛🟨🟨🟨🟨🟥🟥🟨⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨⬛🟥🟥⬛🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛🟨🟨🟨🟨🟨⬛⬛🟨🟨🟨🟨🟨⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟨🟨🟨🟨🟨🟨⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜

Rontea •
[September 28, 2026 9:11 AM](https://www.schneier.com/blog/archives/2026/09/new-attack-against-rsa.html/#comment-458470)

If these results hold, we’re looking at a fundamental shift in how we think about RSA security. Signature forgery without full factoring is a conceptual game-changer. The practical risk is limited today, but research like this is exactly the kind of thing that reinforces why cryptographic agility is critical. Systems still using 1024-bit keys or textbook RSA need to take a hard look at their exposure. Rotating keys and moving to modern padding schemes like PSS isn’t just best practice—it’s survival. And for everyone else, this is another reminder: don’t wait for the emergency to start planning your post-RSA future.

David in Toronto •
[September 28, 2026 9:35 AM](https://www.schneier.com/blog/archives/2026/09/new-attack-against-rsa.html/#comment-458471)

@Rontea in short – the building is going to burn down so we should walk, don’t run to the exit.

RSA has been a wee bit precarious for a while due to the exponential growth in key lengths. I haven’t checked in a while but is anyone supporting keys longer than 4096 bits?

Clive Robinson •
[September 28, 2026 10:20 AM](https://www.schneier.com/blog/archives/2026/09/new-attack-against-rsa.html/#comment-458472)

@ All,

Don’t try saying “NSNFSSSFSFN” it will sound like you are suffering from a sleepless night 😉

But more importantly,

> “[T]he attack only works against pure signatures. That is, signatures without any formatting or padding. This is not generally how we use RSA in practice.”

It needs to be said that as a general rule of thumb in crypto you do not use padding, formatting, or linear codes –error correction– at what would be the “plaintext” level as it can easily give rise to short cuts or distinguishers around which attacks can be improved or automated (Structural Attacks).

As a general rule protection against transmission errors and the like is carried out at or above the ciphertext level specifically to the transmission channel. To avoid “structural attacks”.

In the past people have tried to incorporate error correction and ciphering. Mostly it’s been rejected with the only one to “clear the grass” being the work from the late 1970’s by Robert McEliece.

However a cautionary note about McEliece is that whilst you can use many different linear error correcting codes (‘C’), nearly all have failed to structural attacks, leaving the originally suggested Linear Goppa Codes.

However due to ‘C’ McEliece has made it as a candidate for “Post Quantum Cryptography”(PQC).

KC •
[September 28, 2026 11:38 AM](https://www.schneier.com/blog/archives/2026/09/new-attack-against-rsa.html/#comment-458475)

Hat tip to Bruce, Clive, and Dan
Great FAQs on the authors’ webpage.

From Dan:

> “some real-world systems continue to use blind-signature, also known as textbook, RSA.”

This includes the Privacy Pass protocol in Apple, Cloudflare, and many others. However, an attacker would need to request 2^43 tokens.

And from the paper:

“Apple appears...