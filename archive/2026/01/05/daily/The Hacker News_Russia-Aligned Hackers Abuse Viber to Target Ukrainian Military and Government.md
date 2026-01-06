---
title: Russia-Aligned Hackers Abuse Viber to Target Ukrainian Military and Government
url: https://thehackernews.com/2026/01/russia-aligned-hackers-abuse-viber-to.html
source: The Hacker News
date: 2026-01-05
fetch_date: 2026-01-06T03:28:09.263057
---

# Russia-Aligned Hackers Abuse Viber to Target Ukrainian Military and Government

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

# [Russia-Aligned Hackers Abuse Viber to Target Ukrainian Military and Government](https://thehackernews.com/2026/01/russia-aligned-hackers-abuse-viber-to.html)

**Jan 05, 2026**Ravie LakshmananCyber Espionage / Windows Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZrzpzm3kgY91cQhzyrpbgxomzkri4gsv_GeaFpDMVVj3faZ9_CQAm2c5DvxBbZ15708nW3eJrmSxS9AZBABszXboS-IVyik_4TTrni4xTOJERzoSSF5l7ixY_7n4hIydsBXGozBBS0rF89sIpgxRMHPZbEVe6n2j-nWxP15Y8fsvt7-_KQO-Zjwu_19h2/s790-rw-e365/viber.jpg)

The Russia-aligned threat actor known as **UAC-0184** has been observed targeting Ukrainian military and government entities by leveraging the Viber messaging platform to deliver malicious ZIP archives.

"This organization has continued to conduct high-intensity intelligence gathering activities against Ukrainian military and government departments in 2025," the 360 Threat Intelligence Center [said](https://mp.weixin.qq.com/s?__biz=MzUyMjk4NzExMA==&mid=2247507757&idx=1&sn=cf6b118e88395af45a000aae80811264&poc_token=HNnfW2mjnOhb-9voW7EL-AX6wsrUBqSd4LXEFGMn) in a technical report.

Also tracked as Hive0156, the hacking group is [primarily known](https://thehackernews.com/2024/02/new-idat-loader-attacks-using.html) for leveraging war-themed lures in [phishing emails](https://thehackernews.com/2024/04/ukraine-targeted-in-cyberattack.html) to deliver [Hijack Loader](https://thehackernews.com/2025/07/cyber-espionage-campaign-hits-russian.html) in attacks targeting Ukrainian entities. The malware loader subsequently acts as a pathway for Remcos RAT infections.

The threat actor was first documented by CERT-UA in early January 2024. Subsequent attack campaigns have been [found](https://thehackernews.com/2024/10/pro-ukrainian-hackers-strike-russian.html) to leverage messaging apps like Signal and Telegram as a delivery vehicle for malware. The latest findings from the Chinese security vendors point to a further evolution of this tactic.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

The attack chain involves the use of Viber as an initial intrusion vector to distribute malicious ZIP archives containing multiple Windows shortcut (LNK) files disguised as official Microsoft Word and Excel documents to trick recipients into opening them.

The LNK files are designed to serve as a decoy document to the victim to lower their suspicion, while silently executing Hijack Loader in the background by fetching a second ZIP archive ("smoothieks.zip") from a remote server by means of a PowerShell script.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9gknI8gVMdXNYEjuyWUHE258FRPoWEsOCYuWLzAtGom6FQujsU2TXihAKbQytn0vO5uwlFE24PjXnF12VXfWNAkLg9L0urVJa9I8Z225timhG-_Rc5C89Rd4pv8iICplK0tlTil-iqY34yINi1nbnUOYYZxgPggGfDw1N0yLgASh4x-fxrQeCJvzYtviY/s790-rw-e365/powershell.jpg)

The attack reconstructs and deploys Hijack Loader in memory through a multi-stage process that employs techniques like DLL side-loading and module stomping to evade detection by security tools. The loader then scans the environment for installed security software, such as those related to Kaspersky, Avast, BitDefender, AVG, Emsisoft, Webroot, and Microsoft, by calculating the CRC32 hash of the corresponding program.

Besides establishing persistence by means of scheduled tasks, the loader takes steps to subvert static signature detection before covertly executing Remcos RAT by injecting it into "chime.exe." The remote administration tool grants the attackers the ability to manage the endpoint, execute payloads, monitor activities, and steal data.

"Although marketed as legitimate system management software, its powerful intrusive capabilities make it frequently used by various malicious attackers for cyber espionage and data theft activities," the 360 Threat Intelligence Center said. "Through the graphical user interface (GUI) control panel provided by Remcos, attackers can perform batch automated management or precise manual interactive operations on the victim's host."

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

[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[Messaging Apps](https://thehackernews.com/search/label/Messaging%20Apps)[Phishing](https://thehackernews.com/search/label/Phishing)[Remote Access Trojan](https://thehackernews.com/search/label/Remote%20Access%20Trojan)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[windows security](https://thehackernews.com/search/label/windows%20security)

Trending News

[![DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Worldwide](data:image/svg+xml;base64... "DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Worldwide")

DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Worldwide](https://thehackernews.com/2025/12/darkspectre-browser-extension-campaigns.html)

[![CSA Issues Alert on Critical SmarterMail Bug Allowing Remote Code Execution](data:image/s...