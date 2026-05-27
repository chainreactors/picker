---
title: Possible ACR Stealer From Page Impersonating Claude, (Tue, May 26th)
url: https://isc.sans.edu/diary/rss/33018
source: SANS Internet Storm Center, InfoCON: green
date: 2026-05-26
fetch_date: 2026-05-27T06:12:40.819759
---

# Possible ACR Stealer From Page Impersonating Claude, (Tue, May 26th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Brad Duncan](/handler_list.html#brad-duncan "Brad Duncan")

Threat Level: [green](/infocon.html)

* [previous](/diary/33016)

Click HERE to learn more about classes Brad is teaching for SANS

# [Possible ACR Stealer From Page Impersonating Claude](/forums/diary/Possible%2BACR%2BStealer%2BFrom%2BPage%2BImpersonating%2BClaude/33018/)

**Published**: 2026-05-26. **Last Updated**: 2026-05-26 00:01:48 UTC
**by** [Brad Duncan](/handler_list.html#brad-duncan) (Version: 1)

[0 comment(s)](/diary/Possible%2BACR%2BStealer%2BFrom%2BPage%2BImpersonating%2BClaude/33018/#comments)

***Introduction***

In recent weeks, I've searched for pages impersonating Claude that distribute malware. In recent weeks, I've reliably found these sites through malicious ads in Google searches that lead to these pages, often concealed in URLs for sites.google[.]com, such as [this example from 2026-05-11](https://malware-traffic-analysis.net/2026/05/11/index.html).

These fake Claude pages generally show instructions for macOS malware when viewed through a macOS system, and they will show instructions for Windows malware when viewed through a Windows system. Today's dairy shows an example of Windows malware from one of these pages seen on Monday, 2026-05-25. Based on the C2 domain for post-infection traffic, this appears to be an infection for [ACR Stealer](https://malpedia.caad.fkie.fraunhofer.de/details/win.acr_stealer).

***Images***

[![](https://isc.sans.edu/diaryimages/images/2026-05-25-ISC-diary-image-01.png)](https://isc.sans.edu/diaryimages/images/2026-05-25-ISC-diary-image-01a.png)
*Shown above: Web page impersonating Claude with a button to "Download for Windows."*

[![](https://isc.sans.edu/diaryimages/images/2026-05-25-ISC-diary-image-02.png)](https://isc.sans.edu/diaryimages/images/2026-05-25-ISC-diary-image-02a.png)
*Shown above: Instructions to install Claude on Windows are actually instructions that will infect a vulnerable computer with malware.*

[![](https://isc.sans.edu/diaryimages/images/2026-05-25-ISC-diary-image-03.png)](https://isc.sans.edu/diaryimages/images/2026-05-25-ISC-diary-image-03a.png)
*Shown above: Traffic from a Windows host when following instructions from the fake Claude download page.*

***Indicators of Compromise***

Fake Claude download page:

* hxxps[:]//fairpoint29.com/

From the above page, URL for the initial download:

* hxxps[:]//primemetricsa[.]com/1518925

Follow-up download:

* hxxps[:]//6ryuefl.creativecommunityinfo[.]art/Camel-91267b64-989f-49b4-89b4-9e015844d42d

A further download:

* hxxps[:]//i.ibb[.]co/Xx16sbMz/init-block.jpg

Domain for post-infection HTTPS traffic to C2 server:

* yw.enhanceblabber[.]cc

Initial download:

SHA256 hash: [70b5ecc110e074dbca92932c0e840ea3492ea0a43c3f215b71392c12b02213b2](https://www.virustotal.com/gui/file/70b5ecc110e074dbca92932c0e840ea3492ea0a43c3f215b71392c12b02213b2)

* File size: 2,416,902 bytes
* File type: Zip archive data, at least v1.0 to extract
* File location: hxxps[:]//primemetricsa[.]com/1518925
* NOTE: There's an issue with this zip archive, so its contents will not extract correctly using typical extraction tools.

Follow-up download, PowerShell script:

SHA256 hash: [a14c3ecf5eb3d2543358482e43dc765dbf9ee7a4bec7571f5ecb8829ca719692](https://www.virustotal.com/gui/file/a14c3ecf5eb3d2543358482e43dc765dbf9ee7a4bec7571f5ecb8829ca719692/content)

* File size: 4,177,395 bytes
* File type: ASCII text, with very long lines, with CRLF line terminators
* File location: hxxps[:]//6ryuefl.creativecommunityinfo[.]art/Camel-91267b64-989f-49b4-89b4-9e015844d42d

A further download:

SHA256 hash: [47fa746422f1bf6b7712dc6803378e6a995488007193a7441d790f70d204728f](https://www.virustotal.com/gui/file/47fa746422f1bf6b7712dc6803378e6a995488007193a7441d790f70d204728f)

* File size: 628,035 bytes
* File type: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 5256x5256, components 3
* File location: hxxps[:]//i.ibb[.]co/Xx16sbMz/init-block.jpg
* NOTE: This image doesn't appear to be malicious, nor could I find any obvious signs of embedded data, but it's somehow related to this infection chain.

---
Bradley Duncan
brad [at] malware-traffic-analysis.net

Keywords: [ACRStealer](/tag.html?tag=ACRStealer)

[0 comment(s)](/diary/Possible%2BACR%2BStealer%2BFrom%2BPage%2BImpersonating%2BClaude/33018/#comments)

Click HERE to learn more about classes Brad is teaching for SANS

* [previous](/diary/33016)

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