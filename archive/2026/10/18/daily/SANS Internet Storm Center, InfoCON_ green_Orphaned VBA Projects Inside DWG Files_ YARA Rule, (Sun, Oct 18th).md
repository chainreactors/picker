---
title: Orphaned VBA Projects Inside DWG Files: YARA Rule, (Sun, Oct 18th)
url: https://isc.sans.edu/diary/rss/33434
source: SANS Internet Storm Center, InfoCON: green
date: 2026-10-18
fetch_date: 2026-10-19T07:07:44.665812
---

# Orphaned VBA Projects Inside DWG Files: YARA Rule, (Sun, Oct 18th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Didier Stevens](/handler_list.html#didier-stevens "Didier Stevens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33430)

Click HERE to learn more about classes Didier is teaching for SANS

# [Orphaned VBA Projects Inside DWG Files: YARA Rule](/forums/diary/Orphaned%2BVBA%2BProjects%2BInside%2BDWG%2BFiles%2BYARA%2BRule/33434/)

**Published**: 2026-10-18. **Last Updated**: 2026-10-18 12:59:30 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Orphaned%2BVBA%2BProjects%2BInside%2BDWG%2BFiles%2BYARA%2BRule/33434/#comments)

Here is the YARA rule I used to detect "[Orphaned VBA Projects Inside DWG Files](https://dshield.org/diary/Orphaned%20VBA%20Projects%20Inside%20DWG%20Files/33420)".

> rule autocad\_orphaned\_vba\_project {
>
> strings: $a = "AC10"
>
> $b = {D0 CF 11 E0 A1 B1 1A E1}
>
> $c = "[Host Extender Info]" ascii
>
> condition: $a at 0 and uint32(0x24) == 0 and $b and $c
>
> }

A VirusTotal retrohunt with this rule gave me only 2 detections:

[09d4607941e458f6dbb6be17825641d863c0b37c185027984e137d8a67e919d8](https://www.virustotal.com/gui/file/09d4607941e458f6dbb6be17825641d863c0b37c185027984e137d8a67e919d8)

[3310c1a9bfe6115e49d8ac372cef5f460850da05138340107e66b958a6b5bca6](https://www.virustotal.com/gui/file/3310c1a9bfe6115e49d8ac372cef5f460850da05138340107e66b958a6b5bca6)

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Orphaned%2BVBA%2BProjects%2BInside%2BDWG%2BFiles%2BYARA%2BRule/33434/#comments)

Click HERE to learn more about classes Didier is teaching for SANS

* [previous](/diary/33430)

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