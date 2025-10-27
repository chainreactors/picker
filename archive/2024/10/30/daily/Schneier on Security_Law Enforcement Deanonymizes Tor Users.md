---
title: Law Enforcement Deanonymizes Tor Users
url: https://www.schneier.com/blog/archives/2024/10/law-enforcement-deanonymizes-tor-users.html
source: Schneier on Security
date: 2024-10-30
fetch_date: 2025-10-06T18:55:29.886624
---

# Law Enforcement Deanonymizes Tor Users

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

## Law Enforcement Deanonymizes Tor Users

The German police have [successfully deanonymized](https://marx.wtf/2024/10/10/law-enforcement-undermines-tor/) at least four Tor users. It appears they watch known Tor relays and known suspects, and use timing analysis to figure out who is using what relay.

Tor has [written](https://forum.torproject.org/t/tor-relays-important-update-on-an-upcoming-german-broadcasting-story-about-tor-onion-services/14656) [about](https://blog.torproject.org/tor-is-still-safe/) this.

Hacker News [thread](https://news.ycombinator.com/item?id=41942978).

Tags: [de-anonymization](https://www.schneier.com/tag/de-anonymization/), [law enforcement](https://www.schneier.com/tag/law-enforcement/), [Tor](https://www.schneier.com/tag/tor/)

[Posted on October 29, 2024 at 7:02 AM](https://www.schneier.com/blog/archives/2024/10/law-enforcement-deanonymizes-tor-users.html) •
[12 Comments](https://www.schneier.com/blog/archives/2024/10/law-enforcement-deanonymizes-tor-users.html#comments)

### Comments

Winter •
[October 29, 2024 8:44 AM](https://www.schneier.com/blog/archives/2024/10/law-enforcement-deanonymizes-tor-users.html/#comment-441382)

TOR and TLAs are in an arms race. And, like the TOR project say:

> In an arms race, keep your arms up to date

According to the TOR article, the error of the Onion Service manager is to not keep their software up to date.

Clive Robinson •
[October 29, 2024 9:57 AM](https://www.schneier.com/blog/archives/2024/10/law-enforcement-deanonymizes-tor-users.html/#comment-441383)

Not at all surprising.

Tor was not designed to be proof to “Traffic Analysis” but saying that got so many “incoming” responses from those who did not understand.

As for most users it appeared they wanted low latency for the things they were watching etc.

What does surprise me is just how long it’s taken for this type of obvious attack to become a “tool” and become “known” publicly.

Clive Robinson •
[October 29, 2024 12:20 PM](https://www.schneier.com/blog/archives/2024/10/law-enforcement-deanonymizes-tor-users.html/#comment-441384)

Related in that it involves Tor but…

Posted today is an article about one of the reasons the Internet is so broken, and how some of the cracks can be wedged open to abuse innocent parties,

<https://delroth.net/posts/spoofed-mass-scan-abuse/>

On reading it you will see a way that can be used against Tor network nodes so that they get taken down.

If you are someone who’s interest is in pushing Tor users off of other nodes onto ones you control or monitor this is one of many ways to do. It does of course have the advantage that it’s very difficult to trace back to the source.

gale •
[October 29, 2024 12:23 PM](https://www.schneier.com/blog/archives/2024/10/law-enforcement-deanonymizes-tor-users.html/#comment-441385)

If all Tor does is block tracking by non-law-enforcement entities, and make law enforcement have to work really hard to track people—specific people, with warrants—I think that’s still a pretty good result.

The real threat has always been “drag-net” tracking, like countries and advertisers tracking entire populations. I’m not looking at illegal stuff, but I don’t need some data broker knowing my political leanings and pornography preferences.

Who? •
[October 29, 2024 1:10 PM](https://www.schneier.com/blog/archives/2024/10/law-enforcement-deanonymizes-tor-users.html/#comment-441386)

Slightly off-topic: OpenSSH 9.5, released one year ago, includes a keystroke timing obfuscation mechanism; it has improved over the last year, its goal is making difficult fingerprinting users by listening to their typing patterns. We know certain implementations of encryption algorithms are vulnerable to timing-attacks too.

A new, and profitable, vector attack it seems.

What is really odd is that Tor should be resistant to the attack supposedly used by this law enforcement agency since mid-2018.

lurker •
[October 29, 2024 2:56 PM](https://www.schneier.com/blog/archives/2024/10/law-enforcement-deanonymizes-tor-users.html/#comment-441388)

From the Tor blog

> … an Onion Service used by a Tor user using an old version of the long-retired application Ricochet …

Looks like somebody didn’t get the message about keeping your system up to date.

Sean •
[October 30, 2024 2:52 AM](https://www.schneier.com/blog/archives/2024/10/law-enforcement-deanonymizes-tor-users.html/#comment-441395)

Old news this, Tor has long ago said that it is not totally anonymous, and that it is possible to track users using timing analysis, especially if you have control over a lot of exit nodes with low latency, which often are done by the 3 letter agencies, so as to track use of the network.

iAPX •
[October 30, 2024 6:59 AM](https://www.schneier.com/blog/archives/2024/10/law-enforcement-deanonymizes-tor-users.html/#comment-441396)

Timing analysis, including injecting delay patterns, is used since decades, with great success.

pondering •
[October 30, 2024 10:14 AM](https://www.schneier.com/blog/archives/2024/10/law-enforcement-deanonymizes-tor-users.html/#comment-441399)

According to the linked article, the police had the ISP surveil their customers. I wonder how much a VPN to a Tor bridge (perhaps coupled with pluggable transports) could have helped against this?

And on an other note, whether the new release of the AI update to Apple devices has anything to do with a contested election season and increased risk for domestic terrorism, and the need to query users devices.

Aaron •
[October 30, 2024 11:43 AM](https://www.schneier.com/blog/archives/2024/10/law-enforcement-deanonymizes-tor-users.html/#comment-441402)

Just another case of habits, routines and laziness as security vulnerabilities.

A Felon in BOZO ideho •
[October 31, 2024 7:21 PM](https://www.schneier.com/blog/archives/2024/10/law-enforcement-deanonymizes-tor-users.html/#comment-441436)

Most TOR exit nodes in the U.S.A. are set up/controlled by NSA, and this has been, FOR THOSE WHO CARED TO KNOW, public knowledge for several years now. Another note: FBI has been tracking and SUCCESSFULLY IDENTIFYING TOR users for several years now. I’ve known this since the beginning but most TOR users did NOT, plus if you believe that ANY, and I MEAN A N Y browser extension, (and this DOES INCLUDE NO-Script TOR Browser Extension) is not sending your IP Address info “somewhere” and not just “your IP Address” but all those other nodes, like the Guard, and ALL OTHER IP addresses of the ENTIRE ONION, AND NO, TOR OVER VPN WILL NOT ANONYMIZE YOU either.

Mark •
[November 1, 2024 5:27 PM](https://www.schneier.com/blog/archives/2024/10/law-enforcement-deanonymizes-tor-users.html/#comment-441459)

> I wonder how much a VPN to a Tor bridge (perhaps coupled with pluggable transports) could have helped against this?

Not at all. Law enforcement sees data going into the black box and data coming out of the black box. The nat...