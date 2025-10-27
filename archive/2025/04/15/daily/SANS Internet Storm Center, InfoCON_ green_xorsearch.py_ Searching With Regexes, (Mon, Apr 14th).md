---
title: xorsearch.py: Searching With Regexes, (Mon, Apr 14th)
url: https://isc.sans.edu/diary/rss/31854
source: SANS Internet Storm Center, InfoCON: green
date: 2025-04-15
fetch_date: 2025-10-06T22:09:03.699710
---

# xorsearch.py: Searching With Regexes, (Mon, Apr 14th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31850)
* [next](/diary/31856)

# [xorsearch.py: Searching With Regexes](/forums/diary/xorsearchpy%2BSearching%2BWith%2BRegexes/31854/)

**Published**: 2025-04-14. **Last Updated**: 2025-04-14 09:26:38 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/xorsearchpy%2BSearching%2BWith%2BRegexes/31854/#comments)

As promised in diary entry "[XORsearch: Searching With Regexes](https://isc.sans.edu/diary/XORsearch%2BSearching%2BWith%2BRegexes/31834)", I will outline another method to search with xorsearch and regexes.

In stead of [XORsearch.exe](https://blog.didierstevens.com/programs/xorsearch/), the original tool that is written in C and compiled, we will use [xorsearch.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/xorsearch.py), a new tool written in Python.

Unlike XORsearch.exe, xorsearch.py supports YARA rules, and thus regex searches.

Let's say we want to use this trivial regular expression to match IPv4 addresses (it's matching 4 numbers separated by dots): \d+\.\d+\.\d+\.\d+

We can create a YARA rule for this regex:

![](https://isc.sans.edu/diaryimages/images/20250414-105544.png)

And then we can use this rule on a test file (test-xor-1.bin):

![](https://isc.sans.edu/diaryimages/images/20250414-105832.png)

This tells us that YARA rule ipv4 (namespace ipv4.yara) triggered on file test-xor-1.bin when it is XOR encoded with key 0x19.

To see the YARA rule strings that were matched, use option --yarastrings:

![](https://isc.sans.edu/diaryimages/images/20250414-110204.png)

To see the encoded file, use one of the many dump options, like -a for a HEX/ASCII dump:

![](https://isc.sans.edu/diaryimages/images/20250414-110224.png)

Or a binary dump with option -d:

![](https://isc.sans.edu/diaryimages/images/20250414-111909.png)

If you find it cumbersome to create a YARA rule just for a simple regex (I find it cumbersome :-) ), you can pass the regex via the command line prefixed with #r#, and xorsearch.py will generate the YARA rule for you:

![](https://isc.sans.edu/diaryimages/images/20250414-112151.png)

I will give more examples of this in an upcoming diary entry.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/xorsearchpy%2BSearching%2BWith%2BRegexes/31854/#comments)

* [previous](/diary/31850)
* [next](/diary/31856)

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