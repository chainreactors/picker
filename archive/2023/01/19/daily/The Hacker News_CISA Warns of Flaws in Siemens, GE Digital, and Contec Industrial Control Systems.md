---
title: CISA Warns of Flaws in Siemens, GE Digital, and Contec Industrial Control Systems
url: https://thehackernews.com/2023/01/cisa-warns-of-flaws-in-siemens-ge.html
source: The Hacker News
date: 2023-01-19
fetch_date: 2025-10-04T04:20:37.412342
---

# CISA Warns of Flaws in Siemens, GE Digital, and Contec Industrial Control Systems

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

# [CISA Warns of Flaws in Siemens, GE Digital, and Contec Industrial Control Systems](https://thehackernews.com/2023/01/cisa-warns-of-flaws-in-siemens-ge.html)

**Jan 18, 2023**Ravie LakshmananICS/SCADA Security

[![Industrial Control Systems](data:image/png;base64... "Industrial Control Systems")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEierrm8j0__q82h_hgx3sbAaoZuMNLk6fZINh8FJSzWV03r-BmvArjLkwsuLUh26rPv6-Q97vof136JIHaA-K8nAVF23uZdXMJbAKB3t9zVCcjlFTmlAqaiRtSvAMgLqjOEdlyS1ZDiLIILHdBFoIJchD2EXeVYNH1QBL-_GM3d0EnwqT5b3bsXBjYH/s790-rw-e365/ics.png)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has [published](https://www.cisa.gov/uscert/ncas/current-activity/2023/01/17/cisa-releases-four-industrial-control-systems-advisories) four Industrial Control Systems (ICS) advisories, calling out several security flaws affecting products from Siemens, GE Digital, and Contec.

The most critical of the issues have been identified in Siemens SINEC INS that could lead to remote code execution via a path traversal flaw ([CVE-2022-45092](https://nvd.nist.gov/vuln/detail/CVE-2022-45092), CVSS score: 9.9) and command injection ([CVE-2022-2068](https://nvd.nist.gov/vuln/detail/CVE-2022-2068), CVSS score: 9.8).

Also patched by Siemens is an authentication bypass vulnerability in llhttp parser ([CVE-2022-35256](https://nvd.nist.gov/vuln/detail/CVE-2022-35256), CVSS score: 9.8) as well as an out-of-bounds write bug in the OpenSSL library ([CVE-2022-2274](https://thehackernews.com/2022/07/openssl-releases-patch-for-high.html), CVSS score: 9.8) that could be exploited to trigger remote code execution.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The German automation company, in December 2022, [released](https://support.industry.siemens.com/cs/document/109815432/sinec-ins-v1-0-service-pack-2-update-1-software-%28incl-10-node-demo%29-download?dti=0&lc=en-WW) Service Pack 2 Update 1 software to mitigate the flaws.

Separately, a critical flaw has also been revealed in GE Digital's Proficy Historian solution that could result in code execution regardless of authentication status. The issue, tracked as CVE-2022-46732 (CVSS score: 9.8), impacts Proficy Historian versions 7.0 and higher, and has been remediated in [Proficy Historian 2023](https://www.ge.com/digital/applications/proficy-historian).

"An attacker can take advantage of this fact and bypass the historian authentication by impersonating a local service," Uri Katz, security researcher at industrial security firm Claroty, [said](https://claroty.com/team82/research/hacking-ics-historians-the-pivot-point-from-it-to-ot). "This allows remote attackers the ability to log in to any GE Proficy Historian server and force it to perform unauthorized actions."

CISA also updated an ICS advisory that was published last month, detailing a critical command injection vulnerability in Contec CONPROSYS HMI System (CVE-2022-44456, CVSS score: 10.0) that could permit a remote attacker to send specially crafted requests to execute arbitrary commands.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

While this shortcoming was patched by Contec in version 3.4.5, the software has since been found to be vulnerable to four additional defects that could lead to information disclosure and unauthorized access.

Users of CONPROSYS HMI System are recommended to update to version 3.5.0 or later, in addition to taking steps to minimize network exposure and isolate such devices from business networks.

The advisories come less than a week after CISA released [12 such alerts](https://thehackernews.com/2023/01/cisa-warns-for-flaws-affecting.html) warning of critical flaws impacting software from Sewio, InHand Networks, Sauter Controls, and Siemens.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[industrial control system](https://thehackernews.com/search/label/industrial%20control%20system)[OpenSSL](https://thehackernews.com/search/label/OpenSSL)[SCADA Security](https://thehackernews.com/search/label/SCADA%20Security)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal E...