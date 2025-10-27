---
title: Short-Lived Certificates Coming to Let’s Encrypt
url: https://www.schneier.com/blog/archives/2024/12/short-lived-certificates-coming-to-lets-encrypt.html
source: Schneier on Security
date: 2024-12-17
fetch_date: 2025-10-06T19:44:55.623322
---

# Short-Lived Certificates Coming to Let’s Encrypt

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

## Short-Lived Certificates Coming to Let’s Encrypt

Starting [next year](https://letsencrypt.org/2024/12/11/eoy-letter-2024/):

> Our longstanding offering won’t fundamentally change next year, but we are going to introduce a new offering that’s a big shift from anything we’ve done before—short-lived certificates. Specifically, certificates with a lifetime of six days. This is a big upgrade for the security of the TLS ecosystem because it minimizes exposure time during a key compromise event.
>
> Because we’ve done so much to encourage automation over the past decade, most of our subscribers aren’t going to have to do much in order to switch to shorter lived certificates. We, on the other hand, are going to have to think about the possibility that we will need to issue 20x as many certificates as we do now. It’s not inconceivable that at some point in our next decade we may need to be prepared to issue 100,000,000 certificates per day.
>
> That sounds sort of nuts to me today, but issuing 5,000,000 certificates per day would have sounded crazy to me ten years ago.

This is an excellent idea.

Slashdot [thread](https://it.slashdot.org/story/24/12/15/0059216/lets-encrypt-announces-new-certificate-every-6-days-offering).

Tags: [certificates](https://www.schneier.com/tag/certificates/), [encryption](https://www.schneier.com/tag/encryption/)

[Posted on December 16, 2024 at 7:06 AM](https://www.schneier.com/blog/archives/2024/12/short-lived-certificates-coming-to-lets-encrypt.html) •
[20 Comments](https://www.schneier.com/blog/archives/2024/12/short-lived-certificates-coming-to-lets-encrypt.html#comments)

### Comments

[Impossibly Stupid](https://www.impossiblystupid.com) •
[December 16, 2024 11:58 AM](https://www.schneier.com/blog/archives/2024/12/short-lived-certificates-coming-to-lets-encrypt.html/#comment-442129)

I’m not saying it’s entirely a *bad* feature to support, but it’d be nice to hear what makes it “an excellent idea”. To me it smacks too much of mandating frequent password changes. What’s the actual use case/attack scenario that makes rapid-fire cert hopping a significant protection of my server traffic? Are key compromise events really some huge problem that I’ve simply been unaware of?

The 6 day target seems like a bad choice, too. Maybe it’s more flexible and you can schedule the refresh (at 90 days, it was never so pressing a deadline that I had to fuss with the timing), but I foresee *many* instances of issues that arise when an expiration/refresh falls on the weekends. I get that they probably want to spread the load out on their servers a bit, but we all still have human oversight over our security systems, and I wonder how this will play out when it meets the 5 day work week.

Dave •
[December 16, 2024 8:39 PM](https://www.schneier.com/blog/archives/2024/12/short-lived-certificates-coming-to-lets-encrypt.html/#comment-442131)

An excellent idea? At beast it’s rounding up twice the usual number of suspects, but in practice it’s more of a really dumb idea. What’s going to happen is that you’re going to get a new cert + key almost every time you visit any site, which will be brilliant for phishers because you can no longer rely on any past history of the cert or key for the site. They can stand up a new phishing site with a never-seen-before key and it’ll look like a Let’s-Encrypt business-as-usual cert.

Clive Robinson •
[December 17, 2024 10:52 AM](https://www.schneier.com/blog/archives/2024/12/short-lived-certificates-coming-to-lets-encrypt.html/#comment-442138)

@ ALL,

They say,

> *“This is a big upgrade for the security of the TLS ecosystem because it minimizes exposure time during a key compromise event.”*

But as a matter of note discussions about shortening certificate lifetimes for many years, and step by step we’ve gone down from a quarter century down to now only just a year plus a pause for breath.

It would have been less if certain people had had their way.

And in fact some want rid of the current Certificate Authority issue all together.

Because all to often what is called “key compromise events” is not the fault of the system owners of the system a certificate is used on. But others in or attacking the certificate supply chain or other software supply chains.

For various reasons encryption systems are brittle / fragile and unexpected things can lead to a chain of events where security is not just gone in part but in whole, and it may not be obvious as to how it happened.

The latest example of alleged “enhanced built in security” going wrong this way is probably BadRAM CVE-2024-21944. It’s against the memory AMD’s “Secure Encrypted Virtualization”(SEV), “Trusted Execution Environment”(TEE) uses,

<https://www.csoonline.com/article/3622917/amd-data-center-chips-vulnerable-to-revealing-data-through-badram-attack.html>

In short it allows relatively easy access by low cost hardware to memory (sort of old school “Front Panel Access”).

But that memory content should also be encrypted, so limiting or stoping access to the protected plaintext if “Key Managment”(KeyMan) is sufficient.

Unfortunately not, there is a long known issue with stored ciphertext (encrypted plaintext). Where you do not ever need access to the plaintext just the ciphertexts on either side of a change in plaintext.

Known as a “replay attack” if you have access at that level you simply write the old ciphertext over the new ciphertext, and what was new is now old again.

The example the researchers give is changing the “balance” in an account, such that an expenditure from an account is removed (Surprisingly you can get away with just changing balances inside a computer for a very long time see UK Post Office Horizon’s scandal of malicious prosecutions).

However it’s not just finance data where this is an issue. Other data such as “Key Material”(KeyMat) can also be overwritten with new replaced by old.

So reenabling access that has been removed…

Karl F. •
[December 17, 2024 11:40 AM](https://www.schneier.com/blog/archives/2024/12/short-lived-certificates-coming-to-lets-encrypt.html/#comment-442140)

I know you can have rolling certificates and announce already the next one, but this seems non-practical for especially e-mail servers. I could be mistaken though, just hoping we will never go to such short lifetimes as default. I have cert renawal automated of course, but 3 months give me more leisure in case a renewal job gets stuck. Looking forward to the future with many cert expired warnings.

[Mark](http://suspendedatom.com) •
[December 17, 2024 6:50 PM](https://www.schneier.com/blog/archives/2024/12/short-lived-certificates-coming-to-lets-encrypt.html/#comment-442154)

Wouldn’t this be made null if someone owned the server or was able to compromise the private cert than wouldn’t renewing often be pointless as they already have compromised the server. Especially if the admin has an a...