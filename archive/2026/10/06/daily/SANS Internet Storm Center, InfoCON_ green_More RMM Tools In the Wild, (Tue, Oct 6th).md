---
title: More RMM Tools In the Wild, (Tue, Oct 6th)
url: https://isc.sans.edu/diary/rss/33400
source: SANS Internet Storm Center, InfoCON: green
date: 2026-10-06
fetch_date: 2026-10-07T07:55:23.040343
---

# More RMM Tools In the Wild, (Tue, Oct 6th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33396)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

# [More RMM Tools In the Wild](/forums/diary/More%2BRMM%2BTools%2BIn%2Bthe%2BWild/33400/)

**Published**: 2026-10-06. **Last Updated**: 2026-10-06 13:16:02 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/More%2BRMM%2BTools%2BIn%2Bthe%2BWild/33400/#comments)

It seems that a trend started… I continue my journey discovering more RMM ("Remote Management & Monitoring") tools abused by threat actors! A few days ago, I wrote a diary[[1](https://isc.sans.edu/diary/ScreenConnect%2BClient%2BAbused%2Bby%2BAttackers/33388)] about ScreenConnect used in the wild. Today, I found another one.

Same scenario, it started with a phishing email that delivers a fake PDF invoice to the victim:

![](https://isc.sans.edu/diaryimages/images/isc-20261006-1.png)

When the PDF is opened, it just redirect to a malicious VBS file. Indeed, the PDF contains an “OpenAction” and “URI” keywords, that sounds weird!

```

remnux@remnux:~/files/samples$ pdf-parser.py Transaction\ Receipt\ .pdf -o 3
obj 3 0
Type: /Page
Referencing: 1 0 R, 2 0 R, 4 0 R

  <<
    /Type /Page
    /Parent 1 0 R
    /Resources 2 0 R
    /MediaBox [0 0 595.2799999999999727 841.8899999999999864]
    /Annots
      <<
        /Type /Annot
        /Subtype /Link
        /Rect [0. 841.8899999999999864 595.2799999999999727 71.3010032362460606]
        /Border [0 0 0]
        /A
          <<
            /S /URI
            /URI (hxxps://up-theta-rose.vercel[.]app/adobe_new_update.vbs)
          >>
      >>
    ] /Contents 4 0 R
  >>
```

The URL will be visited thanks to the OpenAction. This is a common trick to avoid writing URLs in email bodies that can be easily detected.

The VBS file is pretty simple and even not obfuscated. It will display another PDF as a decoy: a non-blurred version of the initial attachment.

In parallel, a MSI archive will be downloaded and installed:

```

hxxps://up-theta-rose.vercel[.]app/action1.msi
```

The MSI file contains 4 files that are not reported as malicious by VT:

```

$ sha256sum *
eaff35d250c9b04f51c971e70082740dbfeee5dd846829d541f588ad43378727  a1_7z_dll_file
996b01e15f85e165899630721a141b178a9c372b6e878012180ec9e9d4e7bd06  a1_sas_dll_file
1b19115d5ebdc216e0ab3adf2c643648cfc70a385f4caf0217c679f9f3b20342  action1_remote_exe
941695d20d82dd5d62f74b0111feb23720637202f6c797df2a02e2cb6cb6e8e3  main_service_exe
```

These files belongs to the RMM tool developed by Action1[[2](https://www.action1.com/remote-access/)] and are signed with an "Action1 Corporation" certificate that expired in May 2026.

The tool installs itself as a service for persistence ("A1Agent" - "Action1 Agent"), executing C:\Windows\Action1\action1\_agent.exe.

The registy key "HKLM\Software\Action1\Agent" contains the values: CustomerId, Certificate, PrivateKey, MSI & INSTALLDIR.

The CustomerID is: 49b18106-681d-456a-b098-092e2818c09a and is connecting to the Action1 infrastructure via server[.]na-2.action1[.]com.

We are facing here the same behaviour: the threat actor abuse the cloud infrastructure of the company developing the RMM tool, probably using a free/test account.

[Update 15:11 CET]

A second sample reached my mailbox, this take mimicking a DHL document:

![](https://isc.sans.edu/diaryimages/images/isc-20261006-2.png)

The URL in the PDF is similar, it contains a URL (hxxps://update-two-tau[.]vercel[.]app/adobe-ne) pointing to a ZIP archive with an HTA script. It delivers the same MSI file.

[1] [https://isc.sans.edu/diary/ScreenConnect+Client+Abused+by+Attackers/33388](https://isc.sans.edu/diary/ScreenConnect%2BClient%2BAbused%2Bby%2BAttackers/33388)
[2] <https://www.action1.com/remote-access/>

Xavier Mertens (@xme)
Senior ISC Handler | SANS Principal Instructor | Freelance Consultant
[Xameco](https://xameco.be) | [PGP Key](https://xameco.be/pgpkey.txt)

Keywords: [Action1](/tag.html?tag=Action1) [Phishing](/tag.html?tag=Phishing) [Remote](/tag.html?tag=Remote) [RMM](/tag.html?tag=RMM) [Tool](/tag.html?tag=Tool)

[0 comment(s)](/diary/More%2BRMM%2BTools%2BIn%2Bthe%2BWild/33400/#comments)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

* [previous](/diary/33396)

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