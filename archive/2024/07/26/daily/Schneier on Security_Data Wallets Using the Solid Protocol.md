---
title: Data Wallets Using the Solid Protocol
url: https://www.schneier.com/blog/archives/2024/07/data-wallets-using-the-solid-protocol.html
source: Schneier on Security
date: 2024-07-26
fetch_date: 2025-10-06T17:45:04.282558
---

# Data Wallets Using the Solid Protocol

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

## Data Wallets Using the Solid Protocol

I am the Chief of Security Architecture at [Inrupt, Inc.](https://www.inrupt.com/), the company that is commercializing Tim Berners-Lee’s [Solid](https://solidproject.org/) open W3C standard for distributed data ownership. This week, we [announced](https://www.inrupt.com/blog/data-wallet-release) a digital wallet based on the Solid architecture.

Details are [here](https://www.inrupt.com/release/data-wallet), but basically a digital wallet is a repository for personal data and documents. Right now, there are hundreds of different wallets, but no standard. We think designing a wallet around Solid makes sense for lots of reasons. A wallet is more than a data store—data in wallets is for using and sharing. That requires interoperability, which is what you get from an open standard. It also requires fine-grained permissions and robust security, and that’s what the Solid protocols provide.

I think of Solid as a set of protocols for decoupling applications, data, and security. That’s the sort of thing that will make digital wallets work.

Tags: [data privacy](https://www.schneier.com/tag/data-privacy/), [data protection](https://www.schneier.com/tag/data-protection/), [Inrupt](https://www.schneier.com/tag/inrupt/), [security standards](https://www.schneier.com/tag/security-standards/)

[Posted on July 25, 2024 at 7:05 AM](https://www.schneier.com/blog/archives/2024/07/data-wallets-using-the-solid-protocol.html) •
[13 Comments](https://www.schneier.com/blog/archives/2024/07/data-wallets-using-the-solid-protocol.html#comments)

### Comments

finagle •
[July 25, 2024 7:42 AM](https://www.schneier.com/blog/archives/2024/07/data-wallets-using-the-solid-protocol.html/#comment-439565)

Can you link to the specification please. After 10 minutes of surfing around the Solid site linked, and following links from there down various rabbit holes, I can’t find a link to the actual ‘open’ standard.

Winter •
[July 25, 2024 9:24 AM](https://www.schneier.com/blog/archives/2024/07/data-wallets-using-the-solid-protocol.html/#comment-439567)

> A wallet is more than a data store—data in wallets is for using and sharing. That requires interoperability, which is what you get from an open standard. It also requires fine-grained permissions and robust security, and that’s what the Solid protocols provide.

One really important use case for data wallets would be medical data.

Many countries are struggling with electronic patient/health records. Privacy and Security concerns have shot down many projects. This can lead to bizarre situations where a patient is given a paper file with printouts of their health records from their hospital when they transfer to another hospital (image data on CD/DVD, this actually happens in the Netherlands).

The core difficulty here is that medical data must be accessible in emergency situations when the patient is incapacitated.

This is also a concern with other data wallets which have to be accessible when the owner dies or is otherwise incapacitated for longer times. It is one thing to get to a bank to release accounts of a deceased relative, another to retrieve important data, eg, passwords or account info, for which there is no alternative route.

I would like to know how the current standards treat this case. I could not find this information in the link nor on the Solid web site (there is no search function).

Bruce Schneier •
[July 25, 2024 9:28 AM](https://www.schneier.com/blog/archives/2024/07/data-wallets-using-the-solid-protocol.html/#comment-439568)

@finagle:

Weird. I typed “Solid specification” into Google, and it was the first hit:

<https://solidproject.org/specification>

And totally not vaporware. It’s a W3C standard. It’s been working for years.

Morley •
[July 25, 2024 12:05 PM](https://www.schneier.com/blog/archives/2024/07/data-wallets-using-the-solid-protocol.html/#comment-439572)

I hope it ends up easy to use for end users. Maybe an implementation certification program is in order for security and usability.

Melissa •
[July 25, 2024 12:20 PM](https://www.schneier.com/blog/archives/2024/07/data-wallets-using-the-solid-protocol.html/#comment-439573)

Inrupt is really a weird and paranoid company, it blocks TOR.
So much of the privacy, openness and security.
If you spit on user’s anonymity, why should I care about your products?

Espen •
[July 25, 2024 4:31 PM](https://www.schneier.com/blog/archives/2024/07/data-wallets-using-the-solid-protocol.html/#comment-439580)

I have been following the EU Digital Identity (DI) work for the last couple of years, and with the regulations landing this February it will go into effect early 2026.

The technical specification can be found at <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/>.

It sounds like Solid could help deliver some of the things the EU ID Wallet is trying to achieve, but I have not seen any mention of Solid in the work from EU.

I have not looked at the details but the W3C WebID used by Solid and the W3C Decentralized Identifiers (DIDs) being proposed by EU DI wallet might be trying to do the same thing.

I understand Solid is trying to achieve more than just identification and verifiable credentials, but it would be interesting if these standards would cooperate in some way.

ResearcherZero •
[July 26, 2024 5:04 AM](https://www.schneier.com/blog/archives/2024/07/data-wallets-using-the-solid-protocol.html/#comment-439599)

@Melissa

Many companies and sites block TOR.

VPNs also help route around faults. If TOR is blocked, try a VPN with another browser.
Privacy with more resilient network access helps to avoid upstream exchange failures.

Matt •
[July 26, 2024 11:29 AM](https://www.schneier.com/blog/archives/2024/07/data-wallets-using-the-solid-protocol.html/#comment-439613)

“Weird. I typed “Solid specification” into Google, and it was the first hit:”

Yeah, but the site itself doesn’t appear link to the specification anywhere. Is there some reason it’s okay to not have a link to the spec *on the site itself*?

Richard •
[July 26, 2024 5:08 PM](https://www.schneier.com/blog/archives/2024/07/data-wallets-using-the-solid-protocol.html/#comment-439621)

I’ve been excited about the Solid project since its inception. It overlaps a lot with the Decentralized Identity Foundation’s Decentralized Web Nodes project that has been sponsored by Block TBD and Microsoft. Do you have plans to interoperate?

<https://github.com/decentralized-identity/decentralized-web-node>

Peter •
[July 26, 2024 5:22 PM](https://www.schneier.com/blog/archives/2024/07/data-wallets-using-the-solid-protocol.html/#comment-439622)

“Web 3.0 is all about empowered individuals and personal data.”

In the Sixth World, Web 3.0 is the first version of the Matrix.

Clive Robinson •
[July 27, 2024 7:26 AM](https://www.schneier.com/blog/archives/2024/07/data-wallets-...