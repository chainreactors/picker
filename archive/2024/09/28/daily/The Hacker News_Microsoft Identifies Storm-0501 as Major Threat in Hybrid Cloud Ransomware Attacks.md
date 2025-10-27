---
title: Microsoft Identifies Storm-0501 as Major Threat in Hybrid Cloud Ransomware Attacks
url: https://thehackernews.com/2024/09/microsoft-identifies-storm-0501-as.html
source: The Hacker News
date: 2024-09-28
fetch_date: 2025-10-06T18:38:56.628585
---

# Microsoft Identifies Storm-0501 as Major Threat in Hybrid Cloud Ransomware Attacks

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

# [Microsoft Identifies Storm-0501 as Major Threat in Hybrid Cloud Ransomware Attacks](https://thehackernews.com/2024/09/microsoft-identifies-storm-0501-as.html)

**Sep 27, 2024**Ravie LakshmananRansomware / Cloud Security

[![Hybrid Cloud Ransomware Attacks](data:image/png;base64... "Hybrid Cloud Ransomware Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgkLoJxoEp_DnlEt9CrbBKOycsaGbj6JOhBSUZ28iu8EXRfU3RR-ghbTzkm2DD2NrPu7YbFU6yHQz-vNaUvO2VZ_BRbu8Hjbi_fijtMHCbqRCVpHHmsquaTMUPbRNP7RFRAj1_bvmBDIUYmHhaSLtWzJaKt4Bk9Q6JQ9_WmfD3q7w_YjVuCQwfWp1bWiJ-G/s790-rw-e365/ransomware.png)

The threat actor known as Storm-0501 has targeted government, manufacturing, transportation, and law enforcement sectors in the U.S. to stage ransomware attacks.

The multi-stage attack campaign is designed to compromise hybrid cloud environments and perform lateral movement from on-premises to cloud environment, ultimately resulting in data exfiltration, credential theft, tampering, persistent backdoor access, and ransomware deployment, Microsoft said.

"Storm-0501 is a financially motivated cybercriminal group that uses commodity and open-source tools to conduct ransomware operations," [according](https://www.microsoft.com/en-us/security/blog/2024/09/26/storm-0501-ransomware-attacks-expanding-to-hybrid-cloud-environments/) to the tech giant's threat intelligence team.

Active since 2021, the threat actor has a history of targeting education entities with Sabbath (54bb47h) ransomware before evolving into a ransomware-as-a-service ([RaaS](https://www.bitdefender.com/blog/businessinsights/understanding-the-roles-in-the-ransomware-as-a-service-ecosystem-whos-targeting-your-data-security-gaps/)) affiliate delivering various ransomware payloads over the years, including Hive, BlackCat (ALPHV), Hunters International, LockBit, and Embargo ransomware.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

A notable aspect of Storm-0501's attacks is the use of weak credentials and over-privileged accounts to move from organizations on-premises to cloud infrastructure.

Other initial access methods include using a foothold already established by access brokers like Storm-0249 and Storm-0900, or exploiting various known remote code execution vulnerabilities in unpatched internet-facing servers such as Zoho ManageEngine, Citrix NetScaler, and Adobe ColdFusion 2016.

The access afforded by any of the aforementioned approaches paves the way for extensive discovery operations to determine high-value assets, gather domain information, and perform Active Directory reconnaissance. This is followed by the deployment of remote monitoring and management tools (RMMs) like AnyDesk to maintain persistence.

"The threat actor took advantage of admin privileges on the local devices it compromised during initial access and attempted to gain access to more accounts within the network through several methods," Microsoft said.

"The threat actor primarily utilized Impacket's SecretsDump module, which extracts credentials over the network, and leveraged it across an extensive number of devices to obtain credentials."

The compromised credentials are then used to access even more devices and extract additional credentials, with the threat actor simultaneously accessing sensitive files to extract KeePass secrets and conducting brute-force attacks to obtain credentials for specific accounts.

[![Hybrid Cloud Ransomware Attacks](data:image/png;base64... "Hybrid Cloud Ransomware Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJ8R5Be_IFVRLtHyZOZ5mFO1iovBKD3OBUpNXwc6jmblJOOVMfHnEDr3wVekDQgThXUQiLM55sHyjceO04ucbvl7bnEeIG-CzUDctZ-TtQwJWj6aYxydNHhyphenhyphen9kFPu9gxEwx2GYCw8AwfngZlvyrE9s_Be6O7ccRDPAGyGh_PJ1kbMs50WLaO1gTiDQKI0z/s790-rw-e365/attack-ms.gif)

Microsoft said it detected Storm-0501 employing Cobalt Strike to move laterally across the network using the compromised credentials and send follow-on commands. Data exfiltration from the on-premises environment is accomplished by using Rclone to transfer the data to the MegaSync public cloud storage service.

The threat actor has also been observed creating persistent backdoor access to the cloud environment and deploying ransomware to the on-premises, making it the latest threat actor to target hybrid cloud setups after Octo Tempest and Manatee Tempest.

"The threat actor used the credentials, specifically Microsoft Entra ID (formerly Azure AD), that were stolen from earlier in the attack to move laterally from the on-premises to the cloud environment and establish persistent access to the target network through a backdoor," Redmond said.

The pivot to the cloud is said to be accomplished either through a compromised Microsoft Entra Connect Sync user account or via cloud session hijacking of an on-premises user account that has a respective admin account in the cloud with multi-factor authentication (MFA) disabled.

The attack culminates with the deployment of Embargo ransomware across the victim organization upon obtaining sufficient control over the network, exfiltrating files of interest, and lateral movement to the cloud. [Embargo](https://ransomwareattacks.halcyon.ai/attacks/embargo-ransomware-group-strikes-dme-delivers-in-cyber-attack) is a Rust-based ransomware first discovered in May 2024.

"Operating under the RaaS model, the ransomware group behind Embargo allows affiliates like Storm-0501 to use its platform to launch attacks in exchange for a share of the ransom," Microsoft said.

"Embargo affiliates employ double extortion tactics, where they first encrypt a victim's files and threaten to leak stolen sensitive data unless a ransom is paid."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

That having said, evidence gathered by the Windows maker shows that the threat actor does not always resort to ransomware distribution, instead opting to only maintain backdoor access to the network in some cases.

The...