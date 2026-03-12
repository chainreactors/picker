---
title: Researchers Trick Perplexity's Comet AI Browser Into Phishing Scam in Under Four Minutes
url: https://thehackernews.com/2026/03/researchers-trick-perplexitys-comet-ai.html
source: The Hacker News
date: 2026-03-11
fetch_date: 2026-03-12T04:09:06.670890
---

# Researchers Trick Perplexity's Comet AI Browser Into Phishing Scam in Under Four Minutes

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

# [Researchers Trick Perplexity's Comet AI Browser Into Phishing Scam in Under Four Minutes](https://thehackernews.com/2026/03/researchers-trick-perplexitys-comet-ai.html)

**Ravie Lakshmanan**Mar 11, 2026Artificial Intelligence / Browser Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHkDTAnMilk2AM0Yg71UjZJul-Q0y_QvAqY97sCemt73LNrjo7Rwp7uHjmFpSmeV75WwsRN5tRMdcgACXJFnv7FMOqb9qAnaOoyek1f0KubQtDtdkWZAh6g8ZZXNSwLLmAZYONBXIM-xa9QNbO9qQDI4REUUobzfhTuBJED4ilM5CBA0AmQ6zfyUWpvQDo/s1700-e365/agent.png)

Agentic web browsers that leverage artificial intelligence (AI) capabilities to autonomously execute actions across multiple websites on behalf of a user could be trained and tricked into falling prey to phishing and scam traps.

The attack, at its core, takes advantage of AI browsers' tendency to reason their actions and use it against the model itself to lower their security guardrails, Guardio [said](https://guard.io/labs/agenticblabbering---how-ai-browsers-verbose-reasoning-fuels-the-ultimate-scamming-machine) in a report shared with The Hacker News ahead of publication.

"The AI now operates in real time, inside messy and dynamic pages, while continuously requesting information, making decisions, and narrating its actions along the way. Well, 'narrating' is quite an understatement - It blabbers, and way too much!," security researcher Shaked Chen said.

"This is what we call **Agentic Blabbering**: the AI Browser exposing what it sees, what it believes is happening, what it plans to do next, and what signals it considers suspicious or safe."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

By intercepting this traffic between the browser and the AI services running on the vendor's servers and feeding it as input to a Generative Adversarial Network ([GAN](https://en.wikipedia.org/wiki/Generative_adversarial_network)), Guardio said it was able to make Perplexity's Comet AI browser fall victim to a phishing scam in under four minutes.

The research builds on prior techniques like [VibeScamming](https://thehackernews.com/2025/04/lovable-ai-found-most-vulnerable-to.html) and [Scamlexity](https://thehackernews.com/2025/08/experts-find-ai-browsers-can-be-tricked.html), which found that vibe-coding platforms and AI browsers could be coaxed into generating scam pages or carrying out malicious actions via hidden prompt injections. In other words, with the AI agent handling the tasks without constant human supervision, there arises a shift in the attack surface wherein a scam no longer has to deceive a user. Rather, it aims to trick the AI model itself.

"If you can observe what the agent flags as suspicious, hesitates on, and more importantly, what it thinks and blabbers about the page, you can use that as a training signal," Chen explained. "The scam evolves until the AI Browser reliably walks into the trap another AI set for it."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhl0jYugIHeLg7ZBeZoWjYpGz-30SvC5ghfoVZwOw2SyrWUqhWz5s_PERI0r6qLEcJL7So2CnCPkjyjN4Pwh8W_eomek_5J1ZRRYfC8ze3WM41y-gpiItaHSDMkmOQmmp4v7pc8WaAjg28fnla1YH8f7BrUnggVQWZzfxQoUOqlFAm7Y1cOYQE1soeHwkhj/s1700-e365/scam.png)

The idea, in a nutshell, is to build a "scamming machine" that iteratively optimizes and regenerates a phishing page until the agentic browser stops complaining and proceeds to carry out the threat actor's bidding, such as entering a victim's credentials on a bogus web page designed for carrying out a refund scam.

What makes this attack interesting and dangerous is that once the fraudster iterates on a web page until it works against a specific AI browser, it works on all users who rely on the same agent. Put differently, the target has shifted from the human user to the AI browser.

"This reveals the unfortunate near future we are facing: scams will not just be launched and adjusted in the wild, they will be trained offline, against the exact model millions rely on, until they work flawlessly on first contact," Guardio said. "Because when your AI Browser explains why it stopped, it teaches attackers how to bypass it."

The disclosure comes as Trail of Bits [demonstrated](https://blog.trailofbits.com/2026/02/20/using-threat-modeling-and-prompt-injection-to-audit-comet/) four [prompt injection techniques](https://arxiv.org/abs/2511.20597) against the Comet browser to extract users' private information from services like Gmail by exploiting the browser's AI assistant and exfiltrating the data to an attacker’s server when the user asks to summarize a web page under their control.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fs-report-d)

Last week, Zenity Labs also detailed two zero-click attacks affecting Perplexity's Comet that use [indirect prompt injection](https://thehackernews.com/2025/12/google-adds-layered-defenses-to-chrome.html) seeded within meeting invites to exfiltrate local files to an external server (aka [PerplexedComet](https://labs.zenity.io/p/perplexedbrowser-perplexity-s-agent-browser-can-leak-your-personal-pc-local-files)) or [hijack a user's 1Password account](https://labs.zenity.io/p/perplexedbrowser-how-attackers-can-weaponize-comet-to-takeover-your-1password-vault) if the [password manager extension](https://1password.com/blog/security-advisory-for-ai-assisted-browsing-with-the-1password-browser) is installed and unlocked. The issues, collectively codenamed PerplexedBrowser, have since been addressed by the AI company.

This is achieved by means of a prompt injection technique referred to as intent collision, which occurs "when the agent merges a benign user request with attacker-controlled instructions from untrusted web data into a single execution plan, without a reliable way to distinguish between the two," security researcher Stav Cohen said.

Prompt injection attacks remain a fundamental security challenge for large l...