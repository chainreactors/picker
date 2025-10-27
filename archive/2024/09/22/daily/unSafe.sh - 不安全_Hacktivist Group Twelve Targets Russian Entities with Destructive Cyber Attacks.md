---
title: Hacktivist Group Twelve Targets Russian Entities with Destructive Cyber Attacks
url: https://buaq.net/go-263290.html
source: unSafe.sh - 不安全
date: 2024-09-22
fetch_date: 2025-10-06T18:20:07.039877
---

# Hacktivist Group Twelve Targets Russian Entities with Destructive Cyber Attacks

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

![](https://8aqnet.cdn.bcebos.com/3f48da967459a7262935be04fdf6957d.jpg)

Hacktivist Group Twelve Targets Russian Entities with Destructive Cyber Attacks

Cyber Warfare / Threat IntelligenceA hacktivist group known as Twelve has been observed using an a
*2024-9-21 22:39:0
Author: [thehackernews.com(查看原文)](/jump-263290.htm)
阅读量:19
收藏*

---

Cyber Warfare / Threat Intelligence

[![Destructive Cyber Attacks](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjTV8s8iCxxGc014vYriCca8z2Q_Uc_rt0Qp-WrYa_UizO6qrbu0ObAUPc34Wm6k8vG8zEjOh-wSMksUj6YnAkbqPkXd8mwspMSbzsA37G2sTag_rKFXHbC1ybht3CsVBJ2rU0pH8-6DfPL88T2Zy8j9DDp00_hOoqiZGu89P9ZXp5kJYVNnYcAAi3mbFdF/s728-rw-e365/malware.png "Destructive Cyber Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjTV8s8iCxxGc014vYriCca8z2Q_Uc_rt0Qp-WrYa_UizO6qrbu0ObAUPc34Wm6k8vG8zEjOh-wSMksUj6YnAkbqPkXd8mwspMSbzsA37G2sTag_rKFXHbC1ybht3CsVBJ2rU0pH8-6DfPL88T2Zy8j9DDp00_hOoqiZGu89P9ZXp5kJYVNnYcAAi3mbFdF/s728-rw-e365/malware.png)

A hacktivist group known as Twelve has been observed using an arsenal of publicly available tools to conduct destructive cyber attacks against Russian targets.

"Rather than demand a ransom for decrypting data, Twelve prefers to encrypt victims' data and then destroy their infrastructure with a wiper to prevent recovery," Kaspersky [said](https://securelist.com/twelve-group-unified-kill-chain/113877/) in a Friday analysis.

"The approach is indicative of a desire to cause maximum damage to target organizations without deriving direct financial benefit."

The hacking group, believed to have been formed in April 2023 following the onset of the Russo-Ukrainian war, has a track record of mounting cyber attacks that aim to cripple victim networks and disrupt business operations.

It has also been observed conducting hack-and-leak operations that exfiltrate sensitive information, which is then shared on its Telegram channel.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgDZvDvyWp54Ch7XRFz4ZO0AalryM4VfCPF0b7TGMeX45fjRe_MDN_DxW4zHXUF2cphm5DUuDMwQQGRGaXECrYvOyALD1p7C525KuJg7Rb4Yn4V2PX4_AtXSNI8mjT3DMR-hJjWytQYxZ5afHz6qHMl5U0OKHQfnnbv1SnxzQi0uGbWwuPA8ZtQQn-yjJ6e/s728-e100/ir-book.png)](https://thehackernews.uk/hkn-executive "Cybersecurity")

Kaspersky said Twelve shares infrastructural and tactical overlaps with a ransomware group called [DARKSTAR](https://www.anti-malware.ru/news/2024-02-02-114534/42735) (aka COMET or Shadow), raising the possibility that the two intrusion sets are likely related to one another or part of the same activity cluster.

"At the same time, whereas Twelve's actions are clearly hacktivist in nature, DARKSTAR sticks to the classic double extortion pattern," the Russian cybersecurity vendor said. "This variation of objectives within the syndicate underscores the complexity and diversity of modern cyberthreats."

The attack chains start with gaining initial access by abusing valid local or domain accounts, after which the Remote Desktop Protocol (RDP) is used to facilitate lateral movement. Some of these attacks are also carried out via the victim's contractors.

"To do this, they gained access to the contractor's infrastructure and then used its certificate to connect to its customer's VPN," Kaspersky noted. "Having obtained access to that, the adversary can connect to the customer's systems via the Remote Desktop Protocol (RDP) and then penetrate the customer's infrastructure."

Prominent among the other tools used by Twelve are Cobalt Strike, Mimikatz, Chisel, BloodHound, PowerView, adPEAS, CrackMapExec, Advanced IP Scanner, and PsExec for credential theft, discovery, network mapping, and privilege escalation. The malicious RDP connections to the system are tunneled through ngrok.

Also deployed are PHP web shells with capabilities to execute arbitrary commands, move files, or send emails. These [programs](https://github.com/stefanpejcic/wordpress-malware), such as the [WSO web shell](https://github.com/tennc/webshell/blob/master/php/wso/wso2.php), are readily available on GitHub.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgvMzB7oJ41MbA1DbHz5G5UWMsybAEtsSRYxm-gXqAXQ7xh4KpReuEeOjkyR5HNjFMM0AX1E02o3fA0KjttwVZzmNnnJJelQbMQkmdCfTLZLzQNnpA4DoJif7qC1ln5UI3mYtmO-xrWb-lFJGAet4hDDDoZj_J8Q6tSV0e7tnkPhoDfTiWFN619_FAHLp9M/s728-rw-e365/hacking.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgvMzB7oJ41MbA1DbHz5G5UWMsybAEtsSRYxm-gXqAXQ7xh4KpReuEeOjkyR5HNjFMM0AX1E02o3fA0KjttwVZzmNnnJJelQbMQkmdCfTLZLzQNnpA4DoJif7qC1ln5UI3mYtmO-xrWb-lFJGAet4hDDDoZj_J8Q6tSV0e7tnkPhoDfTiWFN619_FAHLp9M/s728-rw-e365/hacking.png)

In one incident investigated by Kaspersky, the threat actors are said to have exploited known security vulnerabilities (e.g., [CVE-2021-21972](https://nvd.nist.gov/vuln/detail/CVE-2021-21972) and [CVE-2021-22005](https://nvd.nist.gov/vuln/detail/CVE-2021-22005)) in VMware vCenter to deliver a [web shell](https://github.com/NS-Sp4ce/CVE-2021-21972/tree/main/payload/Linux) that then was used to drop a backdoor dubbed FaceFish.

"To gain a foothold in the domain infrastructure, the adversary used PowerShell to add domain users and groups, and to modify ACLs (Access Control Lists) for Active Directory objects," it said. "To avoid detection, the attackers disguised their malware and tasks under the names of existing products or services."

Some of the names used include "Update Microsoft," "Yandex," "YandexUpdate," and "intel.exe."

The attacks are also characterized by the use of a PowerShell script ("Sophos\_kill\_local.ps1") to terminate processes related to Sophos security software on the compromised host.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/hkn-cis-secure-d "Cybersecurity")

The concluding stages entail using the Windows Task Scheduler to launch ransomware and wiper payloads, but not before gathering and exfiltrating sensitive information about their victims via a file-sharing service called DropMeFiles in the form of ZIP archives.

"The attackers used a version of the popular [LockBit 3.0 ransomware](https://thehackernews.com/2024/06/fbi-distributes-7000-lockbit-ransomware.html), compiled from publicly available source code, to encrypt the data," Kaspersky researchers said. "Before starting work, the ransomware terminates processes that may interfere with the encryption of individual files."

The wiper, identical to the [Shamoon](https://thehackernews.com/2022/03/researchers-find-new-evidence-linking.html) malware, rewrites the master boot record (MBR) on connected drives and overwrites all file contents with randomly generated bytes, effectively preventing system recovery.

"The group sticks to a publicly available and familiar arsenal of malware tools, which suggests it makes none of its own," Kaspersky noted. "This makes it possible to detect and prevent Twelve's attacks in due time."

Found this article interesting? Follow us on [Twitter **](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

文章来源: https://thehackernews.com/2024/09/hacktivist-group-twelve-targets-russian.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)