---
title: Friday Squid Blogging: New Jurassic Squid Predecessors
url: https://www.schneier.com/blog/archives/2026/11/friday-squid-blogging-new-jurassic-squid-predecessors.html
source: Schneier on Security
date: 2026-11-06
fetch_date: 2026-11-07T08:02:00.578500
---

# Friday Squid Blogging: New Jurassic Squid Predecessors

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

## Friday Squid Blogging: New Jurassic Squid Predecessors

News story: “[Scientists discover a bizarre Jurassic ‘squid’ unlike anything ever seen](https://www.sciencedaily.com/releases/2026/10/261019093434.htm).”

> Scientists have identified the “fattest” belemnite ever discovered, a bizarre, barrel-shaped squid relative that lived in Wyoming’s ancient seas 160 million years ago. The exceptionally rare fossils reveal a creature unlike anything previously known, potentially a predator of smaller squid-like animals and a surprising survivor of a supposedly vanished family.

As usual, you can also use this squid post to talk about the security stories in the news that I haven’t covered.

[Blog moderation policy.](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

Tags: [squid](https://www.schneier.com/tag/squid/)

[Posted on November 6, 2026 at 5:05 PM](https://www.schneier.com/blog/archives/2026/11/friday-squid-blogging-new-jurassic-squid-predecessors.html) •
[2 Comments](https://www.schneier.com/blog/archives/2026/11/friday-squid-blogging-new-jurassic-squid-predecessors.html#comments)

### Comments

Clive Robinson •
[November 6, 2026 7:23 PM](https://www.schneier.com/blog/archives/2026/11/friday-squid-blogging-new-jurassic-squid-predecessors.html/#comment-459480)

@ Bruce, ALL,

**More Apple backdoor censorship?**

Apple was in effect the first mobile phone OS developer to put into their OS the foundations of “Client Side Scanning”(CSS) under increasing pressure from US legislators and law enforcement agencies.

Apple received a lot of bad press over it and slid some of it backwards.

Importantly though it emphasised the point that the US Gov had finally accepted the impossibility of NOBUS backdoors in “End to End Encryption”(E2EE) even though it had been repeatedly pointed out by those involved with ICTsec.

Thus the USG move to attack privacy on the other side of the “security end point” via CSS as an “end run attack”.

Something pointed out on this blog back in the very early days of “Secure Messaging Apps” and the weak links in the security chains on consumer and commercial systems.

Hence the argument for taking the “security end point” off the device that is the “communications end point” (and why I gave the basics of the design of how to build a “Deniable Encryption” system on this blog).

Well Apple have a new less obvious nod in the direction of “Client Side Censorship”(CSC).

Investigators have discovered quite deliberate censorship in the user side “autocomplete” text entry system,

> **Apple’s autocomplete restrictions include ‘Dictator Trump’ and ‘Sleepy Joe,’ researcher finds**
>
> Apple has an undisclosed multilingual gray list of tens of thousands of words and phrases that its iOS keyboard will ​not autocomplete or swipe-type, a researcher said on Friday.
>
> “*The list is not a ban. iPhone users can still type what they like when drafting emails and texts. But the words on the ‌list will not be suggested to users via autocomplete or swipe-typing in most cases. The researcher, Derik Kauffman, said the find opens a window into how Apple manages the tradeoff between anticipating what hundreds of millions of iPhone users are trying to say and preventing the devices from offering offensive or politically charged suggestions to users – something he said could quietly shape how they communicate.*
>
> “It’s a very light-touch form of censorship,” said Kauffman. “But at the scale that Apple is operating, it only takes a light touch to have a big impact.”“

<https://www.reuters.com/business/retail-consumer/apples-predictive-text-restrictions-include-dictator-trump-sleepy-joe-researcher-2026-11-06/>

Not only is it a first step “light-touch censorship” system, it also opens up fingerprinting users via their typing cadence and word / symantec usage.

[cybershow](https://cybershow.uk) •
[November 7, 2026 2:18 AM](https://www.schneier.com/blog/archives/2026/11/friday-squid-blogging-new-jurassic-squid-predecessors.html/#comment-459485)

@Clive
re: Apple auto-complete

Complexity is the tyrant’s friend

Apple’s actions remind us that anyone making at-scale technology for use by a
significant cohort has the opportunity to exercise subtle soft power and
influence. If fully in control of the system and channels, one can delay,
discard or distort messages, with plausible deniability. Though scientists
spent decades on communications and storage protocols to avoid or correct
integrity failure, we see strategic errors nefariously injected at the
application layer. These can always be blamed on illegible system behaviours
for which no human seems accountable. Indeed this is a ‘feature’ of complex and
opaque systems that serve power, and why simple and open systems are resisted.

Apple, with its closed, tightly integrated ecosystem is especially problematic
in this regard.

The “perfect” system for the soft censor or manipulator is a demonstrably
imperfect one. A fine example is Google’s elaborate and precarious mail
delivery system. Its ever-changing and proprietary interpretation of SPF, DKIM,
spam scores, and “user defined delivery options” makes it a seemingly
non-deterministic beast. However, it’s tedious but amusing to me which messages
– to certain people on certain subjects – are prone to mysterious delivery
problems whereas others are not. The fact that malfeasance is unfalsifiable
even in principle adds another ‘feature’ of gaslighting to the arsenal. One
always falls under the accusation/suspicion of paranoia, lack of understanding
or making spiteful claims. In such systems there is always a “rational
explanation”, albeit one that nobody can name or explain why an error happened
on that particular occasion.

It is not until investigative hackers fully reverse engineer and expose
the code of these systems that the truth gets out.

Things like LLMs and auto-complete serve to amplify this mischief because we’ve
accepted and internalised that Big Tech computer systems may misinterpret,
randomly delay, discard or alter our messages. We should help people understand
that one of the less well understood problems with all “AI” is that it is an
intervention. As interpreter/translator (transformers were developed for
mapping problems) it is a potentially defective agent.

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2026/11/friday-squid-blogging-new-jurassic-squid-predecessors.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2026/11/friday-squid-blogging-new-jurassic-squid-predecessors.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2026%2F11%2Ffriday-squid-b...