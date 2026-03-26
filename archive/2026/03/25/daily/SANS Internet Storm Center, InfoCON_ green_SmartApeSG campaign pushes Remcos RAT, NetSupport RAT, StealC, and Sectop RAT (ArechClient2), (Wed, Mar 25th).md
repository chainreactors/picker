---
title: SmartApeSG campaign pushes Remcos RAT, NetSupport RAT, StealC, and Sectop RAT (ArechClient2), (Wed, Mar 25th)
url: https://isc.sans.edu/diary/rss/32826
source: SANS Internet Storm Center, InfoCON: green
date: 2026-03-25
fetch_date: 2026-03-26T04:32:03.225520
---

# SmartApeSG campaign pushes Remcos RAT, NetSupport RAT, StealC, and Sectop RAT (ArechClient2), (Wed, Mar 25th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Brad Duncan](/handler_list.html#brad-duncan "Brad Duncan")

Threat Level: [green](/infocon.html)

* [previous](/diary/32824)
* [next](/diary/32830)

# [SmartApeSG campaign pushes Remcos RAT, NetSupport RAT, StealC, and Sectop RAT (ArechClient2)](/forums/diary/SmartApeSG%2Bcampaign%2Bpushes%2BRemcos%2BRAT%2BNetSupport%2BRAT%2BStealC%2Band%2BSectop%2BRAT%2BArechClient2/32826/)

**Published**: 2026-03-25. **Last Updated**: 2026-03-25 17:44:25 UTC
**by** [Brad Duncan](/handler_list.html#brad-duncan) (Version: 1)

[0 comment(s)](/diary/SmartApeSG%2Bcampaign%2Bpushes%2BRemcos%2BRAT%2BNetSupport%2BRAT%2BStealC%2Band%2BSectop%2BRAT%2BArechClient2/32826/#comments)

***Introduction***

This diary provides indicators from the SmartApeSG (ZPHP, HANEYMANEY) campaign I saw on Tuesday, 2026-03-24. SmartApeSG is one of many campaigns that use the [ClickFix](https://unit42.paloaltonetworks.com/preventing-clickfix-attack-vector/) technique. This past week, I've seen NetSupport RAT as follow-up malware from Remcos RAT pushed by this campaign. But this time, I also saw indicators for StealC malware and Sectop RAT (ArecheClient2) after NetSupport RAT appeared on my infected lab host.

Not all of the follow-up malware appears shortly after the initial Remcos RAT malware. Here's the timeline for malware from my SmartApeSG activity on Tuesday 2026-03-24:

* 17:11 UTC - Ran ClickFix script from SmartApeSG fake CAPTCHA page
* 17:12 UTC - Remcos RAT post-infection traffic starts
* 17:16 UTC - NetSupport RAT post-infection traffic starts
* 18:18 UTC - StealC post-infection traffic starts
* 19:36 UTC - Sectop RAT post-infection traffic starts

While the NetSupport RAT activity happened approximately 4 minutes after the Remcos RAT activity, the StealC traffic didn't happen until approximately 1 hour after the NetSupport RAT activity started. And the traffic for Sectop RAT happened approximately 1 hour and 18 minutes after the StealC activity started.

***Images from the infection***

[![](https://isc.sans.edu/diaryimages/images/2026-03-25-ISC-diary-image-01a.png)](https://isc.sans.edu/diaryimages/images/2026-03-25-ISC-diary-image-01.png)
*Shown above: Page from a legitimate but compromised website with injected script for the fake CAPTCHA page.*

[![](https://isc.sans.edu/diaryimages/images/2026-03-25-ISC-diary-image-02a.png)](https://isc.sans.edu/diaryimages/images/2026-03-25-ISC-diary-image-02.png)
*Shown above: Fake CAPTCHA page with ClickFix instructions. This image shows the malicious script injected into a user's clipboard.*

[![](https://isc.sans.edu/diaryimages/images/2026-03-25-ISC-diary-image-03d.png)](https://isc.sans.edu/diaryimages/images/2026-03-25-ISC-diary-image-03c.png)
*Shown above: Traffic from the infection filtered in Wireshark.*

***Indicators of Compromise***

Associated domains and IP addresses:

* fresicrto[.]top - Domain for server hosting fake CAPTCHA page
* urotypos[.]com - Called by ClickFix instructions, this domain is for a server hosting the initial malware
* 95.142.45[.]231:443 - Remcos RAT C2 server
* 185.163.47[.]220:443 - NetSupport RAT C2 server
* 89.46.38[.]100:80 - StealC C2 server
* 195.85.115[.]11:9000 - Sectop RAT (ArechClient2) C2 server

Example of HTA file retrieved by ClickFix script:

* SHA256 hash: [212d8007a7ce374d38949cf54d80133bd69338131670282008940f1995d7a720](https://bazaar.abuse.ch/sample/212d8007a7ce374d38949cf54d80133bd69338131670282008940f1995d7a720/)
* File size: 47,714 bytes
* File type: HTML document text, ASCII text, with very long lines (6272)
* Retrieved from: hxxps[:]//urotypos[.]com/cd/temp
* Saved location: C:\Users\[username]\AppData\Local\post.hta
* Note: ClickFix script deletes the file after retrieving and running it

Example of ZIP archive for Remcos RAT retrieved by the above HTA file:

* SHA256 hash: [a6a748c0606fb9600fdf04763523b7da20b382b054b875fdd1ef1c36fc16079a](https://bazaar.abuse.ch/sample/a6a748c0606fb9600fdf04763523b7da20b382b054b875fdd1ef1c36fc16079a)
* File size: 85,328,653 bytes
* File type: Zip archive data, at least v2.0 to extract, compression method=deflate
* Retrieved from: hxxps[:]//urotypos[.]com/ls/production
* Saved location: C:\Users\[username]\AppData\Local\361118191\361118191.pdf

ZIP archive containing NetSupport RAT package:

* SHA256 hash: [6e26ff49387088178319e116700b123d27216d98ba3ae1ce492544cb9acd38f0](https://bazaar.abuse.ch/sample/6e26ff49387088178319e116700b123d27216d98ba3ae1ce492544cb9acd38f0/)
* File size: 9,171,647 bytes
* File type: Zip archive data, at least v2.0 to extract, compression method=deflate
* File name: UpdateInstaller.zip
* Note: I created this zip archive from the extracted files under C:\ProgramData\UpdateInstaller\

RAR archive for StealC package:

* SHA256 hash: [a7b9be1211c6de76bab31dbcd3a1c99861cf18e3230ea9f634e07d22c179d1ca](https://bazaar.abuse.ch/sample/a7b9be1211c6de76bab31dbcd3a1c99861cf18e3230ea9f634e07d22c179d1ca/)
* File size: 6,178,471 bytes
* File type: RAR archive data, v5
* Saved location: C:\Users\Public\Music\finalmesh.zip

RAR archive for Sectop RAT (ArechClient2) package:

* SHA256 hash: [c90435370728d48cba1c00d92cc3bf99e85f01aa52ecd6c6df2e8137db964796](https://bazaar.abuse.ch/sample/c90435370728d48cba1c00d92cc3bf99e85f01aa52ecd6c6df2e8137db964796/)
* File size: 6,908,049 bytes
* File type: RAR archive data, v5
* Saved location: C:\ProgramData\drag2pdf.zip

***Final words***

The archive files for Remcos RAT, StealC and Sectop RAT are packages that use legitimate EXE files to side-load malicious DLLs (a technique called DLL side-loading). The NetSupport RAT package is a legitimate tool that's configured to use an attacker-controlled server.

As always, the files, URLs and domains for SmartApeSG activity change on a near-daily basis. And names of the HTA file and ZIP archive for Remcos RAT are different for each infection. The indicators described in this article may no longer be current as you read this. However, this activity confirms that the SmartApeSG campaign can push a variety of malware after an initial infection.

---
Bradley Duncan
brad [at] malware-traffic-analysis.net

Keywords: [ArechClient2](/tag.html?tag=ArechClient2) [CAPTCHA](/tag.html?tag=CAPTCHA) [ClickFix](/tag.html?tag=ClickFix) [NetSupportRAT](/tag.html?tag=NetSupportRAT) [RAT](/tag.html?tag=RAT) [Remcos](/tag.html?tag=Remcos) [RemcosRAT](/tag.html?tag=RemcosRAT) [SecTopRAT](/tag.html?tag=SecTopRAT) [SmartApeSG](/tag.html?tag=SmartApeSG) [StealC](/tag.html?tag=StealC)

[0 comment(s)](/diary/SmartApeSG%2Bcampaign%2Bpushes%2BRemcos%2BRAT%2BNetSupport%2BRAT%2BStealC%2Band%2BSectop%2BRAT%2BArechClient2/32826/#comments)

* [previous](/diary/32824)
* [next](/diary/32830)

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

[Bluesky](htt...