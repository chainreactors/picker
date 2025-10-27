---
title: Threat Actor Bypass SentinelOne EDR to Deploy Babuk Ransomware
url: https://cybersecuritynews.com/threat-actor-bypass-sentinelone-edr/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-07
fetch_date: 2025-10-06T22:29:08.302689
---

# Threat Actor Bypass SentinelOne EDR to Deploy Babuk Ransomware

[Linkedin](https://www.linkedin.com/company/cybersecurity-news/ "Linkedin")

[Naver](https://news.google.com/publications/CAAqMggKIixDQklTR3dnTWFoY0tGV041WW1WeWMyVmpkWEpwZEhsdVpYZHpMbU52YlNnQVAB?hl=en-IN&gl=IN&ceid=IN:en "Naver")

[RSS](https://cybersecuritynews.com/feed/ "RSS")

[Twitter](https://twitter.com/The_Cyber_News "Twitter")

* [Home](https://cybersecuritynews.com/)
* [Threats](https://cybersecuritynews.com/category/threats/)
* [Cyber Attacks](https://cybersecuritynews.com/category/cyber-attack/)
* [Vulnerabilities](https://cybersecuritynews.com/category/vulnerability/)
* [Breaches](https://cybersecuritynews.com/category/data-breaches/)
* [Top 10](https://cybersecuritynews.com/category/top-10/)

Search

[![Cyber Security News](https://cybersecuritynews.com/wp-content/uploads/2025/05/Cyber-Security-News-Logo.webp "Cyber Security News")Cyber Security NewsLatest Cyber Security News](https://cybersecuritynews.com/ "Cyber Security News")

Monday, October 6, 2025

[Linkedin](https://www.linkedin.com/company/cybersecurity-news/ "Linkedin")

[RSS](https://cybersecuritynews.com/feed/ "RSS")

[Twitter](https://x.com/The_Cyber_News "Twitter")

[Google News](https://news.google.com/publications/CAAqMggKIixDQklTR3dnTWFoY0tGV041WW1WeWMyVmpkWEpwZEhsdVpYZHpMbU52YlNnQVAB?hl=en-IN&gl=IN&ceid=IN:en "Google News")[Google News](https://news.google.com/publications/CAAqMggKIixDQklTR3dnTWFoY0tGV041WW1WeWMyVmpkWEpwZEhsdVpYZHpMbU52YlNnQVAB?hl=en-IN&gl=IN&ceid=IN:en)

[![Cyber Security News](https://cybersecuritynews.com/wp-content/uploads/2025/05/Cyber-Security-News-Logo.webp "Cyber Security News")Cyber Security NewsLatest Cyber Security News](https://cybersecuritynews.com/ "Cyber Security News")

* [Home](https://cybersecuritynews.com/)
* [Threats](https://cybersecuritynews.com/category/threats/)
* [Cyber Attacks](https://cybersecuritynews.com/category/cyber-attack/)
* [Vulnerabilities](https://cybersecuritynews.com/category/vulnerability/)
* [Breaches](https://cybersecuritynews.com/category/data-breaches/)
* [Top 10](https://cybersecuritynews.com/category/top-10/)

[Follow on LinkedIn](https://www.linkedin.com/company/cybersecurity-news/ "Follow on LinkedIn")

Search

[Home](https://cybersecuritynews.com/)  [Cyber Security](https://cybersecuritynews.com/category/cyber-security/ "View all posts in Cyber Security")  Threat Actor Bypass SentinelOne EDR to Deploy Babuk Ransomware

* [Cyber Security](https://cybersecuritynews.com/category/cyber-security/)
* [Cyber Security News](https://cybersecuritynews.com/category/cyber-security-news/)
* [Ransomware](https://cybersecuritynews.com/category/ransomware/)
* [Threats](https://cybersecuritynews.com/category/threats/)

# Threat Actor Bypass SentinelOne EDR to Deploy Babuk Ransomware

By

[Guru Baran](https://cybersecuritynews.com/author/guru/)

-

May 6, 2025

[![SentinelOne EDR](https://i3.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMr8unloNU2GcehZp1R61sMrs5zE8EvT0WpETyWZ-koLgDcc0dl0XEe-kmC6UgTCcjtzSu_s-D0pJQTeSjbnGSkneVh2G4E1K9tSN-QH6eeGwKOmO5zPJIGYA5B2z1jZRwtjqEbKl9QD2KfZi8P0weLahsjYo6mza1DcG69kZA01S9S0UraAvUKKkuwRFD/s16000/Threat%20Actor%20Bypass%20SentinelOne%20EDR%20to%20Deploy%20Babuk%20Ransomware.webp?w=696&resize=696,0&ssl=1 "SentinelOne EDR")](https://i3.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMr8unloNU2GcehZp1R61sMrs5zE8EvT0WpETyWZ-koLgDcc0dl0XEe-kmC6UgTCcjtzSu_s-D0pJQTeSjbnGSkneVh2G4E1K9tSN-QH6eeGwKOmO5zPJIGYA5B2z1jZRwtjqEbKl9QD2KfZi8P0weLahsjYo6mza1DcG69kZA01S9S0UraAvUKKkuwRFD/s16000/Threat%20Actor%20Bypass%20SentinelOne%20EDR%20to%20Deploy%20Babuk%20Ransomware.webp?w=1600&resize=1600,900&ssl=1)

A sophisticated new attack method that disables endpoint security protection has been identified by security researchers, enabling threat actors to deploy ransomware undetected.

The technique, dubbed “Bring Your Own Installer,” was recently discovered by Aon’s Stroz Friedberg Incident Response team during an investigation of a [Babuk ransomware](https://cybersecuritynews.com/babuk-ransomware-group-claims-attack-on-orange/) attack.

The method exploits a vulnerability in SentinelOne’s agent upgrade process, allowing attackers to circumvent the EDR solution’s anti-tamper protection without requiring administrative console access or specialized tools.

## **How the Attack Works**

The bypass technique exploits a critical timing vulnerability during the SentinelOne agent update process, Aon’s Stroz Friedberg observed,

When installing a different version of the SentinelOne agent, the installer first terminates all associated Windows processes before overwriting existing files with the new version.

Attackers leverage this window of opportunity by:

[![google](https://thecybernews.com/csngoogle.svg
)](https://www.google.com/preferences/source?q=cybersecuritynews.com)

* Deploying legitimate signed SentinelOne installer files (such as SentinelOneInstaller\_windows\_64bit\_v23\_4\_4\_223.exe or SentinelInstaller\_windows\_64bit\_v23\_4\_6\_347.msi).
* Letting the installer terminate the running EDR processes.
* Forcibly terminating the Windows Installer (msiexec.exe) process before it can complete installation.
* Leaving the system in an unprotected state with no active [SentinelOne](https://cybersecuritynews.com/sentinelone-and-pingsafe/) processes.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeP-fVZKRA1ui1Vq62VS9vmnI7nskiI9Wxgx6dvALQED5hfRSfz_qgVtXUUusIOL4a111g9QV0P5J-ocp_a64_ecY1dpY01yGKznUMowDHmWf2r63p7W1LEKYT9GoolnxsPoSQSxg?key=JjYUCbjsGUOobtjBGydYKA)

Unlike other EDR bypass methods that rely on vulnerable drivers or third-party tools, this technique uses legitimate SentinelOne installers against themselves.

Forensic evidence includes EventID 93 with “CommandType: unload” as the last event in SentinelOne operational logs and EventID 1042 in Application logs showing “MsiInstaller Exited.”

Once EDR protection is disabled, attackers deploy Babuk ransomware, a sophisticated encryption malware that targets multiple platforms including [Windows and Linux](https://cybersecuritynews.com/new-rust-based-backdoor-attacking/). Babuk emerged in early 2020 and operates as a Ransomware-as-a-Service (RaaS) model.

Babuk uses AES-256 encryption to lock files on infected computers and attempts to terminate processes and services that might inhibit the encryption process. After encryption completes, it displays a ransom note with payment instructions.

## **Mitigation Steps**

SentinelOne responded promptly to Stroz Friedberg’s disclosure and issued guidance to customers in January 2025.

The critical mitigation is enabling the “Online Authorization” feature in SentinelOne’s Policy settings, which requires approval from the management console before any local upgrades, downgrades, or uninstalls can occur.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcnb3jrPTwTG6P5P_eZrzE-r-GUGMVAYHdPG7kKdI04tHoChDcHYKM8vY8pHtxG_wBI8q3PgoXjjsDl1RIBI5NQ3EUYs2Y8FDjNLVLC5GPiBZJIcar3gTKkxHcnt9gVr7yQq1rI?key=JjYUCbjsGUOobtjBGydYKA)

“The feature is turned off by default. At the end of the day, getting the word out to mitigate this bypass is the most important thing”, [warns Ailes](https://www.aon.com/en/insights/cyber-labs/bring-your-own-installer-bypassing-sentinelone).

SentinelOne has also shared this advisory with other major EDR vendors. Palo Alto Networks has confirmed its EDR solution is not affected by this attack method.

Stroz Friedberg advises organizations to:

* Enable the “Online Authorization” setting immediately.
* Monitor systems for unexpected SentinelOne version changes (EventID 1).
* Watch for multiple ProductVersion changes between different versions in short periods.
* Check event logs for the abrupt termination of SentinelOne services.

This discovery highlights the continued evolution of EDR bypass techniques and reinforces the need for organizations to properly configure security tools and maintain awareness of emerging threats targeting their [endpoint protection](https://cyber...