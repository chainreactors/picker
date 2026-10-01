---
title: Know Your Enemy: Browser-Based Attack Techniques in 2026
url: https://thehackernews.com/2026/09/know-your-enemy-browser-based-attack.html
source: The Hacker News
date: 2026-09-30
fetch_date: 2026-10-01T07:59:25.585119
---

# Know Your Enemy: Browser-Based Attack Techniques in 2026

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

# [Know Your Enemy: Browser-Based Attack Techniques in 2026](https://thehackernews.com/2026/09/know-your-enemy-browser-based-attack.html)

**The Hacker News**Sep 30, 2026Web Security / Phishing

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHy63Qp6WLBgRhCGaWARbZzjcdu6DhFo9JxZXTE9Rt4B42ImiW_cB0Fdq2yV_HYiZohMmVMRxTu1DxcbiOE9GNu4lAF2HZZ61QiCrWSEKGJFjEt5E5pKpXhjGK9DsZrqTxHFqF2IIaToRSTItghSELEiA_kgTP69_iOwbHdT35ht3yLCqIiNb5ysgDeuM/s1700-nu-rw-lo-l85-e365/push-phish.jpg)

Given that the browser is where business apps are accessed and used, it makes sense that attacks are happening there too. Most breaches today begin in a browser session. Often, they never leave it, with the entire attack chain from initial access to exfiltration playing out in the browser.

Here are the six most dangerous techniques that should be on every security team's radar in 2026.

## **1. Phishing for credentials and sessions**

Modern phishing kits don't just steal passwords — they intercept live sessions. Reverse-proxy adversary-in-the-middle (AiTM) kits like Tycoon2FA, Sneaky2FA, and Evilginx relay credentials and session tokens in real time, bypassing most forms of MFA. These kits are sold as turnkey Phishing-as-a-Service platforms with anti-bot protection, dynamic lure generation, and automated session replay — reducing the barrier to sophisticated phishing to effectively zero.

At the same time, phishing delivery has moved well beyond email — attackers deliver links over instant messaging, social media, SMS, malicious ads, and in-app messaging. According to Push data, roughly 1 in every 2 phishing attacks is delivered outside of email entirely. And with 89% of phishing domains active for fewer than two days, organizations relying on blocklists are playing a losing game.

## **2. Malicious copy and paste (ClickFix)**

Since late 2024, attackers have been tricking users into copying and executing malicious commands under the pretext of "fixing" an issue — most commonly a fake CAPTCHA or verification challenge. Microsoft's Digital Defense Report identified ClickFix as the most common initial access vector, accounting for 47% of observed attacks. ClickFix became the dominant technique in Push detections for the first time in Q2 2026, reaching 52% of total detections.

ClickFix is a hybrid of browser and endpoint targeting — the lure is delivered via the browser, but the user copies and runs malicious scripts locally, typically installing Remote Access Tools or infostealer malware. Four in five ClickFix payloads intercepted by Push are accessed from search engines via compromised sites, malvertising, and SEO poisoning, completely bypassing email security.

The technique continues to evolve. [InstallFix](https://pushsecurity.com/blog/installfix/?utm_campaign=54037305-2026-Q4%20Browser%20Attacks%20Experience&utm_source=the-hacker-news&utm_medium=article) uses malvertised fake install pages for developer tools like Claude Code and NotebookLM, where the install command has been replaced with a malicious one. The [LLMShare](https://pushsecurity.com/blog/llmshare-malvertising-campaign/?utm_campaign=54037305-2026-Q4%20Browser%20Attacks%20Experience&utm_source=the-hacker-news&utm_medium=article) campaign used shared conversations on AI chatbot platforms to deliver malware via pages hosted on trusted domains. But every variant shares one thing: a malicious copy-and-paste event in the browser.

## **3. Authorization phishing**

A growing class of attacks targets what happens after the login. Instead of stealing a session from the authentication flow, [authorization phishing](https://pushsecurity.com/blog/authorization-phishing?utm_campaign=54037305-2026-Q4%20Browser%20Attacks%20Experience&utm_source=the-hacker-news&utm_medium=article) abuses OAuth mechanisms — consent grants, device code flows, and token exchanges — to obtain access tokens. The attacker never touches the authentication flow, which means every form of MFA, including phishing-resistant passkeys, is irrelevant.

Three techniques currently fall under this umbrella. **Consent phishing** sees the victim authorize a malicious third-party app via an OAuth consent grant. **Device code phishing** abuses the RFC 8628 device authorization grant to circumvent standard authentication entirely — Push now tracks [30+ distinct kits](https://pushsecurity.com/blog/device-code-phishing?utm_campaign=54037305-2026-Q4+Browser+Attacks+Experience&utm_source=the-hacker-news&utm_medium=article) offering the technique. **ConsentFix** is a ClickFix-OAuth hybrid [first observed in Russian APT29 campaigns](https://pushsecurity.com/blog/consentfix/?utm_campaign=54037305-2026-Q4%20Browser%20Attacks%20Experience&utm_source=the-hacker-news&utm_medium=article) that has since been [commoditized into criminal tooling](https://pushsecurity.com/blog/consentfix-v3-analyzing-a-new-toolkit/?utm_campaign=54037305-2026-Q4%20Browser%20Attacks%20Experience&utm_source=the-hacker-news&utm_medium=article).

## **4. Malicious browser extensions**

Attackers use malicious extensions to steal data, log keystrokes, and intercept credentials and tokens as they transit the browser. Most malicious extensions didn't start that way — attackers acquire legitimate extensions and wait until install counts reach maximum impact before deploying a malicious update.

An analysis across Push customers found that **46.76% of extensions have the permission combinations needed for account takeover with no user interaction**. AI browser extensions add a further dimension — the Verizon DBIR 2026 found that more than 15% of corporate users had unauthorized AI browser extensions installed, and [Push found](https://pushsecurity.com/blog/what-push-data-reveals-about-the-state-of-shadow-ai) an average of 17 unique AI extensions per company (with one team running 163), creating data exfiltration pathways independent of traditional DLP controls.

Static risk scoring ...