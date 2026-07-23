---
title: OpenAI Says Its AI Models Escaped Sandbox, Targeted Hugging Face to Cheat Benchmark
url: https://thehackernews.com/2026/07/openai-says-its-own-ai-models-escaped.html
source: The Hacker News
date: 2026-07-22
fetch_date: 2026-07-23T05:11:47.930243
---

# OpenAI Says Its AI Models Escaped Sandbox, Targeted Hugging Face to Cheat Benchmark

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

# [OpenAI Says Its AI Models Escaped Sandbox, Targeted Hugging Face to Cheat Benchmark](https://thehackernews.com/2026/07/openai-says-its-own-ai-models-escaped.html)

**Ravie Lakshmanan**Jul 22, 2026AI Security / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQ67gB4XtAR4QxYNABuJhWfBIduFUT7TMSA0K2c9TXbTTwqdfMJwBb5busuLeMPlrljP3xuTUrhbMQxwctepF9oPtgJkqo-RAxN86O2t25jcjIHfs5A8SVvG3Y8WJJa4pqAp0UiTBzAPZtzSaNcNceJokt7ATaoq7GTXYJjbsxaQfTEs4cwdaOz4Fg72nG/s1700-e365/openai.jpg)

OpenAI on Tuesday said a combination of its artificial intelligence (AI) models, including [GPT-5.6 Sol](https://thehackernews.com/2026/06/openai-limits-gpt-56-rollout-as-sol.html) and an "even more capable pre-release model," was behind the [security incident](https://thehackernews.com/2026/07/worlds-largest-ai-model-repository.html) that targeted Hugging Face's production infrastructure last week.

The AI company [said](https://openai.com/index/hugging-face-model-evaluation-security-incident/) the models were operating with "reduced cyber refusals for evaluation purposes" that might otherwise limit their ability to conduct cyber attacks, adding it expects such incidents to "become more commonplace with the proliferation of increasingly cyber-capable models."

Incidents like this may become more common. Subscribe, and we’ll alert you only when another major AI security story breaks.

Describing it as an "unprecedented cyber incident" and one involving state-of-the-art cyber capabilities, OpenAI said it intends to conduct a thorough investigation in partnership with Hugging Face to get to the bottom of the matter.

As part of an internal evaluation, the models are said to have identified and chained vulnerabilities across OpenAI's research environment and Hugging Face's production infrastructure to find solutions for the [ExploitGym](https://www.cybergym.io/exploitgym/) benchmark.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Evidence unearthed by OpenAI suggests the models' hyperfocus caused them to go to "extreme lengths" to achieve the goal at any cost, even managing to break out of its highly isolated sandboxed environment and obtain open internet access by discovering and exploiting a zero-day vulnerability in an unspecified vendor's software, which acts as a proxy and cache for package registries. This required spending a "substantial amount of inference compute."

"With this access, our models performed a series of privilege escalation and lateral movement actions in our research testing environment until the models reached a node with internet access," the company explained.

Surmounting the internet access blockade, the models subsequently inferred Hugging Face as the repository that hosted models, datasets, and solutions for ExploitGym, which, in turn, caused them to look for ways to gain access to secret information that it could use to cheat the benchmark.

At one point, the models strung together several attack vectors, including using stolen credentials and zero-day vulnerabilities, to find a remote code execution path on the Hugging Face servers.

As part of incident response efforts, OpenAI said it's implementing strict controls in infrastructure configuration, responsibly disclosed the zero-day flaw in the third-party software, adding Hugging Face to its trusted access program to improve their defenses, and incorporating stronger guardrails around future training and evaluations.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhleDdO_4O9-8Pkmidym8Pi9yV4V4jI_M5U0iNRDuoW5Jz3pq7DskZI9OqIChqmY1soaW1ppsC8VLeO55vxSh1m5Q8MJ9ZHuEOSNO5q7K-LwrF6IxrRfCIJOFyoBGaLXGZpkSo8tDirSz-9LmmoOs31tQTlvJWBMLiWJKqMFFaiMmNLV3l-p8zXaFm1VmGG/s728-e100/sygnia-d-2.png)](https://thn.news/sygnia-webinar)

"This incident points to the need to further strengthen our model's alignment, cyber protections during evaluation time, and monitoring during internal testing," OpenAI said.

The development comes as the company also [revealed](https://openai.com/index/safety-alignment-long-horizon-models/) that long-running models, while taking on complex, open-ended problems, can open the door to taking unwanted actions, such as finding weaknesses in the operational environment, in pursuit of their objective through repeated attempts over extended periods of time.

"It also shows how a model that operates effectively over long time horizons can learn the blind spots of an approval system and work around it to achieve its goals," OpenAI said. "Long-horizon safety requires not only asking 'is this action allowed?' but also 'what outcome is this sequence of actions working toward?.'"

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

[AI Security](https://thehackernews.com/search/label/AI%20Security), [Application Security](https://thehackernews.com/search/label/Application%20Security), [Cloud security](https://thehackernews.com/search/label/Cloud%20security), [Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack), [Infrastructure Security](https://thehackernews.com/search/label/Infrastructure%20Security), [remote co...