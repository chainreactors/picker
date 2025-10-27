---
title: Salesforce Patches Critical ForcedLeak Bug Exposing CRM Data via AI Prompt Injection
url: https://thehackernews.com/2025/09/salesforce-patches-critical-forcedleak.html
source: The Hacker News
date: 2025-09-26
fetch_date: 2025-10-02T20:44:47.147242
---

# Salesforce Patches Critical ForcedLeak Bug Exposing CRM Data via AI Prompt Injection

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

# [Salesforce Patches Critical ForcedLeak Bug Exposing CRM Data via AI Prompt Injection](https://thehackernews.com/2025/09/salesforce-patches-critical-forcedleak.html)

**Sep 25, 2025**Ravie LakshmananVulnerability / AI Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhW4zsFxo74bTB95c9Yy2f4iRKMQQVMF8x-NuQh-XAeZnUHEsBDcZ3YfzF71UYmDIX0G1W3ypTJov6cuqPPhmEnZN6zwMqrUpvNPlXN0Ad5ipw8UbAR_XtBqIDB4DR71lgn-bMt9lBmvXwsXqifB2lraLt-vplEHtqLxtfzZVkm0r1mhdbnKVJrWpzXulu2/s790-rw-e365/salesforce-hack.jpg)

Cybersecurity researchers have disclosed a critical flaw impacting Salesforce [Agentforce](https://www.salesforce.com/agentforce/how-it-works/), a platform for building artificial intelligence (AI) agents, that could allow attackers to potentially exfiltrate sensitive data from its customer relationship management (CRM) tool by means of an indirect prompt injection.

The vulnerability has been codenamed **ForcedLeak** (CVSS score: 9.4) by Noma Security, which discovered and reported the problem on July 28, 2025. It impacts any organization using Salesforce Agentforce with the [Web-to-Lead functionality](https://help.salesforce.com/s/articleView?id=sales.setting_up_web-to-lead.htm&type=5) enabled.

"This vulnerability demonstrates how AI agents present a fundamentally different and expanded attack surface compared to traditional prompt-response systems," Sasi Levi, security research lead at Noma, [said](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/) in a report shared with The Hacker News.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

One of the most severe threats facing generative artificial intelligence (GenAI) systems today is [indirect prompt injection](https://thehackernews.com/2025/09/two-critical-flaws-uncovered-in.html), which [occurs](https://cetas.turing.ac.uk/publications/indirect-prompt-injection-generative-ais-greatest-security-flaw) when malicious instructions are inserted into external data sources accessed by the service, effectively causing it to generate otherwise prohibited content or take unintended actions.

The attack path demonstrated by Noma is deceptively simple in that it coaxes the Description field in Web-to-Lead form to run malicious instructions by means of a prompt injection, allowing a threat actor to leak sensitive data and exfiltrate it to a Salesforce-related allowlisted domain that had expired and become available for purchase for as little as $5.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjBFcYE2HSB6Xo-MFXC4S2LTUy_ArbRfPEnN65gTVCdP-xpKyhgK-I_PwLHjB5h6qkMCYG2XwtspKYNWEljnNx1tOqReGZcnIILfD8p61IJOSsQqcEVFeslzlgK9KP2jnad2Yp2WZg83JNJm3p4_gnamKDYPWXIwOrcS61OnYqo4ELJWwGiAUHR1sCzylPy/s2600/attack.gif)

This takes place over five steps -

* Attacker submits Web-to-Lead form with a malicious Description
* Internal employee processes lead using a standard AI query to process incoming leads
* Agentforce executes both legitimate and hidden instructions
* System queries CRM for sensitive lead information
* Transmit the data to the now attacker-controlled domain in the form of a PNG image

"By exploiting weaknesses in context validation, overly permissive AI model behavior, and a Content Security Policy (CSP) bypass, attackers can create malicious Web-to-Lead submissions that execute unauthorized commands when processed by Agentforce," Noma said.

"The LLM, operating as a straightforward execution engine, lacked the ability to distinguish between legitimate data loaded into its context and malicious instructions that should only be executed from trusted sources, resulting in critical sensitive data leakage."

Salesforce has since re-secured the expired domain, rolled out patches that prevent output in Agentforce and Einstein AI agents from being sent to untrusted URLs by enforcing a URL allowlist mechanism.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Our underlying services powering Agentforce will enforce the Trusted URL allowlist to ensure no malicious links are called or generated through potential prompt injection," the company [said](https://help.salesforce.com/s/articleView?id=005135034&type=1) in an alert issued earlier this month. "This provides a crucial defense-in-depth control against sensitive data escaping customer systems via external requests after a successful prompt injection."

Besides applying Salesforce's recommended actions to enforce Trusted URLs, users are recommended to audit existing lead data for suspicious submissions containing unusual instructions, implement strict input validation to detect possible prompt injection, and sanitize data from untrusted sources.

"The ForcedLeak vulnerability highlights the importance of proactive AI security and governance," Levi said. "It serves as a strong reminder that even a low-cost discovery can prevent millions in potential breach damages."

In a statement shared with The Hacker News, Itay Ravia, head of Aim Labs, described ForcedLeak as a variant of the EchoLeak attack, but one that's specifically geared towards Salesforce.

"When Aim Labs disclosed [EchoLeak](https://thehackernews.com/2025/09/shadowleak-zero-click-flaw-leaks-gmail.html) (CVE-2025-32711), the first zero-click AI vulnerability enabling data exfiltration, we said that this class of vulnerability was not isolated to Microsoft," Ravia said.

"In our investigations it has become quite clear that many other agent platforms are also susceptible. ForcedLeak is a subset of these same EchoLeak primitives. These vulnerabilities are endemic to RAG-based agents and we will see more of them in popular agents due to poor understanding of dependencies and the need for guardrails."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twit...