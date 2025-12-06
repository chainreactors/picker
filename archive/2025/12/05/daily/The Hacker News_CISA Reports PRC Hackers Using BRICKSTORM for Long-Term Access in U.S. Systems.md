---
title: CISA Reports PRC Hackers Using BRICKSTORM for Long-Term Access in U.S. Systems
url: https://thehackernews.com/2025/12/cisa-reports-prc-hackers-using.html
source: The Hacker News
date: 2025-12-05
fetch_date: 2025-12-06T03:12:05.647436
---

# CISA Reports PRC Hackers Using BRICKSTORM for Long-Term Access in U.S. Systems

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

# [CISA Reports PRC Hackers Using BRICKSTORM for Long-Term Access in U.S. Systems](https://thehackernews.com/2025/12/cisa-reports-prc-hackers-using.html)

**Dec 05, 2025**Ravie LakshmananNetwork Security / Zero-Day

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjagp4sr3aHhUYdEa6MEO7S5AaVubzpKfuFL9-Zkuv_GjyxT74q_4XA3gAM8xjQdWW8KfgCy2D81j9NoUB0aZI5IK1ciYxf-JFvZiBFVyEsXaxXIuh2mMbqyPGLJcdZxO-XpdxaF4-lbCzdl9f6xgxJABV4uBvxytMfCwLUmEHmyPfhkGF4z2BZiMNhYlbx/s790-rw-e365/chinese-hackers.jpg)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Thursday released details of a backdoor named **BRICKSTORM** that has been put to use by state-sponsored threat actors from the People's Republic of China (PRC) to maintain long-term persistence on compromised systems.

"BRICKSTORM is a sophisticated backdoor for VMware vSphere and Windows environments," the agency [said](https://www.cisa.gov/news-events/alerts/2025/12/04/prc-state-sponsored-actors-use-brickstorm-malware-across-public-sector-and-information-technology). "BRICKSTORM enables cyber threat actors to maintain stealthy access and provides capabilities for initiation, persistence, and secure command-and-control."

Written in Golang, the custom implant essentially gives bad actors interactive shell access on the system and allows them to browse, upload, download, create, delete, and manipulate files

The malware, mainly used in attacks targeting governments and information technology (IT) sectors, also supports multiple protocols, such as HTTPS, WebSockets, and nested Transport Layer Security (TLS), for command-and-control (C2), DNS-over-HTTPS (DoH) to conceal communications and blend in with normal traffic, and can act as a SOCKS proxy to facilitate lateral movement.

The cybersecurity agency did not disclose how many government agencies have been impacted or what type of data was stolen. The activity represents an ongoing tactical evolution of Chinese hacking groups, which have continued to strike edge network devices to breach networks and cloud infrastructures.

In a [statement](https://www.reuters.com/world/china/chinese-linked-hackers-use-back-door-potential-sabotage-us-canada-say-2025-12-04/) shared with Reuters, a spokesperson for the Chinese embassy in Washington rejected the accusations, stating the Chinese government does not "encourage, support, or connive at cyber attacks."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/filefix-d)

BRICKSTORM was [first documented](https://thehackernews.com/2024/05/hackers-created-rogue-vms-to-evade.html) by Google Mandiant in 2024 in attacks linked to the zero-day exploitation of Ivanti Connect Secure zero-day vulnerabilities (CVE-2023-46805 and CVE-2024-21887). The use of the malware has been attributed to two clusters tracked as UNC5221 and a new China-nexus adversary tracked by CrowdStrike as Warp Panda.

Earlier this September, Mandiant and Google Threat Intelligence Group (GTIG) [said](https://thehackernews.com/2025/09/unc5221-uses-brickstorm-backdoor-to.html) they observed legal services, software-as-a-service (SaaS) providers, Business Process Outsourcers (BPOs), and technology sectors in the U.S. being targeted by UNC5221 and other closely related threat activity clusters to deliver the malware.

A key feature of the malware, per CISA, is its ability to automatically reinstall or restart itself by means of a self-monitoring function that allows its continued operation in the face of any potential disruption.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4lM7E1XO-g3uxJ4owPCEjjK83Sx7Qc68U5kuFIDds7QFhd8iSvqZtGQokxxp7b8ChxEqfcEUUG7mJTYI97KkeeRZDoybQjS5ABcN5g8iA3hOe1KTyG5bXdVR3H9d3Qgvd3C4yYAleOzDWJfYJaPyG32en1M6k01OEprI5vnreDYmrJfinZhC0W8FyCg6M/s2600/brick-1.png)

In one case [detected](https://www.cisa.gov/news-events/analysis-reports/ar25-338a) in April 2024, the threat actors are said to have accessed a web server inside an organization's demilitarized zone (DMZ) using a web shell, before moving laterally to an internal VMware vCenter server and implanting BRICKSTORM. However, many details remain unknown, including the initial access vector used in the attack and when the web shell was deployed.

The attackers have also been found to leverage the access to obtain service account credentials and laterally move to a domain controller in the DMZ using Remote Desktop Protocol ([RDP](https://learn.microsoft.com/en-us/troubleshoot/windows-server/remote/understanding-remote-desktop-protocol)) so as to capture Active Directory information. Over the course of the intrusion, the threat actors managed to get the credentials for a managed service provider (MSP) account, which was then used to jump from the internal domain controller to the VMware vCenter server.

CISA said the actors also moved laterally from the web server using Server Message Block ([SMB](https://en.wikipedia.org/wiki/Server_Message_Block)) to two jump servers and an Active Directory Federation Services ([ADFS](https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/ad-fs-overview)) server, exfiltrating cryptographic keys from the latter. The access to vCenter ultimately enabled the adversary to deploy BRICKSTORM after elevating their privileges.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHCsVikDM_aHySGVE3_thutg3TiTucjrrKtItAPj-tbQuHtUZWbjnOtsYOv0PGNI57kfShS2CEf4TdJDZ7g_aJafPZnycztKKmOaEp53UhhWbQKGcR90PcgXiOteRQLwq9YTFElD13bulv-I5nPAD_DjNqzkQ-iIcL9Y8VvwSQtGTTCmvp2J52GAC-wZfM/s2600/brick-2.png)

"BRICKSTORM uses custom handlers to set up a SOCKS proxy, create a web server on the compromised system, and execute commands on the compromised system," it said, adding some artifacts are "designed to work in virtualized environments, using a virtual socket ([VSOCK](https://man7.org/linux/man-pages/man7/vsock.7.html)) interface to enable inter-VM [virtual machine] communication, facilitate data exfiltration, and maintain p...