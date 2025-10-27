---
title: New Rust-Based Ransomware Cicada3301 Targets Windows and Linux Systems
url: https://thehackernews.com/2024/09/new-rust-based-ransomware-cicada3301.html
source: The Hacker News
date: 2024-09-04
fetch_date: 2025-10-06T18:37:41.143795
---

# New Rust-Based Ransomware Cicada3301 Targets Windows and Linux Systems

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

# [New Rust-Based Ransomware Cicada3301 Targets Windows and Linux Systems](https://thehackernews.com/2024/09/new-rust-based-ransomware-cicada3301.html)

**Sep 03, 2024**Ravie LakshmananEndpoint Security / Malware

[![Rust-Based Ransomware](data:image/png;base64... "Rust-Based Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhmlnYevRFVZTttlnIbwaWXTcdmgfBYgtCAnifl_0Q_6ZkPshiv-vb9A1hiuOxe6J6shaUWPzF3yq0fQUu-CmVnVtcVLP8mWlpqq_a6q558J5kRDI8ejO19ssAcyOd9c8DX5Avdi7YOCDuSI82D-9QwPqXq7mfRionmodiAAeEvDCdtbyDkJo0_ar-qJgfq/s790-rw-e365/linux.png)

Cybersecurity researchers have unpacked the inner workings of a new ransomware variant called Cicada3301 that shares similarities with the now-defunct [BlackCat](https://thehackernews.com/2024/03/exit-scam-blackcat-ransomware-group.html) (aka ALPHV) operation.

"It appears that Cicada3301 ransomware primarily targets small to medium-sized businesses (SMBs), likely through opportunistic attacks that exploit vulnerabilities as the initial access vector," cybersecurity company Morphisec [said](https://blog.morphisec.com/cicada3301-ransomware-threat-analysis) in a technical report shared with The Hacker News.

Written in Rust and capable of targeting both Windows and Linux/ESXi hosts, Cicada3301 first emerged in June 2024, inviting potential affiliates to join their ransomware-as-a-service (RaaS) platform via an advertisement on the RAMP underground forum.

A notable aspect of the ransomware is that the executable embeds the compromised user's credentials, which are then used to run [PsExec](https://learn.microsoft.com/en-us/sysinternals/downloads/psexec), a legitimate tool that makes it possible to run programs remotely.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Cicada3301's similarities with BlackCat also extend to its use of ChaCha20 for encryption, [fsutil](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/fsutil-behavior) to evaluate symbolic links and encrypt redirected files, as well as IISReset.exe to stop the IIS services and encrypt files that may otherwise be locked for for modification or deletion.

Other overlaps to BlackCat include steps undertaken to delete shadow copies, disable system recovery by manipulating the [bcdedit](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bcdedit) utility, increase the [MaxMpxCt](https://smallvoid.com/article/winnt-smb-settings.html) value to support higher volumes of traffic (e.g., SMB PsExec requests), and clear all event logs by utilizing the [wevtutil](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wevtutil) utility.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQpcapAzIq5XO2TiTWVJyEJHsj_adndwvuUAIx0aWee1iqq4JhTIPZR18r2aq9O9aKyrPiELMMgKwm7qxrt2WmWkYUwn5Op-zJntY4rwy-SsWD61gISHAn8KLORBE56uInX2uI1DTXcDcaCCJ6ndMeP8CbHDFcvsB1_LaxeDRgPkhkR1Ia5PFeBxp06NfX/s790-rw-e365/ransomware-malware.jpg)

Cicada3301 has also observed stopping locally deployed virtual machines (VMs), a behavior previously adopted by the [Megazord](https://thehackernews.com/2024/05/black-basta-ransomware-strikes-500.html) ransomware and the [Yanluowang](https://thehackernews.com/2022/08/cisco-confirms-its-been-hacked-by.html) ransomware, and terminating various backup and recovery services and a hard-coded list of dozens of processes.

Besides maintaining a built-in list of excluded files and directories during the encryption process, the ransomware targets a total of 35 file extensions - sql, doc, rtf, xls, jpg, jpeg, psd, docm, xlsm, ods, ppsx, png, raw, dotx, xltx, pptx, ppsm, gif, bmp, dotm, xltm, pptm, odp, webp, pdf, odt, xlsb, ptox, mdf, tiff, docx, xlsx, xlam, potm, and txt.

Morphisec said its investigation also uncovered additional tools like [EDRSandBlast](https://github.com/wavestone-cdt/EDRSandblast) that weaponize a vulnerable signed driver to bypass EDR detections, a technique also adopted by the [BlackByte](https://thehackernews.com/2022/10/blackbyte-ransomware-abuses-vulnerable.html) ransomware group in the past.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The findings follow Truesec's analysis of the ESXi version of Cicada3301, while also uncovering indications that the group may have teamed up with the operators of the [Brutus botnet](https://annoyed.engineer/2024/03/23/the-brutus-botnet/) to obtain initial access to enterprise networks.

"Regardless of whether Cicada3301 is a rebrand of ALPHV, they have a ransomware written by the same developer as ALPHV, or they have just copied parts of ALPHV to make their own ransomware, the timeline suggests the demise of BlackCat and the emergence of first the Brutus botnet and then the Cicada3301 ransomware operation may possibly be all connected," the company [noted](https://www.truesec.com/hub/blog/dissecting-the-cicada).

The attacks against VMware ESXi systems also entail using intermittent encryption to encrypt files larger than a set threshold (100 MB) and a parameter named "no\_vm\_ss" to encrypt files without shutting down the virtual machines that are running on the host.

The emergence of Cicada3301 has also prompted an eponymous "non-political movement," which has dabbled in "mysterious" [cryptographic puzzles](https://en.wikipedia.org/wiki/Cicada_3301), to issue a [statement](https://www.cicada3301official.com/pages/content/images/3301-statement-september-1-2024.jpg) that it has no connection to the ransomware scheme.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[*...