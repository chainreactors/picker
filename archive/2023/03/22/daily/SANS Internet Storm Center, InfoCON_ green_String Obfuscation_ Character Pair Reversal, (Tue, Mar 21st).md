---
title: String Obfuscation: Character Pair Reversal, (Tue, Mar 21st)
url: https://isc.sans.edu/diary/rss/29654
source: SANS Internet Storm Center, InfoCON: green
date: 2023-03-22
fetch_date: 2025-10-04T10:18:37.337363
---

# String Obfuscation: Character Pair Reversal, (Tue, Mar 21st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29650)
* [next](/diary/29656)

# [String Obfuscation: Character Pair Reversal](/forums/diary/String%2BObfuscation%2BCharacter%2BPair%2BReversal/29654/)

**Published**: 2023-03-21. **Last Updated**: 2023-03-21 16:48:19 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/String%2BObfuscation%2BCharacter%2BPair%2BReversal/29654/#comments)

I found a [malicious .LNK file on MalwareBazaar](https://bazaar.abuse.ch/sample/8d278172242da77f4bf8bac9ec90152300bde595f8e29de216369ea9dd07abde/) that contains an obfuscated URL. The obfuscation is a classic one, with a twist: string reversal, not per character, but per character pair.

Let's take a look.

The file is indeed a .LNK file:

![](https://isc.sans.edu/diaryimages/images/20230321-171750.png)

And it seems to contain powershell code.

In stead of using a .LNK parser, I'm just going to extract the strings of this .lnk file:

![](https://isc.sans.edu/diaryimages/images/20230321-171938.png)

The powershell script contains a string, that looks like a mangled URL. It looks like a reversed string, but is a bit different.

A hint on how to decode this, can be found 2 lines above the mangled URL: .Substring(..., 2)

The decoding algorithm works with 2 characters.

So this is a reversed string, but in stead of reversing character per character, reversing is done per character pair.

Let's isolated the mangled string and decode it:

![](https://isc.sans.edu/diaryimages/images/20230321-172411.png)

With Python's textwrap.wrap function, we can split up the string in substrings of 2 characters, like this:

![](https://isc.sans.edu/diaryimages/images/20230321-172546.png)

Then we reverse this list of substrings ([::-1]):

![](https://isc.sans.edu/diaryimages/images/20230321-172628.png)

And we join the substrings together:

![](https://isc.sans.edu/diaryimages/images/20230321-172949.png)

Giving us the deobfuscated URL: hxxp://179.43.175[.]187/ksjy/Godisgood.hta

At time of writing, the payload was [6c1be182c5ae4b5cc44d1aedd202327c71253000d29d28e87686ad71bff41804](https://www.virustotal.com/gui/file/6c1be182c5ae4b5cc44d1aedd202327c71253000d29d28e87686ad71bff41804).

This payload will ultimately download zgRAT malware: [f87246f639ed528fe01ee1fea953470a2997ea586779bf085cb051164586cd76](https://bazaar.abuse.ch/sample/f87246f639ed528fe01ee1fea953470a2997ea586779bf085cb051164586cd76/) and [592f1c8ff241da2e693160175c6fc4aa460388aabe1553b4b0f029977ce4ad27](https://bazaar.abuse.ch/sample/592f1c8ff241da2e693160175c6fc4aa460388aabe1553b4b0f029977ce4ad27/).

Tools used in this analysis: zipdump.py, strings.py, re-search.py, python-per-line.py. All can be found on [GitHub](https://github.com/DidierStevens/DidierStevensSuite).

Didier Stevens
Senior handler
Microsoft MVP
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords: [powershell](/tag.html?tag=powershell) [lnk](/tag.html?tag=lnk) [obfuscation](/tag.html?tag=obfuscation)

[0 comment(s)](/diary/String%2BObfuscation%2BCharacter%2BPair%2BReversal/29654/#comments)

* [previous](/diary/29650)
* [next](/diary/29656)

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