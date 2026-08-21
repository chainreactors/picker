---
title: CDN Tsunami Attack Abuses HTTP/3 Translation for Up to 350x DoS Amplification
url: https://thehackernews.com/2026/08/cdn-tsunami-attack-abuses-http3.html
source: The Hacker News
date: 2026-08-20
fetch_date: 2026-08-21T03:05:09.651822
---

# CDN Tsunami Attack Abuses HTTP/3 Translation for Up to 350x DoS Amplification

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

# [CDN Tsunami Attack Abuses HTTP/3 Translation for Up to 350x DoS Amplification](https://thehackernews.com/2026/08/cdn-tsunami-attack-abuses-http3.html)

**Swati Khandelwal**Aug 20, 2026Web Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhDFisNx669R67D6R9VnkWr_DIhB1VjYqDPrXqKAoeCz0YxbSngLxB15XYLtuKb00YSEE0rxQEfop5v7JIr2SMVOErIM2r_GZqA6q1FDNl_wBeAaukVoAse6l0kXv35dJRTQjT8R0DhS9ihwYUXNd9cFuqYM3GS0o28NyIBAgliuQR8XhKQqhixFcjdZpo/s1700-e365/cdn-boost.jpg)

Cybersecurity researchers have disclosed two denial-of-service (DoS) attacks that exploit how major content delivery networks (CDNs) convert client-facing HTTP/3 traffic into HTTP/1.1 requests to the websites they front, amplifying a low-bandwidth request stream by up to 350x against the origin server.

The attacks, collectively named "**[CDN Tsunami](https://arxiv.org/html/2607.26589v1)**," were evaluated against Alibaba, Baidu, Cloudflare, Amazon CloudFront, Fastly, and Tencent.

All six were found susceptible to the bandwidth variant and five to the connection variant, with Cloudflare unaffected by the latter because it buffers the complete request before opening a connection to the origin.

The attack requires a website hosted on one of the six providers, with HTTP/3 serving at the edge, and no configuration changes on the website's part. The paper lists HTTP/3 as enabled by default at Cloudflare and CloudFront.

However, [Cloudflare's documentation](https://developers.cloudflare.com/speed/optimization/protocol/http3/) describes HTTP/3 as available on all plans and provides steps to enable it, rather than stating it is enabled by default. AWS [documentation](https://docs.aws.amazon.com/sdk-for-kotlin/api/latest/cloudfront/aws.sdk.kotlin.services.cloudfront.model/-distribution-config/-builder/http-version.html) gives http2 as the default HTTP version for new CloudFront distributions.

The 350x factor applies only to Alibaba, Baidu, and Tencent. These three providers support the QPACK dynamic table, and it was measured at roughly 64 concurrent streams, with the maximum on Cloudflare, CloudFront, and Fastly ranging from 36.41x to 51.2x.

No CVE identifiers have been assigned, and no exploitation in the wild is reported. While Baidu and Tencent confirmed the reports and deployed the proposed fixes, the researchers say every mitigation proposed is applied at the CDN rather than at the origin website.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

The two techniques are named **HTTP/3 Bandwidth Amplification (HBA)** and **HTTP/3 Connection Amplification (HCA)**, and both rest on the same deployment gap, in which a CDN speaks HTTP/3 to the browser but only HTTP/1.1 to the website behind it, a mismatch the team said exists because "CDNs do not support end-to-end HTTP/3."

HBA leverages [QPACK](https://thehackernews.com/2026/06/f5-patches-two-critical-nginx-open.html), the header compression format introduced with HTTP/3. Because HTTP/1.1 carries no equivalent mechanism, the CDN has to expand every small index value it receives back into a full raw header before forwarding the request, so a request costing the attacker a few bytes on the wire costs the origin the decompressed size.

Attacker-side bandwidth stayed below 500 Kbps against the three CDNs supporting the dynamic table and below 5 Mbps against the rest, while bandwidth consumption measured at the origin exceeded 100 Mbps throughout.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHy3-OJJp-8CR2sOlXhKXZLbWkyTyvE2_K5rK7P_rlZbilb4gNp5X8t-FuYiKs19Vsei_B4oTLQTgKJhbc6wLWAv2PiWl0wtHife8HDx4Yp1-ppxszrdKsR4y11UE4YaDdLBmiD6t_lv5VqO95vAmi0fAsbKGv9IBJEHefi7f8WRcD3WTzKq75JrAUb0I/s1700-e365/cdns.jpg)

The dynamic table variant requires the attacker first to send one HTTP/3 request carrying a large header, which the CDN inserts into the table, and then reference that entry repeatedly using small index values. Support is limited to Alibaba, Baidu, and Tencent, each advertising a 4KB table with a maximum entry size of 3,072 bytes.

The maximum bandwidth amplification factors measured using the QPACK static table are as follows -

* Baidu, 66.06x, dynamic table supported
* Alibaba, 65.8x, dynamic table supported
* Tencent, 54.08x, dynamic table supported
* Amazon CloudFront, 51.2x, no dynamic table support
* Cloudflare, 48.27x, no dynamic table support
* Fastly, 36.41x, no dynamic table support

HCA targets connection capacity rather than bandwidth. Five of the six CDNs open an HTTP/1.1 connection to the origin as soon as they receive the HTTP/3 HEADERS frame, before the request body arrives, and HTTP/3 multiplexing allows a single client connection to carry multiple streams, each of which triggers its own backend TCP connection. Sending DATA frames at a very low rate then keeps those connections open, with the CDN continuing to treat the request as incomplete.

Against an Apache server configured with a 300-second timeout and a 256-connection limit, four HTTP/3 connections, each multiplexing 96 streams, forced 384 backend connections, while Fastly required 48 connections of 8 streams because it caps backend connections at 10 per HTTP/3 connection.

Response times for a benign client reached 60 seconds on Alibaba and up to 90 seconds on Baidu and CloudFront, both returning HTTP 504 Gateway Timeout, while Fastly rose to 15 seconds and returned HTTP 503 Service Unavailable.

Tencent closed the client-side connection roughly 10 seconds after receiving a probe request and returned no response.

The experiments were bounded by limits the researchers imposed on themselves, with the origin capped at 100 Mbps and the attacker at 30 Mbps, and no test above those figures is reported. The paper states that the attacks scale to higher-capacity servers, a claim it does not test.

The amplification factor was also found to peak near 64 concurrent streams and then decline, w...