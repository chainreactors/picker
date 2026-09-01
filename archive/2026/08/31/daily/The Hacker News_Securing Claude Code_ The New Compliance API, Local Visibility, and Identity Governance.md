---
title: Securing Claude Code: The New Compliance API, Local Visibility, and Identity Governance
url: https://thehackernews.com/2026/08/securing-claude-code-new-compliance-api.html
source: The Hacker News
date: 2026-08-31
fetch_date: 2026-09-01T07:01:28.888129
---

# Securing Claude Code: The New Compliance API, Local Visibility, and Identity Governance

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

# [Securing Claude Code: The New Compliance API, Local Visibility, and Identity Governance](https://thehackernews.com/2026/08/securing-claude-code-new-compliance-api.html)

**The Hacker News**Aug 31, 2026Artificial Intelligence / Endpoint Visibility

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEithkMoEFgk1IZj_h_hGp94DwzD4UyQGh2f-epiRD6fn_XcMyB44HkXe-7XaHzviE8sImzIctDBjibyY0Gdrt_OPFFeja3KnOd9KsPFP3PeTxUzlshseSyukl0-cmQWZctAeVQHTUpvW99C8FZrhCcwPDZWoYShfC9jTGqmj1Va2K-Mo2kK6GbSksGIbM4/s1700-nu-rw-lo-l85-e365/dan.jpg)

Claude Code reads files, runs shell commands, invokes MCP tools, and acts through the credentials available on a developer’s machine. Anthropic’s new Compliance API endpoints give security teams their clearest view yet into that activity. They also expose a larger problem: activity logs alone cannot tell you whether an agent’s access is legitimate.

AI has moved from the browser tab to the endpoint with harnesses like Claude Code. They run on developers' machines, execute bash commands locally, and connect to third parties via MCP servers, skills, and plugins. All this so the user can outsource labor to the machine and focus on designing, thinking, and creating.

Local agents are not a niche category. They account for 68.6% of the AI agents [Token Security discovers](https://www.token.security/the-agentic-pulse?utm_source=thehackernews&utm_medium=3rdparty&utm_campaign=thehackernews&utm_content=aug-31) in customer environments, and they often inherit the employee's credentials, network position, and permissions.

The shift to the endpoint has major implications for security. With Claude Code, there is no centralized console to monitor endpoint agents across local configurations, identity and access, and runtime. Before August 2026, Anthropic's native controls had limited visibility into what those agents were actually doing, forcing teams to use third-party extensions just to achieve the bare minimum of governance.

With the new local session transcript endpoints in the Anthropic compliance API, you can better govern your local agents while understanding which limitations still exist.

## A harness is not a chatbot

A harness is a sophisticated orchestrator. It takes user input and sends it to the LLM along with the full session context. The LLM itself doesn’t maintain state; it receives everything it needs from the harness to respond on an ad hoc basis. The component that actually runs commands, authenticates to third parties, and connects to MCP servers is the harness, not the LLM.

Compare an endpoint agent to a human body. The LLM is the brain: it processes the data and calls the shots. Everything else is the harness, from the hands and the legs to the sensory organs. It's a weird hybrid, and our security model has to adapt to fit it. The brain runs in Anthropic's cloud, but the hands run on your endpoints, and that is where your visibility and control have to live.

## Unorthodox design

It’s en vogue to say that SaaS is dead, and it's a little SaaD, because classic SaaS took care of a lot of things for us. We expect a service to let us manage and monitor our enterprise from a central dashboard, control organizational policies, and clearly see what the agents within our enterprise can do.

That is not the case with local harnesses. Claude Code challenges the classic shared-responsibility model and puts more load on admins. In a Token-commissioned Cloud Security Alliance [survey](https://www.token.security/lp/autonomous-but-not-controlled-ai-security-data-report-csa) of 418 IT and security professionals, 68% rated their visibility into AI agents as high. In the same survey, 82% had discovered an agent in the past year that security, IT, or governance did not know existed.

Riddle me this: I live on your host as an agent, but I was here long before any LLM. I know more about your Claude Code than Anthropic does, because endpoints are my realm.

Because much of Claude Code’s execution happens locally, endpoint telemetry can reveal processes, files, and configurations that cloud services cannot see. But EDR provides evidence, not a governance model. It cannot connect an agent’s activity to its owner, intent, credentials, and permissions.

Anthropic's own tooling helps, but it isn't enough to prevent LLMs from performing destructive actions, even if those actions may be legitimate. There are three key layers for gathering data to govern local AI agents effectively. You need to understand what Anthropic gives you, what only an endpoint agent can collect, and what you need to do with the data.

## Layer 1: Managed settings, the policy baseline

Anthropic's enforcement mechanism is managed settings. Every endpoint that installs Claude Code has a managed-settings record: a JSON file on Mac and Linux, and registry records on Windows. Its rules take precedence over global, project, and user settings, allowing you to enforce a baseline over every Claude Code session in the organization. On a Claude Code enterprise plan, you apply policies through the GUI; without one, your MDM can write the managed-settings record across endpoints.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjYaNrK5xw-VI3GlCDJAEd94pu1JzWWzEqACp902n6uRrRzU_3DZwTtsc8z22gkeNXrYa2JtMt9MLP5VYfMnowLXDSVYc_SR3hZwpeg_oLY05zFzP_5b0nglSvVpd3iVma5gM9j1dv68-d8hQZVRVP_Hv1NBV68WjnyLmGAwm-3wyjqiMXAyj6RpTR097Q/s1700-nu-rw-lo-l85-e365/1.png)

The available rules cover a lot:

* Allow and deny lists for specific MCP servers
* Regexes over bash commands
* Disabling skills from running commands, and more

They help, but they take a lot of maneuvering room away from your developers, and static allow/deny policies aren't built for the pace of modern AI. Worse, they don't know context or intent. In effect, they're a big boulder in the middle of a river, disrupting the stream but not stopping it.

## Layer 2: The Compliance API

Until recently, ...