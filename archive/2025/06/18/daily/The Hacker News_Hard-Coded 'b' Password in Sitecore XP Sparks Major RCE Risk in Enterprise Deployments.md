---
title: Hard-Coded 'b' Password in Sitecore XP Sparks Major RCE Risk in Enterprise Deployments
url: https://thehackernews.com/2025/06/hard-coded-b-password-in-sitecore-xp.html
source: The Hacker News
date: 2025-06-18
fetch_date: 2025-10-06T23:00:32.835011
---

# Hard-Coded 'b' Password in Sitecore XP Sparks Major RCE Risk in Enterprise Deployments

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

# [Hard-Coded 'b' Password in Sitecore XP Sparks Major RCE Risk in Enterprise Deployments](https://thehackernews.com/2025/06/hard-coded-b-password-in-sitecore-xp.html)

**Jun 17, 2025**Ravie LakshmananVulnerability / Enterprise Software

[![Password in Sitecore XP](data:image/png;base64... "Password in Sitecore XP")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQFNBHNcSlMBpxA12vCTXNBJJN86l3uyo0ZubB4VorhsxhbPwZwh6ayl7eppYu8F62R0rcqhQAn6LvQQ-DHBfoRuMLV4iGGQ-jU3Mn-cg9RmeEdQbJKre6e_Gx5X8rvc7uieBXmIXFYGuDSo5PsWn-c8mmQ4rGOJIrHUbxaYGwP3d5xVaqFeTOxpDxNxrH/s790-rw-e365/password.jpg)

Cybersecurity researchers have disclosed three security flaws in the popular Sitecore Experience Platform (XP) that could be chained to achieve pre-authenticated remote code execution.

Sitecore Experience Platform is an [enterprise-oriented software](https://www.sitecore.com/products/experience-platform) that provides users with tools for content management, digital marketing, and analytics and reports.

The list of [vulnerabilities](https://support.sitecore.com/kb?id=kb_article_view&sysparm_article=KB1003667) is as follows -

* [**CVE-2025-34509**](https://nvd.nist.gov/vuln/detail/CVE-2025-34509) (CVSS score: 8.2) - Use of hard-coded credentials
* [**CVE-2025-34510**](https://nvd.nist.gov/vuln/detail/CVE-2025-34510) (CVSS score: 8.8) - Post-authenticated remote code execution via path traversal
* [**CVE-2025-34511**](https://nvd.nist.gov/vuln/detail/CVE-2025-34511) (CVSS score: 8.8) - Post-authenticated remote code execution via Sitecore PowerShell Extension

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

watchTowr Labs researcher Piotr Bazydlo said the [default user account](https://doc.sitecore.com/xp/en/developers/latest/platform-administration-and-architecture/the-user-accounts.html) "sitecore\ServicesAPI" has a single-character password that's hard-coded to "**b**." In its documentation, Sitecore advises customers against changing default user account credentials.

While the user has no roles and permissions assigned in Sitecore, the attack surface management firm found that the credentials could be alternately used against the "/sitecore/admin" API endpoint to sign in as "sitecore\ServicesAPI" and obtain a valid session cookie for the user.

"While we can't access 'Sitecore Applications' (where a significant portion of functionality is defined) as the ServicesAPI has no roles assigned, we can still: (1) Access a number of APIs, and (2) Pass through IIS authorization rules and directly access some endpoints," Bazydlo [explained](https://labs.watchtowr.com/is-b-for-backdoor-pre-auth-rce-chain-in-sitecore-experience-platform).

This, in turn, opens the door to remote code execution via a [zip slip vulnerability](https://thehackernews.com/2023/10/openrefines-zip-slip-vulnerability.html) that makes it possible to upload a specially crafted ZIP file via the "/sitecore/shell/Applications/Dialogs/Upload/Upload2.aspx" endpoint and causes the archive's contents (e.g., a web shell) to be written to the webroot directory.

The entire sequence of actions is listed below -

* Authenticate as the "sitecore\ServicesAPI" user
* Access Upload2.aspx
* Upload a ZIP file, which contains a web shell called /\/../<web\_shell>
* When prompted, check the Unzip option and complete the upload
* Access the web shell

The third vulnerability has to do with an unrestricted file upload flaw in PowerShell Extensions that can also be exploited as the "sitecore\ServicesAPI" user to achieve remote code execution through the "/sitecore%20modules/Shell/PowerShell/UploadFile/PowerShellUploadFile2.aspx" endpoint.

watchTowr pointed out that the hard-coded password originates from within the Sitecore installer that imports a pre-configured user database with the ServicesAPI password set to "b." This change, the company said, went into effect starting version 10.1.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This also means that the exploit chain only works if users have installed Sitecore using installers for versions ≥ 10.1. Users are likely not impacted if they were previously running a version prior to 10.1 and then upgraded to a newer vulnerable version, assuming the old database is being migrated, and not the database embedded within the installation package.

With previously disclosed flaws in Sitecore XP coming under active exploitation in the wild ([CVE-2019-9874 and CVE-2019-9875](https://thehackernews.com/2025/03/cisa-flags-two-six-year-old-sitecore.html)), it's essential that users apply the latest patches, if not already, to safeguard against potential cyber threats.

"By default, recent versions of Sitecore shipped with a user that had a hard-coded password of 'b.' It's 2025, and we can't believe we still have to say this, but that's very bad," Benjamin Harris, CEO and founder of watchTowr, told The Hacker News in a statement.

"Sitecore is deployed across thousands of environments, including banks, airlines, and global enterprises – so the blast radius here is massive. And no, this isn't theoretical: we've run the full chain, end-to-end. If you're running Sitecore, it doesn't get worse than this – rotate creds and patch immediately before attackers inevitably reverse engineer the fix."

### Update

When reached for comment, a Sitecore spokesperson shared the following statement with The Hacker News: "We are aware of the recent report from watchTowr identifying several vulnerabilities in our software. We have actively collaborated with them to address the issue and have published a [Knowledge Base article](https://support.sitecore.com/kb?id=kb_article_view&sysparm_article=KB1003667) with details of patches and steps to remediate."

The company also pointed out it has [remediated](https://support.sitecore.com/kb?id=kb_article_view&sysparm_article=KB1003535) a previous finding from watchTowr in February 2025 ([CVE-2025-27218](https://nvd.nist.gov/vuln/detail/CVE-202...