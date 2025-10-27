---
title: New Auto Blocker in Samsung OneUI 6.1.1 Blocking APK Sideloading for Enhanced Security
url: https://securityonline.info/new-auto-blocker-in-samsung-oneui-6-1-1-blocking-apk-sideloading-for-enhanced-security/
source: Instapaper: Unread
date: 2024-07-27
fetch_date: 2025-10-06T17:45:16.542075
---

# New Auto Blocker in Samsung OneUI 6.1.1 Blocking APK Sideloading for Enhanced Security

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
* [Technology](https://securityonline.info/category/news/technology/)
* [New Auto Blocker in Samsung OneUI 6.1.1: Blocking APK Sideloading for Enhanced Security](https://securityonline.info/new-auto-blocker-in-samsung-oneui-6-1-1-blocking-apk-sideloading-for-enhanced-security/)

* [Technology](https://securityonline.info/category/news/technology/)

# New Auto Blocker in Samsung OneUI 6.1.1: Blocking APK Sideloading for Enhanced Security

[![](https://secure.gravatar.com/avatar/1de822c030730109241bcb1f0d4f9c3fd1efd4da9ff33cb7dd85f8d3df417762?s=16&d=mm&r=g) Ddos](https://securityonline.info/author/ddos/)

July 25, 2024

![Samsung Auto Blocker](https://securityonline.info/wp-content/uploads/2024/07/samsung-1283938_640.jpg)

Starting with OneUI 6.1.1, Samsung has [implemented](https://www.androidauthority.com/enable-sideloading-one-ui-6-1-1-3463446/) a default setting that blocks users from sideloading APK files. This setting is now applied to Samsung’s latest Android devices, even if the REQUEST\_INSTALL\_PACKAGES permission has been granted.

The Android system has already established a default mechanism at the operating system level to prevent users from sideloading APK files. The INSTALL\_PACKAGES permission, required to install applications without prompting the user, can only be granted to pre-installed app stores, such as Google Play.

[![CVE Watchtower](https://securityonline.info/wp-content/uploads/2025/09/721.png)](https://securityonline.info/CVE-WATCHTOWER)

Most third-party app stores that utilize the REQUEST\_INSTALL\_PACKAGES permission must also obtain user consent before installation. Even with this permission, Android prompts the user for confirmation each time a new application is installed.

In OneUI 6.1.1, Samsung has introduced the Auto Blocker feature, which entirely prevents the sideloading of applications from unauthorized sources, even if these sources have obtained the REQUEST\_INSTALL\_PACKAGES permission.

Naturally, Samsung’s own Galaxy Store does not require such confirmation. Both the Galaxy Store and Google Play have been granted permission to install applications without prompting the user by default.

For other third-party app stores or users attempting to sideload APK files, it is necessary to disable the Auto Blocker feature in OneUI settings. Even after disabling this feature, users still need to confirm installations from sources other than the Galaxy Store and Google Play, but at least they can install APK files as intended.

While further restricting the Android system may not be detrimental to most users, as Samsung likely aims to enhance [security](https://securityonline.info/CVE-WATCHTOWER) and prevent the installation of malware-laden applications, it is somewhat ironic that the open-source Android system is becoming increasingly closed by OEMs. This trend is not limited to Samsung; many Android OEMs are now finding ways to prevent users from installing applications from sources other than pre-installed app stores.

### Related Posts:

* [Python Developers Beware: Attackers Sneak Malware into Popular Package Manager](https://securityonline.info/python-developers-beware-attackers-sneak-malware-into-popular-package-manager/)
* [Samsung allegedly hit by hackers](https://securityonline.info/samsung-allegedly-hit-by-hackers/)
* [Quasar RAT: Stealthy Data Extraction via DLL Sideloading](https://securityonline.info/quasar-rat-stealthy-data-extraction-via-dll-sideloading/)

Rate this post

### Found this helpful?

If this article helped you, please share it with others who might benefit.

Tags: [android](https://securityonline.info/tag/android/) [Auto Blocker](https://securityonline.info/tag/auto-blocker/) [Galaxy Store](https://securityonline.info/tag/galaxy-store/) [Google Play](https://securityonline.info/tag/google-play/) [OneUI](https://securityonline.info/tag/oneui/) [OneUI 6.1.1](https://securityonline.info/tag/oneui-6-1-1/) [samsung](https://securityonline.info/tag/samsung/) [Samsung Auto Blocker](https://securityonline.info/tag/samsung-auto-blocker/) [sideloading APK](https://securityonline.info/tag/sideloading-apk/) [sideloading APK files](https://securityonline.info/tag/sideloading-apk-files/)

## Post navigation

[Previous: CVE-2024-37084 (CVSS 9.8): Remote code execution in Spring Cloud Data Flow](https://securityonline.info/cve-2024-37084-cvss-9-8-remote-code-execution-in-spring-cloud-data-flow/)

[Next: Acronis Cyber Infrastructure Users Urged to Patch Critical Vulnerability (CVE-2023-45249)](https://securityonline.info/acronis-cyber-infrastructure-users-urged-to-patch-critical-vulnerability-cve-2023-45249/)

### Leave a Reply [Cancel reply](/new-auto-blocker-in-samsung-oneui-6-1-1-blocking-apk-sideloading-for-enhanced-security/#respond)

Logged in as . Edit your profile. [Log out?](https://securityonline.info/wp-login.php?action=logout&redirect_to=https%3A%2F%2Fsecurityonline.info%2Fnew-auto-blocker-in-samsung-oneui-6-1-1-blocking-apk-sideloading-for-enhanced-security%2F&_wpnonce=1d5a2100cd) Required fields are marked \*

Comment \*

## Search

[![CVE Watchtower](https://securityonline.info/wp-content/uploads/2025/09/CVE-Watchtower-1024x683.png)](https://securityonline.info/daily-cybersecurity-launches-cve-watchtower-live-intelligence-for-a-faster-response/)

## Recent Zero-Day Vulnerabilities

* [Zero-Day PoC Published: Privilege Escalation Flaw in VMware Tools Used by Chinese APT](https://securityonline.info/zero-day-poc-published-privilege-escalation-flaw-in-vmware-tools-used-by-chinese-apt/)
* [PoC Exploit Details for Actively Exploited iOS Zero-Day Flaw Now Public](https://securityonline.info/poc-exploit-details-for-actively-exploited-zero-day-flaw-now-public/)
* [CRITICAL Cisco Zero-Day (CVE-2025-20333, CVSS 9.9) Under Active Attack: VPN Flaw Allows Root RCE](https://securityonline.info/critical-cisco-zero-day-cve-2025-20333-cvss-9-9-under-active-attack-vpn-flaw-allows-root-rce/)
* [Cisco Zero-Day CVE-2025-20362 Under Attack: VPN Flaw in ASA/FTD Exposes Restricted Resources](https://securityonline.info/cisco-zero-day-cve-2025-20362-under-attack-vpn-flaw-in-asa-ftd-exposes-restricted-resources/)
* [Two WordPress Core Vulnerabilities Disclosed Without Patch: Sensitive Data Exposure and Stored XSS](https://securityonline.info/two-wordpress-core-vulnerabilities-disclosed-without-patch-sensitive-data-exposure-and-stored-xss/)
* [Cisco SNMP Flaw (CVE-2025-20352) Actively Exploited: Patch Now to Stop Root Access!](https://securityonline.info/cisco-snmp-flaw-cve-2025-20352-actively-exploited-patch-now-to-stop-root-access/)

### 🎯 Supporter Goal

...