---
title: How Synthetic Identity Fraud is Coming for Machine Identities
url: https://thehackernews.com/2026/07/how-synthetic-identity-fraud-is-coming.html
source: The Hacker News
date: 2026-07-23
fetch_date: 2026-07-24T05:05:41.860662
---

# How Synthetic Identity Fraud is Coming for Machine Identities

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

# [How Synthetic Identity Fraud is Coming for Machine Identities](https://thehackernews.com/2026/07/how-synthetic-identity-fraud-is-coming.html)

**The Hacker News**Jul 23, 2026Identity Security / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg3CPk7mPjct6TcYwb9c1LBGjEBTkHjIkX-_CqYIrmdg3nJu-Vyjmc2qCT_cZbFEoUNaiIEQafCVxDDD0RZfflUs8LqGu9Ecx0N7Tu3nEzHXUW2nKLefXYKsRHfVtv-TZXw_WDILy6sKkE5kk3ts5cBTaSfq1mReYwo6Fb1ghPkg4Z4bLiNuAP4ehxqFG0/s1700-e365/keeper.jpg)

Most people understand identity theft as an attacker stealing a real person's sensitive information and impersonating them. Synthetic identity fraud is much harder to catch. Instead of stealing a real identity, the attacker manufactures a new one, frankensteining together several real data points with fabricated ones to create a person who doesn't exist. Since no real victim monitors misuse, a fake identity can silently accumulate permissions and credibility over time before it's ever detected. This same principle has a largely unexplored parallel with Non-Human Identities (NHIs).

Security teams are spending significant effort to protect NHIs from being stolen. Still, the machine-side equivalent of synthetic identity fraud is rarely discussed: identities that were never legitimately provisioned from the start. Following this approach, an attacker doesn't hijack an existing service account but instead fabricates one, blending real environmental attributes with fake ones so it appears to belong. As enterprises accumulate NHIs faster than they can track them, a fabricated one may slip into the mix with ease if governance is weak and there's no human ownership.

## What synthetic identity fraud looks like for machine identities

For human beings, synthetic identity fraud is well understood as an identity assembled, not stolen, to pass checks while connecting to no actual person. The same construction works against machine identities, but most organizations focus on stolen NHI credentials rather than fabricated identities. With fabricated machine identities, an attacker doesn't borrow a real identity but rather creates one that was never supposed to exist. Instead of logging in as a legitimate service account, the attacker registers a new admin-level identity with a similar naming structure, grants it privileges and lets it go unnoticed. Since nothing is hijacked, there's no compromised user to alert and no suspicious behavior to flag.

What makes these identities convincing is the combination of real and invented attributes. A fabricated NHI inherits its environment's naming conventions, exists in the correct domain, carries plausible-looking metadata and requests the kinds of permissions other NHIs already hold. To an administrator skimming a directory of tens of thousands of service accounts, it is simply one more routine workload, which is why this is one of the [most overlooked NHI risks](https://www.keepersecurity.com/blog/2025/11/25/top-7-nhi-risks-and-how-to-mitigate-them/).

## How fabricated machine identities are built

None of the techniques attackers use to create fake machine identities are new. What is new, however, is seeing them as a pattern of inserting a credible-looking but illegitimate identity into an environment predisposed to trust it. In practice, attackers create fabricated machine identities in a few main ways:

* **Rogue service account**: Instead of compromising an account that already exists, an attacker who has gained access creates a new account that *looks* like an existing one, with similar-looking attributes and standing access. An account that was never sanctioned yet behaves like one is the purest form of a fabricated machine identity.
* **DCShadow**: Operating at the infrastructure level, an attacker doesn't fabricate an account but rather an entire source of authority. Because it depends on domain administrator rights the attacker already holds, it's a post-compromise move rather than a way in: The attacker temporarily registers a rogue domain controller so malicious changes look like legitimate replication traffic from a trusted peer. Once that impersonated infrastructure is accepted, whatever it pushes inherits the system's own credibility.
* **Shadow credentials**: An attacker implants fabricated authentication onto an existing object, injecting attacker-controlled material so the attacker can authenticate as that object at will. Since the identity already exists and looks untouched, this is the subtlest means of proving that an identity has been silently forged.

While the mechanics differ, they all involve an illegitimate identity that the environment has accepted as one of its own. It's important to separate this from a related idea called the [synthetic persona](https://nhimg.org/glossary/synthetic-persona/), defined by the NHI Management Group as a fabricated identity built to appear credible to *people* and used to deceive human users through fake profiles and social engineering tactics. That's the inverse of a fabricated machine identity, which isn't a fake human meant to deceive people but a fake machine living inside systems, holding real privileges and answering to no one.

The lack of attention that this machine-side equivalent is getting is what makes it so dangerous. Fabricated machine identities can evade detection built to identify stolen ones because the real owner of a stolen identity may notice a login from an unfamiliar place or receive a dark web alert. Meanwhile, a fabricated identity with no owner will not raise any alarms about suspicious behavior, leaked secrets or anything worth noting. Since NHIs are growing rapidly at a pace outnumbering human users, enterprises may not notice an unmonitored identity as an outlier if it hides and quietly accumulates permissions.

### Why agentic AI makes this more timely

Until recently, fabricating a machine identity required an attacker to get into a system, create the fake account and ass...