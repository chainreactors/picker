---
title: Want More XWorm&#x3f;, (Wed, Mar 4th)
url: https://isc.sans.edu/diary/rss/32766
source: SANS Internet Storm Center, InfoCON: green
date: 2026-03-04
fetch_date: 2026-03-05T04:07:36.169527
---

# Want More XWorm&#x3f;, (Wed, Mar 4th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/32762)
* [next](/diary/32768)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/amsterdam-march-2026/course/reverse-engineering-malware-advanced-code-analysis) | Amsterdam | Mar 16th - Mar 20th 2026 |

# [Want More XWorm?](/forums/diary/Want%2BMore%2BXWorm/32766/)

**Published**: 2026-03-04. **Last Updated**: 2026-03-04 09:48:39 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Want%2BMore%2BXWorm/32766/#comments)

And another XWorm[[1](https://malpedia.caad.fkie.fraunhofer.de/details/win.xworm)] wave in the wild! This malware family is not new and heavily spread but delivery techniques always evolve and deserve to be described to show you how threat actors can be imaginative! This time, we are facing another piece of multi-technology malware.

Here is a quick overview:

![](https://isc.sans.edu/diaryimages/images/isc-20260304-1.png)

The Javascript is a classic obfuscated one:

![](https://isc.sans.edu/diaryimages/images/isc-20260304-2.png)

No need to try to analyze it, just let it run in a sandbox and see its magic. It will drop a PowerShell script in a temporary directory (“C:\Temp\ps\_5uGUQcco8t5W\_1772542824586.ps1*”).* This loader will decode (Base64 + XOR) another payload that invokes another piece of PowerShell in memory:

![](https://isc.sans.edu/diaryimages/images/isc-20260304-3.png)

Because the last payload is XOR-encrypted, it is not obfuscated and easy to understand. The DLL exports a function called “ProcessHollowing” (nice name, btw) and acts as a loader. It inject the XWorm client in the .Net compiler process…

Here is the extracted config:

```

{
    "c2": [
        "204[.]10[.]160[.]190:7003"
    ],
    "attr": {
        "install_file": "USB.exe"
    },
    "keys": [
        {
            "key": "aes_key",
            "kind": "aes.plain",
            "value": "XAorWEAzx4+ic89KWd910w=="
        }
    ],
    "rule": "Xworm",
    "mutex": [
        "Cqu1F0NxohroKG5U"
    ],
    "family": "xworm",
    "version": "XWorm V6.4"
}
```

Do you recognize the C2 IP address? It's the same as the one detected in my latest diary![[2](https://isc.sans.edu/diary/Fake%20Fedex%20Email%20Delivers%20Donuts%21/32754)]

And some IOC's:

| File | SHA256 |
| --- | --- |
| Inv-4091-CBM-4091-CUSTOM-Packing\_List.js | 5140b02a05b7e8e0c0afbb459e66de4d74f79665c1d83419235ff0cdcf046e9c |
| ps\_5uGUQcco8t5W\_1772542824586.ps1 | 5a3d33efaaff4ef7b7d473901bd1eec76dcd9cf638213c7d1d3b9029e2aa99a4 |
| MAD.dll | af3919de04454af9ed2ffa7f34e4b600b3ce24168f745dba4c372eb8bcc22a21 |
| payload.exe (XWorm) | 58e38fffb78964300522d89396f276ae0527def8495126ff036e57f0e8d3c33b |

[1] <https://malpedia.caad.fkie.fraunhofer.de/details/win.xworm>
[2] [https://isc.sans.edu/diary/Fake%20Fedex%20Email%20Delivers%20Donuts!/32754](https://isc.sans.edu/diary/Fake%20Fedex%20Email%20Delivers%20Donuts%21/32754)

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [JavaScript](/tag.html?tag=JavaScript) [Malware](/tag.html?tag=Malware) [PowerShell](/tag.html?tag=PowerShell) [XWorm](/tag.html?tag=XWorm)

[0 comment(s)](/diary/Want%2BMore%2BXWorm/32766/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/amsterdam-march-2026/course/reverse-engineering-malware-advanced-code-analysis) | Amsterdam | Mar 16th - Mar 20th 2026 |

* [previous](/diary/32762)
* [next](/diary/32768)

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