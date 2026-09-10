---
title: Infostealer Logs Expose Replayable AI Tokens That Can Bypass MFA
url: https://thehackernews.com/2026/09/infostealer-logs-expose-replayable-ai.html
source: The Hacker News
date: 2026-09-09
fetch_date: 2026-09-10T06:52:40.829057
---

# Infostealer Logs Expose Replayable AI Tokens That Can Bypass MFA

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Infostealer Logs Expose Replayable AI Tokens That Can Bypass MFA](https://thehackernews.com/2026/09/infostealer-logs-expose-replayable-ai.html)

**Ravie Lakshmanan**Sep 09, 2026Malware / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYP_zrhRTZRWnPPcDkUrE7dBh2Bf5eaQmlBxyl7euTRGjS0C8boQppnrmjY0CIVjGrS_PF13V1W3BPVI3RDPZY59s_7xIkI8LnFkg3Tn_Q0x7_tbCs_sMkvhZMREtFLW3IOJSNNmQrKCDI88FCWhfymdWkEWtdMMRzivv3lZXImjreAz0d74VXt2K80ipH/s1700-nu-rw-lo-l85-e365/tokens.jpg)

Cybercriminals are hijacking artificial intelligence (AI) user accounts via information stealer logs to create "stolen keys" that grant illicit access to tools from model providers like Google, Anthropic, and others.

Information stealers like Lumma Stealer or Vidar are equipped to harvest a wide range of data from compromised systems. This can include credential, session tokens, and API keys.

Once the data is stolen, threat actors who have purchased access to these off-the-shelf offerings put them up for sale on underground forums in the form of stealer logs to enable follow-on attacks.

"Session tokens and API keys are sought specifically by threat actors because it is often possible to replay those secrets and bypass credential-based authentication," Jeremy Kirk, director of threat intelligence at Okta, [said](https://www.okta.com/blog/threat-intelligence/signing_in_without_actually_signing_in) in a report shared with The Hacker News.

"Once successfully replayed, a threat actor is effectively logged in to an LLM service without actually logging in. Use of these skeleton keys makes abuse more challenging but not impossible to detect."

The identity services provider said it analyzed a 7 GB infostealer dump released on a Telegram channel on August 2, 2026, and found that the stealer log contained data belonging to 5,871 infected machines across 162 countries.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

Among those were thousands of unexpired authentication tokens corresponding to services like Google, Microsoft, Anthropic, Amazon, Gamma, Notion, Character.ai, Cursor, Poe.com, and Pika AI. Of the 44,791 unique JSON web tokens (JWTs) from the dataset, 555 JWTs were likely related to authentication for AI services.

Similar to a session token, a valid JWT can be [abused to obtain direct account access](https://developer.okta.com/blog/2018/06/20/what-happens-if-your-jwt-is-stolen), while bypassing regular authentication using a username and password, as well as multi-factor authentication (MFA).

Okta said it also identified 2,937 authentication-related JSON Web Encryption ([JWE](https://auth0.com/docs/secure/tokens/access-tokens/json-web-encryption)) data structures representing encrypted JWTs. Most of these tokens are said to have been set by OpenAI, which uses NextAuth.js. Although these keys can only be decrypted and parsed by the party holding the key, it's still possible for an attacker to replay these tokens and gain access to an account as long as they are not expired.

In all, the stolen data is said to have contained 1,843 unexpired JWTs and JWEs on the day it was released. Worryingly, 17.7% of the 44,791 JWTs have been found to include plaintext personally identifiable information (PII), such as name, phone number, or email address.

"This is another problematic aspect since that information does not expire or disappear, and it directly links a user with a specific service, which could be useful for social engineering attempts or phishing," Kirk said.

One key aspect worth mentioning here is that session replay attacks may not work in scenarios where an organization uses IP allowlisting, a security feature that blocks all network traffic except for specific, approved IP addresses or ranges. In addition, Google has added support for Device Bound Session Credentials ([DBSC](https://thehackernews.com/2026/04/google-rolls-out-dbsc-in-chrome-146-to.html)) to Chrome to cryptographically link a session token to a device so that a stolen token cannot be used on another system.

Besides credentials and tokens, an analysis of the stealer dump using [TruffleHog](https://github.com/trufflesecurity/trufflehog) has unearthed 24 still-valid API keys for four AI-related services, such as Google Gemini, OpenAI, Groq, and OpenRouter. An attacker who is in possession of such a key can weaponize it for espionage, extortion, or resource theft, and rack up AI token bills.

The abuse of API keys by bad actors to gain unauthorized access to a victim's large language model (LLM) and use the services to accomplish their goals, or sell the access to other cybercriminals, is referred to as [LLMjacking](https://thehackernews.com/2025/02/microsoft-exposes-llmjacking.html). The [technique](https://www.fortinet.com/blog/threat-research/someone-else-is-using-your-ai) is similar to campaigns that secretly use a system's resources to mine cryptocurrency, while passing the [heavy compute bills onto the victim](https://auth0.com/blog/llmjacking-stolen-api-key-hidden-cost/).

As adoption of AI surges within enterprise environments, data siphoned from infostealers has diversified the portfolio for cybercriminals to monetize, with [new black market sites](https://thehackernews.com/2026/08/poison-claude-sells-discounted-claude.html) emerging in the threat landscape for purchasing stolen token bundles and anti-detect browsers.

In one Telegram post flagged by Okta, an unspecified vendor has been spotted selling access to Claude, Cursor, ChatGPT, and Gemini at a discounted price, in addition to offering 24x7 support and money-back guarantees. Another service called Poison Claude claims to provide access to Anthropic's Opus 4.8, Opus 4.7, Opus 4.6, and Sonnet 4.6 models.

"Accessing accounts using stolen session data requires specific tooling," Okta said. "So-called 'anti-detect' browsers have features designed to use stolen authentication dat...