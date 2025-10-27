---
title: Fileless Powershell Dropper, (Mon, Oct 17th)
url: https://isc.sans.edu/diary/rss/29156
source: SANS Internet Storm Center, InfoCON: green
date: 2022-10-18
fetch_date: 2025-10-03T20:09:38.747723
---

# Fileless Powershell Dropper, (Mon, Oct 17th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29152)
* [next](/diary/29160)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Fileless Powershell Dropper](/forums/diary/Fileless%2BPowershell%2BDropper/29156/)

**Published**: 2022-10-17. **Last Updated**: 2022-10-18 08:04:23 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[5 comment(s)](/diary/Fileless%2BPowershell%2BDropper/29156/#comments)

I found an interesting Powershell script that drops a malware on the victim's computer. The dropped malware is not new (It's kinda old, though) but the dropper has a very low Virustotal score. The script was detected by one of my hunting rules on VT. It is called "autopowershell.ps1" and has only a score of 3/61 (SHA256:3750576978bfd204c5ac42ee70fb5c21841899878bacc37151370d23e750f8c4)[[1](https://www.virustotal.com/gui/file/3750576978bfd204c5ac42ee70fb5c21841899878bacc37151370d23e750f8c4/detection)]. By "fileless", it means that the malware tries to reduce at the minimum interactions with the file system. But, to achieve persistence, it must write something on the disk. Most of the time, it's done through registry keys. That's what happens with this sample:

![](https://isc.sans.edu/diaryimages/images/isc-20221017-1.PNG)

Suspicious keys are stored in "HKCU\Software\Classes\QDSbIMUygFKR". Note that key names are not randomized, which makes them very interesting IOCs.

In "MSIQ", we find another Powershell script that will be used for persistence.

In "{08CA0AB0-E83C-4BA2-B013-B6359F962B16}", we find the encrypted payload

In "{62352566-EB1A-4C27-81FD-DDEE4E4CFF50}", we find the key to decrypt the payload

The second Powershell script will extract another Base64-encoded script that provides all the classic functions to perform ReflectivePEInjection from PowerSploit[[2](https://powersploit.readthedocs.io/en/latest/CodeExecution/Invoke-ReflectivePEInjection/)]. The injected payload is read from the registry, decrypted and injected. It's a DLL file with a VT score of 30/62 (SHA256:9b3e2e56863fc5a85c5c9f16a82a55c5bc88f5ed049f2e8b21e4e8895e25ec21)[[3](https://www.virustotal.com/gui/file/9b3e2e56863fc5a85c5c9f16a82a55c5bc88f5ed049f2e8b21e4e8895e25ec21/detection)]. Nothing new, it was first uploaded in 2020!

[1] <https://www.virustotal.com/gui/file/3750576978bfd204c5ac42ee70fb5c21841899878bacc37151370d23e750f8c4/detection>
[2] <https://powersploit.readthedocs.io/en/latest/CodeExecution/Invoke-ReflectivePEInjection/>
[3] <https://www.virustotal.com/gui/file/9b3e2e56863fc5a85c5c9f16a82a55c5bc88f5ed049f2e8b21e4e8895e25ec21/detection>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Dropper](/tag.html?tag=Dropper) [Fireless](/tag.html?tag=Fireless) [Malware](/tag.html?tag=Malware) [Powershell](/tag.html?tag=Powershell)

[5 comment(s)](/diary/Fileless%2BPowershell%2BDropper/29156/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/29152)
* [next](/diary/29160)

### Comments

This seems like a typo:
In "{08CA0AB0-E83C-4BA2-B013-B6359F962B16}", we find the encrypted payload
In "{08CA0AB0-E83C-4BA2-B013-B6359F962B16}", we find the key to decrypt the payload

#### Anonymous

#### Oct 18th 2022 2 years ago

Thank you for reporting this! (bad copy/paste)
I just fixed it!

#### Anonymous

#### Oct 18th 2022 2 years ago

The name of this malware family (e.dll) is Misfox -- https://malpedia.caad.fkie.fraunhofer.de/details/win.misfox
The PowerShell loader is -- http://blog.trendmicro.com/trendlabs-security-intelligence/look-js\_powmet-completely-fileless-malware/ -- https://malpedia.caad.fkie.fraunhofer.de/details/js.powmet
9b3e2e56863fc5a85c5c9f16a82a55c5bc88f5ed049f2e8b21e4e8895e25ec21 -- (e.dll) -- also appears to be similar and include code found in the -- bff21cbf95da5f3149c67f2c0f2576a6de44fa9d0cb093259c9a5db919599940 -- https://malpedia.caad.fkie.fraunhofer.de/details/win.andromeda -- sample from that Trend blog post's PowMet -- e27f417b96a33d8449f6cf00b8306160e2f1b845ca2c9666081166620651a3ae

#### Anonymous

#### Oct 18th 2022 2 years ago

artifacts/025381E13342A8EEAA2DBD8182B1824E270D1ECC42B716C75D430246352443A9 contains that same {08CA0AB0-E83C-4BA2-B013-B6359F962B16} value when executed via box-ps. Thank you, I'll look for this sort of box-ps interaction more-oft!

#### Anonymous

#### Oct 18th 2022 2 years ago

Thank you for reporting this!

#### Anonymous

#### Oct 20th 2022 2 years ago

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