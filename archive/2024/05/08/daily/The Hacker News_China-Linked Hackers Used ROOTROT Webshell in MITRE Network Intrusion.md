---
title: China-Linked Hackers Used ROOTROT Webshell in MITRE Network Intrusion
url: https://thehackernews.com/2024/05/china-linked-hackers-used-rootrot.html
source: The Hacker News
date: 2024-05-08
fetch_date: 2025-10-06T17:19:15.526713
---

# China-Linked Hackers Used ROOTROT Webshell in MITRE Network Intrusion

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [China-Linked Hackers Used ROOTROT Webshell in MITRE Network Intrusion](https://thehackernews.com/2024/05/china-linked-hackers-used-rootrot.html)

**May 07, 2024**Ravie LakshmananVulnerability / Network Security

[![MITRE Network Intrusion](data:image/png;base64... "MITRE Network Intrusion")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQCqny-7V74hcHMCQEb6Y5GH-20vL1Yf6vXr8AAcEPKxNs2Nor81d5b2W8li3bilH2155zUVFb9dLWwGvi0loxzwJUmDn81Y59iFyx6lP5gfdrbmV4F46BcA5UBuZVVcVMIedGFpAqPw1aCUxcwS5rmMaHxP6PJv8sJEJjVKNMsBjPdhzazE2anizXUPKD/s790-rw-e365/map.png)

The MITRE Corporation has offered more details into the recently disclosed cyber attack, stating that the first evidence of the intrusion now dates back to December 31, 2023.

The attack, which [came to light last month](https://thehackernews.com/2024/04/mitre-corporation-breached-by-nation.html), singled out MITRE's Networked Experimentation, Research, and Virtualization Environment (NERVE) through the exploitation of two Ivanti Connect Secure zero-day vulnerabilities tracked as CVE-2023–46805 and CVE-2024–21887, respectively.

"The adversary maneuvered within the research network via VMware infrastructure using a compromised administrator account, then employed a combination of backdoors and web shells to maintain persistence and harvest credentials," MITRE [said](https://medium.com/mitre-engenuity/technical-deep-dive-understanding-the-anatomy-of-a-cyber-intrusion-080bddc679f3).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

While the organization had previously disclosed that the attackers performed reconnaissance of its networks starting in January 2024, the latest technical deep dive puts the earliest signs of compromise in late December 2023, with the adversary dropping a Perl-based web shell called [ROOTROT](https://thehackernews.com/2024/04/researchers-identify-multiple-china.html) for initial access.

ROOTROT, per Google-owned Mandiant, is embedded into a legitimate Connect Secure .ttc file located at "/data/runtime/tmp/tt/setcookie.thtml.ttc" and is the handiwork of a China-nexus cyber espionage cluster dubbed UNC5221, which is also linked to other web shells such as BUSHWALK, CHAINLINE, FRAMESTING, and LIGHTWIRE.

Following the web shell deployment, the threat actor profiled the NERVE environment and established communication with multiple ESXi hosts, ultimately establishing control over MITRE's VMware infrastructure and dropping a Golang backdoor called BRICKSTORM and a previously undocumented web shell referred to as BEEFLUSH.

"These actions established persistent access and allowed the adversary to execute arbitrary commands and communicate with command-and-control servers," MITRE researcher Lex Crumpton explained. "The adversary utilized techniques such as SSH manipulation and execution of suspicious scripts to maintain control over the compromised systems."

Further analysis has determined that the threat actor also deployed another web shell known as [WIREFIRE](https://thehackernews.com/2024/01/nation-state-actors-weaponize-ivanti.html) (aka GIFTEDVISITOR) a day after the public disclosure of the twin flaws on January 11, 2024, to facilitate covert communication and data exfiltration.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Besides using the [BUSHWALK](https://thehackernews.com/2024/02/warning-new-malware-emerges-in-attacks.html) web shell for transmitting data from the NERVE network to command-and-control infrastructure on January 19, 2024, the adversary is said to have attempted lateral movement and maintained persistence within NERVE from February to mid-March.

"The adversary executed a ping command for one of MITRE's corporate domain controllers and attempted to move laterally into MITRE systems but was unsuccessful," Crumpton said.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Ivanti](https://thehackernews.com/search/label/Ivanti)[MITRE](https://thehackernews.com/search/label/MITRE)[network security](https://thehackernews.com/search/label/network%20security)[Reconnaissance](https://thehackernews.com/search/label/Reconnaissance)[vmware](https://thehackernews.com/search/label/vmware)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[Web Shell](https://thehackernews.com/search/label/Web%20Shell)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in R...