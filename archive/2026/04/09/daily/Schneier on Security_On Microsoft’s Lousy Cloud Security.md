---
title: On Microsoft’s Lousy Cloud Security
url: https://www.schneier.com/blog/archives/2026/04/on-microsofts-lousy-cloud-security.html
source: Schneier on Security
date: 2026-04-09
fetch_date: 2026-04-10T04:47:45.837777
---

# On Microsoft’s Lousy Cloud Security

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

## On Microsoft’s Lousy Cloud Security

ProPublica has a [scoop](https://arstechnica.com/information-technology/2026/03/federal-cyber-experts-called-microsofts-cloud-a-pile-of-shit-approved-it-anyway/):

> In late 2024, the federal government’s cybersecurity evaluators rendered a troubling verdict on one of Microsoft’s biggest cloud computing offerings.
>
> The tech giant’s “lack of proper detailed security documentation” left reviewers with a “lack of confidence in assessing the system’s overall security posture,” according to an internal government report reviewed by ProPublica.
>
> Or, as one member of the team put it: “The package is a pile of shit.”
>
> For years, reviewers said, Microsoft had tried and failed to fully explain how it protects sensitive information in the cloud as it hops from server to server across the digital terrain. Given that and other unknowns, government experts couldn’t vouch for the technology’s security.
>
> […]
>
> The federal government could be further exposed if it couldn’t verify the cybersecurity of Microsoft’s Government Community Cloud High, a suite of cloud-based services intended to safeguard some of the nation’s most sensitive information.
>
> Yet, in a highly unusual move that still reverberates across Washington, the Federal Risk and Authorization Management Program, or FedRAMP, authorized the product anyway, bestowing what amounts to the federal government’s cybersecurity seal of approval. FedRAMP’s ruling—which included a kind of “buyer beware” notice to any federal agency considering GCC High—helped Microsoft expand a government business empire worth billions of dollars.

Tags: [cloud computing](https://www.schneier.com/tag/cloud-computing/), [cybersecurity](https://www.schneier.com/tag/cybersecurity/), [Microsoft](https://www.schneier.com/tag/microsoft/), [national security policy](https://www.schneier.com/tag/national-security-policy/), [security theater](https://www.schneier.com/tag/security-theater/)

[Posted on April 9, 2026 at 6:51 AM](https://www.schneier.com/blog/archives/2026/04/on-microsofts-lousy-cloud-security.html) •
[7 Comments](https://www.schneier.com/blog/archives/2026/04/on-microsofts-lousy-cloud-security.html#comments)

### Comments

Clive Robinson •
[April 9, 2026 8:23 AM](https://www.schneier.com/blog/archives/2026/04/on-microsofts-lousy-cloud-security.html/#comment-453475)

@ Bruce, ALL,

As noted in the article,

> *The tech giant’s “lack of proper detailed security documentation” left reviewers with a “lack of confidence in assessing the system’s overall security posture,” according to an internal government report reviewed by ProPublica.*
>
> Or, as one member of the team put it: “The package is a pile of shit.”

Do others remember a few months back, a small company doing “lesser crimes” got the full “Go to Jail do not pass Go” treatment?

But “Big’old Micro$haft” just gets handed “mucho dineros” by the container load for their much worse crimes…

Talk about,

“It’s not What you know, but Who you know, to pay off, that counts”

Kind of tells you why the government wants to “nickel and dime” every last tax payer…

Gordon Shumway •
[April 9, 2026 9:22 AM](https://www.schneier.com/blog/archives/2026/04/on-microsofts-lousy-cloud-security.html/#comment-453476)

Bruce-

A minor typo: your text says ProPublica has the scoop, but the link goes to Ars Technica.

I think the ProPublica story you’re refering to is here:

It’s really sad to see how corrupt the process is, simultaneously compromising the spending of taxpayer dollars and the nation’s security is facepalm level incompetence.

Winter •
[April 9, 2026 10:39 AM](https://www.schneier.com/blog/archives/2026/04/on-microsofts-lousy-cloud-security.html/#comment-453477)

The GCC case is like every other “product” of MS. It was built by cobbling together every piece of program code they had.

Think the OOXML standard which is nothing but a serialized memory dump of MS word data structures. Even MS have no idea what’s really in there.

So MS ended up with linking up all network able applications into GCC. However, there was never any attempt to document anything. Encryption was used whenever they felt like it.

So when FedRAMP asked for a flow chart of encrypted information in GCC, there was no way MS could ever deliver that. They simply have no documentation of how and when information is encrypted.

This is no surprise. MS have always put products on the market the moment they could sell them, whatever the state of the product. Quality is just a loss.

Trevor •
[April 9, 2026 11:11 AM](https://www.schneier.com/blog/archives/2026/04/on-microsofts-lousy-cloud-security.html/#comment-453478)

It got pushed through approval because the government was desperate to have a second source over Amazon.

[mark](https://mrw.5-cent.us) •
[April 9, 2026 12:14 PM](https://www.schneier.com/blog/archives/2026/04/on-microsofts-lousy-cloud-security.html/#comment-453479)

I have several issues: first, was the approval in ’24, or ’25 (after the Idiot’s inauguration, and DOGE)?

Second, does this mean that they are not even following PCI-DSS rules, to have *all* communication between two computers encrypted?

I’ll also note that a few years ago, I think it was the UK who said “no, thanks” to cloud, because they could not be guaranteed that government data would remain solely on their country’s soil.

Winter •
[April 9, 2026 12:48 PM](https://www.schneier.com/blog/archives/2026/04/on-microsofts-lousy-cloud-security.html/#comment-453480)

While we are talking about MS Quality Assurance:

**Microsoft locks out VeraCrypt and WireGuard devs, blames verification process**
*No emails, no warnings, no humans – just bots, catch-22s, and a 60-day appeals queue*

<https://www.theregister.com/2026/04/09/microsoft_dev_account_deactivations/>

> Mounir Idrassi and Jason Donenfeld, the developers behind VeraCrypt and WireGuard respectively, both recently reported that Microsoft locked them out of their developer accounts for reasons unknown to them.
>
> Idrassi publicized his experience on March 30, saying: “Microsoft did not send me any emails or prior warnings. I have received no explanation for the termination and their message indicates that no appeal is possible.

Obviously, MS blame it on the victims:

*Microsoft claims WireGuard and Veracrypt account termination was merely due to not verifying an email: ‘Not everything is a conspiracy, sometimes it’s literally paperwork’*
<https://www.pcgamer.com/hardware/microsoft-claims-wireguard-and-veracrypt-account-termination-was-merely-due-to-not-verifying-an-email-not-everything-is-a-conspiracy-sometimes-its-literally-paperwork/>

> It seems like the catalyst for this problem came in the form of an account verification system for the Windows Hardware Program that began in October last year. With this, the partner would have to review and update legal information and...