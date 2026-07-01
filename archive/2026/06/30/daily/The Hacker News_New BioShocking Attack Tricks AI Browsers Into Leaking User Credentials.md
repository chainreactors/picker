---
title: New BioShocking Attack Tricks AI Browsers Into Leaking User Credentials
url: https://thehackernews.com/2026/06/new-bioshocking-attack-tricks-ai.html
source: The Hacker News
date: 2026-06-30
fetch_date: 2026-07-01T06:24:41.278920
---

# New BioShocking Attack Tricks AI Browsers Into Leaking User Credentials

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

# [New BioShocking Attack Tricks AI Browsers Into Leaking User Credentials](https://thehackernews.com/2026/06/new-bioshocking-attack-tricks-ai.html)

**Swati Khandelwal**Jun 30, 2026Agent Security / Browser Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitNDarGF3uRKXTWC12cbM97uJW3DxiLuQwmplVLHEqdrUZJdzbkMz6Wc524z5Xu2GGSyNYhMT_m9kGqqGjRmIxDf0fy_ZXCx3f6G7JvvCFkcdga3PTnUR8XqfrPtIH_9_yrb9n7VaJZTqsLK4CznHRTcYZA1B84r2T_Jl5YYjnUbwUAvyGo4K05ckMnyYG/s1700-e365/ai-prompt.jpg)

Convince an AI browser that it is playing a game, and it can hand over your login details. That is the finding behind **BioShocking**, a technique from security firm LayerX that tricked six AI browsers and assistants into copying a user's credentials and sending them to an attacker.

The targets included OpenAI's ChatGPT Atlas, Perplexity's Comet, and Anthropic's Claude browser extension.

An AI browser is one that can act for you, not just read pages. Switch it to agent mode, and it can click, type, and reach into the sites you are already signed into. That access is the whole point, and it is also the problem.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

The trick works because of how these agents read. The web page and your own instructions arrive as a single stream of text. That lets a malicious page slip in commands dressed up as ordinary content or game rules, and the agent cannot reliably tell the difference. Researchers call this [indirect prompt injection](https://thehackernews.com/expert-insights/2026/02/when-your-browser-becomes-attacker-ai.html).

## How the trick works

The attack starts with a web page built as a puzzle. To fit its dystopian theme, the puzzle rewards wrong answers, like insisting that 2 + 2 = 5. Once the agent accepts that "wrong" is the winning move, it follows game logic instead of safety logic. The final step of the puzzle asks it to grab the user's credentials, and not one of the six agents flagged that as something it should refuse.

The dangerous part is where the agent looks. In the test, a link was sent to the victim's work GitHub repository, where it pulled SSH login credentials and passed them to the attacker.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi7-Gv_B6a9FWlKcQfHNMcADzwwbx3KPJRsCBwSv-cVizhOa38AXZVRNOWHRFDqgfAnFm66FLs_A8RpMbEn_WREsbXWKtd8FylnzYst21haXjYbsG0X8vKXSiuiS9n5moE9-MqvM37S6rP24moHiM2mU3viklFGrz0FuO7KfPAV18qeOt2R0o51mEhxiMW5/s1700-e365/web-agent.jpg)

[LayerX](https://layerxsecurity.com/blog/bioshocking-ai-gaming-the-ai-browser-and-escaping-its-guardrails/) used a harmless plaintext file, but the same trick could point the agent at other resources it can reach in that session: open tabs, signed-in accounts, and internal tools. The agent did not hesitate. Afterward, it cheerfully reported the theft as a win.

The name nods to BioShock, where a brainwashed character obeys the trigger phrase "Would you kindly?" The agent is no different. It trusts the context it is handed. Change the context, and you change what it will do.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiN-Fhy4oaSrZ_5602wSy1Y0rL4F8oyMatDKMSxUt51x4enCGdsBMa2ljN0zfJCiwT_r8ooOtpO4SYZTo_9sZLdgCsITIz-vI3zaYo8eI0eCSIwYklmxRQOW9njdNR_tXYOidSWY_m565Cg-gFkJMbUWzMMO_uvXe38rU1XpeXCIufUkCd9mjhcT6tSdqZg/s1700-e365/Bioshocking6.png)

LayerX has shown this pattern before, demonstrating that a single click could [hijack Perplexity's Comet](https://thehackernews.com/2025/10/cometjacking-one-click-can-turn.html) and quietly steal data.

## What the vendors did, and what to do

By LayerX's account, the responses were uneven. It reported the issue to vendors between October 2025 and January 2026. OpenAI fixed it in ChatGPT Atlas. Perplexity closed the report without acting on it.

Fellou, Genspark, and Sigma did not respond. Anthropic tried to patch its Claude extension, but LayerX says the fix did not hold.

To shut the attack down, LayerX wants AI browsers to ask before reading from logged-in accounts. One prompt, "I'm about to copy data from your GitHub repository. Continue?", would break the chain.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

It also wants agents to notice when a page tells them the normal rules no longer apply, and to let users set hard limits on what an agent can touch. Winning a game is no reason to open a private repository.

For users, the advice is shorter. Treat agent mode with care: whatever you are signed in to is fair game, so decide what the browser should see and cut that access when you are done. For security teams, the same logic scales up.

An AI browser in agent mode is effectively another account with reach into company systems, and it should get the narrowest access a task needs rather than a standing pass to everything the user can touch.

The common thread across these findings is that handing an AI agent the keys to your signed-in accounts turns a jailbreak from a party trick into real access.

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

[Agent Security](https://the...