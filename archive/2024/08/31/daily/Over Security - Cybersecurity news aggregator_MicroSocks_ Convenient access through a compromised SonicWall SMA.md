---
title: MicroSocks: Convenient access through a compromised SonicWall SMA
url: https://dfir.ch/posts/microsocks_sonicwall/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-31
fetch_date: 2025-10-06T18:08:03.357180
---

# MicroSocks: Convenient access through a compromised SonicWall SMA

[Home](https://dfir.ch/)
[ ]

Menu

* [Home](/)
* [Posts](/posts/)
* [Talks](/talks/)
* [Tweets](/tweets/)
* |

LIGHT

DARK

# MicroSocks: Convenient access through a compromised SonicWall SMA

30 Mar 2024

**Table of Contents**

* [Introduction](#introduction)
* [wafySummary](#wafysummary)
* [Analysis of wafySummary](#analysis-of-wafysummary)
* [Conclusion](#conclusion)
* [Indicators of Compromise](#indicators-of-compromise)

## Introduction

In a recent investigation conducted by my colleague, [Giuseppe Paternicola](https://www.linkedin.com/in/giuseppe-paternicola-7a4b5089/), it was discovered that the initial entry point that ultimately led to the deployment of the Abyss ransomware was a compromised SonicWall Secure Mobile Access (SonicWall SMA) device. The threat actor exploited [CVE-2021-20039](https://attackerkb.com/topics/9szJhq46lw/cve-2021-20039/rapid7-analysis) to gain access (Authenticated Command Injection). Subsequent analysis of the SonicWall revealed that the attacker had placed two files on the device, as illustrated in Figure 1.

![Files left behind by the attacker](/images/sonicwall/overview.png "Files left behind by the attacker")

Figure 1: Files left behind by the attacker

We have identified the file named wafxSummary (refer to Figure 1) as a web shell (MD5 (wafxSummary) = b664a4701731651056c22c8d4cd3ed16). Truesec has extensively discussed this specific scenario in their highly informative blog titled [“Persistent web shell identified in SonicWall SMA”](https://www.truesec.com/hub/blog/web-shell-on-a-sonicwall-sma). The hash of the file mentioned in the Truesec blog matches precisely the file we discovered. Therefore, we will refrain from further elaborating on the details of this file and instead recommend reading the blog post from Truesec for more insight.

Remarkably, in our case, the web shell (wafxSummary) had already been installed on the system by April 25, 2023. The duration between the initial compromise, the compromise of the entire domain, and the ransomware distribution was nearly 11 months.

## wafySummary

A quote from the Truesec blog post mentioned earlier: *“Interestingly enough, two additional file names are present: wafySummary and wafzSummary. These were not present on the device Truesec CSIRT examined”.* [[1]](https://www.truesec.com/hub/blog/web-shell-on-a-sonicwall-sma)

We found no traces of the wafzSummary file either, but we found the file wafySummary (refer to Figure 1 again). This file was copied to the system in November 2023, six months after the web shell was dropped to disk. A straightforward examination of the strings of the binary revealed the following line:

* usage: microsocks -1 -q -i listenip -p port -u user -P password -b bindaddr\_

This leads us to the GitHub repository from [microsocks](https://github.com/rofl0r/microsocks). The microsocks binary from our examined device is available on [VirusTotal](https://www.virustotal.com/gui/file/3bac0ac29941e76d0bafae530fe778e437eeeb90286baed20e2bc9b9d47d233a/detection). The thor scanner flags this binary as *PUA\_MicroSocks\_Proxy\_Server\_Oct21* (screenshot below from VirusTotal).

![Thor Scanner](/images/sonicwall/thor.png "Thor Scanner")

Figure 2: THOR scanner

## Analysis of wafySummary

We transferred the binary from the compromised SonicWall device to an Ubuntu test server in the cloud. We started the binary without any command lines, eliminating the need for a username or password (see the README on the GitHub repository for the exact parameters). We successfully routed the traffic from curl through microsocks (in a first attempt, we tested the connection locally).

```
$ curl --socks5-hostname localhost:1080 'https://api64.ipify.org?format=json'
{"ip":"51.103.213.8"}
```

Port 1080 is the default port used by microsocks, as indicated on the README page of the GitHub repository. Port 1080 is also the default Socks port, visible in the */etc/services* file:

```
/etc/services
2363:socks           1080/tcp   # Socks
2364:socks           1080/udp   # Socks
```

By opening the firewall to our Azure cloud machine where the microsocks proxy is running (as inbound ports are typically restricted by default), we will try to utilize the socks proxy from our local machine.

![Azure: Allow Inbound Ports](/images/sonicwall/allow_inbound.png "Azure: Allow Inbound Ports")

Figure 3: Azure: Allow Inbound Ports

From our local machine, we use curl via the socks proxy on the Azure cloud machine to fetch the IP address of the machine where the socks proxy is installed:

```
% curl --socks5-hostname 51.103.213.8:1080 'https://api64.ipify.org?format=json'
{"ip":"51.103.213.8"}
```

And it worked! In our investigation, the attacker tunneled RDP traffic into the internal network through the compromised SonicWall. Through this access, there was no need for the attacker to place further backdoors in the network, and almost no further malicious code was executed, which would have led to anti-virus or other detections. This access allowed the attacker to operate relatively unnoticed until the encryption of the network was done.

## Conclusion

The attackers exploited a vulnerability that had been publicly available in the Metasploit framework since January 2022 ([pull request](https://github.com/rapid7/metasploit-framework/pull/16041)). Over a year later, the attackers used the vulnerability to gain a foothold in the network by placing a web shell on the SonicWall device. Subsequently, they utilized the microsocks proxy to gain access to the internal network by tunneling traffic through the compromised device.

Another case where (no) patch management, a lack of vulnerability scanning, and missing monitoring was a deadly combination. Florian Roth is right when he writes in his [Cyber Security 2024: Key Trends Beyond the Hype](https://www.nextron-systems.com/2024/01/17/cyber-security-2024-key-trends-beyond-the-hype/) article:

*Attackers are increasingly focusing on systems that arenât usually covered by common security tools like Endpoint Detection and Response (EDR) or Antivirus software. This includes everyday devices like appliances, routers, and IoT (Internet of Things) systems. Since these devices arenât typically monitored by standard security software, they become easy targets for attackers looking to sneak into a network unnoticed.*

To wrap up:

* Ensure that your externally facing applications and devices are promptly patched.
* Proactively scan your network for vulnerabilities, both externally and internally.
* Whenever feasible, deploy an EDR agent or utilize agentless solutions to monitor your devices and hosts for indicators of compromise.

## Indicators of Compromise

| Filename | MD5 |
| --- | --- |
| wafySummary | 203d11d50091900e7c0a872d5a95665c |

Â© 2025 .
Powered by [Hugo blog awesome](https://github.com/hugo-sid/hugo-blog-awesome).