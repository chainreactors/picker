---
title: Banking Trojan TrickMo Compromised 13,000 Devices, Now Steals Device Unlock Patterns and PINs
url: https://securityonline.info/banking-trojan-trickmo-compromised-13000-devices-now-steals-device-unlock-patterns-and-pins/
source: Instapaper: Unread
date: 2024-10-15
fetch_date: 2025-10-06T18:55:41.711356
---

# Banking Trojan TrickMo Compromised 13,000 Devices, Now Steals Device Unlock Patterns and PINs

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
* [Banking Trojan TrickMo Compromised 13,000 Devices, Now Steals Device Unlock Patterns and PINs](https://securityonline.info/banking-trojan-trickmo-compromised-13000-devices-now-steals-device-unlock-patterns-and-pins/)

* [Malware](https://securityonline.info/category/news/malware/)

# Banking Trojan TrickMo Compromised 13,000 Devices, Now Steals Device Unlock Patterns and PINs

[![](https://secure.gravatar.com/avatar/1de822c030730109241bcb1f0d4f9c3fd1efd4da9ff33cb7dd85f8d3df417762?s=16&d=mm&r=g) Ddos](https://securityonline.info/author/ddos/)

October 13, 2024

![TrickMo Banking Trojan](https://securityonline.info/wp-content/uploads/2024/10/fake-unlocking-UI.webp)

Fake unlocking UI | Image: Zimperium

Aazim Yaswant, a Malware Analyst at Zimperium, has published a comprehensive analysis of the latest TrickMo samples, revealing alarming new capabilities in this banking trojan. Originally disclosed by Cleafy in early September, this new variant of TrickMo employs techniques designed to evade detection and analysis, including obfuscation and zip file manipulation. Yaswant’s team identified a staggering 40 variants of TrickMo, consisting of 16 droppers and 22 active Command and Control (C2) servers, many of which remain undetected by the broader [security](https://securityonline.info/CVE-WATCHTOWER) community.

While TrickMo’s core capabilities remain focused on banking credential theft, Yaswant’s analysis uncovered more advanced functionalities. “*These capabilities enable the malware to effectively access any type of information stored on the device*,” Yaswant [explains](https://www.zimperium.com/blog/expanding-the-investigation-deep-dive-into-latest-trickmo-samples/). This includes OTP interception, screen recording, remote control, data exfiltration, and abuse of accessibility services to automatically grant permissions and execute actions without user consent. Moreover, TrickMo can display deceptive overlays to steal credentials and facilitate unauthorized financial transactions.

[![CVE Watchtower](https://securityonline.info/wp-content/uploads/2025/09/721.png)](https://securityonline.info/CVE-WATCHTOWER)

![](https://securityonline.info/wp-content/uploads/2024/10/deceptive-overlays-1024x516.webp)

Deceptive overlays | Image: Zimperium

One of the more concerning findings in Yaswant’s analysis is a newly discovered feature in some of the TrickMo variants: the ability to steal the device’s unlock pattern or PIN. This functionality allows attackers to bypass the lock screen and operate on the device even while it is secured. The malware achieves this by displaying a deceptive user interface that mimics the legitimate unlock screen. “*When the user enters their unlock pattern or PIN, the page transmits the captured PIN or pattern details, along with a unique device identifier*,” Yaswant notes.

Zimperium’s team was able to gain access to several C2 servers, discovering approximately 13,000 unique IP addresses linked to victims of the malware. The analysis revealed that TrickMo primarily targets regions such as Canada, the United Arab Emirates, Turkey, and Germany. Yaswant’s investigation uncovered millions of compromised records, with the stolen credentials extending beyond banking information to include access to corporate VPNs and internal websites. This underscores the critical risk posed to organizations, as compromised mobile devices can serve as entry points for larger cyberattacks.

### Related Posts:

* [Beware the New TrickMo Banking Trojan: Enhanced Features, Increased Danger](https://securityonline.info/beware-the-new-trickmo-banking-trojan-enhanced-features-increased-danger/)
* [Attacker use DDoS attack to hit three major Dutch banks](https://securityonline.info/attacker-use-ddos-attack-to-hit-three-major-dutch-banks/)
* [Stealthy New Android Trojan Disguised as Popular Apps Steals Your Data](https://securityonline.info/stealthy-new-android-trojan-disguised-as-popular-apps-steals-your-data/)

Rate this post

### Found this helpful?

If this article helped you, please share it with others who might benefit.

Tags: [Banking Trojan TrickMo](https://securityonline.info/tag/banking-trojan-trickmo/) [TrickMo](https://securityonline.info/tag/trickmo/)

## Post navigation

[Previous: Thousands of Fortinet Devices Remain Exposed to RCE CVE-2024-23113 Vulnerability](https://securityonline.info/thousands-of-fortinet-devices-remain-exposed-to-rce-cve-2024-23113-vulnerability/)

[Next: GitHub Enterprise Server Patches Critical Security Flaw – CVE-2024-9487 (CVSS 9.5)](https://securityonline.info/github-enterprise-server-patches-critical-security-flaw-cve-2024-9487-cvss-9-5/)

### Leave a Reply [Cancel reply](/banking-trojan-trickmo-compromised-13000-devices-now-steals-device-unlock-patterns-and-pins/#respond)

Logged in as . Edit your profile. [Log out?](https://securityonline.info/wp-login.php?action=logout&redirect_to=https%3A%2F%2Fsecurityonline.info%2Fbanking-trojan-trickmo-compromised-13000-devices-now-steals-device-unlock-patterns-and-pins%2F&_wpnonce=1d5a2100cd) Required fields are marked \*

Comment \*

## Search

[![CVE Watchtower](https://securityonline.info/wp-content/uploads/2025/09/CVE-Watchtower-1024x683.png)](https://securityonline.info/daily-cybersecurity-launches-cve-watchtower-live-intelligence-for-a-faster-response/)

## Recent Zero-Day Vulnerabilities

* [Zero-Day PoC Published: Privilege Escalation Flaw in VMware Tools Used by Chinese APT](https://securityonline.info/zero-day-poc-published-privilege-escalation-flaw-in-vmware-tools-used-by-chinese-apt/)
* [PoC Exploit Details for Actively Exploited iOS Zero-Day Flaw Now Public](https://securityonline.info/poc-exploit-details-for-actively-exploited-zero-day-flaw-now-public/)
* [CRITICAL Cisco Zero-Day (CVE-2025-20333, CVSS 9.9) Under Active Attack: VPN Flaw Allows Root RCE](https://securityonline.info/critical-cisco-zero-day-cve-2025-20333-cvss-9-9-under-active-attack-vpn-flaw-allows-root-rce/)
* [Cisco Zero-Day CVE-2025-20362 Under Attack: VPN Flaw in ASA/FTD Exposes Restricted Resources](https://securityonline.info/cisco-zero-day-cve-2025-20362-under-attack-vpn-flaw-in-asa-ftd-exposes-restricted-resources/)
* [Two WordPress Core Vulnerabilities Disclosed Without Patch: Sensitive Data Exposure and Stored XSS](https://securityonline.info/two-wordpress-core-vulnerabilities-disclosed-without-patch-sensitive-data-exposure-and-stored-xss/)
* [Cisco SNMP Flaw (CVE-2025-20352) Actively Exploited: Patch Now to Stop Root Access!](https://securityonline.info/cisco-snmp...