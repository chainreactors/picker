---
title: &#x5b;Guest Diary&#x5d; A Deep Dive into TeamTNT and Spinning YARN, (Wed, Dec 18th)
url: https://isc.sans.edu/diary/rss/31530
source: SANS Internet Storm Center, InfoCON: green
date: 2024-12-19
fetch_date: 2025-10-06T19:41:56.651388
---

# &#x5b;Guest Diary&#x5d; A Deep Dive into TeamTNT and Spinning YARN, (Wed, Dec 18th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31528)
* [next](/diary/31538)

# [[Guest Diary] A Deep Dive into TeamTNT and Spinning YARN](/forums/diary/Guest%2BDiary%2BA%2BDeep%2BDive%2Binto%2BTeamTNT%2Band%2BSpinning%2BYARN/31530/)

**Published**: 2024-12-18. **Last Updated**: 2024-12-18 00:04:50 UTC
**by** [James Levija, SANS.edu BACS Student](/handler_list.html#james-levija,-sans.edu-bacs-student) (Version: 1)

[0 comment(s)](/diary/Guest%2BDiary%2BA%2BDeep%2BDive%2Binto%2BTeamTNT%2Band%2BSpinning%2BYARN/31530/#comments)

[This is a Guest Diary by James Levija, an ISC intern as part of the SANS.edu Bachelor's Degree in Applied Cybersecurity (BACS) program [1].]

## Executive Summary

TeamTNT is running a crypto mining campaign dubbed Spinning YARN. Spinning YARN focuses on exploiting Docker, Redis, YARN, and Confluence [2]. On November 4th, 2024, my DShield sensor recorded suspicious activity targeting my web server. The attacker attempted to use a technique that tricks the server into running harmful commands. This technique is known as server-side scripting vulnerability. This attack originated from IPv4 address `[47.93.56.107](/ipinfo.html?ip=47.93.56.107)` targeting `[port 8090](/port/8090)`. The attacker used a technique to disguise their harmful code by encoding it. This technique hides the code’s true purpose and assists with avoiding detection against antivirus software and firewalls.

An analysis of the obfuscated code revealed that the command would send the victim to another website to download a malicious file. The malicious file dropped is named “`w.sh`” [3]. The purpose of this initial file is to install the requirements to run the intended malware and to download the intended malware from the site **`hxxp://b[.]9-9-8[.]com/brysj`**. Once the intended malware is downloaded, it runs and assesses the environment. It targets Linux distributions and cloud environments. The malware identifies possible cloud security and attempts to disable it to allow the rest of the code to run smoothly. The malware then sets up its persistence through creating secure keys to talk back to the attacker’s server and establishes a connection to the attacker’s server. It also uses techniques to hide itself on the victim’s device or cloud environment. Finally, the malware sets up a crypto miner to utilize the victim’s resources for the attacker’s gain.

**![](https://isc.sans.edu/diaryimages/images/2024-12-18_figure1.png)
Figure 1: Attack Flow**

The impact of this attack extends beyond consuming system resources for cryptocurrency mining. The connection between the victim’s machine or cloud environment and the attacker grants the attacker persistent access. The attacker can abuse this through conducting additional exploits, steal sensitive data, or use the system to launch additional attacks on other systems. TeamTNT is known to have created a work that could steal Amazon Web Service (AWS) credentials. This poses significant risks to operational security and data integrity for any organization.

This attack highlights evolving threats to Linux and cloud environments from sophisticated groups like TeamTNT. Organizations should prioritize securing their infrastructure through regular updates, monitoring suspicious activity, staying up to date on cyber threat intelligence, and implementing robust defenses against malware and their obfuscation techniques. Collaboration withing the cybersecurity community is key to mitigating these ongoing threats.

## TeamTNT – Background

TeamTNT is a cyber threat group that has been active since October 2019. The group is well known for their attacks on cloud environments and cryptojacking [4]. The location of the group members is unknown, but they are suspected of being in Germany due to TeamTNT’s X (formerly Twitter) account, with the handle `@HildeTnT`, sending tweets in English and German [5]. In December 2020, the group was suspected to have 12 members based on a tweet about their group of programmers [6].

**![](https://isc.sans.edu/diaryimages/images/2024-12-18_figure2.png)
Figure 2: Tweet from TeamTNT referencing the number of programmers [6].**

## Indicators of Compromise (IoCs)

### Identified Malicious Domains and URLs

Below are the malicious URLs observed in the binaries:

* Domain – `hxxps://9-9-8[.]com`
* Main URL - `hxxps://b[.]9-9-8[.]com/brysj/`
* Dropper URL - `hxxps://b[.]9-9-8[.]com/brysj/w[.]sh`
* Miner URL – `hxxps://b[.]9-9-8[.]com/brysj/d/ar[.]sh`
* Miner URL - `hxxps://b[.]9-9-8[.]com/brysj/m/enbash[.]tar`
* Remote Shell - `hxxps://b[.]9-9-8[.]com/brysj/m/enbio[.]tar`
* Additional URLs – `hxxps://m[.]9-9-8[.]com`

### IPs Involved

| IP Address | Last Seen |
| --- | --- |
| [52.223.13.41](/ipinfo.html?ip=52.223.13.41) | 2024-11-26 |
| [194.36.190.32](/ipinfo.html?ip=194.36.190.32) | 2024-11-13 |
| [158.160.116.91](/ipinfo.html?ip=158.160.116.91) | 2024-10-20 |
| [212.233.121.136](/ipinfo.html?ip=212.233.121.136) | 2024-09-01 |
| [62.113.111.152](/ipinfo.html?ip=62.113.111.152) | 2024-08-15 |
| [185.208.207.89](/ipinfo.html?ip=185.208.207.89) | 2024-08-01 |
| [154.38.165.7](/ipinfo.html?ip=154.38.165.7) | 2024-07-16 |
| [114.114.114.114](/ipinfo.html?ip=114.114.114.114) | 2024-12-02 |

**Figure 3: IP addresses seen.**

### Associated Files and Hashes

| Filename | Notes | Hash |
| --- | --- | --- |
| w.sh | Dropper | d4508f8e722f2f3ddd49023e7689d8c65389f65c871ef12e3a6635bbaeb7eb6e |
| ar.sh | Dropper | 64d8f887e33781bb814eaefa98dd64368da9a8d38bd9da4a76f04a23b6eb9de5 |
| hf.tar |  | 651a3034429358a0ccb2d58ecbe2b7f3e4ee1bf4bee3e7a86f7ca873f6049ec2 |
| diamorphine.c |  | aec68cfa75b582616c8fbce22eecf463ddb0c09b692a1b82a8de23fb0203fede |
| diamorphine.h |  | d27eeb48b1a74efd8710ef4ce62ee8469dd2352b0079c5b1c82e8da43fe932a2 |
| Makefile |  | d15af7984ed9b33093d7d5725c84ab24edf7c4ff02af3ac0a6c3aa9d5f7e12f4 |
| Makefile |  | 5b9acfd34a30a3f26db492ed4404d518d583c0088a38a7622b683407c34b9108 |
| processhider.c |  | 7e84f9aab329754fe4681d4d6e4c64098731fd55b5998d7cfacb08ba4dbdfd5c |
| enbash.tar |  | 9eafaf5e0fb9a91f2887f3e81fd7ad6d70973ff7cbb807dab4bf0f319a668b95 |
| debash.tar |  | 18137be62c9267cf6b0b40432a91c5818c66bdaa42aad3728c598d3fc65fdcff |
| bash.sh |  | b2e26c7ce901296822085164ede73557a10badfdf99d1aa30f338446d0beb2d7 |
| enbio.tar |  | bb89a6bbddc5dda36542a5fef230b8fa9d98fbdb0ec4fa1794b8c28a0b5a3af4 |
| debio.tar |  | e137bf61096f68478a0daa63fca1b2cc45a99f2dfdcd08d7ff7c449f38cf5ce9 |
| fkoths | Checks for docker containers | afddbaec28b040bcbaa13decdc03c1b994d57de244befbdf2de9fe975cae50c4 |
| sshd | Xmrig Miner | bbcdffd6fa3b1370dfc091bfd3bfca38be013f72f94af7ef29466d911c9604d8 |
| bioset | Establishes reverse shell | 0c7579294124ddc32775d7cf6b28af21b908123e9ea6ec2d6af01a948caf8b87 |
| cronb.sh |  | d4508f8e722f2f3ddd49023e7689d8c65389f65c871ef12e3a6635bbaeb7eb6e |

**Figure 4: Set of files used for this attack.**

## Tools and Tactics Used

### Malware Insights

#### Server-Side injection attack

1. Attempts to execute an `HTTP GET` request to download the file w.sh from `hxxp[://]b[.]9-9-8[.]com/brysj/w[.]sh`
2. Attempts to execute the file

#### w.sh

1. Path and domain variables are set
   1. Domain = `b[.]9-9-8[.]com`
   2. Main URL = `hxxp[://]b[.]9-9-8[.]com/brysj`
2. Bash script checks if the chattr utility is present then renames it to zzhcht and exports the contents.
   1. This is a tactic used by TeamTNT prior to “quitting” in 2021. [7]
3. If chattr is not present, it installs the chatter utility, renames it, and exports the contents.
   1. It tries both yum install and apt install
4. Executes an `HTTP GET` request to download the file ar.sh from `hxxp[://]b[.]9-9-8[.]com/brysj/ar[.]sh`

#### MITRE ATT&CK Framework Mapping

**![](https://isc.sans.edu/diaryimages/images/2024-12-18_figure5.png)
FIgure 5: MITRE A...