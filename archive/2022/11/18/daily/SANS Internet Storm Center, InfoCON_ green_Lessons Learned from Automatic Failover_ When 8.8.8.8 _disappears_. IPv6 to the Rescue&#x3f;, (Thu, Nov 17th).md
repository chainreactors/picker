---
title: Lessons Learned from Automatic Failover: When 8.8.8.8 "disappears". IPv6 to the Rescue&#x3f;, (Thu, Nov 17th)
url: https://isc.sans.edu/diary/rss/29260
source: SANS Internet Storm Center, InfoCON: green
date: 2022-11-18
fetch_date: 2025-10-03T23:07:49.925239
---

# Lessons Learned from Automatic Failover: When 8.8.8.8 "disappears". IPv6 to the Rescue&#x3f;, (Thu, Nov 17th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29256)
* [next](/diary/29264)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

# [Lessons Learned from Automatic Failover: When 8.8.8.8 "disappears". IPv6 to the Rescue?](/forums/diary/Lessons%2BLearned%2Bfrom%2BAutomatic%2BFailover%2BWhen%2B8888%2Bdisappears%2BIPv6%2Bto%2Bthe%2BRescue/29260/)

**Published**: 2022-11-17. **Last Updated**: 2022-11-17 15:16:05 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Lessons%2BLearned%2Bfrom%2BAutomatic%2BFailover%2BWhen%2B8888%2Bdisappears%2BIPv6%2Bto%2Bthe%2BRescue/29260/#comments)

A famous [XKCD cartoon](https://www.explainxkcd.com/wiki/index.php/1361%3A_Google_Announcement) talks about the importance of the often taken for granted "8.8.8.8" Google DNS server. Like many, I use it often as a quick connectivity check. 8.8.8.8 is an anycast address that exists many times around the globe. I also started to use it for automatic failover on my OPNSense firewall/router.

I am using two uplinks. My primary connection uses Comcast, and recently I started using T-Mobile's 5G Home service as a backup. Overall, I was pleasantly surprised by the T-Mobile service. It competed well with my Comcast service for download speed. I even configured my router to use the T-Mobile service as "primary" for some movie streaming, as it does not have a data cap.

To detect if one of the connections is "down," I am using 75.75.75.75 for the Comcast connection (Comcast's default DNS server) and 8.8.8.8 for T-Mobile. Well... until one day, I had odd issues with the T-Mobile connection. OPNSense had marked it as "down," but the connection appeared to work fine for streaming and other data (also, DNS to 8.8.8.8 didn't work). Just "ping" had high packet loss and the couple of packets that made it had very high latencies:

> `% ping -c 100 8.8.8.8
> ...
> --- 8.8.8.8 ping statistics ---
> 100 packets transmitted, 19 packets received, 81.0% packet loss
> round-trip min/avg/max/stddev = 114.412/181.239/302.607/40.971 ms`

Luckily, Google also runs DoH endpoints on its public DNS servers, so we can verify the results using hping3 and TCP SYN Packets:

> `% sudo hping -S -p 443 8.8.8.8 -c 100
> HPING 8.8.8.8 (en5 8.8.8.8): S set, 40 headers + 0 data bytes
> len=44 ip=8.8.8.8 ttl=115 DF id=36841 sport=443 flags=SA seq=0 win=65535 rtt=52.8 ms
> len=44 ip=8.8.8.8 ttl=114 DF id=37609 sport=443 flags=SA seq=1 win=65535 rtt=50.9 ms
> ...
> --- 8.8.8.8 hping statistic ---
> 100 packets transmitted, 100 packets received, 0% packet loss
> round-trip min/avg/max = 32.2/64.6/96.4 ms`

No packet loss! Reasonably latency! And a "speedtest.com" test showed download speeds of around 200 MBit/sec.

I did some more tests pinging a colocated server and got similar results. The colocated server allowed me to test various other packets:

* Empty ICMP packets (no ICMP header, no payload)
* ICMP error packets
* various random ICMP traffic (fragments, misc type and code combinations, different payload sizes)

None of the packets appear to make it. This is, in particular, an issue if ICMP errors are blocked. Like most LTE/5G ISPs, T-Mobile also does carrier-grade NAT, which adds additional "wrinkles" to their network. I could theoretically use IPv6 over T-Mobile, but the modem they provide only offers a /64 and no "Bridge" mode, so you cannot use IPv6 if you are using your own router with IPv6.

Connecting a system directly to the T-Mobile modem via Wi-Fi shows that ICMPv6 is not blocked:

> `% ping6 2001:4860:4860::8888 -c 100
> PING6(56=40+8+8 bytes) 2607:fb90:be84:750f:285b:6b41:63c6:dc46 --> 2001:4860:4860::8888
> 16 bytes from 2001:4860:4860::8888, icmp_seq=0 hlim=114 time=101.936 ms
> 16 bytes from 2001:4860:4860::8888, icmp_seq=1 hlim=114 time=57.622 ms
> 16 bytes from 2001:4860:4860::8888, icmp_seq=2 hlim=114 time=55.386 ms
> ...
> 100 packets transmitted, 100 packets received, 0.0% packet loss
> round-trip min/avg/max/std-dev = 33.788/67.714/153.129/22.813 ms`

For connection status detection, ICMPv6 will do for now, but there is no way to route T-Mobile IPv6 into my network, and IPv6 failover for a setup like this doesn't exist :(.

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [Tmobile](/tag.html?tag=Tmobile) [ipv6](/tag.html?tag=ipv6)

[0 comment(s)](/diary/Lessons%2BLearned%2Bfrom%2BAutomatic%2BFailover%2BWhen%2B8888%2Bdisappears%2BIPv6%2Bto%2Bthe%2BRescue/29260/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

* [previous](/diary/29256)
* [next](/diary/29264)

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