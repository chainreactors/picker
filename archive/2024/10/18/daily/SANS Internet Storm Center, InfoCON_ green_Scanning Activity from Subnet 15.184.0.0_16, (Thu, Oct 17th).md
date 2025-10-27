---
title: Scanning Activity from Subnet 15.184.0.0/16, (Thu, Oct 17th)
url: https://isc.sans.edu/diary/rss/31362
source: SANS Internet Storm Center, InfoCON: green
date: 2024-10-18
fetch_date: 2025-10-06T18:56:51.296212
---

# Scanning Activity from Subnet 15.184.0.0/16, (Thu, Oct 17th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31360)
* [next](/diary/31372)

# [Scanning Activity from Subnet 15.184.0.0/16](/forums/diary/Scanning%2BActivity%2Bfrom%2BSubnet%2B151840016/31362/)

**Published**: 2024-10-17. **Last Updated**: 2024-10-17 19:40:44 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/Scanning%2BActivity%2Bfrom%2BSubnet%2B151840016/31362/#comments)

I noticed in my logs 2 weeks ago regular probe from a subnet in the Amazon cloud only scanning for TCP/8080 capture by the iptables of my DShield sensor. The scanning started on the 15 Aug - 4 Oct 2024 where the sensor recorded **1046** individual IPs from this network.

![](https://isc.sans.edu/diaryimages/images/15_184_15Aug-4Oct2024.PNG)

The IP use the most was 15.184.38.31 that was initially recorded on the 15 Aug 2024 and the recorded almost daily between the 3 Sep - 4 Oct 2024.

![](https://isc.sans.edu/diaryimages/images/15_184_3Sep-4Oct2024.PNG)

Since I have so much data about this single IP, the other thing I was curious about if the Time to Live (TTL) would be centered around the same cluster every time this source would be recorded. The data shows (picture below) shows it was consistently between ~85-118 with some outlier with a TTL of 193 indicating some packets started with a higher TTL. It seems unlikely these outliers would have started with a TTL of 255, that would be 62 hops away.

![](https://isc.sans.edu/diaryimages/images/15_184_38_31_15Aug-4Oct2024.PNG)

I picked the data from the 29 Sep 2024 to look at some of the inbound SYN packets for some clues and found the maximum segment size ([MSS](https://en.wikipedia.org/wiki/Maximum_segment_size)) wasn't the same for all traffic. Today, most traffic has a default MSS normally set to 1500, however, there can be exceptions.

The default TCP Maximum Segment Size in RFC 879 shows for IPv4 is 536. TTL 193 had a MSS of 536 set to the default which it isn't the norme but possible:

![](https://isc.sans.edu/diaryimages/images/mss536_29Sep24.PNG)

The TTL for all other traffic on the 29 Sep range between 80 to 110 and had an MSS of 1452:

![](https://isc.sans.edu/diaryimages/images/mss1452_29Sep24.PNG)

Why 1452? Where is the missing 8 bytes? Point-to-Point Protocol over Ethernet ([PPPoE](https://datatracker.ietf.org/doc/html/rfc2516)) is one that needs those additional 8 bytes and truncates the Ethernet MTU to 1492 to route traffic between the host and the server. However, I have no way to confirm here if this is coming from a PPPoE or some other device but this is one possibility.
If you have a honeypot, packet capture [[1](https://github.com/bruneaug/DShield-SIEM/blob/main/AddOn/packet_capture.md)] is always a friend and useful to see what the logs don’t capture.

[1] https://github.com/bruneaug/DShield-SIEM/blob/main/AddOn/packet\_capture.md
[2] https://en.wikipedia.org/wiki/Maximum\_segment\_size
[3] https://datatracker.ietf.org/doc/html/rfc2516

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My Handler Page](https://handlers.sans.org/gbruneau/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [Cowrie](/tag.html?tag=Cowrie) [IPTables](/tag.html?tag=IPTables) [MSS](/tag.html?tag=MSS) [packet](/tag.html?tag=packet) [PPPoE](/tag.html?tag=PPPoE) [Traffic Analysis](/tag.html?tag=Traffic Analysis) [TTL](/tag.html?tag=TTL)

[0 comment(s)](/diary/Scanning%2BActivity%2Bfrom%2BSubnet%2B151840016/31362/#comments)

* [previous](/diary/31360)
* [next](/diary/31372)

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