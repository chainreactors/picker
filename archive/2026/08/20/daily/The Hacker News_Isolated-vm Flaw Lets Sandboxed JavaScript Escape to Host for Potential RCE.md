---
title: Isolated-vm Flaw Lets Sandboxed JavaScript Escape to Host for Potential RCE
url: https://thehackernews.com/2026/08/isolated-vm-flaw-lets-sandboxed.html
source: The Hacker News
date: 2026-08-20
fetch_date: 2026-08-21T03:05:08.947399
---

# Isolated-vm Flaw Lets Sandboxed JavaScript Escape to Host for Potential RCE

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

# [Isolated-vm Flaw Lets Sandboxed JavaScript Escape to Host for Potential RCE](https://thehackernews.com/2026/08/isolated-vm-flaw-lets-sandboxed.html)

**Ravie Lakshmanan**Aug 20, 2026Vulnerability / Application Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJ3-aEfGwe03ZMojsoiYaQ4TNjUiAPEFK-m68uY5JSlF8knbnGWOcBrqiB_4s6J47lPjyhQEuWdUMHnktRU6YfOcltn7_lXga77C8TNH4GOVAPrmIH_T0MsFKFkmQSMnvf42bnLlH0pC4BVMEpAZJLLTH51GpgfZybiZ_UWNLhKxx1oGi8PyD3bOUGG0_F/s1700-e365/nodejs.jpg)

Cybersecurity researchers have disclosed a critical security flaw in **[isolated-vm](https://github.com/laverdet/isolated-vm)**, a popular open-source sandbox with more than 2,900 stars and 190 forks on GitHub, that could allow attackers to escape the confines of the isolated environment.

The vulnerability ("[GHSA-864f-rcv7-6rh4](https://github.com/laverdet/isolated-vm/security/advisories/GHSA-864f-rcv7-6rh4)"), which has yet to be assigned a CVE identifier, impacts all versions of the library before and including 7.0.0. It has been patched in versions 6.2.0 and 7.0.1 released earlier this month.

Isolated-vm is a Node.js library for running untrusted JavaScript inside a [V8 Isolate](https://v8docs.nodesource.com/node-0.8/d5/dda/classv8_1_1_isolate.html), an independent instance of the Google V8 JavaScript engine, allowing multiple sandboxed JavaScript environments to run concurrently without sharing data or interfering with each other. The [npm package](https://www.npmjs.com/package/isolated-vm) has witnessed nearly 1 million downloads over the past week.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

Because each V8 Isolate has a separate state and maintains its own heap, it is not possible to directly pass JavaScript objects from the main Node.js thread into a worker isolate. Isolated-vm exposes a class called **ExternalCopy** to securely serialize JavaScript objects out of the host isolate and deserialize them into the guest isolate.

The vulnerability identified by Endor Labs resides in this component, allowing code running inside the sandbox to break out and corrupt memory in the host application.

"A type confusion in ExternalCopy's handling of the transferList option lets code running inside the sandbox corrupt memory in the host process," Endor Labs researcher Cristian-Alexandru Staicu, who is credited with discovering and reporting the flaw, [said](https://www.endorlabs.com/learn/ghsa-864f-rcv7-6rh4-critical-type-confusion-vulnerability-in-isolated-vm) in a technical write-up shared with The Hacker News.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMfsvQmmbFd-X8PGgHMFuzrHiMDs1T06796eoZw1yD6X_qvRRGkmeO6iEQC_NzOtAMZETGOrUvj0ahEVoEOF-brJwOQ7ViVeqevpjNWgDNAQ78uQyCIRtvtrHvhEdyjxOF0Ol4ps4q8WYMmi3-jYrjXLRHY-7ZhrNqIq59Z2QPS-zPVZeWnuCpXHct303P/s1700-e365/ExternalCopy.png)

"Starting from nothing but a single ivm.Reference, the standard way hosts hand a sandbox any capability at all, we escalated the bug from a controlled-address crash all the way to hijacking the host's control flow, demonstrating a full guest-to-host sandbox escape."

Successful exploitation of the flaw allows memory corruption in the host process, causing the host process to crash with a segmentation fault ([SIGSEGV](https://blog.cloudflare.com/why-is-there-a-v-in-sigsegv-segmentation-fault/)). It can also lead to a guest-to-host sandbox escape and an erosion of the trust boundary that undermines the very purpose of isolated-vm.

"Minimum demonstrated impact is a reliable, controlled-address crash (denial-of-service) triggerable by any guest that has been given an ivm.Reference (the standard way to grant a sandbox any capability)," project maintainer Marcel Laverdet said in an advisory.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

"Maximum demonstrated impact is control-flow hijack of the host process, i.e., potential remote code execution in the host."

Users who have isolated-vm installed in their developer environments are advised to update to the latest version for optimal protection. Additional details of the full exploit have been withheld so as to prevent bad actors from launching their own attacks.

"The most important takeaway is that what was not broken was the isolation primitive itself," Staicu said. "V8's Isolate boundary held. What failed was the C++ glue code that marshals values across that boundary. A perfectly sound building block was undermined by the binding layer wrapped around it."

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

[Application Security](https://thehackernews.com/search/label/Application%20Security), [Developer Security](https://thehackernews.com/search/label/Developer%20Security), [JavaScript](https://thehackernews.com/search/label/JavaScript), [Open Source](https://thehackernews.com/search/label/Open%20Source), [remote code execution](https://thehackernews.com/search/label/remote%20code%20execution), [Sandbox Security](https://thehackernews.com/search/label/Sandbox%20Security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability...