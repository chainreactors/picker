---
title: Security Analysis of Threema
url: https://www.schneier.com/blog/archives/2023/01/security-analysis-of-threema.html
source: Schneier on Security
date: 2023-01-20
fetch_date: 2025-10-04T04:25:29.725617
---

# Security Analysis of Threema

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

## Security Analysis of Threema

A group of Swiss researchers [have published](https://breakingthe3ma.app/files/Threema-PST22.pdf) an impressive security analysis of Threema.

> We provide an extensive cryptographic analysis of Threema, a Swiss-based encrypted messaging application with more than 10 million users and 7000 corporate customers. We present seven different attacks against the protocol in three different threat models. As one example, we present a cross-protocol attack which breaks authentication in Threema and which exploits the lack of proper key separation between different sub-protocols. As another, we demonstrate a compression-based side-channel attack that recovers users’ long-term private keys through observation of the size of Threema encrypted back-ups. We discuss remediations for our attacks and draw three wider lessons for developers of secure protocols.

From a [news article](https://arstechnica.com/information-technology/2023/01/messenger-billed-as-better-than-signal-is-riddled-with-vulnerabilities/):

> Threema has more than 10 million users, which include the Swiss government, the Swiss army, German Chancellor Olaf Scholz, and other politicians in that country. Threema developers advertise it as a more secure alternative to Meta’s WhatsApp messenger. It’s among the top Android apps for a fee-based category in Switzerland, Germany, Austria, Canada, and Australia. The app uses a custom-designed encryption protocol in contravention of established cryptographic norms.

The company is performing the usual denials and deflections:

> In a [web post](https://threema.ch/en/blog/posts/news-alleged-weaknesses-statement), Threema officials said the vulnerabilities applied to an old protocol that’s no longer in use. It also said the researchers were overselling their findings.
>
> “While some of the findings presented in the paper may be interesting from a theoretical standpoint, none of them ever had any considerable real-world impact,” the post stated. “Most assume extensive and unrealistic prerequisites that would have far greater consequences than the respective finding itself.”
>
> Left out of the statement is that the protocol the researchers analyzed is old because they disclosed the vulnerabilities to Threema, and Threema updated it.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [authentication](https://www.schneier.com/tag/authentication/), [cryptanalysis](https://www.schneier.com/tag/cryptanalysis/), [encryption](https://www.schneier.com/tag/encryption/), [side-channel attacks](https://www.schneier.com/tag/side-channel-attacks/), [threat models](https://www.schneier.com/tag/threat-models/), [vulnerabilities](https://www.schneier.com/tag/vulnerabilities/)

[Posted on January 19, 2023 at 7:21 AM](https://www.schneier.com/blog/archives/2023/01/security-analysis-of-threema.html) •
[31 Comments](https://www.schneier.com/blog/archives/2023/01/security-analysis-of-threema.html#comments)

### Comments

Winter •
[January 19, 2023 8:42 AM](https://www.schneier.com/blog/archives/2023/01/security-analysis-of-threema.html/#comment-415854)

> The app uses a custom-designed encryption protocol in contravention of established cryptographic norms.

That says it all. No more information needed.

Clive Robinson •
[January 19, 2023 9:12 AM](https://www.schneier.com/blog/archives/2023/01/security-analysis-of-threema.html/#comment-415856)

@ ALL,

I will have to read through the paper to be sure, but from what is given above not only have the designed their own cryptography, but their own protocols.

AND in the process not applied the principles of segregation and issolation sufficiently.

Then of course there are those darn “side channels”… Where there is one found there is generally a family of them hiding away, breeding more at every twist and turn.

Frank •
[January 19, 2023 10:05 AM](https://www.schneier.com/blog/archives/2023/01/security-analysis-of-threema.html/#comment-415858)

Someone did a nice analysis of the vulnerabilities described, discussing what is required to pull off the attack, what could be gained, and if/how it was fixed.

<https://blog.dbrgn.ch/2023/1/14/threema/>

Ted •
[January 19, 2023 11:26 AM](https://www.schneier.com/blog/archives/2023/01/security-analysis-of-threema.html/#comment-415862)

@Frank

> Someone did a nice analysis of the vulnerabilities described

It’s funny you say it like that. That analysis is most interesting to me since it’s written by a current software engineer at Threema and provides a more technical eval of the vulnerabilities. Plus, it’s done in a less standoffish manner.

It’s interesting to compare Danilo’s attack analyses with the summaries provided by the ETH Zurich researchers. Dan provided a link to a higher-level summary from the Swiss researchers:

<https://breakingthe3ma.app/>

I guess these specific attacks are moot points since they have supposedly been patched. However, I’m wondering who all is going to do a security review on the updated messenger app and also on the Ibex protocol.

dorukayhan •
[January 19, 2023 11:46 AM](https://www.schneier.com/blog/archives/2023/01/security-analysis-of-threema.html/#comment-415863)

> Left out of [Threema’s] statement is that the protocol the researchers analyzed is old because they disclosed the vulnerabilities to Threema, and Threema updated it.

bruh.

David in Toronto •
[January 19, 2023 2:35 PM](https://www.schneier.com/blog/archives/2023/01/security-analysis-of-threema.html/#comment-415870)

@dorukayhan

“Old.”

“How Old?”

“Tuesday”

“AM or PM?”

vas pup •
[January 19, 2023 5:02 PM](https://www.schneier.com/blog/archives/2023/01/security-analysis-of-threema.html/#comment-416077)

Tag – vulnerabilities

How one volcano could trigger world chaos

<https://www.bbc.com/future/article/20230117-malacca-strait-the-sea-lane-that-could-trigger-world-chaos>

“…below them, running along the seabed, is a dense array of submarine internet cables that keep the world online.

A large and relatively nearby earthquake would be a menace of similar scale. It could cause a tsunami to hit the strait, as the Boxing Day tsunami did in 2004. It would also cause turbidity currents – clouds of fast-moving, shaken-up sediment – that rip across the seabed.

“That’s typically what severs cables,” Mani says. “In the Tonga eruption” – Hunga Tonga-Hunga Ha’apai’s VEI5 eruption in January 2022 – “it was turbidity currents that severed the cables, causing a regional internet blackout. The turbidity currents also bury those cables, making their recovery even harder.” (Read more about the scale and aftermath of this eruption from BBC News: “Tonga eruption: Atlantic seafloor felt Pacific volcano megablast”.

Worse, the severing of those cables would cause economic pandemonium. “Trillions of dollars are transported through those cables every single day,” says Mani, “and that basically props ...