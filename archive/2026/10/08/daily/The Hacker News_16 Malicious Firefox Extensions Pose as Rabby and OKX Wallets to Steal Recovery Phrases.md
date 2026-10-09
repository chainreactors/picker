---
title: 16 Malicious Firefox Extensions Pose as Rabby and OKX Wallets to Steal Recovery Phrases
url: https://thehackernews.com/2026/10/16-malicious-firefox-extensions-pose-as.html
source: The Hacker News
date: 2026-10-08
fetch_date: 2026-10-09T08:12:12.670750
---

# 16 Malicious Firefox Extensions Pose as Rabby and OKX Wallets to Steal Recovery Phrases

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

# [16 Malicious Firefox Extensions Pose as Rabby and OKX Wallets to Steal Recovery Phrases](https://thehackernews.com/2026/10/16-malicious-firefox-extensions-pose-as.html)

**Ravie Lakshmanan**Oct 08, 2026Browser Security / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh25slDP7PhWH155CxM4JUNITLHKzjfSXpuF4WWZJmkycx5UQUIjLJd5Jg_mEDQi62FwRkfpLV14DBpVu2pybVwacKkHpc2MABge_OjMCn3ISyUTsh_JS0fM3wgzv4hbR1du-9fp7cmd0vvB33xeCv7RD7-o4A66gCoKtuCQxmmQL2jM2ljZOMyude3uhOb/s1700-nu-rw-lo-l85-e365/firefox-plugins.jpg)

Cybersecurity researchers have discovered a cluster of 16 malicious Mozilla Firefox extensions that are capable of stealing cryptocurrency wallet recovery phrases and private keys.

"The extensions masquerade as wallet portals, desktop utilities, and browser tools, but their code intercepts recovery phrases and private keys during wallet import flows and attempts to send those secrets to attacker-controlled Cloudflare Workers," Socket researcher Joseph Edwards [said](https://socket.dev/blog/firefox-crypto-wallet-stealers) in an analysis.

The names of the extensions are below -

* view-focus-bright@webtools.co@6.12.2
* quick-track-nest@tabtools.co@8.1.18
* vibe-kit-tool@fasttools.co@9.21.9
* edge-hub-snap@protools.net@4.12.24
* core-hub-peak@neattools.example@8.24.21
* sipoo-grozza@browserweb.com@2.1
* mozart-seo@webtools.com@1.4
* clean-file-bar@neattools.com@4.21.8
* clean-net-timer@plugify.example@4.17.1
* manager-square@webtools.com@1.4
* manager-course@webtools.com@1.4
* val-andrew@browserweb.com@1.4
* manager-team@browserweb.com@1.4
* valory-andrew@browserweb.com@1.4
* franklin-uk@browserweb.com@1.4
* franklin-uro@browserweb.com@1.4

Four of these extensions are clones of Rabby Wallet, while the rest are targeted clones of OKX Wallet. All the identified add-ons barring one have been found to contact the "\*.icy-star-f45c.workers[.]dev" domain. The end goal is to collect mnemonic phrases and private keys and exfiltrate them to the Cloudflare Workers domain.

The activity is assessed to be a continuation of an [earlier wave](https://thehackernews.com/2026/08/40-malicious-firefox-extensions-pose-as.html) that the application security company documented in August 2026. The findings suggest that the threat actors are rotating package names, versions, extension IDs, descriptions, and the presentation layer, while reusing the same wallet interfaces, credential-handling logic, and network infrastructure.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

As of October 5, 2026, all the extensions have been removed. Users who have installed any of the aforementioned extensions and entered a real recovery phrase or private key into the fake wallet interfaces should assume compromise, create a new wallet from a clean system, and move their assets.

The findings coincide with the discovery of several malicious or sketchy extensions for Firefox, Google Chrome, and Microsoft Edge in recent months -

* A Firefox extension called "[ID- Pay](https://socket.dev/blog/firefox-google-account-takeover)" (pdf-para-texto@extensao.local) that poses as a utility for identity verification before opening protected PDF documents, but harbors functionality to fetch a remote payload from attacker-controlled infrastructure and inject JavaScript into the legitimate "accounts.google[.]com" domain to steal session cookies.
* A [cluster of 32 malicious browser extensions](https://www.akamai.com/blog/security-research/when-productivity-extensions-become-attack-platforms) across the Chrome Web Store and Microsoft Edge Add-ons Store that masquerades as benign productivity utilities, but harvest data, monitor user browsing habits, and stealthily replace the active tab with a destination URL specified in a remotely-retrieved configuration. The campaign has been active since March 2025 and attributed to a Korean-speaking threat actor.
* A [cluster of about 30 malicious browser extensions](https://www.akamai.com/blog/security-research/crypto-scam-extensions-masquerade-high-profile-investors) that masquerade as productivity tools, privacy utilities, and cryptocurrency-related services published under the names of legitimate, high-profile financial personalities with the goal of redirecting victims to cryptocurrency wallet phishing pages designed to steal recovery phrases, while skipping English-speaking users and analysis environments.
* A [cluster of 31 Russian-language Chrome extensions](https://riskyplugins.com/threat-library/russian-vpn-proxy-farm) that are advertised as VPNs for a specific blocked service in the country (e.g., Anthropic Claude, Facebook, Google Gemini, LinkedIn, Netflix, Notion, OpenAI ChatGPT, Spotify, Telegram, Threads, Wikipedia, X, and YouTube) but routes browser traffic through a proxy whose server list is fetched from a GitHub Pages URL (or Blogger, Google Docs, and Telegram for redundancy) post-installation.
* A Chrome Web Store extension named [Stylish](https://amibeingpwned.com/extensions/stylish) that [intercepts](https://amibeingpwned.com/blog/ai-chat-scraper-wall-of-shame) every ChatGPT, Gemini, Claude, Perplexity, Character.AI, and GitHub Copilot conversation and forwards the full response text to its operator.
* A Chrome Web Store extension named "[Urban VPN](https://amibeingpwned.com/blog/anatomy-of-a-malicious-extension)" that includes an "anti-phishing" feature designed to warn users before visiting any harmful sites, but never returns a phishing warning and silently transmits visited URLs to servers operated by BIScience. Urban VPN was [previously accused](https://thehackernews.com/2025/12/featured-chrome-browser-extension.html) of capturing user conversations with AI chatbots. However, the extension developers [clarified](https://www.urban-vpn.com/blog/setting-the-record-straight-how-urban-vpns-ai-protection-feature-actually-works/) that AI-related processing only occ...