---
title: Enterprise Defenses Recovered at the Edge and Collapsed Inside
url: https://thehackernews.com/2026/08/enterprise-defenses-recovered-at-edge.html
source: The Hacker News
date: 2026-08-12
fetch_date: 2026-08-13T04:05:20.886955
---

# Enterprise Defenses Recovered at the Edge and Collapsed Inside

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

![cybersecurity](data:image/svg+xml;base64...)

# [Enterprise Defenses Recovered at the Edge and Collapsed Inside](https://thehackernews.com/2026/08/enterprise-defenses-recovered-at-edge.html)

**The Hacker News**Aug 12, 2026Security Validation / Attack Simulation

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjoBNKr6YWBC4uPzzXNZNX_sduYkalrtPSfiT01s6R6tq9uRzAs8TRoyv0DSwM-Wy_RmiGv923yzsB1DK3mgg5vudYdTwIk7wubUJYB0f-6AADquodryt0KofkU5aKxKaKBLirP1A0PuaBC_lfWEYJKlthyphenhyphencmmT2WBQkIRLLFLI5kWKZcJWY5rxrN-qa2M/s1700-e365/picuss.jpg)

Enterprise defenses are tuned to catch the attacks that make noise. This year's data shows attackers winning by making none.

According to Picus Labs' new **[Blue Report 2026](https://hubs.li/Q04s3wdR0)**[,](https://hubs.li/Q04s3wdR0) which measured more than 338 million real attack simulations across actual client production environments in the first half of 2026, defenses are having one of their strongest years yet. Average prevention effectiveness **climbed from 62% to 69%**, matching its 2024 peak, and logging reached a **four-year high of 58%**.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0qoTectFGj0cvhgjcNYxPjotrEoeRegwYnH_0ZmlLr9JNFBK66w2oAsQgGroEMURvP0h2nvmes8eKitspVvvp-YzY2vuxKrWkAc48A-XDTkwMGNi3BDwsiP5YpD8AU-gH170TfTcmPaX6sHdSbe-WXvsPMx3jIcCbWCQJEUzcN2y6HyFO-NLZD6BhKI0/s1700-e365/1.png)

The good news: The recovery is real. The bad news: It's taking place almost exclusively at the perimeter.

The report's sharper finding is what happens **after that perimeter is crossed**. Inside, the picture inverts**: defenses that look strong from the outside turn soft**, and are the softest of all against the quiet moves, the reconnaissance and credential theft that precede every serious breach.

This is a fault line that runs through the entire report.

## **A vulnerable interior behind a recovering perimeter**

For the first time, Picus Labs measured post-compromise prevention with [autonomous penetration testing](https://www.picussecurity.com/platform/autonomous-penetration-testing): what controls actually break the attack chain once an adversary is already operating inside the network as an authenticated user. The **Post-Compromise Prevention Rate was a meager 37%.**

The perimeter now blocks roughly two attacks out of three; inside, defenses stop barely one in three.

But that average hides the more useful pattern. **The interior does not fail evenly.** It fails along one clean line. Here too, **noisy actions get caught, while quiet ones don’t.**

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgo2dPXOPn3nZ3Gv1_UXri-EJRVwxER1HVmuFE3ma9cYHoqgNxUotpNhrKbi2XetzU3rWWmCfeTvou1WR02VFk6Jd6mJn39EWaK5-wzoOtvCXlQmGAIIhISAi_c28YpMt-3musqnmgHu_l8dAfPcM8NGzlLehC0VbGu3gSre5xQGis8oN5gI-qx5jLxXSU/s1700-e365/2.png)

Malicious behavior running code or jumping between machines was blocked most of the time: lateral movement through service execution, using techniques like Sharp-ServiceExec and SMBExec, was stopped around 90% of the time, and UAC-bypass privilege escalation was almost as successful at around 85%.

That’s EDR doing its job, and **years of assume-breach investment** showing up, as hoped, in the numbers.

Meanwhile, the quiet work runs almost *unopposed*.

Reconnaissance, mapping the domain and enumerating shares and sessions, was the least-prevented category of all, only being stopped a paltry 10% of the time. Defenses did a little better at detecting credentials being quietly read out of memory at around 22%, and one variant, pulling secrets straight from the registry, was stopped in less than 1% of attempts.

An attacker can map the environment, harvest sessions, and read credential material with almost no resistance, getting their proverbial ducks in a row **before taking any noisier action that would trip a control.**

## **A signature catches the famous attack, not the behavior**

One result captures why. The same credential-theft tool, Mimikatz, was run at the same objective three ways, and the prevention scores could not have been further apart.

Dumping credentials the classic, heavily signatured way, straight from LSASS process memory, was blocked almost every time. Pulling them from other memory locations, or reading them from the registry, **was almost never blocked at all.**

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2Gjk7nqMRon1Nnp5bxusThN9kyi_KjWNProPw6lbWSZhCkaTV2n1UEG-t887vW4pMPAKSUYvsrgM_7i0SjlQGQpN3u-2bLWAg1I4-SlIL6PEu2FGlcvSGMVp_d7N5U83ejdung7kbTRgOpTnMKK1DByYrUwQvNdXWbJlPjT_VNpXHYAYGjtmDh4E7Xls/s1700-e365/3.png)

Same tool, same goal, same environment.

The only variable between these three was **how conspicuous the route was.** The LSASS path is loud in a way tools can match: a process opens a handle to lsass.exe and reads its memory, an event vendors have instrumented for years. Reading the registry never touches lsass and looks like ordinary privileged activity, so a control built for the first event has nothing to fire on for the second.

**Alarmingly, that 94% is even softer than it sounds**, because it was measured against one known build of an open-source tool whose recognizability lives in **how it was compiled, not in what it does.**

* Rename the strings a signature keys on and the hash is new.
* Load it in memory and nothing lands on disk to scan.
* Or skip Mimikatz altogether and take the same dump with a Microsoft-signed utility already on the box.

Each path ends with credentials in hand; only the thing the signature was watching for changed. A **prevention score built on signatures** tells you how well you catch what you have already seen, **not whether you’re actually stopping the behavior underpinning it**.

## **The data shows stealth pays off for attackers**

And that gap isn’t confined to one tool.

The **[Red Report 2026](https://hubs.li/Q04s3wNv0)** found attackers deliberately shifting toward stealth, and the Blue Report shows this behavior is working for them across the board. The single least-prevented technique in the entire dataset was hiding command history, stopped just 1% of the time. The behaviors defenders miss are exactly the low-noise ones that today’s evasion-minded attacker...