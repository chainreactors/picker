---
title: Compromised TLS Certificates
url: https://www.schneier.com/blog/archives/2026/10/compromised-tls-certificates.html
source: Instapaper: Unread
date: 2026-10-28
fetch_date: 2026-10-29T07:53:20.297933
---

# Compromised TLS Certificates

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

## Compromised TLS Certificates

The Indian CA eMudhra Limited has eight TLS certificates with [laughably weak private keys](https://arstechnica.com/security/2026/10/the-internet-goes-on-high-alert-after-discovery-of-8-compromised-tls-certs/):

> The compromised eMudhra keys were defective at a level that’s challenging the imagination of many of the engineers studying the incident. A normal size for a NIST P-384 elliptic curve cryptography private key contains roughly 384 bits of entropy, a size allowing almost 2384, or a number with 116 digits, different possibilities. The private key sizes of the compromised keys ranged from 3 to 8 bits. Astonishingly, the private keys were 4, 56, 66, 115, 155, 156, 230, 237.
>
> “That is extremely in the ‘this should not be possible’ category,” Valdorda said. “Maybe some horribly dangerous key generation interface has a ‘size’ parameter and they set it to 1 by mistake???”
>
> Ben Cartwright-Cox, director of BGP.tools, said: “My guess is that it’s example code that accidentally leaked to production, but hard to know. But it’s bonkers that no one noticed.”
>
> At this early stage, the most immediate threat appears to be for those using VPNs, especially in countries with governments likely to maliciously intercept traffic. There are likely many other cases for concern. End users largely have no recourse other than to hold off using many non-browser forms of TLS communication until they receive assurances updates are in place.

The whole certificate regime has long been a mess:

> The incident is the latest to expose a fatal flaw in the TLS regimen. It’s only as strong as its weakest link, which in this case was eMudhra. Fortunately, transparency logs account for much of that failure, but this measure requires parties to actively monitor massive feeds and works only after unauthorized certificates have been issued. eMudhra representatives weren’t immediately available to answer questions.
>
> One caveat: exploiting compromised certificates requires an active adversary-in-the-middle attack, meaning the attacker must act as a proxy between two TLS parties and receive encrypted traffic, decrypt it, reencrypt it, and send it to the other party. Such capabilities, in some cases, are usually limited to only the most well-resourced attackers. People with control of a local network­at a coffee shop, university, or other organization­face much less of a challenge.

Cleanup of this is going to be another mess—and it’s right on top of the PHP vulnerabilities.

[Some](https://blog.talosintelligence.com/compromised-intermediate-certificates/) [more](https://www.paloaltonetworks.com/cyberpedia/what-is-a-tls-certificate-risk) [information](https://blog.cloudflare.com/emudhra-certificate-compromise/).

Tags: [India](https://www.schneier.com/tag/india/), [keys](https://www.schneier.com/tag/keys/), [TLS](https://www.schneier.com/tag/tls/)

[Posted on October 23, 2026 at 7:04 AM](https://www.schneier.com/blog/archives/2026/10/compromised-tls-certificates.html) •
[26 Comments](https://www.schneier.com/blog/archives/2026/10/compromised-tls-certificates.html#comments)

### Comments

wiredog •
[October 23, 2026 9:00 AM](https://www.schneier.com/blog/archives/2026/10/compromised-tls-certificates.html/#comment-459187)

Oblig. XKCD (Esp. the alt text.)
<https://m.xkcd.com/3314/>

wiredog •
[October 23, 2026 9:01 AM](https://www.schneier.com/blog/archives/2026/10/compromised-tls-certificates.html/#comment-459188)

Oblig. XKCD (Esp. the alt text.)
<https://m.xkcd.com/3314/>

Clive Robinson •
[October 23, 2026 9:34 AM](https://www.schneier.com/blog/archives/2026/10/compromised-tls-certificates.html/#comment-459190)

@ Bruce, ALL,

With regards,

> “… has eight TLS certificates with laughably weak private keys”

It may be more than eight.

If you go to,

‘https://emudhra.we-have-a-problem.com

It now shows 14 certs to be tested, yesterday afternoon UK time it was 12…

But the reality is that atleast 60million or so certs 3Mudhra signed are now garbage.

But also as many as cyber-attackers want to generate.

Because there are way way to many embedded and similar systems that will never get their cert files upgraded…

This is a problem that is not going to go away for years.

As for the article saying,

> *“NIST P-384 elliptic curve cryptography private key contains roughly 384 bits of entropy, a size allowing almost 2384, or a number with 116 digits, different possibilities.”*

Anyone else thinking it does not take the “leading zeros” issue into the math?

Bcs •
[October 23, 2026 9:43 AM](https://www.schneier.com/blog/archives/2026/10/compromised-tls-certificates.html/#comment-459191)

This incident reenforces the argument that it should be easy to revoke certificates. Both in the mechanism for propagating CRLs quickly and widely as well as in setting things up so that the “economics” favor doing so quickly if there’s even a reasonable suspicion that it is justified.

One change that would facilitate the second part would be to adjust TLS processing so that reporting cert chains to multiple root CAs is both supported and expected, so that it would take multiple revocations to take down sites. (I haven’t actually looked in detail, but I think that could be accomplished by simply expecting TLS clients to ignore “extraneous” certs provided during the handshake.)

Clive Robinson •
[October 23, 2026 10:00 AM](https://www.schneier.com/blog/archives/2026/10/compromised-tls-certificates.html/#comment-459192)

@ Bcs, ALL,

With regards,

> “This incident reenforces the argument that it should be easy to revoke certificates.”

It would be nice if it were not for the flip side of “Censorship” and taking away “Individuals rights”.

We are moving very rapidly into “Authoritarian times” in which the “common truth” gets killed off and replaced by Government or Corporate faux-truth.

For instance if you have a current Android OS phone if you go to the

‘https://emudhra.we-have-a-problem.com

Site and get green across the board what is it actually telling you?

Yup Google has fritzed with your phone and you were not aware of it…

Now consider what Google is going to do in just a few weeks time,

<https://arstechnica.com/gadgets/2026/03/with-developer-verification-googles-apple-envy-threatens-to-dismantle-androids-open-legacy/>

D •
[October 23, 2026 10:25 AM](https://www.schneier.com/blog/archives/2026/10/compromised-tls-certificates.html/#comment-459193)

There is more detail on this, including comments from eMudhra engineers, on the Mozilla issue tracker: <https://bugzilla.mozilla.org/show_bug.cgi?id=2083449>

It looks like they were using the correct HSM device for keys, but the script they used to handle the key generation was not actually using the HSM device for key signing. Looks like a simple enough mistake.

Although it would have been trivial for them to detect this if they had attempted to use t...