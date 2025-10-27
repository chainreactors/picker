---
title: Microsoft SharePoint Connector Flaw Could've Enabled Credential Theft Across Power Platform
url: https://thehackernews.com/2025/02/microsoft-sharepoint-connector-flaw.html
source: The Hacker News
date: 2025-02-05
fetch_date: 2025-10-06T20:47:21.182662
---

# Microsoft SharePoint Connector Flaw Could've Enabled Credential Theft Across Power Platform

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
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
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Microsoft SharePoint Connector Flaw Could've Enabled Credential Theft Across Power Platform](https://thehackernews.com/2025/02/microsoft-sharepoint-connector-flaw.html)

**Feb 04, 2025**Ravie LakshmananVulnerability / SharePoint

[![Microsoft SharePoint Connector](data:image/png;base64... "Microsoft SharePoint Connector")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhY1LiI2LayZbct1jWLQ8Oa4542BGOvGbwaY-mvQvVWSyCSNXkc99J28xRDT_txH-hwGLCgnHMacAmFhyBdAsdfTyFcaI4N1_sHiVC5gVNGZC7W5ckEX60sXXdVpF9dGBUrdUxkeIdXf7KI8jdZfBYsKpPOD-3Y8AFQVkU3vbgEZjy98oXwgzWm3d1Z9FGV/s790-rw-e365/ms.png)

Cybersecurity researchers have disclosed details of a now-patched vulnerability impacting the Microsoft [SharePoint connector](https://learn.microsoft.com/en-us/connectors/sharepointonline/) on [Power Platform](https://learn.microsoft.com/en-us/power-platform/developer/get-started) that, if successfully exploited, could allow threat actors to harvest a user's credentials and stage follow-on attacks.

This could manifest in the form of post-exploitation actions that allow the attacker to send requests to the SharePoint API on behalf of the impersonated user, enabling unauthorized access to sensitive data, Zenity Labs said in a report shared with The Hacker News ahead of publication.

"This vulnerability can be exploited across Power Automate, Power Apps, Copilot Studio, and Copilot 365, which significantly broadens the scope of potential damage," senior security researcher Dmitry Lozovoy [said](https://labs.zenity.io/p/the-power-of-one-ssrf-vulnerability-a-multi-platform-threat).

"It increases the likelihood of a successful attack, allowing hackers to target multiple interconnected services within the Power Platform ecosystem."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Following responsible disclosure in September 2024, Microsoft addressed the security hole, assessed with an "Important" severity assessment, as of December 13. When reached for comment, Redmond confirmed that the issue is resolved.

Microsoft Power Platform is a collection of low-code development tools that allow users to facilitate analytics, process automation, and data-driven productivity applications.

The vulnerability, at its core, is an instance of server-side request forgery ([SSRF](https://owasp.org/www-community/attacks/Server_Side_Request_Forgery)) stemming from the use of the "custom value" functionality within the SharePoint connector that permits an attacker to insert their own URLs as part of a flow.

However, in order for the attack to be successful, the rogue user will need to have an [Environment Maker role](https://learn.microsoft.com/en-us/power-platform/admin/environments-overview) and the [Basic User role](https://learn.microsoft.com/en-us/power-platform/admin/database-security) in Power Platform. This also means that they would need to first gain access to a target organization through other means and acquire these roles.

"With the Environment Maker role, they can create and share malicious resources like apps and flows," Zenity told The Hacker News. "The Basic User role allows them to run apps and interact with resources they own in Power Platform. If the attacker doesn't already have these roles, they would need to gain them first."

In a hypothetical attack scenario, a threat actor could create a flow for a SharePoint action and share it with a low-privileged user (read victim), resulting in a leak of their SharePoint JWT access token.

Armed with this captured token, the attacker could send requests outside of the Power Platform on behalf of the user to whom access was granted to.

That's not all. The vulnerability could be extended further to other services like Power Apps and Copilot Studio by creating a seemingly benign Canvas app or a Copilot agent to harvest a user's token, and escalate access further.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"You can take this even further by embedding the Canvas app into a Teams channel, for example," Zenity noted. "Once users interact with the app in Teams, you can harvest their tokens just as easily, expanding your reach across the organization and making the attack even more widespread."

"The main takeaway is that the interconnected nature of Power Platform services can result in serious security risks, especially given the widespread use of the SharePoint connector, which is where a lot of sensitive corporate data is housed, and it can be complicated to ensure proper access rights are maintained throughout various environments."

The development comes as Binary Security [detailed](https://binarysecurity.no/posts/2025/01/finding-ssrfs-in-devops) three SSRF vulnerabilities in Azure DevOps that could have been abused to communicate with the [metadata API endpoints](https://cybercx.com.au/blog/azure-ssrf-metadata/), thereby permitting an attacker to glean information about the machine's configuration.

*(The story was updated after publication to include a response from Microsoft.)*

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
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data...