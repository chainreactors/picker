---
title: Detecting (Malicious) OneNote Files, (Wed, Feb 1st)
url: https://isc.sans.edu/diary/rss/29494
source: SANS Internet Storm Center, InfoCON: green
date: 2023-02-02
fetch_date: 2025-10-04T05:31:02.641879
---

# Detecting (Malicious) OneNote Files, (Wed, Feb 1st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29490)
* [next](/diary/29500)

# [Detecting (Malicious) OneNote Files](/forums/diary/Detecting%2BMalicious%2BOneNote%2BFiles/29494/)

**Published**: 2023-02-01. **Last Updated**: 2023-02-01 08:57:26 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Detecting%2BMalicious%2BOneNote%2BFiles/29494/#comments)

We are starting to see malicious OneNote documents (cfr. Xavier's diary entry "[A First Malicious OneNote Document](https://isc.sans.edu/diary/A%20First%20Malicious%20OneNote%20Document/29470)").

OneNote files have their own binary fileformat: [[MS-ONESTORE]](https://learn.microsoft.com/en-us/openspecs/office_file_formats/ms-onestore/ae670cd2-4b38-4b24-82d1-87cfb2cc3725).

A OneNote file starts with GUID {7B5C52E4-D88C-4DA7-AEB1-5378D02996D3}.

Files contained in a OneNote file start with a header ([FileDataStoreObject](https://learn.microsoft.com/en-us/openspecs/office_file_formats/ms-onestore/8806fd18-6735-4874-b111-227b83eaac26)) followed by the embedded file itself. This header also starts with a GUID: {BDE316E7-2665-4511-A4C4-8D4D0B7A9EAC}.

Hence, to detect OneNote files with embedded files, look for files that start with byte sequence E4 52 5C 7B 8C D8 A7 4D AE B1 53 78 D0 29 96 D3 (that's GUID {7B5C52E4-D88C-4DA7-AEB1-5378D02996D3}) and contain one ore more instances of byte sequence E7 16 E3 BD 65 26 11 45 A4 C4 8D 4D 0B 7A 9E AC (that's GUID {BDE316E7-2665-4511-A4C4-8D4D0B7A9EAC}).

This allows you to detect OneNote files with embedded files. Which are not necessarily malicious ... Because an embedded file can just be a picture, for example.

I have a bit more detail on the analysis of this format, in my blog post "[Analyzing Malicious OneNote Documents](https://blog.didierstevens.com/2023/01/22/analyzing-malicious-onenote-documents/)".

Florian Roth developed [YARA rules that look for these GUIDs](https://github.com/Neo23x0/signature-base/blob/master/yara/gen_onenote_phish.yar), together with some typical malicious payloads: PE files, BAT files, VBS files, LNK files.

The trick is to look at the beginning of the embedded file, which can be found 36 bytes after the start of structure FileDataStoreObject (hence 36 bytes after each {BDE316E7-2665-4511-A4C4-8D4D0B7A9EAC} guid).

If an embedded file starts with MZ, it's most likely an embedded Windows executable (but it could also be a text file that starts with MZ). If it starts with 4C 00 00 00, it's most likely an LNK file.

BAT and VBS files are harder to recognize, as they have no magic header: they can start with any byte sequence. Florian's rule uses a little heuristic: it identifies files that start with "@ECH" as BAT files (@ECHO OFF) and files that start with "on e" as VBS files (on error resume). Of course, this will not detect all malicious OneNote files, but we can never have perfect detection ...

Here is one of Florian's rules that detects a OneNote file with an embedded PE file ($x1):

![](https://isc.sans.edu/diaryimages/images/20230131-193842.png)

Mostly as an exercise for myself, I created Suricata rules for onenote files. You can find them [here](https://github.com/DidierStevens/Beta/blob/master/onenote.rules), in my [beta GitHub repository](https://github.com/DidierStevens/Beta).

Caveat: these rules have not been tested in production, and the first rules detect any onenote file, with or without benign/malicious payload.

I'll provide more details on these Suricata rules in an upcoming blog post.

Didier Stevens
Senior handler
Microsoft MVP
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords: [maldoc](/tag.html?tag=maldoc) [onenote](/tag.html?tag=onenote) [yara](/tag.html?tag=yara) [suricata](/tag.html?tag=suricata)

[0 comment(s)](/diary/Detecting%2BMalicious%2BOneNote%2BFiles/29494/#comments)

* [previous](/diary/29490)
* [next](/diary/29500)

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