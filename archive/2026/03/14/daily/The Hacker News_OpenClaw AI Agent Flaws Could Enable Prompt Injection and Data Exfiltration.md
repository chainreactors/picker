---
title: OpenClaw AI Agent Flaws Could Enable Prompt Injection and Data Exfiltration
url: https://thehackernews.com/2026/03/openclaw-ai-agent-flaws-could-enable.html
source: The Hacker News
date: 2026-03-14
fetch_date: 2026-03-15T04:34:47.860687
---

# OpenClaw AI Agent Flaws Could Enable Prompt Injection and Data Exfiltration

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [OpenClaw AI Agent Flaws Could Enable Prompt Injection and Data Exfiltration](https://thehackernews.com/2026/03/openclaw-ai-agent-flaws-could-enable.html)

**Ravie Lakshmanan**Mar 14, 2026Artificial Intelligence / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg2mVucJhli25A25joXcap-ewfeMT1Vh-95wQKQfGOue7PwZJ1_55YsG8OQ1DQF7WVOU8tsOy73kGDzgfpTLLeqTYQ1k9LqrFWTNavDmfvCV-9IIER9PfrRsdg1wA5UzpIMrer3xC1mBClBzKkaT6pfczDbppMjZM7afcWu-RURquDGrEfjq3vVBsmlltLm/s1700-e365/open-clawss.jpg)

China's National Computer Network Emergency Response Technical Team (CNCERT) has [issued](https://mp.weixin.qq.com/s/0M1sZq1HqwAAaMbRDBEZEw) a warning about the security stemming from the use of [OpenClaw](https://thehackernews.com/2026/02/openclaw-bug-enables-one-click-remote.html) (formerly Clawdbot and Moltbot), an open-source and self-hosted autonomous artificial intelligence (AI) agent.

In a post shared on WeChat, CNCERT noted that the platform's "inherently weak default security configurations," coupled with its privileged access to the system to facilitate autonomous task execution capabilities, could be explored by bad actors to seize control of the endpoint.

This includes risks arising from prompt injections, where malicious instructions embedded within a web page can cause the agent to leak sensitive information if it's tricked into accessing and consuming the content.

The attack is also [referred](https://securelist.com/indirect-prompt-injection-in-the-wild/113295/) to as indirect prompt injection (IDPI) or cross-domain prompt injection (XPIA), as adversaries, instead of interacting directly with a large language model (LLM), weaponize benign AI features like web page summarization or content analysis to [run manipulated instructions](https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/). This can [range from](https://www.pillar.security/blog/anatomy-of-an-indirect-prompt-injection) evading AI-based ad review systems and influencing hiring decisions to search engine optimization (SEO) poisoning and generating biased responses by suppressing negative reviews.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

OpenAI, in a blog post published earlier this week, said prompt injection-style attacks are evolving beyond simply placing instructions in external content to include elements of social engineering.

"AI agents are increasingly able to browse the web, retrieve information, and take actions on a user's behalf," it [said](https://openai.com/index/designing-agents-to-resist-prompt-injection/). "Those capabilities are useful, but they also create new ways for attackers to try to manipulate the system."

The prompt injection risks in OpenClaw are not hypothetical. Last month, researchers at PromptArmor found that the [link preview feature](https://www.aitextrisk.com/) in messaging apps like Telegram or Discord can be turned into a data exfiltration pathway when communicating with OpenClaw by means of an indirect prompt injection.

The idea, at a high level, is to trick the AI agent into generating an attacker-controlled URL that, when rendered in the messaging app as a link preview, automatically causes it to transmit confidential data to that domain without having to click on the link.

"This means that in agentic systems with link previews, data exfiltration can occur immediately upon the AI agent responding to the user, without the user needing to click the malicious link," the AI security company [said](https://www.promptarmor.com/resources/llm-data-exfiltration-via-url-previews-%28with-openclaw-example-and-test%29). "In this attack, the agent is manipulated to construct a URL that uses an attacker's domain, with dynamically generated query parameters appended that contain sensitive data the model knows about the user."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhQlbEO_3-A3BOegJt_YMqDJZGRhwQlZC-bI8RKyNkRzmRobJ7_SfJfuyVGlXSvbCxmsD3GcFUtV615hmwnsLGWgKcJUkBZNlCA0gqpDcokeCrdhlyO_eGxYUYgQ2v2Izss9y2ZuQk5WV5qmwE6MXV3_LmDtL90JbjBmekI7w28xPx-kwrjVrJFdwvtBfzl/s1700-e365/attackers.png)

Besides rogue prompts, CNCERT has also highlighted three other concerns -

* The possibility that OpenClaw may inadvertently and irrevocably delete critical information due to its misinterpretation of user instructions.
* Threat actors can [upload malicious skills](https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html) to repositories like ClawHub that, when installed, run arbitrary commands or deploy malware.
* Attackers can exploit [recently disclosed security vulnerabilities](https://thehackernews.com/2026/02/clawjacked-flaw-lets-malicious-sites.html) in OpenClaw to compromise the system and leak sensitive data.

"For critical sectors – such as finance and energy – such breaches could lead to the leakage of core business data, trade secrets, and code repositories, or even result in the complete paralysis of entire business systems, causing incalculable losses," CNCERT added.

To counter these risks, users and organizations are advised to strengthen network controls, prevent exposure of OpenClaw's default management port to the internet, isolate the service in a container, avoid storing credentials in plaintext, download skills only from trusted channels, disable automatic updates for skills, and keep the agent up-to-date.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/cyber-comm-guide-d)

The development comes as Chinese authorities have moved to restrict state-run enterprises and government agencies from running OpenClaw AI apps on office computers in a bid to contain security risks, Bloomberg [reported](https://www.bloomberg.com/news/articles/2026-03-11/china-moves-to-limit-use-of-openclaw-ai-at-banks-government-agencies). The ban is also said to extend to the families of military personnel.

The viral po...