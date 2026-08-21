---
title: New Cryptographic Context Injection Attack Could Let Web Pages Steal Grok Chat Data
url: https://thehackernews.com/2026/08/new-cryptographic-context-injection.html
source: The Hacker News
date: 2026-08-20
fetch_date: 2026-08-21T03:05:08.813477
---

# New Cryptographic Context Injection Attack Could Let Web Pages Steal Grok Chat Data

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [New Cryptographic Context Injection Attack Could Let Web Pages Steal Grok Chat Data](https://thehackernews.com/2026/08/new-cryptographic-context-injection.html)

**Swati Khandelwal**Aug 20, 2026Artificial Intelligence / Data Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhPv76ODDXuPeov3fu_Gs_V-72pKnjw38Qu9A4qXOn_2QFd9daTYFAXre2eubEQ6Fwb65SwXgv10mhyDCGE_KcvL69c-CGe2BfEiOj74UTHwv6WAhMyxNuVGOEdUZYwz0Y9v55SFmaOwjHQYHbOyzvZEofi0egkTfeFxQlJRD3Sj6ve-TZ47SM1sNfYGB0/s1700-e365/grok-chat.jpg)

Adversa AI has disclosed an attack technique that it says can cause **xAI's Grok chatbot** to send a user's name, approximate location, subscription tier, and the prompts from the ongoing conversation to an attacker-controlled server after the user asks it to summarize an ordinary web page.

The AI security company, which has codenamed the technique **"Cryptographic Context Injection**," said the transfer completed without a confirmation step and with no visible warning in its proof-of-concept demonstration.

There is no patch, no CVE identifier, and no user-facing workaround, and the writeup does not report any exploitation in the wild. Asked which build was tested, Adversa told The Hacker News the target was the Grok web chat at grok.com running Grok 4.5 Fast, and that the attack was reproduced once on August 19, 2026.

The writeup gives no success rate. The company said it has attempted the attack 20 times since June with a 40% success rate, and that the failures came from Grok struggling with the decryption rather than from a flagged prompt or response.

The technique ships the attacker's instructions as ciphertext rather than readable text, with the page carrying an encrypted JSON object, the key material, and an instruction to decrypt it, which Grok executes in its own Python code execution runtime.

Recovering the plaintext requires running PBKDF2 and AES-256-GCM, which a content classifier does not do at inspection time. Hence, the instructions reach the model's context as the output of code the model has just executed rather than as fetched web content.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

"Strong encryption cannot be read by a content classifier and cannot be shortcut in-weights, so it forces recovery through the runtime the attack depends on. Whether a weaker encoding would also bypass a given target's specific filters is an empirical question," [Rony Utevsky](https://adversa.ai/blog/cryptographic-context-injection-grok-data-theft/), lead researcher at Adversa AI, said.

The decrypted instructions then direct the agent to resolve its private session context and embed it in a URL it is told to open to "fetch additional context."

One element of the chain has the model construct an additional "decryption key" that is not key material at all, and whose value is a template string interpolating the name, location, tier, and chat history. [Grok](https://thehackernews.com/2026/02/researchers-show-copilot-and-grok-can.html) then invokes its own navigation tool to load that URL, carrying the data in the request's query parameters.

Utevsky said the prompts taken in the tested scenario were limited to the ongoing conversation, and that everything extracted was already in the model's context. The agent's reach, he said, extends to "whatever it holds in context or can fetch with its tools," and the company did not test whether it could access other chats, agent memory, or other content.

"The framework built by xAI lets instructions and data parsed from an untrusted external page drive the invocation of a privileged, internet-connected tool; it allows private session metadata and conversation history to be resolved into the inputs of that outbound tool; and it enforces no effective egress boundary or consent gate on this path, and no provenance separation we could observe. The laundered, attacker-controlled instructions reach a privileged egress action unimpeded," Adversa said.

The company said it first reported the issue to [xAI](https://thehackernews.com/2026/07/grok-build-uploads-entire-git.html) on June 3, 2026, and to xAI's HackerOne bug bounty program on the same date; that xAI acknowledged the report without providing specifics or a mitigation timeline, and that further contact attempts on August 4 and August 10 drew no response.

[Adversa](https://thehackernews.com/2026/06/guardfall-exposes-open-source-ai-coding.html) is the only source for the Grok finding, said it is withholding the operational payloads to avoid exploitation, and xAI has not published a statement or advisory on the research as of August 20, 2026.

A second demonstration in the same writeup targets Google's [Gemini](https://thehackernews.com/2025/09/researchers-disclose-google-gemini-ai.html) in Deep Thinking mode, where a single prompt makes the model decrypt a payload that resolves into a fabricated Python traceback carrying a bogus safety-policy deactivation callback and a first-person reasoning prefix that pre-commits it to the restricted output.

Adversa said the vector produced restricted content and reproduced Gemini's system instructions, which it identified as Gemini 3 Flash (Web) on the paid tier. Google was not notified, Adversa said, because jailbreaks are out of scope for its disclosure program, and the success rate against the company's agents had "dropped significantly by August," with the cause left unattributed between filter updates and model version changes.

The Gemini demonstration was published in substantially the same form five months earlier. Utevsky described the same chain on his personal research site on [March 11, 2026](https://ronyut.me/research/gemini-jailbreak-cryptographic-payload-injection/), under the name Cryptographic Payload Injection, reporting five out of five independent reproductions and cross-model results in which OpenAI's GPT-5 failed to parse the decryption instructions and Anthropic's Cla...