---
title: Warning “Educational” Octalyn Forensic Toolkit is a Dangerous Telegram-Controlled Credential Stealer
url: https://securityonline.info/warning-educational-octalyn-forensic-toolkit-is-a-dangerous-telegram-controlled-credential-stealer/
source: Instapaper: Unread
date: 2025-07-17
fetch_date: 2025-10-06T23:56:22.812823
---

# Warning “Educational” Octalyn Forensic Toolkit is a Dangerous Telegram-Controlled Credential Stealer

* About WordPress

  + [WordPress.org](https://wordpress.org/)
  + [Documentation](https://wordpress.org/documentation/)
  + [Learn WordPress](https://learn.wordpress.org/)
  + [Support](https://wordpress.org/support/forums/)
  + [Feedback](https://wordpress.org/support/forum/requests-and-feedback)

* Search

[Skip to content](#content)

October 6, 2025

* [Linkedin](https://www.linkedin.com/in/do-van-son-892a06265/)
* [Twitter](https://www.twitter.com/the_yellow_fall)
* [Facebook](https://www.facebook.com/DdoS-109131310571187/)
* [Youtube](https://www.youtube.com/c/penetrationtestingwithddos)

[Daily CyberSecurity](https://securityonline.info/)

Primary Menu

* [Home](https://securityonline.info)
* [CVE Watchtower](https://securityonline.info/cve-watchtower/)
* [Cyber Criminals](https://securityonline.info/category/news/cybercriminals/)
* [Data Leak](https://securityonline.info/category/news/dataleak/)
* [Linux](https://securityonline.info/category/linux/)
* [Malware](https://securityonline.info/category/news/malware/)
* [Vulnerability](https://securityonline.info/category/news/vulnerability/)
* [Submit Press Release](https://securityonline.info/submit-press-release/)
* [Vulnerability Report](https://securityonline.info/category/news/vulnerability-report/)

Search for:

* [Home](https://securityonline.info/)
* [News](https://securityonline.info/category/news/)
* [Malware](https://securityonline.info/category/news/malware/)
* [Warning: “Educational” Octalyn Forensic Toolkit is a Dangerous Telegram-Controlled Credential Stealer](https://securityonline.info/warning-educational-octalyn-forensic-toolkit-is-a-dangerous-telegram-controlled-credential-stealer/)

* [Malware](https://securityonline.info/category/news/malware/)

# Warning: “Educational” Octalyn Forensic Toolkit is a Dangerous Telegram-Controlled Credential Stealer

[![](https://secure.gravatar.com/avatar/1de822c030730109241bcb1f0d4f9c3fd1efd4da9ff33cb7dd85f8d3df417762?s=16&d=mm&r=g) Ddos](https://securityonline.info/author/ddos/)

July 16, 2025

![Credential Stealer, Octalyn Toolkit](https://securityonline.info/wp-content/uploads/2025/07/octalyn.png)

Researchers at Cyfirma have uncovered a disturbing example of how a so-called “educational” tool can cross the line into full-blown malware. Publicly hosted on GitHub, the Octalyn Forensic Toolkit is masquerading as a digital forensics utility but is, in reality, a modular credential stealer engineered for persistent data theft, silent execution, and Telegram-based command-and-control.

“*Despite its claimed educational intent, the toolkit functions as a full-fledged credential stealer*,” Cyfirma [states](https://www.cyfirma.com/research/octalyn-stealer-unmasked/), emphasizing that even low-skilled actors can wield it with ease.

[![CVE Watchtower](https://securityonline.info/wp-content/uploads/2025/09/721.png)](https://securityonline.info/CVE-WATCHTOWER)

Octalyn is made up of two key components:

* A Delphi-based builder with a friendly GUI for generating payloads
* A C++-written executable that acts as the actual stealer

To generate a malicious payload, an attacker simply enters a Telegram bot token and chat ID, enabling real-time data exfiltration via Telegram. From there, the malware:

* Silently extracts credentials from browsers, VPNs, Discord, Telegram, and gaming accounts
* Hunts for cryptocurrency wallets, capturing everything from private keys to wallet.dat files
* Establishes persistence using Startup folder shortcuts and registry Run keys
* Compresses stolen data and transmits it over encrypted channels to Telegram

Once deployed, Octalyn searches for common Chromium-based browser files and decrypts stored cookies, passwords, and autofill data. It even extracts bookmarks and browsing history to help attackers profile victims.

> “*All stolen credentials and system information are stored in an organized directory structure… Crypto wallets, VPN, Browsers, Discord, and others*.”

In its pursuit of financial data, Octalyn scans for wallets related to Bitcoin, Ethereum, Litecoin, Monero, and popular browser-based extensions like MetaMask and TronLink.

Each category is saved in a tidy subfolder, allowing attackers to quickly sort through and exploit the exfiltrated content.

Octalyn goes to great lengths to avoid detection and ensure longevity on a system:

* Startup folder persistence: Installs rvn.exe in the user’s Startup path
* Registry persistence: Adds itself to the HKCU\Run registry key
* Silent operation: Uses ShellExecuteA with SW\_HIDE to remain invisible to the user
* Secondary payload delivery: Employs Base64-encoded PowerShell to fetch additional malware from GitHub

“*The malware then constructs and executes a Base64-encoded PowerShell script… written in UTF-16LE format*,” Cyfirma notes, highlighting a rarely seen level of stealth and obfuscation.

At the time of analysis, the downloaded payload (winlogon.exe) wasn’t available, but the GitHub repository remained live, indicating future drops could be imminent.

Perhaps Octalyn’s most cunning feature is its use of Telegram as a command-and-control (C2) mechanism. This makes traffic analysis and detection much more difficult than with traditional HTTP-based malware.

> “*The malware establishes a secure connection over TLS to the Telegram API… transmitting a uniquely identifiable ZIP file name to indicate successful infection*.”

These ZIPs, named using the victim’s username, contain the stolen data in a structured format that attackers can immediately exploit.

“*Octalyn poses a serious threat if used outside controlled environments*,” Cyfirma warns.

### Related Posts:

* [Sophisticated Social Engineering Campaign Linked to Black Basta Ransomware](https://securityonline.info/sophisticated-social-engineering-campaign-linked-to-black-basta-ransomware/)
* [Lumma Stealer Malware Campaign Targets Educational Institutions with Deceptive PDF Lures](https://securityonline.info/lumma-stealer-malware-campaign-targets-educational-institutions-with-deceptive-pdf-lures/)
* [Zero-Click iMessage Alert: Paragon’s Graphite Spyware Exploits iOS Flaw, Targets Journalists](https://securityonline.info/zero-click-imessage-alert-paragons-graphite-spyware-exploits-ios-flaw-targets-journalists/)

Rate this post

### Found this helpful?

If this article helped you, please share it with others who might benefit.

Tags: [credential stealer](https://securityonline.info/tag/credential-stealer/) [cybersecurity](https://securityonline.info/tag/cybersecurity/) [digital forensics](https://securityonline.info/tag/digital-forensics/) [GitHub Threat](https://securityonline.info/tag/github-threat/) [info-stealer](https://securityonline.info/tag/info-stealer/) [malware](https://securityonline.info/tag/malware/) [Octalyn Forensic Toolkit](https://securityonline.info/tag/octalyn-forensic-toolkit/) [Telegram C2](https://securityonline.info/tag/telegram-c2/)

## Post navigation

[Previous: GLOBAL GROUP: New Ransomware Giant Emerges with AI Negotiators, Affiliate Incentives, and Industrial-Scale Attacks](https://securityonline.info/global-group-new-ransomware-giant-emerges-with-ai-negotiators-affiliate-incentives-and-industrial-scale-attacks/)

[Next: Warning: Fake Remittance Apps Target Bangladeshi Expats, Stealing IDs & Financial Data](https://securityonline.info/warning-fake-remittance-apps-target-bangladeshi-expats-stealing-ids-financial-data/)

### Leave a Reply [Cancel reply](/warning-educational-octalyn-forensic-toolkit-is-a-dangerous-telegram-controlled-credential-stealer/#respond)

Logged in as . Edit your profile. [Log out?](https://securityonline.info/wp-login.php?action=logout&redirect_to=https%3A%2F%2Fsecurityonline.info%2Fwarning-educational-octalyn-forensic-toolkit-is-a-dangerous-telegram-controlled-credential-stealer%2F&_wpnonce=e1be928a2a) Required fields are marked \*

Comment \*

## Search

[![CVE Watchtower](https://securityonline.info/wp-content/uploads/2025/09/CVE-Watchtower-1024x683.png)](htt...