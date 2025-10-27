---
title: The Decoupling Principle
url: https://www.schneier.com/blog/archives/2022/12/the-decoupling-principle.html
source: Schneier on Security
date: 2022-12-08
fetch_date: 2025-10-04T00:55:29.076726
---

# The Decoupling Principle

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

## The Decoupling Principle

This is a [really interesting paper](https://conferences.sigcomm.org/hotnets/2022/papers/hotnets22_schmitt.pdf) that discusses what the authors call the Decoupling Principle:

> The idea is simple, yet previously not clearly articulated: to ensure privacy, information should be divided architecturally and institutionally such that each entity has only the information they need to perform their relevant function. Architectural decoupling entails splitting functionality for different fundamental actions in a system, such as decoupling authentication (proving who is allowed to use the network) from connectivity (establishing session state for communicating). Institutional decoupling entails splitting what information remains between non-colluding entities, such as distinct companies or network operators, or between a user and network peers. This decoupling makes service providers individually breach-proof, as they each have little or no sensitive data that can be lost to hackers. Put simply, the Decoupling Principle suggests always separating who you are from what you do.

Lots of interesting details in the paper.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [anonymity](https://www.schneier.com/tag/anonymity/), [authentication](https://www.schneier.com/tag/authentication/), [privacy](https://www.schneier.com/tag/privacy/), [pseudonymity](https://www.schneier.com/tag/pseudonymity/)

[Posted on December 7, 2022 at 7:04 AM](https://www.schneier.com/blog/archives/2022/12/the-decoupling-principle.html) •
[25 Comments](https://www.schneier.com/blog/archives/2022/12/the-decoupling-principle.html#comments)

### Comments

loco •
[December 7, 2022 7:48 AM](https://www.schneier.com/blog/archives/2022/12/the-decoupling-principle.html/#comment-413491)

This principle has been “invented” in the 1970s in the debate on data protection in Germany, where it was coined “informationelle Gewaltenteilung” – “informational separation of powers”. It was never fully elaborated beyond the legal sphere, and there it was related primarily to data decoupling and institutional decoupling, rather than technical or architectural decoupling. However, it is related to the protection goal of “unlinkability” that has become widespread in the European debate in recent years.

YF •
[December 7, 2022 8:05 AM](https://www.schneier.com/blog/archives/2022/12/the-decoupling-principle.html/#comment-413492)

In European union they want security in a way it can be unsecured on bureaucrat’s demand for security purposes.

Winter •
[December 7, 2022 8:31 AM](https://www.schneier.com/blog/archives/2022/12/the-decoupling-principle.html/#comment-413495)

This is just an elaboration of the data-minimization requirements in the GDPR. No institution should collect or store data it does not need. Also, data storage should have privacy protection built-in.

Without having had time to read the article, I see this as implementing the GDPR provisions.

Jordan Sherb •
[December 7, 2022 9:08 AM](https://www.schneier.com/blog/archives/2022/12/the-decoupling-principle.html/#comment-413496)

I think it’s synonymous with the concept of “separation of concerns”.

Robin •
[December 7, 2022 9:15 AM](https://www.schneier.com/blog/archives/2022/12/the-decoupling-principle.html/#comment-413497)

@Winter: I wish the GDPR data-minimization requirements were more widely known and respected. It seems to be increasingly the case that even trivial transactions demand unnecessary information.

This morning I bought tickets for a local concert on Friday. A couple of guys in a room not much bigger than my sitting room; 6.50€ per seat so you can see it’s hardly Bruce Springsteen at Olympia. But to do that I had to create an account and to do that it wanted name, DoB, phone number, about 20 opt-in/opt-out choices for newsletters etc, email address and the names of both people who are going to attend. None of this was optional and since they claim that ID will be checked at the door, false names seem to be a no-no. They didn’t get a true DoB though; a tiny victory.

Identical process to buy tickets for an exhibition last week, except there were no options to reject being subscribed during the signing-up. At least there was an option to unsubscribe from publicity in the first email newsletter that arrived but they had already collected more information than I wanted them to have.

If challenged I’m sure they could come up with reasons why they want to offer a “better experience” (pah) but necessary? No. And this happens *all the time*.

/rant

Winter •
[December 7, 2022 9:58 AM](https://www.schneier.com/blog/archives/2022/12/the-decoupling-principle.html/#comment-413498)

@Robin

> But to do that I had to create an account and to do that it wanted name, DoB, phone number, about 20 opt-in/opt-out choices for newsletters etc, email address and the names of both people who are going to attend.

Sounds indeed excessive. I am afraid that unless there are laws against it, the only option is to vote with your feet/wallet.

Robin •
[December 7, 2022 10:12 AM](https://www.schneier.com/blog/archives/2022/12/the-decoupling-principle.html/#comment-413501)

@Winter I am pretty sure that their site contravenes the GDPR but I hold out little hope of being able to get this through to the bureaucracy in the town hall. Having just downloaded the tickets the little bit of rancid cream on the cake is that they insist the two tickets (with their QR codes) are each printed on a sheet of white A4 paper.

But you’re right – I’ll try to avoid them in future.

Clive Robinson •
[December 7, 2022 11:29 AM](https://www.schneier.com/blog/archives/2022/12/the-decoupling-principle.html/#comment-413505)

@ Bruce,

This is an old principle practiced in governments to stop power building up in any one part of Government thus creating a threat.

It was unfortunately the work of IBM that enabled some governments to invert this idea.

With the use of “card tabulators” they could take census and similar data and “audit out” certain information quite rapidly with very few involved.

The results of the inversion of this idea in Europe from the early 1930’s onwards turned out to be quite horrific.

Clive Robinson •
[December 7, 2022 11:33 AM](https://www.schneier.com/blog/archives/2022/12/the-decoupling-principle.html/#comment-413506)

@ YF,

Long time no hear, I trust you are well?

Sofakinbd •
[December 7, 2022 12:47 PM](https://www.schneier.com/blog/archives/2022/12/the-decoupling-principle.html/#comment-413509)

Isn’t this the basis of [Apple’s Private Relay?](https://support.apple.com/en-us/HT212614)

> How Private Relay works
>
> Normally when you browse the web, information contained in your web traffic, such as your DNS records and IP address, can be seen by your network provider and the websites you visit. This information could be used to determine your...