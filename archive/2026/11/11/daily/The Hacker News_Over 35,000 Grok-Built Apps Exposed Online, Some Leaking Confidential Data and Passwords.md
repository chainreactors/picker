---
title: Over 35,000 Grok-Built Apps Exposed Online, Some Leaking Confidential Data and Passwords
url: https://thehackernews.com/2026/11/over-35000-grok-built-apps-exposed.html
source: The Hacker News
date: 2026-11-11
fetch_date: 2026-11-12T09:02:54.901609
---

# Over 35,000 Grok-Built Apps Exposed Online, Some Leaking Confidential Data and Passwords

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgueiGhtTJ4g8vfPjVOP22mnT6eczZI-CgiOkXQ_Zv0gVno2MkG5UlOExxvSSAylm8NAtCfFkeaPxbyR3vYtpyOVi9ROWrrVZ9FKHFBH1IrQCCR46b2kh7JNKxenqefzCkCUewWhqRlds-IYjwzH7N7iWGpXxzeqhS6vIHDWIohTDx2ZZZReOOwVWv-SAmG/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-infographic-d)

# [Over 35,000 Grok-Built Apps Exposed Online, Some Leaking Confidential Data and Passwords](https://thehackernews.com/2026/11/over-35000-grok-built-apps-exposed.html)

**Swati Khandelwal**Nov 11, 2026Artificial Intelligence / Data Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh54t26Pk-bNbcIXgu8KrKpT_zN1KxEov16xTFlJ8kiPJ3-btXjGUE1lb0ZpamQU5jUHwmxzxHpYLsAQfiaHQUu3gxCIUw2gsEYNwMjL6nRm_jWm6t_VdHJkz6xj3fAsmTZKP8Bbax1qdT98a_PY4ynv81njiDyPXvIIihl4dqXxxC9pMMf8-Mn9dziy_A/s1700-nu-rw-lo-l85-e365/grokai.jpg)

Of the 37,571 Grok-built apps that security company **Claroc** found online, 35,578 were open to anyone without a sign-in, the researchers said yesterday.

They included 24 apps built by staff at the social network X and at SpaceXSI, the company that makes the Grok AI assistant. Most of the open apps were games, landing pages, and calculators, but about 1 in 10 contained internal business or personal data.

The staff apps included a confidential onboarding plan for a new sales hire, a sales territory map of 594 accounts, and an X advertising proposal to a U.S. federal agency marked confidential. SpaceXSI, formerly known as xAI, has since taken down all 24 staff apps but not other users' apps, the researchers said.

Besides those staff apps, the open apps contained internal data from 30 other organizations the researchers could identify, across fields ranging from construction and energy to healthcare and defense. Of those, 26 have more than 1,000 employees, and 6 are Fortune 500 companies.

According to the researchers' estimate in their [report](https://blog.claroc.io/ghostshares-grok-build-apps/), roughly 2% of the open apps contained material serious enough to rate as high or critical.

The exposed material included a hospital group's searchable list of more than 3,500 employees, an intensive care briefing on a single patient, a fire department's live shift board, and a contractor's timesheet whose code held every employee's password in plain text.

Grok can build a working app from a description typed into its chat, a feature its maker opened to every Grok plan on August 19. This chat builder shares the Grok Build name with a separate terminal coding tool, whose [repository uploads](https://thehackernews.com/2026/07/grok-build-uploads-entire-git.html) were reported on July 14.

Each published app gets its own subdomain of grok.me, and its creator chooses who can open it, according to the company's [launch announcement](https://x.ai/news/grok-build-for-everyone).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

No app goes public until its creator clicks Publish. In the paid account the researchers used, the next step offered 3 access settings: "Anyone with the link", "Invited users" and "Only you". "Anyone with the link" was already selected.

The setting matters because an app's address does not stay secret, the researchers say. Opening an app makes the visitor's computer look up its subdomain in DNS. Passive DNS services record such lookups, and anyone with an account can search those records by pattern.

Grok suggests 4 random words as each app's name, and about half of the names the researchers found followed that pattern. Such names are hard to guess, but that does not protect an app whose name already sits in a searchable list.

ChatGPT's app builder also puts each app on its own subdomain. But when the researchers shared an app there, its access was set to "Only me" until they changed it. A ChatGPT app address found in DNS data would lead to an app that only its owner can open, they say.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhs8WuVb3JYQy34eSV2jwOerQoLd0Ay60Ujyq4mSERCiowUh9O747pKe9_bgmHOwwa3ju39SsC0u1TBPTQC35xH5PWZjnwsCA-_XkGy77wT4HgK8bzcpS9JPSeuWzfPw7ve5VzfOiHj4X_aHf0-lQkCySguCs9IgqdOSEAQJqkH2aJzDeTxa6q7e3-9eDc/s1700-nu-rw-lo-l85-e365/shost2.png)

The researchers found the Grok app names using common subdomain discovery methods and loaded each app's first page once, without signing in.

To see what protection Grok adds on its own, the researchers built 2 test apps with made-up data and published both with the access setting already selected, "Anyone with the link".

The first, a contact list, got a database but no sign-in. Without signing in, the researchers added a row from a private browser window, and the next visitor saw it.

The second, a customer list for a 4-person sales team, got sign-in buttons that Grok added on its own: "Continue with Google" and "Continue with X". But the code Grok wrote added each person who signed in to the team before checking whether they belonged, so the check always passed.

An uninvited Google account belonging to someone other than the owner got in, viewed every customer, edited one record, and deleted another.

The researchers ran these tests only on their own apps. They did not test whether any of the open apps they found would accept such changes.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiDV9oxFVTUXABpaZrmGxN6-eymAQdMX0aYI8L-6Pm72jX74aW2vHuGJpViSM7ffJinGlokuZf5HCVvTN9ip3U_kiYTllQFybc8c7NM-hx6XW2kxSZbBMyQvr0z8swPKRVgFICT4sdPv2qj10XstkCDufNon5P-agRGPVbexznRYNzQwY5iLCIFafYgaks/s1700-nu-rw-lo-l85-e365/shost2data.png)

The researchers reported their findings to SpaceXSI on Sunday through the address in its security.txt file, including 2 of the staff apps. They reported the other 22 on Monday.

By the time the researchers published yesterday, the company had not replied to their report, but it had answered a reporter's questions about the research.

As the researchers describe, the company said Grok apps stay private until their creator shares them. Publishing takes several steps, including choosing between "Only you" and "Anyone with the link," as well as a legal disclaimer. Employee accounts are set to "Only you" by default.

Even so, 24 apps built by staff a...