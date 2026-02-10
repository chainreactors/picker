---
title: Quick Howto: Extract URLs from RTF files, (Mon, Feb 9th)
url: https://isc.sans.edu/diary/rss/32692
source: SANS Internet Storm Center, InfoCON: green
date: 2026-02-09
fetch_date: 2026-02-10T04:27:18.971744
---

# Quick Howto: Extract URLs from RTF files, (Mon, Feb 9th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Didier Stevens](/handler_list.html#didier-stevens "Didier Stevens")

Threat Level: [green](/infocon.html)

* [previous](/diary/32690)

# [Quick Howto: Extract URLs from RTF files](/forums/diary/Quick%2BHowto%2BExtract%2BURLs%2Bfrom%2BRTF%2Bfiles/32692/)

**Published**: 2026-02-09. **Last Updated**: 2026-02-09 11:38:16 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Quick%2BHowto%2BExtract%2BURLs%2Bfrom%2BRTF%2Bfiles/32692/#comments)

Malicious RTF (Rich Text Format) documents are back in the news with the [exploitation of CVE-2026-21509 by APT28](https://www.helpnetsecurity.com/2026/02/03/russian-hackers-are-exploiting-recently-patched-microsoft-office-vulnerability-cve-2026-21509/).

The malicious RTF documents [BULLETEN\_H.doc](https://www.virustotal.com/gui/file/c91183175ce77360006f964841eb4048cf37cb82103f2573e262927be4c7607f) and [Consultation\_Topics\_Ukraine(Final).doc](https://www.virustotal.com/gui/file/b2ba51b4491da8604ff9410d6e004971e3cd9a321390d0258e294ac42010b546) mentioned in the news are RTF files (despite their .doc extension, a common trick used by threat actors).

Here is a quick tip to extract URLs from RTF files. Use the following command:

```

rtfdump.py -j -C SAMPLE.vir | strings.py --jsoninput | re-search.py -n url -u -F officeurls
```

Like this:

![](https://isc.sans.edu/diaryimages/images/20260209-120912.png)

BTW, if you are curious, this is how that document looks like when opened:

![](https://isc.sans.edu/diaryimages/images/20260208-212413.png)

Let me break down the command:

* [rtfdump.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/rtfdump.py) -j -C SAMPLE.vir: this parses RTF file SAMPLE.vir and produces JSON output with the content of all the items found in the RTF document. Option -C make that all combinations are included in the JSON data: the item itself, the hex-decoded item (-H) and the hex-decoded and shifted item (-H -S). So per item found inside the RTF file, 3 entries are produced in the JSON data.
* [strings.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/strings.py) --jsoninput: this takes the JSON data produced by rtfdump.py and extract all strings
* [re-search.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/re-search.py) -n url -u -F officeurls: this extracts all URLs (-n url) found in the strings produced by strings.py, performs a deduplication (-u) and filters out all URLs linked to Office document definitions (-F officeurls)

So I have found one domain (wellnesscaremed) and one private IP address (192.168...). What I then like to do, is search for these keywords in the string list, like this:

![](https://isc.sans.edu/diaryimages/images/20260209-122140.png)

If found extra IOCs: a UNC and a "malformed" URL. The URL has it's hostname followed by @ssl. This is not according to standards. @ can be used to introduce credentials, but then it has to come in front of the hostname, not behind it. So that's not the case here. More on this later.

Here are the results for the other document:

![](https://isc.sans.edu/diaryimages/images/20260209-122843.png)

![](https://isc.sans.edu/diaryimages/images/20260208-212510.png)

Notice that this time, we have @80.

I believe that this @ notation is used by Microsoft to provide the portnumber when WebDAV requests are made (via UNC). If you know more about this, please post a comment.

In an upcoming diary, I will show how to extract URLs from ZIP files embedded in the objects in these RTF files.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Quick%2BHowto%2BExtract%2BURLs%2Bfrom%2BRTF%2Bfiles/32692/#comments)

* [previous](/diary/32690)

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