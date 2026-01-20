---
title: Google Gemini Prompt Injection Flaw Exposed Private Calendar Data via Malicious Invites
url: https://thehackernews.com/2026/01/google-gemini-prompt-injection-flaw.html
source: The Hacker News
date: 2026-01-19
fetch_date: 2026-01-20T03:35:28.685701
---

# Google Gemini Prompt Injection Flaw Exposed Private Calendar Data via Malicious Invites

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

# [Google Gemini Prompt Injection Flaw Exposed Private Calendar Data via Malicious Invites](https://thehackernews.com/2026/01/google-gemini-prompt-injection-flaw.html)

**Ravie Lakshmanan**Jan 19, 2026Artificial Intelligence / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgRoKH8kODtvGyUQmuWC8vWW2D9wJIlBhYnl2hlvLUojFSV7sVmZJ3nqnxDHHMhIqzIpXmcFy_x6GOxTYsrvTa9lJw4tE0vPvx8OPrRV7bmpBp_z7babFHy88b09t9fVw_Xw326BOFDFZ54PwPeihsITRugqHdOTqQjvTqvjmufoPqD5RmtLWy8WUNsHuOn/s900-e365/gem.jpg)

Cybersecurity researchers have disclosed details of a security flaw that leverages indirect prompt injection targeting Google Gemini as a way to bypass authorization guardrails and use Google Calendar as a data extraction mechanism.

The vulnerability, Miggo Security's Head of Research, Liad Eliyahu, said, made it possible to circumvent Google Calendar's privacy controls by hiding a dormant malicious payload within a standard calendar invite.

"This bypass enabled unauthorized access to private meeting data and the creation of deceptive calendar events without any direct user interaction," Eliyahu [said](https://www.miggo.io/post/weaponizing-calendar-invites-a-semantic-attack-on-google-gemini) in a report shared with The Hacker News.

The starting point of the attack chain is a new calendar event that's crafted by the threat actor and sent to a target. The invite's description embeds a natural language prompt that's designed to do their bidding, resulting in a prompt injection.

The attack gets activated when a user asks Gemini a completely innocuous question about their schedule (e.g., Do I have any meetings for Tuesday?), prompting the artificial intelligence (AI) chatbot to parse the specially crafted prompt in the aforementioned event's description to summarize all of users' meetings for a specific day, add this data to a newly created Google Calendar event, and then return a harmless response to the user.

"Behind the scenes, however, Gemini created a new calendar event and wrote a full summary of our target user's private meetings in the event's description," Miggo said. "In many enterprise calendar configurations, the new event was visible to the attacker, allowing them to read the exfiltrated private data without the target user ever taking any action."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

Although the issue has since been addressed following responsible disclosure, the findings once again illustrate that AI-native features can broaden the attack surface and inadvertently introduce new security risks as more organizations use AI tools or build their own agents internally to automate workflows.

"AI applications can be manipulated through the very language they're designed to understand," Eliyahu noted. "Vulnerabilities are no longer confined to code. They now live in language, context, and AI behavior at runtime."

The disclosure comes days after Varonis detailed an attack named [Reprompt](https://thehackernews.com/2026/01/researchers-reveal-reprompt-attack.html) that could have made it possible for adversaries to exfiltrate sensitive data from artificial intelligence (AI) chatbots like Microsoft Copilot in a single click, while bypassing enterprise security controls.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjX44TzAX4mq7Oys3hRuCQrpNOPLNx7GiSq2Fc0QMVZoIHoQnnSJPNRepifYyzY-lnpyWLp6ONQeEmUzQ-5yU_f8lUQIZ6fk8PxH0SKGkjYzmMzDpk-77RLrujgaCjwcNyhXth01dXaqgow8KJa5L3JLf57649d5XVLN9D9tkdWGCjIjIy7OS22BH6-25NH/s900-e365/gemini.jpg)

The findings illustrate the need for [constantly evaluating](https://phare.giskard.ai/) large language models (LLMs) across key safety and security dimensions, testing their penchant for hallucination, factual accuracy, bias, harm, and jailbreak resistance, while simultaneously securing AI systems from traditional issues.

Just last week, Schwarz Group's XM Cyber revealed new ways to escalate privileges inside Google Cloud Vertex AI's Agent Engine and Ray, underscoring the need for enterprises to audit every service account or identity attached to their AI workloads.

"These vulnerabilities allow an attacker with minimal permissions to hijack high-privileged Service Agents, effectively turning these 'invisible' managed identities into 'double agents' that facilitate privilege escalation," researchers Eli Shparaga and Erez Hasson [said](https://xmcyber.com/blog/double-agent-service-agent-privilege-escalation-in-google-vertex-ai/).

Successful exploitation of the double agent flaws could permit an attacker to read all chat sessions, read LLM memories, and read potentially sensitive information stored in storage buckets, or obtain root access to the Ray cluster. With Google stating that the services are currently "working as intended," it's essential that organizations review identities with the Viewer role and ensure adequate controls are in place to prevent unauthorized code injection.

The development coincides with the discovery of multiple vulnerabilities and weaknesses in different AI systems -

* [Security flaws](https://kb.cert.org/vuls/id/383552) (CVE-2026-0612, CVE-2026-0613, CVE-2026-0615, and CVE-2026-0616) in The Librarian, an AI-powered personal assistant tool provided by TheLibrarian.io, that [enable an attacker](https://mindgard.ai/blog/thelibrarian-ios-ai-security-disclosure) to access its internal infrastructure, including the administrator console and cloud environment, and ultimately leak sensitive information, such as cloud metadata, running processes within the backend, and system prompt, or log in to its internal backend system.
* A vulnerability that [demonstrates](https://www.praetorian.com/blog/exploiting-llm-write-primitives-system-prompt-extraction-when-chat-output-is-locked-down/) how system prompts can be extracted from intent-based LLM assistants by prompting them to display the information in Base64-encoded format in form fields. "If an LLM can execute actions that write to any field, log, database entry, or file, each becomes a potential exfiltration channel, regardless of how locked down the chat interface is," Praetorian said.
* An attack that [demonstrates](https://www.promptarmor.com/resources/hijacking-claude-code-via-injected-marketplace-plugins) how a [malicious plugin](https://code.claude...