---
title: More Free File Sharing Services Abuse, (Wed, Jul 16th)
url: https://isc.sans.edu/diary/rss/32112
source: SANS Internet Storm Center, InfoCON: green
date: 2025-07-17
fetch_date: 2025-10-06T23:56:18.094566
---

# More Free File Sharing Services Abuse, (Wed, Jul 16th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32108)
* [next](/diary/32116)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [More Free File Sharing Services Abuse](/forums/diary/More%2BFree%2BFile%2BSharing%2BServices%2BAbuse/32112/)

**Published**: 2025-07-16. **Last Updated**: 2025-07-16 13:00:28 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/More%2BFree%2BFile%2BSharing%2BServices%2BAbuse/32112/#comments)

A few months ago, I wrote a diary about online services used to exfiltrate data[[1](https://isc.sans.edu/diary/Online%2BServices%2BAgain%2BAbused%2Bto%2BExfiltrate%2BData/31862)]. In this diary, I mentioned some well-known services. One of them was catbox.moe[[2](https://catbox.moe/)]. Recently, I found a sample that was trying to download some payload from this website. I performed a quick research and collected more samples!

I collected (and stopped because it was a constant flood!) 612 URLs pointing to direct downloads (hxxps://files[.]catbox[.]moe/xxxxxx). Some where popular and used by multiple samples:

```

remnux@remnux:~/malwarezoo/catmoe-research$ cat urls.txt | sort | uniq -c | sort -rn| head -10
 23 hxxps://files[.]catbox[.]moe/a1z5ds.dll
 20 hxxps://files[.]catbox[.]moe/63g8p0.dll
 16 hxxps://files[.]catbox[.]moe/h7b4e4.dll
 13 hxxps://files[.]catbox[.]moe/mqhwlv.sys
 13 hxxps://files[.]catbox[.]moe/j5s1uy.bin
 13 hxxps://files[.]catbox[.]moe/3ps4f5.dll
 10 hxxps://files[.]catbox[.]moe/5ikx0w.dll
  9 hxxps://files[.]catbox[.]moe/l3whjb.wav
  9 hxxps://files[.]catbox[.]moe/1z3yes.cmd
  7 hxxps://files[.]catbox[.]moe/eaek1u.dll
```

What are the most popular file types?

```

remnux@remnux:~/malwarezoo/catmoe-research$ file *| cut -d “:” -f 2 | sort | uniq -c | head -30
55 PE32+ executable (DLL) (GUI) x86-64, for MS Windows
29 PE32+ executable (native) x86-64, for MS Windows
21 ASCII text, with no line terminators
20 PE32+ executable (DLL) (console) x86-64, for MS Windows
20 PE32+ executable (console) x86-64, for MS Windows
11 data
10 RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 48000 Hz
9 DOS batch file, ASCII text, with CRLF line terminators
9 ASCII text, with CRLF line terminators
8 DOS batch file, ASCII text, with very long lines, with CRLF line terminators
5 RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, stereo 44100 Hz
5 RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 44100 Hz
3 Zip archive data, at least v2.0 to extract
3 RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, stereo 48000 Hz
3 ASCII text, with very long lines, with CRLF line terminators
2 RAR archive data, v5
2 PNG image data, 800 x 450, 8-bit/color RGB, non-interlaced
2 PNG image data, 500 x 500, 8-bit/color RGBA, non-interlaced
2 PNG image data, 1080 x 1080, 8-bit/color RGB, non-interlaced
2 PE32+ executable (GUI) x86-64, for MS Windows
2 PE32 executable (GUI) Intel 80386, for MS Windows, UPX compressed
2 PE32+ executable (DLL) (EFI application) x86-64, for MS Windows
2 PE32 executable (console) Intel 80386, for MS Windows
2 MS-DOS executable PE32 executable (GUI) Intel 80386, for MS Windows, MZ for MS-DOS
2 JPEG image data, Exif standard
2 ISO Media, MP4 Base Media v1 [IS0 14496-12
2 empty
2 DOS batch file, UTF-8 Unicode text, with CRLF line terminators
2 DOS batch file, ASCII text, with CRLF line terminators, with escape sequences
```

Note that PE files should NOT be available on catbox.moe:

![](https://isc.sans.edu/diaryimages/images/isc-20250716-1.png)

I hope they don't just filter files based on the extension! Conclusion: if you don't use such online services, any traffic to them can be considered as suspicious.

[1] [https://isc.sans.edu/diary/Online+Services+Again+Abused+to+Exfiltrate+Data/31862](https://isc.sans.edu/diary/Online%2BServices%2BAgain%2BAbused%2Bto%2BExfiltrate%2BData/31862)
[2] <https://catbox.moe/>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Files](/tag.html?tag=Files) [Online](/tag.html?tag=Online) [Sharing](/tag.html?tag=Sharing)

[0 comment(s)](/diary/More%2BFree%2BFile%2BSharing%2BServices%2BAbuse/32112/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/32108)
* [next](/diary/32116)

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