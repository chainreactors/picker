---
title: TAG-140 Deploys DRAT V2 RAT, Targeting Indian Government, Defense, and Rail Sectors
url: https://thehackernews.com/2025/07/tag-140-deploys-drat-v2-rat-targeting.html
source: The Hacker News
date: 2025-07-08
fetch_date: 2025-10-06T23:54:08.171808
---

# TAG-140 Deploys DRAT V2 RAT, Targeting Indian Government, Defense, and Rail Sectors

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

# [TAG-140 Deploys DRAT V2 RAT, Targeting Indian Government, Defense, and Rail Sectors](https://thehackernews.com/2025/07/tag-140-deploys-drat-v2-rat-targeting.html)

**Jul 07, 2025**Ravie LakshmananCyber Espionage / Malware

[![Indian Government, Defense, and Rail Sectors](data:image/png;base64... "Indian Government, Defense, and Rail Sectors")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi8Sb0ZEzBOHNqmXKGHjCfv6Qsorn6Bjei9VQnaqQhtAJQ-fFaXXQmViZgMfmc8J1B8bCNQwsYT9twct0kyq6UlkToEiZOAtoWx_IyoPOZ5fIraoAJw9KZkY1lcZZV_aKCEHhs0p65ZsoRD4HSJanznNNjpfrOQ8Mja5jWoKEGz7eR6R62xPJLSLva4GrV3/s790-rw-e365/breach.jpg)

A hacking group with ties other than Pakistan has been found targeting Indian government organizations with a modified variant of a remote access trojan (RAT) called DRAT.

The activity has been attributed by Recorded Future's Insikt Group to a threat actor tracked as TAG-140, which it said overlaps with [SideCopy](https://thehackernews.com/2025/04/pakistan-linked-hackers-expand-targets.html), an adversarial collective assessed to be an operational sub-cluster within Transparent Tribe (aka APT-C-56, APT36, Datebug, Earth Karkaddan, Mythic Leopard, Operation C-Major, and ProjectM).

"TAG-140 has consistently demonstrated iterative advancement and variety in its malware arsenal and delivery techniques," the Mastercard-owned company [said](https://www.recordedfuture.com/research/drat-v2-updated-drat-emerges-tag-140s-arsenal) in an analysis published last month.

"This latest campaign, which spoofed the Indian Ministry of Defence via a cloned press release portal, marks a slight but notable shift in both malware architecture and command-and-control (C2) functionality."

The updated version of DRAT, called DRAT V2, is the latest addition to SideCopy's RAT arsenal, which also [comprises](https://thehackernews.com/2021/07/sidecopy-hackers-target-indian.html) [other tools](https://thehackernews.com/2023/05/sidecopy-using-action-rat-and-allakore.html) like Action RAT, AllaKore RAT, Ares RAT, CurlBack RAT, ReverseRAT, Spark RAT, and Xeno RAT to infect Windows and Linux systems.

The attack activity demonstrates the adversary's evolving playbook, highlighting its ability to refine and diversify to an "interchangeable suite" of RAT malware to harvest sensitive data to complicate attribution, detection, and monitoring efforts.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Attacks orchestrated by the threat actor have broadened their targeting focus beyond government, defense, maritime, and academic sectors to encompass organizations affiliated with the country's railway, oil and gas, and external affairs ministries. The group is known to be active since at least 2019.

The infection sequence documented by Recorded Future leverages a [ClickFix](https://thehackernews.com/2025/06/new-filefix-method-emerges-as-threat.html)-style approach that spoofs the Indian Ministry of Defence's official press release portal to drop a .NET-based version of DRAT to a new Delphi-compiled variant.

The counterfeit website has one active link that, when clicked, initiates an infection sequence that surreptitiously copies a malicious command to the machine's clipboard and urges the victim to paste and execute it by launching a command shell.

This causes the retrieval of an HTML Application (HTA) file from an external server ("trade4wealth[.]in"), which is then executed by means of mshta.exe to launch a loader called BroaderAspect. The loader is responsible for downloading and launching a decoy PDF, setting up persistence through Windows Registry changes, and downloading and running DRAT V2 from the same server.

DRAT V2 adds a new command for arbitrary shell command execution, improving its post-exploitation flexibility. It also obfuscates its C2 IP addresses using Base64-encoding and updates its custom server-initiated TCP protocol to support commands input in both ASCII and Unicode. However, the server responds only in ASCII. The original DRAT requires Unicode for both input and output.

"Compared to its predecessor, DRAT V2 reduces string obfuscation by keeping most command headers in plaintext, likely prioritizing parsing reliability over stealth," Recorded Future said. "DRAT V2 lacks advanced anti-analysis techniques and relies on basic infection and persistence methods, making it detectable via static and behavioral analysis."

Other known capabilities allow it to perform a wide range of actions on compromised hosts, including conducting reconnaissance, uploading additional payloads, and exfiltrating data.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjeoZ7rvFknUDST6JZKkScaB1b3YMUrT9Wf7voLGUPSwI_g46v_SWDsM_gRCiW8nSqffyiL58QVpDTw4EtItYDgyS_gDxE1jRQqHi1PqP5CvUWW8HJPceBZnXBTKXRKbsKSNqH0qUIm9SY5tHE6vXuXVDSjjMPGXZhFcLtPlY_cqKrnyG5Uv4g3BfE5jdom/s790-rw-e365/hta.jpg)

"These functions provide TAG-140 with persistent, flexible control over the infected system and allow for both automated and interactive post-exploitation activity without requiring the deployment of auxiliary malware tools," the company said.

"DRAT V2 appears to be another modular addition rather than a definitive evolution, reinforcing the likelihood that TAG-140 will persist in rotating RATs across campaigns to obscure signatures and maintain operational flexibility."

### APT36 Campaigns Deliver Ares RAT and DISGOMOJI

State-sponsored threat activity and [coordinated hacktivist operations](https://www.radware.com/security/threat-advisories-and-attack-reports/escalating-hacktivist-attacks-amidst-india-pakistan-tensions/) from Pakistan flared up during the [India-Pakistan conflict](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2127370) in May 2025, with APT36 capitalizing on the events to distribute Ares RAT in attacks targeting defense, government, IT, healthcare, education, and telecom sectors.

"With the deployment of tools like Ares RAT, attackers gained complete remote access t...