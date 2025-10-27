---
title: Extracting Multiple Streams From OLE Files, (Wed, Mar 29th)
url: https://isc.sans.edu/diary/rss/29688
source: SANS Internet Storm Center, InfoCON: green
date: 2023-03-30
fetch_date: 2025-10-04T11:09:27.826439
---

# Extracting Multiple Streams From OLE Files, (Wed, Mar 29th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29682)
* [next](/diary/29692)

# [Extracting Multiple Streams From OLE Files](/forums/diary/Extracting%2BMultiple%2BStreams%2BFrom%2BOLE%2BFiles/29688/)

**Published**: 2023-03-29. **Last Updated**: 2023-03-29 19:35:43 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Extracting%2BMultiple%2BStreams%2BFrom%2BOLE%2BFiles/29688/#comments)

Reader Martin asks us for some help extracting embedded content from a submitted [malicious document](https://www.virustotal.com/gui/file/a09c97fd6265caa04ac80f307f2c9d2caa5a12c30ea2a712e2e9f456e1f04c7d).

These are the streams inside the document, listed with [oledump.py](https://blog.didierstevens.com/programs/oledump-py/):

![](https://isc.sans.edu/diaryimages/images/20230329-205636.png)

The streams to extract are those where the stream name includes Package, CONTENTS, ... .

This can be done with oledump as follows: oledump.py -s 6 -d sample.vir > extracted.vir

-s 6 selects stream 6, and -d produces a binary dump which is written to a file via file redirection (>).

This has to be repeated for every stream that could be interesting.

But I also have another method, that involves less repeated commands.

First, we let oledump.py analyze the file, and produce JSON output. This JSON output contains all the streams (id, name and content) and can be consumed by other tools I make, like [file-magic.py](https://blog.didierstevens.com/2023/02/13/update-file-magic-py-version-0-0-6/), a tool to identify files based on their content.

Like this:

![](https://isc.sans.edu/diaryimages/images/20230329-210251.png)

file-magic.py identified the content of each stream: data, Word, PDF, ...

We can now let file-magic.py produce JSON output, that can then be filtered by another tool: [myjson-filter.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/myjson-filter.py):

![](https://isc.sans.edu/diaryimages/images/20230329-210653.png)

By default, myjson-filter.py produces JSON output (filtered), but with option -l (--list), we obtain a list of the items and can easily observe what the effect of our filtering is (for the moment, we have not yet filtered).

With option -t, we will filter by type (determined by file-magic.py). Option -t takes a regular expression that will be used to select types. Let's go with regular expression data:

![](https://isc.sans.edu/diaryimages/images/20230329-210946.png)

At first, what is identified as just data, doesn't interest us. So we will reverse the selection (v), to select everything that isn't data, like this:

![](https://isc.sans.edu/diaryimages/images/20230329-211146.png)

I justed added a new option to my myjson-filter.py tool, to easily write all selected items to disk as individual files: option -W (--write).

Option -W requires a value: vir, hash, hashvir or idvir. Value vir instructs my tool to create files with a filename that is the (cleaned) item name and with extension .vir. Like this:

![](https://isc.sans.edu/diaryimages/images/20230329-211813.png)

So now we have written all streams to disk, that were identified as something else than just plain data.

If you don't find what you are looking for in these files, just use -t data to write all data files to disk, and see if you can find what you are looking for in these files.

For another example of my tools that support JSON, take a look at my blog post "[Combining zipdump, file-magic And myjson-filter](https://blog.didierstevens.com/2022/12/31/combining-zipdump-file-magic-and-myjson-filter/)".

Didier Stevens
Senior handler
Microsoft MVP
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords: [json](/tag.html?tag=json) [oledump](/tag.html?tag=oledump)

[0 comment(s)](/diary/Extracting%2BMultiple%2BStreams%2BFrom%2BOLE%2BFiles/29688/#comments)

* [previous](/diary/29682)
* [next](/diary/29692)

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