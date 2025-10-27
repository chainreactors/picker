---
title: China-Linked Hackers Launch Targeted Espionage Campaign on African IT Infrastructure
url: https://thehackernews.com/2025/07/china-linked-hackers-launch-targeted.html
source: The Hacker News
date: 2025-07-22
fetch_date: 2025-10-06T23:53:05.465382
---

# China-Linked Hackers Launch Targeted Espionage Campaign on African IT Infrastructure

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

# [China-Linked Hackers Launch Targeted Espionage Campaign on African IT Infrastructure](https://thehackernews.com/2025/07/china-linked-hackers-launch-targeted.html)

**Jul 21, 2025**Ravie LakshmananBrowser Security / Malware

[![Espionage Campaign on African IT Infrastructure](data:image/png;base64... "Espionage Campaign on African IT Infrastructure")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgGQ8VNVZWQIB-c3_6loVdbrIjcIQmgUy5EdGnXfL02pBQn-y0v9vTaUXGGOh8F2w5gdnTK7O6mXI35vbnzmTmgxqzW4UgKgTW246OP9eeU1KHamc_aIZ8Ftz9sK_4mTpNaEXS1oLSWkl5QFD7ICeD-eGZ-cq2trNV3lnFvSF8hX5IGCX3VMTLQ4M1kkmoN/s790-rw-e365/chinese-hackers.jpg)

The China-linked cyber espionage group tracked as **APT41** has been attributed to a new campaign targeting government IT services in the African region.

"The attackers used hardcoded names of internal services, IP addresses, and proxy servers embedded within their malware," Kaspersky researchers Denis Kulik and Daniil Pogorelov [said](https://securelist.com/apt41-in-africa/116986/). "One of the C2s [command-and-control servers] was a captive SharePoint server within the victim's infrastructure."

APT41 is the moniker [assigned](https://thehackernews.com/2025/05/chinese-apt41-exploits-google-calendar.html) to a prolific Chinese nation-state hacking group that's known for targeting organizations spanning multiple sectors, including telecom and energy providers, educational institutions, healthcare organizations and IT energy companies in more than three dozen countries.

What makes the campaign noteworthy is its focus on Africa, which, as the Russian cybersecurity vendor noted, "had experienced the least activity" from this specific threat actor. That said, the findings line up with [previous observations](https://thehackernews.com/2024/08/china-backed-earth-baku-expands-cyber.html) from Trend Micro that the continent has found itself in its crosshairs since late 2022.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Kaspersky said it began an investigation after it found "suspicious activity" on multiple workstations associated with an unnamed organization's IT infrastructure that involved the attackers running commands to ascertain the availability of their C2 server, either directly or via an internal proxy server within the compromised entity.

"The source of the suspicious activity turned out to be an unmonitored host that had been compromised," the researchers noted. "[Impacket](https://attack.mitre.org/software/S0357/) was executed on it in the context of a service account. After the Atexec and WmiExec modules finished running, the attackers temporarily suspended their operations."

Soon after, the attackers are said to have harvested credentials associated with privileged accounts to facilitate privilege escalation and lateral movement, ultimately deploying Cobalt Strike for C2 communication using DLL side-loading.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlHUD3CwhezlQovLULGwuE5OWhy02jR8BVqgdqMvsEYv2f-i9wriQpwnFWEzcvLxsaknxem8VvUomMTeISol_1KmwclOmTAU-3VjUxble9dLmHjo2YhVXug4Hbo6550BitQYAsUQqb8DYF3xZM6IdSAyo7Qq3OwiDtDo-YjnJdrMxnBl8_HdIs1Ip8oXbx/s790-rw-e365/apt-2.png)

The malicious DLLs incorporate a check to verify the language packs installed on the host and proceed with the execution only if the following language packs are not detected: Japanese, Korean (South Korea), Chinese (Mainland China), and Chinese (Taiwan).

The attack is also characterized by the use of a hacked SharePoint server for C2 purposes, using it to send commands that are run by a C#-based malware uploaded to the victim hosts.

"They distributed files named agents.exe and agentx.exe via the SMB protocol to communicate with the server," Kaspersky explained. "Each of these files is actually a C# trojan whose primary function is to execute commands it receives from a web shell named CommandHandler.aspx, which is installed on the SharePoint server."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjo0RtlRhclZiNlAE4Duy89OzwUPfj8FAteKvlwXqRexN3tUCnmVE6goEYZLJ_OQsl7FpV9hsUV-OLa8BXZCTWeHdBPvyCjetxAA33TkY9UrZ6EBK8hyphenhyphenx2aAQKxKtfgHY8gmRNO-MF6xVpZpglKkhooejpSxxEhhnlXOf7qEYulKHfJ76btQ9WM4iRvVKfu/s790-rw-e365/apt-1.png)

This method blends traditional malware deployment with living-off-the-land tactics, where trusted services like SharePoint are turned into covert control channels. These behaviors align with techniques categorized under MITRE ATT&CK, including T1071.001 (Web Protocols) and T1047 (WMI), making them difficult to detect using signature-based tools alone.

Furthermore, the threat actors have been spotted carrying out follow-on activity on machines deemed valuable post initial reconnaissance. This is accomplished by running a cmd.exe command to download from an external resource a malicious HTML Application (HTA) file containing embedded JavaScript and run it using mshta.exe.

The exact nature of the payload delivered via the external URL, a domain impersonating GitHub ("github.githubassets[.]net") so as to evade detection, is currently unknown. However, an analysis of one of the previously distributed scripts shows that it's designed to spawn a reverse shell, thereby granting the attackers the ability to execute commands on the infected system.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Also put to use in the attacks are stealers and credential-harvesting utilities to gather sensitive data and exfiltrate the details via the SharePoint server. Some of the tools deployed by the adversary are listed below -

* [Pillager](https://github.com/brittonhayes/pillager), albeit a modified version, to steal credentials from browsers, databases, and administrative utilities like MobaXterm; source code; screenshots; chat sessions and data; email messages; SSH and FTP sessions; list of installed apps; output of the systeminfo and tasklist ...