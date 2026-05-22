---
title: When Identity is the Attack Path
url: https://thehackernews.com/2026/05/when-identity-is-attack-path.html
source: The Hacker News
date: 2026-05-21
fetch_date: 2026-05-22T06:08:40.161332
---

# When Identity is the Attack Path

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [When Identity is the Attack Path](https://thehackernews.com/2026/05/when-identity-is-attack-path.html)

**The Hacker News**May 21, 2026Identity Security / AI Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgv9W2lSuCdHjvqeLUN5WtqUOgCwe2FAyP1Y_z4oUr1LgM1MdOE5A83gkzSOfGjIosfdlfB4SuLbeVbydeuParENW4MH2aWYuWqnB-DeOd7gC3RJnp7wFucmuinh9kiMBI99337kQYcBrlIX-WH3u204eu7FTy5b_gpkXC6ZHupWD3P60yFk4-2DUrTuuc/s1700-e365/xmxm.jpg)

Consider a cached access key on a single Windows machine. It got there the way most cached credentials do - a user logged in, and the key stored itself automatically. Standard AWS behavior. No one misconfigured anything or violated a policy. Yet that single key, which was easily accessible to a minor-league attacker, could have opened a path to some 98% of entities in the company's cloud environment - nearly every critical workload the business depended on.

This real-world exposure was caught before an attacker could use it. But the takeaway is clear: *identity itself, and every permission it carries, has become the attack path.*

Your environment runs on identity. Active Directory, cloud identity providers, service accounts, machine identities, and AI agents - all of these carry permissions that span systems and trust boundaries. A single stolen credential hands the attacker a legitimate identity - along with every permission attached to it.

Despite this, most security programs still treat identity as a perimeter control - something to protect through authentication and access policies. Yet the real risk starts inside the front door. Once an attacker has a foothold, identity is what lets them advance, cross boundaries, and reach critical assets. Because identity is not a perimeter - *it's a highway that runs through every layer of your environment.*

In this article, we'll look at how cached credentials, excessive permissions, and forgotten role assignments can turn into attack paths across hybrid environments - and why the tools designed to catch them keep missing.

## **The Attack Path Runs Through Identity**

The cached access key from that opening scenario is just one example of a much larger phenomenon. Across hybrid environments, identity

One Active Directory group membership that no one reviewed gives an attacker on a retail endpoint a direct path to the corporate domain. A developer SSO role provisioned for a cloud migration keeps its permissions long after the project wraps, giving anyone who compromises that identity a four-step route from developer access to production admin. What makes these real-world examples so dangerous is how they connect. That cached credential on the retail endpoint led to an overprivileged role in Active Directory, which led to a cloud workload with an attached admin policy. Together, the links in this type of identity exposure chain form a single attack path - from an initial foothold to a critical asset.

How prevalent is this? Palo Alto found that identity weaknesses played a serious role in [nearly 90% of its 2025 incident response investigations](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report). And given the prevalence of AI agents taking on enterprise workloads, those numbers are likely to go up. SpyCloud's [2026 Identity Exposure Report](https://spycloud.com/newsroom/annual-identity-exposure-report-2026/) flagged non-human identity theft as one of the fastest-growing categories in the criminal underground, with a third of recovered non-human credentials tied to AI tools.

[![](data:image/png;base64...)](https://info.xmcyber.com/fireside-chat-surviving-the-mythos-era-of-continuous-exposure-management?utm_source=hackernews&utm_medium=display)

What happens when one of those non-human identities carries admin-level permissions? Consider a dev team that configures an MCP server with high-level permissions so their AI tooling can operate across systems. The AI agent using the MCP server inherits those privileges as its own identity. A vulnerability in the open-source tooling can easily hand an attacker the permissions that agent holds. From there, the path runs straight into cloud resources, databases, and production infrastructure. The credentials that make this possible are exactly the kind found circulating in criminal marketplaces by the millions.

## **Why the Tools Keep Missing**

Clearly, the threat of identity exposures is not a new one. Yet the identity tools most organizations still rely on were built to solve specific problems in isolation – and in a different threat era.

IGA platforms manage user lifecycle - provisioning, deprovisioning, access reviews, and more. PAM solutions store privileged credentials and monitor sessions. Each of these tools does its job in isolation. But none of them can map how identity exposures chain together across endpoints, Active Directory, and cloud environments into a single exploitable route.

This is why the rates of identity-based incidents keep climbing even as security spending grows. The IBM [X-Force 2026 Threat Intelligence Index](https://www.ibm.com/reports/threat-intelligence) found that stolen or misused credentials accounted for 32% of incidents - the second most common initial access vector. Today’s attackers really don’t need to write malware or exploits, *they can just log in.*

The vast majority of these identity-based exposures are entirely preventable. In fact, Palo Alto found that over [90% of the breaches](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report) its teams investigated in 2025 were enabled by exposures that existing tools should have caught. The organizations had the tools and the staff. Yet the gaps persisted because no single tool had visibility into how identity exposures chained together across environments into attack paths.

## **Closing the Gap**

Until security programs can connect identity, permissions, and access controls into a unified view of ho...