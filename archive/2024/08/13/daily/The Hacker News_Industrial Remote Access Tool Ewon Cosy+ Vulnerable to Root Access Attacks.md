---
title: Industrial Remote Access Tool Ewon Cosy+ Vulnerable to Root Access Attacks
url: https://thehackernews.com/2024/08/industrial-remote-access-tool-ewon-cosy.html
source: The Hacker News
date: 2024-08-13
fetch_date: 2025-10-06T18:09:01.852988
---

# Industrial Remote Access Tool Ewon Cosy+ Vulnerable to Root Access Attacks

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

# [Industrial Remote Access Tool Ewon Cosy+ Vulnerable to Root Access Attacks](https://thehackernews.com/2024/08/industrial-remote-access-tool-ewon-cosy.html)

**Aug 12, 2024**Ravie LakshmananOperational Technology / Network Security

[![Industrial Remote Access Tool](data:image/png;base64... "Industrial Remote Access Tool")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh3KGbOxXWZDQzkNs_x6p5DMABHqaFg5OyRAsnnh31alpUrYxxT24vuSP8o1d_ACi7UY2SelmhWn6n7DZNv3kG3CMH8gNjdtfz6TrYYhKXhgkE7Ts208SWiGAPQMiXUy_hy-9wqKAW0lXmn2IXf8X3tye1BbFLHjVRBNSPXGg3dJt83Sgc6u2vti51IC_zH/s790-rw-e365/hacking.png)

Security vulnerabilities have been disclosed in the industrial remote access solution Ewon Cosy+ that could be abused to gain root privileges to the devices and stage follow-on attacks.

The elevated access could then be weaponized to decrypt encrypted firmware files and encrypted data such as passwords in configuration files, and even get correctly signed X.509 VPN certificates for foreign devices to take over their VPN sessions.

"This allows attackers hijacking VPN sessions which results in significant security risks against users of the Cosy+ and the adjacent industrial infrastructure," SySS GmbH security researcher Moritz Abrell [said](https://blog.syss.com/posts/hacking-a-secure-industrial-remote-access-gateway/) in a new analysis.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The findings were [presented](https://defcon.org/html/defcon-32/dc-32-speakers.html#54521) at the DEF CON 32 conference over the weekend. Following responsible disclosure, the issues have been addressed in firmware versions 21.2s10 and 22.1s3 as part of an [advisory](https://hmsnetworks.blob.core.windows.net/nlw/docs/default-source/products/cybersecurity/security-advisory/hms-security-advisory-2024-07-29-001--ewon-several-cosy--vulnerabilities.pdf?sfvrsn=37cea022_7) [PDF] issued by Ewon on July 29, 2024 -

* **CVE-2024-33892** (CVSS score: 7.4) - Information leakage through cookies
* **CVE-2024-33893** (CVSS score: 2.1) - XSS when displaying the logs due to improper input sanitization
* **CVE-2024-33894** (CVSS score: 1.0) - Execution of several processes with elevated privileges
* **CVE-2024-33895** (CVSS score: 4.4) - Usage of a unique key to encrypt the configuration parameters
* **CVE-2024-33896** (CVSS score: 3.3) - Code injection due to improper parameter blacklisting
* **CVE-2024-33897** (CVSS score: N/A) - A compromised devices could be used to request a Certificate Signing Request (CSR) from Talk2m for another device, resulting in an availability issue

Ewon Cosy+'s architecture involves the use of a VPN connection that's routed to a vendor-managed platform called Talk2m via OpenVPN. Technicians can remotely connect to the industrial gateway by means of a VPN relay that occurs through OpenVPN.

The Germany-based pentest company said it was able to uncover an operating system command injection vulnerability and a filter bypass that made it possible to obtain a reverse shell by uploading a specially crafted OpenVPN configuration.

An attacker could have subsequently taken advantage of a persistent cross-site scripting (XSS) vulnerability and the fact that the device stores the Base64-encoded credentials of the current web session in an unprotected cookie-named credentials to gain administrative access and ultimately root it.

[![Industrial Remote Access Tool](data:image/png;base64... "Industrial Remote Access Tool")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiIOqkkbROu5GiGuNMExHPftTn7Q1qfAJLNeR6CXAYu9iA7H-EefvlOxcL2zLTrvCAne8cr4Yf9Xca02t0_IyAvvElw4z4ydH3RL9qjE2B5-fRsj0rS23jn7oE9VDo-xBekjwJKLEU8fSSE4QGrIPGe8-hSgJQXRC7yxZAHnpmMuHeZGzDgeX1gEXcSZiRd/s790-rw-e365/id.png)

"An unauthenticated attacker can gain root access to the Cosy+ by combining the found vulnerabilities and e.g., waiting for an admin user to log in to the device," Abrell said.

The attack chain could then be extended further to set up persistence, access firmware-specific encryption keys, and decrypt the firmware update file. What's more, a hard-coded key stored within the binary for password encryption could be leveraged to extract the secrets.

[![Industrial Remote Access Tool](data:image/png;base64... "Industrial Remote Access Tool")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiyPRr06y1C5wY0LQEwjJmXxwKJ5x7etWaz_QMVAc8LVgGTLG18s_BVmEK4tOVXFk2ccu1aVo9EqOr-jR0TJuy4Og8ZXgOCL0l6NKQCIyp_-5iQ5sDv6u231KNbOrjCh_DLcxnPYwOuKTRHIPWdvUEOcTbMLVSk-SIMQdrh6-1gI_u2rzzfEjnny1yOtHV5/s790-rw-e365/root-chain.png)

"The communication between the Cosy+ and the Talk2m API is done via HTTPS and secured via mutual TLS (mTLS) authentication," Abrell explained. "If a Cosy+ device is assigned to a Talk2m account, the device generates a certificate signing request (CSR) containing its serial number as common name (CN) and sends it to the Talk2m API."

This certificate, which can be accessed via the Talk2m API by the device, is used for OpenVPN authentication. However, SySS found that the sole reliance on the device serial number could be exploited by a threat actor to enroll their own CSR with a serial number if a target device and successfully initiate a VPN session.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The original VPN session will be overwritten, and thus the original device is not accessible anymore," Abrell said. "If Talk2m users connect to the device using the VPN client software Ecatcher, they will be forwarded to the attacker."

"This allows attackers to conduct further attacks against the used client, for example accessing network services such as RDP or SMB of the victim client. The fact that the tunnel connection itself is not restricted favors this attack."

"Since the network communication is forwarded to the attacker, the original network and systems could be imitated in order to intercept the victim's user input such as the uploaded PLC programs or similar."...