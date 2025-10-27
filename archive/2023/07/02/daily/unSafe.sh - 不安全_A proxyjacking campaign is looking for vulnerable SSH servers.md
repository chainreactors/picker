---
title: A proxyjacking campaign is looking for vulnerable SSH servers
url: https://buaq.net/go-170936.html
source: unSafe.sh - 不安全
date: 2023-07-02
fetch_date: 2025-10-04T11:51:18.362879
---

# A proxyjacking campaign is looking for vulnerable SSH servers

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

A proxyjacking campaign is looking for vulnerable SSH servers

A researcher at Akamai has posted a blog about a worrying new trend—pro
*2023-7-1 06:15:0
Author: [www.malwarebytes.com(查看原文)](/jump-170936.htm)
阅读量:24
收藏*

---

A researcher at Akamai has [posted a blog](https://www.akamai.com/blog/security-research/proxyjacking-new-campaign-cybercriminal-side-hustle) about a worrying new trend—proxyjacking—where criminals sell your bandwidth to a third-party proxy service.

To understand how proxyjacking works, we’ll need to explain a few things.

There are several legitimate services that pay users to share their surplus Internet bandwidth, such as [Peer2Profit](https://peer2profit.com/) and [HoneyGain](https://www.honeygain.com/). The participants install software that adds their systems to the proxy-network of the service. Customers of the proxy service have their traffic routed through the participants' systems.

The foundation of the proxyjacking problem lies in the fact that these services don’t check where the shared bandwidth is coming from. Peer2Profit and Honeygain claim to only share their proxies with theoretically vetted partners, but according to Akamai's research they don’t check if the one offering the bandwidth is the actual owner.

Proxies and stolen bandwidth have always been popular among cybercriminals since they allow them to anonymize their traffic. What’s new about this campaign is that these same criminals are now “renting out” the bandwidth of compromised systems to make money instead of simply using them.

The researcher became aware of the campaign when they noticed an attacker establishing multiple SSH (Secure Shell) connections to one of their Cowrie honeypots. Cowrie is a medium to high interaction SSH and Telnet honeypot designed to log brute force attacks and the shell interaction performed by the attacker. It can be used to emulate a UNIX system in Python, or to function as an SSH and telnet proxy to observe attacker behavior to another system.

For the criminals the beauty of the attack is that it is mostly [fileless](https://www.malwarebytes.com/blog/business/2023/04/fileless-attacks-how-attackers-evade-traditional-av-and-how-to-stop-them) and the files that are actually used, [curl](https://curl.se/) and the public [Docker](https://www.docker.com/) images for the proxy monetization services Peer2Profit and Honeygain, are legitimate and will not be detected by anti-malware solutions.

And proxyjacking is a lot less likely to be detected than [cryptojacking](https://www.malwarebytes.com/blog/news/2022/08/cryptojackers-are-growing-in-numbers-and-sophistication) since it requires only minimal CPU cycles and uses surplus Internet bandwidth. Interesting to note, the researchers found out that the compromised distribution server also contained a cryptomining utility, as well as many other exploits and common hacking tools.

## Protection

Since these seemingly legitimate services can be used by criminals on both ends, both to anonymize their activities and to sell others’ resources, we would rather see them disappear altogether, but they should at least improve the verification of their customers and their participants.

Home users can protect themselves from proxyjacking by:

* Keeping their [systems and software updated](https://www.malwarebytes.com/business/vulnerability-patch-management)
* Use an effective and secure [password strategy](https://www.malwarebytes.com/blog/news/2023/05/the-one-and-only-password-tip-you-need)

Corporate users can add:

* Monitor network traffic for anomalies
* Keep track of running [containerized applications](https://www.malwarebytes.com/blog/news/2019/12/explained-what-is-containerization).
* Using key-based authentication for SSH instead of passwords

Akamai added:

> “In this particular campaign, we saw the use of SSH to gain access to a server and install a Docker container, but past campaigns have exploited web vulnerabilities as well. If you check your local running Docker services and find any unwanted resource sharing on your system, you should investigate the intrusion, determine how the script was uploaded and run, and perform a thorough cleanup.”

---

文章来源: https://www.malwarebytes.com/blog/news/2023/06/a-proxyjacking-campaign-is-looking-for-vulnerable-ssh-servers
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)