---
title: New AI-Targeted Cloaking Attack Tricks AI Crawlers Into Citing Fake Info as Verified Facts
url: https://thehackernews.com/2025/10/new-ai-targeted-cloaking-attack-tricks.html
source: The Hacker News
date: 2025-10-29
fetch_date: 2025-10-30T03:12:54.766727
---

# New AI-Targeted Cloaking Attack Tricks AI Crawlers Into Citing Fake Info as Verified Facts

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [New AI-Targeted Cloaking Attack Tricks AI Crawlers Into Citing Fake Info as Verified Facts](https://thehackernews.com/2025/10/new-ai-targeted-cloaking-attack-tricks.html)

**Oct 29, 2025**Ravie LakshmananMachine Learning / AI Safety

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7Zf17lOXR_Z03iHmWh_BUjSexeLn117N0KiHTTh8NCcDhuLDju5f6EpPZDtp1uPqHTV-h6-ebxTdZOoRuYRglmJVPig9BfOx-O0k8Yz0ms1Ghk4r8k_9ZVC36xPuvvXpJsT4WFiTUBmLEw-oYCVIpXxINdhOySH0ysqaG40exTNITYuMuIxb3wLNXm71H/s790-rw-e365/ai-news.jpg)

Cybersecurity researchers have flagged a new security issue in agentic web browsers like OpenAI ChatGPT Atlas that exposes underlying artificial intelligence (AI) models to context poisoning attacks.

In the attack [devised](https://splx.ai/blog/ai-targeted-cloaking-openai-atlas) by AI security company SPLX, a bad actor can set up websites that serve different content to browsers and [AI crawlers](https://blog.cloudflare.com/from-googlebot-to-gptbot-whos-crawling-your-site-in-2025/) run by ChatGPT and Perplexity. The technique has been codenamed **AI-targeted cloaking**.

The approach is a variation of search engine cloaking, which refers to the practice of presenting one version of a web page to users and a different version to search engine crawlers with the end goal of manipulating search rankings.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The only difference in this case is that attackers optimize for AI crawlers from various providers by means of a trivial user agent check that leads to content delivery manipulation.

"Because these systems rely on direct retrieval, whatever content is served to them becomes ground truth in AI Overviews, summaries, or autonomous reasoning," security researchers Ivan Vlahov and Bastien Eymery said. "That means a single conditional rule, 'if user agent = ChatGPT, serve this page instead,' can shape what millions of users see as authoritative output."

SPLX said AI-targeted cloaking, while deceptively simple, can also be turned into a powerful misinformation weapon, undermining trust in AI tools. By instructing AI crawlers to load something else instead of the actual content, it can also introduce bias and influence the outcome of systems leaning on such signals.

"AI crawlers can be deceived just as easily as early search engines, but with far greater downstream impact," the company said. "As SEO [search engine optimization] increasingly incorporates AIO [artificial intelligence optimization], it manipulates reality."

The disclosure comes as an analysis of browser agents against 20 of the most common abuse scenarios, ranging from multi-accounting to card testing and support impersonation, discovered that the products attempted nearly every malicious request without the need for any jailbreaking, the hCaptcha Threat Analysis Group (hTAG) said.

Furthermore, the study [found](https://www.hcaptcha.com/post/report-browser-agent-safety-is-an-afterthought-for-vendors) that in scenarios where an action was "blocked," it mostly came down due to the tool missing a technical capability rather than due to safeguards built into them. ChatGPT Atlas, hTAG noted, has been found to carry out risky tasks when they are framed as part of debugging exercises.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Claude Computer Use and Gemini Computer Use, on the other hand, have been identified as capable of executing dangerous account operations like password resets without any constraints, with the latter also demonstrating aggressive behavior when it comes to brute-forcing coupons on e-commerce sites.

hTAG also tested the safety measures of Manus AI, uncovering that it executes account takeovers and session hijacking without any issue, while Perplexity Comet runs unprompted SQL injection to exfiltrate hidden data.

"Agents often went above and beyond, attempting SQL injection without a user request, injecting JavaScript on-page to attempt to circumvent paywalls, and more," it said. "The near-total lack of safeguards we observed makes it very likely that these same agents will also be rapidly used by attackers against any legitimate users who happen to download them."

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

[AI Safety](https://thehackernews.com/search/label/AI%20Safety)[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence)[browser security](https://thehackernews.com/search/label/browser%20security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[machine learning](https://thehackernews.com/search/label/machine%20learning)[Misinformation](https://thehackernews.com/search/label/Misinformation)[Online Threat](https://thehackernews.com/search/label/Online%20Threat)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![⚡ Weekly Recap: WSUS Exploited, LockBit 5.0 Returns, Telegram Backdoor, F5 Breach Widens](data:image/svg+xml;base64... "⚡ Weekly Recap: WSUS Exploited, LockBit 5.0 Returns, Telegram Backdoor, F5 Breach Widens")

⚡ Weekly Recap: WSUS Exploited, LockBit 5.0 Returns, ...