---
title: 900+ Sangoma FreePBX Instances Compromised in Ongoing Web Shell Attacks
url: https://thehackernews.com/2026/02/900-sangoma-freepbx-instances.html
source: The Hacker News
date: 2026-02-27
fetch_date: 2026-02-28T04:01:40.256129
---

# 900+ Sangoma FreePBX Instances Compromised in Ongoing Web Shell Attacks

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [900+ Sangoma FreePBX Instances Compromised in Ongoing Web Shell Attacks](https://thehackernews.com/2026/02/900-sangoma-freepbx-instances.html)

**Ravie Lakshmanan**Feb 27, 2026Network Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVfnqoWodxrya2TOd7lDLrZ23Bvo_FZhrnRLTnOO-Y4zvouKylIpkT7KE_LKo8lQGBCwMo3GCldGiyqSJobUKHLxmKx6hja0EBG6K3DCtQG-bmDDapu2el8CnQMMs971cJ3dICyw4-T1I8o0W7-XNHKzRBO8U48USZlO8MmtJkKKaOkweEzgKZF2PyaUt9/s1700-e365/freepbx.jpg)

The Shadowserver Foundation has [revealed](https://bsky.app/profile/shadowserver.bsky.social/post/3mfmv4o433k2b) that over 900 Sangoma FreePBX instances still remain infected with web shells as part of attacks that exploited a command injection vulnerability starting in December 2025.

Of these, [401 instances](https://dashboard.shadowserver.org/statistics/combined/tree/?date_range=1&source=compromised_iot&source=compromised_website&source=compromised_website6&tag=freepbx-compromised%2B&data_set=count&scale=log&auto_update=on) are located in the U.S., followed by 51 in Brazil, 43 in Canada, 40 in Germany, and 36 in France.

The non-profit entity said the compromises are likely accomplished via the exploitation of CVE-2025-64328 (CVSS score: 8.6), a high-severity security flaw that could enable post-authentication command injection.

"The impact is that any user with access to the FreePBX Administration panel could leverage this vulnerability to execute arbitrary shell commands on the underlying host," FreePBX [said](https://github.com/FreePBX/security-reporting/security/advisories/GHSA-vm9p-46mv-5xvw) in an advisory for the flaw in November 2025. "An attacker could leverage this to obtain remote access to the system as the asterisk user."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ztw-hands-on-d)

The vulnerability affects FreePBX versions higher than and including 17.0.2.36. It was resolved in version 17.0.3. As mitigations, it's advised to add security controls to ensure that only authorized users have access to the FreePBX Administrator Control Panel (ACP), restrict access from hostile networks to the ACP, and update the filestore module to the latest version.

The vulnerability has since come under active exploitation in the wild, prompting the U.S. Cybersecurity and Infrastructure Security Agency (CISA) to [add](https://thehackernews.com/2026/02/cisa-adds-actively-exploited-solarwinds.html) it to its Known Exploited Vulnerabilities (KEV) catalog earlier this month.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCZYVH4oDJOb75UGx2wygy3c53b0FeqMOgyG6HcTAx8vWRgzzwbZfuv3u11Z9CDM9Wt3LBvFJV_3l0vH32apMmtHtRKUIjhnGvbSbRJMHFWvQnFw_1kEjrkdEb1SgZAiu_KjjgzZO4FiQeSBLFqD9yUyfME22bTdUlj75-uB78VxvDVwSr24h7s5O4yPZb/s1700-e365/shadow.jpg) |
| Source: The Shadowserver Foundation |

In a report published late last month, Fortinet FortiGuard Labs revealed that the threat actor behind the cyber fraud operation codenamed INJ3CTOR3 has been exploiting CVE-2025-64328 starting early December 2025 to deliver a web shell codenamed EncystPHP.

"By leveraging Elastix and FreePBX administrative contexts, the web shell operates with elevated privileges, enabling arbitrary command execution on the compromised host and initiating outbound call activity through the PBX environment," the cybersecurity company noted.

FreePBX users are recommended to update their FreePBX deployments to the latest version as soon as possible to counter active threats.

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

[CISA](https://thehackernews.com/search/label/CISA), [Command Injection](https://thehackernews.com/search/label/Command%20Injection), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [FreePBX](https://thehackernews.com/search/label/FreePBX), [network security](https://thehackernews.com/search/label/network%20security), [Patch Management](https://thehackernews.com/search/label/Patch%20Management), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Shell](https://thehackernews.com/search/label/Web%20Shell)

Trending News

[![Researchers Show Copilot and Grok Can Be Abused as Malware C2 Proxies](data:image/svg+xml;base64... "Researchers Show Copilot and Grok Can Be Abused as Malware C2 Proxies")

Researchers Show Copilot and Grok Can Be Abused as Malware C2 Proxies](https://thehackernews.com/2026/02/researchers-show-copilot-and-grok-can.html)

[![⚡ Weekly Recap: Double-Tap Skimmers, PromptSpy AI, 30Tbps DDoS, Docker Malware and More](data:image/svg+xml;base64... "⚡ Weekly Recap: Double-Tap Skimmers, PromptSpy AI, 30Tbps DDoS, Docker Malware and More")

⚡ Weekly Recap: Double-Tap Skimmers, PromptSpy AI, 30Tbps DDoS, Docker Malware and More](https://thehackernews.com/2026/02/weekly-recap-double-tap-skimmers.html)

[![ThreatsDay Bulletin: Kali Linux + Claude, Chrome Crash Traps, WinRAR Flaws, LockBit and 15+ Stories](data:image/svg+xml;base64... "ThreatsDay Bulletin: Kali Linux + Claude, Chrome Crash Traps, WinRAR Flaws, LockBit and 15+ Stories")

ThreatsDay Bulletin: Kali Li...