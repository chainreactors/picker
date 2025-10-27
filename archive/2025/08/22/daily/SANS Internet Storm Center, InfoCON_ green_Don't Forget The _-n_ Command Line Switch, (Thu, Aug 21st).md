---
title: Don't Forget The "-n" Command Line Switch, (Thu, Aug 21st)
url: https://isc.sans.edu/diary/rss/32220
source: SANS Internet Storm Center, InfoCON: green
date: 2025-08-22
fetch_date: 2025-10-07T00:48:38.747414
---

# Don't Forget The "-n" Command Line Switch, (Thu, Aug 21st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32216)
* [next](/diary/32224)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Don't Forget The "-n" Command Line Switch](/forums/diary/Dont%2BForget%2BThe%2Bn%2BCommand%2BLine%2BSwitch/32220/)

**Published**: 2025-08-21. **Last Updated**: 2025-08-21 06:13:16 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Dont%2BForget%2BThe%2Bn%2BCommand%2BLine%2BSwitch/32220/#comments)

A lot of people like the command line, the CLI, the shell (name it as you want) because it provides a lot of powerful tools to perform investigations. The best example is probably parsing logs! Even if we have SIEM to ingest and process them, many people still fall back to the good old suite of grep, cut, awk, sort, uniq, and many more.

They are also many tools that help to process network data like PCAP files or more log files. Most of them offer plenty of command line switches to change their behavior but there is one that remain interesting to use in some cases: the “-n”!

If there is not standardization of command line switches, many tools use “-n” in the same way: It disables DNS resolution of IP addresses. The following tools have this switch:

* tcpdump
* tshark
* ngrep
* iftop
* nethogs
* nmap
* masscan
* arping
* ping
* netstat
* ss
* lsof
* fuser
* conntrack
* iptables
* ip
* route

They are probable many more!

The risk is the following: If a tool tries to resolve an IP address into its FQDN (Fully Qualified Domain Name), and if the PTR[[1](https://www.nslookup.io/learning/dns-record-types/ptr/)] record is delegated to the attacker, he or she may become aware that investigations against the infrastructure are ongoing. Some ISPs implement sub-delegation[[2](https://simpledns.plus/kb/77-how-to-sub-delegate-a-reverse-zone-ipv4)] of reverse DNS to their customers. This means that PTR records can be managed by customers and they could log attempts to resolve in-addr.arpa records!

Example:

```

$ dig -x 23.30.39.252 @192.168.254.8

; <<>> DiG 9.10.6 <<>> -x 23.30.39.252 @192.168.254.8
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 19658
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;252.39.30.23.in-addr.arpa.    IN    PTR

;; ANSWER SECTION:
252.39.30.23.in-addr.arpa. 3582    IN    PTR    23-30-39-252-static.hfc.comcastbusiness.net.

;; Query time: 8 msec
;; SERVER: 192.168.254.8#53(192.168.254.8)
;; WHEN: Thu Aug 21 08:01:45 CEST 2025
;; MSG SIZE  rcvd: 111
```

The DNS resolver handling PTR records for this zone will log:

```

21-Aug-2025 08:01:45.856 queries: info: client @0x7fd5287c0688 192.168.254.218#64869 (252.39.30.23.in-addr.arpa): query: 252.39.30.23.in-addr.arpa IN PTR +E(0) (192.168.254.8)
```

The attacker knows that his/her IP address is being investigated and your IP address can also be disclosed (another good reason to always use a dedicated/anonymous system)

Note that the opposite is also dangerous. Imagine you find a script containing an arrary of three domains:

```

c2 = [ "domain1.top", "domain2.xyz", "domain3.cx" ]
```

You can be tempted to resolve all domains but only the last one is the effective C2 server and the others are decoys. The malware should never use them. If you try to resolve them and the attacker controls the primary domain, you'll be spotted!

[1] <https://www.nslookup.io/learning/dns-record-types/ptr/>
[2] <https://simpledns.plus/kb/77-how-to-sub-delegate-a-reverse-zone-ipv4>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [DNS](/tag.html?tag=DNS) [FQDN](/tag.html?tag=FQDN) [PTR](/tag.html?tag=PTR) [Resolver](/tag.html?tag=Resolver)

[0 comment(s)](/diary/Dont%2BForget%2BThe%2Bn%2BCommand%2BLine%2BSwitch/32220/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/32216)
* [next](/diary/32224)

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