---
title: Scans for Hikvision Intelligent Security API, (Sun, Jul 19th)
url: https://isc.sans.edu/diary/rss/33164
source: SANS Internet Storm Center, InfoCON: green
date: 2026-07-19
fetch_date: 2026-07-20T05:32:41.289099
---

# Scans for Hikvision Intelligent Security API, (Sun, Jul 19th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/33156)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Scans for Hikvision Intelligent Security API](/forums/diary/Scans%2Bfor%2BHikvision%2BIntelligent%2BSecurity%2BAPI/33164/)

**Published**: 2026-07-19. **Last Updated**: 2026-07-19 15:00:38 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Scans%2Bfor%2BHikvision%2BIntelligent%2BSecurity%2BAPI/33164/#comments)

We have been following issues with Hikvision cameras for a [long, long time](https://isc.sans.edu/diary/18071). Like many similar products, Hikvision cameras have a long history of vulnerabilities and are often targeted by internet-wide scans that our honeypot network detects.

This weekend, I noticed a new type of recon scans against the newer OPEN Intelligent Security API (ISAPI) provided by Hikvision cameras. This REST-based API does provide access to a wide range of features. Despite using the word "Intelligent" in its name, the API is not limited to some of the AI/facial recognition functions, but can be used to fully control the camera settings and manage the camera. The API is intended for integration with various third-party products and is well-documented by Hikvision. The ISAPI has been around since at least 2018, but I have only now noticed scans for /ISAPI/System/status, an endpoint that is an obvious choice to profile ISAPI devices. Messages can use XML or JSON. Most examples I have seen use XML.

ISAPI requests are authenticated using Basic or Digest authentication. The cameras support HTTPS, but of course, like for many similar IoT devices, it must first be configured with appropriate keys and certificates. Messages may also be encrypted with AES 128 or 256 in CBC mode. The encryption key is derived from the password, and the iv is exposed in the URL. As a result, the encryption does not provide any additional security if Basic authentication is used and the password is sent in the clear. HTTPS should provide more comprehensive protection.

The URL our sensors noticed this weekend, /ISAPI/System/status, returns XML (or JSON) formatted system information. It is likely a simple way to verify whether the device supports ISAPI (I expect a 401 or 403 response if the URL exists, and a 404 response if it does not), and the URL may be useful for brute-forcing a password.

So far, our honeypots have not captured full requests (not all honeypots do so). I will update this diary if I find some complete requests with authentication data (if included). And as always, do not expose these cameras to the internet, and do not place them in sensitive areas.

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords:

[0 comment(s)](/diary/Scans%2Bfor%2BHikvision%2BIntelligent%2BSecurity%2BAPI/33164/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/33156)

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