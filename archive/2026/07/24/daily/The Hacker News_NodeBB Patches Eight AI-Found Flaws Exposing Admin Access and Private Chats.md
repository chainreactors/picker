---
title: NodeBB Patches Eight AI-Found Flaws Exposing Admin Access and Private Chats
url: https://thehackernews.com/2026/07/nodebb-patches-eight-ai-found-flaws.html
source: The Hacker News
date: 2026-07-24
fetch_date: 2026-07-25T05:00:49.480189
---

# NodeBB Patches Eight AI-Found Flaws Exposing Admin Access and Private Chats

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [NodeBB Patches Eight AI-Found Flaws Exposing Admin Access and Private Chats](https://thehackernews.com/2026/07/nodebb-patches-eight-ai-found-flaws.html)

**Swati Khandelwal**Jul 24, 2026Web Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixTLaT7NCY3UuotqW1AHLiB1xN5K-nlqtpnOav_n7PWHNWWZmrSmmPTzmL6oA7N7dOgwSGxEbbBq90Q3OVK6wF2PSXdXLs7mKmBYc1dEBIc64Qsq6XEl7rYbv5PjRMViYiGXr8-ypMSs0ZJv_rJXqSWIbS4FVTuIphO7g9IfC0MG6m5dDXPXJoz7iezck/s1700-e365/nodebb.jpg)

Eight security flaws in NodeBB went public on Wednesday, along with the code to exploit them. Aikido Security rates all eight as high severity and says its AI pentest agents [found them](https://www.aikido.dev/blog/eight-high-severity-vulnerabilities-nodebb) in a six-hour review of the forum software's source code.

Every version before 4.14.0 is affected. NodeBB has fixed them all, and administrators should be on 4.14.2.

The simplest one takes a settings change. A regular forum member could point their homepage setting at the admin address, reload the page, and the admin dashboard opened for them. No password, no exploit code.

The forum's own interface blocks that setting, but the block only ran in the browser and could be sidestepped. Most of what a member could then reach was read-only, including the error log and any user list an admin had exported, though they could also swap the site logo.

Two more gave an attacker with no account at all access to things meant to be private. One let anyone claim to be any user and read private messages one at a time. The other handed over the contents of private categories to anyone who asked for them the right way.

The widest flaw was in how NodeBB builds its pages. The software fills a page in, then makes a second pass to swap in translated text. User input was already sitting in the page by then, and it could smuggle in the codes that second pass looks for. That let an attacker plant a link almost anywhere on the site, including inside ordinary forum posts, that runs their code when a visitor clicks it.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The rest let an attacker take over an existing post, inflate a post's vote count, and run two attacks that plant malicious code by way of a fake server on the fediverse, the network of connected social sites a NodeBB forum can join.

## Who Was Actually Exposed

The eight are not equal. Three need no account on the target forum. Two need an ordinary member account. The last three need someone to click a link or open a page.

Five of the eight, by The Hacker News' count, sit in NodeBB's federation code, the part that connects a forum to Mastodon and other social sites. That decides who was at risk. Forums installed fresh on version 4 [federate by default](https://docs.nodebb.org/activitypub/), so they had all eight. Forums that upgraded from version 3 had federation switched off automatically, and unless an administrator turned it back on, only three of the flaws applied.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhPAsFqrqZ46KMYzyiH7SDh2P5ahwwtWVV-tJzuk5rqEqjmQH4h0IzScb_LUCkB1XSjlaWW4i7Eu30qUh9CPB2U3bkEDJA7fgA_5j2cSTx8Mtiz8S_Z5HrlmTYkHwzPVjdCEgdGiHdmGJ-MtRhcLa68BbdL95WqmDfRw726hBoSGSI-0P05jhtLOmTa73Q/s1700-e365/xss.png)

Aikido published no severity scores for the individual flaws, and NodeBB's release notes do not rate them. NodeBB's own [bug bounty scale](https://nodebb.org/bounty) rates cross-site scripting and account takeover as high, and getting admin access as critical.

## Patched in Pieces Since May

NodeBB fixed most of them quietly, without saying what they were. The Hacker News checked each fix against NodeBB's release history: four shipped in May, two in June, and the biggest, a rebuild of how the software handles page text, arrived in 4.14.0 on July 9. That rebuild [touched 325 files](https://github.com/NodeBB/NodeBB/pull/14341).

Aikido's writeup says the issues were fixed in early July, which does not match that record. Its link for the admin-panel fix points to a change made in January 2024, two years before the review, while NodeBB's own release notes name a different change from May. Neither side explains the gap.

Administrators should upgrade to [4.14.2](https://github.com/NodeBB/NodeBB/releases/tag/v4.14.2), released July 23. Expect some work, because 4.14.0 changed how page templates handle text and custom themes and plugins may need updating. Switching federation off is not a full answer either, since three of the flaws have nothing to do with it.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhrEy9jEFSadp95ztaH87-97Z_U9V94nUsE-BsrdwSR8ETPJDyCjy63vNxc-O26z6VhA3nDOrU24lJqNdy24bfNxGPxGxXNRvM_XCwnZ7ukY5wDnXKsvDZN42aCT1JFYXZZGoZFEtSQgbba742oPTEgEbtoa0GBYWWkkkU43P1wPq-LByZPJfbzwZsb1RiI/s728-e100/sygnia-d-1.png)](https://thn.news/sygnia-webinar)

None of the eight has a CVE tracking number, and nobody has reported attacks using them. A separate NodeBB federation flaw does have one, [CVE-2026-58593](https://nvd.nist.gov/vuln/detail/CVE-2026-58593), filed on July 1. It is not one of Aikido's eight, but it sits in the same code and lets an outside server post and send messages in the name of any local account, the administrator's included. It needs federation switched on, and the record names no fixed version.

NodeBB's bug bounty page says it rejects AI-generated reports and pays only for work the submitter did themselves. That governs payouts rather than fixes, and these eight were reported to the maintainers directly and patched.

NodeBB is not the only project fielding them: the automation platform n8n patched a [login flaw](https://thehackernews.com/2026/07/n8n-token-exchange-flaw-could-let.html) in June that a different AI pentest agent found. Co-founder Julian Lam's [note in the release announcement](https://community.nodebb.org/topic/19387/nodeb...