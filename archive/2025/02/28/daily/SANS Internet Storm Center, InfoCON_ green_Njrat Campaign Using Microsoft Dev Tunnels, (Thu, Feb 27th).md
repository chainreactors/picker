---
title: Njrat Campaign Using Microsoft Dev Tunnels, (Thu, Feb 27th)
url: https://isc.sans.edu/diary/rss/31724
source: SANS Internet Storm Center, InfoCON: green
date: 2025-02-28
fetch_date: 2025-10-06T20:47:33.015561
---

# Njrat Campaign Using Microsoft Dev Tunnels, (Thu, Feb 27th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31716)
* [next](/diary/31728)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Njrat Campaign Using Microsoft Dev Tunnels](/forums/diary/Njrat%2BCampaign%2BUsing%2BMicrosoft%2BDev%2BTunnels/31724/)

**Published**: 2025-02-27. **Last Updated**: 2025-02-27 08:54:32 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Njrat%2BCampaign%2BUsing%2BMicrosoft%2BDev%2BTunnels/31724/#comments)

I spotted new  Njrat[[1](https://malpedia.caad.fkie.fraunhofer.de/details/win.njrat)] samples that (ab)use the Microsoft dev tunnels[[2](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/overview)] service to connect to their C2 servers. This is a service that allows developers to expose local services to the Internet securely for testing, debugging, and collaboration. It provides temporary, public, or private URLs that will enable remote access to a development environment without deploying code to production. Dev tunnels create a secure, temporary URL that maps to a local service running on your machine, they work across firewalls and NAT, and their access can be restricted. This is a service similar to the good old ngrok[[3](https://ngrok.com)].

Here are two samples:

* dsadasfjamsdf.exe (SHA256: 0b0c8fb59db1c32ed9d435abb0f7e2e8c3365325d59b1f3feeba62b7dc0143ee[[4](https://www.virustotal.com/gui/file/0b0c8fb59db1c32ed9d435abb0f7e2e8c3365325d59b1f3feeba62b7dc0143ee/detection)])
* c3df7e844033ec8845b244241c198fcc.exe (SHA256: 9ea760274186449a60f2b663f535c4fbbefa74bc050df07614150e8321eccdb7[[5](https://www.virustotal.com/gui/file/9ea760274186449a60f2b663f535c4fbbefa74bc050df07614150e8321eccdb7)])

They use different dev tunnel URLs but their ImpHash (Import Hash) is the same (f34d5f2d4577ed6d9ceec516c1f5a744):

* hxxps://nbw49tk2-25505[.]euw[.]devtunnels[.]ms/
* hxxps://nbw49tk2-27602[.]euw[.]devtunnels[.]ms/

This is the code where the malware will send its status to the C2 server:

![](https://isc.sans.edu/diaryimages/images/isc-20250227-1.png)

The variable "OK.HH" contains the dev tunnel URL. At the end, a "text" variable is created to contain the status of the malware capabilities (True or False). Note the "OK.usb" variable: If set to True, the malware will try to propagate through USB devices:

![](https://isc.sans.edu/diaryimages/images/isc-20250227-2.png)

Here is one of their extracted config:

```

{
  "C2": "hxxps://nbw49tk2-25505[.]euw[.]devtunnels[.]ms/",
  "Ports": "25505",
  "Botnet": "HacKed","Options": {
      "Auto-run registry key": "Software\\Microsoft\\Windows\\CurrentVersion\\Run\\af63c521a8fa69a8f1d113eb79855a75",
      "Splitter": "|'|'|"
  },
  "Version": "im523"
}
```

Conclusion: If you don't use the Microsoft service, hunting for devtunnels[.]ms in your DNS logs is a good idea!

[1] <https://malpedia.caad.fkie.fraunhofer.de/details/win.njrat>
[2] <https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/overview>
[3] <https://ngrok.com>
[4] <https://www.virustotal.com/gui/file/0b0c8fb59db1c32ed9d435abb0f7e2e8c3365325d59b1f3feeba62b7dc0143ee/detection>
[5] [https://www.virustotal.com/gui/file/9ea760274186449a60f2b663f535c4fbbefa74bc050df07614150e8321eccdb7/detection](https://www.virustotal.com/gui/file/9ea760274186449a60f2b663f535c4fbbefa74bc050df07614150e8321eccdb7)

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Njrat](/tag.html?tag=Njrat) [Malware](/tag.html?tag=Malware) [Microsoft](/tag.html?tag=Microsoft) [Dev](/tag.html?tag=Dev) [Tunnel](/tag.html?tag=Tunnel) [Grok](/tag.html?tag=Grok) [C2](/tag.html?tag=C2)

[0 comment(s)](/diary/Njrat%2BCampaign%2BUsing%2BMicrosoft%2BDev%2BTunnels/31724/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/31716)
* [next](/diary/31728)

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