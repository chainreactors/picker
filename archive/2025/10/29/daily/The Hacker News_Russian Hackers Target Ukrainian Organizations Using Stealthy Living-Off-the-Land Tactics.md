---
title: Russian Hackers Target Ukrainian Organizations Using Stealthy Living-Off-the-Land Tactics
url: https://thehackernews.com/2025/10/russian-hackers-target-ukrainian.html
source: The Hacker News
date: 2025-10-29
fetch_date: 2025-10-30T03:12:55.318021
---

# Russian Hackers Target Ukrainian Organizations Using Stealthy Living-Off-the-Land Tactics

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

# [Russian Hackers Target Ukrainian Organizations Using Stealthy Living-Off-the-Land Tactics](https://thehackernews.com/2025/10/russian-hackers-target-ukrainian.html)

**Oct 29, 2025**Ravie LakshmananVulnerability / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjX53AJ2ZRF76XuNCIbv1Eoj3ugawtHgL9MA-KgpYweY8I98juyR1U7bzj5XDPBNbdMncN3EN3G2-gML7KAoHjWqskTslBDNg2k4Aj6hPOzv_597krzz8nge5VY5LEiXjV3IxtVxXhH9K35jEXfL1mIGm0yu0Kw_w1qpC4M66Pv8sTy2hTB3K_q_Ved_jNn/s790-rw-e365/malware-attac.jpg)

Organizations in Ukraine have been targeted by threat actors of Russian origin with an aim to siphon sensitive data and maintain persistent access to compromised networks.

The activity, according to a [new report](https://www.security.com/blog-post/ukraine-russia-attacks) from the Symantec and Carbon Black Threat Hunter Team, targeted a large business services organization for two months and a local government entity in the country for a week.

The attacks mainly leveraged living-off-the-land (LotL) tactics and dual-use tools, coupled with minimal malware, to reduce digital footprints and stay undetected for extended periods of time.

"The attackers gained access to the business services organization by deploying web shells on public-facing servers, most likely by exploiting one or more unpatched vulnerabilities," the Broadcom-owned cybersecurity teams said in a report shared with The Hacker News.

One of the web shells used in the attack was Localolive, which was [previously flagged](https://thehackernews.com/2025/02/microsoft-uncovers-sandworm-subgroups.html) by Microsoft as put to use by a sub-group of the Russia-linked Sandworm crew as part of a multi-year campaign codenamed BadPilot. LocalOlive is designed to facilitate the delivery of next-stage payloads like Chisel, plink, and rsockstun. It has been utilized since at least late 2021.

Early signs of malicious activity targeting the business services organization date back to June 27, 2025, with the attackers leveraging the foothold to drop a web shell and use it to conduct reconnaissance. The threat actors have also been found to run PowerShell commands to exclude the machine's Downloads from Microsoft Defender Antivirus scans, as well as set up a scheduled task to perform a memory dump every 30 minutes.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Over the next couple of weeks, the attackers carried out a variety of actions, including -

* Save a copy of the registry hive to a file named 1.log
* Dropping more web shells
* Using the web shell to enumerate all files in the user directory
* Running a command to list all running processes beginning with "kee," likely with the goal of targeting the KeePass password storage vault
* Listing all active user sessions on a second machine
* Running executables named "service.exe" and "cloud.exe" located in the Downloads folder
* Running reconnaissance commands on a third machine and performing a memory dump using the Microsoft Windows Resource Leak Diagnostic tool (RDRLeakDiag)
* Modifying the registry permits RDP connections to allow inbound RDP connections
* Running a PowerShell command to retrieve information about the Windows configuration on a fourth machine
* Running RDPclip to gain access to the clipboard in remote desktop connections
* Installing OpenSSH to facilitate remote access to the computer
* Running a PowerShell command to allow TCP traffic on port 22 for the OpenSSH server
* Creating a scheduled task to run an unknown PowerShell backdoor (link.ps1) every 30 minutes using a domain account
* Running an unknown Python script
* Deploying a legitimate MikroTik router management application ("[winbox64.exe](https://help.mikrotik.com/docs/spaces/ROS/pages/328129/WinBox)") in the Downloads folder

Interestingly, the presence of "winbox64.exe" was also documented by CERT-UA in April 2024 in connection with a [Sandworm campaign](https://thehackernews.com/2024/04/ukraine-targeted-in-cyberattack.html) aimed at energy, water, and heating suppliers in Ukraine.

Symantec and Carbon Black said it could not find any evidence in the intrusions to connect it to Sandworm, but said it "did appear to be Russian in origin." The cybersecurity company also revealed that the attacks were characterized by the deployment of several PowerShell backdoors and suspicious executables that are likely to be malware. However, none of these artifacts have been obtained for analysis.

"While the attackers used a limited amount of malware during the intrusion, much of the malicious activity that took place involved legitimate tools, either Living-off-the-Land or dual-use software introduced by the attackers," Symantec and Carbon Black said.

"The attackers demonstrated an in-depth knowledge of Windows native tools and showed how a skilled attacker can advance an attack and steal sensitive information, such as credentials, while leaving a minimal footprint on the targeted network."

The disclosure comes as Gen Threat Labs detailed [Gamaredon](https://thehackernews.com/2025/09/russian-hackers-gamaredon-and-turla.html)'s exploitation of a now-patched security flaw in WinRAR ([CVE-2025-8088](https://thehackernews.com/2025/08/winrar-zero-day-under-active.html), CVSS score: 8.8) to strike Ukrainian government agencies.

"Attackers are abusing #CVE-2025-8088 (WinRAR path traversal) to deliver RAR archives that silently drop HTA malware into the Startup folder – no user interaction needed beyond opening the benign PDF inside," the company [said](https://x.com/GenThreatLabs/status/1982890656147108151) in a post on X. "These lures are crafted to trick victims into opening weaponized archives, continuing a pattern of aggressive targeting seen in previous campaigns."

The findings also follow a report from Recorded Future, which found that the Russian cybercriminal ecosystem is being actively shaped by international law enforcement campaigns such as [Operation Endgame](htt...