---
title: Major Vulnerabilities Patched in SonicWall, Palo Alto Expedition, and Aviatrix Controllers
url: https://thehackernews.com/2025/01/major-vulnerabilities-patched-in.html
source: The Hacker News
date: 2025-01-10
fetch_date: 2025-10-06T20:12:32.290071
---

# Major Vulnerabilities Patched in SonicWall, Palo Alto Expedition, and Aviatrix Controllers

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

# [Major Vulnerabilities Patched in SonicWall, Palo Alto Expedition, and Aviatrix Controllers](https://thehackernews.com/2025/01/major-vulnerabilities-patched-in.html)

**Jan 09, 2025**Ravie LakshmananVulnerability / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgzJRRhibudM7wrHQoyHhlETY-Uar-Ypo0EOR4fzE_-7e0J3Fe5s-KkXalb-WS2cYotoOg8Fjie2sZJv4CBUEthwuJERHhPdrBo5nhrPx9pcewskBGUT6iDuwaKs5VwiANyXzJ9-m4PCJTil5shXU-mZSrJVrcS5yKrx31YBlXB8yGp-WvuOJQwWzSEqE2l/s790-rw-e365/software-update.jpg)

Palo Alto Networks has released software patches to address several security flaws in its Expedition migration tool, including a high-severity bug that an authenticated attacker could exploit to access sensitive data.

"Multiple vulnerabilities in the Palo Alto Networks Expedition migration tool enable an attacker to read Expedition database contents and arbitrary files, as well as create and delete arbitrary files on the Expedition system," the company [said](https://security.paloaltonetworks.com/PAN-SA-2025-0001) in an advisory.

"These files include information such as usernames, cleartext passwords, device configurations, and device API keys for firewalls running PAN-OS software."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Expedition, a free tool offered by Palo Alto Networks to facilitate migration from other firewall vendors to its own platform, reached end-of-life (EoL) as of December 31, 2024. The list of flaws is as follows -

* **CVE-2025-0103** (CVSS score: 7.8) - An SQL injection vulnerability that enables an authenticated attacker to reveal Expedition database contents, such as password hashes, usernames, device configurations, and device API keys, as well as create and read arbitrary files
* **CVE-2025-0104** (CVSS score: 4.7) - A reflected cross-site scripting (XSS) vulnerability that enables attackers to execute malicious JavaScript code in the context of an authenticated user's browser if that authenticated user clicks a malicious link that allows phishing attacks and could lead to browser-session theft
* **CVE-2025-0105** (CVSS score: 2.7) - An arbitrary file deletion vulnerability that enables an unauthenticated attacker to delete arbitrary files accessible to the www-data user on the host file system
* **CVE-2025-0106** (CVSS score: 2.7) - A wildcard expansion vulnerability that allows an unauthenticated attacker to enumerate files on the host file system
* **CVE-2025-0107 (CVSS score: 4.4)** - An operating system (OS) command injection vulnerability that enables an authenticated attacker to run arbitrary OS commands as the www-data user in Expedition, which results in the disclosure of usernames, cleartext passwords, device configurations, and device API keys for firewalls running PAN-OS software

Palo Alto Networks said the vulnerabilities have been addressed in version 1.2.100 (CVE-2025-0103, CVE-2025-0104, and CVE-2025-0107) and 1.2.101 (CVE-2025-0105 and CVE-2025-0106), and that it does not intend to release any additional updates or security fixes.

As workarounds, it's recommended to ensure that all network access to Expedition is restricted to only authorized users, hosts, and networks, or shut down the service if it's not in use.

### SonicWall Releases SonicOS Patches

The development coincides with SonicWall [shipping patches](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2025-0003) to remediate multiple flaws in SonicOS, two of which could be abused to achieve authentication bypass and privilege escalation, respectively -

* **CVE-2024-53704** (CVSS score: 8.2) - An Improper Authentication vulnerability in the SSLVPN authentication mechanism that allows a remote attacker to bypass authentication.
* **CVE-2024-53706** (CVSS score: 7.8) - A vulnerability in the Gen7 SonicOS Cloud platform NSv (AWS and Azure editions only) that allows a remote authenticated local low-privileged attacker to elevate privileges to root and potentially lead to code execution.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

While there is no evidence that any of the aforementioned vulnerabilities have been exploited in the wild, it's essential that users take steps to apply the latest fixes as soon as possible.

### Critical Flaw in Aviatrix Controller Detailed

The updates also come as Polish cybersecurity company Securing detailed a maximum severity security flaw impacting Aviatrix Controller (CVE-2024-50603, CVSS score: 10.0) that could be exploited to obtain arbitrary code execution. It affects versions 7.x through 7.2.4820.

The flaw, which is rooted in the fact that certain code segments in an API endpoint do not sanitize user-supplied parameters ("list\_flightpath\_destination\_instances" and "flightpath\_connection\_test"), has been addressed in [versions 7.1.4191 or 7.2.4996](https://docs.aviatrix.com/documentation/latest/release-notices/psirt-advisories/psirt-advisories.html?expand=true#remote-code-execution-vulnerability-in-aviatrix-controllers).

"Due to the improper neutralization of special elements used in an OS command, an unauthenticated attacker is able to remotely execute arbitrary code," security researcher Jakub Korepta [said](https://www.securing.pl/en/cve-2024-50603-aviatrix-network-controller-command-injection-vulnerability/).

*(The story was updated after publication on January 15, 2025, to reflect the change in the CVSS score for CVE-2025-0107 from 2.3 to 4.4.)*

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
[**Share on Facebo...