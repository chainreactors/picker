---
title: The Ongoing Fallout from a Breach at AI Chatbot Maker Salesloft
url: https://krebsonsecurity.com/2025/09/the-ongoing-fallout-from-a-breach-at-ai-chatbot-maker-salesloft/
source: Krebs on Security
date: 2025-09-02
fetch_date: 2025-10-02T19:32:11.702779
---

# The Ongoing Fallout from a Breach at AI Chatbot Maker Salesloft

Advertisement

[![](/b-sysdig/1.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000460_1240x110)

Advertisement

[![](/b-gartner/4.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# The Ongoing Fallout from a Breach at AI Chatbot Maker Salesloft

September 1, 2025

[33 Comments](https://krebsonsecurity.com/2025/09/the-ongoing-fallout-from-a-breach-at-ai-chatbot-maker-salesloft/#comments)

The recent mass-theft of authentication tokens from **Salesloft**, whose AI chatbot is used by a broad swath of corporate America to convert customer interaction into **Salesforce** leads, has left many companies racing to invalidate the stolen credentials before hackers can exploit them. Now **Google** warns the breach goes far beyond access to Salesforce data, noting the hackers responsible also stole valid authentication tokens for hundreds of online services that customers can integrate with Salesloft, including Slack, Google Workspace, Amazon S3, Microsoft Azure, and OpenAI.

![](https://krebsonsecurity.com/wp-content/uploads/2025/09/salesloft-customers.png)

Salesloft [disclosed on August 20](https://trust.salesloft.com/?uid=Drift%2FSalesforce+Security+Notification) that, “Today, we detected a security issue in the **Drift** application,” referring to the technology that powers an AI chatbot used by so many corporate websites. The alert urged customers to re-authenticate the connection between the Drift and Salesforce apps to invalidate their existing authentication tokens, but it said nothing then to indicate those tokens had already been stolen.

On August 26, the **Google Threat Intelligence Group** (GTIG) [warned](https://cloud.google.com/blog/topics/threat-intelligence/data-theft-salesforce-instances-via-salesloft-drift) that unidentified hackers tracked as **UNC6395** used the access tokens stolen from Salesloft to siphon large amounts of data from numerous corporate Salesforce instances. Google said the data theft began as early as Aug. 8, 2025 and lasted through at least Aug. 18, 2025, and that the incident did not involve any vulnerability in the Salesforce platform.

Google said the attackers have been sifting through the massive data haul for credential materials such as AWS keys, VPN credentials, and credentials to the cloud storage provider Snowflake.

“If successful, the right credentials could allow them to further compromise victim and client environments, as well as pivot to the victim’s clients or partner environments,” the GTIG report stated.

The GTIG updated its advisory on August 28 to acknowledge the attackers used the stolen tokens to access email from “a very small number of Google Workspace accounts” that were specially configured to integrate with Salesloft. More importantly, it warned organizations to immediately invalidate all tokens stored in or connected to their Salesloft integrations — regardless of the third-party service in question.

“Given GTIG’s observations of data exfiltration associated with the campaign, organizations using Salesloft Drift to integrate with third-party platforms (including but not limited to Salesforce) should consider their data compromised and are urged to take immediate remediation steps,” Google advised.

On August 28, Salesforce blocked Drift from integrating with its platform, and with its productivity platforms Slack and Pardot.

The Salesloft incident comes on the heels of a broad social engineering campaign that used voice phishing to trick targets into connecting a malicious app to their organization’s Salesforce portal. That campaign led to data breaches and extortion attacks affecting a number of companies including Adidas, Allianz Life and Qantas.

On August 5, Google [disclosed](https://cloud.google.com/blog/topics/threat-intelligence/voice-phishing-data-extortion) that one of its corporate Salesforce instances was compromised by the attackers, which the GTIG has dubbed **UNC6040** (“UNC” stands for “uncategorized threat group”). Google said the extortionists consistently claimed to be the threat group **ShinyHunters**, and that the group appeared to be preparing to escalate its extortion attacks by launching a data leak site.

ShinyHunters is an amorphous threat group known for using social engineering to break into cloud platforms and third-party IT providers, and for posting dozens of stolen databases to cybercrime communities like the now-defunct Breachforums.

The ShinyHunters brand dates back to 2020, and the group has been credited with or taken responsibility for [dozens of data leaks](https://en.wikipedia.org/wiki/ShinyHunters) that exposed hundreds of millions of breached records. The group’s member roster is thought to be somewhat fluid, drawing mainly from active denizens of the **Com**, a mostly English-language cybercrime community scattered across an ocean of Telegram and Discord servers.

Recorded Future’s **Alan Liska** [told](https://www.bleepingcomputer.com/news/security/shinyhunters-behind-salesforce-data-theft-attacks-at-qantas-allianz-life-and-lvmh/) **Bleeping Computer** that the overlap in the “tools, techniques and procedures” used by ShinyHunters and the [Scattered Spider extortion group](https://krebsonsecurity.com/tag/scattered-spider/) likely indicate some crossover between the two groups.

To muddy the waters even further, on August 28 a Telegram channel that now has nearly 40,000 subscribers was launched under the intentionally confusing banner “**Scattered LAPSUS$ Hunters 4.0**,” wherein participants have repeatedly claimed responsibility for the Salesloft hack without actually sharing any details to prove their claims.

The Telegram group has been trying to attract media attention by threatening security researchers at Google and other firms. It also is using the channel’s sudden popularity to promote a new cybercrime forum called “Breachstars,” which they claim will soon host data stolen from victim companies who refuse to negotiate a ransom payment.

![](https://krebsonsecurity.com/wp-content/uploads/2025/09/scatteredlapsusshunters.png)

But **Austin Larsen**, a principal threat analyst at Google’s threat intelligence group, said there is no compelling evidence to attribute the Salesloft activity to ShinyHunters or to other known groups at this time.

“Their understanding of the incident seems to come from public reporting alone,” Larsen told KrebsOnSecurity, referring to the most active participants in the Scattered LAPSUS$ Hunters 4.0 Telegram channel.

**Joshua Wright**, a senior technical director at **Counter Hack,** is credited with coining the term “authorization sprawl” to describe one key reason that social engineering attacks from groups like Scattered Spider and ShinyHunters so often succeed: They abuse legitimate user access tokens to move seamlessly between on-premises and cloud systems.

Wright said this type of attack chain often goes undetected because the attacker sticks to the resources and access already allocated to the user.

“Instead of the conventional chain of initial access, privilege escalation and endpoint bypass, these threat actors are using centralized identity platforms that offer single sign-on (SSO) and integrated authentication and authorization schemes,” Wright [wrote in a June 2025 column](https://www.techtarget.com/searchsecurity/post/Authorization-sprawl-Attacking-modern-access-models). “Rather than creating custo...