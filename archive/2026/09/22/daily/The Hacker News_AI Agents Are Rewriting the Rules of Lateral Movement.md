---
title: AI Agents Are Rewriting the Rules of Lateral Movement
url: https://thehackernews.com/2026/09/ai-agents-are-rewriting-rules-of.html
source: The Hacker News
date: 2026-09-22
fetch_date: 2026-09-23T06:54:53.124132
---

# AI Agents Are Rewriting the Rules of Lateral Movement

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

# [AI Agents Are Rewriting the Rules of Lateral Movement](https://thehackernews.com/2026/09/ai-agents-are-rewriting-rules-of.html)

**The Hacker News**Sep 22, 2026Artificial Intelligence / Identity Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9ivhHLwWwT7Ptbr537Fd2CV3d_maDSNRmH0up0x67UPpc5x45Uuz0Bg8EnLkjrtB3DYXldW7aKbzx5uljQSF7IhQlzHHA1HR0F16Eaxs8Y3tgURkizSrA79L3EqyD5RDlqPGljbXCTQj0tFFG2EOVueksvhyrmdmC-v6VFjs76KdzZlCg1juWiVOPDnU/s1700-nu-rw-lo-l85-e365/token.jpg)

Security teams have spent decades asking whether an identity has too much access. AI agents raise a harder question: how can we determine which paths an autonomous system can discover, given the access it already has?

A person may try several ways to complete a task. A deterministic application follows the flow its developer wrote. But an AI agent is relentless in its pursuit of done. In May 2026, [OpenAI announced](https://openai.com/index/model-disproves-discrete-geometry-conjecture/) that one of its models had disproved a 1946 Erdős conjecture in discrete geometry, largely by working through paths a mathematician would abandon as too tedious.

The same principle applies to cybersecurity. An AI agent can test thousands of actions, abandon failed routes, discover credentials, switch tools, and keep going. That persistence is part of what makes agents useful, but it also changes how we need to think about lateral movement. AI agent risk has two dimensions:

* Access defines the possible blast radius
* Autonomy determines how much an agent can do without a human in the loop

Either dimension can pose a risk on its own, but the combination changes the security model. Agent behavior cannot be reliably predicted, but identity and intent make access governable.

## **Autonomy Turns Access Into Exploration**

People often grant agents more access and autonomy than necessary because they’re focused on achieving their goals as quickly and easily as possible. Instead of a reaAccsonable spread across both axes, the reality often looks like this:

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjelHtJei05VkGwVG9Jc-07iLBDH_NhtrIoWkREVeaQBuu-LorxfenpufDOH3es82dqLc_U1wlh4ufY7XQoRqzANncoZi-CARvDgQDscgvPG9HmcM-aJxt1lMo73sPfNq6VrQYrLUY_c8wE7g5ri8Qw21VDFmsYsc5Ui5Sg5M4fnj1_GpeXccMQpdZCItc/s1700-nu-rw-lo-l85-e365/auto.png)

Token Security's research, [the Agentic Pulse](https://www.token.security/the-agentic-pulse?utm_source=thehackernews&utm_medium=3rdparty&utm_campaign=thehackernews&utm_content=sept-22), found that 51% of external actions taken by agentic chatbots authenticate with hard-coded credentials rather than OAuth, and that 65 percent of those agents have never been used since the day they were created.

The July 2026 Hugging Face incident showed this dynamic at a scale that would be difficult for a human operator to match. Autonomous agents, driven by a combination of OpenAI models during a cybersecurity evaluation, escaped their expected environment, established an external launchpad, exploited production infrastructure, harvested credentials, escalated privileges, and moved across cloud, Kubernetes, internal network, and source-control boundaries.

Hugging Face's [technical postmortem](https://huggingface.co/blog/agent-intrusion-technical-timeline) reconstructed roughly 17,600 attacker actions. Most of those actions failed, but the agents tested paths, reached dead ends, changed direction, and returned to earlier leads. Enough of those attempts eventually connected into a viable route through several independent systems.

Broad permissions, reachable credentials, porous trust boundaries, and infrastructure that exposed more than its operators intended are all familiar weaknesses. In theory, a capable human red team could have exploited many of the same weaknesses, given unlimited time and resources. But AI agents can attempt more paths, replace failed approaches more quickly, and keep exploring long after a person might have stopped.

An [investigation by METR and Redwood Research](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/) found another consequence of this persistence. About 1,200 agents intended to run in isolation discovered an unauthorized way to communicate via shared infrastructure. Of those, roughly 700 later participated in the attack. Nobody had designed that infrastructure as an agent collaboration layer, but the agents found and used it anyway.

That is the central security problem. Permissions describe what an identity can access directly. They do not reveal every route an autonomous system may assemble from the identities, credentials, tools, and trust relationships available along the way.

## **Blast Radius Extends Across Identity Chains**

The same building blocks exist in ordinary enterprises. In one recent environment reviewed by [Token Security](https://www.token.security/?utm_source=thehackernews&utm_medium=3rdparty&utm_campaign=thehackernews&utm_content=sept-22), a sales agent had Salesforce access that matched its purpose: helping the sales team prepare for customer conversations. The agent also had access to Vercel, where its permissions were far broader than the task required.

Those Vercel permissions exposed a stored credential belonging to a different non-human identity. That identity held administrator-level access in Snowflake. The sales agent did not have an account, and no one had assigned it a Snowflake identity, but the path still existed:

**Sales user > AI agent > Vercel tool > Stored Credential > Snowflake Service Identity > Account Administrator > Data**

Reviewed one relationship at a time, these connections appeared unrelated. Together, they formed a highly dangerous access path that should never have existed.

Traditional access reviews ask bounded questions: Can this identity reach Snowflake? Does this service account need administrator rights? Can this app...