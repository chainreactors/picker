---
title: Macfinger ClickFix campaign, (Tue, Sep 22nd)
url: https://isc.sans.edu/diary/rss/33360
source: SANS Internet Storm Center, InfoCON: green
date: 2026-09-23
fetch_date: 2026-09-24T07:08:12.742635
---

# Macfinger ClickFix campaign, (Tue, Sep 22nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33358)
* [next](/diary/33366)

Click HERE to learn more about classes Brad is teaching for SANS

# [Macfinger ClickFix campaign](/forums/diary/Macfinger%2BClickFix%2Bcampaign/33360/)

**Published**: 2026-09-22. **Last Updated**: 2026-09-23 16:14:37 UTC
**by** [Brad Duncan](/handler_list.html#brad-duncan) (Version: 1)

[0 comment(s)](/diary/Macfinger%2BClickFix%2Bcampaign/33360/#comments)

***Introduction***

I've found several legitimate websites with injected script for a campaign using the [ClickFix social engineering technique](https://www.microsoft.com/en-us/security/blog/2025/08/21/think-before-you-clickfix-analyzing-the-clickfix-social-engineering-technique/). This particular ClickFix campaign [was documented earlier this month](https://ransom-isac.org/blog/macos-clickfix-amos-campaign/) on the Ransom-ISAC Blog, but it doesn't appear to have a nickname yet. Since this campaign is targeting macOS environments through a fingerprinting process, I'm calling it the "Macfinger ClickFix" campaign. No, this is not related to the MacFinger utility from decades ago. Instead, think of the movie [Goldfinger](https://en.wikipedia.org/wiki/Goldfinger_%28film%29), but with macOS malware and the internet instead of James Bond and Miss Galore.

[![](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-01.png)](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-01.png)
*Shown above: An image I created to represent the Macfinger ClickFix campaign.*

Today's diary presents indicators from the Macfinger ClickFix campaign that I saw on Tuesday, 2026-09-22.

***Images From the Infection***

[![](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-02a.png)](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-02.png)
*Shown above: First part of the Macfinger injected script in a page from a legitimate website.*

[![](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-03a.png)](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-03.png)
*Shown above: Second part of the Macfinger injected script in a page from a legitimate website.*

[![](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-04a.png)](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-04.png)
*Shown above: Fake bot protection page caused by the injected Macfinger script.*

[![](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-05a.png)](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-05.png)
*Shown above: ClickFix instructions from fake verification pop-up caused by the injected Macfinger script.*

While displaying the fake bot protection page with the verification instructions, the Macfinger domain receives frequent POST requests from the victim host. These report information on the user and track the user actions. Here's an example of a POST request through HTTPS traffic after the user has clicked on the page. In this case, the user abandoned the page without following the instructions.

[![](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-06a.png)](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-06.png)
*Shown above: POST request over HTTPS to the Macfinger domain reporting the user information.*

I had tested one of the Macfinger-infected sites on Monday, 2026-09-21 which had the same post-infection traffic that I saw the next day on Tuesday, 2026-09-22. The image below shows an example of the infection traffic, with the malware files retrieved from 45.150.33[.]128 and the post-infection C2 traffic on 95.163.153[.]80 over TCP port 8133.

[![](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-07b.png)](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-07.png)
*Shown above: Traffic from an infection filtered in Wireshark.*

***Indicators of Compromise***

The following are indicators from Tuesday, 2026-09-22.

Traffic to the Macfinger domain:

* hxxps[:]//velvet-otter-glagceis[.]life/t.js?site=4f0529f47320472732961318d7d0dfd1
* hxxps[:]//velvet-otter-glagceis[.]life/t.4b1009ff6c3f.js
* hxxps[:]//velvet-otter-glagceis[.]life/ext-b.4f9db6afd06a.js
* hxxps[:]//velvet-otter-glagceis[.]life/collect
* hxxps[:]//velvet-otter-glagceis[.]life/collect
* hxxps[:]//velvet-otter-glagceis[.]life/collect
* hxxps[:]//velvet-otter-glagceis[.]life/collect
* hxxps[:]//velvet-otter-glagceis[.]life/collect
* hxxps[:]//velvet-otter-glagceis[.]life/collect
* hxxps[:]//velvet-otter-glagceis[.]life/collect
* hxxps[:]//velvet-otter-glagceis[.]life/collect

ClickFix text from the Macfinger domain, saved to a text file:

SHA-256 hash: [6606a5f18184b224a56c9cb658fa26f7fce45099da548a30a8db2c5f2c70377c](https://www.virustotal.com/gui/file/6606a5f18184b224a56c9cb658fa26f7fce45099da548a30a8db2c5f2c70377c/)

* File size: 581 bytes

Initial download:

SHA-256 hash: [9d87b41c2b29ccbeac851b98f1a7dce4ab4781fec0cbc55fa6f93a6299a3d564](https://www.virustotal.com/gui/file/9d87b41c2b29ccbeac851b98f1a7dce4ab4781fec0cbc55fa6f93a6299a3d564/)

* File size: 4,674 bytes
* File type: Bourne-Again shell script text executable, ASCII text, with very long lines
* File location: hxxp[:]//45.150.33[.]128/92961f75b259df2?force=1

Follow-up malware from the above shell script:

SHA-256 hash: [b68cdb1b46502fbce67ce3f8110682936d06afd2116af096e30abd4c8376b6dc](https://www.virustotal.com/gui/file/b68cdb1b46502fbce67ce3f8110682936d06afd2116af096e30abd4c8376b6dc)

* File size: 33,285,040 bytes
* File type: Mach-O 64-bit executable arm64
* File location: hxxp[:]//45.150.33[.]128/d4c8083a7d97?force=1

SHA-256 hash: [1a3765e8cb0055ec31693b8f82ce9744106dee08368259661600b072c6805af4](https://www.virustotal.com/gui/file/1a3765e8cb0055ec31693b8f82ce9744106dee08368259661600b072c6805af4)

* File size: 34,118,904 bytes
* File type: Mach-O 64-bit executable x86\_64
* File location: hxxp[:]//45.150.33[.]128/2286de55f9afd?force=1

Post-infection Traffic:

* 2026-09-21 23:12:58 UTC - hxxp[:]//45.150.33[.]128 - GET /92961f75b259df2?force=1
* 2026-09-21 23:12:59 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:12:59 UTC - hxxp[:]//45.150.33[.]128 - GET /d4c8083a7d97?force=1
* 2026-09-21 23:13:04 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:05 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:05 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:08 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:08 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:11 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:14 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:15 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:20 UTC - ipinfo[.]io - HTTPS traffic
* 2026-09-21 23:13:21 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:21 UTC - hxxp[:]//95.163.153[.]80:8133 - GET /api/shell/agent
* 2026-09-21 23:13:21 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:21 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/credentials
* 2026-09-21 23:13:22 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/credentials
* 2026-09-21 23:13:22 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/credentials
* 2026-09-21 23:13:23 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:23 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/credentials
* 2026-09-21 23:13:23 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/credentials
* 2026-09-21 23:13:24 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/credentials
* 2026-09-21 23:13:26 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/credentials
* 2026-09-21 23:13:30 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api...