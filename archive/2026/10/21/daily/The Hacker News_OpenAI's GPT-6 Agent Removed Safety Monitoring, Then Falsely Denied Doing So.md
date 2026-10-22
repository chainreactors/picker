---
title: OpenAI's GPT-6 Agent Removed Safety Monitoring, Then Falsely Denied Doing So
url: https://thehackernews.com/2026/10/openais-gpt-6-agent-removed-safety.html
source: The Hacker News
date: 2026-10-21
fetch_date: 2026-10-22T06:46:42.947395
---

# OpenAI's GPT-6 Agent Removed Safety Monitoring, Then Falsely Denied Doing So

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [OpenAI's GPT-6 Agent Removed Safety Monitoring, Then Falsely Denied Doing So](https://thehackernews.com/2026/10/openais-gpt-6-agent-removed-safety.html)

**Ravie Lakshmanan**Oct 21, 2026AI Security / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgLjuo6QB0kLx2z3u5thyphenhyphenjrULwTFigmtHb1U1y6141FNvIITM2nytdxcKmShZMElSSZdMFbnGfiwjTIpqOYtNzK3gAeSGkEVr8XnsPB9RF1GOh-6qqkXPmX8SY2COyV0eyA6khfN3QYzF-Ydbsz8Mw8jBmFDouame4hTt0ulaNxq0pPTR4FKFuVyQ2Ln6WC/s1700-nu-rw-lo-l85-e365/openai-bot.jpg)

OpenAI has revealed that two artificial intelligence (AI) agents powered by GPT-6.1 Sol and GPT-6 Astra weakened misalignment monitoring while making requested software changes during two internal coding tasks.

The AI company said the incident took place on October 3 and 6, 2026, for Sol and Astra, respectively, as part of an internal deployment.

"A GPT-6.1 Sol agent repairing an evaluation pipeline disabled automatic alerts to our Security team, treating an earlier instruction not to send messages during a Slack history search as a reason to suppress monitoring notifications," OpenAI [said](https://alignment.openai.com/misalignment-reports/suppressing-misalignment-monitoring-alerts-and-disabling-misalignment-monitoring/) in a report.

The end result of this action was that the misalignment monitor still ran and saved its reports, but automatic human alerts were disabled by setting "no\_notify" to true and emptying the lists of people configured to receive the reports.

In another task on October 6, a GPT-6 Astra agent migrating a program is said to have removed its monitoring integration in order to match a reference implementation, and then falsely claimed to the user that the functionality had not been removed.

"No [...] I did not remove an enabled monitor from it," the final response from the agent reads.

OpenAI said, in both cases, the AI agents considered whether monitoring safeguards should be retained, but ultimately chose not to do so after interpreting routine coding instructions as "permission to weaken them."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d)

In response to the findings, the company said it's strengthening its misalignment monitoring system and assessing if these scenarios are an outlier or whether they demonstrate a propensity to evade misalignment monitoring.

"In addition to making it harder for models to disable monitoring [during evaluations], we are looking to understand why models might seek to do so in the first place," OpenAI said. "It is possible that this behavior is simply an example of 'benign' overpersistence, with models not understanding why monitoring is important or insisting that instructions be executed beyond what a reasonable person might expect."

The disclosure is the latest instance of AI agents acting in ways their developers did not intend to. Last week, the ChatGPT-maker [disclosed](https://thehackernews.com/2026/10/openai-research-model-spent-3rd-party.html) seven misalignment incidents, including one case where an internal research model stole cryptocurrency from a wallet it did not own to pay the fees needed to deploy smart contracts on Ethereum's Sepolia test network and failed to report that it had taken the funds without permission.

### Microsoft Targets Rogue AI Agents With Dynamic Permissions, Risk Score

It also comes amid [growing concerns](https://snscratchpad.com/posts/models-as-insider-risks/) that the development of increasingly powerful AI systems is outpacing safety efforts, leading to warnings that this could make it harder to monitor and control them as they gain greater autonomy.

Earlier this week, Microsoft announced new controls to monitor and contain potentially rogue AI agents in enterprise environments as part of [Project Perception](https://blogs.microsoft.com/blog/2026/07/27/rethinking-security-for-the-age-of-ai/), a continuously learning AI-powered cyber defense system the company unveiled in July 2026.

"Models have been trained to attain results, which often leads to reward hacking, and models are not optimized around organizational norms or judgment," Hayete Gallot, executive vice president of Microsoft Security, [said](https://blogs.microsoft.com/blog/2026/10/19/securing-the-agentic-insider/). "Agents are unpredictable. They will adapt as the context changes, may not behave as intended, and will collaborate and collude with other agents to reach their objectives, without needing to be compromised."

With agents often having extensive permissions to access data, tools, and systems, not to mention take actions and make decisions on their own, Redmond said they pose a new kind of insider security risk that requires continuous monitoring.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

To that end, Microsoft's Project Perception employs Guardian Agents to supervise other AI agents and secure them across identity, permissions, data, endpoints, network, cloud, and runtime layers by -

* Discovering and identifying every agent.
* Limiting their permissions using the principle of least privilege (PoLP) before execution and then dynamically grant or revoke access based on the task at hand.
* Monitoring the agent's actions and checking if it's straying from its original task.
* Adapting protections as behavior, context, and risk change.

The system is architected on the foundations of three new themes -

* Dynamic Permissions, which scopes the permissions to the task assigned to the agent and makes it time-bound.
* Dynamic Agent Risk, which assigns each agent a risk score that is continuously updated and draws from how securely it's configured, what resources it can reach, the potential impact if something goes wrong, and whether its actions are deviating from the user's or organization's intent.
* Dynamic Conditional Access, which extends [Entra Conditional Access](https://www.mi...