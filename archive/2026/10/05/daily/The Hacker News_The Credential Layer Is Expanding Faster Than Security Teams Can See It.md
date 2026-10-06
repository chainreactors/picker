---
title: The Credential Layer Is Expanding Faster Than Security Teams Can See It
url: https://thehackernews.com/2026/10/the-credential-layer-is-expanding.html
source: The Hacker News
date: 2026-10-05
fetch_date: 2026-10-06T08:25:26.336257
---

# The Credential Layer Is Expanding Faster Than Security Teams Can See It

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

# [The Credential Layer Is Expanding Faster Than Security Teams Can See It](https://thehackernews.com/2026/10/the-credential-layer-is-expanding.html)

**The Hacker News**Oct 05, 2026DevSecOps / Supply Chain

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9NofOEElVw39cu_5AzUbEaPI4_wqRGgOfXyk9voMCnZk7q2yJmAePUqEKpis-Rj2APw5W4HYAGLfat5NwcWmSRN0hc6aL4ydrCJH_KiAQPgW7dvr3EwtcG4vlua2VIMkqkE7Nmjgf80-PjoA7nIO0KFSvaux-rlhh6kpKlxdvMorgusBynSBJWTpcZzE/s1700-nu-rw-lo-l85-e365/main.gif)

Every modern enterprise depends on credentials. This is how humans, systems, and now AI, all connect to data, services, and each other securely. GitGuardian helps secure that credential layer through three connected capabilities: Detect, Remediate, and Prevent. The journey starts with detection, because organizations first need to understand what credentials exist, where they live, and what they can access. This is the first of three articles we are releasing that explain the reason behind our mission.

—

Software production is accelerating beyond the growth assumptions that shaped many of today's security controls. GitHub COO Kyle Daigle said the platform had gone from roughly 1 billion commits during all of [2025 to 2.9 billion commits in August 2026,](https://thenewstack.io/github-2-9b-monthly-commits/) an annualized pace of over 14 billion for the 2026 reporting year. GitHub's own engineering team has gone further in its capacity planning, saying it moved from preparing for 10x scale to designing for a future that requires 30x today's scale as agentic development accelerated.

All of this code prodiction means more infrastructure and more secrets. More applications, new types of integrations, automations, and now agents, mean more systems need to authenticate to something else. Credential exposure has already been a problem of increasing scale. [GitGuardian detected 28.65 million new hardcoded secrets in public GitHub commits in 2025](https://www.gitguardian.com/state-of-secrets-sprawl-report-2026), up 34% year over year. Leaked credentials associated with AI services increased 81%.

Security teams need to establish visibility into that expanding credential layer right now.

GitGuardian approaches credential-layer security through three connected stages: Detect, Remediate, and Prevent. Detection comes first because every action that follows depends on knowing which credentials actually exist, where they have spread, and what access they represent.

## **The credential layer has no convenient perimeter**

The credential layer is the collection of credentials connecting people, applications, infrastructure, and services across an enterprise.

Its perimeter follows the credentials themselves.

A developer will create a secret inside a sanctioned cloud account and later that same key, in plaintext, will appear in a repository or in a shared knowledgebase. Other secrets will be stored in an approved vault while a plaintext copies remain on the developer's laptop. More may be created outside security's normal vantage point through a personal project or a newly adopted AI service, especially by an increasingly growing number fo 'citizen developers' who now have access to coding agents.

The result is an attack surface that crosses all technology and ownership boundaries.

The same GitGuardian State of Secrets Sprawl 2026 research we referenced earlier shows how wide this surface has become. Internal repositories were roughly six times more likely than public repositories to contain at least one secret. Around 28% of secrets incidents originated entirely outside source-code repositories in collaboration and productivity systems.

That leaves security teams with a basic discovery challenge. Each scanner, vault, repository, or endpoint can describe the part of the credential layer it sees. The organization still needs a way to understand the combined population.

## **Every discovery source provides a partial picture**

Source control remains essential because hardcoded credentials leave durable evidence.

A credential removed from the current version of a file can remain in Git history. Copies can spread into other branches or repositories. Public exposure can put the value beyond the organization's control, making it extremely challenging for anyone to immediately notice.

Internal repositories reveal another large population. They contain the credentials developers and applications use during normal work, including access to cloud environments and internal services.

Collaboration systems expose a different part of the credential layer. Credentials get pasted into tickets while troubleshooting. They move through chat during handoffs. They can remain searchable long after the work that required them is finished.

## Developer laptops are holding all the credentials

Developers are at the heart of all of this creation, use and placement of secrets. Until recently it was considered normal form to use local local environment files to hold application secrets using command-line tools cache credentials used to reach cloud services. The danger of an unscrubbed local shell history, which can preserve values long after someone has forgotten they were entered, seemed rather low.

Then the attackers shifted. The end of 2025 brought new waves of infostealer attacks like Shai-Hulud and S1ingularity, which turned the developer laptop into a target and an entry point into the supply chain.

Every laptop is part of the credential layer and the secrets they hold need to be mapped.

Repository scanning shows credentials that reached source control. Public monitoring reveals exposures outside corporate repositories. Endpoint discovery identifies secrets that may never have entered a centrally monitored system.

The credential layer only becomes visible when those perspectives are connected.

## **Attackers already search across those boundaries**

Attackers have alrea...