---
title: /proxy/ URL scans with IP addresses, (Mon, Mar 16th)
url: https://isc.sans.edu/diary/rss/32800
source: SANS Internet Storm Center, InfoCON: green
date: 2026-03-16
fetch_date: 2026-03-17T04:17:13.171455
---

# /proxy/ URL scans with IP addresses, (Mon, Mar 16th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32796)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/sans-2026/course/application-security-securing-web-apps-api-microservices) | Orlando | Mar 29th - Apr 3rd 2026 |

# [/proxy/ URL scans with IP addresses](/forums/diary/proxy%2BURL%2Bscans%2Bwith%2BIP%2Baddresses/32800/)

**Published**: 2026-03-16. **Last Updated**: 2026-03-16 13:48:54 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/proxy%2BURL%2Bscans%2Bwith%2BIP%2Baddresses/32800/#comments)

Attempts to find proxy servers are among the most common scans our honeypots detect. Most of the time, the attacker attempts to use a host header or include the hostname in the URL to trigger the proxy server forwarding the request. In some cases, common URL prefixes like "/proxy/" are used. This weekend, I noticed a slightly different pattern in our logs:

| First Seen | Last Seen | Count | Path |
| --- | --- | --- | --- |
| 2026-03-15 | 2026-03-16 | 2 | /proxy/http:/[::ffff:a9fe:a9fe]/latest/meta-data/iam/security-credentials/ |
| 2026-03-15 | 2026-03-16 | 2 | /proxy/169.254.169.254/latest/meta-data/iam/security-credentials/ |
| 2026-03-15 | 2026-03-16 | 2 | /proxy/http:/169.254.169.254/latest/meta-data/iam/security-credentials/ |
| 2026-03-15 | 2026-03-16 | 2 | /proxy/absolute/[0:0:0:0:0:ffff:a9fe:a9fe]/latest/meta-data/iam/security-credentials/ |
| 2026-03-15 | 2026-03-16 | 2 | /proxy/absolute/[::ffff:a9fe:a9fe]/latest/meta-data/iam/security-credentials/ |
| 2026-03-15 | 2026-03-16 | 2 | /proxy/absolute/169.254.169.254/latest/meta-data/iam/security-credentials/ |
| 2026-03-15 | 2026-03-16 | 2 | /proxy/[0:0:0:0:0:ffff:a9fe:a9fe]/latest/dynamic/instance-identity/document |
| 2026-03-15 | 2026-03-16 | 2 | /proxy/[0:0:0:0:0:ffff:a9fe:a9fe]/latest/meta-data/iam/security-credentials/ |
| 2026-03-15 | 2026-03-16 | 2 | /proxy/[::ffff:a9fe:a9fe]/latest/dynamic/instance-identity/document |
| 2026-03-15 | 2026-03-16 | 2 | /proxy/[::ffff:a9fe:a9fe]/latest/meta-data/iam/security-credentials/ |
| 2026-03-15 | 2026-03-16 | 2 | /proxy/169.254.169.254/latest/dynamic/instance-identity/document |
| 2026-03-16 | 2026-03-16 | 1 | /proxy/2852039166/latest/meta-data/iam/security-credentials/ |

The intent of these requests is to reach the cloud metadata service, which is typically listening on 169.254.169.254, a non-routable link-local address. The "security-credentials" directory should list entities with access to the service, and can then lead to requests for key material used for authentication.

The attacker does not just use the IPv4 address, but attempts to bypasspass some filters by using the IPv4 mapped IPv6 address. The prefix ::ffff/96, followed by the IPv4 address, is used to express IPv4 addresses in IPv6. Note that these addresses are not intended to be routable, but just like 169.254.169.254 they may work on the host itself. In addition, the attacker is used the "less apprviated" form by specifying the first few bytes with 0:0:0:0. Finally, the long unsigned integer form of the IP address is used.

The meta data service is often exploited using SSRF vulenrabilities. However, the more modern "version 2" of the meta data service is attempting to prevent simple SSRF attacks by requiring two requests with different methods and specific custom headers. SSRF vulnerabilities are just like a less functional open proxy. In this case, the attacker assumes a full proxy, and an attack may not be prevented by the more modern meta data service implementation.

Modern web applications use proxies in many different forms. For example you may have API gateways, load balancers, web application firewalls or even still some proxies to bypass CORS constraints. Any of these cases is potentially vulenrable if badly configured. The above list of URLs may make a good starting point to test the implementation of your proxy.

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [proxy](/tag.html?tag=proxy)

[0 comment(s)](/diary/proxy%2BURL%2Bscans%2Bwith%2BIP%2Baddresses/32800/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/sans-2026/course/application-security-securing-web-apps-api-microservices) | Orlando | Mar 29th - Apr 3rd 2026 |

* [previous](/diary/32796)

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

© 2026 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)