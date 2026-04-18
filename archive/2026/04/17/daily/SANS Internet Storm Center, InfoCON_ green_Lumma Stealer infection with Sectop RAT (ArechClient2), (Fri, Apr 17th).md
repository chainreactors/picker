---
title: Lumma Stealer infection with Sectop RAT (ArechClient2), (Fri, Apr 17th)
url: https://isc.sans.edu/diary/rss/32904
source: SANS Internet Storm Center, InfoCON: green
date: 2026-04-17
fetch_date: 2026-04-18T04:33:18.738092
---

# Lumma Stealer infection with Sectop RAT (ArechClient2), (Fri, Apr 17th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Brad Duncan](/handler_list.html#brad-duncan "Brad Duncan")

Threat Level: [green](/infocon.html)

* [previous](/diary/32898)

Click HERE to learn more about classes Brad is teaching for SANS

# [Lumma Stealer infection with Sectop RAT (ArechClient2)](/forums/diary/Lumma%2BStealer%2Binfection%2Bwith%2BSectop%2BRAT%2BArechClient2/32904/)

**Published**: 2026-04-17. **Last Updated**: 2026-04-17 00:30:27 UTC
**by** [Brad Duncan](/handler_list.html#brad-duncan) (Version: 1)

[0 comment(s)](/diary/Lumma%2BStealer%2Binfection%2Bwith%2BSectop%2BRAT%2BArechClient2/32904/#comments)

***Introduction***

This diary provides indicators from a [Lumma Stealer](https://malpedia.caad.fkie.fraunhofer.de/details/win.lumma) infection that was followed by [Sectop RAT](https://malpedia.caad.fkie.fraunhofer.de/details/win.sectop_rat) (ArechClient2). I searched for cracked versions of popular copyright-protected software, and I downloaded the initial malware after following the results of one such search. This is a common distribution technique for various families of malware, and I often find Lumma Stealer this way.

In this case, the initial malware for Lumma Stealer was delivered as a password-protected 7-zip archive. The extracted malware is an inflated Windows executable (EXE) file at 806 MB. The EXE is padded with null-bytes (0x00), a technical which increases the EXE size while allowing the compressed archive file to be much smaller. The password-protected archive and inflated EXE file are designed to avoid detection.

***Images from the infection***

[![](https://isc.sans.edu/diaryimages/images/2026-04-17-ISC-diary-image-01.jpg)](https://isc.sans.edu/diaryimages/images/2026-04-17-ISC-diary-image-01a.jpg)
*Shown above: Example of a page with instructions to download the initial malware file.*

[![](https://isc.sans.edu/diaryimages/images/2026-04-17-ISC-diary-image-02.jpg)](https://isc.sans.edu/diaryimages/images/2026-04-17-ISC-diary-image-02a.jpg)
*Shown above: Traffic from the infection filtered in Wireshark.*

[![](https://isc.sans.edu/diaryimages/images/2026-04-17-ISC-diary-image-03.jpg)](https://isc.sans.edu/diaryimages/images/2026-04-17-ISC-diary-image-03a.jpg)
*Shown above: Sectop RAT persistent on an infected Windows host.*

***Indicators of Compromise***

Example of download link from the site advertising cracked versions of copyright-protected software:

hxxps[:]//incolorand[.]com/how-visual-patch-enhances-ui-consistency-across-releases/?utm\_source={CID}&utm\_term=Adobe%20Premiere%20Pro%20(2026)%20Full%20v26.0.2%20Espa%C3%B1ol%20[Mega]&utm\_content={SUBID1}&utm\_medium={SUBID2}

Example of URL for page with the file download instructions:

hxxps[:]//mega-nz.goldeneagletransport[.]com/Adobe\_Premiere\_Pro\_%282026%29\_Full\_v26.0.2\_Espa%C3%B1ol\_%5BMega%5D.zip?c=ABUZ4WkRgQUA\_YUCAFVTFwASAAAAAACh&s=360721

Example of URL for file download from site above site impersonating MEGA:

hxxps[:]//arch.primedatahost3[.]cfd/auth/media/JvWcFd5vUoYTrImvtWQAASTh/Adobe\_Premiere\_Pro\_(2026)\_Full\_v26.0.2\_Espa%C3%B1ol\_%5BMega%5D.zip

Downloaded file:

* SHA256 hash: [c7489e3bf546c5f2d958ac833cc7dbca4368dfba03a792849bc99c48a6b2a14f](https://www.virustotal.com/gui/file/c7489e3bf546c5f2d958ac833cc7dbca4368dfba03a792849bc99c48a6b2a14f)
* File size: 3,888,051 bytes
* File name: adobe\_premiere\_pro\_(2026)\_full\_v26.0.2\_espan?ol\_[mega].7z
* File type: 7-zip archive data, version 0.4
* File description: Password-protected 7-zip archive
* Password: 6919

Extracted malware:

* SHA256 hash: 4849f76dafbef516df91fecfc23a72afffaf77ade51f805eae5ad552bed88923
* File size: 806,127,604 bytes
* File name: appFile.exe
* File type: PE32 executable (GUI) Intel 80386, for MS Windows
* File description: Inflated Windows EXE file for Lumma Stealer, padded with null-bytes

Deflated malware:

* SHA256 hash: [353ddce78d58aef2083ca0ac271af93659cf0039b0b29d0d169fc015bd3610bc](https://www.virustotal.com/gui/file/353ddce78d58aef2083ca0ac271af93659cf0039b0b29d0d169fc015bd3610bc)
* File size: 7,114,156 bytes
* File type: PE32 executable (GUI) Intel 80386, for MS Windows
* File description: Above appFile.exe with most of null-byte padding removed
* [Any.Run sandbox analysis](https://app.any.run/tasks/da962798-e18c-4e47-9379-81ffd72584ff)
* [Triage sandbox analysis](https://tria.ge/260416-wfgr7sbt6y)

Lumma Stealer command and control (C2) domains from Triage sandbox analysis:

* cankgmr[.]cyou
* carytui[.]vu
* decrnoj[.]club
* genugsq[.]best
* longmbx[.]click
* mushxhb[.]best
* pomflgf[.]vu
* strikql[.]shop
* ulmudhw[.]shop

Follow-up malware:

* SHA256 hash: [d9b576eb6827f38e33eda037d2cda4261307511303254a8509eeb28048433b2f](https://www.virustotal.com/gui/file/d9b576eb6827f38e33eda037d2cda4261307511303254a8509eeb28048433b2f)
* File size: 16,450,560 bytes
* File type: PE32+ executable (DLL) (GUI) x86-64, for MS Windows
* Retrieved from: hxxps[:]//enotsosun[.]pw/NetGui.dll
* Saved to: C:\Users\*[username]*\AppData\Local\Temp\16XBPQ29ZBG94TYNOA.dll
* File description: 64-bit DLL to install and run Sectop RAT (ArechClient2)
* Run method: rundll32 *[file path]*,LoadForm
* [Any.Run sandbox analysis](https://app.any.run/tasks/3cb39011-e845-410d-83e3-cfebb69a68b7)
* [Triage sandbox analysis](https://tria.ge/260416-zmr4asdx3v)

Example of Sectop RAT C2 traffic from an infected Windows host:

* hxxp[:]//91.92.241[.]102:9000/wmglb
* hxxp[:]//91.92.241[.]102:9000/wbinjget?q=66B553A8B94CE37C16F4EBC863D51FCC
* tcp[:]//91.92.241[.]102:443/ - encoded or otherwise encrypted traffic (not HTTPS/TLS)

---
Bradley Duncan
brad [at] malware-traffic-analysis.net

Keywords: [LummaStealer](/tag.html?tag=LummaStealer) [Lumma](/tag.html?tag=Lumma) [SectopRAT](/tag.html?tag=SectopRAT) [ArechClient2](/tag.html?tag=ArechClient2)

[0 comment(s)](/diary/Lumma%2BStealer%2Binfection%2Bwith%2BSectop%2BRAT%2BArechClient2/32904/#comments)

Click HERE to learn more about classes Brad is teaching for SANS

* [previous](/diary/32898)

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