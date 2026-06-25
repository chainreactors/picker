---
title: Insufficient Egress Filtering: How Weak Outbound Controls Enable Attacks
url: https://www.blackhillsinfosec.com/insufficient-egress-filtering/
source: Black Hills Information Security, Inc.
date: 2026-06-24
fetch_date: 2026-06-25T06:09:08.073595
---

# Insufficient Egress Filtering: How Weak Outbound Controls Enable Attacks

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/traditional-penetrating-testing/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [Web Application Testing](https://www.blackhillsinfosec.com/services/web-application-testing/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [Fusion PenTest](https://www.blackhillsinfosec.com/fusion-penetration-testing/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-consultants/)
  + [Admin Team](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [Active SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [Antisyphon Training](https://www.blackhillsinfosec.com/about/antisyphon/)
  + [BHIS Tribe of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://bhispodcasts.transistor.fm/)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Community](https://blackhillsinfosec.com/community)
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

24
Jun
2026

[Blue Team](https://www.blackhillsinfosec.com/category/blue-team/), [C2](https://www.blackhillsinfosec.com/category/red-team/c2/), [David Fletcher](https://www.blackhillsinfosec.com/category/author/david-fletcher/), [Finding](https://www.blackhillsinfosec.com/category/finding/), [Informational](https://www.blackhillsinfosec.com/category/informational/)
[Top 100 Findings](https://www.blackhillsinfosec.com/tag/top-100-findings/)

# [Insufficient Egress Filtering: How Weak Outbound Controls Enable Attacks](https://www.blackhillsinfosec.com/insufficient-egress-filtering/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/05/DFletcher-150x150.png)

| [David Fletcher](https://www.blackhillsinfosec.com/team/david-fletcher/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/06/egress_header.png)

Insufficient egress filtering is a commonly identified vulnerability found during BHIS penetration tests. The insufficient egress filtering finding indicates that network traffic leaving the organization’s environment is not properly restricted. Lack of outbound network traffic filtering often makes it easier for an attacker to carry out attacks like establishment of Command and Control (C2) communication, credential theft, and credential relay. In addition, when outbound network communication is not sufficiently restricted, network defenders must work harder to find abnormalities in that traffic, because there is a greater variety and larger volume of network communication.

Adoption of cloud computing has extended the network boundary to include resources hosted in those cloud providers. As a result, it is critical for organizations to ensure that egress controls are applied uniformly across all paths used to reach the internet.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/06/egress_filtering_01.png)

Ideally, egress filters should be engineered to allow the absolute minimum number of outbound ports and protocols necessary for employees to complete assigned tasks.  One strategy to reach this goal involves the following steps:

* Profile outbound network connections using firewall logs or netflow data over a sufficient period to reasonably identify necessary outbound connections. Identify internal IP addresses initiating outbound connections, the destination IP addresses associated with those connections, and the destination ports used for communication.
* Determine whether any of the above connections violate organizational policy.
* Configure egress rules to accommodate authorized or ambiguous (uncatalogued but potentially necessary) outbound traffic.
* Configure a default deny egress rule to stop any traffic that does not meet the criteria in the prior step.
* Investigate communication associated with ambiguous network connections to determine root cause and conformance with organizational policy.
  + Disable rules associated with unauthorized ambiguous network communication.
  + Mark rules associated with authorized ambiguous network communication as authorized.
* Review the complete rule set for sufficient specificity. For example, if a host regularly communicates with a single remote IP address, configure the rule as such, rather than allowing communication to any destination IP address on the internet.
* Monitor firewall logs for any blocked connections and repeat the process above to determine whether the connection should be authorized.

The analysis outlined above should be repeated on every egress point that allows communication with the internet. Ensure that you consider on-premises and cloud service connections.

## Testing Your Own Egress Controls

If you are unsure whether you have sufficient egress controls in place, you can perform your own tests as described below.

### Outbound TCP Scan

By performing an outbound scan initiated from inside your network, you can identify TCP ports that can potentially be used for outbound communication. There is one catch: you cannot just scan any arbitrary host on the internet. The host has to listen and respond on all 65,535 available TCP ports. The letmeoutofyour.net host is configured to do just that. In addition, you can use a tool like [GoSpoof](https://github.com/blackhillsinfosec/GoSpoof) to create your own instance on the Virtual Private Server (VPS) provider of your choice.

The outbound scan can be executed using the PowerShell script below.

```
1..65535 | % {$test=new-object system.Net.Sockets.T...