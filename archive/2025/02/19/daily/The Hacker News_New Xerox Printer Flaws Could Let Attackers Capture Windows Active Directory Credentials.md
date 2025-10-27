---
title: New Xerox Printer Flaws Could Let Attackers Capture Windows Active Directory Credentials
url: https://thehackernews.com/2025/02/new-xerox-printer-flaws-could-let.html
source: The Hacker News
date: 2025-02-19
fetch_date: 2025-10-06T20:49:36.206964
---

# New Xerox Printer Flaws Could Let Attackers Capture Windows Active Directory Credentials

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

# [New Xerox Printer Flaws Could Let Attackers Capture Windows Active Directory Credentials](https://thehackernews.com/2025/02/new-xerox-printer-flaws-could-let.html)

**Feb 18, 2025**Ravie LakshmananVulnerability / Enterprise Security

[![Windows Active Directory Credentials](data:image/png;base64... "Windows Active Directory Credentials")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhmph4JRPwI9qWQf9XCrJFyychoWf_feTg9HWYMKtabRnbcFRw2t-xJ6HaVyJJ-SGbQOO0hP7bQCUaFVrTh8b6fUFO5FveesZ5Lp9KyK_LJOiGtc6fPb-4ZEYSw1uSc5Sg9NnDB6RQ6hRD7xvU-Ad6J5m-k6Sz0B-ZrtDPosbMNVuAlYMQBcw9jaRe93GUs/s790-rw-e365/printers.png)

Security vulnerabilities have been disclosed in Xerox VersaLink C7025 Multifunction printers (MFPs) that could allow attackers to capture authentication credentials via pass-back attacks via Lightweight Directory Access Protocol ([LDAP](https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol)) and SMB/FTP services.

"This pass-back style attack leverages a vulnerability that allows a malicious actor to alter the MFP's configuration and cause the MFP device to send authentication credentials back to the malicious actor," Rapid7 security researcher Deral Heiland [said](https://www.rapid7.com/blog/post/2025/02/14/xerox-versalink-c7025-multifunction-printer-pass-back-attack-vulnerabilities-fixed/).

"If a malicious actor can successfully leverage these issues, it would allow them to capture credentials for Windows Active Directory. This means they could then move laterally within an organization's environment and compromise other critical Windows servers and file systems."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The identified vulnerabilities, which affect firmware versions 57.69.91 and earlier, are listed below -

* **[CVE-2024-12510](https://nvd.nist.gov/vuln/detail/CVE-2024-12510)** (CVSS score: 6.7) - Pass-back attack via LDAP
* **[CVE-2024-12511](https://nvd.nist.gov/vuln/detail/CVE-2024-12511)** (CVSS score: 7.6) - Pass-back attack via user's address book

Successful exploitation of CVE-2024-12510 could allow authentication information to be redirected to a rogue server, potentially exposing credentials. This, however, requires an attacker to gain access to the LDAP configuration page and that LDAP is used for authentication.

CVE-2024-12511, likewise, allows a malicious actor to gain access to the user address book configuration to modify the SMB or FTP server's IP address and make it point to a host under their control, causing SMB or FTP authentication credentials to be captured during file scan operations.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgu6u94jLBs7XKe9q12nHkLf2DDwpzc5Iq2mgc8MMHvRwCiy-eh_hRW3rdv79393utMO0H7kaY7sCq9ti-233PIS3WaQ5xOdTr_pSXYA7nPuVEA5SirnT94xactDSI4OXGtJLR79MHSycMEijJstR2thwWIwwpYT7RJrgzP3HPg3nrH76Q0Xuo26OPaFn9e/s790-rw-e365/exploit.png)

"For this attack to be successful, the attacker requires an SMB or FTP scan function to be configured within the user's address book, as well as physical access to the printer console or access to remote-control console via the web interface," Heiland noted. "This may require admin access unless user level access to the remote-control console has been enabled."

Following responsible disclosure on March 26, 2024, the vulnerabilities were addressed as part of [Service Pack 57.75.53](https://www.support.xerox.com/en-us/product/versalink-c7020-c7025-c7030/content/169633) released late last month for VersaLink C7020, 7025, and 7030 series printers.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

If immediate patching is not an option, users are recommended to set a complex password for the admin account, avoid using Windows authentication accounts that have elevated privileges, and disable the remote-control console for unauthenticated users.

The development comes as Specular founder and CEO Peyton Smith detailed an unauthenticated SQL injection vulnerability affecting a widely deployed healthcare software named [HealthStream MSOW](https://www.healthstream.com/solution/credentialing/provider-credentialing/msow) (CVE-2024-56735) that could lead to a full database compromise, allowing threat actors to access sensitive data of 23 healthcare organizations from the public internet.

The company said it identified 50 instances of internet-exposed MSOW instances, of which 23 are susceptible to security shortcomings.

The vulnerability could allow "the entire database could be returned in-band, meaning an attacker could retrieve the plaintext database contents in a HTTP response from a crafted SQL injection HTTP payload," Smith [said](https://www.specular.ai/blog/breaching-the-perimeter-using-ai-to-compromise-23-healthcare-organizations).

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

[Authentication](https://thehackernews.com/search/label/Authentication)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data breach](https://thehackernews.com/search/label/data%20breach)[enterprise security](https://thehackernews.com/search/label/enterprise%20security)[Healthcare Security](https://thehack...