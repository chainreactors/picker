---
title: EagleMsgSpy Unmasking a Sophisticated Chinese Surveillance Tool
url: https://securityonline.info/eaglemsg-spyware-unmasking-a-sophisticated-chinese-surveillance-tool/
source: Instapaper: Unread
date: 2024-12-13
fetch_date: 2025-10-06T19:42:13.291397
---

# EagleMsgSpy Unmasking a Sophisticated Chinese Surveillance Tool

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
* [EagleMsgSpy: Unmasking a Sophisticated Chinese Surveillance Tool](https://securityonline.info/eaglemsg-spyware-unmasking-a-sophisticated-chinese-surveillance-tool/)

* [Data Leak](https://securityonline.info/category/news/dataleak/)
* [Malware](https://securityonline.info/category/news/malware/)

# EagleMsgSpy: Unmasking a Sophisticated Chinese Surveillance Tool

[![](https://secure.gravatar.com/avatar/1de822c030730109241bcb1f0d4f9c3fd1efd4da9ff33cb7dd85f8d3df417762?s=16&d=mm&r=g) Ddos](https://securityonline.info/author/ddos/)

December 12, 2024

![EagleMsgSpy Spyware Tool](https://securityonline.info/wp-content/uploads/2024/12/surveillance-5595451_1280.jpg)

Researchers at the Lookout Threat Lab have identified a sophisticated surveillance tool, dubbed EagleMsgSpy, reportedly used by law enforcement agencies in mainland China. The tool, operational since at least 2017, showcases advanced capabilities for extracting sensitive information from mobile devices.

The researchers [describe](https://www.lookout.com/threat-intelligence/article/eaglemsgspy-chinese-android-surveillanceware) EagleMsgSpy as a “*comprehensive mobile phone judicial monitoring product*,” designed to covertly monitor devices. According to the report, it *“**can obtain* *real-time mobile phone information of suspects through network control without the suspect’s knowledge, monitor all mobile phone activities of criminals and summarize them*.” Notably, this tool has variants targeting both Android and potentially iOS devices, though evidence of the latter remains undiscovered.

[![CVE Watchtower](https://securityonline.info/wp-content/uploads/2025/09/721.png)](https://securityonline.info/CVE-WATCHTOWER)

The installation process is particularly concerning, as it reportedly requires physical access to an unlocked device. An installer app delivers a “*headless*” payload, which operates silently in the background. The payload enables:

* Monitoring incoming notifications and intercepting messages from apps like QQ, WhatsApp, and Telegram.
* Capturing screenshots, audio recordings, and device activity via screen recording.
* Collecting detailed call logs, GPS locations, Wi-Fi connections, and browser bookmarks.
* Initiating real-time surveillance actions such as blocking calls or recording live audio.

Once collected, the data is stored in hidden directories on the device, compressed, and password-protected before being exfiltrated to command-and-control (C2) servers.

The Lookout team identified key infrastructure overlaps linking EagleMsgSpy to a Chinese technology company, Wuhan Chinasoft Token Information Technology Co., Ltd. (武汉中软通证信息技术有限公司). Their investigation uncovered significant evidence, including references to the company’s domain in promotional materials and C2 infrastructure.

Additionally, the administrative panel for EagleMsgSpy’s C2, labeled as a “Stability Maintenance Judgment System” (维稳研判系统), further underscores its use in law enforcement contexts. Publicly available contracts suggest similar systems are widely employed by Public [Security](https://securityonline.info/CVE-WATCHTOWER) Bureaus (PSBs) across China.

The report notes an evolution in obfuscation techniques, indicating active maintenance and enhancement of the tool. The researchers observed, “*This indicates that this surveillanceware is an actively maintained product whose creators make continuous efforts to protect it from discovery and analysis*.”

EagleMsgSpy’s connections to earlier Chinese surveillance tools, such as PluginPhantom and CarbonSteal, reveal a pattern of state-sponsored monitoring. Historical campaigns using these tools targeted ethnic minorities, including Uyghurs and Tibetans, raising concerns about potential human rights implications.

### Related Posts:

* [Driver Signature Enforcement Cracked: OS Downgrade Attacks Possible on Windows](https://securityonline.info/driver-signature-enforcement-cracked-os-downgrade-attacks-possible-on-windows/)
* [Synology Surveillance Station Vulnerabilities Expose Systems to Attack – Update Immediately](https://securityonline.info/synology-surveillance-station-vulnerabilities-expose-systems-to-attack-update-immediately/)
* [NSA can continue its surveillance will depend on Trump?](https://securityonline.info/nsa-can-continue-its-surveillance-will-depend-on-trump/)
* [Massive Illegal Streaming Network Dismantled in Europe-Wide Operation](https://securityonline.info/massive-illegal-streaming-network-dismantled-in-europe-wide-operation/)

Rate this post

### Found this helpful?

If this article helped you, please share it with others who might benefit.

Tags: [android](https://securityonline.info/tag/android/) [EagleMsg Spyware](https://securityonline.info/tag/eaglemsg-spyware/) [EagleMsgSpy](https://securityonline.info/tag/eaglemsgspy/)

## Post navigation

[Previous: CVE-2024-53677 (CVSS 9.5): Critical Vulnerability in Apache Struts Allows Remote Code Execution](https://securityonline.info/cve-2024-53677-critical-vulnerability-in-apache-struts-allows-remote-code-execution/)

[Next: Operation PowerOFF: Europol Cracks Down on Global DDoS-for-Hire Platforms](https://securityonline.info/operation-poweroff-europol-cracks-down-on-global-ddos-for-hire-platforms/)

### Leave a Reply [Cancel reply](/eaglemsg-spyware-unmasking-a-sophisticated-chinese-surveillance-tool/#respond)

Logged in as . Edit your profile. [Log out?](https://securityonline.info/wp-login.php?action=logout&redirect_to=https%3A%2F%2Fsecurityonline.info%2Feaglemsg-spyware-unmasking-a-sophisticated-chinese-surveillance-tool%2F&_wpnonce=1d5a2100cd) Required fields are marked \*

Comment \*

## Search

[![CVE Watchtower](https://securityonline.info/wp-content/uploads/2025/09/CVE-Watchtower-1024x683.png)](https://securityonline.info/daily-cybersecurity-launches-cve-watchtower-live-intelligence-for-a-faster-response/)

## Recent Zero-Day Vulnerabilities

* [Zero-Day PoC Published: Privilege Escalation Flaw in VMware Tools Used by Chinese APT](https://securityonline.info/zero-day-poc-published-privilege-escalation-flaw-in-vmware-tools-used-by-chinese-apt/)
* [PoC Exploit Details for Actively Exploited iOS Zero-Day Flaw Now Public](https://securityonline.info/poc-exploit-details-for-actively-exploited-zero-day-flaw-now-public/)
* [CRITICAL Cisco Zero-Day (CVE-2025-20333, CVSS 9.9) Under Active Attack: VPN Flaw Allows Root RCE](https://securityonline.info/critical-cisco-zero-day-cve-2025-20333-cvss-9-9-under-active-attack-vpn-flaw-allows-root-rce/)
* [Cisco Zero-Day CVE-2025-20...