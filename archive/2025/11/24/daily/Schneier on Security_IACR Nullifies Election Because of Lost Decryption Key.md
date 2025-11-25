---
title: IACR Nullifies Election Because of Lost Decryption Key
url: https://www.schneier.com/blog/archives/2025/11/iacr-nullifies-election-because-of-lost-decryption-key.html
source: Schneier on Security
date: 2025-11-24
fetch_date: 2025-11-25T03:13:24.555871
---

# IACR Nullifies Election Because of Lost Decryption Key

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

## IACR Nullifies Election Because of Lost Decryption Key

The International Association of Cryptologic Research—the academic cryptography association that’s been putting conferences like Crypto (back when “crypto” meant “cryptography”) and Eurocrypt since the 1980s—had to [nullify](https://www.iacr.org/news/item/27138) an online election when trustee Moti Yung lost his decryption key.

> For this election and in accordance with the bylaws of the IACR, the three members of the IACR 2025 Election Committee acted as independent trustees, each holding a portion of the cryptographic key material required to jointly decrypt the results. This aspect of Helios’ design ensures that no two trustees could collude to determine the outcome of an election or the contents of individual votes on their own: all trustees must provide their decryption shares.
>
> Unfortunately, one of the three trustees has irretrievably lost their private key, an honest but unfortunate human mistake, and therefore cannot compute their decryption share. As a result, Helios is unable to complete the decryption process, and it is technically impossible for us to obtain or verify the final outcome of this election.

The group will redo the election, but this time setting a 2-of-3 threshold scheme for decrypting the results, instead of requiring all three

[News](https://arstechnica.com/security/2025/11/cryptography-group-cancels-election-results-after-official-loses-secret-key/) [articles](https://www.nytimes.com/2025/11/21/world/cryptography-group-lost-election-results.html?smid=nytcore-android-share).

Tags: [encryption](https://www.schneier.com/tag/encryption/), [keys](https://www.schneier.com/tag/keys/), [operational security](https://www.schneier.com/tag/operational-security/), [voting](https://www.schneier.com/tag/voting/)

[Posted on November 24, 2025 at 7:03 AM](https://www.schneier.com/blog/archives/2025/11/iacr-nullifies-election-because-of-lost-decryption-key.html) •
[8 Comments](https://www.schneier.com/blog/archives/2025/11/iacr-nullifies-election-because-of-lost-decryption-key.html#comments)

### Comments

Alan •
[November 24, 2025 7:11 AM](https://www.schneier.com/blog/archives/2025/11/iacr-nullifies-election-because-of-lost-decryption-key.html/#comment-450107)

Zero Knowledge Proofs could do this better — secure, confidential voting with no decryption key required to see the results.

Jan Willem de Vries •
[November 24, 2025 8:08 AM](https://www.schneier.com/blog/archives/2025/11/iacr-nullifies-election-because-of-lost-decryption-key.html/#comment-450109)

This is a brilliant joke. A cryptology organisation which fails due to a tobe foreseen mistake.

Clive Robinson •
[November 24, 2025 8:29 AM](https://www.schneier.com/blog/archives/2025/11/iacr-nullifies-election-because-of-lost-decryption-key.html/#comment-450111)

@ ALL,

**To much security makes things fragile**

First off there is the old human sayings of,

1, Accidents happen.

I’m known for saying,

“There is no such thing as accidents, only too little time, knowledge or both.”

As for humans, they are not the only thing to err or fail, systems do it to as many can attest. But untill recently we said that such things were the product of man thus man was the element that was responsible as an easy get out rather than admit “we don’t know enough”.

The design of the voting system was not that of the IACR but another organisation entirely. I would also guess that based on appearances neither the IACR or the voting system organisation had any engineers that had experience in designing intrinsically safe, or fail safe systems, or they got over ridden.

Because there are two fundamental rules for such design,

1, Design to have no single point of failure.
2, Design to fail safe.

If we look at what happened both rules were apparently broken.

The article says,

> *“Per the association’s bylaws, three members of the election committee act as independent trustees. To prevent two of them from colluding to cook the results, each trustee holds a third of the cryptographic key material needed to decrypt results.”*

And thereby each of the trustee becomes intrinsically,

“A single point of failure”

Whilst the second point of “fail safe” can be problematic with some security protocols and the supporting Cryptographic based systems. The first rule becomes even more critical and should always hold.

The use of an M of N shared secret protocol would have stopped this particular “fail unsafe” issue.

As I’ve previously noted,

> *“At the very least the associations rules should have allowed for human frailty. Aircraft fall out of the sky, ships sink, and motor vehicles crash many on more than a daily basis, likewise sickness and unfortunate health events take many more, often quite unexpectedly.”*

These things may be unpalatable, but we do recognise they happen all the time.

Robin •
[November 24, 2025 8:52 AM](https://www.schneier.com/blog/archives/2025/11/iacr-nullifies-election-because-of-lost-decryption-key.html/#comment-450112)

I am reassured that there are at least some officials who are honorable enough to resign when they screw up. Once upon a time politicians did that.

KC •
[November 24, 2025 9:56 AM](https://www.schneier.com/blog/archives/2025/11/iacr-nullifies-election-because-of-lost-decryption-key.html/#comment-450113)

**From Ben Adida on Bluesky:**

> The International Association for Cryptologic Research has used [heliosvoting.org](https://vote.heliosvoting.org/) – my online voting system – for a number of years.
>
> This year, a trustee lost their secret key. The election has to be re-run.
>
> Below, a few thoughts that didn’t fit in the NYT piece.

<https://bsky.app/profile/benadida.com/post/3m66rgiiogc2a>

NombreNoImportante •
[November 24, 2025 12:27 PM](https://www.schneier.com/blog/archives/2025/11/iacr-nullifies-election-because-of-lost-decryption-key.html/#comment-450117)

……….. Kind of hard to miss the point that the current president of that board messed up… Crypto the point of the Org he is president of… New President time?

Clive Robinson •
[November 24, 2025 2:53 PM](https://www.schneier.com/blog/archives/2025/11/iacr-nullifies-election-because-of-lost-decryption-key.html/#comment-450119)

@ KC, ALL,

With regards the comments of “Ben Adida” –the implementor of the Helios Voting system used–, he links to the NYT article, the last two paragraphs of which are,

> *“Though errors are rare in Helios’s work with the cryptology group, said Mr. Adida, the software engineer, the case showed that there can be trade-offs in designing and using hyper-secure systems.*
>
> “It turns out that managing keys and managing secret keys is the hardest part of this — even among the world’s best cryptographers,” he said.”

The article and what has subsequently been said in the MSM and trade press and blogs etc still does not say who was responsible for the desig...