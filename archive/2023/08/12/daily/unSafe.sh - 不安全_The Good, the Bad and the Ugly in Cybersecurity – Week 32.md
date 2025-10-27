---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 32
url: https://buaq.net/go-174278.html
source: unSafe.sh - 不安全
date: 2023-08-12
fetch_date: 2025-10-04T12:00:17.224275
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 32

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

![](https://8aqnet.cdn.bcebos.com/925ece04afde6ec98701dc35dff0e4fc.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 32

The Good | White House Launches AI-Centric Cybersecurity Contest to Protect US EntitiesThe Biden-H
*2023-8-11 23:39:42
Author: [www.sentinelone.com(查看原文)](/jump-174278.htm)
阅读量:28
收藏*

---

## The Good | White House Launches AI-Centric Cybersecurity Contest to Protect US Entities

The Biden-Harris administration this week [announced](https://www.whitehouse.gov/briefing-room/statements-releases/2023/08/09/biden-harris-administration-launches-artificial-intelligence-cyber-challenge-to-protect-americas-critical-software/) a new hacking challenge with the purpose of using [artificial intelligence](https://www.sentinelone.com/blog/advancing-security-the-age-of-ai-machine-learning-in-cybersecurity/) (AI) to protect critical US infrastructure from growing cybersecurity threats. In collaboration with tech companies such as OpenAI and Anthropic who are making their technology available for the competition, the “AI Cyber Challenge” (aka AIxCC) offers up to $20 million in prizes for participating [hackers](https://www.sentinelone.com/cybersecurity-101/what-is-a-hacker/). AIxCC will be led by the Defense Advanced Research Projects Agency (DARPA) who have made an additional $7 million available for SMBs looking to compete. The challenge was announced at [Black Hat USA 2023](https://www.sentinelone.com/blog/day-1-of-black-hat-usa-2023/) cybersecurity conference in Las Vegas in line with this years’ theme of [generative AI](https://www.sentinelone.com/blog/integrating-chatgpt-generative-ai-within-cybersecurity-best-practices/).

> I’m excited to announce the AI Cyber Challenge, a major, two-year [@DARPA](https://twitter.com/DARPA?ref_src=twsrc%5Etfw) competition challenging the best and the brightest in cybersecurity and AI to secure the systems on which all American rely.<https://t.co/mZR4ZNSiaM> [pic.twitter.com/VF1LiSGijh](https://t.co/VF1LiSGijh)
>
> — Perri Adams @ Black Hat and DEF CON (@perribus) [August 9, 2023](https://twitter.com/perribus/status/1689321023718789120?ref_src=twsrc%5Etfw)

The challenge is a practical exercise in demonstrating the potential benefits of AI in securing various software used across all industry verticals. Described by White House officials as being a “clarion call” for organizations to strengthen the security of their critical software, AIxCC plans to leverage the winning code to protect federal and critical infrastructure immediately. As part of the administration’s 2021 [executive order](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/) on improving the nation’s cybersecurity posture, AIxCC is the latest effort in exploring AI-based security and innovation to mitigate the severe damage and costs associated with modern cyber risks.

The challenge also calls to attention the notion that AI holds potential in [helping](https://www.sentinelone.com/blog/what-it-takes-to-be-a-top-gun-genai-cybersecurity/) security professionals remain steps ahead of increasingly sophisticated cyber threat actors only if used safely and responsibly. Earlier this year, NIST [launched](https://www.nist.gov/itl/ai-risk-management-framework) an AI risk management framework and last month, the administration [secured](https://www.whitehouse.gov/briefing-room/statements-releases/2023/07/21/fact-sheet-biden-harris-administration-secures-voluntary-commitments-from-leading-artificial-intelligence-companies-to-manage-the-risks-posed-by-ai/) voluntary commitments from leading AI companies to manage the risk posed by the budding popularity of the technology.

Semi-finalists of the challenge can expect to compete at DEF CON 2024 with the final leg of the competition to be hosted the following year at DEF CON 2025.

## The Bad | High-Severity RCE Vulnerability Threatens Windows Print Management Software

Earlier this week cybersecurity researchers [uncovered](https://www.horizon3.ai/cve-2023-39143-papercut-path-traversal-file-upload-rce-vulnerability/) a critical vulnerability in a print management software for Windows called PaperCut. Tracked as [CVE-2023-39143](https://nvd.nist.gov/vuln/detail/CVE-2023-39143), the path traversal and file upload flaw allows potential attackers to upload, read, or delete arbitrary files leading to remote code execution (RCE) of the application server.

Exploitation of this vulnerability requires the external device integration to be enabled, which is a default configuration for specific installations of the software. According to the researcher, they estimate that the vast majority of PaperCut installations currently run on Windows with this particular setting turned on. They also note that this vulnerability, though severe, involves multiple issues that must be chained together before server compromise is successful.

The company has strongly recommended their users to [patch](https://www.papercut.com/kb/Main/SecurityBulletinJuly2023/) their installations to version 22.1.3 or later. To check if a server is vulnerable to CVE-2023-39143, use the following command:

![](https://www.sentinelone.com/wp-content/uploads/2023/08/papercut.jpg)

CVE-2023-39143 is the latest in a string of vulnerabilities afflicting the PaperCut software this year. In April, two similar vulnerabilities, CVE-2023-27350 (an RCE flaw) and CVE-2023-27351 (an information disclosure flaw), came under widespread use by ransomware affiliates, most notably [Cl0p](https://www.sentinelone.com/anthology/clop/) and [LockBit](https://www.sentinelone.com/anthology/lockbit-2-0/), to deliver [Cobalt Strike](https://www.sentinelone.com/cybersecurity-101/what-is-cobalt-strike/) and ransomware. Nearly two weeks later, the same vulnerabilities were exploited by Iranian-backed threat actors to gain access into targeted networks and exfiltrate corporate data.

SentinelOne customers are automatically protected against both Cl0p and LockBit 2.0 and [3.0](https://www.sentinelone.com/anthology/lockbit-3-0-lockbit-black/) through the [Singularity XDR platform](https://www.sentinelone.com/platform/singularity-xdr-protection/) which identifies and stops any malicious activities related to either ransomware affiliate.

## The Ugly | DPRK-Backed Hack Group Breaches Russian Missile Makers

North Korean state-sponsored hacking group, ScarCruft (aka APT37), has been identified as the culprit behind a cyberattack on NPO Mashinostroyeniya, a Russian organization known for designing space rockets and intercontinental ballistic missiles. Despite being sanctioned by the U.S. Department of Treasury due to its involvement in the [Russo-Ukrainian war](https://www.sentinelone.com/labs/hermetic-wiper-ukraine-under-attack/), NPO Mashinostroyeniya fell victim to the attack, which involved planting an ‘OpenCarrot’ Windows backdoor for remote network access.

According an [analysis](https://www.sentinelone.com/labs/comrades-in-arms-north-korea-compromises-sanctioned-russian-missile-engineering-company/) by SentinelLabs, ScarCruft specializes in cyber espionage, targeting and exfiltrating data from various entities as part of its operations though the motives for this campaign are still unclear. The breach was initially discovered when leaked emails from NPO Mashinostroyeniya revealed suspicious network communications and a malicious DLL file installed on internal systems. This prompted further investigation by SentinelLabs, uncovering a more extensive intrusion than the missile makers initially realized.

![Example of unrelated email alerts from Rus...