---
title: Partial ZIP File Downloads, (Mon, Jan 20th)
url: https://isc.sans.edu/diary/rss/31608
source: SANS Internet Storm Center, InfoCON: green
date: 2025-01-21
fetch_date: 2025-10-06T20:12:51.160521
---

# Partial ZIP File Downloads, (Mon, Jan 20th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31602)
* [next](/diary/31612)

# [Partial ZIP File Downloads](/forums/diary/Partial%2BZIP%2BFile%2BDownloads/31608/)

**Published**: 2025-01-20. **Last Updated**: 2025-01-20 07:27:48 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Partial%2BZIP%2BFile%2BDownloads/31608/#comments)

Say you want a file that is inside a huge online ZIP file (several gigabytes large). Downloading the complete ZIP file would take too long.

If the HTTP server supports the range header, you can do the following:

We will work with my DidierStevensSuite.zip file as an example (it's 13MB in size, not several GBs, but the principle remains te same).

First, with a HEAD HTTP request, we figure out the ZIP file size:

![](https://isc.sans.edu/diaryimages/images/20250120-075900.png)

The size of the ZIP file is 13189336 bytes.

The end of a ZIP file contains a series of DIR records that compose the directory of files (and directories) contained inside the ZIP file. This directory is usually small, compared to the file size, so we will do a partial download starting at position 13000000.

This can be done with the curl range option: this will add a header that specifies the range we want to download:

![](https://isc.sans.edu/diaryimages/images/20250120-080252.png)

Next we use my [zipdump.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/zipdump.py) tool to parse the ZIP records (-f l) inside the partial ZIP download like this:

![](https://isc.sans.edu/diaryimages/images/20250120-080610.png)

Let's say that the file we want to obtain, is xor-kpa.py. It's ZIP DIR record starts at posistion 0x0002e05d.

We can analyze that record like this:

![](https://isc.sans.edu/diaryimages/images/20250120-081054(1).png)

Field headeroffset tells us were the corresponding ZIP FILE record is insize the ZIP file: at position 11892478. That ZIP FILE record contains the compressed data of the file (xor-kpa.py) we want. So that's the begin value of our range option: -r 11892478-

To determine the end value of our range option, we look at the next record in line (that's for file XORSearch.exe):

![](https://isc.sans.edu/diaryimages/images/20250120-081136.png)

That ZIP FILE record starts at position 11899893. So 11899893 minus 1 is the end value of our range option: -r 11892478-11899892.

Here is the curl command to download the entiry ZIP FILE record for file xor-kpa.py:

![](https://isc.sans.edu/diaryimages/images/20250120-082121.png)

And we analyze that partial download with zipdump.py like this:

![](https://isc.sans.edu/diaryimages/images/20250120-082213.png)

The zipdump.py command to decompress (-s decompress) the ZIP data for file xor-kpa.py and write it to disk (-d), is the following:

![](https://isc.sans.edu/diaryimages/images/20250120-082418.png)

And that gives us the desired file:

![](https://isc.sans.edu/diaryimages/images/20250120-082442.png)

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Partial%2BZIP%2BFile%2BDownloads/31608/#comments)

* [previous](/diary/31602)
* [next](/diary/31612)

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