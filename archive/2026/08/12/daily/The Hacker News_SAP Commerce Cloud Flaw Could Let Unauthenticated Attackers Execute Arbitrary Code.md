---
title: SAP Commerce Cloud Flaw Could Let Unauthenticated Attackers Execute Arbitrary Code
url: https://thehackernews.com/2026/08/sap-commerce-cloud-flaw-could-let.html
source: The Hacker News
date: 2026-08-12
fetch_date: 2026-08-13T04:05:21.432667
---

# SAP Commerce Cloud Flaw Could Let Unauthenticated Attackers Execute Arbitrary Code

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

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

![cybersecurity](data:image/svg+xml;base64...)

# [SAP Commerce Cloud Flaw Could Let Unauthenticated Attackers Execute Arbitrary Code](https://thehackernews.com/2026/08/sap-commerce-cloud-flaw-could-let.html)

**Ravie Lakshmanan**Aug 12, 2026Enterprise Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbIbhajZdWb8FMAsUCcL8bufmUEbpuTCSFvKhvJgecxUZcO3rH1QV1bVNrOJ1W8oqge3sBIMwmHZxXR9l1PyrOGDEuAZZJkwFBmMlFGWwjU5-3CDmUQsz08HzrZ23kg9HSv3X7MrOryUe-T-PZCmpr8csna-nQcAg-b3RSeWiWsHuaBFAiJmjTrVI5WBQM/s1700-e365/sap.jpg)

SAP has [released patches](https://support.sap.com/en/my-support/knowledge-base/security-notes-news/august-2026.html) to address a maximum-severity security flaw impacting Commerce Cloud (Data Hub Adapter) that could result in arbitrary code execution.

The vulnerability, assigned the CVE identifier **[CVE-2026-58231](https://www.cve.org/CVERecord?id=CVE-2026-58231)**, is rated 10.0 on the CVSS scoring system. It has been described as a case of insufficient authorization checks and input validation.

"SAP Commerce Cloud allows an unauthenticated attacker to abuse a default authentication client and submit specially crafted input to certain functions lacking sufficient validation," according to a description of the flaw on CVE.org.

"Successful exploitation could enable arbitrary code execution and compromise internal components, resulting in high impact on confidentiality, integrity, and availability of the application."

SAP security company Onapsis has [urged](https://onapsis.com/blog/sap-security-patch-day-august-2026/) customers to patch to a fixed Commerce Cloud release and then re-deploy the updated SAP Commerce Cloud version. As a temporary workaround until a fix can be applied, the exposure can be reduced by configuring an IP Filter Set to restrict access to the vulnerable endpoint.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

SAP has also addressed three other critical flaws as part of its August 2026 update -

* **[CVE-2026-44772](https://www.cve.org/CVERecord?id=CVE-2026-44772)** (CVSS score: 9.9) - A code injection vulnerability in Manufacturing Integration and Intelligence
* **[CVE-2026-34265](https://www.cve.org/CVERecord?id=CVE-2026-34265)** (CVSS score: 9.8) - An out-of-bounds write vulnerability in Application Server ABAP for SAP NetWeaver and ABAP Platform that allows an unauthenticated attacker to exploit logical errors in DIAG protocol parsing, resulting in memory corruption. This could be exploited to disclose sensitive system information or crash the system.
* **[CVE-2026-44758](https://www.cve.org/CVERecord?id=CVE-2026-44758)** (CVSS score: 9.1) - A code injection vulnerability in Manufacturing Integration and Intelligence that could allow an attacker with high privileges to execute arbitrary commands on the underlying operating system.

Per Onapsis, CVE-2026-44758 plugs an issue with a servlet component that's susceptible to server-side template injection (SSTI) and server-side request forgery (SSRF), which could pave the way for command execution. The patch released by SAP removes the vulnerable servlet component.

CVE-2026-44772 patches a vulnerable servlet that allows a low-privileged attacker to submit specially crafted input that causes the application to fetch and process attacker-controlled content from an external source, ultimately leading to arbitrary command execution on the underlying host.

"After implementing the patch, customers need to maintain the new system property 'Secure Transformer' with a list of allowed hosts for hosting XSL files," it said. "Only XSL files from these hosts can be consumed by the vulnerable servlet."

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

[Application Security](https://thehackernews.com/search/label/Application%20Security), [Cloud security](https://thehackernews.com/search/label/Cloud%20security), [Code Execution](https://thehackernews.com/search/label/Code%20Execution), [enterprise security](https://thehackernews.com/search/label/enterprise%20security), [Patch Management](https://thehackernews.com/search/label/Patch%20Management), [SAP](https://thehackernews.com/search/label/SAP), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehackernews.com/search/label/Web%20Security)

⚡ Top Stories This Week

[![Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database](data:image/svg+xml;base64... "Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database")

Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database](https://thehackernews.com/2026/07/azure-cosmos-db-flaw-exposed-platform.html)

[![Anthropic Says Claude Mistook the Open Internet for a CTF and Breached Three Organizations](data:image/svg+xml;base64... "Anthropic Says Claude Mistook the Open Internet for a CTF and Breached Three Organizations")

Anthropic Says Claude Mistook the Open Internet for a CTF and Breached Three Organizations](https://thehackernews.com/2026/07/anthropic-says-claude-mistook-open.html)

[![Researchers Report 84 Flaws in 4G and 5G Cores, Including a Session Hijacking Flaw](data:image/svg+xml;base64... "Researchers Report 84 Flaws in 4G and 5G Cores, Including a Session Hijacking Flaw")

Researchers Report 84 Flaws in 4G and 5G Cores, Including a Session Hijacking Flaw](https://thehackernews.com/2026/07/researchers-report-84-flaws-in-4g-and.html)

[![Cheap Android T...