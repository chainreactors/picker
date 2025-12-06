---
title: JPCERT Confirms Active Command Injection Attacks on Array AG Gateways
url: https://thehackernews.com/2025/12/jpcert-confirms-active-command.html
source: The Hacker News
date: 2025-12-05
fetch_date: 2025-12-06T03:12:05.784673
---

# JPCERT Confirms Active Command Injection Attacks on Array AG Gateways

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

# [JPCERT Confirms Active Command Injection Attacks on Array AG Gateways](https://thehackernews.com/2025/12/jpcert-confirms-active-command.html)

**Dec 05, 2025**Ravie LakshmananVulnerability / Network Security

[![Command Injection Attacks on Array AG Gateways](data:image/png;base64... "Command Injection Attacks on Array AG Gateways")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEijkDT1pB32P4Aj-XUQjHXzXUeKtUjJ6Jsm66Ap9f1RNJkQpMsAiEtkVJgUqHHJzcHyLEeCrzIqcehBy5SXX4eSdN4LaFYAB7SR-YflLdNG2YyuVotys9i1HpheYNeAO6PcAicSsLYa-TGxgOnmdR_JzRg1HvQwTfoxA8qkzwTF-B9UScG957OkFBdxnc1B/s790-rw-e365/array.jpg)

A command injection vulnerability in Array Networks AG Series secure access gateways has been exploited in the wild since August 2025, according to an alert issued by JPCERT/CC this week.

The vulnerability, which does not have a CVE identifier, was addressed by the company on May 11, 2025. It's rooted in Array's DesktopDirect, a remote desktop access solution that allows users to securely access their work computers from any location.

"Exploitation of this vulnerability could allow attackers to execute arbitrary commands," JPCERT/CC [said](https://www.jpcert.or.jp/at/2025/at250024.html). "This vulnerability affects systems where the 'DesktopDirect' feature, which provides remote desktop access, is enabled."

The agency said it has confirmed incidents in Japan that have exploited the shortcoming after August 2025 to drop web shells on susceptible devices. The attacks have originated from the IP address "[194.233.100[.]138](https://www.virustotal.com/gui/ip-address/194.233.100.138/details)."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ransomware_dragon_d)

There are currently no details available on the scale of the attacks, weaponizing the flaw, and identity of the threat actors exploiting it.

However, an authentication bypass flaw in the same product ([CVE-2023-28461](https://thehackernews.com/2024/11/cisa-urges-agencies-to-patch-critical.html), CVSS score: 9.8) was exploited last year by a China-linked cyber espionage group dubbed [MirrorFace](https://thehackernews.com/2024/11/china-aligned-mirrorface-hackers-target.html), which has a history of targeting Japanese organizations since at least 2019. That said, there is no evidence to suggest that at this stage the threat actor could be linked to the latest attack spree.

The vulnerability impacts ArrayOS versions 9.4.5.8 and earlier, and has been addressed in version ArrayOS 9.4.5.9. Users are advised to apply the latest updates as soon as possible to mitigate potential threats. In case patching is not an immediate option, it's recommended to disable DesktopDirect services and use URL filtering to deny access to URLs containing a semicolon, JPCERT/CC said.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[network security](https://thehackernews.com/search/label/network%20security)[Patching](https://thehackernews.com/search/label/Patching)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/sentinelone-protect)

Trending News

[![⚡ Weekly Recap: Hot CVEs, npm Worm Returns, Firefox RCE, M365 Email Raid and More](data:image/svg+xml;base64... "⚡ Weekly Recap: Hot CVEs, npm Worm Returns, Firefox RCE, M365 Email Raid and More")

⚡ Weekly Recap: Hot CVEs, npm Worm Returns, Firefox RCE, M365 Email Raid and More](https://thehackernews.com/2025/12/weekly-recap-hot-cves-npm-worm-returns.html)

[![ShadowPad Malware Actively Exploits WSUS Vulnerability for Full System Access](data:image/svg+xml;base64... "ShadowPad Malware Actively Exploits WSUS Vulnerability for Full System Access")

ShadowPad Malware Actively Exploits WSUS Vulnerability for Full System Access](https://thehackernews.com/2025/11/shadowpad-malware-actively-exploits.html)

[![China-Linked APT31 Launches Stealthy Cyberattacks on Russian IT Using Cloud Services](data:image/svg+xml;base64... "China-Linked APT31 Launches Stealthy Cyberattacks on Russian IT Using Cloud Services")

China-Linked APT31 Launches Stealthy Cyberattacks on Russian IT Using Cloud Services](https://thehackernews.com/2025/11/china-linked-apt31-launches-stealthy.html)

[![Second Sha1-Hulud Wave Affects 25,000+ Repositories via npm Preinstall Credential Theft](data:image/svg+xml;base64... "Second Sha1-Hulud Wave Affects 25,000+ Repositories via npm Preinstall Credential Theft")

Second Sha1-Hulud Wave Affects 25,000+ Repositories via npm Preinstall Credential Theft](https://thehackernews.com/2025/11/second-sha1-hulud-wave-affects-25000.html)

[![CISA Warns of Active Spyware Campaigns Hijacking High-Value Signal and WhatsApp Users](data:image/svg+xml;base64... "CISA Warns of Active Spyware Campaigns Hijacking High-Value Signal and WhatsApp Users")

CISA Warns of Active Spyware Campaigns Hijacking High-Value Signal and WhatsApp Users](https://thehackernews.com/2025/11/cisa-warns-of-active-spyware-campaigns.html)

[![ToddyCat’s New Hacking Tools Steal Outlook Emails and Microsoft 365 Access Tokens](data:image/svg+xml;base64... "ToddyCat’s New Hacking To...