---
title: A JPEG With A Payload, (Mon, Jun 16th)
url: https://isc.sans.edu/diary/rss/32048
source: SANS Internet Storm Center, InfoCON: green
date: 2025-06-17
fetch_date: 2025-10-06T22:57:00.897985
---

# A JPEG With A Payload, (Mon, Jun 16th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32044)
* [next](/diary/32052)

# [A JPEG With A Payload](/forums/diary/A%2BJPEG%2BWith%2BA%2BPayload/32048/)

**Published**: 2025-06-16. **Last Updated**: 2025-06-16 08:59:44 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/A%2BJPEG%2BWith%2BA%2BPayload/32048/#comments)

Over the weekend, Xavier posted about another image with a payload: "[More Steganography!](https://isc.sans.edu/diary/More%20Steganography%21/32044)".

Xavier did a static analysis, and I want to explain how you can decode the payload if you opted for a dynamic analysis.

During your dynamic analysis, you will notice the download of a JPEG image from hxxps://zynova[.]kesug[.]com/new\_image.jpg.

You can use my tool [jpegdump.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/jpegdump.py) to analyze this file:

![](https://isc.sans.edu/diaryimages/images/20250616-104118.png)

You can see that data is appended (after EOI, End Of Image). Notice \*trailing\*.

This can be selected:

![](https://isc.sans.edu/diaryimages/images/20250616-104200.png)

Notice the TVqQ that Xavier pointed out. That's [BASE64 encoding of MZ](https://isc.sans.edu/diary/22199), the magic header of a PE file.

But the @ character is unexpected. That's not part of the BASE64 standard. So let's do some statistics with [byte-stats.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/byte-stats.py):

![](https://isc.sans.edu/diaryimages/images/20250616-104350.png)

So we see that all the letters appears in this payload, except for letter A. Let's try out an hypothesis: character @ is a substitute for character A.

![](https://isc.sans.edu/diaryimages/images/20250616-104619.png)

That's indeed the case, [base64dump.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/base64dump.py) finds a huge BASE64 string, that once decoded starts with MZ.

If you want to see the SHA256 hash in stead of the MD5 hash, so that we can compare it with what Xavier published, you can set environment variable [DSS\_DEFAULT\_HASH\_ALGORITHMS](https://blog.didierstevens.com/2025/06/06/dss_default_hash_algorithms/).

![](https://isc.sans.edu/diaryimages/images/20250616-104655.png)

And that's the same hash as Xavier published for the .NET DLL.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/A%2BJPEG%2BWith%2BA%2BPayload/32048/#comments)

* [previous](/diary/32044)
* [next](/diary/32052)

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