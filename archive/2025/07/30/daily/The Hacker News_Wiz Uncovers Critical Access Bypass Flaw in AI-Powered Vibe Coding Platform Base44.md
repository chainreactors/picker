---
title: Wiz Uncovers Critical Access Bypass Flaw in AI-Powered Vibe Coding Platform Base44
url: https://thehackernews.com/2025/07/wiz-uncovers-critical-access-bypass.html
source: The Hacker News
date: 2025-07-30
fetch_date: 2025-10-06T23:57:09.193519
---

# Wiz Uncovers Critical Access Bypass Flaw in AI-Powered Vibe Coding Platform Base44

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

# [Wiz Uncovers Critical Access Bypass Flaw in AI-Powered Vibe Coding Platform Base44](https://thehackernews.com/2025/07/wiz-uncovers-critical-access-bypass.html)

**Jul 29, 2025**Ravie LakshmananLLM Security / Vulnerability

[![AI-Powered Vibe Coding Platform Base44](data:image/png;base64... "AI-Powered Vibe Coding Platform Base44")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjeZrcBOQhbS9YVJR_Cvi4P3Mx4x2g228c8m4JNJwsCEQMq8lLszB1AtcyLIzT_tibWs9glwIFXAx-0Gb4XJywbKQCJW33ilf01r_Bo8soG6Z0jLa7mYrJoBchDnnrUMJinzRTge6DN4m0fMAqDqELO3YU-14uE5IheUFIklhuDVz1UiKTV_D_pEG_2WRu9/s790-rw-e365/base44.jpg)

Cybersecurity researchers have disclosed a now-patched critical security flaw in a popular vibe coding platform called Base44 that could allow unauthorized access to private applications built by its users.

"The vulnerability we discovered was remarkably simple to exploit -- by providing only a non-secret 'app\_id' value to undocumented registration and email verification endpoints, an attacker could have created a verified account for private applications on their platform," cloud security firm Wiz [said](https://www.wiz.io/blog/critical-vulnerability-base44) in a report shared with The Hacker News.

A net result of this issue is that it bypasses all authentication controls, including Single Sign-On (SSO) protections, granting full access to all the private applications and data contained within them.

Following responsible disclosure on July 9, 2025, an official fix was rolled out by Wix, which owns Base44, within 24 hours. There is no evidence that the issue was ever maliciously exploited in the wild.

While [vibe coding](https://thehackernews.com/2025/04/lovable-ai-found-most-vulnerable-to.html) is an artificial intelligence (AI)-powered approach designed to generate code for applications by simply providing as input a text prompt, the latest findings highlight an emerging attack surface, thanks to the popularity of AI tools in enterprise environments, that may not be adequately addressed by traditional security paradigms.

The shortcoming unearthed by Wiz in Base44 concerns a misconfiguration that left two authentication-related endpoints exposed without any restrictions, thereby permitting anyone to register for private applications using only an "app\_id" value as input -

* api/apps/{app\_id}/auth/register, which is used to register a new user by providing an email address and password
* api/apps/{app\_id}/auth/verify-otp, which is used to verify the user by providing a one-time password (OTP)

As it turns out, the "app\_id" value is not a secret and is visible in the app's URL and in its manifest.json file path. This also meant that it's possible to use a target application's "app\_id" to not only register a new account but also verify the email address using OTP, thereby gaining access to an application that they didn't own in the first place.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"After confirming our email address, we could just login via the SSO within the application page, and successfully bypass the authentication," security researcher Gal Nagli said. "This vulnerability meant that private applications hosted on Base44 could be accessed without authorization."

The development comes as security researchers have shown that state-of-the-art large language models (LLMs) and generative AI (GenAI) tools can be jailbroken or subjected to prompt injection attacks and make them behave in unintended ways, breaking free of their ethical or safety guardrails to produce malicious responses, synthetic content, or hallucinations, and, in some cases, even [abandon correct answers](https://www.arxiv.org/abs/2507.03120) when presented with false counterarguments, posing risks to multi-turn AI systems.

Some of the attacks that have been documented in recent weeks include -

* A "toxic" combination of improper validation of context files, prompt injection, and misleading user experience (UX) in [Gemini CLI](https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.14) that could [lead](https://tracebit.com/blog/code-exec-deception-gemini-ai-cli-hijack) to silent execution of malicious commands when inspecting untrusted code.
* Using a special crafted email hosted in Gmail to [trigger](https://www.pynt.io/blog/llm-security-blogs/code-execution-through-email-how-i-used-claude-mcp-to-hack-itself) code execution through Claude Desktop by tricking Claude to rewrite the message such that it can bypass restrictions imposed on it.
* Jailbreaking xAI's Grok 4 model using [Echo Chamber and Crescendo](https://thehackernews.com/2025/06/echo-chamber-jailbreak-tricks-llms-like.html) to [circumvent](https://neuraltrust.ai/blog/grok-4-jailbreak-echo-chamber-and-crescendo) the model's safety systems and elicit harmful responses without providing any explicit malicious input. The LLM has also been [found](https://splx.ai/blog/grok-4-security-testing) leaking restricted data and abiding hostile instructions in over 99% of prompt injection attempts absent any hardened system prompt.
* Coercing OpenAI ChatGPT into [disclosing](https://0din.ai/blog/chatgpt-guessing-game-leads-to-users-extracting-free-windows-os-keys-more) valid Windows product keys via a guessing game
* Exploiting Google Gemini for Workspace to [generate](https://0din.ai/blog/phishing-for-gemini) an email summary that looks legitimate but includes malicious instructions or warnings that direct users to phishing sites by embedding a hidden directive in the message body using HTML and CSS trickery.
* Bypassing Meta's Llama Firewall to [defeat](https://medium.com/trendyol-tech/bypassing-metas-llama-firewall-a-case-study-in-prompt-injection-vulnerabilities-fb552b93412b) prompt injection safeguards using prompts that used languages other than English or simple obfuscation techniques like leetspeak and invisible Unicode characters.
* Deceiving browser agents into [revealing](https://arimlabs.ai/news/the-hidden-dangers-of-brow...