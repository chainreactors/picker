---
title: An Untrustworthy TLS Certificate in Browsers
url: https://www.schneier.com/blog/archives/2022/11/an-untrustworthy-tls-certificate-in-browsers.html
source: Schneier on Security
date: 2022-11-11
fetch_date: 2025-10-03T22:26:20.352486
---

# An Untrustworthy TLS Certificate in Browsers

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

## An Untrustworthy TLS Certificate in Browsers

The major browsers natively trust a whole bunch of certificate authorities, and some of them are [really sketchy](https://www.washingtonpost.com/technology/2022/11/08/trustcor-internet-addresses-government-connections/):

> Google’s Chrome, Apple’s Safari, nonprofit Firefox and others allow the company, TrustCor Systems, to act as what’s known as a root certificate authority, a powerful spot in the internet’s infrastructure that guarantees websites are not fake, guiding users to them seamlessly.
>
> The company’s Panamanian registration records show that it has the identical slate of officers, agents and partners as a spyware maker identified this year as an affiliate of Arizona-based Packet Forensics, which public contracting records and company documents show has sold communication interception services to U.S. government agencies for more than a decade.
>
> […]
>
> In the earlier spyware matter, researchers Joel Reardon of the University of Calgary and Serge Egelman of the University of California at Berkeley found that a Panamanian company, Measurement Systems, had been paying developers to include code in a variety of innocuous apps to record and transmit users’ phone numbers, email addresses and exact locations. They estimated that those apps were downloaded more than 60 million times, including 10 million downloads of Muslim prayer apps.
>
> Measurement Systems’ website was registered by Vostrom Holdings, according to historic domain name records. Vostrom filed papers in 2007 to do business as Packet Forensics, according to Virginia state records. Measurement Systems was registered in Virginia by Saulino, according to another state filing.

More  [details](https://groups.google.com/a/mozilla.org/g/dev-security-policy/c/oxX69KFvsm4) by Reardon.

Cory Doctorow does a [great job](https://pluralistic.net/2022/11/09/infosec-blackpill/#on-trusting-trust) explaining the context and the general security issues.

EDITED TO ADD (11/10): Slashdot [thread](https://yro.slashdot.org/story/22/11/10/1622239/mysterious-company-with-government-ties-plays-key-internet-role).

Tags: [browsers](https://www.schneier.com/tag/browsers/), [certificates](https://www.schneier.com/tag/certificates/), [TLS](https://www.schneier.com/tag/tls/), [trust](https://www.schneier.com/tag/trust/)

[Posted on November 10, 2022 at 9:18 AM](https://www.schneier.com/blog/archives/2022/11/an-untrustworthy-tls-certificate-in-browsers.html) •
[29 Comments](https://www.schneier.com/blog/archives/2022/11/an-untrustworthy-tls-certificate-in-browsers.html#comments)

### Comments

Clive Robinson •
[November 10, 2022 9:52 AM](https://www.schneier.com/blog/archives/2022/11/an-untrustworthy-tls-certificate-in-browsers.html/#comment-412068)

@ Bruce, ALL,

Re : CA’s

> “and some of them are really sketchy:”

Only some?

Most western nations like America, Australia… etc have legislation “to compell” in one way or abother.

Others have placed staff in CA’s or by financial manipulation (RSA) have gained sympathetic help.

But mostly, due to the cut-throat nature of the business most CA’s have cut back not just security staff but security systems, thus they are in effectct a “push over” even for “script-kiddy” like attackers.

The real cause of the problem and why it’s so easy to get security credentials that are at best highly questionable is as I mention from time to time,

“Hierarchical Trust Systems”

In fact any and all Hierarchical poeer structures are by definition “corrupt”. Due to the way power gets vested in the very top of the pyramid and every human has “a price”, every system “a vulnerability”…

Yet we do not do research to get rid of hierarchies,

“Why?”

Are we complicitly corrupt?

Clive Robinson •
[November 10, 2022 10:42 AM](https://www.schneier.com/blog/archives/2022/11/an-untrustworthy-tls-certificate-in-browsers.html/#comment-412072)

@ Bruce, ALL,

Re : The dificulties.

> “Cory Doctorow does a great job explaining the context and the general security issues.”

Long story short, all information security is built out of a single foundation some call it a “Shared Secret” others call it a “Root of Trust”.

The primary requirment of a “Root of Trust” is not actually that it remains a “secret” but that it remains “unguessable” thus “unknown”. To see the distiction all Public Key Certificates contain as a minimum two “Roots of Trust” as Primary numbers that are multiplied together. It’s the “multiplication in a prime field” that –hopefully– keeps either Prime from becoming “known” to an attacker.

Thus the question of how to find “unguessable” numbers falls to what we chose to call “True Random Generators”(TRNG / TRBG) of numbers or individual bits[1].

You could call TRNG’s the fundemental problem of “information security” as that is effectively what they are.

This has been discused a few times over the years on this blog, one such was nearly a decade ago when similar PKcert issues arose,

<https://www.schneier.com/blog/archives/2013/09/new_nsa_leak_sh.html/#comment-204119>

From the discussion you can find earlier refrences to earlier discussions on TRNGs on this blog as they go back a near decade before that.

As far as I’m aware this was the first place on the Internet where open conversations on TRNGs their strengths, weaknesses and darn right failings happened so freely with so much exchange of information.

[1] To a computer all numbers are “integers” that may or may not have some structure. Such structure is generally described in “Abstract Data Types”, the base of which is a “bit” that then get aggregated into larger sets known informally as “bag of bits”.

Peter Pearson •
[November 10, 2022 12:55 PM](https://www.schneier.com/blog/archives/2022/11/an-untrustworthy-tls-certificate-in-browsers.html/#comment-412073)

So, can we finally get some attention on the need for users to vet their browsers’ root certificate databases? I understand that Google and Mozilla need to include the Elbonian Post Office’s root certificate in order to provide a smooth experience for their Elbonian users, but to the vast majority of users, that certificate is much more a threat than a blessing.

- •
[November 10, 2022 2:57 PM](https://www.schneier.com/blog/archives/2022/11/an-untrustworthy-tls-certificate-in-browsers.html/#comment-412076)

@Peter Pearson:

“So, can we finally get some attention on the need for users to vet their browsers’ root certificate databases?”

Maybe we should first get the browser developers to make it easy for ordinary users/people to do so, instead of needing a Doctorate in meta-gymnastics.

You would almost think that Apple’s Safari, Firefox, and Google’s Chrome developers have very much gone out of there way to make what should be a simple task difficult.

Makes you wonder why they would do that, and who gains by it, certainly not the ordinary users/people of the...