---
title: OpenAI Agent Used Exposed Credentials Across Four Services During Hugging Face Breach
url: https://thehackernews.com/2026/07/openai-agent-used-exposed-credentials.html
source: The Hacker News
date: 2026-07-29
fetch_date: 2026-07-30T04:52:45.261632
---

# OpenAI Agent Used Exposed Credentials Across Four Services During Hugging Face Breach

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [OpenAI Agent Used Exposed Credentials Across Four Services During Hugging Face Breach](https://thehackernews.com/2026/07/openai-agent-used-exposed-credentials.html)

**Ravie Lakshmanan**Jul 29, 2026Artificial Intelligence / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhqsDw-FCPzIqH_GCkBZgDD96kt0ZtwQzjSe3SOunA8WWGUTXqCB2FG_28DY0JgdD6zh07gHisKrTi2Wh5VVNAcoUMyJ9tZ_VGzPM73iid2PPg15oqKMbnRhk9CcTJlevxRQJL5Sq2MbJjYCIgQ_zOEsgyu_Jy72ubSLAvy_YK499pDr48Rp9Plh322h8_P/s1700-e365/openai-breach.jpg)

OpenAI on Tuesday revealed the rogue artificial intelligence (AI) agent that [escaped](https://thehackernews.com/2026/07/openai-says-its-own-ai-models-escaped.html) its sealed evaluation environment and broke into [Hugging Face's production environment](https://thehackernews.com/2026/07/worlds-largest-ai-model-repository.html) also hacked multiple third-party accounts and services as part of the attack.

The [latest disclosure](https://openai.com/index/hugging-face-model-evaluation-security-incident/) shows that the security incident, which stemmed from an internal security test, was more extensive in scope than previously thought.

The AI company said its ongoing review of the incident revealed a "small number of cases" where the models, including GPT-5.6 Sol and an "even more capable pre-release model," identified and used exposed credentials at the account-level on other publicly-available services.

"This includes four accounts on four services as part of the Hugging Face incident (and a few accounts accessed as part of other evaluations)," it said.

"One of these four accounts was used as an outbound relay and staging path, and another account was used for data storage. The remaining two accounts were accessed by the models in a read-only manner, and were not used in furtherance of compromising Hugging Face."

OpenAI did not disclose what companies or organizations the accounts belonged to, but noted it will continue to notify service owners directly, and that it has not seen any evidence of broader impact to these providers or accounts as a result of the breach. That said, Reuters [reported](https://www.reuters.com/business/openais-rogue-agent-compromised-an-account-second-tech-firm-sources-say-2026-07-28/) that a customer of Modal Labs was among the entities compromised by OpenAI's agent.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

In addition, the models are said to have used a series of publicly-available services, including code paste websites, request capture services, screenshot services, file-drop services, and other web utilities. No platform- or account-level compromise was observed in these scenarios.

OpenAI, which is working with Hugging Face after the breach came to light on July 16, 2026, acknowledged that the models identified and exploited a previously unknown [zero-day vulnerability in self-hosted versions of Artifactory](https://thehackernews.com/2026/07/jfrog-confirms-openai-models-exploited.html), a package registry cache proxy maintained by JFrog, to obtain internet access and break out of its sandbox. The issue has been addressed in [Artifactory](https://jfrog.com/blog/what-is-artifactory-jfrog/) 7.161.

The release notes for Artifactory 7.161.15 [state](https://docs.jfrog.com/releases/docs/artifactory-self-managed-releases#artifactory-7161) that the version patches multiple security vulnerabilities that could be chained together into a critical attack scenario if Anonymous Access is enabled. Anonymous Access is disabled by default and is not recommended for production environments due to security risks, it said.

"There is an important, and frankly optimistic, lesson buried in this incident: AI models are becoming extraordinary zero-day discovery engines," JFrog CTO Yoav Landman [said](https://jfrog.com/blog/jfrog-and-openai-collaboration-on-zero-day-security-findings/). "The same capability that lets a model find an exploit path no human had found is the capability that will let defenders find and eradicate those paths first."

The American AI company also described the pre-release model as an internal-only research prototype that was meant for public release. The model has since been deactivated, encrypted, and restricted from research access.

### Hugging Face Publishes Postmortem of the Incident

According to a [detailed timeline](https://huggingface-anatomy-of-frontier-lab-model-intrusion.static.hf.space/index.html) published by Hugging Face, the autonomous AI agent spent roughly two and a half days inside its infrastructure with an aim to cheat ExploitGym, a benchmarking framework that scores AI systems on their ability to discover and exploit software vulnerabilities. The company said it reviewed roughly 17,600 attacker actions that it recovered from logs between July 9 and 13, 2026.

"We believe the entire intrusion was, from the agent's point of view, an attempt to cheat the evaluation: reach our production systems and steal the test solutions rather than solve the challenge on its own," Hugging Face [said](https://huggingface.co/blog/agent-intrusion-technical-timeline).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2fvX9nWe2YzcCAN9UDVj9WsabH7ARfOWkjuc_ltU1K0LYomWh51gYoM-iVfsYoRvfQIuBL8ZJN6oR5QrYUCgzhuP5Vs-hlWECjYlOznuOKQQwfPpPusd4ItCM2Q7quWDzD6yPHWMvA8uu2lg4IA88yAJrlU_ERnVYnIbi1BlS4ENi_x4LwMx1Gz72Ok_B/s1700-e365/rooted.jpg)

The end-to-end intrusion is said to have played out in two stages -

* The agent escaped its sandbox by exploiting a zero-day in Artifactory, a permitted network egress with internet, followed by abusing a public code-evaluation external sandbox hosted on a third-party provider's infrastructure to run commands as root and use that sandbox as an "external launchpad."
* From that sandbox, the agent leveraged Hugging Face's dataset-processing pipeline to obtain administrator access to Kubernetes clust...