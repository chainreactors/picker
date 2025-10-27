---
title: Thai Officials Targeted in Yokai Backdoor Campaign Using DLL Side-Loading Techniques
url: https://thehackernews.com/2024/12/thai-officials-targeted-in-yokai.html
source: The Hacker News
date: 2024-12-15
fetch_date: 2025-10-06T19:38:56.429660
---

# Thai Officials Targeted in Yokai Backdoor Campaign Using DLL Side-Loading Techniques

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

# [Thai Officials Targeted in Yokai Backdoor Campaign Using DLL Side-Loading Techniques](https://thehackernews.com/2024/12/thai-officials-targeted-in-yokai.html)

**Dec 14, 2024**Ravie LakshmananMalware / Cyber Threat

[![Yokai Backdoor Campaign](data:image/png;base64... "Yokai Backdoor Campaign")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZOGTKRo8AgOrGrDGguwKn-IOstG7hgHE9G_oh0cDppHZZNbzp-YpWGbOHHgaz_9DU16z04PZkuLAOD381w-YyonhvEtgf-iV4D7JqxxSTeLDFaM4axWIc0M2X-2NHq499rveQnkp_aViApPOg6tQwX6QGgyZJ13X_ty8R2GvVI6IvX8Aazvb48bwIrHWY/s790-rw-e365/malware.png)

Thai government officials have emerged as the target of a new campaign that leverages a technique called [DLL side-loading](https://www.crowdstrike.com/en-us/blog/dll-side-loading-how-to-combat-threat-actor-evasion-techniques/) to deliver a previously undocumented backdoor dubbed **Yokai**.

"The target of the threat actors were Thailand officials based on the nature of the lures," Nikhil Hegde, senior engineer for Netskope's Security Efficacy team, told The Hacker News. "The Yokai backdoor itself is not limited and can be used against any potential target."

The [starting point of the attack chain](https://www.netskope.com/blog/new-yokai-side-loaded-backdoor-targets-thai-officials) is a RAR archive containing two Windows shortcut files named in Thai that translate to "United States Department of Justice.pdf" and "United States government requests international cooperation in criminal matters.docx."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The exact initial vector used to deliver the payload is currently not known, although Hegde speculated that it would likely be spear-phishing due to the lures employed and the fact that RAR files have been used as malicious attachments in phishing emails.

Launching the shortcut files causes a decoy PDF and Microsoft Word document to be opened, respectively, while also dropping a malicious executable stealthily in the background. Both the lure files relate to [Woravit Mektrakarn](https://namus.nij.ojp.gov/case/MP39535), a Thai national who is wanted in the U.S. in connection with the disappearance of a Mexican immigrant. Mektrakarn was charged with murder in 2003 and is said to have fled to Thailand.

The executable, for its part, is designed to drop three more files: A legitimate binary associated with the iTop Data Recovery application ("IdrInit.exe"), a malicious DLL ("ProductStatistics3.dll"), and a DATA file containing information sent by an attacker-controlled server. In the next stage, "IdrInit.exe" is abused to [sideload the DLL](https://cloud.google.com/blog/topics/threat-intelligence/abusing-dll-misconfigurations), ultimately leading to the deployment of the backdoor.

[![DLL Side-Loading Techniques](data:image/png;base64... "DLL Side-Loading Techniques")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjOS_N41GD_D48JftyBPd3LRnnehPC9OZ4HIF7q_Wxk_fQUsuNJ54THinfj-ik1b40zYoaJO7YqiA41wLK3H3N9oxz8kqMevEkwz_nNPfpbyOXY_Kx4SviW6zvnJKY7FZFpdKQIQxhl3_8VHKHzhvEJRzUkeVaBUXg-Jv2oMaZWLa_5Vr6SFKtbVBCZYB6I/s790-rw-e365/pwershell.png)

Yokai is responsible for setting up persistence on the host and connecting to the command-and-control (C2) server in order to receive command codes that allow it to spawn cmd.exe and execute shell commands on the host.

The development comes as Zscaler ThreatLabz revealed it discovered a malware campaign leveraging Node.js-compiled executables for Windows to distribute cryptocurrency miners and information stealers such as XMRig, [Lumma](https://thehackernews.com/2024/06/beware-fake-browser-updates-deliver.html), and [Phemedrone Stealer](https://thehackernews.com/2024/01/hackers-weaponize-windows-flaw-to.html). The rogue applications have been codenamed NodeLoader.

The attacks employ malicious links embedded in YouTube video descriptions, leading users to MediaFire or phony websites that urge them to download a ZIP archive that is disguised as video game hacks. The end goal of the attacks is to extract and run NodeLoader, which, in turn, downloads a PowerShell script responsible for launching the final-stage malware.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"NodeLoader uses a module called sudo-prompt, a publicly available tool on GitHub and npm, for privilege escalation," Zscaler [said](https://www.zscaler.com/blogs/security-research/nodeloader-exposed-node-js-malware-evading-detection). "The threat actors employ social engineering and anti-evasion techniques to deliver NodeLoader undetected."

It also follows a spike in phishing attacks distributing the commercially available [Remcos RAT](https://thehackernews.com/2024/11/cybercriminals-use-excel-exploit-to.html), with threat actors giving the infection chains a makeover by employing Visual Basic Script (VBS) scripts and Office Open XML documents as a launchpad to trigger the multi-stage process.

[![DLL Side-Loading Techniques](data:image/png;base64... "DLL Side-Loading Techniques")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg57xc9KIUc_dAHs-6zLeRhoxN7x2bF1pBgomeOuWP6R9AGmk-VnWVS05iJbCE-aXi2-uaYGutfk-J5eaXbwAXtGJn1AAd2mh0by5wEEUUQjnZKchd-6YMWagPrAETt5HHw-KAv3tnXhIzKVjjfwMT08ZlFRKPRGLZ5Gm16C4IvMBt7Gm7bBYd4970DmdJd/s790-rw-e365/zz.jpg)

In one set of attacks, executing the VBS file leads to a highly obfuscated PowerShell script that downloads interim payloads, ultimately resulting in the injection of Remcos RAT into RegAsm.exe, a legitimate Microsoft .NET executable.

The other variant entails using an Office Open XML document to load an RTF file that's susceptible to [CVE-2017-11882](https://thehackernews.com/2023/12/hackers-exploiting-old-ms-excel.html), a known remote code execution flaw in Microsoft Equation Editor, to fetch a VBS file that subsequently proceeds to fetch PowerShell in order to inject Remcos payload into the memory of RegAsm.exe.

[![](data:image/png;base64...)](https://blogger.googleusercontent.c...