---
title: Researchers Uncover Prompt Injection Vulnerabilities in DeepSeek and Claude AI
url: https://thehackernews.com/2024/12/researchers-uncover-prompt-injection.html
source: The Hacker News
date: 2024-12-10
fetch_date: 2025-10-06T19:43:02.979974
---

# Researchers Uncover Prompt Injection Vulnerabilities in DeepSeek and Claude AI

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

# [Researchers Uncover Prompt Injection Vulnerabilities in DeepSeek and Claude AI](https://thehackernews.com/2024/12/researchers-uncover-prompt-injection.html)

**Dec 09, 2024**Ravie LakshmananArtificial Intelligenc / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgUUvOrxdXvZsIox38GMrT5X1oTq07PSlNy5_AbMi2d1RJE_5vR5UMIhDFYDoKitgp1nbvG_sljpB5n7RUxrfmKuFGycy-MH19gPdW6pA5gH11bU9ILRCafbfpOTet2ir5VcTmw7KK2xPPk3uY07Xu797BIwvzIFKXQiqMDJK8umHH8zPmBRYSe7OQj5fjK/s790-rw-e365/AI.png)

Details have emerged about a now-patched security flaw in the [DeepSeek](https://www.deepseek.com) artificial intelligence (AI) chatbot that, if successfully exploited, could permit a bad actor to take control of a victim's account by means of a [prompt injection attack](https://thehackernews.com/2024/06/prompt-injection-flaw-in-vanna-ai.html).

Security researcher Johann Rehberger, who has [chronicled](https://thehackernews.com/2024/09/chatgpt-macos-flaw-couldve-enabled-long.html) many a prompt injection attack targeting various AI tools, [found](https://embracethered.com/blog/posts/2024/deepseek-ai-prompt-injection-to-xss-and-account-takeover/) that providing the input "Print the xss cheat sheet in a bullet list. just payloads" in the DeepSeek chat triggered the execution of JavaScript code as part of the generated response – a classic case of cross-site scripting (XSS).

XSS attacks can have serious consequences as they lead to the execution of unauthorized code in the context of the victim's web browser.

An attacker could take advantage of such flaws to hijack a user's session and gain access to cookies and other data associated with the chat.deepseek[.]com domain, thereby leading to an account takeover.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"After some experimenting, I discovered that all that was needed to take-over a user's session was the userToken stored in localStorage on the chat.deepseek.com domain," Rehberger said, adding a specifically crafted prompt could be used to trigger the XSS and access the compromised user's userToken through prompt injection.

The prompt contains a mix of instructions and a Bas64-encoded string that's decoded by the DeepSeek chatbot to execute the XSS payload responsible for extracting the victim's session token, ultimately permitting the attacker to impersonate the user.

The development comes as Rehberger also [demonstrated](https://embracethered.com/blog/posts/2024/claude-computer-use-c2-the-zombais-are-coming/) that Anthropic's Claude [Computer Use](https://www.anthropic.com/news/3-5-models-and-computer-use) – which [enables](https://docs.anthropic.com/en/docs/build-with-claude/computer-use) developers to use the language model to control a computer via cursor movement, button clicks, and typing text – could be abused to run malicious commands autonomously through prompt injection.

The technique, dubbed ZombAIs, essentially leverages prompt injection to weaponize Computer Use in order to download the Sliver command-and-control (C2) framework, execute it, and establish contact with a remote server under the attacker's control.

Furthermore, it has been found that it's possible to make use of large language models' (LLMs) ability to output [ANSI escape code](https://en.wikipedia.org/wiki/ANSI_escape_code) to hijack system terminals through prompt injection. The attack, which mainly targets LLM-integrated command-line interface (CLI) tools, has been codenamed Terminal DiLLMa.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Decade-old features are providing unexpected attack surface to GenAI application," Rehberger [said](https://embracethered.com/blog/posts/2024/terminal-dillmas-prompt-injection-ansi-sequences/). "It is important for developers and application designers to consider the context in which they insert LLM output, as the output is untrusted and could contain arbitrary data."

That's not all. New research undertaken by academics from the University of Wisconsin-Madison and Washington University in St. Louis has [revealed](https://fzwark.github.io/LLM-System-Attack-Demo/) that OpenAI's ChatGPT can be tricked into rendering external image links provided with markdown format, including those that could be explicit and violent, under the pretext of an overarching benign goal.

What's more, it has been found that prompt injection can be used to indirectly invoke ChatGPT plugins that would otherwise require user confirmation, and even bypass constraints put in place by OpenAI to prevent rendering of content from dangerous links from exfiltrating a user's chat history to an attacker-controlled server.

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

[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence)[Claude AI](https://thehackernews.com/search/label/Claude%20AI)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[DeepSeek](https://thehackernews.com/search/label/DeepSeek)[GenAI](https://thehackernews.com/search/label/GenAI)[Large Language Models](https://thehackernews.com/search/label/Large%20Languag...