---
title: Attackers Target miniOrange SAML Flaws That Can Grant WordPress Admin Access
url: https://thehackernews.com/2026/08/attackers-target-miniorange-saml-flaws.html
source: The Hacker News
date: 2026-08-25
fetch_date: 2026-08-26T03:07:03.042500
---

# Attackers Target miniOrange SAML Flaws That Can Grant WordPress Admin Access

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [Attackers Target miniOrange SAML Flaws That Can Grant WordPress Admin Access](https://thehackernews.com/2026/08/attackers-target-miniorange-saml-flaws.html)

**Ravie Lakshmanan**Aug 25, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhtxn6tX1r1BmVfN_4cdoh6p5jmcAe3D9ckNhjscacXx5HpxZJAdb1SvIWo404cGlwahzCLyFIRB-MdUjGcQdBLLC5pMwaCB75e9AT5jKvC49cvIP5jGIOB4IjcQGaOpibWbIPKj929DICeMilGRZn5JmVIcVslRm2hWgz5RTXIZK5d2b2N5dlEnRBBwWVO/s1700-e365/wordpress-hack.jpg)

Bad actors are attempting to exploit two severe unauthenticated authentication bypasses in the Xecurify miniOrange SAML 2.0 Single Sign On plugin that make it possible for an attacker to sign in as any WordPress user, including administrators.

The vulnerabilities, as disclosed by [Patchstack](https://patchstack.com/articles/one-slug-seven-editions-the-miniorange-saml-sso-bug-that-let-anyone-log-in-as-your-wordpress-admin/), are listed below -

* **[CVE-2026-61979](https://www.cve.org/CVERecord?id=CVE-2026-61979)** (CVSS score: 8.1) - An unauthenticated privilege escalation vulnerability stemming from signature algorithm confusion (Fixed in version 17.0.5 for the Standard edition)
* **[CVE-2026-15981](https://www.cve.org/CVERecord?id=CVE-2026-15981)** (CVSS score: 9.8) - An authentication bypass vulnerability stemming from accepting malformed signatures as valid (Fixed in version 17.0.6 for the Standard edition)

"This is due to the mo\_saml\_validate\_signature() function performing a loose boolean check on the raw tri-state integer returned by PHP's openssl\_verify(), causing an error return value of -1 to be evaluated as truthy and therefore treated as a successful signature verification," according to a description of CVE-2026-15981 on CVE.org.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

"This makes it possible for unauthenticated attackers to log in as any existing WordPress user, including administrators, by submitting a crafted SAMLResponse containing an attacker-controlled NameID and a deliberately malformed signature value that triggers an OpenSSL processing error — bypassing verification entirely and resulting in wp\_set\_auth\_cookie() being called for the targeted account."

The WordPress security company, which credited the DigitalOcean security team for reporting the issues, said an attacker can craft a SAML response with a malformed signature and send it to the plugin, causing it to treat it as valid.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjYevjba6N2QNYvYUMyVCK8kIJsA5m29GPpGU2SoUuxg_Meo2sDATxtZ_WSTC62JNH80yalaHPHCEI0DAlshWNOiL82nqt17TnANm7962KpUGKAlUca4B1fpyM1oflpzZrD-ZokejMhy3syCDamrnyie_I0Gfgcv0oE1aZJTxj3Km4yD-1Hwf5vEkeYLfi1/s1700-e365/word.jpg)

The cloud infrastructure provider is said to have discovered the vulnerabilities after observing an anomalous WordPress administrator session attempt from outside their trusted network. "The attacker had already used the bypass to obtain a WordPress admin session cookie, but was stalled because the admin panel operations themselves sat restricted behind the trusted network," Patchstack said.

The scanning activity has been recorded from the following IP addresses -

* 207.211.214.41
* 79.127.224.14
* 102.91.71.83
* 162.243.116.148
* 84.201.6.54
* 64.225.25.188

"The spread suggests opportunistic scanning rather than a targeted campaign," Patchstack added. "Whoever is running this appears to be throwing the exploit at every site with the plugin installed without checking which edition or version is behind it."

WordPress site owners are advised to apply the latest fixes to stay protected, especially given the availability of a proof-of-concept (PoC) code that allows attackers to chain the flaws to obtain admin privileges and take control of susceptible sites.

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

[Application Security](https://thehackernews.com/search/label/Application%20Security), [Authentication Security](https://thehackernews.com/search/label/Authentication%20Security), [privilege escalation](https://thehackernews.com/search/label/privilege%20escalation), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehackernews.com/search/label/Web%20Security), [WordPress](https://thehackernews.com/search/label/WordPress)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Microsoft Patches Severe Entra ID Flaw (CVSS 10.0) Allowing Remote Code Execution](https://thehackernews.com/2026/08/microsoft-entra-id-flaw-cvss-100.html)

[![The Hacker News](data:image/svg+xml;base64...)

ThreatsDay: Gogs 10.0 RCE, n8n Workflow-to-RCE, $10M Reward, GLM-5.3 AI Exploit, and More](https://thehackernews.com/2026/08/threatsday-gogs-100-rce-n8n-workflow-to.html)

[![The Hacker News](data:image/svg+xml;base64...)

New Cryptographic Context Injection Attack Could Let Web Pages Steal Grok Chat Data](https://thehackernews.com/2026/08/new-cryptographic-context-injection.html)

[![The Hacker News](data:image/svg+xml;base64...)

Zombie Card Attack Can Revive Expired Visa C...