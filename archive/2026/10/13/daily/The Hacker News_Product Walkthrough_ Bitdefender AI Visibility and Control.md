---
title: Product Walkthrough: Bitdefender AI Visibility and Control
url: https://thehackernews.com/2026/10/product-walkthrough-bitdefender-ai.html
source: The Hacker News
date: 2026-10-13
fetch_date: 2026-10-14T06:53:25.113476
---

# Product Walkthrough: Bitdefender AI Visibility and Control

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [Product Walkthrough: Bitdefender AI Visibility and Control](https://thehackernews.com/2026/10/product-walkthrough-bitdefender-ai.html)

**The Hacker News**Oct 13, 2026Artificial Intelligence / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjkLz0n_kNY4YMLYNTi1KElj3dkaig5LqA6Koy92X4ndKfwBO8ctC5bNVyII81TUHljc7MGrpMZBsUX5j4126sBd3Sk5fX_DGjIo-yz5qGrRsHgi2qiLNUUbfCSvOHcE-KoYqGzNLBvTVzwEKDt2hZ4dvGK8YYOTeA-f6FHX49GA0myiau9Mqgc_LT7D1k/s1700-nu-rw-lo-l85-e365/bit.jpg)

A user opens a browser tab, pastes data into a chat assistant, and nothing is installed.

A developer adds a coding assistant as an editor extension, and nothing shows up in the installed programs list.

Someone downloads a local model runtime, a program that runs models directly on the machine instead of sending data to an external service, because they were told not to send company data outside.

None of this reaches your software inventory. Tasked with controlling AI, an administrator often resorts to blocking well-known AI websites and taking enforcement action without knowing what is actually running.

[Bitdefender GravityZone AI Visibility and Control (AIVC)](https://www.bitdefender.com/en-us/business/products/gravityzone-ai-visibility-and-control?cid=ref%7Cb%7C-CORE-EPP-PHASR-THN-AR) is the discovery and risk layer that answers the questions you have, first: Which AI software is present on your protected Windows endpoints, who is running it, and how much risk does each one carry.

## What Your Software Inventory Was Never Built to Watch

AI Visibility and Control covers four classes of exposure, and each one sits outside a control you already own.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgKk17gfdh2Bl-mAKK9Y8i7bEETU6nGwHdBwLhix0KogCCgm4YDYEMwmR98zPKmwoW7LO91ilqKRLT43U0g28F69t8B8LCQ_YftmXRkKruPwdqD4DI6Svu-zN8mHDS-5pdKDBKf3zwkP19dlPkbL6IuR9KiY2OAg7Peocnpvy7F-C3zBGE_6OEiQnO5b0c/s1700-nu-rw-lo-l85-e365/1.jpg)

* **AI services reached through the browser.** Hosted assistants are the path most organizations already worry about. The inventory identifies which services are running, on which machines, and whether you have marked them as approved. A service with no findings is not automatically approved; a clean result on a tool your organization never sanctioned is still shadow AI. This ensures filtering decisions are based on real user activity rather than hand-picked domain lists.
* **AI inside the development environment.** Coding assistants run inside editors that already hold source repositories, and often credentials and configuration files in the same working directory. They are rarely covered by whatever you decided about chat assistants, because nobody classified them as the same kind of tool.
* **AI running locally on the endpoint.** Local model runtimes, MCP servers, and agent frameworks execute on the machine itself. A control that governs which websites an endpoint may reach does not see them at all. The MCP server is the sharpest case: its entire purpose is to hand a model access to something else, and it usually arrives as a configuration entry rather than as an install.
* **AI with reach into other systems.** Where a tool is configured to connect to a database, a code repository, an internal API, or a third-party model service, that connection is part of your attack surface. AI Visibility and Control records the configured scope of those connections, not the data moving across them.

## **How AIVC Finds and Categorizes What It Finds**

GravityZone AI Visibility and Control discovery takes place during the risk scan. The GravityZone BEST agent collects metadata from each endpoint and keeps that collection minimized: it records what AI software is present and how it is configured, not what anyone does with it. AIVC does not inspect prompts, chat history, model weights, credentials, or full file content.

AI Visibility and Control recognizes more than 50 AI agents and more than 70,000 skills, the modular code packages that extend an agent's capabilities and that arrive from public registries. Because agents exercise permissions through these skills, considering only agents while ignoring skills would account for only a fraction of the total exposure.

Every discovered service is assigned to one of 17 functional categories based on its primary function (e.g., LLMs, coding, productivity, and others). The category makes the inventory actionable at the policy level because it maps to the question the reviewer arrived with. A security team investigating data-handling risk, filters to LLMs and chatbots plus Platforms and infrastructure. A development manager auditing what touches source code goes straight to Coding and Tools and skills. A governance review covering automation risk works from Agents, Automation, and MCP.

## **Two Views, and a Connector Nobody Installed**

AI Visibility and Control appears in Bitdefender GravityZone Console as two views, each answering a different question.

**AI Services** **answers** **"what AI is running in my environment?"** It is the inventory: every discovered service with its risk score. This includes the function category, the related AI assets it depends on or exposes, its count of open findings, the affected resources and endpoints it was found on, its state of Active or Ignored, and whether it sits on the watchlist. Opening a service shows its details alongside mitigation guidance.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgb2szOebwrE-eJR3vPwVQbEHVtY6Th1hAdbe_krsSCyrckCi-FkSf5Ue_wBUXrriNYxdJOhSnSqpsvbwlvDmVNIwhKCG0OxCqXJfKAbcovltmWDOLcwuESg9JV9A_npcj0uYQgkDaaM0CE_888tzz8z-rWj0k_eqU1aT5n6vyYEwxh_cxDrTVLRoGC_pE/s1700-nu-rw-lo-l85-e365/2.jpg)

**AI Findings** **answers "what should I look at first?"** It is the prioritized risk view. Each finding includes a risk score, the service it relates to, th...