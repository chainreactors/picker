---
title: What Security Teams Can Do To Tame Wild Code
url: https://thehackernews.com/2026/10/what-security-teams-can-do-to-tame-wild.html
source: The Hacker News
date: 2026-10-20
fetch_date: 2026-10-21T06:51:12.567034
---

# What Security Teams Can Do To Tame Wild Code

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

# [What Security Teams Can Do To Tame Wild Code](https://thehackernews.com/2026/10/what-security-teams-can-do-to-tame-wild.html)

**The Hacker News**Oct 20, 2026Artificial Intelligence / Runtime Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi7Q3156iY5WJRnphGSZ5PuIiMopF0sG7ku3FR-WROda9fE4jCSIOQpClG1HOBRCvbuqDyLHgsC0N3UFjowgnXzZN4T1mDpkQbTz2gX7z4NRZsfoEpimVlZ7hevcXmeTfpOt1iFrHqvLXubegNIRz15gjlQNHIBBYzQVAmy8MNAGiZs6OXIEuWNntLwTlI/s1700-nu-rw-lo-l85-e365/tines-main.jpg)

A sales manager builds an AI-assisted workflow to route leads. It connects to customer records, summarizes inbound requests, and posts updates to a shared channel. The workflow saves time, reduces manual work, and soon becomes part of the team’s daily routine. Across the same organization, employees are building useful apps, agents, and automations faster than existing processes can support them.

If you work in security, that success introduces a new set of questions. Whose credentials does the workflow use? Which records can it access? Who can see its output? If it starts exposing information it shouldn’t, can you trace what happened and stop further access?

Wild code takes root when useful builds spread faster than the processes for owning, securing, and maintaining them. It isn’t simply another name for unapproved software. Employees are creating new capabilities, not just adopting existing products. A small experiment can become an operational dependency before security knows it exists.

The risk goes beyond vulnerabilities in generated code. Even code that works as intended can operate with too much access or expose data to the wrong audience:

* **Excessive permissions.** A workflow needs a small set of records but runs with credentials that can read or modify far more.
* **Sensitive data exposure.** An employee connects an agent to information it doesn’t need, or makes its output available too broadly. Sensitive information can also end up in model requests or logs.
* **Unintended actions.** An agent can change records or permissions without an approval boundary appropriate to the action.
* **Orphaned access.** A useful workflow keeps running after its creator changes roles or leaves, with no clear owner reviewing its permissions.
* **Investigation gaps**. When something goes wrong, security can’t readily establish which identity ran the workflow, what it accessed, or what changed.

Employee education, sandboxes, and AI steering committees are a good start, but they aren’t enough to control wild code on their own. A more sustainable approach builds controls into the environment itself: what employees can connect to, what their apps and agents can do, and how that work is monitored once it’s running.

## Why the usual fixes fall short

Education, sandboxes, and steering committees all have a role. The mistake is expecting them to govern software they may never encounter, or control what happens after it starts running. A policy describes what should happen. Security also needs controls that constrain what can happen, evidence of what did happen, and a way to intervene.

### 1. Education explains good practice, but can’t enforce it

An AI policy can explain what’s allowed. Training can introduce good practices. Neither guarantees that someone building a reporting workflow will recognize the moment they cross into handling sensitive data or operating production software.

As AI brings more employees into building software, organizations have an opportunity to make practices like least privilege, secrets management, and separating test environments from production more accessible. Policies can set expectations, but employees also need practical guidance and built-in safeguards to apply them in everyday work.

Even employees who recognize a risk still face deadlines and pressure to move faster. If the approved route is slow or confusing, knowing the rules doesn’t make following them easier.

Education helps people make better decisions. It shouldn’t be the only thing preventing an unsafe connection or an unauthorized action.

### 2. Sandboxes protect experiments, not their entire future

An isolated environment is useful for testing prompts, models, and generated code. But a prototype’s value often depends on eventually reaching real business systems and data.

Once a prototype connects to live business systems, it needs controls that extend beyond the test environment. Permissions, monitoring, and change reviews have to remain in place throughout its working life, not just during the experiment. A successful test doesn’t establish which data the production workflow should access or which actions it should be allowed to take.

As Brad Rumph, field CTO at Tines, puts it: “Sandboxes solve the design problem and leave the runtime problem alone.”

A successful experiment still needs a governed path into operation. Without that path, isolation postpones the hard questions rather than resolving them.

### 3. Committees can’t review what they can’t see

Steering committees can set direction, establish accountability, and make decisions about high-risk use cases. But their review cycles don’t always match the speed at which employees can create and deploy software.

A committee might prohibit one risky practice while employees discover another way to achieve the same result. Oversight can also concentrate on engineering, where established controls already exist, while overlooking builds in finance, HR, or operations.

The limitation isn’t the quality of the committee. It’s a model that depends on each build becoming visible before it becomes useful. An approval process can’t be the only way security discovers new paths to sensitive data and privileged actions.

## Put security controls where the work happens

The alternative is to build controls into the environment employees use to create, run, and maintain their work.

Rather than asking everyone...