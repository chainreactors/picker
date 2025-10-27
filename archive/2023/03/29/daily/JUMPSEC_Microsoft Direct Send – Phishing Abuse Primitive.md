---
title: Microsoft Direct Send – Phishing Abuse Primitive
url: https://www.jumpsec.com/guides/microsoft-direct-send-phishing-abuse-primitive/
source: JUMPSEC
date: 2023-03-29
fetch_date: 2025-10-04T11:03:08.899113
---

# Microsoft Direct Send – Phishing Abuse Primitive

[Skip to main content](#ajax-content-wrap)

* [twitter](https://twitter.com/JUMPSEC)
* [linkedin](https://www.linkedin.com/company/jumpsec/)
* [youtube](https://www.youtube.com/channel/UCpwVvJpDfFzBClzGhLUAZBw)

[New Blog - Building resilience against modern cyber threats -Read here](https://www.jumpsec.com/guides/building-resilience-against-modern-cyber-threats/)

* [About](https://www.jumpsec.com/about/ "About")
* [Careers](https://www.jumpsec.com/careers/ "Careers")
* [Accreditations](https://www.jumpsec.com/accreditations-awards/ "Accreditations")

Hit enter to search or ESC to close

Close Search

[![JUMPSEC](https://www.jumpsec.com/wp-content/uploads/2022/08/JUMPSEC-2021-Retina.png)![JUMPSEC](https://www.jumpsec.com/wp-content/uploads/2022/08/jumpsec-white-logo.png)](https://www.jumpsec.com)

[search](#searchbox)

[Menu](#slide-out-widget-area)

* [Home](https://www.jumpsec.com/ "Home")
* [Solutions](https://www.jumpsec.com/solutions/ "Solutions")
  + [Offensive](/solutions/#off "Offensive")
    - [Adversary Simulation Services](https://www.jumpsec.com/red-teaming-advanced-simulated-attack/ "Adversary Simulation Services")
    - [Purple Teaming](https://www.jumpsec.com/purple-teaming/ "Purple Teaming")
    - [Red Teaming](https://www.jumpsec.com/red-teaming/ "Red Teaming")
    - [Penetration Testing Services](https://www.jumpsec.com/penetration-testing/ "Penetration Testing Services")
  + [Defensive](/solutions/#def "Defensive")
    - [Continuous Attack Surface Management (CASM)](https://www.jumpsec.com/continuous-attack-surface-management-casm/ "Continuous Attack Surface Management (CASM)")
    - [Attack Path Mapping](https://www.jumpsec.com/attack-path-mapping/ "Attack Path Mapping")
    - [Incident Response Services](https://www.jumpsec.com/incident-response/ "Incident Response Services")
    - [Cyber Incident Exercising](https://www.jumpsec.com/cyber-incident-exercising/ "Cyber Incident Exercising")
    - [Cyber Incident Readiness](https://www.jumpsec.com/cyber-incident-readiness/ "Cyber Incident Readiness")
    - [Managed Extended Detection and Response (MXDR)](https://www.jumpsec.com/managed-detection-and-response-mdr/ "Managed Extended Detection and Response (MXDR)")
  + [Strategic](/solutions/#str "Strategic")
    - [Cyber Maturity Development](https://www.jumpsec.com/cyber-maturity-development/ "Cyber Maturity Development")
    - [Cyber Security Audit](https://www.jumpsec.com/security-audit-compliance/ "Cyber Security Audit")
  + [Casm](/continuous-attack-surface-management-casm/ "Casm")
* Resources
  + –
    - [InsightsUnderstand the threats you face and threats in the industry](https://www.jumpsec.com/insights/)
    - [Threat Intelligence HubHelping you to understand the threats you face](https://www.jumpsec.com/threat-intelligence-hub/)
    - [Case StudiesChallenges we have helped to resolve for leading organisations](https://www.jumpsec.com/case-studies/)
  + –
    - [VideosHave a look at our video guides to the cybersecurity sector](https://www.jumpsec.com/videos/)
    - [Ebooks and BrochuresWhat our experts have written about keeping your network safe](https://www.jumpsec.com/ebooks-and-brochures/)
    - [Jargon BustersNavigate the complex world of cyber security](https://www.jumpsec.com/jargon-busters/)
  + [–](https://www.jumpsec.com/new-events/)
    - [EventsWhat JUMPSEC has coming up and our previous events](https://www.jumpsec.com/new-events/)
    - [Webinars and PodcastsWatch our previous live events from industry professionals](https://www.jumpsec.com/webinars-and-podcasts/)
  + [Newest Blog PostUK Ransomware Payment Ban Implications](https://www.jumpsec.com/guides/uk-ransomware-payment-ban-implications-what-it-means-for-public-and-private-sector-cybersecurity/)
* [About](https://www.jumpsec.com/about/ "About")
  + [About Us](https://www.jumpsec.com/about/ "About Us")
  + [Leadership Team](https://www.jumpsec.com/leadership-team/ "Leadership Team")
  + [Accreditations & Awards](https://www.jumpsec.com/accreditations-awards/ "Accreditations & Awards")
  + [Careers](https://www.jumpsec.com/careers/ "Careers")
  + [News & Press Releases](https://www.jumpsec.com/news/ "News & Press Releases")
* [Labs](https://labs.jumpsec.com/ "Labs")
* [Contact](https://www.jumpsec.com/contact/ "Contact")

* [search](#searchbox)

![Microsoft Direct Send – Phishing Abuse Primitive](https://www.jumpsec.com/wp-content/uploads/2023/10/how-to-prepare-copy.webp)

# Microsoft Direct Send – Phishing Abuse Primitive

By [Miles](https://www.jumpsec.com/guides/author/miles/ "Posts by Miles")March 28, 2023July 22nd, 2025[Consultant Blog](https://www.jumpsec.com/guides/category/consultant-blog/), [Insights](https://www.jumpsec.com/guides/category/insights/)3 min read

[No Comments](https://www.jumpsec.com/guides/microsoft-direct-send-phishing-abuse-primitive/#respond)

Share

ShareShareSharePin

This vector abuses Microsoft Direct Send service in order to propagate phishing emails from an external sender to an internal user, whilst spoofing the properties of a valid internal user. This “feature” has existed since before 2016. However, threat intelligence available to JUMPSEC has only observed it being abused recently.

### Abuse Primitives

As part of the research conducted by JUMPSEC and other organisations, this “feature” can be abused to spoof emails inside an organisation externally. This means that without needing access to the network, an attacker can send emails between internal users by spoofing the sender address and they will appear to be from the spoofed user. The caveats to doing so require the organisation to be using an external mail proxy provider such as Mimecast.

Organisations that consume Microsoft 365 for Exchange Online service will automatically be registered with an MX record (**Company-tld**.mail.protection.outlook.com). This server can be used as a SMTP server to send mail inside an organisation to valid users.

### Am I Affected?

As part of an ongoing effort, JUMPSEC has built the following service that allows organisations to check whether they are affected and if their implemented controls will fix the issue:

Visiting the following URL and following the instructions.

[**https://ds.jumpsec.net**](https://ds.jumpsec.net)

![phishing abuse](https://www.jumpsec.com/wp-content/uploads/2023/03/Screenshot-2023-03-28-at-2.35.14-pm.png)

### Impact

The technique grants the ability to send emails as trusted users within an organisation. Additionally, spoofing / controlling the sender address can lead to more sophisticated phishing attacks. The population of the users properties within M365 including photos and Teams information increases the quality of the phish by luring victims into believing this is a genuine email / user from within the organisation. Generally speaking, without more granular preventative controls, this could lead to compromise of accounts, assets and resources.

JUMPSEC expects threat groups to be using this technique to target affected organisations. As affected organisations can be determined via a simple dig issuance, it’s trivial to determine likely affected organisations. Additionally, users of said organisations can be enumerated via previous breaches and additionally by performing targeted open source intelligence gathering.

### Mitigations

**Direct Send cannot be disabled.** The best mitigatory steps if you are using an external mail proxy, would be to force all internal and external mail flows through that mail gateway proxy. Emails should not be allowed into the organisation from untrusted sources.

Generally, enforcing “SPF hardfail” within Exchange Online Protection (EOP) will add an extra layer of protection and should be enabled where possible.

Additional Controls can be enabled via Exchange Admin Center using connector rules, these rules allow bespoke configuration for when you need to route mail differently. The Exchange Admin Center connector rules can be configured to force all incoming mai...