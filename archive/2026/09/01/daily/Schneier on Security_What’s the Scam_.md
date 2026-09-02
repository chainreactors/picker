---
title: What’s the Scam?
url: https://www.schneier.com/blog/archives/2026/09/whats-the-scam.html
source: Schneier on Security
date: 2026-09-01
fetch_date: 2026-09-02T06:41:42.013104
---

# What’s the Scam?

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

## What’s the Scam?

To subscribe to my monthly email newsletter, you have to enter your information on the webpage, and then reply to an automatically generated email. This is, of course, to prevent people from subscribing addresses other than their own.

Starting last weekend, I have been receiving a lot of individual responses to those emails. Always one line:

> Thank you for the positive impact your emails have had on my life.
> Your emails are a game-changer.
> Your emails are a constant reminder of why I subscribed.
> Your emails rock.
> Thank you for the time and effort you put into creating these informative emails.
> Thank you for the passion and enthusiasm you infuse into your email content.
> Your emails consistently exceed my expectations. Thank you for the exceptional value!

I responded to the first few, because sometimes I do get these nice emails from readers and I hadn’t yet realized it was all fake. But so many, and all at once—this is obviously AI. And obviously a scam, except I can’t figure out what the scam is.

The addresses are things like:

> jnnvcddghjgfdryhj67@gmail.com
> nbhgdfhjedty896565@gmail.com
> jesikawells6873@gmail.com
> niffelatopserean92@gmail.com
> reinareyes983@gmail.com
> htfhtfhhjkgth@gmail.com

All Gmail. None of the addresses has actually subscribed to Crypto-Gram. They could; whoever is sending the emails could easily have confirmed the subscription.

My first thought was pig butchering—wanting me to respond and turn this into a conversation—but no one has responded to any of my responses. Anyone have any idea?

Tags: [scams](https://www.schneier.com/tag/scams/)

[Posted on September 1, 2026 at 1:36 PM](https://www.schneier.com/blog/archives/2026/09/whats-the-scam.html) •
[27 Comments](https://www.schneier.com/blog/archives/2026/09/whats-the-scam.html#comments)

### Comments

Alan •
[September 1, 2026 1:46 PM](https://www.schneier.com/blog/archives/2026/09/whats-the-scam.html/#comment-457376)

My thought is Pig Butchering but:
(a) you don’t respond fast enough (by the time you respond, the email address has already been suspended), or
(b) it’s just not working right, or they’re still trying to get it going.

M •
[September 1, 2026 1:56 PM](https://www.schneier.com/blog/archives/2026/09/whats-the-scam.html/#comment-457377)

To make Google’s fraud detection think that these accounts are not going to be used for nefarious purposes.
So aging them and having “genuine” conversations, with real human operated addresses is probably helpful.
Getting you to respond is probably even better and it seem to have worked.
Probably doing that with various people, before it’s time for business.

Bruce •
[September 1, 2026 2:16 PM](https://www.schneier.com/blog/archives/2026/09/whats-the-scam.html/#comment-457378)

Unless SPF, DMARC, DKIM etc pass muster, the From header is probably garbage. The sender can put whatever they want (probably email addresses taken from a dump of compromised accounts.)

Stu •
[September 1, 2026 2:27 PM](https://www.schneier.com/blog/archives/2026/09/whats-the-scam.html/#comment-457379)

Came here to say something to “M” above…my guess is this is the modern equivalent of “laundering” email addresses…exercizing them enough that they are old/trusted/used enough that they pass various fraud detection methodologies.

Pau Amma •
[September 1, 2026 3:15 PM](https://www.schneier.com/blog/archives/2026/09/whats-the-scam.html/#comment-457382)

Another possibility: someone is weeding an email address list that your newsletter’s sender address is in. So checking whether that address accepts emails and and how quickly someone replies to emails.

Yossarian •
[September 1, 2026 3:21 PM](https://www.schneier.com/blog/archives/2026/09/whats-the-scam.html/#comment-457383)

Interesting puzzle!
Along the lines of how they might benefit, M makes a good point that maybe it helps legitimize their email address.

What else might they learn from your mail?
The sending machine’s (or its gateway’s) public IP address is in the headers (at least with my ISP), and that seems potentially interesting. With enough email, they might learn when you are awake. If a sender isn’t using a VPN to mask this address, then they could learn something interesting from the geo-location data associated with the IP address.

I suppose they could also be interested in your “personal” email address in case that’s different than what’s on your contact page.

Given that LLMs are trained on bootlegged human-made content, maybe they don’t know have a “good reason” for what they are doing and don’t have any ulterior “motive.” Or as Alan said “they’re still trying to get it [the scamming] going.”

N.Critser •
[September 1, 2026 3:24 PM](https://www.schneier.com/blog/archives/2026/09/whats-the-scam.html/#comment-457384)

It could be information for a phishing outfit targeting computer folk. They could scrape all the visible pieces and use that as their initial phish email. Surely someone would bite.

Or the wordpress stack you use is the target and you just happen to be a site that is running that stack. So they are getting intel by they request process.

anonymouse random •
[September 1, 2026 3:42 PM](https://www.schneier.com/blog/archives/2026/09/whats-the-scam.html/#comment-457385)

I guess it’s AI agents doing whatever they do. It’s not necessarily a scam.

Evgeny •
[September 1, 2026 3:51 PM](https://www.schneier.com/blog/archives/2026/09/whats-the-scam.html/#comment-457386)

Most likely warming up spam accounts to make them look sufficiently innocent.

[Alan Fleming](https://alanfleming.org) •
[September 1, 2026 4:19 PM](https://www.schneier.com/blog/archives/2026/09/whats-the-scam.html/#comment-457387)

I’d agree that there’s a good chance this is AI scraping. There is benefit to being able to acquire data that gives a model advantage, and data not available to generalised scraping is exactly that.

David Platt Sanford •
[September 1, 2026 4:48 PM](https://www.schneier.com/blog/archives/2026/09/whats-the-scam.html/#comment-457388)

Quoting and then elaborating on what anonymous random said, “I guess it’s AI agents doing whatever they do. It’s not necessarily a scam.” This could be AIs assigned a security-related task, reading your posts and thanking you via the most readily available email address? I’m guessing we’ll see a lot of activity similar to the more egregious rogue hacking AIs, but with less problematic actions and outcomes.

Clive Robinson •
[September 1, 2026 5:37 PM](https://www.schneier.com/blog/archives/2026/09/whats-the-scam.html/#comment-457389)

@ Bruce, ALL,

The first question to answer is,

1, Does there have to be a reason?

And if you can think of one the next question is,

2, Does it effect me?
3, How?
4, What actions to take.

The problem with the first question is it’s a “random rabbit hole” with a near infinite warren behind it.

Thus you need to find a way to ...