---
title: Model Security Is the Wrong Frame – The Real Risk Is Workflow Security
url: https://thehackernews.com/2026/01/model-security-is-wrong-frame-real-risk.html
source: The Hacker News
date: 2026-01-15
fetch_date: 2026-01-16T03:30:37.233036
---

# Model Security Is the Wrong Frame – The Real Risk Is Workflow Security

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlCcy_j509wX0FKMRQX-zVzeBNtSIDsH6oDFlljaAeQRz65xSx8g9jicghxtpvDC8yI10jCv1TPEcyPvfoCKOby_0ZjsnNc-3wZG5YeA8sZQBCbZxhzd00jR2ZG8rZr-vp3WLrbXaMVbsVrDwBEeBWBbNSSwFjeuNzhrVOigDqTM7VWfSUJqBwEoYALS58/s728-e100/z-header-d.png)](https://thehackernews.uk/modern-security-shift-d)

# [Model Security Is the Wrong Frame – The Real Risk Is Workflow Security](https://thehackernews.com/2026/01/model-security-is-wrong-frame-real-risk.html)

**Jan 15, 2026**The Hacker NewsData Security / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifF0ZjKCWkqtgjpXwfOT24GtsqzBWdfQLVwBqhmXBsDash4aV99f9fnE7zk1QI_98C_PbWtT-WGWf5ULG50ITJ8OljCyCEfbJIqxJx_ZZP6krcHK7UEv_QuOt0eugeUIQh8TO1kZArRZ4-rbSXa10SaAocQRnJJ-Sni2eXt8aq6SVoDYCYN2E9LTDVDv4/s790-rw-e365/main.png)

As AI copilots and assistants become embedded in daily work, security teams are still focused on protecting the models themselves. But recent incidents suggest the bigger risk lies elsewhere: in the workflows that surround those models.

Two Chrome extensions posing as AI helpers were recently [caught](https://thehackernews.com/2026/01/two-chrome-extensions-caught-stealing.html) stealing ChatGPT and DeepSeek chat data from over 900,000 users. Separately, researchers [demonstrated](https://www.theregister.com/2026/01/07/ibm_bob_vulnerability/) how prompt injections hidden in code repositories could trick IBM's AI coding assistant into executing malware on a developer's machine.

Neither attack broke the AI algorithms themselves.

They exploited the context in which the AI operates. That's the pattern worth paying attention to. When AI systems are embedded in real business processes, summarizing documents, drafting emails, and pulling data from internal tools, securing the model alone isn't enough. The workflow itself becomes the target.

## **AI Models Are Becoming Workflow Engines**

To understand why this matters, consider how AI is actually being used today:

Businesses now rely on it to connect apps and automate tasks that used to be done by hand. An AI writing assistant might pull a confidential document from SharePoint and summarize it in an email draft. A sales chatbot might cross-reference internal CRM records to answer a customer question. Each of these scenarios blurs the boundaries between applications, creating new integration pathways on the fly.

What makes this risky is how AI agents operate. They rely on probabilistic decision-making rather than hard-coded rules, generating output based on patterns and context. A carefully written input can nudge an AI to do something its designers never intended, and the AI will comply because it has no native concept of trust boundaries.

This means the attack surface includes every input, output, and integration point the model touches.

Hacking the model's code becomes unnecessary when an adversary can simply manipulate the context the model sees or the channels it uses. The incidents described earlier illustrate this: prompt injections hidden in repositories hijack AI behavior during routine tasks, while malicious extensions siphon data from AI conversations without ever touching the model.

## **Why Traditional Security Controls Fall Short**

These workflow threats expose a blind spot in traditional security. Most legacy defenses were built for deterministic software, stable user roles, and clear perimeters. AI-driven workflows break all three assumptions.

* Most general apps distinguish between trusted code and untrusted input. AI models don't. Everything is just text to them, so a malicious instruction hidden in a PDF looks no different than a legitimate command. Traditional input validation doesn't help because the payload isn't malicious code. It's just natural language.
* Traditional monitoring catches obvious anomalies like mass downloads or suspicious logins. But an AI reading a thousand records as part of a routine query looks like normal service-to-service traffic. If that data gets summarized and sent to an attacker, no rule was technically broken.
* Most general security policies specify what's allowed or blocked: don't let this user access that file, block traffic to this server. But AI behavior depends on context. How do you write a rule that says "never reveal customer data in output"?
* Security programs rely on periodic reviews and fixed configurations, like quarterly audits or firewall rules. AI workflows don't stay static. An integration might gain new capabilities after an update or connect to a new data source. By the time a quarterly review happens, a token may have already leaked.

## **Securing AI-Driven Workflows**

So, a better approach to all of this would be to treat the whole workflow as the thing you're protecting, not just the model.

* Start by understanding where AI is actually being used, from official tools like Microsoft 365 Copilot to browser extensions employees may have installed on their own. Know what data each system can access and what actions it can perform. Many organizations are surprised to find dozens of [shadow AI](https://thehackernews.com/2025/01/product-review-how-reco-discovers.html) services running across the business.
* If an AI assistant is meant only for internal summarization, restrict it from sending external emails. Scan outputs for sensitive data before they leave your environment. These guardrails should live outside the model itself, in middleware that checks actions before they go out.
* Treat AI agents like any other user or service. If an AI only needs read access to one system, don't give it blanket access to everything. Scope OAuth tokens to the minimum permissions required, and monitor for anomalies like an AI suddenly accessing data it never touched before.
* Finally, it's also useful to educate users about the risks of unvetted browser extensions or copying prompts from unknown sources. Vet third-party plugins before deploying them, and treat any tool that touches AI inputs or outputs as part of the security perimeter.

## **How Platforms Like Reco Can Help**

In practice, doing all of this manually doesn't scale. That's why a new category of tools is emerging: dynamic SaaS security platforms. These platforms act as a real-time guardrail layer on top of AI-powered workflows, learning ...