---
title: Radio With No Radar: Why Agent Runtime Security Fails Without the Layers Beneath It
url: https://thehackernews.com/2026/11/radio-with-no-radar-why-agent-runtime.html
source: The Hacker News
date: 2026-11-04
fetch_date: 2026-11-05T08:45:13.078467
---

# Radio With No Radar: Why Agent Runtime Security Fails Without the Layers Beneath It

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg98jBiF1GNyn9ReXVuuNzrDrJ8-mdCvE5IhR6dUbEnucAAvmCW-lbjZmzjJx0EhFV2R6xhfph0uQ-cz4IO46xmarphU8oOZmuqbdHxTeosFZTJ45LN6VEQOAdLCFB_iwlP3t9_i9qiQqQua1oJMGmp5wILrYvUWRBTMAVJphcDt7Qo0Yi5gK9pIHhW5pAb/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/appsec-ai-readiness-d)

# [Radio With No Radar: Why Agent Runtime Security Fails Without the Layers Beneath It](https://thehackernews.com/2026/11/radio-with-no-radar-why-agent-runtime.html)

**The Hacker News**Nov 04, 2026AI Agent Security / SaaS Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhQqFIm3V3DsL6rHtjhkN8qVT2sU-caHUEuPgeepdZ6lLsIJ-09GFg_HVVBgeHP36W0abqUeCuaNuAOIheSGYB9hxmHbQGcgREBBxStEFLijgx-Cd8C8Z8wLuxgFFu75O8hAAOcdjAxgCZ-iYoBvYS09AcITdqMnmLZOn2JdGaEp04SPrgYkgQ14dl1S0JS/s1700-nu-rw-lo-l85-e365/reco.gif)

Nearly every agent security pitch now ends on the same promise: the product stops the bad action in real time. The promise holds for one kind of agent, the kind whose traffic passes through a gateway the enterprise owns. Most agents never touch one.

One recent case shows what that gap looks like in practice. An employee asked an AI assistant to trigger a mass-email automation. The automation hit a recipient-limit policy and failed, so the assistant, which was also connected to the employee's personal mailbox, offered to send the batch from there instead. The employee approved without registering that the assistant was about to route around the sanctioned system. An unknown number of external recipients received email from a personal account rather than the approved channel.

No jailbreak was involved. The assistant did exactly what it was built to do, and the fix was not retraining a model. It was a single runtime rule that blocks any attempt to reach more than fifty external domains and explains to the user what the tool is about to do. Knowing where to apply a rule like that depends on seeing which agents exist, what they are connected to and what normal looks like for each. That visibility is the part most runtime pitches skip.

## **The runtime is the application, not the pipe**

The year's largest agent launches placed agents inside platforms the buyer does not own. Claudeforce runs Claude inside Salesforce's trust boundary, Claude Tag lives inside Slack and Copilot lives inside Microsoft 365. Workday, which says AI now drives more than a quarter of its new annual contract value, runs its agents inside Workday. In each case the agent's tools are the application's features, its knowledge is the application's data and its permissions are the application's permission model.

A gateway can only inspect what passes through it. An agent that runs inside Salesforce, fires from a Flow, reads CRM records and writes case comments sends nothing past an inspection point, and the same is true of a Copilot agent assembling a document from SharePoint or a Slack-native agent reading years of channel history. The OWASP Agentic Skills Top 10 describes this gap as the "unreachable skill" scenario under AST09, No Governance: a capability deployed inside a third-party platform where no external scanner can go.

Security has made a move like this before. Firewalls once inspected packets by source, destination and port, until applications stopped mapping cleanly to ports and malicious traffic began to look identical to legitimate traffic. The inspection point moved up the stack to the application, where the signal lives. Agent runtime needs the same move, with a complication the earlier one never faced: the application layer belongs to someone else. A gateway-only strategy protects the agents an enterprise hosts itself, which are the fewest and the slowest growing.

## **The inspection point is also a target**

In March 2026, attackers compromised LiteLLM, the open-source gateway that routes agent traffic to model providers. The malicious packages were live for about forty minutes, and CloudSEK later put the exposure at more than 2,500 organizations. LiteLLM is the kind of component a security-conscious team adds on purpose to watch AI traffic, which made the inspection point itself the attack vector.

None of this argues against gateways. It argues against treating any single component as the whole strategy. A gateway is more software in the supply chain, with its own release pipeline and dependencies, and it concentrates exactly the traffic an attacker wants. When enforcement is a shared component, its failure is a shared failure.

## **A millisecond verdict needs a memory**

Runtime decisions are made in milliseconds, and the hard cases are the gray ones. A support agent pulling customer data may be doing its job or exfiltrating it. A coding agent reading a repository may be gathering context or performing reconnaissance. A finance agent creating an OAuth connection may be doing integration work or making the first move of a compromise. The action alone does not carry the verdict. The agent's identity and owner, its permissions, its normal behavior, the sensitivity of the data, the destination and the delegation chain behind the request do.

Chains raise the bar. Enforcement that evaluates only the last hop sees an authorized agent performing an action it has permission for, and misses that the authority arrived through a chain nobody approved. Judging the whole chain at runtime means already knowing it, and that knowledge cannot be assembled in a millisecond. Enforcement without that map is an air-traffic controller with a radio but no radar: commands can be issued, but the picture of which plane is headed where does not exist.

[![](data:image/png;base64...)](https://reco.ai/into-the-expanse-agent-runtime-security?utm_source=hackernews)

## **What real agent runtime looks like**

Three properties follow. Enforcement has to sit where the agents are, across several vantage points such as native platform hooks, API-level controls, the MCP layer, the browser and the endpoint, rather than at a single gateway. Every verdict has to be computed against a live map of identity, permissions, connectivity and activity (IPCA), plus data sensitivity and delegation, which is what turns the gray cases into judgments. And the response menu has to be wider than block.

Mature enforcement is...