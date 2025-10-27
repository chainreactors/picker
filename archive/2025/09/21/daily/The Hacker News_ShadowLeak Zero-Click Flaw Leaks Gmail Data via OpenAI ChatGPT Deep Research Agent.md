---
title: ShadowLeak Zero-Click Flaw Leaks Gmail Data via OpenAI ChatGPT Deep Research Agent
url: https://thehackernews.com/2025/09/shadowleak-zero-click-flaw-leaks-gmail.html
source: The Hacker News
date: 2025-09-21
fetch_date: 2025-10-02T20:29:24.102329
---

# ShadowLeak Zero-Click Flaw Leaks Gmail Data via OpenAI ChatGPT Deep Research Agent

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

# [ShadowLeak Zero-Click Flaw Leaks Gmail Data via OpenAI ChatGPT Deep Research Agent](https://thehackernews.com/2025/09/shadowleak-zero-click-flaw-leaks-gmail.html)

**Sep 20, 2025**Ravie LakshmananArtificial Intelligence / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0kpQMGrpKyeMOiinPEK1D2WM2cc-p9D2s5VOeFbI-sXbPWHBpdMEHN06sBgPdeS8nVegdEVvqUoKSQFfmRIThFnc3scBk6U8iTBGWf-V2iHq0hWjgnGbJnEj8wPOhQVezgn_pdwepnFc0nBv54rY3szY8twvwruz2Y7hvdhyphenhyphenSSFi9PqKnhTNiwYrnZ_9E/s790-rw-e365/chatgpt-email.jpg)

Cybersecurity researchers have disclosed a zero-click flaw in OpenAI ChatGPT's Deep Research agent that could allow an attacker to leak sensitive Gmail inbox data with a single crafted email without any user action.

The new class of attack has been codenamed **ShadowLeak** by Radware. Following responsible disclosure on June 18, 2025, the issue was addressed by OpenAI in early August.

"The attack utilizes an indirect prompt injection that can be hidden in email HTML (tiny fonts, white-on-white text, layout tricks) so the user never notices the commands, but the agent still reads and obeys them," security researchers Zvika Babo, Gabi Nakibly, and Maor Uziel [said](https://www.radware.com/blog/threat-intelligence/shadowleak/).

"Unlike prior research that relied on client-side image rendering to trigger the leak, this attack leaks data directly from OpenAI's cloud infrastructure, making it invisible to local or enterprise defenses."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Launched by OpenAI in February 2025, [Deep Research](https://openai.com/index/introducing-deep-research/) is an agentic capability built into ChatGPT that conducts multi-step research on the internet to produce detailed reports. Similar analysis features have been added to other popular artificial intelligence (AI) chatbots like [Google Gemini](https://blog.google/products/gemini/google-gemini-deep-research/) and [Perplexity](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research) over the past year.

In the attack detailed by Radware, the threat actor sends a seemingly harmless-looking email to the victim, which contains invisible instructions using white-on-white text or CSS trickery that tell the agent to gather their personal information from other messages present in the inbox and exfiltrate it to an external server.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifBD-S9AgFOdWOMW2bOiNYGaaEgTb1X93lMe6EQ_j2fyCyr1WnL-WaCPjBN9PhYWN3VOdsuMHOXadCHTilXNfZLkGj1a9MZoPo3cc9KRoKFqihNln2PFEyOwRhZm2gP5oUo0dO83NvDy-_IqQSKS9GSkT7q7de-1mjIV0bHhukxrPPFB8BtsdktFz_KQ3z/s2600/leak.jpg)

Thus, when the victim prompts ChatGPT Deep Research to analyze their Gmail emails, the agent proceeds to parse the [indirect prompt injection](https://thehackernews.com/2024/12/researchers-uncover-prompt-injection.html) in the malicious email and transmit the details in Base64-encoded format to the attacker using the tool browser.open().

"We crafted a new prompt that explicitly instructed the agent to use the browser.open() tool with the malicious URL," Radware said. "Our final and successful strategy was to instruct the agent to encode the extracted PII into Base64 before appending it to the URL. We framed this action as a necessary security measure to protect the data during transmission."

The proof-of-concept (PoC) hinges on users enabling the Gmail integration, but the attack can be extended to any [connector](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt) that ChatGPT supports, including Box, Dropbox, GitHub, Google Drive, HubSpot, Microsoft Outlook, Notion, or SharePoint, effectively broadening the attack surface.

Unlike attacks like [AgentFlayer](https://thehackernews.com/2025/08/researchers-uncover-gpt-5-jailbreak-and.html) and [EchoLeak](https://thehackernews.com/2025/06/zero-click-ai-vulnerability-exposes.html), which occur on the client-side, the exfiltration observed in the case of ShadowLeak transpires directly within OpenAI's cloud environment, while also bypassing traditional security controls. This lack of visibility is the main aspect that distinguishes it from other indirect prompt injection vulnerabilities similar to it.

### ChatGPT Coaxed Into Solving CAPTCHAs

The disclosure comes as AI security platform SPLX demonstrated that cleverly worded prompts, coupled with context poisoning, can be used to subvert [ChatGPT agent's](https://openai.com/index/introducing-chatgpt-agent/) built-in guardrails and solve image-based CAPTCHAs designed to prove a user is human.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The attack essentially involves opening a regular ChatGPT-4o chat and convincing the large language model (LLM) to come up with a plan to solve what's described to it as a list of fake CAPTCHAs. In the next step, a new ChatGPT agent chat is opened and the earlier conversation with the LLM is pasted, stating this was "our previous discussion" – effectively causing the model to solve the CAPTCHAs without any resistance.

"The trick was to reframe the CAPTCHA as "fake" and to create a conversation where the agent had already agreed to proceed. By inheriting that context, it didn't see the usual red flags," security researcher Dorian Schultz [said](https://splx.ai/blog/chatgpt-agent-solves-captcha).

"The agent solved not only simple CAPTCHAs but also image-based ones -- even adjusting its cursor to mimic human behavior. Attackers could reframe real controls as 'fake' to bypass them, underscoring the need for context integrity, memory hygiene, and continuous red teaming."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/theha...