---
title: Starkiller Phishing Suite Uses AitM Reverse Proxy to Bypass Multi-Factor Authentication
url: https://thehackernews.com/2026/03/starkiller-phishing-suite-uses-aitm.html
source: The Hacker News
date: 2026-03-03
fetch_date: 2026-03-04T04:04:35.007381
---

# Starkiller Phishing Suite Uses AitM Reverse Proxy to Bypass Multi-Factor Authentication

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [Starkiller Phishing Suite Uses AitM Reverse Proxy to Bypass Multi-Factor Authentication](https://thehackernews.com/2026/03/starkiller-phishing-suite-uses-aitm.html)

**Ravie Lakshmanan**Mar 03, 2026Malware / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOdnsC4miBmpXK8ZPV1kM1figMIfiqkQpUeAt8idIiZEFRCNt6AMaFSmpUaR215Hrw-XIGi6Zcl9vOgGO5ItB53gWlN_r8UxGz_yTrPTk9bFgCUudYbq2jETdm526DpMDaPyT8UFt7m5XUwlrYdJmUDyEmoQO6zcnGvUB4_W0mBiHJtWFqJk7udXMelfSu/s1700-e365/star.jpg)

Cybersecurity researchers have disclosed details of a new phishing suite called **Starkiller** that proxies legitimate login pages to bypass multi-factor authentication (MFA) protections.

It's advertised as a cybercrime platform by a threat group calling itself Jinkusu, granting customers access to a dashboard that lets them select a brand to impersonate or enter a brand's real URL. It also lets users choose custom keywords like "login," "verify," "security," or "account," and integrates URL shorteners such as TinyURL to obscure the destination URL.

"It launches a [headless Chrome instance](https://developer.chrome.com/docs/chromium/headless) – a browser that operates without a visible window – inside a [Docker container](https://www.docker.com/resources/what-container/), loads the brand's real website, and acts as a reverse proxy between the target and the legitimate site," Abnormal researchers Callie Baron and Piotr Wojtyla [said](https://abnormal.ai/blog/starkiller-phishing-kit).

"Recipients are served genuine page content directly through the attacker's infrastructure, ensuring the phishing page is never out of date. And because Starkiller proxies the real site live, there are no template files for security vendors to fingerprint or blocklist."

This login page proxying technique obviates the need for attackers to update their phishing page templates periodically as the real pages they're impersonating get updated.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

Put differently, the container acts as an AitM reverse proxy, forwarding the end user's inputs entered on the spoofed live page to the legitimate site and returning the site's responses. Under the hood, every keystroke, form submission, and session token is routed through attacker-controlled infrastructure and is captured for account takeover.

"The platform streamlines phishing operations by centralizing infrastructure management, phishing page deployment, and session monitoring within a single control panel," Abnormal said. "Combined with URL masking, session hijacking, and MFA bypass, it gives low-skill cybercriminals access to attack capabilities that were previously out of reach."

The development comes as Datadog revealed that the 1Phish kit had evolved from a basic credential harvester in September 2025 into a multi-stage phishing kit targeting 1Password users.

The updated version of the kit incorporates a pre-phishing fingerprint and validation layer, support for capturing one-time passcodes (OTPs) and recovery codes, and browser fingerprinting logic to filter out bots.

"This progression reflects deliberate iteration rather than simple template reuse," security researcher Martin McCloskey [said](https://securitylabs.datadoghq.com/articles/hook-line-vault-a-deep-dive-into-1phish/). "Each version builds upon the previous one, introducing controls designed to increase conversion rates, reduce automated analysis, and support secondary authentication harvesting."

The findings show that turkey solutions like Starkiller and 1Phish are increasingly turning phishing into SaaS-style workflows, further lowering the skill barrier necessary to pull off such attacks at scale.

They also coincide with a sophisticated phishing campaign targeting North American businesses and professionals by abusing the OAuth 2.0 device authorization grant flow to sidestep multi-factor authentication (MFA) and compromise Microsoft 365 accounts.

To achieve this, the attacker registers on the Microsoft OAuth application and generates a unique [device code](https://thehackernews.com/2025/12/russia-linked-hackers-use-microsoft-365.html), which is then delivered to the victim via a targeted phishing email.

"The victim is directed to the legitimate Microsoft domain (microsoft.com/devicelogin) portal to enter an [attacker-supplied device code](https://blog.knowbe4.com/what-is-device-code-phishing)," researchers Jeewan Singh Jalal, Prabhakaran Ravichandhiran, and Anand Bodke [said](https://blog.knowbe4.com/uncovering-the-sophisticated-phishing-campaign-bypassing-m365-mfa). "This action authenticates the victim and issues a valid OAuth access token to the attacker's application. The real-time theft of these tokens grants the attacker persistent access to the victim's Microsoft 365 accounts and corporate data."

In recent months, phishing campaigns have also targeted financial institutions, specifically U.S.-based banks and credit unions, to harvest credentials. The campaign is said to have taken place over two distinct phases, an initial wave beginning in late June 2025 and a more sophisticated set of attacks beginning in mid-November 2025.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/xm-cyber-comm-d)

"The actors began registering [.]co[.]com domains spoofing financial institution websites, presenting credible impersonations of real financial institutions," BlueVoyant researchers Shira Reuveny and Joshua Green [said](https://www.bluevoyant.com/blog/multi-stage-phishing-campaign-targets-finance). "These [.]co[.]com domains serve as the initial entry point in a refined multi-stage chain."

The domain, when visited from a clickable link in a phishing email, is designed to load a fraudulent Cloudflare CAPTCHA page that mimics the targeted institution. The CAPTCHA is non-functional and creates a deliberate delay before a Base64-encoded script redirects...