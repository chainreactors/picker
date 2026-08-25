---
title: DOUBLECUP's PNG Payload, (Mon, Aug 24th)
url: https://isc.sans.edu/diary/rss/33274
source: SANS Internet Storm Center, InfoCON: green
date: 2026-08-24
fetch_date: 2026-08-25T03:00:29.826221
---

# DOUBLECUP's PNG Payload, (Mon, Aug 24th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Didier Stevens](/handler_list.html#didier-stevens "Didier Stevens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33272)

Click HERE to learn more about classes Didier is teaching for SANS

# [DOUBLECUP's PNG Payload](/forums/diary/DOUBLECUPs%2BPNG%2BPayload/33274/)

**Published**: 2026-08-24. **Last Updated**: 2026-08-24 07:23:16 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/DOUBLECUPs%2BPNG%2BPayload/33274/#comments)

New malware that uses steganography always gets my attention, but I was disappointed when I looked at the latest [DOUBLECUP write-up](https://socradar.io/blog/doublecup-clickfix-loader-devicemanager-rats/). It doesn't use real steganography:

![](https://isc.sans.edu/diaryimages/images/2026-08-23_10-01-09.png)

You can see the PowerShell payload as cleartext: it has not been encoded into the pixels of the image.

It's even not embedded in the image (like inside the metadata), it's just appended after the PNG file:

![](https://isc.sans.edu/diaryimages/images/2026-08-23_10-01-43.png)

Yet there is a clever little trick:

![](https://isc.sans.edu/diaryimages/images/2026-08-23_10-02-58.png)

The PowerShell script starts with 0x0D 0x0A, Carriage-Return + Newline: that terminates a line of text in Windows.

That makes that you don't need a custom payload extractor, you can just use the FINDSTR command (Windows' grep) with a unique identifier to extract the script:

![](https://isc.sans.edu/diaryimages/images/2026-08-23_10-03-40.png)

And then pipe it into the PowerShell interpreter.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/DOUBLECUPs%2BPNG%2BPayload/33274/#comments)

Click HERE to learn more about classes Didier is teaching for SANS

* [previous](/diary/33272)

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