---
title: Attempts to Bypass CDNs, (Wed, Dec 3rd)
url: https://isc.sans.edu/diary/rss/32532
source: SANS Internet Storm Center, InfoCON: green
date: 2025-12-03
fetch_date: 2025-12-04T03:19:38.978094
---

# Attempts to Bypass CDNs, (Wed, Dec 3rd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/32524)
* [next](/diary/32536)

My next class:

|  |  |  |
| --- | --- | --- |
| [Network Monitoring and Threat Detection In-Depth](https://www.sans.org/event/sec503-europe-online-december-2025/course/network-monitoring-threat-detection) | Online | Central European Time | Dec 15th - Dec 20th 2025 |

# [Attempts to Bypass CDNs](/forums/diary/Attempts%2Bto%2BBypass%2BCDNs/32532/)

**Published**: 2025-12-03. **Last Updated**: 2025-12-03 19:31:22 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Attempts%2Bto%2BBypass%2BCDNs/32532/#comments)

Currently, in order to provide basic DDoS protection and filter aggressive bots, some form of Content Delivery Network (CDN) is usually the simplest and most cost-effective way to protect a web application. In a typical setup, DNS is used to point clients to the CDN, and the CDN will then forward the request to the actual web server. There are a number of companies offering services like this, and cloud providers will usually have solutions like this as well.

However, this setup comes with a significant weakness: If an attacker can identify the IP address of the actual web server, they are often able to bypass the CDN and reach the web server directly. There are a few ways to prevent this. Depending on the CDN selected, it may be possible to allow access only from the CDN's IP address space. However, for some of the larger providers, this list of addresses may be large and very dynamic. Another option is to add custom headers. Some CDNs offer special custom headers with randomized values to identify requests that passed through the CDN. A less secure (lazier?) option is to look for any header that identifies the CDN. This last option should be avoided, as attackers can easily include this header.

In recent days, our honeypots detected an uptick of requests that included these CDN-related headers, indicating that attackers may attempt to bypass this protection. For example:

### Cf-Warp-Tag-Id

This header started showing up yesterday and is associated with Cloudflare's "Warp" VPN service. The scans do include a random-looking value, but may count on the value to either not be verified, or the request actually went through the Cloudflare Warp VPN to obfuscate its source.

### X-Fastly-Request-Id

As the name implies, this header is associated with the Fastly CDN. It started showing up in our data on November 20th.

### X-Akamai-Transformed

A header added by Akamai. Also started showing up on November 20th (so are the remaining headers)

### X-T0Ken-Inf0

Not sure what this header is used for (any ideas? Let me know). It looks like it could contain some form of authentication token, but the "l33t spelling" is odd.

### x-sfdc-request-id x-sfdc-lds-endpoints

These headers are used by Salesforce to track requests.

Around the same time, we also started seeing a lot of headers starting with the string "Xiao9-", but I have no idea what they are used for. If anybody has any ideas, please let me know :)

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [CDN headers](/tag.html?tag=CDN headers)

[0 comment(s)](/diary/Attempts%2Bto%2BBypass%2BCDNs/32532/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Network Monitoring and Threat Detection In-Depth](https://www.sans.org/event/sec503-europe-online-december-2025/course/network-monitoring-threat-detection) | Online | Central European Time | Dec 15th - Dec 20th 2025 |

* [previous](/diary/32524)
* [next](/diary/32536)

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