---
title: Everything You Need to Know About Email Encryption in 2026
url: https://soatok.blog/2026/01/04/everything-you-need-to-know-about-email-encryption-in-2026/
source: Dhole Moments
date: 2026-01-04
fetch_date: 2026-01-05T03:51:36.673225
---

# Everything You Need to Know About Email Encryption in 2026

[Skip to the content](#site-content)

Search

[Dhole Moments](https://soatok.blog/)

Software, Security, Cryptography, and Furries

Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Search

Search for:

Close search

Close Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Categories

[Open Source](https://soatok.blog/category/technology/open-source/) [Software Security](https://soatok.blog/category/technology/software-security/)

# Everything You Need to Know About Email Encryption in 2026

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [January 4, 2026](https://soatok.blog/2026/01/04/everything-you-need-to-know-about-email-encryption-in-2026/)

![Everything You Need to Know About Email Encryption in 2026](https://i0.wp.com/soatok.blog/wp-content/uploads/2026/01/BlogHeader-2026-Encrypted-Email.png?fit=1200%2C675&ssl=1)

If you think about emails as if they’re anything but the digital equivalent of a postcard–that is to say, they provide **zero confidentiality**–then someone lied to you and I’m sorry you had to find out from a furry blog that sometimes talks about applied cryptography.

![Sad Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/03/soatoktelegramswave3-04.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

At the end of 2025, at the 39th Chaos Communications Congress in Hamburg, Germany, a team of security researchers posted some devastating vulnerabilities in PGP software (with a focus on GnuPG), and published them at [gpg.fail](https://gpg.fail).

> Note: They also discussed a minisign vulnerability and another attacking age’s plugin system, but these were much less severe than some of the GnuPG vulns.

This disclosure reignited message board debates about GnuPG, OpenPGP, and related topics. I’m not going to reiterate [the many problems with PGP](https://www.latacora.com/blog/2019/07/16/the-pgp-problem/) or [what you should use instead](https://soatok.blog/2024/11/15/what-to-use-instead-of-pgp/).

Instead, I want to explain why cryptographers and security engineers that work on cryptography have largely abandoned any efforts to make “encrypted email” happen.

## Why People Want to Encrypt Email

Email is not simple. Even before you get into protocol discussions, email is actually several things bundled into one software package:

* The most basic mental model for email is an asynchronous “store-and-forward” message sent from you to other parties.
  + Not to mention the notion of `Cc:` and `Bcc:` fields.
* Email addresses are an identity anchor for most of the Internet.
  + Forgot your password? Don’t worry, we’ll just… send you an email. Wow.
* Mailing lists allow members of a group to send an email once and have everyone else receive an identical copy.

The way society uses email (at least in the United States, anyway) has conditioned everyone to treat email as more reliable than it actually is.

So it’s really no wonder that email is how most medical, legal, and financial workers operate in their day-to-day (assuming they aren’t using certified mail or fax machines).

But then the security nerds point out that:

* SMTP, the protocol for sending email, rarely enforces TLS (if it’s even supported at all)
* STARTLS, an opportunistic attempt to increase TLS usage for email protocols, is trivially stripped by active attackers
* Emails are not end-to-end encrypted between inboxes

…it’s tempting to rush to PGP or S/MIME to reclaim a bit of privacy for your communications.

> If that doesn’t make you feel all warm and fuzzy, remember that many industries still use FTP to transfer encrypted ZIP files back and forth in 2026.

Then, when even more security nerds point out how bad PGP and S/MIME are ([EFAIL](https://efail.de/), [gpg.fail](https://gpg.fail), [Why Johnny Can’t Encrypt](https://people.eecs.berkeley.edu/~tygar/papers/Why_Johnny_Cant_Encrypt/OReilly.pdf), etc.), everyone gets frustrated.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/07/neophyte-confused.png?resize=409%2C512&ssl=1)

[Harubaki](https://harubaki.carrd.co/)

## How Email Encryption Fails

Let’s set aside all the security vulnerabilities for a moment and explore an extremely common failure mode.

Suppose you send some of your friends an encrypted email.

First, your friends need to have their own private/public key pairs and exchange public keys with each other.

In PGP land, this sometimes meant setting up a “key signing party” to attest to each other’s identities, so that others could see these vouches from the “Web of Trust”. (This was [a really big *thing*](https://en.wikipedia.org/wiki/CryptoParty) right after the Snowden leaks.)

But for simplicity, let’s ignore PGP entirely.

Let’s say you do all this, and successfully begin sending encrypted emails. Hooray!

How long until one of them, in a hurry, hits “Reply All” without encrypting first?

![Soatok thinking sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2025/11/SoatokTelegrams2020-12.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

This exact kind of failure happens all the time with encrypted email solutions.

And since email responses, by default, quote the thing they’re replying to, this kind of mistake can leak *the entire message chain* leading up to the mistake too.

One of the main reasons I recommend Signal is because **there is [no plaintext mode](https://soatok.blog/2024/07/31/what-does-it-mean-to-be-a-signal-competitor/)** to accidentally use.

#### But you can forward/screenshot Signal…

Sure, you can **go out of your way** to bypass the encryption if you want to. No one disputes that.

But what you cannot do with Signal is **accidentally emit plaintext to the Internet by using the Reply feature**.

With encrypted emails, the “accidentally disclose a bunch of plaintext” footgun is in the hot path of the user experience.

These are *very* different propositions of misuse and anyone that conflates them is being dishonest because they want to mislead you.

![NO sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/08/soatoktelegrams2020-04.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

### It Gets Worse, Of Course

One of the limitations of encrypting the message body of emails is that there is still a ton of metadata that gets transmitted in the clear (i.e., often without even transport-layer encryption).

If nothing else, a passive adversary learns the following:

* The `To:` and `Cc:` fields (and, practically, always the `Bcc:` field)
* The subject line for the email
* Timestamps
* Attachment metadata (file names, types)
* DKIM signatures (more on that in a minute)
* IP addresses (this one is included for completeness, since people forget about it)

But the subject line is the most critical. Users and software alike use the subject line to file replies into neat “threads”.

Unfortunately, knowing the subject line and which person replied to whom at what point in time can tell you **a lot** even if you can’t read the message contents.

So now you’re forced to choose between perfect operational security discipline 100% of the time and using software in a totally normal way.

#### But that’s just metadata!

[Nation-state spy agencies use metadata](https://abcnews.go.com/blogs/headlines/2014/05/ex-nsa-chief-we-kill-people-based-on-metadata) to decide who to kill.

If you care about privacy, you should never send this kind of extremely sensitive metadata in the clear.

Even if you take nation states off the table, private intelligence companies like Palantir and their international competitors are almost certainly up to no good.

![Disgusted Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/09/soatoktelegrams2020-14.png?resize=512%2C512&ssl=1)

[...