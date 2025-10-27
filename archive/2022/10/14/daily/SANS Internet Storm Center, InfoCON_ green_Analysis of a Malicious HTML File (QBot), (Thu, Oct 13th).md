---
title: Analysis of a Malicious HTML File (QBot), (Thu, Oct 13th)
url: https://isc.sans.edu/diary/rss/29146
source: SANS Internet Storm Center, InfoCON: green
date: 2022-10-14
fetch_date: 2025-10-03T19:52:50.465636
---

# Analysis of a Malicious HTML File (QBot), (Thu, Oct 13th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29142)
* [next](/diary/29150)

# [Analysis of a Malicious HTML File (QBot)](/forums/diary/Analysis%2Bof%2Ba%2BMalicious%2BHTML%2BFile%2BQBot/29146/)

**Published**: 2022-10-13. **Last Updated**: 2022-10-13 17:37:42 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[1 comment(s)](/diary/Analysis%2Bof%2Ba%2BMalicious%2BHTML%2BFile%2BQBot/29146/#comments)

Reader Eric submitted a [malicious HTML page](https://www.virustotal.com/gui/file/79cd49dc922c41b2845787c7835063e6ed77507001df133e7d7aafa3d13b6e20) that contains BASE64 images with malware.

Let's take a look. With my tool [base64dump.py](https://blog.didierstevens.com/2022/07/19/update-base64dump-py-version-0-0-23/) I search for long BASE64 strings inside the HTML code:

![](https://isc.sans.edu/diaryimages/images/20221013-180324.png)

Looks like there are indeed 2 images. A GIF and a SVG file.

Let's take a closer look:

![](https://isc.sans.edu/diaryimages/images/20221013-191212.png)

![](https://isc.sans.edu/diaryimages/images/20221013-191241.png)

The GIF file has very high entropy, and no long strings. While the SVG file contains a byte sequence of BASE64 digits that's 596938 bytes long.

So it's very likely that something is hidden in the SVG file.

Let's try a second level of base64 decoding:

![](https://isc.sans.edu/diaryimages/images/20221013-192042.png)

PK: that's probably a ZIP file. Let's try with [zipdump.py](https://blog.didierstevens.com/2022/05/13/update-zipdump-py-version-0-0-22/):

![](https://isc.sans.edu/diaryimages/images/20221013-181259.png)

It's indeed a ZIP file, but it is password protected. Let's grep for the password in the HTML file:

![](https://isc.sans.edu/diaryimages/images/20221013-181315.png)

![](https://isc.sans.edu/diaryimages/images/20221013-181330.png)

Looks like abc333 is the password. Let's try:

![](https://isc.sans.edu/diaryimages/images/20221013-181356.png)

The ZIP file contains an ISO file.

Let's take a look with [isodump.py](https://github.com/DidierStevens/Beta/blob/master/isodump.py):

![](https://isc.sans.edu/diaryimages/images/20221013-181419.png)

![](https://isc.sans.edu/diaryimages/images/20221013-181437.png)

isodump.py only sees one text file. That's very unlickely that a malicious document (it's clear that this is malicious, by now) just contains a text file. What is going on, is that there's a seconday volume decriptor, but the pathlab module that isodump uses, is not capable of recognizing that secondary volume.

As I now expect a Windows executable inside that ISO file, I use [pecheck.py](https://blog.didierstevens.com/2022/05/26/update-pecheck-py-version-0-7-15/) to carve out PE files:

![](https://isc.sans.edu/diaryimages/images/20221013-181506.png)

And indeed, we have a 32-bit DLL, that turns out to be [QBot](https://www.virustotal.com/gui/file/8bf00c146ff533fa193c448d5ccdeb0ba5f56764d290b3de0f55f1b40acf810a).

The 7-zip utility can help us look inside ISO files, but it does not accept an ISO file as input via stdin.

So I first must write the file to disk, and then have 7-zip analyze it:

![](https://isc.sans.edu/diaryimages/images/20221013-181554.png)

![](https://isc.sans.edu/diaryimages/images/20221013-181616.png)

Didier Stevens
Senior handler
Microsoft MVP
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords: [base64](/tag.html?tag=base64) [html](/tag.html?tag=html) [iso](/tag.html?tag=iso) [qbot](/tag.html?tag=qbot) [svg](/tag.html?tag=svg) [zip](/tag.html?tag=zip)

[1 comment(s)](/diary/Analysis%2Bof%2Ba%2BMalicious%2BHTML%2BFile%2BQBot/29146/#comments)

* [previous](/diary/29142)
* [next](/diary/29150)

### Comments

Hello. Thanks for the info. I also dealt with malicious code that embedded some of its unnecessary code in my files (

#### Anonymous

#### Oct 18th 2022 2 years ago

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