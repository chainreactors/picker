---
title: Citrix Patches Six NetScaler Flaws Allowing File Read and Denial-of-Service
url: https://thehackernews.com/2026/07/citrix-patches-six-netscaler-flaws.html
source: The Hacker News
date: 2026-07-01
fetch_date: 2026-07-02T05:58:23.634752
---

# Citrix Patches Six NetScaler Flaws Allowing File Read and Denial-of-Service

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

# [Citrix Patches Six NetScaler Flaws Allowing File Read and Denial-of-Service](https://thehackernews.com/2026/07/citrix-patches-six-netscaler-flaws.html)

**Ravie Lakshmanan**Jul 01, 2026Vulnerability / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhkaU5jHNUkuBuH0Obx-gU_L4wSKOWP9bPwZeyD8tY1hIHShQozXYO2UckRTb2z5SwreXgHxLzePWkBfixNzYWsJ6eXioRllicv96TA8QvXBerGAguD3uA2T1DcMaURdi5BdMcNlY4DF_DPk-kdNXvIZfz8QMnrekgc-Hjksqf5OCHy11j0zcT668GgBhnc/s1700-e365/citrix.jpg)

Citrix on Tuesday [released](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX696604) security updates to address multiple flaws in NetScaler ADC (formerly Citrix ADC) and NetScaler Gateway (formerly Citrix Gateway) that could be exploited by an attacker to facilitate arbitrary file reads or trigger a denial-of-service (DoS) condition.

The vulnerabilities are listed below -

* **CVE-2026-8451** (CVSS score: 8.8) - An insufficient input validation vulnerability leading to memory overread when NetScaler ADC or NetScaler Gateway is configured as a SAML IDP
* **CVE-2026-8452** (CVSS score: 8.8) - A memory overflow vulnerability leading to unpredictable or erroneous behavior and denial-of-service when the appliance is configured as a Gateway or an AAA virtual server
* **CVE-2026-8655** (CVSS score: 8.8) - Multiple memory overflow vulnerabilities leading to unpredictable or erroneous behavior and denial-of-service when NetScaler ADC is configured as an LB of type Oracle, a DNS Proxy, or a DNS recursive resolver deployment
* **CVE-2026-10816** (CVSS score: 7.7) - An external control of the file name of the path vulnerability leading to unauthenticated, arbitrary file read when access to NSIP, Cluster Management IP, or SNIP with management access is enabled
* **CVE-2026-10817** (CVSS score: 6.9) - An insufficient input validation vulnerability leading to memory overread when TCP TimeStamp is enabled in TCP Profile and associated with the virtual server (of type LB, CS, VPN) or the service configured on NetScaler
* **CVE-2026-13474** (CVSS score: 8.7) - A missing release of memory after effective lifetime vulnerability leading to denial-of-service via malformed HTTP/2 requests when HTTP/2 is enabled in the HTTP Profile and associated with the virtual server (of type LB, CS, VPN) or the service configured on NetScaler

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Patches for the security defects have been released in the following versions -

* NetScaler ADC and NetScaler Gateway 14.1-72.61 and later releases
* NetScaler ADC and NetScaler Gateway 13.1-63.18 and later releases of 13.1
* NetScaler ADC 14.1-FIPS 14.1-72.61 FIPS and later releases of 14.1-FIPS
* NetScaler ADC 13.1-FIPS and 13.1-NDcPP 13.1.37.272 and later releases of 13.1-FIPS and 13.1-NDcPP

As for CVE-2026-13474, customers are also advised to update their configurations by modifying the Http2SmallWndTimeout parameter, which controls the timeout (in seconds) for HTTP/2 small‑window stalled streams -

* For appliances using HTTP Strict Profiles, this parameter defaults to 30 seconds. The fix is effective immediately after the upgrade.
* For appliances NOT using HTTP Strict Profiles, the default value is 0. In this case, merely upgrading to the builds containing the fix will not address the vulnerability completely. Customers must manually set Http2SmallWndTimeout to 30 seconds.

The command to set this parameter is below -

```
set ns httpProfile <profile_name> -http2SmallWndTimeout <value_in_seconds>
```

Cisco credited Michael Tucker from the XOR team at JPMorgan Chase, Aliz Hammond of watchTowr, and Maxim Suhanov for reporting the vulnerabilities. There is no evidence that the issues have been exploited in the wild.

watchTowr Labs, in a technical write-up released alongside Citrix's bulletin, said CVE-2026-8451 was discovered and reported in late March 2026 after attempts to reproduce [CVE-2026-3055](https://thehackernews.com/2026/03/citrix-urges-patching-critical.html) (CVSS score: 9.3), a separate insufficient input validation flaw that was disclosed earlier this year.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqmM4NpfZsx4cw-HrXQlCjZQmrF8bYnmB23AmpOPi16kPNB9lvICjpdYEclxJwyQ9OE8GgzQ8aOEI68tRuxNqov0MHz2Sq8xEPiYWM3Js6FM5t2nm2JHWodmR7qVSot14ZtWVqQRQ6B88OnMaVxCPwRG7xGPoIIZxF6QAhWVhMkQfs11NjyNtHsGEUH4_q/s728-e100/sygnia-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

The cybersecurity company said the vulnerability stems from how NetScaler parses SAML authentication requests and shares the same root cause as the March 2026 flaw, resulting in out-of-bounds memory reads when sending malformed SAML requests.

"One thing we're keen to note: in contrast to the original CVE-2026-3055, in which kilobytes of binary data can be leaked, this overread will terminate the out-of-bounds read when various control characters are read, such as NULL (or even >)," security researcher Hammond [said](https://labs.watchtowr.com/citrixbleed-to-infinity-and-beyond-citrix-netscaler-pre-auth-memory-overread-cve-2026-8451/). "In practice, we found that by varying the request length, we could consistently squeeze a few bytes out of the server."

"However, what should be of concern is the bigger picture - the trend, which is very clearly suggesting that memory management continues to appear fragile within Citrix NetScaler appliances, to the extent that even accidentally misconfiguring an appliance can lead to the disclosure of leaked memory."

In recent years, Citrix appliances have been a lucrative attack target, with [multiple](https://thehackernews.com/2026/03/citrix-urges-patching-critical.html) [flaws](https://thehackernews.com/2026/03/citrix-netscaler-under-active-recon-for.html) in its software exploited by threat actors for ransomware deployment in the past, making it crucial that users apply the patches for optimal prot...