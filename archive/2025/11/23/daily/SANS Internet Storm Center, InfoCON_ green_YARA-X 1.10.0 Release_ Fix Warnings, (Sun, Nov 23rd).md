---
title: YARA-X 1.10.0 Release: Fix Warnings, (Sun, Nov 23rd)
url: https://isc.sans.edu/diary/rss/32514
source: SANS Internet Storm Center, InfoCON: green
date: 2025-11-23
fetch_date: 2025-11-24T03:22:21.167382
---

# YARA-X 1.10.0 Release: Fix Warnings, (Sun, Nov 23rd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Didier Stevens](/handler_list.html#didier-stevens "Didier Stevens")

Threat Level: [green](/infocon.html)

* [previous](/diary/32512)

# [YARA-X 1.10.0 Release: Fix Warnings](/forums/diary/YARAX%2B1100%2BRelease%2BFix%2BWarnings/32514/)

**Published**: 2025-11-23. **Last Updated**: 2025-11-23 10:50:02 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/YARAX%2B1100%2BRelease%2BFix%2BWarnings/32514/#comments)

[YARA-X's 1.10.0](https://github.com/VirusTotal/yara-x/releases/tag/v1.10.0) release brings a new command: fix warnings.

If you have a rule that would generate a warning with a help section (explaining how to fix it), like this example rule:

```

rule FixableCountWarning
{
    strings:
        $a1 = "malicious"
        $a2 = "badstuff"

    condition:
        0 of ($a*)
}
```

![](https://isc.sans.edu/diaryimages/images/20251123-110201.png)

Then YARA-X from version 1.10.0 on can fix this for you

You will get a warning when you use this rule:

![](https://isc.sans.edu/diaryimages/images/20251123-110226.png)

The suggested fix is to replace 0 with none.

This can be done automatically with command fix warnings:

![](https://isc.sans.edu/diaryimages/images/20251123-110255.png)

Remark that this command alters your original rule file, and doesn't make a backup of the unaltered file:

![](https://isc.sans.edu/diaryimages/images/20251123-110323.png)

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/YARAX%2B1100%2BRelease%2BFix%2BWarnings/32514/#comments)

* [previous](/diary/32512)

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