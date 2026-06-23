---
title: Researchers Detail DifyTap Flaws in Dify That Could Expose AI Chats Across Tenants
url: https://thehackernews.com/2026/06/researchers-detail-difytap-flaws-in.html
source: The Hacker News
date: 2026-06-22
fetch_date: 2026-06-23T06:08:25.678779
---

# Researchers Detail DifyTap Flaws in Dify That Could Expose AI Chats Across Tenants

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [Researchers Detail DifyTap Flaws in Dify That Could Expose AI Chats Across Tenants](https://thehackernews.com/2026/06/researchers-detail-difytap-flaws-in.html)

**Ravie Lakshmanan**Jun 22, 2026AI Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjrjCumekV1hjkgdgebp4RqfYc_Yt9Swv4lG7ds3XMDHG9f-JxSuJSWY3UcWIoivJoJkJjdlBvtiQAHKy7NNgApCoD8ADtOpicXvKf9RJwAZT1DEGUkgX87bmSR8cO75Ss__mnLn8MyDEddnzhyphenhyphenRfcf_gWEtoLiKu53yXNQJtT0DP7nZufqBhB3P8VmvV48/s1700-e365/dify.png)

Cybersecurity researchers have disclosed details of four vulnerabilities in [Dify](https://dify.ai/), an open-source agentic workflow platform with more than [146,000 GitHub stars](https://github.com/langgenius/dify), that could allow attackers to stealthily read artificial intelligence (AI) conversions from other customers' applications without requiring authentication.

The vulnerabilities have been collectively codenamed **DifyTap** by Zafran Security.

"Two were critical severity, two required no authentication, and three carried cross-tenant impact on Dify's multi-tenant cloud service, allowing one customer's data to be exposed to another," researchers Ido Shani and Gal Zaban [said](https://www.zafran.io/resources/difytap-zafran-discovers-how-attackers-can-silently-wiretap-ai-data-across-tenants-on-a-platform-powering-1m-apps).

The security defects could have allowed attackers to read private AI chats from other customers' applications, creating a covert exfiltration channel for every message and model response.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

They also made it possible to traverse Dify's internal Plugin Daemon API from unauthenticated requests and trigger cross-tenant internal API calls, as well as preview documents uploaded by other tenants and leak files across users within a tenant by attaching another user's file unique identifier.

Separately, Zafran said it also discovered that Dify's file parsing stack relied on a version of PDFium, an open-source C++ library for PDF rendering, that was vulnerable to [CVE-2024-5846](https://nvd.nist.gov/vuln/detail/CVE-2024-5846) (CVSS score: 8.8), a two-year-old use-after-free bug that could allow a remote attacker to potentially exploit heap corruption via a crafted PDF file.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhOacqKBwVZPaGldSr42iMNW-FKKXfOZef4S84j3gcNraQeFnT78Iguthvl6n-9mYROWO6-R-PV3_2Ma4kpsroespVm1SrcTjw_OK_weSK8L1MEiMvib7fM-nr4RsAfseIYxCaq1yqfZROu-4-zNAHDMcVBtAcfeKtT_C9oltbKcfZqZgKR2fagLW5MLMsx/s1700-e365/dify.png)

The remaining vulnerabilities are listed below -

* **[CVE-2026-41947](https://nvd.nist.gov/vuln/detail/CVE-2026-41947)** (CVSS score: 9.1) - An authorization bypass vulnerability that allows authenticated editor users to set and enable trace configurations for any application regardless of tenant ownership.
* **[CVE-2026-41948](https://nvd.nist.gov/vuln/detail/CVE-2026-41948)** (CVSS score: 9.4) - A path traversal vulnerability that allows authenticated users to manipulate requests forwarded to the Plugin Daemon's internal REST API by exploiting insufficient URL path sanitization and access internal, private endpoints.
* **[CVE-2026-41949](https://nvd.nist.gov/vuln/detail/CVE-2026-41949)** (CVSS score: 7.5/5.9) - An authorization bypass vulnerability in the file preview endpoint ("/console/api/files/{file\_id}/preview") that allows any authenticated user to read up to 3,000 characters of any uploaded document across all tenants and workspaces using only the file's UUID.
* **[CVE-2026-41950](https://nvd.nist.gov/vuln/detail/CVE-2026-41950)** (CVSS score: 6.5) - An authorization bypass vulnerability that allows authenticated users to read the full contents of files uploaded by other users within the same tenant by supplying an arbitrary file UUID in the files array of a chat-messages request.

The missing tenant ownership checks can be exploited to redirect all messages and responses from victim applications to an attacker-controlled LLM trace provider. It's worth noting that anyone can freely register for a Dify account.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

"Consequently, an attacker can configure their own tracing for any application they can access as a client, which includes all publicly accessible applications," the researchers explained. "This allows an attacker to create a persistent exfiltration channel for all messages and responses sent in the application."

Following responsible disclosure, all vulnerabilities barring CVE-2026-41948 have been addressed in [version 1.14.2](https://github.com/langgenius/dify/releases/tag/1.14.2), which was shipped last month. A fix for the pending flaw is expected to be made available in the next release of Dify.

"DifyTap demonstrates where the challenge lies in vulnerability visibility, particularly in container images, where differences between deployments can create visibility gaps that traditional scanners cannot detect," the company [said](https://www.linkedin.com/posts/zafran-labs-has-disclosed-difytap-%F0%9D%97%B3%F0%9D%97%BC%F0%9D%98%82-share-7474558469791014912-vqrq/).

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
[![Facebook Mess...