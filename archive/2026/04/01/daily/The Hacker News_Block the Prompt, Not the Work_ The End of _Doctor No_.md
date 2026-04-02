---
title: Block the Prompt, Not the Work: The End of "Doctor No"
url: https://thehackernews.com/2026/04/block-prompt-not-work-end-of-doctor-no.html
source: The Hacker News
date: 2026-04-01
fetch_date: 2026-04-02T04:31:35.761552
---

# Block the Prompt, Not the Work: The End of "Doctor No"

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWajeG0cdaapf1GKTZRUZUB7BzuYGegyw5k0eAorJXlmkFdYCCeLXXhXYJuXU9lWD33rV6rRnIyly3czoNfYifpxk1eGA5slItPmim3HkubXoQMgC4J7hdQPywxGbWq7Eqeff_o6s2Fq-WmSFd5guwdLn7IqpveMqULqtVnd-ndnljWYGj45EkMFB7m0qm/s728-e100/z-d.jpg)](https://thehackernews.uk/zscaler-threatlabz-d)

# [Block the Prompt, Not the Work: The End of "Doctor No"](https://thehackernews.com/2026/04/block-prompt-not-work-end-of-doctor-no.html)

**The Hacker News**Apr 01, 2026Endpoint Security / Data Protection

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgvlo2Z4APlfxw_Y81FpX62ySlxihctfAGwiT0WYd1bPrdk5sMFO8w7__xRzVqn9vYqFpE4TSS80iuNQZ9SgcR4Hz8f6WYFhD5OaoRmY-sD20cYox6Tx-_xbhiawEh0cy3YNvv9iD75BIsW5NNA8tafY4inhGtFBer5pan0xjr-vyLZmHyIFHc-LaTNcMZC/s1700-e365/red.jpg)

There is a character that keeps appearing in enterprise security departments, and most CISOs know exactly who that is. It doesn’t build. It doesn’t enable. Its entire function is to say "No."

No to ChatGPT.

No to DeepSeek.

No to the file-sharing tool the product team swears by.

For years, this looked like security. But in 2026, "Doctor No" is no longer just a management headache – it is a systemic security liability. Because when you block the work, users don’t stop. They reroute.

## The Tax-Evaders of Productivity

When security feels like a tax on efficiency, employees find a way to "evade" it.

The industry has long relied on Endpoint Agents to enforce control. But as any CISO knows, these agents come with a heavy "tax." They hook into the OS kernel, they’re invasive, they notoriously break during macOS updates, and they make high-performance machines run hot.

The result? Users find workarounds. Files move into personal Gmail. Prompts are pasted into unmanaged AI tools. This is the Workaround Economy – a shadow infrastructure that exists not despite your security, but because of it. And the defining characteristic of this economy is that it operates with zero organizational visibility.

## The Illusion of Control: The "Theatrical" Stack

Most teams still default to blocking because their legacy tools were never built to do much else. It’s not that these capabilities don't exist; it's that they are architecturally untenable for modern web work.

* **The SSL Inspection Trap:** Firewalls, Secure Web Gateways (SWG), and even many modern **SASE/SSE solutions** technically attempt to "see" encrypted traffic through SSL decryption. But in a world of certificate pinning and complex web app "plumbing," this brute-force approach is a high-risk trade-off. Because these tools sit *between* the user and the web, they frequently break the very tools – like Slack, WhatsApp, or high-performance GenAI interfaces – that the business relies on. For a CISO, the choice is binary and brutal: turn on inspection and break the user experience, or turn it off and remain blind.
* The Visibility Gap: EDR sees machine-level processes, and legacy DLP scans files at rest. But for most organizations, the live, streaming browser session remains a black box. While some newer 'suite' extensions attempt to peek inside, they only work on managed devices where the IT team has total control. Even then, they often come with a hidden cost: **micro-latencies that make typing feel 'laggy,' rendering errors that break complex web app interfaces, and heavy CPU usage that turns a high-end laptop into a space heater.** And even still, they remain blind to the prompt typed on a contractor’s laptop, a partner’s browser, or an unmanaged home device—the exact places where sensitive data is most likely to leak before the user even clicks 'send'.
* The Extension Jungle: You can block a URL, but can you see the [browser extension silently harvesting credentials](https://redaccess.io/use-case-browser-extensions/)? Most stacks cannot.

Blocking a website while leaving the browser session unmonitored is Theatrical Security. It provides the appearance of a policy without the reality of protection.

## The Law Firm Lesson: A Case of "Ghost" Compliance

A prominent U.S. law firm recently discovered the danger of this gap. When data sovereignty concerns arose around DeepSeek, they did what seemed right: they blocked the domain. IT closed the ticket. Leadership felt covered.

A subsequent visibility exercise told a different story.

Seventy percent of their users had already installed an AI "wrapper" extension. Because the extension executed entirely inside the browser session, it was invisible to the firewall and the endpoint agent. Corporate traffic was being silently routed through servers in China. No alert had fired. No policy had triggered.

**They had blocked the website. They hadn't blocked the risk.**

While satisfied to find this gap, that feeling was quickly overshadowed by the particular stress of discovering that a control you'd trusted was purely theatrical. The compliance implications could have been dire.

## The New Standard: Secure the Session, Not the Device

The browser has become the new OS of work. Security that lives anywhere else is simply too far away from the "Point of Risk."

The standard in 2026 is moving away from invasive agents and toward Session-Level Governance. The goal is a toolset that provides surgical control – governing the data, not the destination.

This requires a standard of security that can:

* [Execute Prompt-Level DLP](https://redaccess.io/use-case-dlp/): Identifying and redacting sensitive code or PII in real-time, within the buffer, before the "Send" button is ever clicked.
* Govern the Extension Layer: Identifying and risk-scoring the "silent" extensions that bypass domain blocks entirely.
* Enforce Agentless Controls: Providing clipboard and upload governance that works on any browser, on any device (including BYOD and contractors), without the "kernel-hooking" performance tax that drives users toward workarounds.

## From Gatekeeper to Enabler

The role of security teams is changing. Instead of defining themselves as “gatekeepers”, most successful security leaders are now becoming a visibility layer – one that enables the business to say "Yes" because they can finally see, and govern, what happens when people work.

The question is no longer whether your users are using AI. The...