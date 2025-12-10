---
title: Google Adds Layered Defenses to Chrome to Block Indirect Prompt Injection Threats
url: https://thehackernews.com/2025/12/google-adds-layered-defenses-to-chrome.html
source: The Hacker News
date: 2025-12-09
fetch_date: 2025-12-10T03:23:02.805293
---

# Google Adds Layered Defenses to Chrome to Block Indirect Prompt Injection Threats

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
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
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [Google Adds Layered Defenses to Chrome to Block Indirect Prompt Injection Threats](https://thehackernews.com/2025/12/google-adds-layered-defenses-to-chrome.html)

**Dec 09, 2025**Ravie LakshmananBrowser Security / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiuzTTpUhFNugGRa1jc7w-4LTjvLeZ-OaYTZ9C_zymrAnY-oQP-X_hyphenhyphenE8zVTX6KJTp7B6nrbrptzuDPClEEODKyC757npjyoRrIVIGUOkCw-5m-wx7jiFVeGXm5PlLuAq4D1rrSWDgAErrpGCdMLnrQHREtMLhl13arje9O0uWsQEu2VSNacaU7AJ0qb1_e/s790-rw-e365/chrome-browser.jpg)

Google on Monday announced a set of new security features in Chrome, following the company's addition of agentic artificial intelligence (AI) capabilities to the web browser.

To that end, the tech giant said it has implemented layered defenses to make it harder for bad actors to exploit indirect prompt injections that arise as a result of exposure to untrusted web content and inflict harm.

Chief among the features is a User Alignment Critic, which uses a second model to independently evaluate the agent's actions in a manner that's isolated from malicious prompts. This approach complements Google's existing techniques, like [spotlighting](https://arxiv.org/abs/2403.14720), which instruct the model to stick to user and system instructions rather than abiding by what's embedded in a web page.

"The User Alignment Critic runs after the planning is complete to double-check each proposed action," Google [said](https://security.googleblog.com/2025/12/architecting-security-for-agentic.html). "Its primary focus is task alignment: determining whether the proposed action serves the user's stated goal. If the action is misaligned, the Alignment Critic will veto it."

The component is designed to view only metadata about the proposed action and is prevented from accessing any untrustworthy web content, thereby ensuring that it is not poisoned through malicious prompts that may be included in a website. With the User Alignment Critic, the idea is to provide safeguards against any malicious attempts to exfiltrate data or hijack the intended goals to carry out the attacker's bidding.

"When an action is rejected, the Critic provides feedback to the planning model to re-formulate its plan, and the planner can return control to the user if there are repeated failures," Nathan Parker from the Chrome security team said.

Google is also enforcing what's called Agent Origin Sets to ensure that the agent only has access to data from origins that are relevant to the task at hand or data sources the user has opted to share with the agent. This aims to address site isolation bypasses where a compromised agent can interact with arbitrary sites and enable it to exfiltrate data from logged-in sites.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/windows-stealer-alert-d)

This is implemented by means of a gating function that determines which origins are related to the task and categorizes them into two sets -

* Read-only origins, from which Google's Gemini AI model is permitted to consume content
* Read-writable origins, to which the agent can type or click on in addition to reading from

"This delineation enforces that only data from a limited set of origins is available to the agent, and this data can only be passed on to the writable origins," Google explained. "This bounds the threat vector of cross-origin data leaks."

Similar to the User Alignment Critic, the gating function is not exposed to untrusted web content. The planner is also required to obtain the gating function's approval before adding new origins, although it can use context from the web pages a user has explicitly shared in a session.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjh6kkZyLORQXQaK3KLdLqSMf7pzqO-VLFP36KG0a4eKiLoikiFey0u0EohgmAdPvT8AYXRom4A82wK5CiCoT2pedN5XrfPRz6YaaEzzvyxTY3RPmcj7bHaaovs95-BukOD1_J9ey0Xkx97r0s34Dth9KozG5zM9RhwW1i7X-oCmrgb_LayMAjlBqAy7V4/s2600/cart.png)

Another key pillar underpinning the new security architecture relates to transparency and user control, allowing the agent to create a work log for user observability and request their explicit approval before navigating to sensitive sites, such as banking and healthcare portals, permitting sign-ins via Google Password Manager, or completing web actions like purchases, payments, or sending messages.

Lastly, the agent also checks each page for indirect prompt injections and operates alongside Safe Browsing and on-device scam detection to block potentially suspicious content.

"This prompt-injection classifier runs in parallel to the planning model's inference, and will prevent actions from being taken based on content that the classifier determined has intentionally targeted the model to do something unaligned with the user's goal," Google said.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-wrYKcBz_CubVG48zaFy4yvX3ePMmYaSe4UfNFomKWc3U26XN-e0bfiOTVndYYqs5-HOAAEc_7SLRZZYr3Tg8GEWLh_dBMsqowhZGU-m_xfZaabBsqk3mPoJzU88-lvEHG8jhkrRgGPxP9sTfLeVRAnoAWs7OHAya0kMa2vGqBY39-m_z1TTULJQ0TMYV/s2600/google.png)

To further incentivize research and poke holes in the system, the company said it will pay up to $20,000 for demonstrations that result in a breach of the security boundaries. These [include](https://bughunters.google.com/about/rules/chrome-friends/5745167867576320/chrome-vulnerability-reward-program-rules#qualifying-ai-report-categories) indirect prompt injections that allow an attacker to -

* Carry out rogue actions without confirmation
* Exfiltrate sensitive data without an effective opportunity for user approval
* Bypass a mitigation that should have ideally prevented the attack from succeeding in the first place

"By extending some core principles like origin-isolation and layered defenses, and introducing a trusted-model architecture, we're building a secure foundation for Gemini's agentic experiences in Chrome," Google said. "We remain committed to conti...