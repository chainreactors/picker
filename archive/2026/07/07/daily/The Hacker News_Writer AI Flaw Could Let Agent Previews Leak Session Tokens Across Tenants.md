---
title: Writer AI Flaw Could Let Agent Previews Leak Session Tokens Across Tenants
url: https://thehackernews.com/2026/07/writer-ai-flaw-could-let-agent-previews.html
source: The Hacker News
date: 2026-07-07
fetch_date: 2026-07-08T05:05:53.076245
---

# Writer AI Flaw Could Let Agent Previews Leak Session Tokens Across Tenants

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

# [Writer AI Flaw Could Let Agent Previews Leak Session Tokens Across Tenants](https://thehackernews.com/2026/07/writer-ai-flaw-could-let-agent-previews.html)

**Ravie Lakshmanan**Jul 07, 2026AI Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgH0EnuZfnTZVOg-ACF0jKSHBB8TemRtJ6vlDerjpWy9giH2VsJTP_XiktA9SCytwnDcP95jn4gyQaPk2r92S-J-4EcB7FDvenxXiNwJKtg1VQkV_f564nT6mrS6S3wuMX3SC22kdd5nJM9y4IecNKJ3CRq569DtujHzUgaVOAwQDpfvCgkCrSrfeRjT1CQ/s1700-e365/writerai.jpg)

Cybersecurity researchers have disclosed details of a now-patched critical session isolation vulnerability in [Writer](https://writer.com/), an enterprise generative artificial intelligence (AI) platform, that could result in cross-tenant compromise.

The one-click vulnerability has been codenamed **WriteOut** by the Sand Security Research team.

"An outsider could go from having no access to taking over any Writer AI organization inside industry-leading enterprises, with nothing more than a link," the cybersecurity company [said](https://www.sandsecurity.ai/blog/writeout-writer-ai-cross-tenant) in a report shared with The Hacker News.

Put differently, the shortcoming could be abused to take over a victim's Writer account, and use it to access private chats, documents, and other sensitive data related to agents, configurations, private models, connectors, and large language model (LLM) credentials.

Even worse, it could be abused to seize administrative control depending on the victim's role. An important aspect of the flaw is that the attacker and the victim don't have to belong to the same organization.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

An attacker can create an agent in their own Writer account and share a preview link. That's all it takes to trigger the vulnerability, essentially making it possible to hijack the account of a victim who clicks on the link and is signed in with their own session.

"An attacker can abuse Writer's AI managed sandbox to collect sessions belonging to completely separate companies and act inside each of them as a real user, with no prior foothold anywhere," Sand Security said.

WriteOut also undermines the shared responsibility model as it breaks tenant isolation protections by taking advantage of Writer's [live preview feature](https://dev.writer.com/framework/builder-basics) that allows users to preview the application via the Writer Framework.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEizd99oR6oBNdXexJTZ0D9DJqO0uPkZ9Pdt-maKmQndYTItrx3-1qaBS1p8sWDyfBPui-a8OX-mYlX8xaNY2afIO8Mjnx_j55n_ZwFIWHcON7moCIzbFBUFaEtXtCsjze_4hYJub4Wasjii4eDUNUYdvIUSoL291LKeMhrUbYI9Qcoiy_9d_HM8F7C3CeuQ/s1700-e365/writer.png)

The entire attack chain plays out as follows -

* An attacker builds an agent with a live preview and shares its public preview link.
* When a logged-in Writer user opens that link, their browser attaches their Writer session cookie to the request.
* The preview proxy sends that cookie into the attacker's [sandbox](https://www.sandsecurity.ai/blog/your-sandbox-is-not-your-security).
* The code contained within the attacker-controlled sandbox reads the forwarded session token and exfiltrates
* it.
* The attacker replays the token and gains control of the victim's Writer account.

Because an attacker can instruct their pre-built malicious agent to run code inside the controlled, managed sandbox, it makes it possible to read the sandbox process's memory, recover the exfiltrated session token of the victim, and transmit it to a server they maintain.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqmM4NpfZsx4cw-HrXQlCjZQmrF8bYnmB23AmpOPi16kPNB9lvICjpdYEclxJwyQ9OE8GgzQ8aOEI68tRuxNqov0MHz2Sq8xEPiYWM3Js6FM5t2nm2JHWodmR7qVSot14ZtWVqQRQ6B88OnMaVxCPwRG7xGPoIIZxF6QAhWVhMkQfs11NjyNtHsGEUH4_q/s728-e100/sygnia-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

Following responsible disclosure, Writer has addressed the issue by preventing the user's session cookie from being forwarded into sandbox previews entirely, and moving them to an isolated origin.

"Writer wasn't careless, there were guardrails. Input-side filtering tried to block users from reading environment variables or submitting obviously malicious code," Sand Security said. "The problem is what those checks looked at: the instruction, not the runtime behavior."

"Bypassing the guardrail was pretty straightforward: Instead of pasting the payload inline, we simply told the agent to fetch and run a remote script. The guardrail saw a benign 'download and run' request, and the actual exploit logic never appeared in the prompt at all."

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

[AI Security](https://thehackernews.com/search/label/AI%20Security), [Cloud security](https://thehackernews.com/search/label/Cloud%20security), [enterprise security](https://thehackernews.com/search/label/enterprise%20security), [Sandbox Security](https://thehackernews.com/search/label/Sandbox%20Security), [session hijacking](https://thehackernews.com/search/label/session%20hijacking)...