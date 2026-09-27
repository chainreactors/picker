---
title: Zero Trust for AI Agents Starts With Fixing Zero Visibility
url: https://thehackernews.com/2026/09/zero-trust-for-ai-agents-starts-with.html
source: The Hacker News
date: 2026-09-26
fetch_date: 2026-09-27T07:25:09.489144
---

# Zero Trust for AI Agents Starts With Fixing Zero Visibility

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [Zero Trust for AI Agents Starts With Fixing Zero Visibility](https://thehackernews.com/2026/09/zero-trust-for-ai-agents-starts-with.html)

**The Hacker News**Sep 26, 2026Artificial Intelligence / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhbfTXTCeNSvaPIRWOUJJxKPfYp45QnSjl24XZ1Set210zScJhg03o_TYX0QKPQdcSq-vkiWnymSqBu-bSwcCm1Kb2Te5do1VIcbCQjc_-TOOR6VwqRiHu5LE-tBb0gdrDjmPuDADfUraASQenGh-1gI4PF_xa2GwREsDM4vq4_C-aEU8EJsBBvhykJ1E0/s1700-nu-rw-lo-l85-e365/sans-article.jpg)

The way we talk about AI agents is shifting, and the way we implement them requires an even more fundamental shift. While earlier discourse focused on how quickly organizations could stand up agents and how much productivity they could promise, a string of recent incidents, including a widely discussed intrusion at Hugging Face during an evaluation of OpenAI agents, has spurred organizations to examine whether speed has outpaced the ability to [secure what gets deployed](https://thehackernews.com/2026/09/ai-agents-are-rewriting-rules-of.html). Security teams are increasingly asking what an agent can reach once it's running, and whether anyone would notice before it mattered. However tempting it may be to jump directly into enforcement controls and detections, you need to look before you leap.

[Research from Veeam](https://www.veeam.com/company/press-release/emea-organizations-facing-a-shadow-agent-crisis-as-boardroom-anxiety-over-personal-liability-grows-veeam-research-finds.html) reveals that 70% of organizations admit that AI workflows are already in contact with sensitive corporate data without full oversight in place, and 67% report that IT cannot fully track the autonomous workflows that employees are building. Shadow AI is just one of the challenges to visibility of AI agents, but it exemplifies how quickly and pervasively this fundamental first step can slip through your grasp.

Zero Trust principles can support an AI governance program, but only in the right order. "You cannot govern what you cannot see" is the underlying principle right at the top of the SANS cheat sheet, [Zero Trust for AI Agents: The Security Checklist](https://www.sans.org/posters/zero-trust-ai-agents-security-checklist?utm_medium=Sponsored_Content&utm_source=Hacker_News&utm_rdetail=NA&utm_goal=Orders&utm_type=Live_Training_Events&utm_content=THN_CDI26_Sep_OA_AIChecklist&utm_campaign=SANS_CDI_2026). The cheat sheet places inventory ahead of every enforcement control and treats this as a foundational prerequisite for a reason. In practice, organizations may skip to a policy enforcement point or an authorization scheme for an agent that has no named owner, no defined scope, and no entry in any inventory. That order of operations is a diagnosis of where Zero Trust programs can fail. A proxy or an authorization layer sitting in front of an unknown population of agents has nothing real to enforce against.

Here are three visibility challenges to look for, with implications for you to consider when you “Think Red” like an attacker, and the solutions you can employ when you “Act Blue” as an informed defender.

## **Challenge One: Agent Use Is a New Form of Shadow IT**

With any new technology, adoption moves first, and governance follows later, if it follows at all. Once security teams notice this gap, the first instinct is often prevention, which can include blocking unapproved tools, cutting off access, or just shutting down anything unfamiliar. Budget and attention accumulate for these processes first, but blocking things before anyone has a picture of what already exists risks shutting down legitimate use along with the shadow deployments. While the problem of Shadow IT has been acknowledged and addressed in other technologies for a long time, we are still crawling when it comes to doing this for AI.

**Think Red:** When the agent is effectively invisible to you, an attacker doesn't need to breach much of anything to gain a foothold. A recent example in the news was [an incident at METR](https://thehackernews.com/2026/09/attackers-steal-metr-api-key-and.html), the nonprofit known recently for their evaluation of the Hugging Face incident. An attacker discovered an employee’s personal EC2 instance running a vibe-coded agentic app, then trivially bypassed authentication and prompted the agent to hand over its model provider API key. Over three weeks, the intruder used the equivalent of $600,000 in tokens, as there was no spending limit on the API key. METR’s internal dashboard simply didn’t show data on rate-limited requests at all, and token volume alone was not enough to raise any flags.

**Act Blue:** Cloud technology has experienced these same growing pains, and we can look there for the road to visibility. Every company now has tighter controls around cloud, such as monitoring AWS/Azure usage and spending, and ensuring unused VMs are turned off or destroyed; but nobody does this for agents yet. Treat AI and agent spend, along with API-key issuance, as discovery signals. Finance and procurement are another vantage point that may also be overlooked. Publish an approved-provider path before blocking anything, so legitimate use has somewhere to go, and when it comes the operating order, start with the principle of "know first, then restrict."

## **Challenge Two: No Single Camera Can Take the Full Picture**

Even once an organization commits to discovery, there is no single vantage point that gives you the whole population. Agents live across the network, the endpoint, the browser, and inside SaaS hosted elsewhere, and any one lens leaves large blind spots.

Traffic to AI providers is TLS-encrypted, so an inline sensor sees a destination and a byte count, not a prompt, a tool call, or a data exfiltration, often going to the exact same domains as legitimate apps. Network analysis alone can't tell this apart from anything else on the wire. Endpoint tools miss...