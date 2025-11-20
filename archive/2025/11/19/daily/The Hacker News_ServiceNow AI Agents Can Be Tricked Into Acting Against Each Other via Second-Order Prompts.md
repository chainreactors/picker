---
title: ServiceNow AI Agents Can Be Tricked Into Acting Against Each Other via Second-Order Prompts
url: https://thehackernews.com/2025/11/servicenow-ai-agents-can-be-tricked.html
source: The Hacker News
date: 2025-11-19
fetch_date: 2025-11-20T03:10:23.968355
---

# ServiceNow AI Agents Can Be Tricked Into Acting Against Each Other via Second-Order Prompts

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

# [ServiceNow AI Agents Can Be Tricked Into Acting Against Each Other via Second-Order Prompts](https://thehackernews.com/2025/11/servicenow-ai-agents-can-be-tricked.html)

**Nov 19, 2025**Ravie LakshmananAI Security / SaaS Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgoPK3N8k6tgxGcB7a-bCV3NfNUyR_iJuH7RxJJjya0hePCXNoQDQhZvHWDcsunCpNlA9F4uhk0EzWA1sFw5rCRa6zd4hUH3SzRcDusauukG-GA-tGfmex2HFTndPiTT1LeexpWsNBfmv70tiAB04J1yTIXSdnpm2_-Q12RaCfBzkr3aG_Icv5pEe-NI-ed/s790-rw-e365/ai-agents.jpg)

Malicious actors can exploit default configurations in ServiceNow's Now Assist generative artificial intelligence (AI) platform and leverage its agentic capabilities to conduct prompt injection attacks.

The second-order prompt injection, according to AppOmni, makes use of Now Assist's agent-to-agent discovery to execute unauthorized actions, enabling attackers to copy and exfiltrate sensitive corporate data, modify records, and escalate privileges.

"This discovery is alarming because it isn't a bug in the AI; it's expected behavior as defined by certain default configuration options," [said](https://appomni.com/ao-labs/ai-agent-to-agent-discovery-prompt-injection) Aaron Costello, chief of SaaS Security Research at AppOmni.

"When agents can discover and recruit each other, a harmless request can quietly turn into an attack, with criminals stealing sensitive data or gaining more access to internal company systems. These settings are easy to overlook."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

The attack is made possible because of agent discovery and agent-to-agent collaboration capabilities within ServiceNow's Now Assist. With Now Assist offering the ability to automate functions such as help-desk operations, the scenario opens the door to possible security risks.

For instance, a benign agent can parse specially crafted prompts embedded into content it's allowed access to and recruit a more potent agent to read or change records, copy sensitive data, or send emails, even when built-in prompt injection protections are enabled.

The most significant aspect of this attack is that the actions unfold behind the scenes, unbeknownst to the victim organization. At its core, the cross-agent communication is enabled by controllable configuration settings, including the default LLM to use, tool setup options, and channel-specific defaults where the agents are deployed -

* The underlying large language model (LLM) must support agent discovery (both Azure OpenAI LLM and Now LLM, which is the default choice, support the feature)
* Now Assist agents are automatically grouped into the same team by default to invoke each other
* An agent is marked as being discoverable by default when published

While these defaults can be useful to facilitate communication between agents, the architecture can be susceptible to prompt injections when an agent whose main task is to read data that's not inserted by the user invoking the agent.

"Through second-order prompt injection, an attacker can redirect a benign task assigned to an innocuous agent into something far more harmful by employing the utility and functionality of other agents on its team," AppOmni said.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

"Critically, Now Assist agents run with the privilege of the user who started the interaction unless otherwise configured, and not the privilege of the user who created the malicious prompt and inserted it into a field."

Following responsible disclosure, ServiceNow said the behavior is intended to be this way, but the company has since updated its documentation to provide more clarity on the matter. The findings demonstrate the need for strengthening AI agent protection, as enterprises increasingly incorporate AI capabilities into their workflows.

To mitigate such prompt injection threats, it's advised to configure supervised execution mode for privileged agents, disable the autonomous override property ("sn\_aia.enable\_usecase\_tool\_execution\_mode\_override"), segment agent duties by team, and monitor AI agents for suspicious behavior.

"If organizations using Now Assist's AI agents aren't closely examining their configurations, they're likely already at risk," Costello added.

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

[Access Control](https://thehackernews.com/search/label/Access%20Control)[AI Security](https://thehackernews.com/search/label/AI%20Security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[privilege escalation](https://thehackernews.com/search/label/privilege%20escalation)[Prompt Injection](https://thehackernews.com/search/label/Prompt%20Injection)[SaaS Security](https://thehackernews.com/search/label/SaaS%20Security)[ServiceNow](https://thehackernews.com/search/label/ServiceNow)[threat detection](https://thehackernews.com/search/label/threat%20detection)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/wiz-aws-ai-security)

Trending News

[![⚡ Weekly Recap: Hyper-V Malware, Malicious AI Bots, RDP Exploits, WhatsApp Lockdown and More](data:image/svg+xml;base64... "⚡ Weekly...