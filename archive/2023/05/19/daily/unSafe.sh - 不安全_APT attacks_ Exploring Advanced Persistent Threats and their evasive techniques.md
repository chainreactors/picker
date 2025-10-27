---
title: APT attacks: Exploring Advanced Persistent Threats and their evasive techniques
url: https://buaq.net/go-164278.html
source: unSafe.sh - 不安全
date: 2023-05-19
fetch_date: 2025-10-04T11:37:54.966357
---

# APT attacks: Exploring Advanced Persistent Threats and their evasive techniques

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

![](https://8aqnet.cdn.bcebos.com/e809a2cf4774ad9ba339eff021d5984c.jpg)

APT attacks: Exploring Advanced Persistent Threats and their evasive techniques

Cyber criminals come in all shapes and sizes.On one end of the spectru
*2023-5-18 22:0:0
Author: [www.malwarebytes.com(查看原文)](/jump-164278.htm)
阅读量:48
收藏*

---

Cyber criminals come in all shapes and sizes.

On one end of the spectrum, there’s the script kiddie or inexperienced ransomware gang looking to make a quick buck. On the other end are state-sponsored groups using far more sophisticated tactics—often with long-term, strategic goals in mind.

[Advanced Persistent Threats (APT](https://www.malwarebytes.com/blog/news/2016/07/explained-advanced-persistent-threat-apt)) groups fall into this latter category.

Well-funded and made up of an elite squadron of hackers, these groups target high-value entities like governments, large corporations, or critical infrastructure. They often deploy multi-stage, multi-vector approaches with a high degree of obfuscation and persistence.

But for every small-to-medium-sized business (SMB) out there asking themselves "Why would an APT group care about me?" We have the answer.

**SMBs can be stepping stones to bigger targets—especially if they're in a supply chain or serve larger entities**. A whopping 93% of SMB execs even think nation-state hackers are using businesses like theirs as a backdoor into the country's digital defenses.

In this post, we’ll break down how APT groups work, explain their tactics and evasive techniques, and how to detect APT attacks.

## How APT groups work

The aim of APT groups is not a quick hit, but a long-term presence within a system, allowing them to gather as much information as they can while remaining undetected.

APTs stand apart from typical cybercriminals in several key ways:

* **Motive**: Unlike ordinary cybercriminals, APTs are primarily driven by the acquisition of intelligence. While they might engage in activities that yield financial gains, their primary funding comes from the state they serve, not from their operations.
* **Tools**: APTs have access to advanced tools and zero-day vulnerabilities. They keep these under wraps for as long as they can, only resorting to destructive malware when necessary.
* **Crew**: APTs consist of experienced and motivated individuals who work in close coordination with one another. This is a stark contrast to traditional cybercriminals, where distrust often prevails.

![](https://www.malwarebytes.com/blog/business/2023/05/easset_upload_file19888_266112_e.png)

So, how does an APT work its dark magic? Here's a quick rundown:

* **Step 1**: *Reconnaissance*. This could be anything from figuring out whether there's sensitive data or information worth stealing to making a hit list of employees or ex-employees.
* **Step 2**: *Infiltration*. Usually, this involves some crafty social engineering, like spear phishing or setting up a watering hole to deliver custom malware.
* **Step 3**: *Establishing a foothold*. APTs need someone inside the target's network to run their malware.
* **Step 4**: *Expanding their reach*. This might involve further deployment of malware, reconnaissance of the network, or other activities aimed at consolidating their position.
* **Step 5**: *Data acquisition*. The ultimate goal is to acquire the desired data. They might need to get more access in the network to do this.
* **Step 6**: *Maintaining presence*. Once they're in, they might need to create more entry points or even leave a backdoor open for a return visit. If they're done, they'll clean up their mess to cover their tracks.

While not all these steps are required in every case, and the time and effort expended on each can vary widely, this provides a general framework for understanding how APTs operate.

## Evasive techniques of APT attacks

Alright, now that we know the basics of how APTs operate, let's dive into the specifics of their tools, techniques, and procedures (TTPs).

| TTP (MITRE ATT&CK) | Description |
| --- | --- |
| **Phishing (Spear-phishing Attachment, Spear-phishing Link)** | APT groups frequently initiate targeted spear-phishing attacks, often combined with social engineering and exploitation of software vulnerabilities, to gain initial access to a target network. |
| **Execution through API (T1059.005) or User Execution (T1204)** | Once inside a network, APTs use legitimate system tools and processes to carry out their activities in a way that blends in with normal network activity and avoids detection. |
| **Exploitation for Client Execution (T1203)** | APT groups frequently discover and exploit zero-day vulnerabilities — these are software flaws unknown to the software's vendor at the time of exploitation. |
| **Lateral Movement (Tactic ID: TA0008)** | After gaining initial access, APTs use lateral movement techniques, such as Pass the Hash (PtH), to explore the network, elevate their privileges, and gain access to more systems. |
| **Exfiltration Over C2 Channel (T1041)** | APTs typically employ advanced, stealthy techniques for stealing data, such as splitting it into small packets, encrypting it, or sending it out during normal business hours to blend in with regular traffic. |
| **Establish Persistence (Tactic ID: TA0003)** | APT groups use techniques like multiple backdoors, rootkits, and even firmware or hardware-based attacks to maintain access to a network even after detection and remediation efforts. |
| **Supply Chain Compromise (T1195)** | APTs sometimes compromise software or hardware vendors to exploit the trust relationships between those vendors and their customers, thereby gaining access to the customers' systems. |

In a word, APT groups use methods like "[living off the land" (utilizing built-in software tools to carry out their activities)](https://www.malwarebytes.com/blog/business/2023/04/living-off-the-land-lotl-attacks-detecting-ransomware-gangs-hiding-in-plain-sight), [fileless malware (malware that resides in memory rather than on disk),](https://www.malwarebytes.com/blog/business/2023/04/fileless-attacks-how-attackers-evade-traditional-av-and-how-to-stop-them) encryption (to hide their communication), and anti-forensic measures (to cover their tracks).

## Breakdown of different APT groups

Attribution is always a bit thorny when it comes to different APT groups, but some groups are rather well-known and their origin has become clear. A naming convention that not everyone follows is: Chinese APT actors are commonly known as “Pandas,” Russian APTs as “Bears,” and Iranian APTs as “Kittens”.

Some examples:

* **APT28** aka Fancy Bear (Russia)
* **Nemesis Kitten** (Iran) a sub-group of Iranian threat actor Phosphorus (APT35)
* **APT1** aka Comment Panda aka unit 61398 of the People's Liberation Army (China)

Countries typically have different groups that focus on different targets, but generally speaking, some of the most frequently hit sectors are governments, aerospace, and telecommunications.

According to the cyber threat group list compiled by [MITRE ATT&CK](https://attack.mitre.org/groups/), we're aware of over 100 APT groups worldwide. The majority of these groups have ties to China, Russia, and Iran. In fact, China and Russia alone are reportedly connected to nearly [63% of all these](https://www.securin.io/prevent-falling-victim-to-apt-groups-using-securins-ai-based-vulnerability-and-threat-intelligence/) known groups.

For the purposes of this article, I compiled data on [37 different APT groups listed by American cybersecurity firm Mandiant](https://www.mandiant.com/resources/insights/apt-groups) and br...