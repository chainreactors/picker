---
title: Backdoor in TETRA Police Radios
url: https://www.schneier.com/blog/archives/2023/07/backdoor-in-tetra-police-radios.html
source: Schneier on Security
date: 2023-07-27
fetch_date: 2025-10-04T11:57:11.075255
---

# Backdoor in TETRA Police Radios

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

## Backdoor in TETRA Police Radios

Seems that there is a [deliberate backdoor](https://www.vice.com/en/article/4a3n3j/backdoor-in-police-radios-tetra-burst) in the twenty-year-old TErrestrial Trunked RAdio (TETRA) standard used by police forces around the world.

> The European Telecommunications Standards Institute (ETSI), an organization that standardizes technologies across the industry, first created TETRA in 1995. Since then, TETRA has been used in products, including radios, sold by Motorola, Airbus, and more. Crucially, TETRA is not open-source. Instead, it relies on what the researchers describe in their presentation slides as “secret, proprietary cryptography,” meaning it is typically difficult for outside experts to verify how secure the standard really is.
>
> The researchers said they worked around this limitation by purchasing a TETRA-powered radio from eBay. In order to then access the cryptographic component of the radio itself, Wetzels said the team found a vulnerability in an interface of the radio.
>
> […]
>
> Most interestingly is the researchers’ findings of what they describe as the backdoor in TEA1. Ordinarily, radios using TEA1 used a key of 80-bits. But Wetzels said the team found a “secret reduction step” which dramatically lowers the amount of entropy the initial key offered. An attacker who followed this step would then be able to decrypt intercepted traffic with consumer-level hardware and a cheap software defined radio dongle.

Looks like the encryption algorithm was intentionally weakened by intelligence agencies to facilitate easy eavesdropping.

> Specifically on the researchers’ claims of a backdoor in TEA1, Boyer added “At this time, we would like to point out that the research findings do not relate to any backdoors. The TETRA security standards have been specified together with national security agencies and are designed for and subject to export control regulations which determine the strength of the encryption.”

And I would like to point out that that’s the very definition of a backdoor.

Why aren’t we done with secret, proprietary cryptography? It’s just not a good idea.

[Details](https://tetraburst.com/) of the security analysis. Another [news article](https://www.wired.com/story/tetra-radio-encryption-backdoor/).

Tags: [backdoors](https://www.schneier.com/tag/backdoors/), [cryptography](https://www.schneier.com/tag/cryptography/), [eavesdropping](https://www.schneier.com/tag/eavesdropping/), [encryption](https://www.schneier.com/tag/encryption/), [infrastructure](https://www.schneier.com/tag/infrastructure/), [law enforcement](https://www.schneier.com/tag/law-enforcement/), [police](https://www.schneier.com/tag/police/), [radio](https://www.schneier.com/tag/radio/)

[Posted on July 26, 2023 at 7:05 AM](https://www.schneier.com/blog/archives/2023/07/backdoor-in-tetra-police-radios.html) •
[40 Comments](https://www.schneier.com/blog/archives/2023/07/backdoor-in-tetra-police-radios.html#comments)

### Comments

David McClain •
[July 26, 2023 9:25 AM](https://www.schneier.com/blog/archives/2023/07/backdoor-in-tetra-police-radios.html/#comment-424818)

I agree on the weak homebrew crypto.

But the article also stated that they used shortened 32- and 40-bit keying on the weakened systems. It wouldn’t matter how good the algorithm is in those cases. The weakness of the key allows for simple brute force searching. Took about a minute on a laptop computer.

Dexter •
[July 26, 2023 9:58 AM](https://www.schneier.com/blog/archives/2023/07/backdoor-in-tetra-police-radios.html/#comment-424821)

“Why aren’t we done with secret, proprietary cryptography?”

Presumably for the reason you give here: <https://www.youtube.com/watch?v=n61_0-gG6Hg>.

Ted •
[July 26, 2023 11:13 AM](https://www.schneier.com/blog/archives/2023/07/backdoor-in-tetra-police-radios.html/#comment-424828)

In Midnight Blue’s write up of TETRA:BURST (and its five CVEs), they report the following on CVE-2022-24403: “…consider TEA1 equivalent to cleartext”

This is not dissimilar to Matthew Green’s statement to KZ: “I wouldn’t say it’s equivalent to using no encryption, but it’s really bad.”

Kim Zetter also published a follow-up interview with ETSI’s Brian Murgatroyd:

<https://zetter.substack.com/p/interview-with-the-etsi-standards>

Clive Robinson •
[July 26, 2023 11:51 AM](https://www.schneier.com/blog/archives/2023/07/backdoor-in-tetra-police-radios.html/#comment-424831)

As this is getting auto-moded, so black-holed I must appologize for choping it into bits,

@ Bruce, ALL,

Part 1,

Re : It started in WWII.

> “Why aren’t we done with secret, proprietary cryptography? It’s just not a good idea.”

Remember this actually goes back well into the last century, that is it’s more than 20years old.

The TEA1 and TEA2 idea, is exactly the same as the GSM A5/1 and A5/2 over the air crypto[1].

All the EU standards bodies of the time were doing this nonsense of Weak Crypto for second and third world countries. Heck look up the history of the NSA and CIA with regards Crypto AG of Zug Switzerland. They had three levels of crypto.

Clive Robinson •
[July 26, 2023 11:57 AM](https://www.schneier.com/blog/archives/2023/07/backdoor-in-tetra-police-radios.html/#comment-424832)

@ Bruce, ALL,

Part 2,

As I’ve indicated before the original “coin counting” mechanism designed by Boris Haglin and used in the US army Field Cipher machines in WWII –of which around 140,000 were issued and still in use during the Korean War,– had a range of keys covering from very weak through to strong (for the time). The keys issued to the forces were done from a central managment, and were thus mostly strong.

However with more than 85% of the key space not being strong, any one capturing and copying the design without knowing about the key strengths would like as not just use the keys randomly, so on average around half could be broken fairly quickly.

Bob •
[July 26, 2023 12:03 PM](https://www.schneier.com/blog/archives/2023/07/backdoor-in-tetra-police-radios.html/#comment-424836)

“It’s not a backdoor, it’s a government backdoor.”

Clive Robinson •
[July 26, 2023 12:05 PM](https://www.schneier.com/blog/archives/2023/07/backdoor-in-tetra-police-radios.html/#comment-424837)

@ Bruce, ALL,

Part 3,

If people study the history of WWII code breaking in Bletchly and other places (like India, where my father was stationed). It was mostly based on the idea of “possibles” that is as messages got decoded they became part of a “card index” database. When a new message came in “Huf Duf” HF Direction Finding and other “tells” in the then nascent “Traffic Analysis” gave lookups in the database.

Clive Robinson •
[July 26, 2023 12:06 PM](https://www.schneier.com/blog/archives/2023/07/backdoor-in-tetra-police-radios.html/#comment-424838)

@ Bruce, ALL,

Part 4,

This gave “probable plaintext” that were then used in “cribs” to reduce the code ...