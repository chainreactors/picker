---
title: Attacker Hijacks AI Coding Assistant Session, Spreads Shai-Hulud Across About 100 Repositories
url: https://thehackernews.com/2026/09/attacker-hijacks-ai-coding-assistant.html
source: The Hacker News
date: 2026-09-16
fetch_date: 2026-09-17T06:59:40.902746
---

# Attacker Hijacks AI Coding Assistant Session, Spreads Shai-Hulud Across About 100 Repositories

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Attacker Hijacks AI Coding Assistant Session, Spreads Shai-Hulud Across About 100 Repositories](https://thehackernews.com/2026/09/attacker-hijacks-ai-coding-assistant.html)

**Swati Khandelwal**Sep 16, 2026Artificial Intelligence / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEghZsSi9JbsiALEhfWv_49vjKw2uHa-lBOUWCwhyphenhyphensppIZLuNgoQ-VQTs2EjRmXjemfvM0Fj9knUSdDIYbSWg5Pf_sqKBOGV5BA67GVYn_lNreIN_Kwpp3u0yxKgF4dIHXRj-NKcCyimE0kwHUWHqxP7SHUd-Tu31S3jfzxOPmN8_Xk8d5GYRce2N4MdmYY/s1700-nu-rw-lo-l85-e365/shai.jpg)

Mandiant says an attacker hijacked an active AI coding-assistant session at an unnamed software-as-a-service provider and later spread [Shai-Hulud](https://thehackernews.com/2025/09/40-npm-packages-compromised-in-supply.html) across about 100 internal code repositories.

Before the repository spread, the assistant recommended software that the attacker had poisoned, and the recommendation was accepted. The worm stole repository secrets and source code for the company's products.

The case appears in [Mandiant's September 2026 report](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026). The public case study does not say when the intrusion happened or how the attacker took over the active coding-assistant session.

### How the Attack Unfolded

After the recommendation was accepted, the attacker used the developer's active session to install an infostealer through a poisoned PyPI package. The attacker also stole GitHub OAuth tokens.

The attacker then deployed the self-spreading Shai-Hulud worm across approximately 100 internal code repositories.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The attacker also poisoned a package in the company's official namespace. Another employee pulled the compromised version, causing a second infection.

Mandiant had already documented attackers using AI in real attacks. In a [March 2026 report](https://cloud.google.com/security/resources/ai-risk-and-resilience), it said attackers had moved during 2025 from using generative AI mainly to speed up work to using large language models in malware and active attacks.

### How Defenders Can Protect AI-Assisted Development

For this case, Mandiant recommends three controls for AI-assisted development:

* Check AI-recommended third-party dependencies against cryptographic checksums and approved allowlists.
* Keep raw API keys, long-lived OAuth tokens, and other secrets out of direct reach of extensions.
* Route dependency traffic through controlled internal repositories.

Recent Shai-Hulud-family attacks have also targeted developer tools and credentials. In August, a [Keyv-linked npm worm](https://thehackernews.com/2026/08/keyv-linked-npm-worm-poisons-hundreds.html) poisoned hundreds of packages and planted hooks for Claude Code and Visual Studio Code, while a later analysis found a Shai-Hulud variant scanning [469 locations for credentials](https://thehackernews.com/2026/09/shai-huluds-reach-just-grew-to-469.html) across developer systems, CI/CD tools, cloud configurations, and AI tool files.

These were separate campaigns, and the available evidence does not link them to the unnamed Mandiant intrusion.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

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
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence), [Malware](https://thehackernews.com/search/label/Malware), [Software Security](https://thehackernews.com/search/label/Software%20Security), [Supply Chain](https://thehackernews.com/search/label/Supply%20Chain)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

OpenAI Agents Linked to RubyGems Campaign That Gained RCE on RubyDoc Servers](https://thehackernews.com/2026/09/openai-agents-linked-to-rubygems.html)

[![The Hacker News](data:image/svg+xml;base64...)

GitLab CVSS 10 File-Read Flaw Draws In-the-Wild Probes After Disclosure](https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html)

[![The Hacker News](data:image/svg+xml;base64...)

Claude Used to Automate Exploitation and Data Theft Across Multiple Victims](https://thehackernews.com/2026/09/claude-used-to-automate-exploitation.html)

[![The Hacker News](data:image/svg+xml;base64...)

Attackers Chain JFrog Artifactory Flaws to Gain Admin Control and Plant Backdoors](https://thehackernews.com/2026/09/attackers-chain-jfrog-artifactory-flaws.html)

[![The Hacker News](data:image/svg+xml;base64...)

PaperCut Replaces Emergency Patches With Fixes for Two Actively Exploited Flaws](https://thehackernews.com/2026/09/papercut-replaces-emergency-patches.html)

[![The Hacker News](data:image/svg+xml;base64...)

Cisco FMC Flaws Exploited to Steal Credentials and Deploy Qilin Ransomware](https://thehackernews.com/2026/09/cisco-fmc-flaws-exploited-to-steal.html)

[![The Hacker News](data:image/svg+xml;base64...)

ThreatsDay: 200 Android Flaws, Browser-Built Phishing, 119K Scam Shops + 23 More Stories](https://thehackernews.com/2026/09/threatsday-200-android-flaws-browser.html)

[![The Hacker News](data:image/svg+xml;base64...)

Check Point Disclo...