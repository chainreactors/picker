---
title: &#x5b;Guest Diary&#x5d; Distracting the Analyst for Fun and Profit, (Tue, Sep 23rd)
url: https://isc.sans.edu/diary/rss/32308
source: SANS Internet Storm Center, InfoCON: green
date: 2025-09-24
fetch_date: 2025-10-02T20:35:50.452640
---

# &#x5b;Guest Diary&#x5d; Distracting the Analyst for Fun and Profit, (Tue, Sep 23rd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jesse La Grew](/handler_list.html#jesse-la-grew "Jesse La Grew")

Threat Level: [green](/infocon.html)

* [previous](/diary/32302)
* [next](/diary/32310)

# [[Guest Diary] Distracting the Analyst for Fun and Profit](/forums/diary/Guest%2BDiary%2BDistracting%2Bthe%2BAnalyst%2Bfor%2BFun%2Band%2BProfit/32308/)

**Published**: 2025-09-23. **Last Updated**: 2025-09-23 12:55:18 UTC
**by** [Jesse La Grew](/handler_list.html#jesse-la-grew) (Version: 1)

[1 comment(s)](/diary/Guest%2BDiary%2BDistracting%2Bthe%2BAnalyst%2Bfor%2BFun%2Band%2BProfit/32308/#comments)

[This is a Guest Diary by Taylor House, an ISC intern as part of the SANS.edu Bachelor's Degree in Applied Cybersecurity (BACS) program [1].]

Distributed denial of service (DDoS) attacks are a type of cyber-attack where the threat actor attempts to disrupt a service by flooding the target with a ton of requests to overload system resources and prevent legitimate traffic from reaching it. From March 31st until April 20th of this year, my honeypot went under a constant barrage of TCP SYN packets over port 443. This post seeks to go over this attack and share observations proving how looks can be deceiving.

In total, this attack sent **2389339** packets from **6039** hosts. The attack came over a series of three waves, with no relation other than the destination port and the flag that was set. A sample was taken from the first of these waves, and each packet was found to have these properties:

* A total length of 60 bytes.
* Targeted port 443 using the TCP protocol.
* Had the SYN flag and no other flags set.
* Had a window size of 32768.
* Had a maximum segment size of 1460 bytes.
* A trailer in the Ethernet header containing 2 bytes of padding.

**![](https://isc.sans.edu/diaryimages/images/2025-09-23_figure1.PNG)
Figure 1. Wireshark output displaying a sample of packets from wave 1.**

## The First Wave

The first wave occurred from March 31st until April 4th, sending **647069** packets from **743** hosts. The top 10 hosts from this wave were:

| Host | Number of Packets |
| --- | --- |
| [103.15.246.198](/ipinfo.html?ip=103.15.246.198) | 1030 |
| [103.15.247.87](/ipinfo.html?ip=103.15.247.87) | 1028 |
| [103.15.247.17](/ipinfo.html?ip=103.15.247.17) | 1028 |
| [103.15.247.111](/ipinfo.html?ip=103.15.247.111) | 1028 |
| [103.15.245.80](/ipinfo.html?ip=103.15.245.80) | 1028 |
| [103.15.245.249](/ipinfo.html?ip=103.15.245.249) | 1028 |
| [103.15.245.239](/ipinfo.html?ip=103.15.245.239) | 1028 |
| [103.15.245.169](/ipinfo.html?ip=103.15.245.169) | 1028 |
| [103.15.245.0](/ipinfo.html?ip=103.15.245.0) | 1028 |
| [103.15.247.93](/ipinfo.html?ip=103.15.247.93) | 1027 |
| **Total** | **10281** |

**Figure 2. Top 10 hosts from wave 1 by number of packets sent.**

An overwhelming majority of the hosts (86%) were within the IP address range 103.15.245.0-103.15.247.99. Of those hosts, 36 of them had domain name entries. All these hosts are assigned to Summit Communications, an ISP located in Bangladesh. Of those 36 hosts, Shodan intelligence [2] shows multiple possible vulnerabilities due to outdated software such as:

* `dropband[.]summitiig[.]net` is running a web server on Apache version 2.4.18 and may be vulnerable to critical vulnerabilities such as buffer overflow attacks and remote code execution attacks that enable attackers to exert direct control over the system through the web server. [3,4]
* `mrtg[.]summitiig[.]net` is running an even older version of Apache, version 2.2.15, and may be vulnerable to vulnerabilities such as buffer overflow and reading process memory. [5,6]

## Crafted Packets?

It is possible that this could be the result of a botnet. However, with only a minority of hosts having domain names or clearly exposed services, another possible explanation is the connections were spoofed. The consistent size and attributes of the packets, including window size and maximum segment size, is a sign this might be happening because of packet crafting using a tool like Scapy. Packet crafting is a process for sending fake packets to a target with custom fields. Suppose I craft a packet to send to my loopback address using the following commands. Padding can be any value, since there are two random bytes that can be found at the end of each packet:

```

packet = IP(src=RandIP(), dst='127.0.0.0')/TCP(sport=RandShort(), dport=443, window=32768, options=[('MSS',1460)])/Padding('\x00\x00')
send(packet, iface=?lo?) #Repeat many times?
```

What we find on the other side is the following:

**![](https://isc.sans.edu/diaryimages/images/2025-09-23_figure2.PNG)
Figure 3. Screenshot of the crafted packets captured in Wireshark.**

Shockingly similar to the observed activity! This proves that packet crafting may have a role to play in this attack.

## The Second Wave

The second wave occurred from April 7th until April 14th, sending 885209 packets from 1054 hosts. The top 10 hosts from this wave were:

| Host | Number of |
| --- | --- |
| [86.105.145.100](/ipinfo.html?ip=86.105.145.100) | 8375 |
| [86.105.144.104](/ipinfo.html?ip=86.105.144.104) | 8373 |
| [86.105.145.254](/ipinfo.html?ip=86.105.145.254) | 8372 |
| [86.105.145.205](/ipinfo.html?ip=86.105.145.205) | 8371 |
| [86.105.145.135](/ipinfo.html?ip=86.105.145.135) | 8371 |
| [86.105.145.37](/ipinfo.html?ip=86.105.145.37) | 8370 |
| [86.105.145.16](/ipinfo.html?ip=86.105.145.16) | 8370 |
| [86.105.144.83](/ipinfo.html?ip=86.105.144.83) | 8370 |
| [86.105.144.167](/ipinfo.html?ip=86.105.144.167) | 8370 |
| [86.105.144.132](/ipinfo.html?ip=86.105.144.132) | 8370 |
| **Total** | **83712** |

**Figure 4. Top 10 hosts from wave 2 by number of packets sent.**

This wave had both more hosts and each host sent more packets, demonstrating a slight increase in the rate of packets sent. The majority of hosts (60%) were from the IP range 85.194.196.1-85.194.198.99. All these hosts are assigned to ScopeSky, an ISP located in Iraq. CloudFlare reports a spike in Layer 7 attacks sourcing from ScopeSky’s autonomous systems number for the period of this attack, suggesting that many attacks involving the application layer, like web application firewall bypasses and DdoS attacks are coming from this autonomous systems number over the period relative to previous periods [7].

**![](https://isc.sans.edu/diaryimages/images/2025-09-23_figure3.PNG)
Figure 5. Application layer attack volume change relative to the previous period from AS50597: ScopeSky [7].**

## Is this a new botnet?

The chance these are the legitimate sources is low. Given that it makes up a third of the address space assigned to ScopeSky, this would be a major incident for the company and would make the news. This proves that threat actors can spoof their traffic to make it look like it is coming from another source, but an 1800% increase is very unrealistic for it to appear like a legitimate threat.

## The Third Wave

The third wave occurred from April 16th until April 20th, sending 857061 packets from 4242 hosts. The top 10 hosts from this wave were:

| Host | Number of Packets |
| --- | --- |
| [176.241.82.245](/ipinfo.html?ip=176.241.82.245) | 262 |
| [176.241.89.194](/ipinfo.html?ip=176.241.89.194) | 261 |
| [176.241.82.87](/ipinfo.html?ip=176.241.82.87) | 261 |
| [176.241.87.173](/ipinfo.html?ip=176.241.87.173) | 259 |
| [176.241.85.61](/ipinfo.html?ip=176.241.85.61) | 257 |
| [176.241.85.40](/ipinfo.html?ip=176.241.85.40) | 256 |
| [176.241.84.153](/ipinfo.html?ip=176.241.84.153) | 256 |
| [176.241.88.35](/ipinfo.html?ip=176.241.88.35) | 254 |
| [176.241.82.90](/ipinfo.html?ip=176.241.82.90) | 254 |
| [176.241.91.8](/ipinfo.html?ip=176.241.91.8)9 | 253 |
| Total | 2573 |

**Figure 6. Top 10 hosts from wave 3 by number of packets sent.**

An overwhelming majority of hosts (96%) came from the ip range 176.241.80.0-176.241.95.99. These ranges are covered by two autonomous systems numbers: AS57588, mana...