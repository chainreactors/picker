---
title: What 2,000 Exposed Vibe-Coded Apps Reveal About the Limits of Most Security Stacks
url: https://thehackernews.com/2026/05/what-2000-exposed-vibe-coded-apps.html
source: The Hacker News
date: 2026-05-29
fetch_date: 2026-05-30T05:44:31.635680
---

# What 2,000 Exposed Vibe-Coded Apps Reveal About the Limits of Most Security Stacks

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [What 2,000 Exposed Vibe-Coded Apps Reveal About the Limits of Most Security Stacks](https://thehackernews.com/2026/05/what-2000-exposed-vibe-coded-apps.html)

**The Hacker News**May 29, 2026Vibe Coding / Shadow AI

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg9_WTd_LhWXwvu2jTcVVVgE_IpLISA8vfn0awG8fVwVv_vxx1LvLU7XOxFCtSLMbiP6JKPQfFMdpA7cRJy0Phlu-RWtKH8m57ZMUwRI-tz0C-cAiASKIFS2Fytms6DnCCEif9l-CYN0drhFUEbrt71isM3LmzuA8Guqmhn6iiRqrTROcX-9tniNTQsglc/s1700-e365/red.jpg)

Shadow AI used to mean employees pasting things they shouldn't into ChatGPT. It now means something bigger: employees building full applications with AI, wiring them into production systems, and publishing them on the open internet. Without Security or IT in the loop.

The artifact moved from a prompt to a product. The risk surface moved with it.

In *The Shadow Builders* report ([get it here](https://info.redaccess.io/shadow-ai-builders-security-report)), a new category-level investigation covered in May by Axios, WIRED, and VentureBeat, Red Access identified more than 380,000 publicly accessible web assets across the leading vibe-coding platforms.

Roughly 5,000 looked corporate. More than 2,000 of those held sensitive corporate, operational, or personal data - sitting on the open web, deployed without basic access controls, often granting admin access by default to anyone who reached the URL. Six continents. Every industry is examined. No exploitation required.

Inside organizations, passing their audits while these exposures were live.

## **The new Shadow AI isn't about prompts. It's about products.**

Vibe coding - the broader space of AI-driven development platforms where anyone can build a working application by describing what they want - has compressed what used to take engineering teams months into something a non-developer can ship before lunch.

A marketing manager builds a campaign tracker and connects it to the BI tool where the real numbers live. An operations manager builds a vendor-intake form and connects it to the ticketing system. A finance team builds a board-prep dashboard and pulls invoice data into it before Friday. Those applications get connected to sanctioned production systems - CRMs, ERPs, ticketing tools, BI platforms - and frequently published to the open internet, with whatever access controls the builder happened to configure. Often, none.

The people doing this aren't malicious. They are competent employees solving real problems faster than their organization could, doing exactly what the platforms invited them to do. The platforms aren't villains either - they're delivering what their original audience asked for. What hasn't kept pace is the guardrails, technical and behavioral, governing what happens after the build.

This isn't Shadow IT in the old sense. Shadow IT was bounded: when a team bought a Trello account on a corporate card without telling anyone, the data sat inside an unsanctioned SaaS vendor, but identity, audit logs, and a governance surface at least existed. [Shadow Builders](https://redaccess.io/use-case-shadow-builders) invert that. The application is custom-built, the data is custom-loaded, the integrations are direct connections to production systems of record, and the artifact is often published on the open internet. The platform underneath may be audited; the application built on it isn't. There is the builder, the platform, and the URL. IT? Mostly not in the room.

## **Why a mature security stack still misses this**

The reflex of a CISO reading the numbers above is to check the stack. EDR is running. DLP is configured. CASB is licensed. Firewall and SSE are in place. Some organizations have added an enterprise browser. Each of those tools is doing what it was designed to do. The category sits in the gaps between them.

EDR sees the browser process, not the build inside it. To an endpoint agent, a Shadow Builder using a vibe-coding platform looks like ordinary, non-malicious browser activity - the same shape of telemetry as someone reading the news. Where modern EDR or an enterprise browser does see deeper, it only does so on devices the organization owns and inside browsers it manages. Personal laptops, contractor machines, BYOD devices, and personal-browser tabs are invisible by definition.

DLP watches enumerated channels. It can flag a user pasting regulated data into a known AI chat. It can't see a vibe-coded application connecting programmatically to a sanctioned BI tool via API, moving data cloud-to-cloud, physically bypassing the endpoint entirely.

CASB was built for Shadow IT - for SaaS vendors with discoverable identities. It can't readily distinguish an unbounded population of custom applications hosted on a vibe-coding platform's subdomains from the platform itself. The whole population tends to register as one approved SaaS vendor.

Firewall and SSE see traffic to the platform's domain but lack the application-as-business-object context. And most SASE/SSE deployments are partial - even the mature ones leave [the unmanaged-device problem](https://redaccess.io/use-case-byod/) unsolved.

None of these tools is failing. The category just sits across the gaps the existing architecture leaves between layers, generating fragments of signal that never assemble into a single, governable picture.

## **Where visibility actually has to live**

End-to-end, vibe coding is a web-session event. The build is a browser event. The OAuth grant that ties the new application to a sanctioned enterprise system is a browser event. The data the application is built around moves through the session. The deployment is a browser event - the publish action that turns the build into a live application at a public URL is a click inside the same tab where everything else happened.

Every step happens at the session layer. Not adjacent to it. Inside it.

A control positioned at the session layer, therefore, sees the whole build path - not a fragment of it. T...