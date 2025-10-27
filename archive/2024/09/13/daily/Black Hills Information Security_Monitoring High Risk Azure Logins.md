---
title: Monitoring High Risk Azure Logins
url: https://www.blackhillsinfosec.com/monitoring-high-risk-azure-logins/
source: Black Hills Information Security
date: 2024-09-13
fetch_date: 2025-10-06T18:27:43.209228
---

# Monitoring High Risk Azure Logins

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

12
Sep
2024

[Blue Team](https://www.blackhillsinfosec.com/category/blue-team/), [David Perez](https://www.blackhillsinfosec.com/category/author/david-perez/), [Incident Response](https://www.blackhillsinfosec.com/category/blue-team/incident-response/), [Informational](https://www.blackhillsinfosec.com/category/informational/)
[Azure](https://www.blackhillsinfosec.com/tag/azure/), [Entra ID](https://www.blackhillsinfosec.com/tag/entra-id/), [SIEM](https://www.blackhillsinfosec.com/tag/siem/), [SOC](https://www.blackhillsinfosec.com/tag/soc/)

# [Monitoring High Risk Azure Logins](https://www.blackhillsinfosec.com/monitoring-high-risk-azure-logins/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/08/DPerez-150x150.png)

| [David Perez](https://www.blackhillsinfosec.com/team/cameron-cartier/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/08/BLOG_chalkboard_000687.png)

Recently in the SOC, we were notified by a partner that they had a potential business email compromise, or BEC. We commonly catch these by identifying suspicious email forwarding rules, utilizing anomaly detection services, or by reports from our partners, as we did in this scenario. As always, the earlier we can catch these events in the attack chain, the better. This led us to begin investigating high risk logins identified by Azure AD Identity Protection, or what is now known as Entra Identity Protection.

Entra ID protection categorizes risk levels as low, medium, or high. Entra ID also attaches the atRisk label if a potential threat actor has gained access to a user’s account. Determination of risk level is based on the confidence in the signals by Entra ID and utilizes Real-time and Offline [detection techniques](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks) to assess these values. Organizations not utilizing an [Azure AD P2 license](https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection#license-requirements) will have limited detection capabilities using this service.

[Investigating](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk) these events is straight-forward once you understand what information Entra ID is using to make these detections. The most useful attributes being *IP address*, *operating system*, *ASN*, and *country of origin*. Once an atRisk login has been identified, I start my investigation by querying the related user account and comparing the surrounding log’s login information to see what normal activity looks like for the user.

The detections most closely correlated with multi-factor authentication events were the most useful. Logically speaking, if an MFA request has been sent to a device, then the user account’s password has very likely been compromised. I’ve included this as part of the sigma rule at the bottom of the blog.

The most common false positives I have seen so far are from users signing in from mobile devices or from different IP addresses due to them being on travel. True positives seem to stick out like a sore thumb, whereas a user is most often seen signing in from a Windows machine, and then suddenly they are seen using a Mac in a different country.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/09/2024-07-31_22-11.png)

**Azure atRisk Sign-in Events**

In summary, monitoring these alerts more closely has helped us to catch more of these events earlier in the attack chain. I hope this helps you as well.

### **Sigma Rule:**

```
title: High Risk Azure Login Requiring MFA
status: tested
description: This detection leverages Azure AD’s built-in service, Azure AD Identity protection, to detect anomalous high risk sign ins to cloud accounts requiring MFA approval. This is an indication that a user’s password has been compromised.
references:
author: David Perez
date: 2024/07/16
tags:
	- attack.t1528
	- attack.credential_access
logsource:
product: azure
	service: signinlogs
detection:
	selection:
risk_state : ‘atRisk’
authentication_requirement : ‘multiFactorAuthentication’
risk1:
risk_level_aggregated : ‘High’
risk2:
risk_level_during_signin : ‘High’
	condition: selection and 1 of risk*
falsepositives:
	- Users known to be on travel(most common).
	- Users authenticating with new devices in their possession (i.e. mobile device).
```

### **Entra Risk Detections:**

The time difference between a suspicious sign-in event versus a detection in logs/reports can range significantly — for real-time detections, it is 5-10 minutes, and up to 48 hours for offline detections.

|  |  |  |  |
| --- | --- | --- | --- |
| **Risk detection** | **Detection type** | **Type** | **riskEventType** |...