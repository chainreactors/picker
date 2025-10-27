---
title: New HardBit Ransomware 4.0 Uses Passphrase Protection to Evade Detection
url: https://thehackernews.com/2024/07/new-hardbit-ransomware-40-uses.html
source: The Hacker News
date: 2024-07-16
fetch_date: 2025-10-06T17:52:19.496278
---

# New HardBit Ransomware 4.0 Uses Passphrase Protection to Evade Detection

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

# [New HardBit Ransomware 4.0 Uses Passphrase Protection to Evade Detection](https://thehackernews.com/2024/07/new-hardbit-ransomware-40-uses.html)

**Jul 15, 2024**Ravie LakshmananNetwork Security / Data Protection

[![HardBit Ransomware](data:image/png;base64... "HardBit Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgu-mUPcxAvCNombKEdgs_Lazl1FJtHJntEzLfiHUjCVgfhuDlPL7vdy188ezbgMAqGi2j0cFqFGHWd15LhFH0Dg51I1NpERM6KfkXmytBLYsOwO176FbVglq5fVYcn7NB7umuOnwP1_h4IPFRJyhoJlF4MqiXnxHf6C9N7Poe0ou-nux8vPGSbUZ8hiqo1/s790-rw-e365/hardbit-ransomware.png)

Cybersecurity researchers have shed light on a new version of a ransomware strain called HardBit that comes packaged with new obfuscation techniques to deter analysis efforts.

"Unlike previous versions, HardBit Ransomware group enhanced the version 4.0 with passphrase protection," Cybereason researchers Kotaro Ogino and Koshi Oyama [said](https://www.cybereason.com/blog/hardening-of-hardbit) in an analysis.

"The passphrase needs to be provided during the runtime in order for the ransomware to be executed properly. Additional obfuscation hinders security researchers from analyzing the malware."

HardBit, which [first emerged](https://www.fortinet.com/blog/threat-research/fortiguard-labs-ransomware-roundup) in October 2022, is a financially motivated threat actor that, similar to other ransomware groups, operates with an aim to generate illicit revenues via double extortion tactics.

What makes the threat group stand out is that it does not operate a data leak site, and instead pressurizes victims to pay up by threatening to conduct additional attacks in the future. Its primary mode of communication occurs over the Tox instant messaging service.

The exact initial access vector used to breach target environments is currently not clear, although it's suspected to involve brute-forcing RDP and SMB services.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The follow-up steps encompass performing credential theft using tools like Mimikatz and NLBrute, and network discovery via utilities such as Advanced Port Scanner, allowing the attackers to laterally move across the network by means of RDP.

"Having compromised a victim host, the HardBit ransomware payload is executed and performs a number of steps that reduce the security posture of the host before encrypting victim data," Varonis [noted](https://www.varonis.com/blog/hardbit-2.0-ransomware) in its technical write-up about HardBit 2.0 last year.

Encryption of the victim hosts is carried out by deploying HardBit, which is delivered using a known file infector virus called [Neshta](https://blogs.blackberry.com/en/2019/10/threat-spotlight-neshta-file-infector-endures). It's worth noting that Neshta has been used by threat actors in the past to also [distribute Big Head ransomware](https://thehackernews.com/2023/07/beware-of-big-head-ransomware-spreading.html).

HardBit is also designed to disable Microsoft Defender Antivirus and terminate processes and services to evade potential detection of its activities and inhibit system recovery. It then encrypts files of interest, updates their icons, changes desktop wallpaper, and alters the system's volume label with string "Locked by HardBit."

[![HardBit Ransomware](data:image/png;base64... "HardBit Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6BIjjz4raXxBCEPnWJ6rjS_suhHSq4VAbzxEo3GOzeQAV6R512BkyRFL2MLsLzvaOI2xJHLcLaxEmznEnMHhzs0of1niUzoFXyINFa5bt_hePn4xHGw86UptIRL7_YHBvz31ih0Vg0FLrgoQTyrH9EXXOu06bdzrSzyNPdrifA0OyfZiSaSsXseOWdf6E/s790-rw-e365/ransomware.png)

Besides being offered to operators in the form of command-line or GUI versions, the ransomware requires an authorization ID in order for it to be successfully executed. The GUI flavor further supports a wiper mode to irrevocably erase files and wipe the disk.

"Once threat actors successfully input the decoded authorization ID, HardBit prompts for an encryption key to encrypt the files on the target machines and it proceeds with ransomware procedure," Cybereason noted.

"Wiper mode feature needs to be enabled by the HardBit Ransomware group and the feature is likely an additional feature that operators need to purchase. If the operators need wiper mode, the operator would need to deploy hard.txt, an optional configuration file of HardBit binary and contains authorization ID to enable wiper mode."

The development comes as cybersecurity firm Trellix [detailed](https://www.trellix.com/blogs/research/cactus-ransomware-new-strain-in-the-market/) a [CACTUS](https://thehackernews.com/2023/12/microsoft-warns-of-malvertising-scheme.html) ransomware attack that has been observed exploiting security flaws in Ivanti Sentry ([CVE-2023-38035](https://thehackernews.com/2023/08/ivanti-warns-of-critical-zero-day-flaw.html)) to install the file-encrypting malware using legitimate remote desktop tools like AnyDesk and Splashtop.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Ransomware activity continues to "remain on an upward trend" in 2024, with ransomware actors claiming 962 attacks in the first quarter of 2024, up from 886 attacks reported year-over-year. [LockBit](https://thehackernews.com/2024/06/fbi-distributes-7000-lockbit-ransomware.html), [Akira](https://thehackernews.com/2024/07/new-ransomware-group-exploiting-veeam.html), and [BlackSuit](https://thehackernews.com/2023/06/new-linux-ransomware-strain-blacksuit.html) have emerged as the most prevalent ransomware families during the time period, Symantec said.

According to Palo Alto Networks' 2024 Unit 42 Incident Response report, the [median time](https://www.paloaltonetworks.com/blog/2024/02/unit-42-incident-response-report/) it takes to go from compromise to data exfiltration plummeted from nine days in 2021 to two days last year. In almost half (45%) of cases this year, it was just under 24 hours.

"Available evidence suggests that exploitation of k...