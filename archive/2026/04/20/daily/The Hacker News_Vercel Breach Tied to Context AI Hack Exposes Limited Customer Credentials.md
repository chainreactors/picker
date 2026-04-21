---
title: Vercel Breach Tied to Context AI Hack Exposes Limited Customer Credentials
url: https://thehackernews.com/2026/04/vercel-breach-tied-to-context-ai-hack.html
source: The Hacker News
date: 2026-04-20
fetch_date: 2026-04-21T04:51:46.255833
---

# Vercel Breach Tied to Context AI Hack Exposes Limited Customer Credentials

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

# [Vercel Breach Tied to Context AI Hack Exposes Limited Customer Credentials](https://thehackernews.com/2026/04/vercel-breach-tied-to-context-ai-hack.html)

**Ravie Lakshmanan**Apr 20, 2026Cloud Security / Data Breach

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjcLAcekric_be3bGt2lBu4NxiCcd3FZap2VzD0r9Z8zGegVjwixsexsGVGVmwvLwpaercKHyq9BFA7WV2a_DApLP7qpjg17hE8bu63FHsBoW1wFV0BJmATkuKIM1YU2bf8v9gRPM_tyw8RNINMSXiwzM5jbxjamO8HYm-VsVxgB0lbyRKr4kNuzzRY-JXq/s1700-e365/breach.jpg)

Web infrastructure provider Vercel has disclosed a security breach that allows bad actors to gain unauthorized access to "certain" internal Vercel systems.

The incident stemmed from the compromise of Context.ai, a third-party artificial intelligence (AI) tool, that was used by an employee at the company.

"The attacker used that access to take over the employee's Vercel Google Workspace account, which enabled them to gain access to some Vercel environments and environment variables that were not marked as 'sensitive,'" the company [said](https://vercel.com/kb/bulletin/vercel-april-2026-security-incident) in a bulletin.

Vercel said environment variables marked as "sensitive" are stored in an encrypted manner that prevents them from being read, and that there is currently no evidence suggesting that those values were accessed by the attacker.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d-1)

It described the threat actor behind the incident as "sophisticated" based on their "operational velocity and detailed understanding of Vercel's systems." The company also said it's working with Google-owned Mandiant and other cybersecurity firms, as well as notifying law enforcement and engaging with Context.ai to better understand the full scope of the breach.

A "limited subset" of customers is said to have had their credentials compromised, with Vercel reaching out to them directly and urging them to rotate their credentials with immediate effect. The company is continuing to investigate what data was exfiltrated, and plans to contact customers if further evidence of compromise is discovered.

Vercel is also advising Google Workspace administrators and Google account owners to check for the following application OAuth application:

> 110671459871-30f1spbu0hptbs60cb4vsmv79i7bbvqj.apps.googleusercontent.com

As additional mitigations, the following best practices have been recommended -

* Enable [multi-factor authentication](https://vercel.com/docs/two-factor-authentication).
* Review [activity log](https://vercel.com/activity-log) for signs of suspicious activity.
* Audit and rotate environment variables that contain secrets and are not marked as sensitive. Use [sensitive environment variables](https://vercel.com/docs/environment-variables/sensitive-environment-variables) to ensure secrets are protected.
* Investigate recent deployments for anything unexpected or suspicious. Ensure that [Deployment Protection](https://vercel.com/docs/deployment-protection) is set to Standard at a minimum.
* Rotate [Deployment Protection tokens](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation), if set.

While Vercel has yet to share details about which of its systems were broken into, how many customers were affected, and who may be behind it, a threat actor using the ShinyHunters persona has [claimed](https://x.com/DiffeKey/status/2045813085408051670) responsibility for the hack, selling the stolen data for an asking price of $2 million.

Context.ai has also published a security bulletin in which it disclosed a March 2026 incident that saw it identify and block unauthorized access to its AWS environment. However, it has since emerged that the attacker also likely compromised OAuth tokens for some of its consumer users.

"We also learned that the unauthorized actor appears to have used a compromised OAuth token to access Vercel's Google Workspace," the company [said](https://context.ai/security-update). "Vercel is not a Context customer, but it appears at least one Vercel employee signed up for the AI Office Suite using their Vercel enterprise account and granted 'Allow All' permissions. Vercel's internal OAuth configurations appear to have allowed this action to grant these broad permissions in Vercel's enterprise Google Workspace."

Context.ai said it immediately alerted all impacted customers and provided them with the necessary steps they needed to take. It did not reveal how many customers were affected by the breach.

In a report published today, Hudson Rock has uncovered that a Context.ai employee was compromised with [Lumma Stealer](https://thehackernews.com/2024/06/beware-fake-browser-updates-deliver.html) in February 2026, raising the possibility that the infection may have triggered the "supply chain escalation." The corporate credentials harvested during the attack consisted of Google Workspace credentials, along with keys and logins for Supabase, Datadog, and Authkit.

Also present among the stolen records was the "support@context.ai" account, likely allowing the threat actor to escalate privileges, bypass security controls, and successfully pivot into Vercel's infrastructure. The user is assessed to be a core member of the "context-inc" Vercel team.

"Logs indicate the user was actively searching for and downloading game exploits, specifically Roblox 'auto-farm' scripts and executors," the cybersecurity company [said](https://www.infostealers.com/article/breaking-vercel-breach-linked-to-infostealer-infection-at-context-ai/). "These types of malicious downloads are notorious vectors for Lumma Stealer deployments."

"We've deployed extensive protection measures and monitoring. We've analyzed our supply chain, ensuring Next.js, Turbopack, and our many open source projects remain safe for our community," Vercel CEO Guillermo Rauch [said](https://x.com/rauchg/status/2045995362499076169) in a post on X.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

"In response to this, and to aid in the improvement of all of our customers’ security postures, we've already rolled out new capabilities in the dashboard, including an overview page of environment variables, an...