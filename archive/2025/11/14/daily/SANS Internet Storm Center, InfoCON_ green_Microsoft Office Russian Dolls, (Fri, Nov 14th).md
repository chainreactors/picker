---
title: Microsoft Office Russian Dolls, (Fri, Nov 14th)
url: https://isc.sans.edu/diary/rss/32484
source: SANS Internet Storm Center, InfoCON: green
date: 2025-11-14
fetch_date: 2025-11-15T03:09:15.725415
---

# Microsoft Office Russian Dolls, (Fri, Nov 14th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/32480)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/sans-november-singapore-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Singapore Standard Time | Nov 17th - Nov 21st 2025 |

# [Microsoft Office Russian Dolls](/forums/diary/Microsoft%2BOffice%2BRussian%2BDolls/32484/)

**Published**: 2025-11-14. **Last Updated**: 2025-11-14 13:42:55 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Microsoft%2BOffice%2BRussian%2BDolls/32484/#comments)

You probably know what are the Russian or Matryoshka dolls. It's a set of wooden dolls of decreasing size placed one inside another[[1](https://en.wikipedia.org/wiki/Matryoshka_doll)]. I found an interesting Microsoft Office document that behaves like this. There was a big decrease in malicious Office documents due to the new Microsoft rules to prevent automatic VBA macros execution. But they remain used, especially RTF documents that exploits the good [CVE-2017-11882](/vuln.html?cve=2017-11882).

The document (SHA256:8437cf40bdd8b005b239c163e774ec7178195f0b80c75e8d27a773831479f68f) that I found uses another technique to prevent the RTF document to be spread directly to the victim. The RTF document is placed into the OOXML document:

```

remnux@remnux:~/malwarezoo/20251113$ zipdump.py mexico_november_po.docx
Index Filename Encrypted Timestamp
1 _rels/ 0 2025-10-22 21:55:10
2 docProps/ 0 2025-10-22 21:55:10
3 word/ 0 2025-11-12 02:58:50
4 [Content_Types].xml 0 2025-10-22 21:55:22
5 docProps/app.xml 0 1980-01-01 00:00:00
6 docProps/core.xml 0 1980-01-01 00:00:00
7 word/_rels/ 0 2025-10-22 21:55:10
8 word/theme/ 0 2025-10-22 21:55:10
9 word/document.xml 0 2025-11-12 02:59:04
10 word/endnotes.xml 0 1980-01-01 00:00:00
11 word/Engaging.rtf 0 2025-11-12 02:58:34
12 word/fontTable.xml 0 1980-01-01 00:00:00
13 word/footer1.xml 0 1980-01-01 00:00:00
14 word/footnotes.xml 0 1980-01-01 00:00:00
15 word/numbering.xml 0 1980-01-01 00:00:00
16 word/settings.xml 0 1980-01-01 00:00:00
17 word/styles.xml 0 1980-01-01 00:00:00
18 word/webSettings.xml 0 1980-01-01 00:00:00
19 word/theme/theme1.xml 0 1980-01-01 00:00:00
20 word/_rels/document.xml.rels 0 2025-11-12 02:58:58
21 word/_rels/settings.xml.rels 0 1980-01-01 00:00:00
22 _rels/.rels 0 1980-01-01 00:00:00
```

The file is referenced in the Word document:

```

remnux@remnux:~/malwarezoo/20251113$ zipdump.py mexico_november_po.docx -s 20 -d | grep Engaging.rtf
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
...
<Relationship Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/aFChunk" Target="/word/Engaging.rtf" Id="YAjq8U"/>
</Relationships>

remnux@remnux:~/malwarezoo/20251113$ zipdump.py mexico_november_po.docx -s 9 -d | grep YAjq8U
<w:document xmlns:wpc=“http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas”
...
<w:body><w:altChunk r:id=“YAjq8U”/>
...
</w:document>
```

The RTF document contains a shellcode that triggers the Equation Editor exploit. The next payload is C:\Users\user01\AppData\Local\Temp\license.ini. It's a DLL (SHA256:d8ed658cc3d0314088cf8135399dbba9511e7f117d5ec93e6acc757b43e58dbc) that is invoked with the following function: IEX

```

CmD.exe /C rundll32 %tmp%\license.ini,IEX A\x12\x0cC
```

You can see the special characters used as parameters to the function here:

![](https://isc.sans.edu/diaryimages/images/isc-20251114-1.png)

This DLL is pretty well obfuscated, I'l still having a look at it but the malware family is not sure... Maybe another Formbook.

[1] <https://en.wikipedia.org/wiki/Matryoshka_doll>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Malware](/tag.html?tag=Malware) [RTF](/tag.html?tag=RTF) [Office](/tag.html?tag=Office) [Microsoft](/tag.html?tag=Microsoft)

[0 comment(s)](/diary/Microsoft%2BOffice%2BRussian%2BDolls/32484/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/sans-november-singapore-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Singapore Standard Time | Nov 17th - Nov 21st 2025 |

* [previous](/diary/32480)

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