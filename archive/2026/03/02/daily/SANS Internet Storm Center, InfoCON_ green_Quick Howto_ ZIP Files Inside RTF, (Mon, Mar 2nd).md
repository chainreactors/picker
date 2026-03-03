---
title: Quick Howto: ZIP Files Inside RTF, (Mon, Mar 2nd)
url: https://isc.sans.edu/diary/rss/32696
source: SANS Internet Storm Center, InfoCON: green
date: 2026-03-02
fetch_date: 2026-03-03T04:13:34.603496
---

# Quick Howto: ZIP Files Inside RTF, (Mon, Mar 2nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Didier Stevens](/handler_list.html#didier-stevens "Didier Stevens")

Threat Level: [green](/infocon.html)

* [previous](/diary/32692)
* [next](/diary/32700)

# [Quick Howto: ZIP Files Inside RTF](/forums/diary/Quick%2BHowto%2BZIP%2BFiles%2BInside%2BRTF/32696/)

**Published**: 2026-03-02. **Last Updated**: 2026-03-02 11:13:04 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[1 comment(s)](/diary/Quick%2BHowto%2BZIP%2BFiles%2BInside%2BRTF/32696/#comments)

In diary entry "[Quick Howto: Extract URLs from RTF files](https://isc.sans.edu/diary/Quick%20Howto%3A%20Extract%20URLs%20from%20RTF%20files/32692)" I mentioned ZIP files.

There are OLE objects inside this RTF file:

![](https://isc.sans.edu/diaryimages/images/20260209-124939.png)

![](https://isc.sans.edu/diaryimages/images/20260209-124956.png)

![](https://isc.sans.edu/diaryimages/images/20260209-125102.png)

They can be analyzed with [oledump.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/oledump.py) like this:

![](https://isc.sans.edu/diaryimages/images/20260209-125403.png)

Options --storages and -E %CLSID% are used to show the abused CLSID.

![](https://isc.sans.edu/diaryimages/images/20260209-125518.png)

Stream CONTENTS contains the URL:

![](https://isc.sans.edu/diaryimages/images/20260209-125609.png)

We extracted this URL with the method described in my previous diary entry "[Quick Howto: Extract URLs from RTF files](https://isc.sans.edu/diary/Quick%20Howto%3A%20Extract%20URLs%20from%20RTF%20files/32692)".

But this OLE object contains a .docx file.

![](https://isc.sans.edu/diaryimages/images/20260209-125740.png)

![](https://isc.sans.edu/diaryimages/images/20260209-125928.png)

A .docx file is a ZIP container, and thus the URLs it contains are inside compressed files, and will not be extracted with the technique I explained.

But this file can be looked into with [zipdump.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/zipdump.py):

![](https://isc.sans.edu/diaryimages/images/20260209-130005.png)

It is possible to search for ZIP files embedded inside RTF files: 50 4B 03 04 -> hex sequence of magic number header for file record in ZIP file.

![](https://isc.sans.edu/diaryimages/images/20260209-130139.png)

Search for all embedded ZIP files:

![](https://isc.sans.edu/diaryimages/images/20260209-130412.png)

Extract URLs:

![](https://isc.sans.edu/diaryimages/images/20260209-130600.png)

![](https://isc.sans.edu/diaryimages/images/20260209-130636.png)

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[1 comment(s)](/diary/Quick%2BHowto%2BZIP%2BFiles%2BInside%2BRTF/32696/#comments)

* [previous](/diary/32692)
* [next](/diary/32700)

### Comments

Curious to know if this was coincidence or not that the URL in your example is the same domain IOC in this blog.

https://www.akamai.com/blog/security-research/inside-the-fix-cve-2026-21513-mshtml-exploit-analysis

#### 3000060128

#### Mar 2nd 2026 15 hours ago

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