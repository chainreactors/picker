---
title: Windows Event Logs A Key to Unmasking Human-Operated Ransomware
url: https://securityonline.info/windows-event-logs-a-key-to-unmasking-human-operated-ransomware/
source: Instapaper: Unread
date: 2024-10-02
fetch_date: 2025-10-06T18:58:58.525230
---

# Windows Event Logs A Key to Unmasking Human-Operated Ransomware

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
* [Windows Event Logs: A Key to Unmasking Human-Operated Ransomware](https://securityonline.info/windows-event-logs-a-key-to-unmasking-human-operated-ransomware/)

* [Malware](https://securityonline.info/category/news/malware/)

# Windows Event Logs: A Key to Unmasking Human-Operated Ransomware

[![](https://secure.gravatar.com/avatar/1de822c030730109241bcb1f0d4f9c3fd1efd4da9ff33cb7dd85f8d3df417762?s=16&d=mm&r=g) Ddos](https://securityonline.info/author/ddos/)

September 30, 2024

![Windows Event Logs](https://securityonline.info/wp-content/uploads/2024/09/Event-logs-confirmed-during-Bisamware-execution.png)

Event logs confirmed during Bisamware execution | Image: JPCERT/CC

Human-operated ransomware represents a particularly insidious challenge, combining sophisticated techniques with manual execution to evade traditional [security](https://securityonline.info/CVE-WATCHTOWER) measures. A new [report](https://blogs.jpcert.or.jp/en/2024/09/windows.html) from the Japan Computer Emergency Response Team Coordination Center (JPCERT/CC) illuminates the potential of Windows Event Logs as a potent tool in the fight against this evolving threat.

Unlike automated ransomware attacks, human-operated ransomware leverages the expertise of skilled threat actors who navigate victim networks, exfiltrating data and strategically deploying encryption. This hands-on approach allows attackers to bypass standard [security](https://securityonline.info/CVE-WATCHTOWER) defenses, necessitating advanced detection and response capabilities.

[![CVE Watchtower](https://securityonline.info/wp-content/uploads/2025/09/721.png)](https://securityonline.info/CVE-WATCHTOWER)

The JPCERT/CC report underscores the value of Windows Event Logs as a source of crucial forensic evidence. By examining event log patterns, security professionals can identify and attribute human-operated ransomware, aiding in timely containment and mitigation efforts.

* **Conti Ransomware**

First identified in 2020, Conti ransomware is notorious for exploiting Windows Restart Manager to facilitate file encryption. A large number of event logs (Event IDs: 10000, 10001) are generated in a short span when Conti is executed, providing a clear indication of its presence on a compromised machine. Interestingly, ransomware variants like Akira and Lockbit 3.0, which share similarities with Conti, also generate similar event logs.

* **Phobos Ransomware**

Phobos, a variant of the Dharma ransomware, leaves a trail of destruction by deleting system backup catalogs and volume shadow copies. Notably, it generates Event IDs such as 612 and 524 during execution, which can be used to track its activities. Other ransomware like 8base and Elbie exhibit similar behavior, potentially linked to the Phobos ransomware group.

* **Midas Ransomware**

Midas, identified in 2021, leaves event logs related to changes in network settings during its execution. For example, Event ID 7040 records modifications to network service configurations, such as SSDP Discovery and UPnP Device Host, which are essential for spreading the ransomware across a network. Axxes ransomware, suspected to be a variant of Midas, shows similar traits.

* **BadRabbit Ransomware**

First confirmed in 2017, BadRabbit ransomware’s execution is marked by Event ID 7045, which logs the installation of the encryption component cscc.dat. This log can be a telling sign of a BadRabbit infection, helping investigators trace the attack’s origin.

* **Bisamware Ransomware**

Discovered in 2022, Bisamware takes advantage of [vulnerabilities](https://securityonline.info/CVE-WATCHTOWER) in Microsoft tools to infect Windows users. When this ransomware is executed, Event IDs 1040 and 1042 log the start and end of the Windows Installer transaction, providing concrete evidence of Bisamware activity.

JPCERT/CC also discovered event log traces common across multiple ransomware strains. For instance, ransomware like GandCrab, AKO, and BLACKBASTA often leave behind Event IDs 13 and 10016 when they fail to access COM server applications tied to the Volume Shadow Copy Service.

This recurring pattern suggests that even when ransomware doesn’t function as intended, the event logs can still reveal critical insights, making them an essential asset in damage investigations and ransomware attribution.

The report emphasizes that Windows Event Logs should not be overlooked in ransomware investigations. While event logs alone may not provide a complete picture, they can offer valuable clues when traditional identification methods, like ransom notes or encrypted file extensions, fall short.

By analyzing these logs, security teams can detect ransomware traces early, potentially reducing downtime and financial impact. Moreover, with the rise of new ransomware variants, these logs can help professionals keep pace with attackers’ evolving tactics.

### Related Posts:

* [Conti ransomware source code leaks](https://securityonline.info/conti-ransomware-source-code-leaks/)
* [ZeroLogon to NoPac Vulnerability: Black Basta Group’s Exploit Arsenal Revealed](https://securityonline.info/zerologon-to-nopac-vulnerability-black-basta-groups-exploit-arsenal-revealed/)
* [Google ban fake ID apps on Play Store](https://securityonline.info/google-ban-fake-id-apps-on-play-store/)

Rate this post

### Found this helpful?

If this article helped you, please share it with others who might benefit.

Tags: [AKO](https://securityonline.info/tag/ako/) [BadRabbit Ransomware](https://securityonline.info/tag/badrabbit-ransomware/) [Bisamware Ransomware](https://securityonline.info/tag/bisamware-ransomware/) [BlackBasta](https://securityonline.info/tag/blackbasta/) [Conti ransomware](https://securityonline.info/tag/conti-ransomware/) [GandCrab](https://securityonline.info/tag/gandcrab/) [Midas Ransomware](https://securityonline.info/tag/midas-ransomware/) [Windows Event Logs](https://securityonline.info/tag/windows-event-logs/)

## Post navigation

[Previous: KartLANPwn (CVE-2024-45200) Exploits Mario Kart 8 Deluxe LAN Play Feature for RCE](https://securityonline.info/kartlanpwn-cve-2024-45200-exploits-mario-kart-8-deluxe-lan-play-feature-for-rce/)

[Next: CISA Adds Four Actively Exploited Vulnerabilities to KEV Catalog](https://securityonline.info/cisa-adds-four-actively-exploited-vulnerabilities-to-kev-catalog/)

### Leave a Reply [Cancel reply](/windows-event-logs-a-key-to-unmasking-human-operated-ransomware/#respond)

Logged in as . Edit your profile. [Log out?](https://securityonline.info/wp-login....