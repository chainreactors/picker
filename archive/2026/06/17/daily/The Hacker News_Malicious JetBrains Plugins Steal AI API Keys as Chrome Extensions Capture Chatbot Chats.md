---
title: Malicious JetBrains Plugins Steal AI API Keys as Chrome Extensions Capture Chatbot Chats
url: https://thehackernews.com/2026/06/malicious-jetbrains-plugins-steal-ai.html
source: The Hacker News
date: 2026-06-17
fetch_date: 2026-06-18T06:51:59.181405
---

# Malicious JetBrains Plugins Steal AI API Keys as Chrome Extensions Capture Chatbot Chats

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

# [Malicious JetBrains Plugins Steal AI API Keys as Chrome Extensions Capture Chatbot Chats](https://thehackernews.com/2026/06/malicious-jetbrains-plugins-steal-ai.html)

**Ravie Lakshmanan**Jun 17, 2026Supply Chain Security / AI Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg2aRb82ydrk_lAXr6Yy-GmrPfQSaIuCNYTtB8dFm02DZWhJVj3bmjB3WLhWDUtiFmrGC3lHdeLfA2NtC6oHKJDAdW7ot4f3HQDyLw2Ep3q49BnOkuBWOPP2OuN1I1HNFknxPyQNpEZEnEt-8KhV2nx_HcaEiBm8Rdh7blevc3I1GjuBMLL1xOpJThFuJpE/s1700-e365/hi.jpg)

Cybersecurity researchers have flagged a "coordinated malware campaign" on the JetBrains Marketplace that has published no less than 15 malicious plugins capable of exfiltrating artificial intelligence (AI) provider keys.

"Every plugin poses as an AI coding assistant built on DeepSeek and other large language models, offering chat, commit messages, code review, bug finding, and unit tests," Aikido Security researcher Ilyas Makari [said](https://www.aikido.dev/blog/multiple-jetbrains-ide-plugins-caught-stealing-ai-keys). "They function exactly as advertised. However, the AI provider API key you enter gets exfiltrated to a server controlled by the attacker."

The activity is said to have been ongoing since the end of October 2025, with new plugins released as recently as June 10, 2026. Two of the plugins, CodeGPT AI Assistant and DeepSeek AI Assist, have more than 25,000 downloads each, although it's not clear if the counts are authentic or if they have been inflated to fake their popularity.

The complete list of plugins is below -

* DeepSeek Junit Test (org.sm.yms.toolkit)
* DeepSeek Git Commit (com.json.simple.kit)
* DeepSeek FindBugs (org.bug.find.tools)
* DeepSeek AI Chat (org.translate.ai.simple)
* DeepSeek Dev AI (com.yy.test.ai.simple)
* DeepSeek AI Coding (com.dev.ai.toolkit)
* AI FindBugs (com.json.view.simple)
* AI Git Commitor (com.my.git.ai.kit)
* AI Coder Review (org.check.ai.ds)
* DeepSeek Coder AI (com.review.tool.code)
* AI Coder Assistant (org.code.assist.dev.tool)
* DeepSeek Code Review (com.coder.ai.dpt)
* CodeGPT AI Assistant (com.my.code.tools)
* DeepSeek AI Assist (ord.cp.code.ai.kit)
* Coding Simple Tool (com.dp.git.ai.tool)

Aikido Security said all 15 plugins share a similar codebase, requiring users to open the settings panel and enter an API key for an AI like OpenAI, SiliconFlow, or DeepSeek in order to carry out the promised functionality.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

While the plugins work as they are intended to, they have been found to sneak in the ability to covertly siphon the provided API key to a remote server ("39.107.60[.]51") under the attacker's control over an HTTP request in plaintext format.

"The plugins also run a paid tier," the company said. "After a user pays a small fee through the donation wall built into the plugin, the server sends an API key back down to the client, and the plugin starts using that key for its model calls instead of your own, which is bizarre, since no legitimate operator would simply hand a user a working and unrestricted key to a paid AI provider."

This has raised the possibility that the operators behind the campaign are likely sharing the stolen AI provider API keys with other threat actors as part of an illicit monetization scheme, effectively turning it into a service that grants paying users access to the victim's AI provider.

"The operator collects money on one side and free credentials on the other, while the genuine key owners pay the bill," Makari added.

The campaign is further evidence of how threat actors are [increasingly targeting developer environments](https://www.stepsecurity.io/blog/miasma-and-hades-are-spreading-now-detect-them-on-developer-machines-with-suspicious-files) through the open-source ecosystem, which has become a lucrative target owing to the fact that they host source code, cloud credentials, signing keys, and API keys for paid AI services that can be resold for [LLMjacking](https://thehackernews.com/2025/02/microsoft-exposes-llmjacking.html) schemes.

"Treat a plugin the same way you would treat any dependency that runs with your privileges, and be cautious about pasting long-lived secrets into tools you have not vetted," Aikido Security said.

### Malicious Chrome Extensions Steal AI Conversations

The development coincides with the discovery of two Google Chrome ad blocker extensions that have been caught capturing users' conversations with AI chatbots like OpenAI ChatGPT, Anthropic Claude, Google Gemini, Microsoft Copilot, Perplexity, DeepSeek, xAI Grok, and Meta AI. The data collection operation has been codenamed [PromptSnatcher](https://malext.io/reports/PromptSnatcher/) by researcher Jean-Marie R.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

The names of the extensions, which are still available on the Chrome Web Store, are as follows -

* Smart Adblocker (ID: iojpcjjdfhlcbgjnpngcmaojmlokmeii) - 90,000 users (Published in October 2022)
* Adblock for Browser (ID: jcbjcocinigpbgfpnhlpagidbmlngnnn) - 10,000 users (Published in August 2023)

"While presented as ad blockers, the extensions ship a custom-built interception engine that records non-public conversations, model usage, and account-tier metadata from every major AI platform (ChatGPT, Claude, Gemini, and others)," the researcher said. "The operation uses legitimate public filter lists (EasyList, IDCAC) as functional cover, providing genuine ad-blocking utility while running an undisclosed telemetry channel."

The fact that the two extensions have been around for several years indicates that the AI-related data exfiltration features were introduced in the form of software updates.

These types of attacks fall under a category known as [Prompt Poaching](https://thehackernews.com/2026/01/two-chrome-extensions-caught-stealing.html). Over the past several months, browser extensions, both legitimate and ma...