---
title: oledump &#x26; MSI Files, (Sun, Feb 26th)
url: https://isc.sans.edu/diary/rss/29584
source: SANS Internet Storm Center, InfoCON: green
date: 2023-02-27
fetch_date: 2025-10-04T08:11:33.031410
---

# oledump &#x26; MSI Files, (Sun, Feb 26th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29582)
* [next](/diary/29588)

# [oledump & MSI Files](/forums/diary/oledump%2BMSI%2BFiles/29584/)

**Published**: 2023-02-26. **Last Updated**: 2023-02-26 18:29:54 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/oledump%2BMSI%2BFiles/29584/#comments)

We regularly write about MSI files, as it is one of the many fileformats used by attackers. For example, here is a diary entry from Xavier in 2018: "[Malware Delivered via Windows Installer Files](https://isc.sans.edu/diary/Malware%2BDelivered%2Bvia%2BWindows%2BInstaller%2BFiles/23349)".

MSI files are ole files, that can be analyzed with my [oledump](https://blog.didierstevens.com/programs/oledump-py/) tool. Unfortunately, the stream names are encoded, that why back then, I wrote a little plugin to decode the stream names: [plugin\_msi.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/plugin_msi.py). This plugin is often enough for me, when I have to analyze macilious MSI files, as it will help to quickly find embedded payloads.

But recently, I had to dig deeper in MSI files, to look at the actions encoded in tables.

This weekend, I went down the rabbit hole and reversed the binary structures in MSI files to store numbers, strings and tables (apparently, Microsoft did not release a document for the binary structures found inside MSI files). This results in a new oledump plugin: [plugin\_msi\_info.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/plugin_msi_info.py).

This plugin will evolve, so the format of its output will probably change. For the moment, it dumps out all the tables, and provides and overview of streams that don't contain tables or table-supporting data. It does not use the Windows API, so you can run it on any operating system that supports Python.

![](https://isc.sans.edu/diaryimages/images/20230226-190443.png)

Let's use it on an msi file created with exetomsi, the tool Xavier talked about in his [2018 diary entry](https://isc.sans.edu/diary/Malware%2BDelivered%2Bvia%2BWindows%2BInstaller%2BFiles/23349).

![](https://isc.sans.edu/diaryimages/images/20230226-190902.png)

First the plugin list all the tables. Table property is a table that Xavier looked at in his diary entry, to show you the exetomsi meta data. He did this with a custom VBS script, and with WIX.

My plugin dumps out all the tables, also the Property table (this table is in stream !Property):

![](https://isc.sans.edu/diaryimages/images/20230226-190931.png)

When you take a look at the custom actions table, you will see a custom action to run an executable:

![](https://isc.sans.edu/diaryimages/images/20230226-191011.png)

This PE file is stored inside a stream:

![](https://isc.sans.edu/diaryimages/images/20230226-191043.png)

It's in stream 2, so if you need to extract it, you can just use oledump without plugin:

![](https://isc.sans.edu/diaryimages/images/20230226-192244.png)

Didier Stevens
Senior handler
Microsoft MVP
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords: [msi](/tag.html?tag=msi) [oledump](/tag.html?tag=oledump)

[0 comment(s)](/diary/oledump%2BMSI%2BFiles/29584/#comments)

* [previous](/diary/29582)
* [next](/diary/29588)

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