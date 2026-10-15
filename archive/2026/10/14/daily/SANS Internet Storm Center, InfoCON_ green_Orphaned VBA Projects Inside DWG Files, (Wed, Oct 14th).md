---
title: Orphaned VBA Projects Inside DWG Files, (Wed, Oct 14th)
url: https://isc.sans.edu/diary/rss/33420
source: SANS Internet Storm Center, InfoCON: green
date: 2026-10-14
fetch_date: 2026-10-15T06:45:21.274076
---

# Orphaned VBA Projects Inside DWG Files, (Wed, Oct 14th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/33414)
* [next](/diary/33422)

Click HERE to learn more about classes Didier is teaching for SANS

# [Orphaned VBA Projects Inside DWG Files](/forums/diary/Orphaned%2BVBA%2BProjects%2BInside%2BDWG%2BFiles/33420/)

**Published**: 2026-10-14. **Last Updated**: 2026-10-14 06:49:46 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Orphaned%2BVBA%2BProjects%2BInside%2BDWG%2BFiles/33420/#comments)

Years ago I wrote [diary](https://isc.sans.edu/diary/Malicious%2BDWG%2BFiles/25612) [entries](https://isc.sans.edu/diary/Extracting%2BVBA%2BMacros%2BFrom%2BDWG%2BFiles/25634) about VBA code stored inside AutoCAD drawing files (.dwg).

In a nutshell: the VBA code is stored inside an OLE file, that is embedded inside the DWG file. You can do a brute-force search for the embedded OLE file, or you can follow a pointer inside the header of the DWG file.

I wrote a small Python script ([autocad.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/autocad.py)) for this second case. It looks at a 32-bit pointer at position 0x24 inside the DWG file. This points to a 16-byte long header, followed by the embedded file. This 16-byte long header contains the length of the embedded file. You use the script together with my tool [cut-bytes.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/cut-bytes.py), like this:

> cut-bytes.py -S autocad.py -P AutoCAD : 461ed52aeb75384133a8238b2eb481ae5d505d4961effa622673d65a889c8218.vir.zip | oledump.py

![](https://isc.sans.edu/diaryimages/images/2026-10-13_17-49-50.png)

This command carves the DWG file (inside the ZIP file) and extracts the embedded OLE file, and pipes it into [oledump.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/oledump.py) for analysis.

When the pointer is zero, there is no embedded OLE file, and cut-bytes.py returns nothing.

Recently, I discovered 2 DWG files that are an exception: their pointer to the embedded OLE file is zero, but if you do a brute-force search, you will find an embedded OLE file with a VBA project.

For example [this DWG file](https://www.virustotal.com/gui/file/09d4607941e458f6dbb6be17825641d863c0b37c185027984e137d8a67e919d8).

Its pointer to the embedded VBA project is zero:

![](https://isc.sans.edu/diaryimages/images/2026-10-13_17-57-23.png)

But it contains an embedded OLE file:

![](https://isc.sans.edu/diaryimages/images/2026-10-13_17-58-05.png)

And right in front of the embedded OLE file, there is the 16-byte long header that contains the lenght of the embedded file.

Using the AutoCAD script to extract the file gives nothing:

![](https://isc.sans.edu/diaryimages/images/2026-10-13_18-02-46.png)

But oledump.py can find the embedded OLE file and analyze it:

![](https://isc.sans.edu/diaryimages/images/2026-10-13_18-04-26.png)

So while using oledump.py to analyze DWG files you find a VBA project embedded inside a DWG file, then also verify if it is not orphaned: verify that the pointer at 0x24 is not zero (or use the autocad.py script).

Because when a DWG file contains an orphaned VBA project, the VBA code can not have executed when someone opened the DWG file with AutoCAD. AutoCAD "does not see" orphaned VBA projects.

Notice that a default installation of AutoCAD does not support VBA. VBA for AutoCAD is a [separate install](https://www.autodesk.com/support/technical/article/caas/tsarticles/ts/3kxk0RyvfWTfSfAIrcmsLQ.html).

I don't know how orphaning happens, but I did find an [AutoLISP command to remove a VBA project from a DWG file](https://forums.autodesk.com/t5/autocad-forum/need-to-remove-old-vba-from-2020-dwg/td-p/11235044):

> (dictremove (namedobjdict) "ACAD\_VBA")

Maybe this dictremove command clears the pointer, but does not remove the embedded OLE file.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Orphaned%2BVBA%2BProjects%2BInside%2BDWG%2BFiles/33420/#comments)

Click HERE to learn more about classes Didier is teaching for SANS

* [previous](/diary/33414)
* [next](/diary/33422)

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