---
title: Bring Your Own Agent: Your Employees' Assistants Are Already Logged In
url: https://thehackernews.com/2026/10/bring-your-own-agent-your-employees.html
source: The Hacker News
date: 2026-10-12
fetch_date: 2026-10-13T08:38:43.088460
---

# Bring Your Own Agent: Your Employees' Assistants Are Already Logged In

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

# [Bring Your Own Agent: Your Employees' Assistants Are Already Logged In](https://thehackernews.com/2026/10/bring-your-own-agent-your-employees.html)

**The Hacker News**Oct 12, 2026Artificial Intelligence / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjyfIDT5M3MmWcxPZrWKZ_8EOy_WZY9iQHv9CQrAKcSZ7_EAadHyWzg9Aa5zQizJiwjNNLp6TDGShed4uvK0iq0d5TQHOV4wqah_jnbuJK-gFuObDCjO_bhwobK9PlO-CmK92s9PueGqpPI_puFGDAS_t4evoyjokLRlaXbql9cGN3d7POdsiXyUYvicVs/s1700-nu-rw-lo-l85-e365/bring.jpg)

The personal AI agents rollout is going about as smoothly as expected: Amazon [now blocks Meta's Muse](https://techrepublic.com/article/news-amazon-blocks-meta-muse) because it doesn't identify itself as a bot while browsing; Instinct keeps [raising privacy concerns](https://www.scworld.com/brief/instinct-ai-assistant-faces-privacy-concerns-amid-praise); and the horror stories from pretty much every personal AI agent keep piling up.

Regardless, the tech world is mesmerized by the capabilities and potential of these services. Less than a year after the first release of the open-source agent now called OpenClaw, the juggernauts are putting their weight behind the idea that each of us needs a personal assistant.

You know what's coming: your employees will connect their personal agents to work systems. There's no stopping that. Their agents already manage their home time, and managing their work time is the next logical step. For them, that is. Not for your security.

Given that personal agents will reach corporate systems whether approved or not, you might be wondering what the best way is to block them. If that’s your thinking, we’re here to offer you another path: enable safe usage instead, with identity as the control plane, and reap the benefits.

## **BYOD, meet BYOA(I)**

The Bring-Your-Own-Device shift is the obvious comparison, but calling this the new era of BYOD would undersell the challenges personal AI agents introduce. These aren't just devices presumed to be insecure that contain company data, but entire AIs that act on company systems in the employee’s name.

Bring-Your-Own-AI (or Bring-Your-Own-Agent) is, then, an identity challenge first and foremost. The best-case scenario is an agent wielding identities with an owner of record, limited approval, and no offboarding. You will also have agents who pretend to be employees, and agents with identities that have no easily recognizable owner.

But the main difference between the two movements is where the control point sits. BYOD gave IT a device to enroll. A personal agent is something you can't register: it lives on the vendor's computer or blends into the employee's. And it's likely in your systems today, whether you can see it or not.

## **How personal agents get in**

Whoever connects a personal AI agent to your systems today likely does this without ever filing a ticket. Instead, they connect it the way they'd connect other apps:

* **OAuth consent.** The agent requests access to Google Workspace, Microsoft 365, or Slack, and the employee clicks Allow. If your tenant lets users consent to third-party apps, that's the whole process.
* **A text thread.** Take Instinct, for example. Users text it, link their Google, Apple, or Facebook account, and it acts through the services they connect.
* **Saved passwords in the agent's browser.** Many of the agents can sign in to supported sites using passwords via a browser and an internal password manager. To your app, it looks like the employee is logging in.
* **API keys and personal access tokens.** For unofficial integrations, many agents can use API keys and personal access tokens, which require users to create long-term credentials.
* **The employee's own laptop.** A local agent like OpenClaw reaches whatever the machine it's installed on can see. Muse got a Mac app on September 18 that reads files, notes, calendars, and email with the user's permission, and can take optional Full Disk Access. Dots can work from the user's laptop once it's connected. The same goes for AI browsers like Atlassian's Dia, which read your open pages and connect to Slack and Gmail.

## **Meet the agents**

Less than a year into the category, we’re already starting to see sub-categories emerge in the nascent personal AI agent market. Some agents are more corporate, and others are more personal. But you’ll be hard-pressed to find one that’s truly tailored to a work environment in terms of what it does, and, more importantly, doesn’t do.

Take OpenAI’s Dots, for example. It’s as corporate as a product such as this can be. “Specialist dots” will have their own identities and credentials. OpenAI is working with Microsoft to deploy them under Agent 365, and the connectors are based on those created for ChatGPT. Even the rollout is limited to enterprise accounts and high-tier subscriptions.

xAI’s GrokBot has an R&D distribution channel via Cursor. If your devs have Cursor, they might have access to GrokBot. Here, the idea is to turn the AI bot tied to the work-controlled development environment into a personal assistant, but that doesn’t make it more governed. Like its competitors, GrokBot is more than willing to sign in to tools without using a clean API via its virtual computer.

Meta’s muse is consumer-first, and currently US and Canada-only. That said, a few weeks after launch, it gained many organizational connectors, including Slack, Linear, and Vercel. It’s also, ostensibly, the fastest-growing personal AI agent in the fall of 2026.

The buzziest personal AI agent in tech circles is Instinct. It’s a personal AI agent from a small start-up that works through text apps. It can connect to pretty much any work environment. And it has a privacy policy that raised many an eyebrow. Speaking of raising, Instinct itself raised $1 billion at a $10 billion valuation, so it’s one of the best-funded underdogs ever.

Finally, we’d be remiss if we did...