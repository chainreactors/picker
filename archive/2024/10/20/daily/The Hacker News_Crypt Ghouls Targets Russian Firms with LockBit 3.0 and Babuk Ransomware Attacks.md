---
title: Crypt Ghouls Targets Russian Firms with LockBit 3.0 and Babuk Ransomware Attacks
url: https://thehackernews.com/2024/10/crypt-ghouls-targets-russian-firms-with.html
source: The Hacker News
date: 2024-10-20
fetch_date: 2025-10-06T18:51:32.370351
---

# Crypt Ghouls Targets Russian Firms with LockBit 3.0 and Babuk Ransomware Attacks

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

# [Crypt Ghouls Targets Russian Firms with LockBit 3.0 and Babuk Ransomware Attacks](https://thehackernews.com/2024/10/crypt-ghouls-targets-russian-firms-with.html)

**Oct 19, 2024**Ravie LakshmananNetwork Security / Data Breach

[![Ransomware Attacks](data:image/png;base64... "Ransomware Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgcRV5GzR0sNMPEMuGzbEMjbxJhqbySnf3Y2FPIWDMDaGY1MCd36oz7kQORebmAFNmB3FRB8C80kcwqLdwqtXeA5gobDOPk8onhse8tsNA4v34jQgHaJtECq1p5Q-iqMaGT-16McWYPcOnAbmTm95v4998N7-cLL0kKFXZh1fc-Dru7N-f7j-cN75ceQ7vV/s790-rw-e365/russia.png)

A nascent threat actor known as **Crypt Ghouls** has been linked to a set of cyber attacks targeting Russian businesses and government agencies with ransomware with the twin goals of disrupting business operations and financial gain.

"The group under review has a toolkit that includes utilities such as Mimikatz, XenAllPasswordPro, PingCastle, Localtonet, resocks, AnyDesk, PsExec, and others," Kaspersky [said](https://securelist.com/crypt-ghouls-hacktivists-tools-overlap-analysis/114217/). "As the final payload, the group used the well-known ransomware LockBit 3.0 and Babuk."

Victims of the malicious attacks span government agencies, as well as mining, energy, finance, and retail companies located in Russia.

The Russian cybersecurity vendor said it was able to pinpoint the initial intrusion vector in only two instances, with the threat actors leveraging a contractor's login credentials to connect to the internal systems via VPN.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The VPN connections are said to have originated from IP addresses associated with a Russian hosting provider's network and a contractor's network, indicating an attempt to fly under the radar by weaponizing trusted relationships. It's believed that the contractor networks are breached by means of VPN services or unpatched security flaws.

The initial access phase is succeeded by the use of NSSM and Localtonet utilities to maintain remote access, with follow-on exploitation facilitated by tools such as follows -

* XenAllPasswordPro to harvest authentication data
* [CobInt](https://thehackernews.com/2024/06/excobalt-cyber-gang-targets-russian.html) backdoor
* Mimikatz to extract victims' credentials
* dumper.ps1 to dump Kerberos tickets from the LSA cache
* MiniDump to extract login credentials from the memory of lsass.exe
* cmd.exe to copy credentials stored in Google Chrome and Microsoft Edge browsers
* PingCastle for network reconnaissance
* [PAExec](https://github.com/poweradminllc/PAExec) to run remote commands
* AnyDesk and [resocks](https://github.com/RedTeamPentesting/resocks) SOCKS5 proxy for remote access

The attacks end with the encryption of system data using publicly available versions of LockBit 3.0 for Windows and Babuk for Linux/ESXi, while also taking steps to encrypt data present in the Recycle Bin to inhibit recovery.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The attackers leave a ransom note with a link containing their ID in the Session messaging service for future contact," Kaspersky said. "They would connect to the ESXi server via SSH, upload Babuk, and initiate the encryption process for the files within the virtual machines."

Crypt Ghouls' choice of tools and infrastructure in these attacks overlaps with similar campaigns conducted by other groups targeting Russia in recent months, including [MorLock](https://thehackernews.com/2024/05/ransomware-attacks-exploit-vmware-esxi.html), [BlackJack, Twelve](https://thehackernews.com/2024/09/hacktivist-group-twelve-targets-russian.html), and [Shedding Zmiy](https://thehackernews.com/2024/06/excobalt-cyber-gang-targets-russian.html) (aka ExCobalt)

"Cybercriminals are leveraging compromised credentials, often belonging to subcontractors, and popular open-source tools," the company said. "The shared toolkit used in attacks on Russia makes it challenging to pinpoint the specific hacktivist groups involved."

"This suggests that the current actors are not only sharing knowledge but also their toolkits. All of this only makes it more difficult to identify specific malicious actors behind the wave of attacks directed at Russian organizations."

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

[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[Cyber Threat](https://thehackernews.com/search/label/Cyber%20Threat)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data breach](https://thehackernews.com/search/label/data%20breach)[network security](https://thehackernews.com/search/label/network%20security)[ransomware](https://thehackernews.com/search/label/ransomware)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defens...