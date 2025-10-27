---
title: Finger.exe LOLBin, (Sun, Dec 4th)
url: https://isc.sans.edu/diary/rss/29298
source: SANS Internet Storm Center, InfoCON: green
date: 2022-12-05
fetch_date: 2025-10-04T00:31:53.092726
---

# Finger.exe LOLBin, (Sun, Dec 4th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29296)
* [next](/diary/29300)

# [Finger.exe LOLBin](/forums/diary/Fingerexe%2BLOLBin/29298/)

**Published**: 2022-12-04. **Last Updated**: 2022-12-04 11:15:23 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[1 comment(s)](/diary/Fingerexe%2BLOLBin/29298/#comments)

Guy's diary entry "[Linux LOLBins Applications Available in Windows](https://isc.sans.edu/diary/Linux%20LOLBins%20Applications%20Available%20in%20Windows/29296)" reminded me of another Linux tool that is available on Windows: the ancient [finger](https://en.wikipedia.org/wiki/Finger_%28protocol%29) command.

Here is an example with weather info for the North Pole:

![](https://isc.sans.edu/diaryimages/images/20221204-115704.png)

Communication takes place over TCP. Destination port is 79.

The finger.exe command sends the string before the @ sign to the host specified after the @ sign.

![](https://isc.sans.edu/diaryimages/images/20221204-120020.png)

![](https://isc.sans.edu/diaryimages/images/20221204-120055.png)

![](https://isc.sans.edu/diaryimages/images/20221204-120134.png)

finger.exe is not proxy aware, and port 79 is hardcoded inside the finger.exe executable. Not as a number, but as a [protocol name (finger) that is defined](https://blog.didierstevens.com/2020/12/07/quickpost-finger-exe/) in the services list (%SystemRoot%\system32\drivers\etc\services);

Didier Stevens
Senior handler
Microsoft MVP
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords: [lolbin](/tag.html?tag=lolbin) [finger](/tag.html?tag=finger)

[1 comment(s)](/diary/Fingerexe%2BLOLBin/29298/#comments)

* [previous](/diary/29296)
* [next](/diary/29300)

### Comments

Didier:-

You were off by about 5839 km (3628 miles). Try "finger 'north\_pole'@graph.no" instead. :-)

And, for the USA at least, "finger [your\_postal\_code]@graph.no" also seems to work. Kudos to the personnel behind this app.

#### Dshield Reporter 309

#### Jan 4th 2023 2 years ago

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