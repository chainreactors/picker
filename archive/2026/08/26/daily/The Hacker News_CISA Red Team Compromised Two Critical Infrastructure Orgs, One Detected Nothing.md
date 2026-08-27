---
title: CISA Red Team Compromised Two Critical Infrastructure Orgs, One Detected Nothing
url: https://thehackernews.com/2026/08/cisa-red-team-compromised-two-critical.html
source: The Hacker News
date: 2026-08-26
fetch_date: 2026-08-27T12:14:29.635693
---

# CISA Red Team Compromised Two Critical Infrastructure Orgs, One Detected Nothing

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [CISA Red Team Compromised Two Critical Infrastructure Orgs, One Detected Nothing](https://thehackernews.com/2026/08/cisa-red-team-compromised-two-critical.html)

**Swati Khandelwal**Aug 26, 2026Red Teaming / Security Operations

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhW3w9bF-wcalV_4xeymOZiHzRSkeBfz8Vh1B58JkthAgonYo-DGr3kWwNQ8ia760jX1kfC7NTkitD9rWxJNSNzMZWTAVWqrmJQXL7-1rOHbmC7mKSmfArdBAp5s4phuF3SlKr20agmwKrpI56a9SijzuYLnhYlb3R4l7uhb4S0Na0d3_OplvHmbC1EDCk/s1700-e365/cisa-hack.jpg)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has published the results of two red team assessments it conducted simultaneously against two critical infrastructure organizations, using what it described as similar tradecraft while recording sharply different defensive outcomes.

Both organizations were fully compromised at the domain level, and in both, the red team also reached sensitive business systems (SBSs) and cloud resources.

The advisory, tracked as **[AA26-237A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-237a)** and titled "A Tale of Two SOCs," was released on August 25, 2026. CISA identified the first target only as a Government Services and Facilities Sector organization, referred to as **Organization A**, and the second as a Water and Wastewater Systems Sector entity, referred to as **Organization B**.

"CISA conducted two simultaneous red team assessments using similar tradecraft but observed different defensive responses," the agency said in the advisory.

Against Organization A, the red team gained initial access after identifying a web application with default credentials for several built-in accounts, which allowed it to send phishing emails from an internal address and land on four workstations.

It then escalated privileges by abusing a default Machine Account Quota alongside a misconfigured Active Directory Certificate Services (AD CS) template, the same class of certificate-template abuse behind [a recently disclosed domain-takeover exploit](https://thehackernews.com/2026/07/certighost-exploit-lets-low-privileged.html) called **Certighost**.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

The team went on to access three sensitive business systems using credentials stored in cleartext, including decrypted database configuration files and static Amazon Web Services (AWS) access keys set never to expire.

In the cloud, it stole [a Primary Refresh Token](https://thehackernews.com/2026/08/malware-can-abuse-windows-hello-for.html) and abused Entra ID applications carrying elevated permissions to read the security team's email and check whether defenders were aware of the activity.

Organization A did not detect any of it. CISA said thousands of false-positive alerts from normal business operations, many rated at higher severity, obscured the alerts the red team generated, and that the organization ran multiple security operations centers (SOCs) and endpoint tools with no shared visibility between them.

Analysts also lacked escalation procedures and had limited authority to act, and a real alert tied to red team activity on a System Center Configuration Manager (SCCM) server was dismissed as a false positive after defenders could not identify the system's owner.

CISA flagged the following weaknesses as the main enablers of the compromise -

* **Machine Account Quota** left at the default, letting any domain user add machine accounts.
* **AD CS certificate templates** were misconfigured, allowing certificate requests for any user (ESC1).
* **Cleartext credentials** for service and database accounts stored on reachable systems.
* **Static cloud access keys** set never to expire, with no token revocation in place.
* **Over-permissioned applications** in Entra ID able to read mail across all users.

Organization B, running the same style of attack against it, told a different story. Its SOC detected the initial phishing payloads as each executed and isolated the affected workstations within 2 to 20 minutes, cutting off command-and-control (C2) communications before the intrusion could spread.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

Because that foothold was severed, CISA's trusted agents at the organization executed a red team payload on a designated non-privileged host to replicate the access the team would otherwise have obtained, shifting the engagement to an assume-breach model.

From there, the team found the same underlying problems, including cleartext credentials for a domain service account in an SCCM configuration file that carried rights over a domain controller, which it used to run a DCSync attack and retrieve the krbtgt secret.

The team also reached a bastion host in Organization B's operational technology (OT) demilitarized zone, but the host blocked outbound internet access, so no C2 channel was established, and the team did not enter the OT systems themselves.

CISA attributed the gap between the two outcomes to [the people and processes](https://thehackernews.com/2026/05/your-purple-team-isnt-purple-its-just.html) operating the tools, rather than the tools themselves.

"Detection tools are only as effective as the people, processes, and procedures supporting them," the agency said.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#...