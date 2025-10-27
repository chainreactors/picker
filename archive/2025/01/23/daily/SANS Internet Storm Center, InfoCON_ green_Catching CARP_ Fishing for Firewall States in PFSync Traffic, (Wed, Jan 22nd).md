---
title: Catching CARP: Fishing for Firewall States in PFSync Traffic, (Wed, Jan 22nd)
url: https://isc.sans.edu/diary/rss/31616
source: SANS Internet Storm Center, InfoCON: green
date: 2025-01-23
fetch_date: 2025-10-06T20:12:01.345768
---

# Catching CARP: Fishing for Firewall States in PFSync Traffic, (Wed, Jan 22nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31612)
* [next](/diary/31620)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Catching CARP: Fishing for Firewall States in PFSync Traffic](/forums/diary/Catching%2BCARP%2BFishing%2Bfor%2BFirewall%2BStates%2Bin%2BPFSync%2BTraffic/31616/)

**Published**: 2025-01-22. **Last Updated**: 2025-01-22 18:14:30 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Catching%2BCARP%2BFishing%2Bfor%2BFirewall%2BStates%2Bin%2BPFSync%2BTraffic/31616/#comments)

Legend has it that in the Middle Ages, monchs raised carp to be as "round" as possible. The reason was that during Lent, one could only eat as much as fit on a plate, and the round shape of a carp gave them the most "fish per plate". But we are not here to exchange recipes. I want to talk about CARP and the network failover feature.

CARP stands for Common Address Redundancy Protocol [1]. OpenBSD developed it as a free alternative to similar commercial protocols. It is typically used to manage the failover between two firewalls. CARP deals, first of all, with managing the IP address handover. But for a seamless handover, the two firewalls must also synchronize state. This is where PFSYNC comes in. PFSYNC allows the primary firewall to notify the secondary firewall of any changes in the connection state. This way, the secondary firewall is aware of established connections and can pick up where the primary firewall left off in case of a failover.

A dedicated network link is highly recommended for CARP/PFSYNC traffic. The amount of traffic can be substantial, and as you will see, the information is sensitive and needs to be protected. The PFSYNC protocol is in the clear and (spoiler alert!) easily decoded. Using a dedicated network link will limit the risk of the data landing in the wrong hands.

PFSYNC traffic is unicast and uses protocol 240. IANA considers protocol 240 unassigned [2]. PFSYNC packets have a TTL of 255, likely to prevent spoofing of messages from sources outside the current network.

I found one document that describes pfsync well [3]. It is based on posts to the OpenBSD journal and includes code snippets for more background. The document was created to outline some changes from PFSYNC 4 to 5.

The payload starts with a version, a length field (size of the message in bytes), and an MD5 message hash. The MD5 hash is meant to be used as a checksum. The current version of PFSYNC is 5. Version 4 and older would include a message type and count next. However, version 5 allows multiple message types per packet. Next follows a "subheader" describing the next set of messages.

Each subheader starts with a message type and length (= number of messages). IP addresses always use 16 Bytes, suitable for IPv6. IPv4 addresses are just zero-padded.

Analyzing these messages is made a. bit more challenging by Wireshark not decoding PFSYNC. However, some tcpdump versions will do so. Below is an example including the decode from tcpdump on an OPNsense system:

![example pfsync packet as decoded by tcpdump on OPNsense](https://isc.sans.edu/diaryimages/images/Screenshot%202025-01-22%20at%201_04_36%E2%80%AFPM.png)

You should probably open the image in a new tab.

The two firewalls have the IP addresses 192.0.2.2 and 192.0.2.3. There are first three new states added. You will see the traffic to DNS servers. Next, seven compressed messages that are updated.

The data contained in PFSYNC is a bit like netflow. It provides information about session states, IP addresses, and ports. You may be able to derive details about the duration of sessions. The amount of traffic exchanged is not communicated. The Window Scale and some sequence number information are included for TCP, but I need to dive into that a bit more (it may indicate the amount of data transmitted).

Let me know if you want to learn more about decoding this traffic, and I may record a quick "Packet Tuesday" style video about PFSYNC.

[1] https://www.openbsd.org/faq/pf/carp.html
[2] https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml
[3] https://www.openbsd.org/papers/pfsync\_v5.pdf

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [pfsync](/tag.html?tag=pfsync) [carp](/tag.html?tag=carp)

[0 comment(s)](/diary/Catching%2BCARP%2BFishing%2Bfor%2BFirewall%2BStates%2Bin%2BPFSync%2BTraffic/31616/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31612)
* [next](/diary/31620)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2025 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)