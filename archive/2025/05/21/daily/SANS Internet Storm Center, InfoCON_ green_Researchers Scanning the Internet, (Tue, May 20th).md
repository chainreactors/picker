---
title: Researchers Scanning the Internet, (Tue, May 20th)
url: https://isc.sans.edu/diary/rss/31964
source: SANS Internet Storm Center, InfoCON: green
date: 2025-05-21
fetch_date: 2025-10-06T22:31:51.378582
---

# Researchers Scanning the Internet, (Tue, May 20th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31960)
* [next](/diary/31968)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Researchers Scanning the Internet](/forums/diary/Researchers%2BScanning%2Bthe%2BInternet/31964/)

**Published**: 2025-05-20. **Last Updated**: 2025-05-20 13:59:12 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[2 comment(s)](/diary/Researchers%2BScanning%2Bthe%2BInternet/31964/#comments)

We have been using our data to identify researchers scanning the internet for a few years. Currently, we are tracking 36 groups performing such scans, and our data feed of the IP addresses used contains around 33k addresses [1].

Of course, no clear definition of when a scan is inappropriate exists. Some consider any scan performed nationally and without permission to be unethical. Others have a higher bar, for example, considering scans appropriate if they do not exploit vulnerabilities or cause damage. Legal frameworks vary around the world.

Earlier today, Caleb reminded me of RFC 9511, which I believe offers some good ideas and should be considered if you plan to perform an internet-wide scan [2]. The RFC is entitled "Attribution of Internet Probes." It gets to one of the main issues: Identify yourself if you are performing these scans. This way, if you are causing problems, targets can contact you. This should be a minimum requirement to limit unintentional damage.

Can a simple "scan" cause damage? Of course, it can! We had plenty of examples of such scans causing problems. My favorite example is an old Cisco bug that caused routers to crash if they were scanned with empty UDP packets.

RFC9511 suggests adding a URL to your probe packets and a probe description file at "/.well-known/probing.txt." The IP address the probe originates from should reverse resolve to a hostname, and the probe description file can be found at that hostname. Alternatively, the host the probe originates from should run a web server offering the file. Or the probe description URL should be included as a payload.

For web-based scanning, I see many scanners adding a URL to the user-agent header, which I think fulfills what RFC 9511 is attempting to achieve.

In the past, we have received requests to exclude these scanners from our "Blocklist" (https://isc.sans.edu/block.txt). So far, I have not removed them. But I will consider removing them as long as they are easily identified. There is usually little value in blocking them from your network. If you want to block them, consider our API data at your own risk [1]. But for the most part, I think this feed is more helpful in helping you identify these scanners in your logs to better judge the intention of a particular log entry. Some of our honeypots block these requests as they do not necessarily add value to our data collection, and these scans may make it easier to fingerprint our honeypots.

Most importantly, Before starting your internet-wide scans, consider using existing data. Organizations like Shodan and CENSYS do provide some access to their data and may even share it with researchers.

How do we know if a scan is done for non-malicious purposes? We take people's word for it. Unless we can show malicious intent, if someone claims to scan the internet for research purposes, we believe them. This includes commercial entities that may offer attack surface monitoring to their clients.

And while I was working on this diary, I think I just saw two new organizations I would add to my feed shortly.

[1] https://isc.sans.edu/api/threatcategory/research
[2] https://datatracker.ietf.org/doc/rfc9511/

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [researchers](/tag.html?tag=researchers) [scanners](/tag.html?tag=scanners)

[2 comment(s)](/diary/Researchers%2BScanning%2Bthe%2BInternet/31964/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31960)
* [next](/diary/31968)

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