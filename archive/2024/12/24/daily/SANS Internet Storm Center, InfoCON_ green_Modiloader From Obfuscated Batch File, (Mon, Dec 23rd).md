---
title: Modiloader From Obfuscated Batch File, (Mon, Dec 23rd)
url: https://isc.sans.edu/diary/rss/31540
source: SANS Internet Storm Center, InfoCON: green
date: 2024-12-24
fetch_date: 2025-10-06T19:42:53.256966
---

# Modiloader From Obfuscated Batch File, (Mon, Dec 23rd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31538)
* [next](/diary/31542)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Modiloader From Obfuscated Batch File](/forums/diary/Modiloader%2BFrom%2BObfuscated%2BBatch%2BFile/31540/)

**Published**: 2024-12-23. **Last Updated**: 2024-12-23 06:25:57 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Modiloader%2BFrom%2BObfuscated%2BBatch%2BFile/31540/#comments)

My last investigation is a file called “Albertsons\_payment.GZ”, received via email. The file looks like an archive but is identified as a picture by TrID:

```

Collecting data from file: Albertsons_payment.GZ
100.0% (.PG/BIN) PrintFox/Pagefox bitmap (640x800) (1000/1)
```

Finally, it’s a Windows Cabinet file:

```

remnux@remnux:/MalwareZoo/20241218$ cabextract -t Albertsons_payment.GZ
Testing cabinet: Albertsons_payment.GZ
  Chine_ana22893D347515193D264135FF38996037FF515169loodatke.PNG  OK  dc156637aebf04336700a9bc71c78aad
                          OK                   7cd592cb2f2179e188e9e99cb7c06bba
  Svcrhpjadgyclc.cmd  OK                       7afcba92a35ba26fcde12f3aba8ff7d8
```

The archive contains a picture that mimics a document:

![](https://isc.sans.edu/diaryimages/images/Chine_ana22893D347515193D264135FF38996037FF515169loodatke.PNG)

The file with strange characters contains only an integer value:

```

64928
```

(The purpose is unknown at this time)

The .cmd file looks much more interesting!

![](https://isc.sans.edu/diaryimages/images/isc-20241223-1.PNG)

Yes, even Windows bat files can be deeply obfuscated! The obfuscation used by the Attacker is called “string slicing”. Commands are reconstructed by extracting characters from a string. Here is a simple example:

```

set “VARIABLE=abcdef"
echo %VARIABLE:~2,1%”
c
```

The file seems to contain an interesting payload:

```

remnux@remnux:/MalwareZoo/20241218/files$ grep "\-\-\-\-" Svcrhpjadgyclc.cmd
%XbymqYoxZh%                                                 -----BEGIN X509 CRL-----
-----END X509 CRL-----
```

Based on the file size,  the deobfuscate process will take some time but also because the technique above is used multiple times. Let’s execute the script and capture its behaviour:

![](https://isc.sans.edu/diaryimages/images/isc-20241223-2.PNG)

Here are the most interesting action performed by the script. The script uses a LOLbin called extrac32.exe[[1](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/extract)]. To defeat security rules looking for suspicious processes, it copies commands to another directory. First cmd.exe:

```

C:\Windows\System32\extrac32  /C /Y C:\Windows\System32\cmd.exe  "C:\Users\Public\alpha.exe"
```

Then certutil.exe:

```

C:\Users\Public\alpha /c extrac32 /C /Y C:\Windows\System32\certutil.exe C:\Users\Public\kn.exe
```

Based on the grep command (see above), we have an interesting payload in this file. Indeed, the copy of certutil.exe is used to extract the next stage from the .cmd file:

```

C:\Users\Public\alpha  /c  C:\Users\Public\kn  -decodehex -F "C:\Users\REM\Desktop\folder\Svcrhpjadgyclc.cmd" \
    "C:\\Users\\Public\\spoolsv.MPEG" 9
C:\Users\Public\alpha  /c  C:\Users\Public\kn  -decodehex -F "C:\Users\Public\spoolsv.MPEG" \
    "C:\Users\Public\Libraries\spoolsv.COM" 12
```

The next stage is spoolsv.com[[2](https://www.virustotal.com/gui/file/baa12b649fddd77ef62ecd2b3169fab9bb5fbe78404175485f9a7fb48dc4456d)] (SHA256:baa12b649fddd77ef62ecd2b3169fab9bb5fbe78404175485f9a7fb48dc4456d).

The payload is a Delphi-based malware that looks to be Modiloader[[3](https://malpedia.caad.fkie.fraunhofer.de/details/win.dbatloader)]. It tries to fetch the next stage from this URL: hxxps://swamfoxinnc[.]com/233\_Svcrhpjadgy. The site does not provide the payload anymore but I was able to grab it from Virustotal. I simulated the website and content in my lab but spoolsv.com crashes! It just performed the DNS lookup but did not fetched the URL...

[1] <https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/extract>
[2] <https://www.virustotal.com/gui/file/baa12b649fddd77ef62ecd2b3169fab9bb5fbe78404175485f9a7fb48dc4456d>
[3] <https://malpedia.caad.fkie.fraunhofer.de/details/win.dbatloader>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Batch](/tag.html?tag=Batch) [Malware](/tag.html?tag=Malware) [Cmd](/tag.html?tag=Cmd) [Modiloader](/tag.html?tag=Modiloader) [Obfuscation](/tag.html?tag=Obfuscation)

[0 comment(s)](/diary/Modiloader%2BFrom%2BObfuscated%2BBatch%2BFile/31540/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/31538)
* [next](/diary/31542)

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