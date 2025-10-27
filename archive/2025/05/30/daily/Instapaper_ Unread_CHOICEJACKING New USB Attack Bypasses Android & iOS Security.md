---
title: CHOICEJACKING New USB Attack Bypasses Android & iOS Security
url: https://securityonline.info/choicejacking-new-usb-attack-bypasses-android-ios-security/
source: Instapaper: Unread
date: 2025-05-30
fetch_date: 2025-10-06T22:29:08.645022
---

# CHOICEJACKING New USB Attack Bypasses Android & iOS Security

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
* [CHOICEJACKING: New USB Attack Bypasses Android & iOS Security](https://securityonline.info/choicejacking-new-usb-attack-bypasses-android-ios-security/)

* [Malware](https://securityonline.info/category/news/malware/)

# CHOICEJACKING: New USB Attack Bypasses Android & iOS Security

[![](https://secure.gravatar.com/avatar/1de822c030730109241bcb1f0d4f9c3fd1efd4da9ff33cb7dd85f8d3df417762?s=16&d=mm&r=g) Ddos](https://securityonline.info/author/ddos/)

May 29, 2025

![choice](https://securityonline.info/wp-content/uploads/2025/05/choice.png)

A decade after the original “JuiceJacking” threat prompted mobile operating systems to require user consent for USB data connections, researchers from Graz University of Technology have uncovered a new class of USB-based attacks that bypass these protections. Their study, presented at USENIX, introduces CHOICEJACKING — a powerful, stealthy family of attacks that compromise Android and iOS devices using seemingly harmless chargers.

“We present a novel family of USB-based attacks on mobile devices, CHOICEJACKING, which is the first to bypass existing JuiceJacking mitigations,” the authors [write](https://graz.elsevierpure.com/en/publications/choicejacking-compromising-mobile-devices-through-malicious-charg).

[![CVE Watchtower](https://securityonline.info/wp-content/uploads/2025/09/721.png)](https://securityonline.info/CVE-WATCHTOWER)

CHOICEJACKING attacks exploit a core design [flaw](https://securityonline.info/CVE-WATCHTOWER) in current JuiceJacking countermeasures: the assumption that attackers cannot inject user input to approve data connections. The researchers show that this assumption no longer holds — malicious chargers can simulate user interaction and gain unauthorized access to personal data and even execute code on the device.

These attacks combine characteristics of USB hosts (which initiate data transfers) and peripherals (which simulate input like keyboards or mice), creating a hybrid threat model that evades existing defenses.

![CHOICEJACKING USB attack](https://securityonline.info/wp-content/uploads/2025/05/USB.png)

The study outlines three attack vectors:

* AOAP Exploit (T1): Leverages [flaws](https://securityonline.info/CVE-WATCHTOWER) in the Android Open Accessory Protocol to inject input events and approve USB data connections autonomously.
* Race Condition Exploit (T2): Abuses a timing issue in Android’s input subsystem to queue input events that accept prompts before the user sees them.
* Bluetooth Bridge (T3): Pairs a Bluetooth input device through USB and uses it to approve access — affecting both Android and iOS.

“*In our evaluation, this technique allows gaining file access on all Android devices*,” the paper confirms about T1.

The research team tested 11 devices from 8 major vendors — including Samsung, Xiaomi, Huawei, Oppo, Vivo, Honor, Google, and Apple — and found all were vulnerable. Some attacks succeeded even when the screen was locked.

“*All but one (including Google, Samsung, Xiaomi, and Apple) acknowledged our attacks and are in the process of integrating mitigations*,” the authors reported.

Notably, Xiaomi devices were found to be particularly vulnerable, allowing ADB-level access even on non-development-enabled devices, opening the door for persistent compromise.

Some of the attacks are almost unnoticeable. The fastest technique took just 133 milliseconds, less than the duration of a human blink. This brief flicker is often invisible to users distracted during calls, watching videos, or navigating.

To further boost stealth, the team developed a power line side-channel method to detect when the device is unobserved (like during a call) — perfect timing to launch the attack silently.

“*We conclude that the CNN allows determining when the user is in a phone call*,” the paper states regarding their machine learning-based detection model.

Current protections like lock screen-only USB blocking or USB data blockers are no longer sufficient. The researchers advocate for user prompts for all USB access types, including peripherals and accessories, to ensure that malicious input can’t be injected without the user’s knowledge.

“*CHOICEJACKING represents a primitive for obtaining access to users’ private files stored on the mobile device*,” the study warns.

### Related Posts:

* [EV Fast Chargers Vulnerable to Remote Hacking, Study Finds](https://securityonline.info/ev-fast-chargers-vulnerable-to-remote-hacking-study-finds/)
* [Security Expert Announces PoC to Crashes All Recent Windows](https://securityonline.info/security-expert-announces-poc-to-crashes-all-recent-windows/)

Rate this post

### Found this helpful?

If this article helped you, please share it with others who might benefit.

[security](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fsecurityonline.info%2Fchoicejacking-new-usb-attack-bypasses-android-ios-<a href=)%2F" target="\_blank" rel="nofollow" aria-label="Facebook">

Tags: [android](https://securityonline.info/tag/android/) [CHOICEJACKING](https://securityonline.info/tag/choicejacking/) [ios](https://securityonline.info/tag/ios/) [JuiceJacking](https://securityonline.info/tag/juicejacking/) [mobile security](https://securityonline.info/tag/mobile-security/) [security](https://securityonline.info/tag/security/) [usb](https://securityonline.info/tag/usb/) [Vulnerability](https://securityonline.info/tag/vulnerability/)

## Post navigation

[Previous: Ransomware Attack: MSP’s RMM Tool Abused to Spread DragonForce](https://securityonline.info/ransomware-attack-msps-rmm-tool-abused-to-spread-dragonforce/)

[Next: Stealthy Attacks: Silent Werewolf Deploys Custom Loaders in Espionage Operations](https://securityonline.info/stealthy-attacks-silent-werewolf-deploys-custom-loaders-in-espionage-operations/)

### Leave a Reply [Cancel reply](/choicejacking-new-usb-attack-bypasses-android-ios-security/#respond)

Logged in as . Edit your profile. [Log out?](https://securityonline.info/wp-login.php?action=logout&redirect_to=https%3A%2F%2Fsecurityonline.info%2Fchoicejacking-new-usb-attack-bypasses-android-ios-security%2F&_wpnonce=e1be928a2a) Required fields are marked \*

Comment \*

## Search

[![CVE Watchtower](https://securityonline.info/wp-content/uploads/2025/09/CVE-Watchtower-1024x683.png)](https://securityonline.info/daily-cybersecurity-launches-cve-watchtower-live-intelligence-for-a-faster-response/)

## Recent Zero-Day Vulnerabilities

* [Zero-Day PoC Published: Privilege Escalation Flaw in VMware Tools Used by Chinese APT](htt...