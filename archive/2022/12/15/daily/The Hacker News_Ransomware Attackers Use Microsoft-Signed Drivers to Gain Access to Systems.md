---
title: Ransomware Attackers Use Microsoft-Signed Drivers to Gain Access to Systems
url: https://thehackernews.com/2022/12/ransomware-attackers-use-microsoft.html
source: The Hacker News
date: 2022-12-15
fetch_date: 2025-10-04T01:34:46.127681
---

# Ransomware Attackers Use Microsoft-Signed Drivers to Gain Access to Systems

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

# [Ransomware Attackers Use Microsoft-Signed Drivers to Gain Access to Systems](https://thehackernews.com/2022/12/ransomware-attackers-use-microsoft.html)

**Dec 14, 2022**Ravie LakshmananEndpoint Security / Firmware Security

[![Ransomware](data:image/png;base64... "Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhC0YFxPW0F2EEjjLE6yM4RNDX9FSsFi1dhqg80hvGRh9VoIyJAM7Hzps5d7KucdYEoH5bTuw-6PgEyd3ahi5H9PZvqC0bYVPYXggOWPeUNn4n116GZgb-TtmjmbWAKq5bi7Yd1T7Ni5j7uDCGc71vAGp6_KGUzCS6SuPGTHdrzzqPLvzXMmDgHGFYy/s790-rw-e365/windows.png)

Microsoft on Tuesday disclosed it took steps to implement blocking protections and suspend accounts that were used to publish malicious [drivers](https://learn.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/what-is-a-driver-) that were certified by its Windows [Hardware Developer Program](https://partner.microsoft.com/en-us/dashboard/Registration/Hardware).

The tech giant said its investigation revealed the activity was restricted to a number of developer program accounts and that no further compromise was detected.

Cryptographically signing malware is concerning not least because it not only undermines a key security mechanism but also allows threat actors to subvert traditional detection methods and infiltrate target networks to perform highly privileged operations.

The probe, Redmond stated, was initiated after it was notified of rogue drivers being used in post-exploitation efforts, including deploying ransomware, by cybersecurity firms Mandiant, SentinelOne, and Sophos on October 19, 2022.

One notable aspect of these attacks was that the adversary had already obtained administrative privileges on compromised systems before using the drivers.

"Several developer accounts for the Microsoft Partner Center were engaged in submitting malicious drivers to obtain a Microsoft signature," Microsoft [explained](https://msrc.microsoft.com/update-guide/vulnerability/ADV220005). "A new attempt at submitting a malicious driver for signing on September 29, 2022, led to the suspension of the sellers' accounts in early October."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

According to an analysis from Sophos, threat actors affiliated with the [Cuba ransomware](https://thehackernews.com/2022/12/cuba-ransomware-extorted-over-60.html) (aka COLDDRAW) planted a malicious signed driver in a failed attempt at disabling endpoint detection tools via a novel malware loader dubbed BURNTCIGAR, which was [first revealed](https://www.mandiant.com/resources/blog/unc2596-cuba-ransomware) by Mandiant in February 2022.

The company also identified three variants of the driver signed by code signing certificates that belong to two Chinese companies, Zhuhai Liancheng Technology and Beijing JoinHope Image Technology.

The reasoning behind using signed drivers is that it offers a way for threat actors to get around [crucial security measures](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/driver-signing) which require kernel-mode drivers to be signed in order for Windows to load the package. What's more, the technique misuses the de facto trust security tools place in Microsoft-attested drivers to their advantage.

"Threat actors are moving up the trust pyramid, attempting to use increasingly more well-trusted cryptographic keys to digitally sign their drivers," Sophos researchers Andreas Klopsch and Andrew Brandt [said](https://news.sophos.com/en-us/2022/12/13/signed-driver-malware-moves-up-the-software-trust-chain/). "Signatures from a large, trustworthy software publisher make it more likely the driver will load into Windows without hindrance."

[![Ransomware](data:image/png;base64... "Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgPn6pcUHz82SdGSZzh3s3Uea_Shcy_WAS6FHpr1R-7Y0iHX42Ovkp6EHvte5noobSnTuv-15WCVDKzbphHVsuk7Jjc5ZbweFCAz5M1EKEssunvne_RxkO7YtJdByJZS-VRVcUWZhrDaHD_m6WsnsLSGobkEXwvrf6vhEfeuZE0Ae5cn-pCWtnirLTK/s790-rw-e365/driver-ransomware.png)

Google-owned Mandiant, in a coordinated disclosure, [said](https://www.mandiant.com/resources/blog/hunting-attestation-signed-malware) it observed a financially motivated threat group known as UNC3944 employing a loader named STONESTOP to install a malicious driver dubbed POORTRY that's designed to terminate processes associated with security software and delete files.

Stating that it has "continually observed threat actors use compromised, stolen, and illicitly purchased code-signing certificates to sign malware," the threat intelligence and incident response firm noted that "several distinct malware families, associated with distinct threat actors, have been signed with this process."

This has given rise to the possibility that these hacking groups could be leveraging a criminal service for code signing (i.e., malicious driver signing as a service), wherein the provider gets the malware artifacts signed through Microsoft's attestation process on behalf of the actors.

[![Ransomware](data:image/png;base64... "Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4B0fOzTD_4kYBPayN9ywx8VjCJHukqioim03rUd_WlyNI6LLH1ViRx_qI6877jMvpJt0Te219W6kQ9jjD_MYeBipELbycKzkjiwohyj81r5Hs_FdhlGQbcjfmkHUkrIhoyz9OVogVtesUEOTKLw74Jt40BAq9tn3wBONZSHbOQYlmrl4DJ1rgKfeH/s790-rw-e365/ransomware.png)

STONESTOP and POORTRY are said to have been used by UNC3944 in attacks aimed at telecommunication, BPO, MSSP, financial services, cryptocurrency, entertainment, and transportation sectors, SentinelOne [said](https://www.sentinelone.com/labs/driving-through-defenses-targeted-attacks-leverage-signed-malicious-microsoft-drivers/), adding a different threat actor utilized a similar signed driver that resulted in the deployment of [Hive ransomware](https://thehackernews.com/2022/11/hive-ransomware-attackers-extorted-100.html).

The intrusion set identified by SentinelOne also likely overlaps with a "persistent" campaign orchestrated by a threat actor tracked by Cr...