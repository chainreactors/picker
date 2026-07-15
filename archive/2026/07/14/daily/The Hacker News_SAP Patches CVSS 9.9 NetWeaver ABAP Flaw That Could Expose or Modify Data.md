---
title: SAP Patches CVSS 9.9 NetWeaver ABAP Flaw That Could Expose or Modify Data
url: https://thehackernews.com/2026/07/sap-patches-cvss-99-netweaver-abap-flaw.html
source: The Hacker News
date: 2026-07-14
fetch_date: 2026-07-15T04:49:59.059932
---

# SAP Patches CVSS 9.9 NetWeaver ABAP Flaw That Could Expose or Modify Data

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [SAP Patches CVSS 9.9 NetWeaver ABAP Flaw That Could Expose or Modify Data](https://thehackernews.com/2026/07/sap-patches-cvss-99-netweaver-abap-flaw.html)

**Ravie Lakshmanan**Jul 14, 2026Enterprise Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9rN4ge3zuUmonccBl2yC_AcOKiCQPKQFAV31BzB3DZk3JO7SxAjx1HdJlg1vBOMEj3cq2Mrg06ZU64I1fdkWCDRBsPhqpuyJwTxjbJHJXmzUoXF8KRDkupk6JxznlI9tjMXwU_hJqh4InVEOsiknPoszVZkQsqWSKfcD5Y90qz63Cv_pOHL8zO4CxGOop/s1700-e365/sap-patch.jpg)

SAP has rolled out updates to address [multiple vulnerabilities](https://support.sap.com/en/my-support/knowledge-base/security-notes-news/july-2026.html) as part of its July 2026 security updates, including a critical flaw in SAP NetWeaver Application Server ABAP.

The vulnerability in question is **[CVE-2026-44747](https://nvd.nist.gov/vuln/detail/CVE-2026-44747)** (CVSS score: 9.9), an out-of-bounds write flaw that allows an authenticated attacker to leverage logical errors in memory management to cause a memory corruption that could lead to unauthorized data access, modification, or system unavailability.

"As a temporary workaround the note proposes to disable all ICF nodes with a specific property in transaction SICF," SAP security firm Onapsis [said](https://onapsis.com/blog/sap-security-patch-day-july-2026/). "Since the workaround will disable opening transactions in SAP GUI for HTML, it is not an option for all customers and it is strongly recommended to install the patching ABAP Kernel version."

Also addressed by SAP are two other critical vulnerabilities -

* **[CVE-2026-27690](https://nvd.nist.gov/vuln/detail/CVE-2026-27690)** (CVSS score: 9.1) - An HTTP request/response smuggling flaw in SAP Approuter deployments in non-Cloud Foundry environments that allows an unauthenticated attacker to send a specially crafted HTTP request that leads to request-response desynchronization and results in the exposure of user responses and triggers denial-of-service (DoS) attacks.
* **[CVE-2026-44761](https://nvd.nist.gov/vuln/detail/CVE-2026-44761)** (CVSS score: 9.1) - A use of default credentials flaw in SAP Commerce Cloud that could retain a sample OAuth 2.0 client with publicly documented sample credentials originating from a sample configuration provided in SAP Help Portal documentation.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

"If left unchanged, an unauthenticated attacker could use these well-known credentials to obtain a valid access token and invoke certain APIs to read and modify data," according to a description of CVE-2026-44761 in the NIST National Vulnerability Database (NVD). "Successful exploitation results in high impact on confidentiality and integrity, with no impact on availability."

Onapsis noted that the vulnerability stems from sample configuration scripts previously provided in the SAP Help Portal. These scripts, originally meant for development and testing, configure OAuth 2.0 clients with hard-coded, well-known credentials.

"Older versions of the documentation did not explicitly warn customers against importing these default settings into production," it noted. "An unauthenticated attacker can leverage these publicly available, default credentials to obtain a valid access token. With this token, they can invoke specific APIs to read and alter system data. Exploitation requires that the customer executed the sample script and retained the resulting OAuth 2.0 client in production without replacing the hard-coded secret."

It's worth noting that customers who removed the sample client or replaced the secret with a strong, unique value are not impacted by the bug. Customers are recommended to audit their production environments for the presence of the affected sample OAuth 2.0 client. If the client exists, it must be removed.

Although there is no evidence of the flaws being exploited in the wild, it's advised to apply the necessary updates for optimal protection.

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

[API Security](https://thehackernews.com/search/label/API%20Security), [Application Security](https://thehackernews.com/search/label/Application%20Security), [Authentication Security](https://thehackernews.com/search/label/Authentication%20Security), [Cloud security](https://thehackernews.com/search/label/Cloud%20security), [data security](https://thehackernews.com/search/label/data%20security), [denial of service](https://thehackernews.com/search/label/denial%20of%20service), [enterprise security](https://thehackernews.com/search/label/enterprise%20security), [SAP](https://thehackernews.com/search/label/SAP), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehackernews.com/search/label/Web%20Security)

⚡ Top Stories This Week

[![16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems](data:image/svg+xml;base64... "16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems")

16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems](https://thehackernews.com/20...