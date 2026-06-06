---
title: The Evil MSI Background is Back&#x21;, (Fri, Jun 5th)
url: https://isc.sans.edu/diary/rss/33054
source: SANS Internet Storm Center, InfoCON: green
date: 2026-06-05
fetch_date: 2026-06-06T05:51:32.477047
---

# The Evil MSI Background is Back&#x21;, (Fri, Jun 5th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33048)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

# [The Evil MSI Background is Back!](/forums/diary/The%2BEvil%2BMSI%2BBackground%2Bis%2BBack/33054/)

**Published**: 2026-06-05. **Last Updated**: 2026-06-05 06:47:26 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/The%2BEvil%2BMSI%2BBackground%2Bis%2BBack/33054/#comments)

A few months ago, I wrote a diary about a payload that was embedded into a JPEG picture. It was a MSI-branded background[[1](https://isc.sans.edu/diary/Malicious%2BScript%2BDelivering%2BMore%2BMaliciousness/32682)]. Yesterday, I spotted another one! It seems that the technic is getting more and more popular. This time, it started with a mail containing a WeTransfer link.

![](https://isc.sans.edu/diaryimages/images/isc-20260605-1.png)

Often, the WeTransfer brand is abused in phishing emails. Here, it's was an official link:

```

hxxps://we[.]tl/t-R4Wv1JkvFfC4Awus
```

The thread-actor shared the initial file via this platform. The file is a piece of Javascript called "Remittance Advice.js" (SHA256:8a83de81fbac4eb0961f3d58982f299664a5fa4c874c7469e69f85f3fc5bd33f).

The contains a lot of junk code that will just do nothing:

![](https://isc.sans.edu/diaryimages/images/isc-20260605-2.png)

Every for-loop will just move to the next line. In the middle of the file (>2MB), we have the interesting code that will perform the following tasks:

It will decode the next payload in an environment variable:

```

[Environment]::SetEnvironmentVariable("INTERNAL_DB_CACHE", <encoded_payload>)
```

The obfuscation technique used is ROT13, old but still very efficient:

```

cbjrefuryy.rkr -RkrphgvbaCbyvpl Olcnff -AbCebsvyr -JvaqbjFglyr Uvqqra -Pbzznaq
```

Decoded, it becomes:

```

powershell.exe -ExecutionPolicy Bypass -NoProfile -WindowStyle Hidden -Command
```

PowerShell is executed throug WMI:

* winmgmts:root\cimv2: connect to WMI
* Win32\_ProcessStartup: configure process startup (hidden window)
* Win32\_Process.Create(): spawn the process

The full command is:

```

powershell.exe -ExecutionPolicy Bypass -NoProfile -WindowStyle Hidden -Command [ScriptBlock]::Create(${env:INTERNAL_DB_CACHE})
```

This code will fetch an MSI background JPEG file from this location:

```

hxxp://icy-lab-0431[.]guilherme-telecomunicacoes2024[.]workers[.]dev/mCSlB
```

Note that the threat-actor likes to use well-known services to store his/her payloads. workers.dev is the default, free subdomain provided by Cloudflare for deploying serverless applications[[2](https://developers.cloudflare.com/workers/)].

The technique to hide the next payload is the same as my previous diary. The Base64-encode payload is delimited here with "IN-" and "-in1". To defeat simple Base64 lookups, all "A" characters have been replaced by "#". Once decoded, the payload is a .Net DLL (SHA256:184a3008adff54cb345a599b4f3ca0c7bde29d8ac8379783ff40cd4e7ecc931b). It's a modified version of the Microsoft.Win32.TaskScheduler, an open-source .NET library for managing Windows Task Scheduler[[3](https://github.com/dahall/taskscheduler)].

The PowerShell payload will also fetch another file that will be passed to the loaded malicious DLL:

```

hxxps://pub-a06eb79f0ebe4a6999bcc71a2227d8e3[.]r2[.]dev/snake.png
```

Here again, a legit online service is used. r2.dev is the default domain used by Cloudflare R2 to serve files and assets stored in public cloud-native buckets. It is a globally distributed, S3-compatible object storage service that allows developers to store large amounts of unstructured data[[4](https://developers.cloudflare.com/r2/buckets/public-buckets/)].

The file looks to be another background and contains probably another payload protected by steganograpy (very common with the .Net loaders):

![](https://isc.sans.edu/diaryimages/images/isc-20260605-3(1).png)

I'm now reversing the .Net loader. Stay tuned for more details soon!

[1] [https://isc.sans.edu/diary/Malicious+Script+Delivering+More+Maliciousness/32682](https://isc.sans.edu/diary/Malicious%2BScript%2BDelivering%2BMore%2BMaliciousness/32682)
[2] <https://developers.cloudflare.com/workers/>
[3] <https://github.com/dahall/taskscheduler>
[4] <https://developers.cloudflare.com/r2/buckets/public-buckets/>

**Xavier Mertens (@xme)**
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://raw.githubusercontent.com/xme/pgp/refs/heads/main/public.key)

Keywords: [JavaScript](/tag.html?tag=JavaScript) [Malware](/tag.html?tag=Malware) [MSI](/tag.html?tag=MSI) [Payload](/tag.html?tag=Payload) [Background](/tag.html?tag=Background) [WeTransfer](/tag.html?tag=WeTransfer)

[0 comment(s)](/diary/The%2BEvil%2BMSI%2BBackground%2Bis%2BBack/33054/#comments)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

* [previous](/diary/33048)

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