---
title: Interesting Message Stored in Cowrie Logs, (Wed, Mar 18th)
url: https://isc.sans.edu/diary/rss/32810
source: SANS Internet Storm Center, InfoCON: green
date: 2026-03-19
fetch_date: 2026-03-20T04:09:26.996429
---

# Interesting Message Stored in Cowrie Logs, (Wed, Mar 18th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/32808)

# [Interesting Message Stored in Cowrie Logs](/forums/diary/Interesting%2BMessage%2BStored%2Bin%2BCowrie%2BLogs/32810/)

**Published**: 2026-03-18. **Last Updated**: 2026-03-19 00:38:49 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[1 comment(s)](/diary/Interesting%2BMessage%2BStored%2Bin%2BCowrie%2BLogs/32810/#comments)

This activity was found and reported by BACS student Adam Thorman as part of one of his assignments which I posted his final paper [[1](https://isc.sans.edu/diary/32788)] last week. This activity appeared to only have occurred on the 19 Feb 2026 where at least 2 sensors detected on the same day by DShield sensor in the cowrie logs an echo command that included: "MAGIC\_PAYLOAD\_KILLER\_HERE\_OR\_LEAVE\_EMPTY\_iranbot\_was\_here". My DShield sensor captured activity from source IP [64.89.161.198](https://isc.sans.edu/weblogs/sourcedetails.html?date=2026-02-19&ip=64.89.161.198) between 30 Jan - 22 Feb 2026 that included portscans, a successful login via Telnet (TCP/23) and web access that included all the activity listed below captured by the DShield sensor (cowrie, webhoneypot & iptables logs).

![](https://isc.sans.edu/diaryimages/images/64_89_161_198_pic1.png)

Bot successfully logged in twice into the sensor on the 15 and 19 Feb 2026 via Telnet. The bot activity of interest was a shell script uploaded on the 19 Feb 2026 in an attempt to exploit IoTs and 64-bit Linux systems.

Using Adam [1] grep command, I found in my logs the same script uploaded to the DShield sensor:

ubuntu@vps-711a413c:~/downloads$ sudo cat f1c0e109640d154246d27ff05074365740e994f142ef9846634bec7b18e3b715

**Script Content**
![](https://isc.sans.edu/diaryimages/images/64_89_161_198_pic2.png)

**Cowrie Log**

![](https://isc.sans.edu/diaryimages/images/64_89_161_198_pic3.png)

**Indicators**

64.89.161.198
188.214.30.5
http[:]//188.214.30.5/r.sh
f1c0e109640d154246d27ff05074365740e994f142ef9846634bec7b18e3b715

If you detected the same type of activity, we also appreciate feedback and suggestions about what tool might be used to perform these scans. Please use our [contact](https://isc.sans.edu/contact.html) page to provide feedback.

[1] https://isc.sans.edu/diary/32788
[2] https://www.virustotal.com/gui/file/f1c0e109640d154246d27ff05074365740e994f142ef9846634bec7b18e3b715/detection
[3] https://www.linkedin.com/in/adam-thorman/
[4] https://isc.sans.edu/ipinfo/64.89.161.198
[5] https://isc.sans.edu/weblogs/sourcedetails.html?date=2026-02-19&ip=64.89.161.198
[6] https://isc.sans.edu/ipinfo/188.214.30.5
[7] https://www.shodan.io/host/64.89.161.198
[8] https://www.virustotal.com/gui/ip-address/64.89.161.198/detection
[9] https://github.com/DShield-ISC/dshield
[10] https://github.com/bruneaug/DShield-SIEM/tree/main

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My GitHub Page](https://github.com/bruneaug/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [Analysis](/tag.html?tag=Analysis) [Web Scanning](/tag.html?tag=Web Scanning) [DShield SIEM](/tag.html?tag=DShield SIEM) [DShield sensor](/tag.html?tag=DShield sensor) [Malware](/tag.html?tag=Malware)

[1 comment(s)](/diary/Interesting%2BMessage%2BStored%2Bin%2BCowrie%2BLogs/32810/#comments)

* [previous](/diary/32808)

### Comments

Firewall logs I have checked have shown activity until the 22th of February using telnet, ssh/sftp, http(s), TCP/8080 and other ports. Let's say I saw a few surprises there that warrant further investigation by the receivers of this traffic.

#### hvdk

#### Mar 19th 2026 13 hours ago

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

© 2026 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)