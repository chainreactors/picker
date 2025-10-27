---
title: Evolution of Tycoon 2FA Defense Evasion Mechanisms: Analysis and Timeline
url: https://any.run/cybersecurity-blog/tycoon2fa-evasion-analysis/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-14
fetch_date: 2025-10-06T22:30:46.263203
---

# Evolution of Tycoon 2FA Defense Evasion Mechanisms: Analysis and Timeline

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2020/07/Logo-1.png)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and Tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Raccoon Stealer 2.0 Malware analysis](/cybersecurity-blog/raccoon-stealer-v2-malware-analysis/)
  + [How to Get Free Malware Samples and Reports](/cybersecurity-blog/free-malware-samples-reports/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2020/07/Logo-1.png)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and Tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Raccoon Stealer 2.0 Malware analysis](/cybersecurity-blog/raccoon-stealer-v2-malware-analysis/)
  + [How to Get Free Malware Samples and Reports](/cybersecurity-blog/free-malware-samples-reports/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2022/10/mini-logo.png)](/cybersecurity-blog/)

* + Search

![Evolution of Tycoon 2FA Defense Evasion Mechanisms: Analysis and Timeline](/cybersecurity-blog/wp-content/uploads/2025/05/tycoon_blog.png)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# Evolution of Tycoon 2FA Defense Evasion Mechanisms: Analysis and Timeline

May 13, 2025

[Add comment](#comments-13375)
7786 views
18 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Evolution of Tycoon 2FA Defense Evasion Mechanisms: Analysis and Timeline

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1617
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3164
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3182
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Evolution of Tycoon 2FA Defense Evasion Mechanisms: Analysis and Timeline

Attackers keep improving ways to avoid being caught, making it harder to detect and investigate their attacks. The Tycoon 2FA phishing kit is a clear example, as its creators regularly add new tricks to bypass detection systems.

In this study, we’ll take a closer look at how Tycoon 2FA’s anti-detection methods have changed over the past several months and suggest ways to spot them effectively.

This article will discuss:

* A review of old and new anti-detection techniques.

* How the new tricks compared to the old ones.

* Tips for spotting these early.

Knowing how attackers dodge detection and keeping user detection rules up to date are key to fighting these anti-detection methods.

## What is Tycoon 2FA

Tycoon 2FA is a modern [Phishing-as-a-Service (PhaaS)](https://any.run/cybersecurity-blog/how-to-track-phishkits/) platform designed to bypass two-factor authentication (2FA) for Microsoft 365 and Gmail. It was first identified by [Sekoia](https://www.bleepingcomputer.com/news/security/new-mfa-bypassing-phishing-kit-targets-microsoft-365-gmail-accounts/) analysts in October 2023, though the Saad Tycoon group, which promotes this tool through private Telegram channels, has been active since August 2023.

Tycoon 2FA uses an Adversary-in-the-Middle (AiTM) approach, where attackers set up a phishing page through a reverse proxy server. After a user enters their credentials and completes the 2FA process, the server captures session cookies, allowing attackers to reuse the session and bypass security measures.

Currently, Tycoon 2FA is highly popular and widely used by cybercriminals, including the Saad Tycoon group. The platform offers ready-made phishing pages and an easy-to-use admin panel, making it accessible even to less technically skilled attackers.

Discover the latest examples of Tycoon 2FA attacks using this search query in [ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=tycoon2fa_evasion&utm_term=130525&utm_content=linktolanding)’s [Threat Intelligence Lookup](https://any.run/cybersecurity-blog/introducing-any-run-threat-intelligence-lookup/):

[threatName:”Tycoon”](https://intelligence.any.run/analysis/lookup/?utm_source=anyrunblog&utm_medium=article&utm_campaign=tycoon2fa_evasion&utm_term=130525&utm_content=linktotiplans#%7B%2522query%2522:%2522threatName:%255C%2522Tycoon%255C%2522%2522,%2522dateRange%2522:180%7D)

In 2024, an updated version of Tycoon 2FA was released, featuring enhanced evasion techniques, including dynamic code generation, obfuscation, and traffic filtering to block bots. Phishing emails are now frequently sent from legitimate, potentially compromised email addresses.

The evolution of this phishing kit continues, with ANY.RUN researchers [noting regular updates and new evasion mechanisms](https://x.com/anyrun_app/status/1914999622881235340) in its malicious software. This article aims to investigate and provide technical details on how Tycoon 2FA has evolved, is evolving, and may continue to evolve.

### Before We Begin

Tune in to [ANY.RUN’s live webinar](https://anyrun.webinargeek.com/how-soc-teams-save-time-and-effort-with-any-run-action-plan?cst=blog) on Wednesday, May 14 | 3:00 PM GMT. We welcome **heads of SOC teams, managers, and security specialists** of different tiers who want to:

* Solve common security issues
* Optimize their work processes
* Find out how to save company’s resources

[Sign up for webinar →](https://anyrun.webinargeek.com/how-soc-teams-save-time-and-effort-with-any-run-action-plan?cst=blog)

## Analysis of a Tycoon2FA Attack from 01.10.2024

Let’s begin the analysis with a typical Tycoon2FA attack observed in October of 2024. The attack starts with a malicious URL and employs multiple evasion techniques to avoid detection. Below, we well break down each stage of the attack, highlighting its protective mechanisms and their purposes.

[View s...