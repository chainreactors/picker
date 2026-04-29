---
title: Microsoft Patches Entra ID Role Flaw That Enabled Service Principal Takeover
url: https://thehackernews.com/2026/04/microsoft-patches-entra-id-role-flaw.html
source: The Hacker News
date: 2026-04-28
fetch_date: 2026-04-29T05:13:06.073239
---

# Microsoft Patches Entra ID Role Flaw That Enabled Service Principal Takeover

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

# [Microsoft Patches Entra ID Role Flaw That Enabled Service Principal Takeover](https://thehackernews.com/2026/04/microsoft-patches-entra-id-role-flaw.html)

**Ravie Lakshmanan**Apr 28, 2026Vulnerability / Identity Management

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4YomH2AGnUSAePfyyvEMXCbULukirvclzEJ6gnsm30Y2PApuarWfCLpKrBng3qYhhINWPwn99rVtdqKcEtbnVR9jkXkpBY-vDByDzMmZgLPPPrqyodmgqBCfR3ojF1tbyaFHQxIdr8voZgDugagnBymAchRR99uUm_0btEdWYeir8B6njw6Q1lPTcugcB/s1700-e365/azure.jpg)

An administrative role meant for artificial intelligence (AI) agents within Microsoft Entra ID could enable privilege escalation and identity takeover attacks, according to new findings from **Silverfort**.

[Agent ID Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference) is a privileged built-in role introduced by Microsoft as part of its [agent identity platform](https://learn.microsoft.com/en-us/entra/agent-id/what-is-agent-id-platform) to handle all aspects of an AI agent's identity lifecycle operations in a tenant. The platform enables AI agents to authenticate securely and access necessary resources, as well as discover other agents.

However, the shortcoming discovered by the identity security platform meant that users assigned the Agent ID Administrator role could take over arbitrary [service principals](https://learn.microsoft.com/en-us/entra/identity-platform/app-objects-and-service-principals), including those beyond agent-related identities, by becoming an owner and then add their own credentials to authenticate as that principal.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d-1)

"That's full service principal takeover," security researcher Noa Ariel [said](https://www.silverfort.com/blog/agent-id-administrator-scope-overreach-service-principal-takeover-in-entra-id/). "In tenants where high-privileged service principals exist, it becomes a privilege escalation path."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWveFhhMQcTBkaG4hCYtXTMOCBC2qi3l0SWAP8WbTO3ocDNHG_9crspjYhrKXTlE00tC1ZBNsrlax1mqwBtg5j3lYS4xD80DX2woqHdsnF0EC56kSF1Tv4rioBESstJ9tXLpd5owzSLQFtVwjyaJGD8PmM_FE6LW4aInJUL5it-jgiYczaqFL0-nmIPWGY/s1700-e365/flow.jpg)

This ownership of a service principal effectively opens the door to an attacker to operate within the scope of its existing permissions. If the targeted service principal holds elevated permissions – particularly privileged directory roles and high-impact Graph app permissions – it can give an attacker broader control over the tenant.

Following responsible disclosure on March 1, 2026, Microsoft rolled out a patch across all cloud environments to remediate the scope overreach on April 9. Following the fix, any attempt to assign ownership over non-agent service principals using the Agent ID Administrator role is now blocked, and leads to a "Forbidden" error message being displayed.

Silverfort noted that the architectural issue highlights the need for validating how roles are scoped and permissions are applied, especially when it comes to shared identity components and new identity types are built on top of the foundations of existing primitives.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

To mitigate the threat posed by this risk, organizations are advised to monitor sensitive role usage, particularly those related to service principal ownership or credential changes, track service principal ownership changes, secure privileged service principals, and audit credential creation on service principals.

"Agent identities are part of the broader shift toward non-human identities, built for the age of AI agents," Ariel noted. "When role permissions are applied on top of shared foundations without strict scoping, access can extend beyond what was originally intended. In this case, that gap led to broader access, especially when privileged service principals were involved."

"Additionally, the overall risk is influenced by tenant posture, particularly around privileged service principals, where ownership abuse remains a well-known and impactful attack path."

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

[Access Control](https://thehackernews.com/search/label/Access%20Control), [AI Agent](https://thehackernews.com/search/label/AI%20Agent), [Cloud security](https://thehackernews.com/search/label/Cloud%20security), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Identity Management](https://thehackernews.com/search/label/Identity%20Management), [Microsoft Entra ID](https://thehackernews.com/search/label/Microsoft%20Entra%20ID), [Patch Management](https://thehackernews.com/search/label/Patch%20Management), [privilege escalation](https://thehackernews.com/search/label/privilege%20escalation), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

Trending News

[![108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000 Users](data:image/svg+xml;base64... "108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000 Users")

108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000 Users](https://thehackernews.com/2026/04/108-malicious-chrome-extensions-steal.html)

[![Mirax Android RAT Turns Devices into SOCKS5 Proxies, Reaching 220,000 via Meta Ads](data:image/svg+xml;b...