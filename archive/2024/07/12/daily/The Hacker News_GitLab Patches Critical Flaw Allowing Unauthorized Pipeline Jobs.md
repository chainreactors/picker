---
title: GitLab Patches Critical Flaw Allowing Unauthorized Pipeline Jobs
url: https://thehackernews.com/2024/07/gitlab-patches-critical-flaw-allowing.html
source: The Hacker News
date: 2024-07-12
fetch_date: 2025-10-06T17:46:35.901861
---

# GitLab Patches Critical Flaw Allowing Unauthorized Pipeline Jobs

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

# [GitLab Patches Critical Flaw Allowing Unauthorized Pipeline Jobs](https://thehackernews.com/2024/07/gitlab-patches-critical-flaw-allowing.html)

**Jul 11, 2024**Ravie LakshmananSoftware Security / Vulnerability

[![Software Flaws](data:image/png;base64... "Software Flaws")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHPHR1y16nNoD9WzEJzNMa3M31xoAMnoItAXcwOhdgVeplTv8LbhOhRvWTj-GYi5pFUtrJ6Ho2pShb666-sW4P8we-ojXe40QtV9wH6rg-lgJpdBftSIRGrv01EPD1f3YGxzkOzSZVvC_slR91M6GzSxYAn0rJ7BgFaEAuDHQ70fYSiiG8ftLAJa8sHpah/s790-rw-e365/software-update.png)

GitLab has shipped another round of updates to close out security flaws in its software development platform, including a critical bug that allows an attacker to run pipeline jobs as an arbitrary user.

Tracked as CVE-2024-6385, the vulnerability carries a CVSS score of 9.6 out of a maximum of 10.0.

"An issue was discovered in GitLab CE/EE affecting versions 15.8 prior to 16.11.6, 17.0 prior to 17.0.4, and 17.1 prior to 17.1.2, which allows an attacker to trigger a pipeline as another user under certain circumstances," the company [said](https://about.gitlab.com/releases/2024/07/10/patch-release-gitlab-17-1-2-released/) in a Wednesday advisory.

It's worth noting that the company patched a similar bug late last month ([CVE-2024-5655](https://thehackernews.com/2024/06/gitlab-releases-patch-for-critical-cicd.html), CVSS score: 9.6) that could also be weaponized to run pipelines as other users.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Also addressed by GitLab is a medium-severity issue (CVE-2024-5257, CVSS score: 4.9) that allows a Developer user with admin\_compliance\_framework permissions to modify the URL for a group namespace.

All the security shortcomings have been fixed in GitLab Community Edition (CE) and Enterprise Edition (EE) versions 17.1.2, 17.0.4, and 16.11.6.

The disclosure comes as Citrix [released](https://support.citrix.com/article/CTX677998/netscaler-console-agent-and-sdx-security-bulletin-for-cve20246235-and-cve20246236) updates for a critical, improper authentication flaw impacting NetScaler Console (formerly NetScaler ADM), NetScaler SDX, and NetScaler Agent (CVE-2024-6235, CVSS score: 9.4) that could result in information disclosure.

Patches have also also released by Broadcom for two medium-severity injection vulnerabilities in [VMware Cloud Director](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/security-advisories/0/24557) (CVE-2024-22277, CVSS score: 6.4) and [VMware Aria Automation](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/security-advisories/0/24598) (CVE-2024-22280, CVSS score: 8.5) that could be abused to execute malicious code using specially crafted HTML tags and SQL queries, respectively.

### CISA Releases Bulletins to Tackle Software Flaws

The developments also follow a new bulletin released by the U.S. Cybersecurity and Infrastructure Security Agency (CISA) and the Federal Bureau of Investigation (FBI) urging technology manufacturers to weed out operating system (OS) command injection flaws in software that allow threat actors to remotely execute code on network edge devices.

Such flaws arise when user input is not adequately sanitized and validated when constructing commands to be executed on the underlying operating system, thereby permitting an adversary to smuggle arbitrary commands that can lead to the deployment of malware or information theft.

"OS command injection vulnerabilities have long been preventable by clearly separating user input from the contents of a command," the agencies [said](https://www.cisa.gov/news-events/alerts/2024/07/10/cisa-and-fbi-release-secure-design-alert-eliminating-os-command-injection-vulnerabilities). "Despite this finding, OS command injection vulnerabilities — many of which result from [CWE-78](https://cwe.mitre.org/data/definitions/78.html) — are still a prevalent class of vulnerability."

The alert is the third such caution issued by CISA and FBI since the start of the year. The agencies previously sent out two other alerts about the need for eliminating [SQL injection](https://www.cisa.gov/news-events/alerts/2024/03/25/cisa-and-fbi-release-secure-design-alert-urge-manufacturers-eliminate-sql-injection-vulnerabilities) (SQLi) and [path traversal vulnerabilities](https://www.cisa.gov/news-events/alerts/2024/05/02/cisa-and-fbi-release-secure-design-alert-urge-manufacturers-eliminate-directory-traversal) in March and May 2024.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Last month, CISA, along with cybersecurity agencies from Canada and New Zealand, also released guidance recommending businesses to adopt more robust security solutions — such as [Zero Trust](https://en.wikipedia.org/wiki/Zero_trust_security_model), Secure Service Edge ([SSE](https://www.cloudflare.com/learning/access-management/security-service-edge-sse/)), and Secure Access Service Edge ([SASE](https://en.wikipedia.org/wiki/Secure_access_service_edge)) — that provide greater visibility of network activity.

"By using risk-based access control policies to deliver decisions through policy decision engines, these solutions integrate security and access control, strengthening an organization's usability and security through adaptive policies," the authoring agencies [noted](https://www.cisa.gov/news-events/alerts/2024/06/18/cisa-and-partners-release-guidance-modern-approaches-network-access-security).

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_shar...