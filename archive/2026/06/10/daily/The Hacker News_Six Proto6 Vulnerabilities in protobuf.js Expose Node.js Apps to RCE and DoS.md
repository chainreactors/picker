---
title: Six Proto6 Vulnerabilities in protobuf.js Expose Node.js Apps to RCE and DoS
url: https://thehackernews.com/2026/06/six-proto6-vulnerabilities-in.html
source: The Hacker News
date: 2026-06-10
fetch_date: 2026-06-11T06:37:06.801042
---

# Six Proto6 Vulnerabilities in protobuf.js Expose Node.js Apps to RCE and DoS

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

# [Six Proto6 Vulnerabilities in protobuf.js Expose Node.js Apps to RCE and DoS](https://thehackernews.com/2026/06/six-proto6-vulnerabilities-in.html)

**Ravie Lakshmanan**Jun 10, 2026Vulnerability / JavaScript

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJXkAy-j0jwPWQiC9bJinbwINT6pxRmO7CJ_df4bkbAP3VD-xU8oblGB5ZBBR1oLMN0uqf_lBb5al4KSR82lU1kZsXu14TAMaXi6kIjcp5xxk5yLKnOCTloqgZd6w_PuzPxTxNROksgp9pld0D9HoxceBwprkC5cDXEvoSP64bzC_UZyZthInrECAReAeH/s1700-e365/protobuf.jpg)

Cybersecurity researchers have flagged half a dozen vulnerabilities in protobuf.js, a JavaScript and TypeScript implementation of Protocol Buffers ([Protobuf](https://protobuf.dev/)), that, if successfully exploited, could result in remote code execution (RCE) and denial-of-service (DoS) attacks.

"In affected environments, a single malicious protobuf schema, descriptor, or crafted payload could be enough to trigger crashes, runtime corruption, or even code execution," Cyera security researcher Assaf Morag [said](https://www.cyera.com/blog/cyera-research-uncovers-six-protobuf-js-vulnerabilities-impacting-the-backbone-of-data-and-ai-systems). The vulnerabilities have been codenamed **Proto6**.

Protobuf is a free and open-source, language-agnostic mechanism for serializing structured data. It was originally developed and used internally by Google before it was made publicly available in 2008.

The identified vulnerabilities affect Node.js applications that use protobuf.js, Google Cloud client libraries, messaging frameworks like [Baileys](https://baileys.wiki/docs/intro/), and CI/CD pipelines. Per Cyera, any Node.js service that deserializes Protobuf data or generates code from schemas with protobuf.js is likely impacted as well.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

A brief description of each of the flaws is below -

* **CVE-2026-44289** (CVSS score: 7.5): DoS through unbounded protobuf recursion
* **CVE-2026-44290** (CVSS score: 7.5): Process-wide DoS when loading schemas with unsafe option paths
* **CVE-2026-44291** (CVSS score: 8.1): Code generation gadget after prototype pollution
* **CVE-2026-44292** (CVSS score: 5.3): Prototype injection in generated message constructors
* **CVE-2026-44294** (CVSS score: 5.3): DoS from crafted field names in generated code
* **CVE-2026-44295** (CVSS score: 8.7): Code injection in pbjs static output from crafted schema names

Cyera said all the vulnerabilities stem from the library's handling of schema and metadata as trusted by default. This validation oversight could influence application behavior and lead to code execution.

"While exploitation of these vulnerabilities generally requires specific conditions, those conditions are increasingly common in data and AI ecosystems that routinely exchange data, schemas, and configuration files across services, repositories, cloud platforms, and third-party integrations," Morag noted.

In a potential attack scenario, a bad actor could introduce a malicious protobuf schema to poison CI/CD workflows, leaking build secrets in the process (CVE-2026-44295), or crash Node.js services such as WhatsApp bots built using Baileys, a WhatsApp Web API automation TypeScript library, by means of a specially crafted message (CVE-2026-44292).

The most severe of the lot is CVE-2026-44291, which results in code execution when a Node.js application accepts attacker-controlled input.

"That input reaches a prototype pollution gadget," security researcher Vladimir Tokarev [explained](https://www.cyera.com/research/proto6-the-schema-was-not-supposed-to-run). "Later, the same process uses protobuf.js to encode or decode a message. Because protobuf.js resolves type names through plain property lookups, a polluted Object.prototype can make an attacker-controlled string look like a valid protobuf primitive."

"Protobuf.js then inserts that string into a generated encoder or decoder function and compiles it with Function(). The attacker gets arbitrary JavaScript execution inside the Node.js process."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

The following versions of the tool are vulnerable -

* protobuf.js: versions <= 7.5.5 and >= 8.0.0 <= 8.0.1
* protobufjs-cli: versions <= 1.2.0 and >= 2.0.0 <= 2.0.1

Patches for the flaws are available in protobufjs 7.5.6 and 8.0.2, and protobufjs-cli 1.2.1 and 2.0.2. Users are advised to apply the latest fixes to safeguard against potential threats.

"Because protobuf.js is heavily used inside databases, vector stores, inference pipelines, orchestration systems, CI/CD tooling, and cloud SDKs, successful exploitation could impact sensitive enterprise and AI workloads at scale," Cyera said.

"Modern software increasingly treats schemas, metadata, and configuration files as trusted inputs that drive automation, orchestration, and code generation. When those trust assumptions break, data can become behavior. That shift creates new attack surfaces that security teams must learn to identify and manage."

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

[CI/CD](https://thehackernews.com/search/label/CI/CD), [c...