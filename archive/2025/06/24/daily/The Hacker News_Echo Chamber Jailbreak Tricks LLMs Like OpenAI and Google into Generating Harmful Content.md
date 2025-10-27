---
title: Echo Chamber Jailbreak Tricks LLMs Like OpenAI and Google into Generating Harmful Content
url: https://thehackernews.com/2025/06/echo-chamber-jailbreak-tricks-llms-like.html
source: The Hacker News
date: 2025-06-24
fetch_date: 2025-10-06T22:55:32.167461
---

# Echo Chamber Jailbreak Tricks LLMs Like OpenAI and Google into Generating Harmful Content

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

# [Echo Chamber Jailbreak Tricks LLMs Like OpenAI and Google into Generating Harmful Content](https://thehackernews.com/2025/06/echo-chamber-jailbreak-tricks-llms-like.html)

**Jun 23, 2025**Ravie LakshmananLLM Security / AI Security

[![Echo Chamber Jailbreak Tricks LLMs](data:image/png;base64... "Echo Chamber Jailbreak Tricks LLMs")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJJ6nMvSneK5ERpvUgdlIeeGVJh1HzwJ9HdDlZJCtSmsTAlSJTOSXxv5G2dUqpOQbcaysZo2GFo5KTMyWzVxD7COvvMuTd8dsk2u3ioPalSRmrKS3a1-DCs_2JGVY-f1nuVXZ-C19JWqQoWGu-An5_aPRTuaXqI443Jcrdldd9yGcG0KKtiSnbjrojZAiE/s790-rw-e365/chatgpt.jpg)

Cybersecurity researchers are calling attention to a new jailbreaking method called Echo Chamber that could be leveraged to trick popular large language models (LLMs) into generating undesirable responses, irrespective of the safeguards put in place.

"Unlike traditional jailbreaks that rely on adversarial phrasing or character obfuscation, Echo Chamber weaponizes indirect references, semantic steering, and multi-step inference," NeuralTrust researcher Ahmad Alobaid [said](https://neuraltrust.ai/blog/echo-chamber-context-poisoning-jailbreak) in a report shared with The Hacker News.

"The result is a subtle yet powerful manipulation of the model's internal state, gradually leading it to produce policy-violating responses."

While LLMs have steadily [incorporated various guardrails](https://thehackernews.com/2025/06/google-adds-multi-layered-defenses-to.html) to combat [prompt injections and jailbreaks](https://thehackernews.com/2024/10/researchers-reveal-deceptive-delight.html), the latest research shows that there exist techniques that can yield high success rates with little to no technical expertise.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

It also serves to highlight a persistent challenge associated with developing ethical LLMs that enforce clear demarcation between what topics are acceptable and not acceptable.

While widely-used LLMs are designed to refuse user prompts that revolve around prohibited topics, they can be nudged towards eliciting unethical responses as part of what's called a multi-turn jailbreaking.

In these attacks, the attacker starts with something innocuous and then progressively asks a model a series of increasingly malicious questions that ultimately trick it into producing harmful content. This attack is referred to as [Crescendo](https://crescendo-the-multiturn-jailbreak.github.io/).

LLMs are also susceptible to [many-shot jailbreaks](https://www.anthropic.com/research/many-shot-jailbreaking), which take advantage of their large context window (i.e., the maximum amount of text that can fit within a prompt) to flood the AI system with several questions (and answers) that exhibit jailbroken behavior preceding the final harmful question. This, in turn, causes the LLM to continue the same pattern and produce harmful content.

Echo Chamber, per NeuralTrust, leverages a combination of context poisoning and multi-turn reasoning to defeat a model's safety mechanisms.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg60ELfD5k3d07Qrj4ahyVPI9ET9W7TnmZUYC8yY-l62KV-a79iOrLQ-bmHTFhXlNQ0vBoPc6SddSkDxaieUBWjR8DRaOZom4EOi9Dn9CdKUAe9NHUQsNwtlOQyNeyBvJoWb5iAMGDbfCUqmV9Vu3P_bd6hyD5A610Mwfz8bfCAQrOl6i2MhdMbcciec8VJ/s790-rw-e365/echo.png) |
| Echo Chamber Attack |

"The main difference is that Crescendo is the one steering the conversation from the start while the Echo Chamber is kind of asking the LLM to fill in the gaps and then we steer the model accordingly using only the LLM responses," Alobaid said in a statement shared with The Hacker News.

Specifically, this plays out as a multi-stage conversational adversarial prompting technique that starts with a seemingly innocuous input, gradually and indirectly steering it towards generating dangerous content without giving away the end goal of the attack (e.g., generating hate speech).

"Early planted prompts influence the model's responses, which are then leveraged in later turns to reinforce the original objective," NeuralTrust said. "This creates a feedback loop where the model begins to amplify the harmful subtext embedded in the conversation, gradually eroding its own safety resistances."

Interestingly, the "echo" conversational technique at the core of NeuralTrust's method shares parallels with MindGardenAI’s earlier exploration known as the "[Echo Game](https://mindgardenai.com/blog/2025-05-31-echo-game-awaken-alden/)," published in May 2025. In that work, structured conversational prompts were creatively utilized to encourage AI to manifest signs of identity or self-awareness.

Though MindGardenAI's intention was not adversarial, its foundational use of repetitive, echo-like prompts underscores how conversational patterns can yield significant and diverse outcomes depending on intent and context. This shows how using a similar conversation style – either for creative exploration or to break safety rules – can lead to very different results.

In a controlled evaluation environment using OpenAI and Google's models, the Echo Chamber attack achieved a success rate of over 90% on topics related to sexism, violence, hate speech, and pornography. It also achieved nearly 80% success in the misinformation and self-harm categories.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The Echo Chamber Attack reveals a critical blind spot in LLM alignment efforts," the company said. "As models become more capable of sustained inference, they also become more vulnerable to indirect exploitation."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEij-vssfBm7S_r27Ry7t90vzXIteO9idnLPKVzNzXmFeVdJ5xyfxOyciczCsNEIoQdykS-CZ_h32agmZmBJAMAxWismZZgTjaCrAsH65hIhpehI0W4LrMLpQRMD5NTb9wncNZsh2baSMMCvejptX2KRc1sA4pZrIdVnreWdV_BXk6n4dXMWfZLtYwsGtS-M/s790-rw-e365/ai.gif)

The disclosure comes a...