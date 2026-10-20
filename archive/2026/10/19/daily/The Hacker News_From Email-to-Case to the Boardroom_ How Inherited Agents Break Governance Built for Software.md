---
title: From Email-to-Case to the Boardroom: How Inherited Agents Break Governance Built for Software
url: https://thehackernews.com/2026/10/from-email-to-case-to-boardroom-how.html
source: The Hacker News
date: 2026-10-19
fetch_date: 2026-10-20T06:53:58.633954
---

# From Email-to-Case to the Boardroom: How Inherited Agents Break Governance Built for Software

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

# [From Email-to-Case to the Boardroom: How Inherited Agents Break Governance Built for Software](https://thehackernews.com/2026/10/from-email-to-case-to-boardroom-how.html)

**The Hacker News**Oct 19, 2026Artificial Intelligence / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1uAZRypeHl_8TjAU-3mwmvjdbCH0SZJwZBZOoEXcehaQfod9rpBvAl72JCjV8xF2KF4VbSVzWezAmkXjmbaxdIkK854Pa-yV4nkkRNe-l82mPM_VW1fLSE5Ib-RhyphenhypheneGga3KZ_9wQu76clTABJwGp_3N_M-6QBZMXFSISC56JWHVHpylO-uTenNO3kRlg/s1700-nu-rw-lo-l85-e365/reco.gif)

In Salesforce Agentforce, the recommended way to make an agent respond to events is a Flow: a record is created or a case is updated, and the Flow passes data into the agent's prompt. Separately, Email-to-Case and Web-to-Case turn inbound customer messages into case records; it is how airlines and hotels run support intake. Both are standard, documented, as-designed features. Chained together, they produce this path:

**public internet → email → case record → agent prompt → agent action → case comment → outbound reply**

An unauthenticated outsider now has a route into an internal agent's instructions, and the agent's reply leaves through the same door. Nothing was misconfigured. The finding, documented by researchers in August 2026, is a clean example of how agents that arrive inside existing platforms fail: through the application around them, not the model inside them.

### **The risk is in the application, and the application is the thing nobody re-reviewed**

Which intake features are enabled, which triggers fire, which objects are exposed to guest users, which automation passes untrusted data where, and which model version the agent is quietly calling underneath: these are the variables that decide whether the Agentforce chain is a support-queue nuisance or a data exposure. A vendor risk review performed once at procurement sees none of them, because the agent did not exist at procurement. A prompt filter watching the agent's inputs does not know that a particular input originated from a stranger, because prompt filters do not understand Email-to-Case.

[Securing an inherited agent](https://www.reco.ai/agent-ecosystem-security/where-ai-agents-come-from?utm_source=hackernews) therefore means understanding its host application at the depth its own admins do. That depth is the one thing a questionnaire and a scanner both lack. The City-Forum campaign, an active worldwide data-theft operation against Salesforce and ServiceNow instances running since March 2025, was found in exactly this territory: the gap between platform features and the configurations enterprises actually run.

### **Builders are multiplying, and some of them are agents**

The platforms have made agent creation as accessible as making a slide deck. Marketing operations builds an agent to pull pipeline reports. Finance builds one to reconcile invoices. Each rides its creator's permissions, because that is what makes it useful. Shadow AI was an employee pasting data into a chatbot. Shadow agents are that employee's access, running unattended, multiplied across everything they were ever granted.

Increasingly, agents also build agents. A coding agent tagged into a chat channel can scaffold and deploy another agent as easily as it opens a pull request; an orchestration platform spins up sub-agents to divide a task, each with its own connections and none with its own review. Any governance model that assumes a human requested each agent is quietly obsolete.

### **Why governance keeps producing a document**

Ask a large enterprise about [agent governance](https://www.reco.ai/agent-ecosystem-security/ai-agent-governance?utm_source=hackernews) and the answer is usually a document: an acceptable-use policy, a monthly committee, a set of principles nobody disputes and nothing enforces. Ask the operational question, how many agents are running right now, what can they reach, and who owns each one, and the document does not know.

The OWASP Agentic Skills Top 10 now describes the sharpest version of this gap under its "No Governance" category: a skill deployed and managed inside a third-party platform is unreachable by external scanners (OWASP Agentic Skills Top 10 whitepaper, ast10-top10-whitepaper-2, published at owasp.github.io). The tools an enterprise points at the problem from outside cannot see inside the venues where most agents live. Governance fails most often because the rules get written before the security team can see the things the rules apply to.

### **The stack, bottom-up, with a test for each layer**

The working order is bottom-up, and each layer is the precondition for the one above it. A practical way to check whether a program is real is to apply an operational test at each level.

|  |  |  |
| --- | --- | --- |
| **Layer** | **What it has to produce** | **The operational test** |
| **Discovery** | A continuously refreshed population across app configs, OAuth grants, network, endpoint, email metadata, and browser | Is the discovered count several multiples of the list IT keeps? If not, discovery isn't reaching where agents live. |
| **Posture** | Every platform's agent-relevant settings, measured against how they should be configured | Can the team list the intake features and guest-user exposures wired to agent triggers on its top three platforms? |
| **Identity and ownership** | An identity and a named owner per agent, with a lifecycle | Pick an agent at random. Does a human raise a hand within a day when asked "whose is this?" |
| **Usage** | Who is building what, through which surface, with what data | Is there a sanctioned path that ships a business team's agent with secure defaults, or only a block? |
| **Agent controls** | Least privilege against observed need, approval and quarantine for new agents, risk tiering that reflects each agent's full context | Does the same finding on a sandboxed dev agent and...