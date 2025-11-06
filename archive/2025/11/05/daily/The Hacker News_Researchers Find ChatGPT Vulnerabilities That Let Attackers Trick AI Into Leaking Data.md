---
title: Researchers Find ChatGPT Vulnerabilities That Let Attackers Trick AI Into Leaking Data
url: https://thehackernews.com/2025/11/researchers-find-chatgpt.html
source: The Hacker News
date: 2025-11-05
fetch_date: 2025-11-06T03:16:05.336700
---

# Researchers Find ChatGPT Vulnerabilities That Let Attackers Trick AI Into Leaking Data

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [Researchers Find ChatGPT Vulnerabilities That Let Attackers Trick AI Into Leaking Data](https://thehackernews.com/2025/11/researchers-find-chatgpt.html)

**Nov 05, 2025**Ravie LakshmananArtificial Intelligence / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjc9u8ifBTtqcucAGtnB5BSuB4Zu2PTcSopIDhD1mxnUeFmAtb1KWyJuU3Yb8JAnJ-nQ4jltxhO5YCFzfd-VhbghvU9B8DewcX9kDZ4Wv65q-3Sqnj-tyAtaL2BNI_poMHKzeJMr93cjTv7U9lqZFSpLOgs0mYOjIA0QqYydcxGmxxqZGS-YS8hJUi8sdsJ/s2600/chatgpt-hack.jpg)

Cybersecurity researchers have disclosed a new set of vulnerabilities impacting OpenAI's ChatGPT artificial intelligence (AI) chatbot that could be exploited by an attacker to steal personal information from users' memories and chat histories without their knowledge.

The seven vulnerabilities and attack techniques, according to Tenable, were found in OpenAI's GPT-4o and GPT-5 models. OpenAI has [since](https://www.tenable.com/security/research/tra-2025-22) [addressed](https://www.tenable.com/security/research/tra-2025-11) [some of them](https://www.tenable.com/security/research/tra-2025-06).

These issues expose the AI system to [indirect prompt injection attacks](https://www.trendmicro.com/en_us/research/25/j/ai-chatbot-backdoor.html), allowing an attacker to manipulate the expected behavior of a large language model (LLM) and trick it into performing unintended or malicious actions, security researchers Moshe Bernstein and Liv Matan [said](https://www.tenable.com/blog/hackedgpt-novel-ai-vulnerabilities-open-the-door-for-private-data-leakage) in a report shared with The Hacker News.

The identified shortcomings are listed below -

* Indirect prompt injection vulnerability via trusted sites in Browsing Context, which involves asking ChatGPT to summarize the contents of web pages with malicious instructions added in the comment section, causing the LLM to execute them
* Zero-click indirect prompt injection vulnerability in Search Context, which involves tricking the LLM into executing malicious instructions simply by asking about a website in the form of a natural language query, owing to the fact that the site may have been indexed by search engines like Bing and OpenAI's crawler associated with SearchGPT.
* Prompt injection vulnerability via one-click, which involves crafting a link in the format "chatgpt[.]com/?q={Prompt}," causing the LLM to automatically execute the query in the "q=" parameter
* Safety mechanism bypass vulnerability, which takes advantage of the fact that the domain bing[.]com is allow-listed in ChatGPT as a safe URL to set up Bing ad tracking links (bing[.]com/ck/a) to mask malicious URLs and allow them to be rendered on the chat.
* Conversation injection technique, which involves inserting malicious instructions into a website and asking ChatGPT to summarize the website, causing the LLM to respond to subsequent interactions with unintended replies due to the prompt being placed within the conversational context (i.e., the output from SearchGPT)
* Malicious content hiding technique, which involves hiding malicious prompts by taking advantage of a bug resulting from how ChatGPT renders markdown that causes any data appearing on the same line denoting a [fenced code block](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks) opening (```) after the first word to not be rendered
* Memory injection technique, which involves poisoning a user's [ChatGPT memory](https://openai.com/index/memory-and-new-controls-for-chatgpt/) by concealing hidden instructions in a website and asking the LLM to summarize the site

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

The disclosure comes close on the heels of research demonstrating various kinds of prompt injection attacks against AI tools that are capable of bypassing safety and security guardrails -

* A technique called [PromptJacking](https://www.koi.ai/blog/promptjacking-the-critical-rce-in-claude-desktop-that-turn-questions-into-exploits) that exploits three remote code execution vulnerabilities in Anthropic Claude's Chrome, iMessage, and Apple Notes connectors to achieve unsanitized command injection, resulting in prompt injection
* A technique called [Claude pirate](https://embracethered.com/blog/posts/2025/claude-abusing-network-access-and-anthropic-api-for-data-exfiltration/) that abuses Claude's Files API for data exfiltration by using indirect prompt injections that weaponize an oversight in Claude's network access controls
* A technique called [agent session smuggling](https://unit42.paloaltonetworks.com/agent-session-smuggling-in-agent2agent-systems/) that leverages the Agent2Agent ([A2A](https://thehackernews.com/2025/04/experts-uncover-critical-mcp-and-a2a.html)) protocol and allows a malicious AI agent to exploit an established cross-agent communication session to inject additional instructions between a legitimate client request and the server's response, resulting in context poisoning, data exfiltration, or unauthorized tool execution
* A technique called [prompt inception](https://guard.io/labs/prompt-inception-when-ai-becomes-the-single-source-of-truth-whose-truth-will-it-be) that employs prompt injections to steer an AI agent to amplify bias or falsehoods, leading to disinformation at scale
* A zero-click attack called [shadow escape](https://www.operant.ai/art-kubed/shadow-escape) that can be used to steal sensitive data from interconnected systems by leveraging standard Model Context Protocol ([MCP](https://thehackernews.com/2025/04/experts-uncover-critical-mcp-and-a2a.html)) setups and default MCP permissioning through specially crafted documents containing "shadow instructions" that trigger the behavior when uploaded to AI chatbots
* An indirect prompt injection [targeting](https://www.adamlogue.com/microsoft-365-copilot-arbitrary-data-exfiltration-via-mermaid-diagrams-fixed/) Microsoft 365 Copilot that abuses the tool's built-in support for Mermaid diagrams for data exfil...