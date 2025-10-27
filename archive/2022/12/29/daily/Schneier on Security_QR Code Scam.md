---
title: QR Code Scam
url: https://www.schneier.com/blog/archives/2022/12/qr-code-scam.html
source: Schneier on Security
date: 2022-12-29
fetch_date: 2025-10-04T02:41:42.319933
---

# QR Code Scam

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

## QR Code Scam

An enterprising individual made [fake parking tickets](https://www.autoblog.com/2022/12/27/santa-cruz-fake-parking-tickets/) with a QR code for easy payment.

Tags: [forgery](https://www.schneier.com/tag/forgery/), [QR codes](https://www.schneier.com/tag/qr-codes/), [scams](https://www.schneier.com/tag/scams/)

[Posted on December 28, 2022 at 1:14 PM](https://www.schneier.com/blog/archives/2022/12/qr-code-scam.html) •
[27 Comments](https://www.schneier.com/blog/archives/2022/12/qr-code-scam.html#comments)

### Comments

Peterpotamux •
[December 28, 2022 1:43 PM](https://www.schneier.com/blog/archives/2022/12/qr-code-scam.html/#comment-414664)

I know this happened in a couple of towns in Spain some months ago. Bad guys created sticks they placed in parking totems. The QR codes directed to a fake municipality site to buy parking minutes. Bad guys recovered small payments but most important card details.

Most of people is used to QR codes (widely used during COVID crisis) and has a natural tendency to scan any code they see (for some people is as unavoidable as not not pushing that button under the “do not push this button” sentence).

QR code scanners shall double-check reputation of the URLs in a DB before accessing?

[JMM](https://rinzewind.org) •
[December 28, 2022 1:55 PM](https://www.schneier.com/blog/archives/2022/12/qr-code-scam.html/#comment-414665)

As Peterpotamux commented, here’s a new article (in Spanish) that describes the same scam in Spain a few weeks ago: <https://motor.elpais.com/actualidad/multas-de-trafico-falsas-una-campana-de-fraude-hecha-con-fotocopias/>

Brenden Walker •
[December 28, 2022 2:16 PM](https://www.schneier.com/blog/archives/2022/12/qr-code-scam.html/#comment-414666)

I don’t even have a QR code scanner on anything. Never understood the need. If the QR code doesn’t also have the website URL in text, I’m not going there.

People are way too quick to give up security for convenience IMO.

Michael •
[December 28, 2022 3:11 PM](https://www.schneier.com/blog/archives/2022/12/qr-code-scam.html/#comment-414667)

So if the perpretrator had instead written an account number to which to pay, would this have been a “digits” scam instead?

Seriously. How is the fact that it was done via a QR code *the* defining characteristic of the scam?

Dan Hugo •
[December 28, 2022 4:03 PM](https://www.schneier.com/blog/archives/2022/12/qr-code-scam.html/#comment-414669)

The comment from Brendan is interesting, as many people I encounter are suspicious of and thus avoid using QR codes entirely, though inclusion of the URL text doesn’t really help. We have QR-enabled parking spots to enable paying the parking fees (here in Vegas, those are like water, except available in larger quantities), where the code is printed on a sign at or near a particular parking space.

To me, this seems like a client software issue with a user education component. Rather than enabling direct click-through when a URL QR Code is scanned (in your modern mobile camera app on your mobile device, for example), perhaps an intermediate local landing with the full URL displayed and the possibility of online checks (Peterpotamax)and the possibility of follow-up for problematic codes (a crowd-sourced knowledge base, for criminal as well as regular old problematic QR codes).

Clive Robinson •
[December 28, 2022 4:31 PM](https://www.schneier.com/blog/archives/2022/12/qr-code-scam.html/#comment-414670)

@ ALL,

I’M assuming this is the same story,

<https://lookout.co/santacruz/news/story/2022-12-23/santa-cruz-police-fradulent-tickets>

But without the yahoo scamers behind it.

I’ve looked at several stories and they all appear to be the same.

Interestingly the Police say the 19year old admited putting the fake notices on the cars, BUT claims not to have received any money.

Hence his being charged with,

1, Unlawful use of a computer system.

The only picture I found of the fake tickets did not have a QR code visable on them, yet the real ticket shown does…

Something tells me there is a little more behind this story than we are being told.

Antwan •
[December 28, 2022 4:44 PM](https://www.schneier.com/blog/archives/2022/12/qr-code-scam.html/#comment-414671)

> Seriously. How is the fact that it was done via a QR code the defining characteristic of the scam?

If the ticket listed a “wrong” phone number, we might be calling it a “phone number scam”. If it had a “shortened” URL, we might call it a URL shortener scam. People trust things they shouldn’t, and the details of this social engineering are interesting to Bruce’s readers. Part of the problem is that the people designing these systems don’t think about trustworthiness, leaving little way to distinguish fake fom real. We’d likely be screwed if the scammers got paper with holograms, or paid for an actual metre(s)-wide “city parking” steel sign and mounted it while wearing reflective vests (à la [Richard Ankrom](https://thelandmag.com/richard-ankrom-guerrilla-public-service-los-angeles-free/)).

I once spent 30 minutes on the phone with my bank after encountering a “verified by Visa” prompt asking for my date of birth, to determine whether it was real. It was an SSL-protected iframe with a domain and cert referencing some company I’d never heard of. “Does it have the Visa logo?” was suggested by the first bank employee as a way of determining legitimacy; I asked to speak to someone else, of course, and eventually got a series of SSL-protected links from the bank’s site to that site (run by an apparently legitimate contractor). I got the impression it was uncommon for anyone to ask about it.

lurket •
[December 28, 2022 5:47 PM](https://www.schneier.com/blog/archives/2022/12/qr-code-scam.html/#comment-414674)

I’m with @Clive on this one: the various versions of this I’ve found show a “fake” ticket that has no QR code. AFAICT it doesn’t seem to be folded to conceal the code. Hmmm …

As for using a phone or bank acct number, it might still fool most of the public. Readers of this blog might notice something odd/different in a phone nr. that’s frequently used, but how many could tell at a glance that a QR code was not the same as last week?

My behaviour is not typical, but for non-human-readable data, curiosity overcomes convenience. I have a bar/QR code reader which just reads, no network connection (I trust), and just shows the url/phone/serial/part Nr. on screen, from where it can be copied and pasted into a browser/dialler/whatever.

Clive Robinson •
[December 28, 2022 6:21 PM](https://www.schneier.com/blog/archives/2022/12/qr-code-scam.html/#comment-414677)

If you search on the 19 year olds details given in various articles, you end up being told that he is “hispanic” and officially what he’s been (or was being) held on is,

1, 532(A) – Obtaining Food Or Property By False Pretenses.

2, 502C1A – Deleting/Altering Data to Commit Fraud.

The ...