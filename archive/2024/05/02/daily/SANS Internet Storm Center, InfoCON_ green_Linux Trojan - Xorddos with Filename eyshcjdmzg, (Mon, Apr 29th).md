---
title: Linux Trojan - Xorddos with Filename eyshcjdmzg, (Mon, Apr 29th)
url: https://isc.sans.edu/diary/rss/30880
source: SANS Internet Storm Center, InfoCON: green
date: 2024-05-02
fetch_date: 2025-10-06T17:17:49.186639
---

# Linux Trojan - Xorddos with Filename eyshcjdmzg, (Mon, Apr 29th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/30878)
* [next](/diary/30884)

# [Linux Trojan - Xorddos with Filename eyshcjdmzg](/forums/diary/Linux%2BTrojan%2BXorddos%2Bwith%2BFilename%2Beyshcjdmzg/30880/)

**Published**: 2024-04-29. **Last Updated**: 2024-05-01 01:58:53 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/Linux%2BTrojan%2BXorddos%2Bwith%2BFilename%2Beyshcjdmzg/30880/#comments)

I reviewed a filename I see regularly uploaded to my DShield sensor *eyshcjdmzg* that have been seeing since the 1 October 2023 which has multiple hashes and has been labeled as trojan.xorddos/ddos. These various files have only been uploaded to my DShield sensor by IP 218.92.0.60. Here is the timeline of the activity since 1 October 2023.

![](https://isc.sans.edu/diaryimages/images/eyshcjdmzg_1Oct23_Apr24.PNG)

According to VirusTotal the oldest file submission is b39633ff1928c7f548c6a27ef4265cfd2c380230896b85f432ff15c7c819032c [1] last submitted in Aug 2019 and was uploaded to the DShield sensor only once on the 7 March 2024.

This file can be detected with ET MALWARE DDoS.XOR Checkin via HTTP at Proofpoint Emerging Threats Open.

**Sandbox Analysis**

I submitted file ea40ecec0b30982fbb1662e67f97f0e9d6f43d2d587f2f588525fae683abea73 to a few sandbox including AssemblyLine [[7](https://cybercentrecanada.github.io/assemblyline4_docs/)] to get any and all indicators that were part of this sample:

![](https://isc.sans.edu/diaryimages/images/eyshcjdmzg_Indicators.PNG)

Other indicators appear to include a config file [[5](https://www.virustotal.com/gui/file/b4a86fdf08279318c93a9dd6c61ceafc9ca6e9ca19de76c69772d1c3c89f72a8)] that is used for C2 communications. I compared my results against other online sandbox [[8](https://www.hybrid-analysis.com/sample/ea40ecec0b30982fbb1662e67f97f0e9d6f43d2d587f2f588525fae683abea73/6542ca0426609dce5c06aef5)][[9](https://www.hybrid-analysis.com/sample/f0e4649181ee9917f38233a1d7b6cbb98c9f7b484326f80c1bebc1fa3aef0645/65c332e1c38ced89350a1e94)] and there isn't much that has changed in the most active sample [[1](http://ea40ecec0b30982fbb1662e67f97f0e9d6f43d2d587f2f588525fae683abea73)].

**Indicators - Hashes**

ea40ecec0b30982fbb1662e67f97f0e9d6f43d2d587f2f588525fae683abea73 - 65
cd9bc23360e5ca8136b2d9e6ef5ed503d2a49dd2195a3988ed93b119a04ed3a9 - 2
98e53e2d11d0aee17be3fe4fa3a0159adef6ea109f01754b345f7567c92ebebb - 1
b39633ff1928c7f548c6a27ef4265cfd2c380230896b85f432ff15c7c819032c - 1
ecc33502fa7b65dd56cb3e1b6d3bb2c0f615557c24b032e99b8acd40488fad7c - 1
b4a86fdf08279318c93a9dd6c61ceafc9ca6e9ca19de76c69772d1c3c89f72a8 - lib.xlsx
b4a86fdf08279318c93a9dd6c61ceafc9ca6e9ca19de76c69772d1c3c89f72a8 - lib.xlsxpi.enoan2107[.]com:112

**Indicator - IP**

218.92.0.60
114.114.114.114

**Indicator - Domain**

qq[.]com/lib.asp
qq[.]com/lib.xlsx
qq[.]com/lib.xlsxpi.enoan2107.com:112

**Indicator - Email**

[[email protected]](/cdn-cgi/l/email-protection)

[1] https://www.virustotal.com/gui/file/ea40ecec0b30982fbb1662e67f97f0e9d6f43d2d587f2f588525fae683abea73
[2] https://www.virustotal.com/gui/file/cd9bc23360e5ca8136b2d9e6ef5ed503d2a49dd2195a3988ed93b119a04ed3a9
[3] https://www.virustotal.com/gui/file/98e53e2d11d0aee17be3fe4fa3a0159adef6ea109f01754b345f7567c92ebebb
[3] https://www.virustotal.com/gui/file/b39633ff1928c7f548c6a27ef4265cfd2c380230896b85f432ff15c7c819032c
[4] https://www.virustotal.com/gui/file/ecc33502fa7b65dd56cb3e1b6d3bb2c0f615557c24b032e99b8acd40488fad7c
[5] https://www.virustotal.com/gui/file/b4a86fdf08279318c93a9dd6c61ceafc9ca6e9ca19de76c69772d1c3c89f72a8
[6] https://isc.sans.edu/ipinfo/218.92.0.60
[7] https://cybercentrecanada.github.io/assemblyline4\_docs/
[8] https://www.hybrid-analysis.com/sample/ea40ecec0b30982fbb1662e67f97f0e9d6f43d2d587f2f588525fae683abea73/6542ca0426609dce5c06aef5
[9] https://www.hybrid-analysis.com/sample/f0e4649181ee9917f38233a1d7b6cbb98c9f7b484326f80c1bebc1fa3aef0645/65c332e1c38ced89350a1e94

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My Handler Page](https://handlers.sans.org/gbruneau/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [Xorddos](/tag.html?tag=Xorddos) [ThreatIntel](/tag.html?tag=ThreatIntel) [Malware](/tag.html?tag=Malware) [Analysis](/tag.html?tag=Analysis) [Linux](/tag.html?tag=Linux)

[0 comment(s)](/diary/Linux%2BTrojan%2BXorddos%2Bwith%2BFilename%2Beyshcjdmzg/30880/#comments)

* [previous](/diary/30878)
* [next](/diary/30884)

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