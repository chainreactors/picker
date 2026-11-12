---
title: We Built An Agent That Broke All of Our Security Rules. Here's What We Learned.
url: https://thehackernews.com/2026/11/we-built-agent-that-broke-all-of-our.html
source: The Hacker News
date: 2026-11-11
fetch_date: 2026-11-12T09:02:55.061339
---

# We Built An Agent That Broke All of Our Security Rules. Here's What We Learned.

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgueiGhtTJ4g8vfPjVOP22mnT6eczZI-CgiOkXQ_Zv0gVno2MkG5UlOExxvSSAylm8NAtCfFkeaPxbyR3vYtpyOVi9ROWrrVZ9FKHFBH1IrQCCR46b2kh7JNKxenqefzCkCUewWhqRlds-IYjwzH7N7iWGpXxzeqhS6vIHDWIohTDx2ZZZReOOwVWv-SAmG/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-infographic-d)

# [We Built An Agent That Broke All of Our Security Rules. Here's What We Learned.](https://thehackernews.com/2026/11/we-built-agent-that-broke-all-of-our.html)

**The Hacker News**Nov 11, 2026AI Agent Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhB22NtEOE6ioVcc92S5bLfFX3tbKyjNkx0j8OmHekqWq6Od4h9DtFmbmdd74VzwHCh5h6NbWnBgHgKzC49DwS7QAgA0uH3eL7BvBnN9QJu3U5-oiy5ZFMN7PvaJTBqjP7TR5VMjzrGxjfOfjgBqs3lecFZnWGEYNDp_BJgklco1L_acBqGm1M_CvtfLaY/s1700-nu-rw-lo-l85-e365/AI-AGENT.png)

We tell customers three things about securing AI agents: they need their own identities, access that fits the job they’re given, and traceability that’s separate from any human’s. That was true for us at Token as well. Then, we built an agent that broke all three by default.

This helped us think through how such agents should be defended. When a browser agent acts inside a user’s authenticated session, the application may see the user but not the agent, the delegation, or the task’s intended scope. By creating an agent that breaks all the security rules, Token learned how companies should be using identity to gain control, especially as agent use scales. Standards are coming, but there are steps security teams can take today.

## **The agent we would have flagged**

The [agent we created is named Rehearsal](https://www.token.security/blog/introducing-token-rehearsal-walkthrough-learning?utm_source=thehackernews&utm_medium=3rdparty&utm_campaign=thehackernews&utm_content=nov-11). Its job is to answer questions inside the Token platform by doing rather than telling. It autonomously opens pages in the browser tab, sets filters, and fills in forms.

From a security perspective, it’s a typical UI agent that runs in the user’s browser. That’s what makes it useful. But it also means the agent runs within the user’s session and has their reach.

Moreover, to the server behind the page, the agent’s clicks are inherently indistinguishable from the user’s, because nothing in a session cookie points to who the session driver is.

## **What controlling both sides made possible**

Because Token owns both the agent and the app it runs, we can close each gap from the inside. For example, Token knows who’s driving the session because Rehearsal tells it who is.

We learned that there are multiple best practices that you can apply when you control the AI agent itself:

* While the agent moves, dim and lock the application and clearly indicate who has control.
* Record every move for each session, including those that were blocked.
* Reduce the agent’s reach below the user’s. For Rehearsal, we ensure the dashboards are read-only. It can’t save anything without the user’s approval, doesn’t fill in secret fields, and never sends a call that the platform has refused. It also understands the dashboard controls through the page’s accessibility labels.

This works for our own agent, but only because it relies on access that no outside agent has.

## **Who has to fix it for everyone else?**

We could give Rehearsal an actor, a scope, and a page map because we're the ones who wrote it. A browser agent driving your CRM or your cloud console has none of that. The app can't tell that it’s there, and the agent can't tell which field holds a secret or which button deletes a record. The session itself carries the user's identity.

The way out is to give agents their own lanes, separate from human users'. The web has started building them, but it isn't necessarily focused on holistic approaches.

The browser can mark when its agent is driving and restrict itself accordingly. Chrome auto-browse, for example, already requires a person’s approval before high-stakes actions such as payments or mass emails, limits its agent to the sites the task requires, and tags the pages the agent visits in the user’s history. Microsoft lets admins turn agentic browsing on per site and pause it before passwords and card numbers are entered.

The app can publish its actions as tools. WebMCP, a draft that Google and Microsoft are writing in a W3C community group, lets a site expose actions that an agent can call directly and flag each one as read-only or consequential. That way, the agent doesn't need to guess what a button does.

The agent can sign its requests. Web Bot Auth, now an IETF working group draft, lets a site verify which agent sent a request.

What’s missing is a layer that connects them. Each lane knows something the others don’t, and none of them passes it on. The browser knows its agent is driving, but neither Chrome nor Edge describes how to tell the app on the other end. A WebMCP tool runs inside the user’s session, with the user’s rights, so it doesn’t, by itself, narrow what the agent can reach. Web Bot Auth names the agent, but the draft makes it plain that it doesn’t cover delegation, so it omits the person the agent works for.

The app ends up holding on to pieces of context rather than delivering something actionable.

Now consider that the agents are arriving faster than the standards. Agent-friendly isn’t enough on its own. Every lane built for agents should carry the agent’s identity, a verifiable link to the person it acts for, and a scope narrower than that person’s. Together, those three signals give an application the minimum context it needs to make an authorization decision. Otherwise, a faster lane is just a faster path to the misuse of privilege.

## **What security teams can do before standards catch up**

Waiting for standardization is not an option. You need to [start discovering agentic browsers and extensions as soon as possible](https://www.token.security/book-a-demo?utm_source=thehackernews&utm_medium=3rdparty&utm_campaign=thehackernews&utm_content=nov-11), including the users whose sessions they borrow. And while you can’t tell who clicked, you can choose which clicks need a person by adding a step-up check such as a passkey prompt.

* Inventory browser agents, agentic extensions, and endpoint ag...