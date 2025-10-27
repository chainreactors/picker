---
title: Apple Patches iPhone Zero-Day
url: https://www.schneier.com/blog/archives/2022/12/apple-patches-iphone-zero-day.html
source: Schneier on Security
date: 2022-12-17
fetch_date: 2025-10-04T01:50:34.036632
---

# Apple Patches iPhone Zero-Day

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

## Apple Patches iPhone Zero-Day

The most recent iPhone update—to version 16.2—patches a zero-day vulnerability [that](https://support.apple.com/en-us/HT213516) “may have been actively exploited against versions of iOS released before iOS 15.1.”

[News](https://techcrunch.com/2022/12/13/apple-zero-day-webkit-iphone/):

> Apple said security researchers at Google’s Threat Analysis Group, which investigates nation state-backed spyware, hacking and cyberattacks, discovered and reported the WebKit bug.
>
> WebKit bugs are often exploited when a person visits a malicious domain in their browser (or via the in-app browser). It’s not uncommon for bad actors to find vulnerabilities that target WebKit as a way to break into the device’s operating system and the user’s private data. WebKit bugs can be “chained” to other vulnerabilities to break through multiple layers of a device’s defenses.

Tags: [Apple](https://www.schneier.com/tag/apple/), [iOS](https://www.schneier.com/tag/ios/), [iPhone](https://www.schneier.com/tag/iphone/), [patching](https://www.schneier.com/tag/patching/), [zero-day](https://www.schneier.com/tag/zero-day/)

[Posted on December 16, 2022 at 7:04 AM](https://www.schneier.com/blog/archives/2022/12/apple-patches-iphone-zero-day.html) •
[15 Comments](https://www.schneier.com/blog/archives/2022/12/apple-patches-iphone-zero-day.html#comments)

### Comments

J Bull •
[December 16, 2022 8:18 AM](https://www.schneier.com/blog/archives/2022/12/apple-patches-iphone-zero-day.html/#comment-414079)

The most recent update is to 16.2.

Clive Robinson •
[December 16, 2022 8:44 AM](https://www.schneier.com/blog/archives/2022/12/apple-patches-iphone-zero-day.html/#comment-414081)

@ ALL

Re : WebKit is elsewhere.

Seeing in the snipit,

> *“discovered and reported the **WebKit** bug”*

Makes me wonder what else is going to need an emergancy patch,

<https://en.m.wikipedia.org/wiki/WebKit>

Clive Robinson •
[December 16, 2022 9:27 AM](https://www.schneier.com/blog/archives/2022/12/apple-patches-iphone-zero-day.html/#comment-414083)

@ ALL,

Re : CVE-2022-42856

For those that don’t use TechCrunch because of the way the Yahho’s force themselves onto your browser,

There are other information sources, just one of which is,

‘https://thehackernews.com/2022/12/new-actively-exploited-zero-day.html

However before you go there or TecCrunch a look at,

<https://www.cvedetails.com/cve/CVE-2022-42856/>

Which currently tells you next to nothing, tells you most ICTsec and other ICT news sites will not have much of anything to tell you as of yet.

TimH •
[December 16, 2022 10:15 AM](https://www.schneier.com/blog/archives/2022/12/apple-patches-iphone-zero-day.html/#comment-414086)

I wish these attack reports would just advise one feature: is the vector foiled by having javascript disabled in the browser?

Denton Scratch •
[December 16, 2022 11:33 AM](https://www.schneier.com/blog/archives/2022/12/apple-patches-iphone-zero-day.html/#comment-414089)

> a zero-day vulnerability that “may have been actively exploited[…]”

I thought a “zero-day” was a vuln that has *not* been observed being exploited in the wild. Obviously I’m wrong about that – evidently I’ve been labouring under a misapprehension for some years!

So what does Bruce mean by a “zero day”?

Andrew P •
[December 16, 2022 11:43 AM](https://www.schneier.com/blog/archives/2022/12/apple-patches-iphone-zero-day.html/#comment-414090)

It would be interesting if Apple would indicate what, if any, protection Lockdown Mode provided against this CVE (and against all iOS CVEs).

Jinx •
[December 16, 2022 12:17 PM](https://www.schneier.com/blog/archives/2022/12/apple-patches-iphone-zero-day.html/#comment-414091)

@Denton Scratch:

Usually, “zero-day” means a newly-disclosed vulnerability for which the developer or vendor has had zero days to remediate or mitigate.

Some zero-days may have been discovered independently, kept secret, and are actively being exploited at the time of disclosure. Some zero-days are new to everyone, and there is a race between the patchers and the exploiters. If the discoverer works with the vendor, it’s possible that the (at one time) zero-day can be announced at the same time as the patch. I guess that is what the article implies?

Quantry •
[December 16, 2022 12:49 PM](https://www.schneier.com/blog/archives/2022/12/apple-patches-iphone-zero-day.html/#comment-414095)

@ Denton Scratch

hence my term “pre-zero-day”: like [a government] exploiting heart-bleed for years before disclosing it.

Clive Robinson •
[December 16, 2022 1:01 PM](https://www.schneier.com/blog/archives/2022/12/apple-patches-iphone-zero-day.html/#comment-414098)

@ TimH, ALL,

Re : The heresy of not kow-towing to JavaScript.

> “…is the vector foiled by having javascript disabled…”

You can be burned at the stake for saying such things, I know, I’m still brushing out the scorch marks from my “Flame Proof” protection…

Unfortunately a lot of very lazy people have turned a mess that was renamed as JavaScript back last century[1] into the veritable disaster and ICTsec hamster wheel of pain / Red Queen’s Race of today.

Nearly all that have JavaScript on their computers via their web browsers ~98% of Internet users, are getting right royally abused by it. In so many ways it’s not possible to list them all as the list grows alarmingly whilst you are writting.

I usually have both Cookies and JavaScript disabled and I’ve mentioned and advised this ever since this blog has existed, not just on this blog but other places.

Whilst the response here was initially cold, in other places it actually induced violent out burst from those who viewed me as “breaking their rice bowl”.

I used to say the same about other Web-tech like flash that nolonger realy exists and Java (not to be confused with JavaScrip). They have faded from Web client use thankfully, but,

“That scorched smell still lingers”

Just to be blunt,

“Untill developers understand the pit falls of client-side equivalent of “Off-Line” security, any code they right will be ‘insecure by default'”.

Understanding the finer points between “Off-line” and “On-line” security is majorly lacking in the ICT sector, especially in ICTsec which realy does surprise me…

To understand the differences start looking into,

1, Failed Credit-Card Security.

And quite a few more examples. You fairly quickly get to see the “failed” instances forming classes, and from there making the development of new instances all so much the easier for those that want to Crack, or Steal peoples Privacy.

But the short version is,

“Off-Line security is Faux-Security as the ‘Root of Trust’ is always vulnerable in some way to a hostile user”.

(We used to say it was “Game-over if they get Front-Pannel Access” back in the early 1980’s and probably back as far as the 1950’s but even I was not as such “a twinkle in the eye” back then 😉

All JavaScrip...