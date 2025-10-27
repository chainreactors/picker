---
title: Obfuscated Hexadecimal Payload, (Sat, Mar 16th)
url: https://isc.sans.edu/diary/rss/30750
source: SANS Internet Storm Center, InfoCON: green
date: 2024-03-18
fetch_date: 2025-10-04T12:08:32.536106
---

# Obfuscated Hexadecimal Payload, (Sat, Mar 16th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/30746)
* [next](/diary/30752)

# [Obfuscated Hexadecimal Payload](/forums/diary/Obfuscated%2BHexadecimal%2BPayload/30750/)

**Published**: 2024-03-16. **Last Updated**: 2024-03-17 00:36:54 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Obfuscated%2BHexadecimal%2BPayload/30750/#comments)

This [PE file](https://www.virustotal.com/gui/file/e778ba2e16b6117b847ed753904e11954bec87178df0898be59c77b1eaf383f8) contains an obfuscated hexadecimal-encoded payload. When I analyze it with base64dump.py searching for all supported encodings, a very long payload is detected:

![](https://isc.sans.edu/diaryimages/images/20240317-005057.png)

It's 2834443 characters long, and matches base85 encoding (b85), but this is likely a false positive, as base85 uses 85 unique characters (as its name suggests), but in this particular encoded content, only 23 unique characters are used (out of 85).

Analyzing the PE file with my strings.py tool (calculating statistics with option -a) reveals it does indeed contain one very long string:

![](https://isc.sans.edu/diaryimages/images/20240317-010549.png)

Verbose mode (-V) gives statistics for the 10 longests strings. We see that 2 characters (# and %) appear very often in this string, more than 75% of this long string is made up of these 2 characters:

![](https://isc.sans.edu/diaryimages/images/20240317-010901.png)

These 2 characters are likely inserted for obfuscation. Let's use base64dump.py and let it ignore these 2 characters (-i #%"):

![](https://isc.sans.edu/diaryimages/images/20240317-013426.png)

Now we have a hex encoded payload that decodes to a PE file (MZ), and most likely a Cobalt Strike beacon (MZARUH).

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Obfuscated%2BHexadecimal%2BPayload/30750/#comments)

* [previous](/diary/30746)
* [next](/diary/30752)

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