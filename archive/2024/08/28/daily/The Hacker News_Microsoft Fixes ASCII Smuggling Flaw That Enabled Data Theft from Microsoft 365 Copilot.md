---
title: Microsoft Fixes ASCII Smuggling Flaw That Enabled Data Theft from Microsoft 365 Copilot
url: https://thehackernews.com/2024/08/microsoft-fixes-ascii-smuggling-flaw.html
source: The Hacker News
date: 2024-08-28
fetch_date: 2025-10-06T18:09:28.167921
---

# Microsoft Fixes ASCII Smuggling Flaw That Enabled Data Theft from Microsoft 365 Copilot

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

# [Microsoft Fixes ASCII Smuggling Flaw That Enabled Data Theft from Microsoft 365 Copilot](https://thehackernews.com/2024/08/microsoft-fixes-ascii-smuggling-flaw.html)

**Aug 27, 2024**Ravie LakshmananAI Security / Vulnerability

[![Microsoft Fixes ASCII Smuggling Flaw](data:image/png;base64... "Microsoft Fixes ASCII Smuggling Flaw")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlIxxfhgvEbEYDG3wHQ2eKqzhAqQ6QYBSgpg5F4fNXxf3N_OUK6wVpDby0mrHMMk89hVFAbePc8wJo_yt-NyNLTIexlKrKZ5e1vPOUQwWbzCgixXsOzFkD6-cTfHIh0ExIj-yeH0DoVcyLlWxNgyft-L_BWAyjZgJ6JSRzVVM7ncNvc0nDAUiGvO2F9PGu/s790-rw-e365/ms.png)

Details have emerged about a now-patched vulnerability in Microsoft 365 Copilot that could enable the theft of sensitive user information using a technique called ASCII smuggling.

"[ASCII Smuggling](https://embracethered.com/blog/posts/2024/hiding-and-finding-text-with-unicode-tags/) is a novel technique that uses special Unicode characters that mirror ASCII but are actually not visible in the user interface," security researcher Johann Rehberger [said](https://embracethered.com/blog/posts/2024/m365-copilot-prompt-injection-tool-invocation-and-data-exfil-using-ascii-smuggling/).

"This means that an attacker can have the [large language model] render, to the user, invisible data, and embed them within clickable hyperlinks. This technique basically stages the data for exfiltration!"

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The entire attack strings together a number of attack methods to fashion them into a reliable exploit chain. This includes the following steps -

* Trigger [prompt injection](https://thehackernews.com/2024/06/prompt-injection-flaw-in-vanna-ai.html) via malicious content concealed in a document shared on the chat to seize control of the chatbot
* Using a prompt injection payload to instruct Copilot to search for more emails and documents, a technique called [automatic tool invocation](https://embracethered.com/blog/posts/2024/llm-apps-automatic-tool-invocations/)
* Leveraging ASCII smuggling to entice the user into clicking on a link to exfiltrate valuable data to a third-party server

The net outcome of the attack is that sensitive data present in emails, including multi-factor authentication (MFA) codes, could be transmitted to an adversary-controlled server. Microsoft has since addressed the issues following responsible disclosure in January 2024.

The development comes as proof-of-concept (PoC) attacks have been [demonstrated](https://www.wired.com/story/microsoft-copilot-phishing-data-extraction/) against Microsoft's Copilot system to manipulate responses, exfiltrate private data, and dodge security protections, once again highlighting the need for monitoring risks in artificial intelligence (AI) tools.

The methods, detailed by [Zenity](https://labs.zenity.io/p/hsc24), allow malicious actors to perform retrieval-augmented generation ([RAG](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)) poisoning and indirect prompt injection leading to remote code execution attacks that can fully control Microsoft Copilot and other AI apps. In a hypothetical attack scenario, an external hacker with code execution capabilities could trick Copilot into providing users with phishing pages.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Perhaps one of the most novel attacks is the ability to turn the AI into a spear-phishing machine. The red-teaming technique, dubbed [LOLCopilot](https://github.com/mbrg/power-pwn), allows an attacker with access to a victim's email account to send phishing messages mimicking the compromised users' style.

Microsoft has also [acknowledged](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels?tabs=web) that publicly exposed Copilot bots created using Microsoft Copilot Studio and lacking any authentication protections could be an avenue for threat actors to extract sensitive information, assuming they have prior knowledge of the Copilot name or URL.

"Enterprises should evaluate their risk tolerance and exposure to prevent data leaks from Copilots (formerly Power Virtual Agents), and enable [Data Loss Prevention](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance) and other security controls accordingly to control creation and publication of Copilots," Rehberger [said](https://embracethered.com/blog/posts/2024/copilot-studio-protect-your-copilots/).

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

[AI Security](https://thehackernews.com/search/label/AI%20Security)[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence)[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data protection](https://thehackernews.com/search/label/data%20protection)[enterprise security](https://thehackernews.com/search/label/enterprise%20security)[hacking](https://thehackernews.com/search/label/hacking)[Information security](https://thehackernews.com/search/label/Information%20security)[Microsoft](https:/...