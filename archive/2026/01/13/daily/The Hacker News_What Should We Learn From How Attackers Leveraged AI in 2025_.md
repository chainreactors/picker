---
title: What Should We Learn From How Attackers Leveraged AI in 2025?
url: https://thehackernews.com/2026/01/what-should-we-learn-from-how-attackers.html
source: The Hacker News
date: 2026-01-13
fetch_date: 2026-01-14T03:36:14.588610
---

# What Should We Learn From How Attackers Leveraged AI in 2025?

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlCcy_j509wX0FKMRQX-zVzeBNtSIDsH6oDFlljaAeQRz65xSx8g9jicghxtpvDC8yI10jCv1TPEcyPvfoCKOby_0ZjsnNc-3wZG5YeA8sZQBCbZxhzd00jR2ZG8rZr-vp3WLrbXaMVbsVrDwBEeBWBbNSSwFjeuNzhrVOigDqTM7VWfSUJqBwEoYALS58/s728-e100/z-header-d.png)](https://thehackernews.uk/modern-security-shift-d)

# [What Should We Learn From How Attackers Leveraged AI in 2025?](https://thehackernews.com/2026/01/what-should-we-learn-from-how-attackers.html)

**Jan 13, 2026**The Hacker NewsThreat Intelligence / Identity Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg11caZQqhaS0OyoXT_GpH_CIUPoC00sjkeg4ycrORRwI75LWELCfMCO0yyfL1FoKf8jrX6NJZsGVFZ2m1o_H3VFdFtBJprczhcQn5bbS5YH65k4I1PVoGAJGZP4N2NHfj_m2VjXJPmO8k-GfaZFUcIXSN9lLuOZ3Dnl8cqQkwkMEWHWY0cYuu4QIBKXVE/s790-rw-e365/AI.jpg)

***Old Playbook, New Scale:*** *While defenders are chasing trends, attackers are optimizing the basics*

The security industry loves talking about "new" threats. AI-powered attacks. Quantum-resistant encryption. Zero-trust architectures. But looking around, it seems like [the most effective attacks in 2025](https://www.ox.security/webinar/threat-intelligence-update-whats-been-working-for-hackers-and-what-have-the-good-guys-been-doing/?utm_source=hacker_news&utm_medium=paid&utm_campaign=threat_intel_update_webinar&utm_content=sponsored_article) are pretty much the same as they were in 2015. Attackers are exploiting the same entry points that worked - they're just doing it better.

## **Supply Chain: Still Cascading Downstream**

As the Shai Hulud NPM campaign showed us, supply chain remains a major issue. A single compromised package can cascade through an entire dependency tree, affecting thousands of downstream projects. The attack vector hasn't changed. What's changed is how efficiently attackers can identify and exploit opportunities.

AI has collapsed the barrier to entry. Just as AI has enabled one-person software projects to build sophisticated applications, the same is true in cybercrime. What used to require large, organized operations can now be executed by lean teams, even individuals. We suspect some of these NPM package attacks, including Shai-Hulud, might actually be one-person operations.

As software projects become simpler to develop, and threat actors show an ability to play the long game (as with the XZ Utils attack) - we're likely to see more cases where attackers publish legitimate packages that build trust over time, then one day, with the click of a button, inject malicious capabilities to all downstream users.

## **Phishing: Still Just One Click Away**

Phishing still works for the same reason it always has: humans remain the weakest link. But the stakes have changed dramatically. The recent npm supply chain attack demonstrates the ripple effect: one developer clicked a bad link, entered his credentials and his account was compromised. Packages with tens of millions of weekly downloads were poisoned. Despite the developer publicly reporting the incident to npm, mitigation took time - and during that window, the attack spread at scale.

## **Official Stores: Still Not Safe**

Perhaps most frustrating: malware continues to bypass official gatekeepers. Our research on malicious Chrome extensions stealing ChatGPT and DeepSeek conversations revealed something we already know from mobile app stores—automated reviews and human moderators aren't keeping pace with attacker sophistication.

The permissions problem should sound familiar because it's already been solved. Android and iOS give users granular control: you can allow location access but block the microphone, permit camera access only when an app is open, not in the background. Chrome could implement the same model for extensions - the technology exists. It's a matter of prioritization and implementation.

Instead, users face a binary choice with extensions requesting permission to "read information from all websites." If an extension asks for that level of access, in most cases it will be used for malicious purposes, or it will later be updated to do so.

## **Attackers don't have the Shiny Tool Syndrome**

Attackers didn't throw out their playbook when AI arrived - they automated it. They're still exploiting supply chains, phishing developers, and sneaking malware past reviewers. They're just doing it with one-tenth the resources.

We shouldn't be chasing shiny new defense strategies while the basics still don't work. Fix permissions models. Harden supply chain verification. Make phishing-resistant authentication the default. The fundamentals matter more now, not less.

**Attackers optimized the basics. What should defenders prioritize?** Join OX for [our upcoming webinar:](https://www.ox.security/webinar/threat-intelligence-update-whats-been-working-for-hackers-and-what-have-the-good-guys-been-doing/?utm_source=hacker_news&utm_medium=paid&utm_campaign=threat_intel_update_webinar&utm_content=sponsored_article) **Threat Intelligence Update: What's Been Working for Hackers and What Have the Good Guys Been Doing?**

We'll cover attack techniques gaining traction, what's actually stopping them, and what to prioritize when resources are limited. Register here.

[Register here.](https://www.ox.security/webinar/threat-intelligence-update-whats-been-working-for-hackers-and-what-have-the-good-guys-been-doing/?utm_source=hacker_news&utm_medium=paid&utm_campaign=threat_intel_update_webinar&utm_content=sponsored_article)

Note: This article was exclusively written and contributed by Moshe Siman Tov Bustan, Security Research Team Lead at OX.

Found this article interesting? This article is a contributed piece from one of our valued partners. Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Sh...