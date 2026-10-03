---
title: Antino Backdoor Uses Outlook and OneDrive for C2 in China-Nexus Espionage Campaign
url: https://thehackernews.com/2026/10/antino-backdoor-uses-outlook-and.html
source: The Hacker News
date: 2026-10-02
fetch_date: 2026-10-03T07:13:21.369040
---

# Antino Backdoor Uses Outlook and OneDrive for C2 in China-Nexus Espionage Campaign

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

# [Antino Backdoor Uses Outlook and OneDrive for C2 in China-Nexus Espionage Campaign](https://thehackernews.com/2026/10/antino-backdoor-uses-outlook-and.html)

**Ravie Lakshmanan**Oct 02, 2026Cyber Espionage / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjE3s79KuB4kHE3Kf6kjA84HqdcQ2TTVyJCgIkLcSnpbMr6vCwjaLjJVE1KiXT2lZfcx_CbKlHjiX9PrEppf53uaTvQ_Vyicl447mGIkdz1ZOzmGR1hPJzgODM2J_lnsbKPhTBvvTgdDcSS4V1JzJ-feSpyJFDyDkKS0BfK7AXTCNWaL9DZ60tmWVysyVo0/s1700-nu-rw-lo-l85-e365/ms-cyber.jpg)

Government and policy organizations across Asia have become the target of a new campaign orchestrated by a China-nexus threat actor.

The activity, which has targeted government and policy organizations in Taiwan, India, the Philippines, Cambodia, Pakistan, Thailand, and Myanmar, involves the deployment of a previously undocumented backdoor codenamed Antino. Cisco Talos is tracking the cluster under the moniker **UAT-11587**.

The threat actor was first detected in September 2025 in connection with a spear-phishing campaign directed against Taiwan's academic, think tank, and civil society policy community. Since then, attacks linked to the intrusion set have expanded to target 16 entities across eight Asian countries.

"Antino is a Rust-compiled Windows backdoor that supports host reconnaissance, shell and PowerShell execution, file transfer, in-memory shellcode loading and persistence," security researcher Ashley Shen [said](https://blog.talosintelligence.com/china-nexus-uat-11587-targets-government-and-policy-organizations-across-asia-with-antino-backdoor/). "Its native command-and-control channel operates exclusively through Microsoft 365, using Microsoft Graph to interact with Outlook and OneDrive."

UAT-11587 is assessed to share some level of overlap with Jewelbug, which, in turn, exhibits tactical similarities with China-aligned clusters known as CL-STA-0049, Earth Alux, Ink Dragon, and REF7707. A report published by Broadcom-owned Symantec and Carbon Black in August 2026 [characterized](https://thehackernews.com/2026/08/china-linked-jewelbug-uses-xg-web-for.html) Jewelbug as a China-based hackers-for-hire group that carries out espionage operations and a for-profit cryptocurrency fraud business.

However, Cisco Talos said its own investigation has failed to unearth a connection between the espionage campaign and Jewelbug's financially motivated activity, prompting it to designate UAT-11587 as a separate activity set.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

The challenges in establishing definitive links notwithstanding, the adversary has been classified as China-nexus with high confidence, citing the presence of zh-CN language and Simplified Chinese metadata in the lure documents and the UTC+08:00 time zone in the spear-phishing message header.

"The campaign's lure theme and targeting provide additional contextual support," Talos said. "Its lures and observed targets include Taiwanese political, legislative, civil defense, and policy research subjects, together with regional government, maritime, diplomatic, and security themes. This collection focus is consistent with China-nexus actor interests."

Two other indicators that point to a China-nexus are below -

* Nearly a dozen distinct Antino build outputs feature Cargo registry paths referencing rsproxy[.]cn, a high-speed domestic mirror and proxy service for crates.io catering to mainland China
* A JavaScript downloader associated with UAT-11587 that references "d32tpl7xt7175h.cloudfront[.]net," a CloudFront domain previously flagged by Arctic Wolf in connection with a campaign conducted by a China-affiliated threat actor known as [UNC6384](https://thehackernews.com/2025/10/china-linked-hackers-exploit-windows.html) targeting European diplomatic and government entities last year using an unpatched Windows shortcut vulnerability.

Evidence indicates that UAT-11587 has also trained its sights on organizations in Syria around May 2026, indicating a focus beyond Asia. Attacks mounted by the threat actor have been found to spike between March and early June 2026, with a "concentrated wave" taking place on June 8 and 9, 2026, targeting dozens of systems associated with government IT infrastructure.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEioYd2judsLk9D_SSMaFwbEOLfyjPi8J7AfYMaymMPZtuW3In3sIxXgaprgePmzwjOWS4qRIkPn3GUFnK6lkBMfFbxoVKUom7mnUDN71EiAU1lhf512rUW2vzPRwuyinhOQ6ugc4-U4RdOi_Nb8pvLiFmqkE9QbpAI45qooUZRcbC5CQsoX1UrphJXHZbOo/s1700-nu-rw-lo-l85-e365/antino-chain.jpg)

While the choice of spear-phishing as an initial access vector is unsurprising, the choice of the lures employed suggests the threat actor conducted extensive reconnaissance of the target organizations in order to tailor the content and maximize the chance of success.

In an attempt to lend credibility to the emails, UAT-11587 is said to have spoofed sender identities trusted by the intended recipients to bypass [SPF and DMARC security checks](https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/) and ensure that the messages land on the victims' inboxes.

"Another social engineering technique used for initial access in this campaign was the closely replicated reconstruction of Gmail's native attachment preview widget inside the email HTML body," Shen explained. "The actor replicated the styling of Gmail's attachment card using four inline PNG images embedded as Base64-encoded MIME parts."

"The entire attachment card was wrapped in an anchor tag pointing to an attacker-controlled [Cloudflare Pages] URL. When a Gmail user opens the email in a browser, Gmail's renderer faithfully displays the attacker-controlled HTML, producing a fake attachment widget that is visually indistinguishable from a legitimate Gmail attachment preview."

An analysis of the lures demonstrates a propensity to target audien...