---
title: 282 iOS AI Apps Leak API Keys and Open AI Proxy Access in Network Traffic Study
url: https://thehackernews.com/2026/06/282-ios-apps-found-leaking-llm-api-keys.html
source: The Hacker News
date: 2026-06-30
fetch_date: 2026-07-01T06:24:40.764473
---

# 282 iOS AI Apps Leak API Keys and Open AI Proxy Access in Network Traffic Study

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

# [282 iOS AI Apps Leak API Keys and Open AI Proxy Access in Network Traffic Study](https://thehackernews.com/2026/06/282-ios-apps-found-leaking-llm-api-keys.html)

**Swati Khandelwal**Jun 30, 2026API Security / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJ9nmTBu_vYBf5fRZV4Jc-qtFGPySofVDYHUd-9-ogdve-M4Qd4j7_CnH9Zmvln6O3nfXSsDqQiMoL3rDYBSXZSrXlkCnSWSQUdAYJX1PkRzmytlVaYAc2AyrFOCpo9doU58gO6Gl5fQ-0SZ5D3yGP2SspNgK0U4f5jViSBnY_PAMUOjr42Nt8OLrhnTsQ/s1700-e365/llm-keys.jpg)

Researchers tested 444 AI chatbot apps for iPhone and found that 282 of them, nearly two-thirds, exposed paid AI access through their network traffic.

In many cases, the path in was visible just by watching what the app sent: a plaintext API key, a reusable token, or a backend server that accepted requests with no key at all.

Whoever grabs it can send model requests on the developer's account, and the developer pays the bill. Three months after the researchers warned the developers, only 28% had fixed it.

The work, from researchers at Wake Forest University, is the [first in-depth study of the problem on iOS](https://arxiv.org/abs/2606.12212). It is striking partly because of how little effort the snooping took. The team used a tool they built, **LLMKeyLens**, that watches an app's traffic and pulls out the credentials as they go by. No jailbreaking, no cracking the app open.

The key is the secret that lets the app call a service like OpenAI or Google Gemini. Embed it in the app, and it is exposed with every request the app makes.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

All 282 fell into one of three groups:

* **Plaintext keys (54 apps):** the key is sent in the open, readable from a single captured request.
* **No key needed (92 apps):** the app routes requests through a server that answers anyone, with no check on who is asking. An open relay to a paid AI account.
* **Replayable tokens (136 apps, the most common):** the app hands out temporary access tokens instead of the raw key, the approach that is supposed to be safer, but the tokens leak in the same traffic and were usually still valid when captured. Some were not temporary at all, as the cases below show.

For 28 of the 54 plaintext-key apps, the same request also exposed the app's hidden system prompt, the behind-the-scenes instructions that define what the assistant does and how the product works. One capture, two prizes.

The leaks span at least ten AI providers, with OpenAI the most common, and reach across 13 app categories. Productivity apps were the biggest group; health and fitness apps had the highest leak rate. Finance and medical apps, notably, leaked nothing. Most affected apps were small, but not all of them: one had more than two million user ratings.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiuWDQ-Ngp2mWzjyVIas-osWjfekjbHI6jRAPMjLjkHXNIctVTk00Cw0QsuT6xdS8m3k06FPr6-KhmuujrWNdm67FUN54etFy0fDr0SAMTNZtTzImLiNpH56-KIaTCeinyeX0XGxH2F7G38L1YqNFdyAfozE2FvXprPRjnMfGiXm4apsL2srK3qZ9yBUbht/s1700-e365/ios.jpg)

This is not theoretical money. Stolen AI keys feed a practice the industry calls [LLMjacking](https://thehackernews.com/2024/05/researchers-uncover-llmjacking-scheme.html), where attackers run other people's keys to get free model access. Sysdig [calculated a worst-case scenario](https://www.sysdig.com/blog/llmjacking-stolen-cloud-credentials-used-in-new-ai-attack) in which stolen credentials could run up more than $46,000 a day in AI charges.

The researchers notified all 282 developers and waited three months. Only 28% had clearly fixed it.

Another 23% were still wide open; the leaked access was working. The rest had gone offline, become unreachable, or returned errors. The token apps were often the worst: one popular app, with over 100,000 ratings, set its access token to expire in the year 2125, a hundred-year pass.

Another app's one-hour token still worked 128 days after it had expired.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

The fix is old advice that few followed: Do not put the key in the app. Route AI calls through your own server, make that server check who is calling, and revoke any key that has already leaked.

The researchers also want AI providers to label client-side keys as unsafe in their documentation and to flag keys that suddenly get used by thousands of devices, and they want Apple to screen for this during App Store review.

The pattern is familiar. A 2025 study, [LM-Scout](https://arxiv.org/abs/2505.08204), found the same insecure AI wiring across Android apps and automatically broke into 120 of them. A larger audit, [Leaky Apps](https://doi.org/10.1145/3719027.3765033), pulled secrets from thousands of Android and iOS apps and found developers routinely fail to revoke keys even after removing them, leaving the old ones live.

Others have probed the [broader LLM app ecosystem](https://arxiv.org/abs/2407.08422) for similar holes. The AI rush has not changed the habit. It has raised the bill, because a leaked key is now charged with the token.

One caveat: the two-thirds figure is a floor. Many apps blocked the interception entirely, and the study covers only the US App Store in late 2025, so the true rate is likely higher.

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
[**Sh...