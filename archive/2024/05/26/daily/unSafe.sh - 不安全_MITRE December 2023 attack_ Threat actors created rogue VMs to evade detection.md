---
title: MITRE December 2023 attack: Threat actors created rogue VMs to evade detection
url: https://buaq.net/go-241558.html
source: unSafe.sh - 不安全
date: 2024-05-26
fetch_date: 2025-10-06T16:49:08.659816
---

# MITRE December 2023 attack: Threat actors created rogue VMs to evade detection

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

MITRE December 2023 attack: Threat actors created rogue VMs to evade detection

MITRE December 2023 attack: Threat actors created rogue VMs to evade detectionThe MITRE Corpor
*2024-5-25 17:51:2
Author: [securityaffairs.com(查看原文)](/jump-241558.htm)
阅读量:14
收藏*

---

## MITRE December 2023 attack: Threat actors created rogue VMs to evade detection

![](https://i0.wp.com/securityaffairs.com/wp-content/uploads/2022/06/mitre.png?fit=225%2C225&ssl=1)

## The MITRE Corporation revealed that threat actors behind the December 2023 attacks created rogue virtual machines (VMs) within its environment.

The MITRE Corporation has provided a new update about the [December 2023 attack](https://securityaffairs.com/163144/security/mitre-released-emb3d-framework.html). In April 2024, MITRE disclosed a security breach in one of its research and prototyping networks. The security team at the organization promptly launched an investigation, logged out the threat actor, and engaged third-party forensics Incident Response teams to conduct independent analysis in collaboration with internal experts.

According to the MITRE Corporation, [**China-linked nation-state actor UNC5221**](https://securityaffairs.com/162811/hacking/mitre-security-breach-china.html) breached its systems in January 2024 by chaining two [Ivanti Connect Secure zero-day vulnerabilities](https://securityaffairs.com/161465/security/ivanti-code-execution-dos-flaws.html).

MITRE spotted the foreign nation-state threat actor probing its Networked Experimentation, Research, and Virtualization Environment (NERVE), used for research and prototyping. The organization immediately started mitigation actions which included taking NERVE offline. The investigation is still ongoing to determine the extent of information involved.

The organization notified authorities and affected parties and is working to restore operational alternatives for collaboration.

Despite MITRE diligently following industry best practices, implementing vendor recommendations, and complying with government guidance to strengthen, update, and fortify its Ivanti system, they overlooked the lateral movement into their VMware infrastructure.

The organization said that the core enterprise network or partners’ systems were not affected by this incident.

According to the new update, threat actors exploited zero-day flaws in Ivanti Connect Secure (ICS) and created rogue virtual machines (VMs) within the organization’s VMware environment.

*“The adversary created their own rogue VMs within the VMware environment, leveraging compromised vCenter Server access. They wrote and deployed a JSP web shell (**BEEFLUSH**) under the vCenter Server’s Tomcat server to execute a Python-based tunneling tool, facilitating SSH connections between adversary-created VMs and the ESXi hypervisor infrastructure.” reads the [**latest update**](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b). “By deploying rogue VMs, adversaries can evade detection by hiding their activities from centralized management interfaces like vCenter. This allows them to maintain control over compromised systems while minimizing the risk of discovery.”*

The attackers deployed rogue virtual machines (VMs) to evade detection by hiding their activities from centralized management interfaces like vCenter. This tactic allows them to control the compromised systems while minimizing the risk of discovery.

On January 7, 3034, the adversary accessed VMs and deployed malicious payloads, including the BRICKSTORM backdoor and a web shell tracked as BEEFLUSH, enabling persistent access and arbitrary command execution.

The hackers relied on SSH manipulation and script execution to maintain control over the compromised systems. Mitre noted attackers exploiting a default VMware account to list drives and generate new VMs, one of which was removed on the same day. BRICKSTORM was discovered in directories with local persistence setups, communicating with designated C2 domains. BEEFLUSH interacted with internal IP addresses, executing dubious scripts and commands from the vCenter server’s /tmp directory

In the following days, the threat actors deployed additional payloads on the target infrastrcuture, including the [WIREFIRE](https://www.mandiant.com/resources/blog/investigating-ivanti-zero-day-exploitation) (aka GIFTEDVISITOR) web shell, and the BUSHWALK webshell for data exfiltration.

The threat actors exploited a default VMware account, VPXUSER, to make API calls for enumerating drives. They bypassed detection by deploying rogue VMs directly onto hypervisors, using SFTP to write files and executing them with /bin/vmx. These operations were invisible to the Center and the ESXi web interface. The rogue VMs included the BRICKSTORM backdoor and persistence mechanisms, configured with dual network interfaces for communication with both the Internet/C2 and core administrative subnets.

*“Simply using the hypervisor management interface to manage VMs is often insufficient and can be pointless when it comes to dealing with rogue VMs.” continues the update. “This is because rogue VMs operate outside the standard management processes and do not adhere to established security policies, making them difficult to detect and manage through the GUI alone. Instead, one needs special tools or techniques to identify and mitigate the risks associated with rogue VMs effectively.”*

MITRE shared two scripts, [Invoke-HiddenVMQuery](https://github.com/center-for-threat-informed-defense/public-resources/tree/master/nerve-incident#rogue-vm-detection-script) and [VirtualGHOST](https://github.com/CrowdStrike/VirtualGHOST), that allow admins to identify and mitigate potential threats within the VMware environment. The first script, developed by MITRE, [Invoke-HiddenVMQuery](https://github.com/center-for-threat-informed-defense/public-resources/tree/master/nerve-incident#rogue-vm-detection-script) is written in PowerShell and serves to detect malicious activities. It scans for anomalous invocations of the `/bin/vmx` binary within `rc.local.d` scripts.

*“As adversaries continue to evolve their tactics and techniques, it is imperative for organizations to remain vigilant and adaptive in defending against cyber threats. By understanding and countering their new adversary behaviors, we can bolster our defenses and safeguard critical assets against future intrusions.” MITRE concludes.*

[**Pierluigi Paganini**](http://www.linkedin.com/pub/pierluigi-paganini/b/742/559)

Follow me on Twitter: [**@securityaffairs**](https://twitter.com/securityaffairs) and [**Facebook**](https://www.facebook.com/sec.affairs) and [Mastodon](https://infosec.exchange/%40securityaffairs)

**(**[**SecurityAffairs**](http://securityaffairs.co/wordpress/)**–** **hacking, China)**

---

文章来源: https://securityaffairs.com/163658/apt/mitre-december-2023-attack-rogue-vms.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)