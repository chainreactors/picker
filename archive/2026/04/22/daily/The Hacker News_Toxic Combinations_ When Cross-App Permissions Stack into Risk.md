---
title: Toxic Combinations: When Cross-App Permissions Stack into Risk
url: https://thehackernews.com/2026/04/toxic-combinations-when-cross-app.html
source: The Hacker News
date: 2026-04-22
fetch_date: 2026-04-23T04:45:14.677549
---

# Toxic Combinations: When Cross-App Permissions Stack into Risk

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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

# [Toxic Combinations: When Cross-App Permissions Stack into Risk](https://thehackernews.com/2026/04/toxic-combinations-when-cross-app.html)

**The Hacker News**Apr 22, 2026SaaS Security / AI Agents

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjeaSL6v6uahfzJpHJb0ATKZ7cbexnfYIayT74IyU1S-7f3T-4gfnWowlobm5RH4ZYrsIdeNq_OOHGxp2LbU-aELaO9RbYa15MfKN38-ZQPGhrgH0PYCsVIucG95SSw-WCzzo9eUhITn4A3txsa8H59XhTcAaOObC0r-Es_7i0RH8aDo_qhZ45MfaOTVF2t/s1700-e365/reco.png)

On January 31, 2026, researchers [disclosed](https://treblle.com/blog/moltbook-breach-breakdown) that Moltbook, a social network built for AI agents, had left its database wide open, exposing 35,000 email addresses and 1.5 million agent API tokens across 770,000 active agents.

The more worrying part sat inside the private messages. Some of those conversations held plaintext third-party credentials, including OpenAI API keys shared between agents, stored in the same unencrypted table as the tokens needed to hijack the agent itself.

This is the shape of a toxic combination: a permission breakdown between two or more applications, bridged by an AI agent, integration, or OAuth grant, that no single application owner ever authorized as its own risk surface.

Moltbook's agents sat at that bridge, carrying credentials for their host platform and for the outside services their users had wired them into, in a place that neither platform owner had line of sight into. Most SaaS access reviews still examine one application at a time, which is the blind spot attackers are learning to target.

## How Toxic Combinations Form

Toxic combinations are rarely the product of a single bad decision. They appear when an AI agent, an integration, or an MCP server bridges two or more applications through OAuth grants, API scopes, or tool-use chains, and each side of the bridge looks fine on its own because the bridge itself is what no one reviewed.

As an example, imagine a developer installs an MCP connector so their IDE can post code snippets into a Slack channel on request. The Slack admin signs off on the bot; the IDE admin signs off on the outbound connection; neither signs off on the trust relationship between source editing and business messaging that exists the moment both sides are live. It runs in both directions: prompt injections inside the IDE push confidential code into Slack, and instructions planted in Slack flow back into the IDE's context on the next session.

The same shape appears wherever an AI agent bridges Drive and Salesforce, a bot wires a source repository into a team channel, or any intermediary makes two apps trust each other through a grant that looks normal in each.

## Why Single-App Reviews Miss Them

Conventional access review rarely catches this shape. It strains in the territory modern SaaS has opened up: non-human identities like service accounts, bots, and AI agents with no human behind them, trust relationships that form at runtime rather than at provisioning time, and OAuth and MCP bridges are wired between apps without the governance catalog knowing.

Answering "who holds this scope plus those two other scopes, and what can those scopes accomplish together" becomes much harder once the scopes in question live on a token nobody provisioned through any identity system to begin with.

The telemetry gap is widening quite fast.

AI agents, MCP servers, and third-party connectors now sit across two or three adjacent apps by default, and non-human identities outnumber human ones in most SaaS environments. The Cloud Security Alliance's State of SaaS Security 2025 report [found](https://cloudsecurityalliance.org/artifacts/state-of-saas-security-report-2025) that 56% of organizations are already concerned about over-privileged API access across their SaaS-to-SaaS integrations.

## Things Worth Thinking About

Closing the gap is largely a matter of shifting where review happens, from inside each app to between them. Here are a handful of things worth thinking about to address this type of issue:

| Area to review | What it looks like in practice |
| --- | --- |
| Non-human identity inventory | Every AI agent, bot, MCP server, and OAuth integration sits in the same register as a user account, with an owner and a review date. |
| Cross-app scope grants | A new write scope on an identity that already holds read scopes in a different app is flagged before approval, not after. |
| Bridge review on creation | Every connector that links two systems has a review trail naming both sides and the trust relationship between them. |
| Long-lived token hygiene | Tokens whose activity has drifted from the scopes they were originally granted are candidates for revocation, not renewal. |
| Runtime drift monitoring | Cross-app scope anomalies and identities operating across a new app combination are the tells a toxic combination is forming. |

These are procedural disciplines more than product choices, and they work with whatever access review tooling is in place. The reality is that seeing these connections at scale is hard without a platform built to watch the runtime graph continuously. Manual review doesn't scale past the first few dozen integrations.

## Where Dynamic SaaS Security Platforms Fit In

Dynamic SaaS security platforms automate the cross-app view that procedural review sets up. Where IGA inventories roles for onboarded systems, dynamic SaaS security watches the runtime graph continuously: which identities exist, which apps they touch, what scopes live on which tokens, and which trust relationships have been wired in after the last provisioning review.

The monitoring has to run continuously, because the bridges these platforms need to catch are created at the speed of an MCP install or an OAuth consent click.

Reco is one example of this category. Its platform connects identities, permissions, and data flows across the whole SaaS environment, so a combination of scopes in Slack, Drive, and Salesforce is evaluated as one exposure rather than three separate approvals.

The first step is discovering every AI agent, integration, and OAuth identity operating across the environment, so the inventory any cross-app review depends on actually exists. Agents that security teams did not know were there, or agents that quietly...