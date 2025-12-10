---
title: Storm-0249 Escalates Ransomware Attacks with ClickFix, Fileless PowerShell, and DLL Sideloading
url: https://thehackernews.com/2025/12/storm-0249-escalates-ransomware-attacks.html
source: The Hacker News
date: 2025-12-09
fetch_date: 2025-12-10T03:23:02.449542
---

# Storm-0249 Escalates Ransomware Attacks with ClickFix, Fileless PowerShell, and DLL Sideloading

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [Storm-0249 Escalates Ransomware Attacks with ClickFix, Fileless PowerShell, and DLL Sideloading](https://thehackernews.com/2025/12/storm-0249-escalates-ransomware-attacks.html)

**Dec 09, 2025**Ravie LakshmananRansomware / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixBoX8Y_4rL0Vkj6ibnS6h71Grbik0y4PIQVzLfAbqQPi5Ll8mmgg8pMunKvbZq6hJOX1QHmr5r26EwYkgXl7uSFNmMFVgtBYnv45zgwUuTKu25OQJtFKHgvovBnfVf2O6j9FOjYonoc6aFEaWLhnVW65D3RC2XRIWgPrGQwC3Kzr50v43QxYOpQx6Tx1c/s790-rw-e365/ransomware-attack.jpg)

The threat actor known as **Storm-0249** is likely shifting from its role as an initial access broker to adopt a combination of more advanced tactics like domain spoofing, DLL side-loading, and fileless PowerShell execution to facilitate ransomware attacks.

"These methods allow them to bypass defenses, infiltrate networks, maintain persistence, and operate undetected, raising serious concerns for security teams," ReliaQuest [said](https://reliaquest.com/blog/threat-spotlight-storm-0249-precision-endpoint-exploitation) in a report shared with The Hacker News.

Storm-0249 is the moniker assigned by Microsoft to an initial access broker that has sold footholds into organizations to other cybercrime groups, including ransomware and extortion actors like [Storm-0501](https://thehackernews.com/2024/09/microsoft-identifies-storm-0501-as.html). It was first highlighted by the tech giant in September 2024.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/rat-d)

Then, earlier this year, Microsoft also [revealed](https://thehackernews.com/2025/04/microsoft-warns-of-tax-themed-email.html) details of a phishing campaign mounted by the threat actor that used tax-related themes to target users in the U.S. ahead of the tax filing season and infect them with Latrodectus and the BruteRatel C4 (BRc4) post-exploitation framework.

The end goal of these infections is to [obtain persistent access](https://thehackernews.com/2025/08/storm-0501-exploits-entra-id-to.html) to various enterprise networks and monetize them by selling them to ransomware gangs, providing them with a ready supply of targets, and accelerating the pace of such attacks.

The latest findings from ReliaQuest demonstrate a tactical shift, where Storm-0249 has resorted to using the infamous [ClickFix](https://thehackernews.com/2025/11/new-evalusion-clickfix-campaign.html) social engineering tactic to trick prospective targets into running malicious commands via the Windows Run dialog under the pretext of resolving a technical issue.

In this case, the command copied and executed leverages the legitimate "curl.exe" to fetch a PowerShell script from a URL that mimics a Microsoft domain to give victims a false sense of trust ("sgcipl[.]com/us.microsoft.com/bdo/") and execute it in a fileless manner via PowerShell.

This, in turn, results in the execution of a malicious MSI package with SYSTEM privileges, which drops a trojanized DLL associated with SentinelOne's endpoint security solution ("SentinelAgentCore.dll") into the user's AppData folder along with the legitimate "SentinelAgentWorker.exe" executable.

In doing so, the idea is to sideload the rogue DLL when the "SentinelAgentWorker.exe" process is launched, thereby allowing the activity to stay undetected. The DLL then establishes encrypted communication with a command-and-control (C2) server.

Storm-0249 has also been observed making use of legitimate Windows administrative utilities like reg.exe and findstr.exe to extract unique system identifiers like MachineGuid to lay the groundwork for follow-on ransomware attacks. The use of living-off-the-land (LotL) tactics, coupled with the fact that these commands are run under the trusted "SentinelAgentWorker.exe" process, means the activity is unlikely to raise any red flags.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zscaler-ai-event-d)

The findings indicate a departure from mass phishing campaigns to precision attacks that weaponize the trust associated with signed processes for added stealth.

"This isn't just generic reconnaissance – it's preparation for ransomware affiliates," ReliaQuest said. "Ransomware groups like LockBit and ALPHV use MachineGuid to bind encryption keys to individual victim systems."

"By tying encryption keys to MachineGuid, attackers ensure that even if defenders capture the ransomware binary or attempt to reverse-engineer the encryption algorithm, they cannot decrypt files without the attacker-controlled key."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[DLL Sideloading](https://thehackernews.com/search/label/DLL%20Sideloading)[endpoint security](https://thehackernews.com/search/label/endpoint%20security)[Initial Access Broker](https://thehackernews.com/search/label/Initial%20Access%20Broker)[Phishing](https://thehackernews.com/search/label/Phishing)[powershell](https://thehackernews.com/search/label/powershell)[ransomware](https://thehackernews.com/search/label/ransomware)[social engineering](https://thehackernews.com/search/label/social%20engineering)

Trending News

[![ThreatsDay Bulletin: Wi-Fi Hac...