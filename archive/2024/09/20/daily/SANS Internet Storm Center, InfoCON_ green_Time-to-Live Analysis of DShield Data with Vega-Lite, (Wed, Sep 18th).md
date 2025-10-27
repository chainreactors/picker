---
title: Time-to-Live Analysis of DShield Data with Vega-Lite, (Wed, Sep 18th)
url: https://isc.sans.edu/diary/rss/31278
source: SANS Internet Storm Center, InfoCON: green
date: 2024-09-20
fetch_date: 2025-10-06T18:30:49.191750
---

# Time-to-Live Analysis of DShield Data with Vega-Lite, (Wed, Sep 18th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31276)
* [next](/diary/31282)

# [Time-to-Live Analysis of DShield Data with Vega-Lite](/forums/diary/TimetoLive%2BAnalysis%2Bof%2BDShield%2BData%2Bwith%2BVegaLite/31278/)

**Published**: 2024-09-18. **Last Updated**: 2024-09-19 00:20:09 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 2)

[1 comment(s)](/diary/TimetoLive%2BAnalysis%2Bof%2BDShield%2BData%2Bwith%2BVegaLite/31278/#comments)

Since posting a diary about Vega-Lite [[1](https://isc.sans.edu/diary/VegaLite%2Bwith%2BKibana%2Bto%2BParse%2Band%2BDisplay%2BIP%2BActivity%2Bover%2BTime/31210/)], I have "played" with other queries that might be interesting and the first one that I wanted to explore since the DShield SIEM [[2](https://github.com/bruneaug/DShield-SIEM/tree/main)] capture and parse the iptables logs and store the Time-to-Live (TTL) for analysis.

One of the things I was really curious about, whether any of the source IPs my DShield sensor capture, have more than one or multiple TTL. I started looking at some of the traffic to review the activity of some of the IPs and noticed that infact some have multiple TTL either in the same day or multiple days. One of the ELK dashboard displays the TTL with their Total, the traffic I reviewed was from IP [45.148.10[.]242](https://isc.sans.edu/ipinfo/45.148.10.242) to port TCP/8080 scanning every day for /login.cgi and /cgi-bin/luci/;stok=/locale. In order to better see this activity over the past 14 days; I use a vega-lite query to display the activity with this graph.

First, this first picture shows all the TTL in the past 2 weeks of activity by Total for IP 45.148.10[.]242 :

![](https://isc.sans.edu/diaryimages/images/ttl_total_pic1.PNG)

The TTL 50 is likely a outlier from likely the default 51. Anything in the two 200+ might need to review the IP packet ID to get some clues.

This shows the TTL in the past 2 weeks with vega-lite, the darker the color the more activity for that time period:

![](https://isc.sans.edu/diaryimages/images/ttl_pic1.PNG)

While reviewing DShield sensor data, I like sometimes to look at some of the other data captured by the honeypot, and explore why some of the traffic by each IPs might be coming from different directions by using the TTL for some clues. In this example, why is the TTL sometimes different? What other route is the IP taking? Is VPN involved?

I took one of the TTL, in this case 239 and reviewed when it was captured by the sensor. The sensor received the first one on the 7 Sep and the second on the 11 Sep 2024. I review the 1 hour period this TTL was capture and 5 other packets with TTL 51 was also capture during that same one hour period. Is TTL 239 2 lost packet?

![](https://isc.sans.edu/diaryimages/images/ttl_pic2.PNG)

[1] https://isc.sans.edu/diary/VegaLite+with+Kibana+to+Parse+and+Display+IP+Activity+over+Time/31210/
[2] https://github.com/bruneaug/DShield-SIEM/tree/main
[3] https://vega.github.io/vega/examples/
[4] https://github.com/DShield-ISC/dshield
[5] https://isc.sans.edu/ipinfo/45.148.10.242

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My Handler Page](https://handlers.sans.org/gbruneau/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [Analysis](/tag.html?tag=Analysis) [ELK](/tag.html?tag=ELK) [infosec](/tag.html?tag=infosec) [SIEM](/tag.html?tag=SIEM) [TimetoLive](/tag.html?tag=TimetoLive) [TTL](/tag.html?tag=TTL) [VegaLite](/tag.html?tag=VegaLite)

[1 comment(s)](/diary/TimetoLive%2BAnalysis%2Bof%2BDShield%2BData%2Bwith%2BVegaLite/31278/#comments)

* [previous](/diary/31276)
* [next](/diary/31282)

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