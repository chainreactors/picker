---
title: Tool update: sigs.py - added check mode, (Fri, Feb 21st)
url: https://isc.sans.edu/diary/rss/31706
source: SANS Internet Storm Center, InfoCON: green
date: 2025-02-22
fetch_date: 2025-10-06T20:40:05.575036
---

# Tool update: sigs.py - added check mode, (Fri, Feb 21st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31704)
* [next](/diary/31710)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Malware Analysis Tools and Techniques](https://www.sans.org/event/tokyo-autumn-2025/course/reverse-engineering-malware-malware-analysis-tools-techniques) | Online | Japan Standard Time | Oct 20th - Oct 25th 2025 |

# [Tool update: sigs.py - added check mode](/forums/diary/Tool%2Bupdate%2Bsigspy%2Badded%2Bcheck%2Bmode/31706/)

**Published**: 2025-02-21. **Last Updated**: 2025-02-21 00:00:36 UTC
**by** [Jim Clausing](/handler_list.html#jim-clausing) (Version: 1)

[0 comment(s)](/diary/Tool%2Bupdate%2Bsigspy%2Badded%2Bcheck%2Bmode/31706/#comments)

Over the years, I've written a number of scripts to make my life easier. One of those tools was sigs.py (which was a rewrite of an old perl script sigs.pl) to hash files. I wanted something portable that could potentially be a drop-in replacement for things like md5sum, sha1sum, etc. (and can do hashes like sha512, sha3-224, and sha3-384). I've even had cases where my python script ran faster than those Linux tools. Anyway, in some recent cases I've been working on, I've been getting manifests with hashes and to validate that I got good copies, I wanted to verify the hashes. Sometimes I was getting md5s, sometimes, sha1s, sometimes sha256s. On Linux, md5sum, sha1sum, sha256sum, etc. have the -c switch to do the checking, but my script did not have that, so I took an hour over a weekend recently and I added that capability. The script determines which hash to use based on the length of the hash it finds in the text file, so it can check any of the hashes it can calculate.

![](https://isc.sans.edu/diaryimages/images/2025-02-20%2013_48_22-leibnitz-nat%20-%20SecureCRT.png)

![](https://isc.sans.edu/diaryimages/images/2025-02-20%2013_49_39-leibnitz-nat%20-%20SecureCRT.png)

And even, SHA3-384

![](https://isc.sans.edu/diaryimages/images/2025-02-20%2013_51_09-leibnitz-nat%20-%20SecureCRT.png)

Hopefully others find this as useful as I do. The script can be found in my [scripts repo](https://github.com/clausing/scripts)[1] or [here](https://raw.githubusercontent.com/clausing/scripts/refs/heads/master/sigs.py)[2] directly.

References:

1. <http://github.com/clausing/scripts>

2. <http://raw.githubusercontent.com/clausing/scripts/refs/heads/master/sigs.py>

---------------
Jim Clausing, GIAC GSE #26
jclausing --at-- isc [dot] sans (dot) edu

Keywords:

[0 comment(s)](/diary/Tool%2Bupdate%2Bsigspy%2Badded%2Bcheck%2Bmode/31706/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Malware Analysis Tools and Techniques](https://www.sans.org/event/tokyo-autumn-2025/course/reverse-engineering-malware-malware-analysis-tools-techniques) | Online | Japan Standard Time | Oct 20th - Oct 25th 2025 |

* [previous](/diary/31704)
* [next](/diary/31710)

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