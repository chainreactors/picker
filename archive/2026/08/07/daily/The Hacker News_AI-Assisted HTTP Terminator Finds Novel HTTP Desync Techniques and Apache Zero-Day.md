---
title: AI-Assisted HTTP Terminator Finds Novel HTTP Desync Techniques and Apache Zero-Day
url: https://thehackernews.com/2026/08/ai-assisted-http-terminator-finds-novel.html
source: The Hacker News
date: 2026-08-07
fetch_date: 2026-08-08T03:25:01.670616
---

# AI-Assisted HTTP Terminator Finds Novel HTTP Desync Techniques and Apache Zero-Day

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

# [AI-Assisted HTTP Terminator Finds Novel HTTP Desync Techniques and Apache Zero-Day](https://thehackernews.com/2026/08/ai-assisted-http-terminator-finds-novel.html)

**Swati Khandelwal**Aug 07, 2026Web Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgynSSg0CZ1sssmMR8F0u09LmQ82liuj5nt2aor3klmi-xPcKTmalo4JLFQ7jd2mU9Ycnltsrnw2MiVVjmlT-wcYR74Ob7NMN31KNnny14lqVRdrmj30r3yqTSxapzCmQPk9lPG7v9GDSVKQwE4ufB-jWfsx1lc2O5GNd0bHd5M6FbMNah3dcLzu2EAFXo/s1700-e365/Desync.jpg)

PortSwigger says HTTP Terminator, an artificial intelligence (AI)-assisted research system built by **James Kettle**, generated and proved new HTTP desynchronization techniques after exploring 30,000 candidate desync vectors.

PortSwigger said a separate human-guided discovery cascade also exposed a zero-day in Apache Traffic Server. Kettle said HTTP Terminator tested 30,000 websites where scanning was authorized through bug bounty or vulnerability disclosure programs and found roughly 700 vulnerable targets before deeper validation and RQP research.

Kettle said those findings involved banks, government infrastructure, security products, and an airport.

The research produced new desync triggers, a dual-matching Content-Length pattern, and a "dangling-byte" technique designed to make response queue poisoning (RQP) more reliable. RQP can potentially make a front end lose track of which back-end response belongs to which user, potentially exposing another user's response, including session cookies or API keys.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

The researchers also disclosed Shared-Parser Confusion, a broader attack concept that the system proposed but Kettle validated. The defense has not changed: PortSwigger recommends avoiding [HTTP/1.1 upstream](https://thehackernews.com/2025/08/new-http2-madeyoureset-vulnerability.html). Where HTTP/1.1 cannot be removed, it recommends allow-listing methods at both layers and restricting which methods may carry request bodies.

In the [technical write-up](https://portswigger.net/research/can-ai-do-novel-security-research), Kettle said he fed HTTP Terminator 138 HTTP and SMTP RFCs. Those RFCs were split into about 15,000 small fragments and used as inspiration to generate 30,000 unique candidate vectors.

One Content-Type: multipart/byteranges technique worked across multiple server implementations and exposed more than 200 websites in the test set, including an unnamed U.S. bank.

The autonomous research then tested 16 ideas for improving RQP. Only the dangling-byte technique survived evaluation. It leaves a smuggled request one byte short so the second back-end response is not produced until a victim request supplies the missing byte, eliminating a race condition that otherwise makes RQP unreliable on many sites.

In the human-guided cascade, a malformed request eventually exposed the desynchronization zero-day in Apache Traffic Server. The researchers said the issue has since been patched and tracked as CVE-2026-63078.

An August 7 check by The Hacker News did not find a public record for CVE-2026-63078 in CVE.org or NVD, and [Apache's July advisory covering 34 flaws](https://trafficserver.apache.org/security-2026-07.html) did not list it. That leaves a verification gap around the Apache case: the cited public records do not yet let defenders map CVE-2026-63078 to a specific fixed Traffic Server release.

Kettle said Shared-Parser Confusion emerged when HTTP Terminator noticed that response-processing rules could be misapplied to requests when servers reuse parsing logic. The system proposed the concept, but Kettle, director of research at PortSwigger, validated and generalized it. "Neither of us would have discovered it alone," he said.

That distinction defines the autonomy boundary in this research: the system generated and proved several techniques without direct human discovery input, while the Apache zero-day and Shared-Parser Confusion still required Kettle's intervention.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

PortSwigger has [open-sourced HTTP Terminator](https://github.com/PortSwigger/http-terminator). The paper does not identify which exact model or version generated each autonomous discovery. The released implementation uses Claude for document extraction and test-case generation, while its investigator stage requires [Claude Code](https://thehackernews.com/2026/02/anthropic-launches-claude-code-security.html).

Separately, researchers behind CRLF-powered desync attacks released public tools for studying that attack class, including [crlf-desyncs](https://github.com/turtlesec-software/crlf-desyncs) and [crlf-powered-desync-scanner](https://github.com/t0xodile/crlf-powered-desync-scanner).

Kettle separately tested newer models on a rediscovery benchmark and reported a 30% success rate for [GPT-5.6 Sol](https://thehackernews.com/2026/06/openai-limits-gpt-56-rollout-as-sol.html) when given an inspiration technique.

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

[Application Security](https://thehackernews.com/search/label/Application%20Security), [artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence), [enterprise security](https://thehackernews.com/search/label/enterprise%20security), [network security](https://thehackernews.com/search/label/network%20security), [Open Source](https:...