---
title: UAT-10147 Uses AI to Scale Server Attacks, Deploys SPECTRE With EDR Bypass and Linux Rootkit
url: https://thehackernews.com/2026/08/uat-10147-uses-ai-to-scale-server.html
source: The Hacker News
date: 2026-08-24
fetch_date: 2026-08-25T03:00:41.645016
---

# UAT-10147 Uses AI to Scale Server Attacks, Deploys SPECTRE With EDR Bypass and Linux Rootkit

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [UAT-10147 Uses AI to Scale Server Attacks, Deploys SPECTRE With EDR Bypass and Linux Rootkit](https://thehackernews.com/2026/08/uat-10147-uses-ai-to-scale-server.html)

**Ravie Lakshmanan**Aug 24, 2026Cybercrime / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4-mx98ENuq77sCTBd49TSl4Ov5dD1Wua0Vf1MiyVVPfcFckY__TjnTEOeC5CIQWX4L_OLA-xZHHY5nAlp926SIpa3eK8Tvfw1HSHHK1GMot7noTz4Cg36t-ZuZ-NUh5mnsfzs0HJ8F7p410LgWFVPN39PYh8YR6qkDlE8duNKmKpOtJHW4NA9T_ddTGLp/s1700-e365/hackers.jpg)

Cybersecurity researchers have disclosed details of a Chinese-speaking cybercrime group dubbed **UAT-10147** that's targeting Windows and Linux web servers globally across the education, media, technology, and gaming sectors.

The vast majority of the targets are located in Brazil, Bolivia, China, Canada, and Vietnam. Details of the threat activity came to light following the discovery of an open directory hosted at "139.180.197[.]150," which was observed communicating with one of the compromised machines.

"The actor leveraged publicly disclosed vulnerabilities to gain initial access at scale," Cisco Talos [said](https://blog.talosintelligence.com/uat-10147-chinese-speaking-adversary-integrates-agentic-ai-into-post-compromise-operations/) in a two-part report published last week. The actor employed a mixture of open-source offensive frameworks, including [Metasploit](https://docs.metasploit.com/), [ysoserial](https://github.com/pwntester/ysoserial.net), [PentestGPT](https://pentestgpt.com/), DeepAudit, and multiple privilege escalation exploits to automate intrusion operations and establish persistence."

UAT-10147 has been described as a threat actor that conducts search engine optimization (SEO) fraud and data theft, while integrating artificial intelligence (AI)-powered tools at various phases of the attack cycle to facilitate exploitation, reconnaissance, payload generation, validation, and persistence.

Specifically, this involves using AI to refine exploits, troubleshoot logic, automate post-exploitation workflows, validate exploits, and generate operational documentation, indicating an attempt to implement offensive tradecraft at scale.

An analysis of the exposed directory has identified a text file containing a target list with approximately 170,000 URLs, with the attacker splitting it into 17 smaller files containing about 10,000 URLs each to more efficiently parse the set. The top five destinations based on the target list consist of the U.S., India, the U.K., Germany, and the Netherlands.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

Attack chains involve exploiting known flaws to achieve remote code execution (RCE) on a website or a vulnerable IIS server, and then run an automated script to install and deploy malware for SEO fraud or data stealing. Select instances entail the deployment of a web shell, which then paves the way for [BadIIS](https://thehackernews.com/2026/01/china-linked-uat-8099-targets-iis.html) and additional backdoors for persistent access.

Some of the other steps undertaken by UAT-10147 is as follows -

* Using a batch script that employs certutil to download a privilege escalation tool ("EfsPotato"), a secondary batch script, and Quasar RAT from a remote server ("adminapi.tippusoni[.]in")
* Using EfsPotato to gain elevated system privileges, configure Microsoft Defender exclusions
* Deleting initial payloads to cover its tracks and thwart forensic analysis
* Deploying follow-on implants like [Gh0stCringe](https://thehackernews.com/2025/06/silver-fox-apt-targets-taiwan-with.html) and a previously unreported cross-platform implant dubbed SPECTRE
* Using the secondary batch script to silently execute Quasar RAT and establish persistence using a deceptive scheduled task named "Google Chrome Start"
* Abusing the elevated privileges to download a third batch script, which then installs BadIIS

Interestingly, the core BadIIS malware is the same specific variant that's known to operate under a [malware-as-a-service (MaaS) model](https://thehackernews.com/2026/05/webworm-deploys-echocreep-and-graphworm.html) and is used by multiple Chinese-speaking cybercrime groups.

The Linux attacks, like in the case, leverage various known vulnerabilities to obtain an initial foothold, followed by abusing various known Local Privilege Escalation (LPE) exploits to escalate to root, including [CVE-2022-0995](https://nvd.nist.gov/vuln/detail/CVE-2022-0995), [CVE-2021-3156](https://nvd.nist.gov/vuln/detail/CVE-2021-3156), [CVE-2015-5287](https://nvd.nist.gov/vuln/detail/CVE-2015-5287), [CVE-2015-3246](https://nvd.nist.gov/vuln/detail/CVE-2015-3246), [CVE-2010-3904](https://nvd.nist.gov/vuln/detail/CVE-2010-3904), and [CVE-2022-0847](https://nvd.nist.gov/vuln/detail/CVE-2022-0847).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjOWr-aSd1GVNHaWHvMP4kHa7b1iC8U489bAzw0EzbNNqIaGg_PPL46vE7HqEfBosifkZtlpoPIbR2oW4u6qfZdQX29Y9Tb7GiRXLWVjPNue9Ec47tqxRhHC1abM4c01uBlIYIb9nyw09d7t1cmicaLcy7JkOgCYlcfNzFY4wxmnCbSz-Ga4MpiRnCAqf6U/s1700-e365/iis.jpg)

Once root-level access is unlocked, the threat actor has been observed deploying multiple backdoors like [Noodle RAT](https://thehackernews.com/2024/06/new-cross-platform-malware-noodle-rat.html) (a variant of Gh0st RAT and Rekoobe), SPECTRE, and Meterpreter to enable outbound connections to remote command-and-control (C2) infrastructure. Some of the vulnerabilities weaponized by the threat actor over the course of the campaign include [CVE-2022-27925](https://nvd.nist.gov/vuln/detail/CVE-2022-27925) (Zimbra), [CVE-2021-23758](https://nvd.nist.gov/vuln/detail/CVE-2021-23758) (AjaxPro), [CVE-2019-18935](https://nvd.nist.gov/vuln/detail/cve-2019-18935) (Telerik UI for ASP.NET AJAX), [CVE-2021-29441](https://nvd.nist.gov/vuln/detail/CVE-2021-29441), and [CVE-2021-29442](https://nvd.nist.gov/vuln/detail/CVE-2021-29442) (Alibaba Nacos).

"By routing ex...