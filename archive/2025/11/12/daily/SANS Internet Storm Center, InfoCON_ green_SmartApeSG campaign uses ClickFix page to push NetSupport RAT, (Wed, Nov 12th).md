---
title: SmartApeSG campaign uses ClickFix page to push NetSupport RAT, (Wed, Nov 12th)
url: https://isc.sans.edu/diary/rss/32474
source: SANS Internet Storm Center, InfoCON: green
date: 2025-11-12
fetch_date: 2025-11-13T03:16:02.900312
---

# SmartApeSG campaign uses ClickFix page to push NetSupport RAT, (Wed, Nov 12th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32468)

# [SmartApeSG campaign uses ClickFix page to push NetSupport RAT](/forums/diary/SmartApeSG%2Bcampaign%2Buses%2BClickFix%2Bpage%2Bto%2Bpush%2BNetSupport%2BRAT/32474/)

**Published**: 2025-11-12. **Last Updated**: 2025-11-12 21:49:32 UTC
**by** [Brad Duncan](/handler_list.html#brad-duncan) (Version: 1)

[0 comment(s)](/diary/SmartApeSG%2Bcampaign%2Buses%2BClickFix%2Bpage%2Bto%2Bpush%2BNetSupport%2BRAT/32474/#comments)

***Introduction***

This diary describes a NetSupport RAT infection I generated in my lab from the SmartApeSG campaign that used a ClickFix-style fake CAPTCHA page.

Known as ZPHP or HANEYMANEY, SmartApeSG is a campaign [reported as early as June 2024](https://www.threatdown.com/blog/smartapesg-06-11-2024/). When it started, this campaign used fake browser update pages. But it currently uses the [ClickFix method](https://unit42.paloaltonetworks.com/preventing-clickfix-attack-vector/) of fake CAPTCHA-style "verify you are human" pages.

This campaign pushes malicious [NetSupport RAT](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Trojan:Win32/NetSupportRat!MTB&ocid=magicti_blog_ency) packages for its initial malware infection, and I've [seen follow-up malware](https://www.malware-traffic-analysis.net/2025/08/20/index.html) from these NetSupport RAT infections.

***How To Find SmartApeSG Activity***

I can usually find SmartApeSG indicators from the [Monitor SG account](https://infosec.exchange/%40monitorsg) on Mastodon. I use [URLscan](https://urlscan.io/search/#*) to pivot on those indicators, so I can find compromised websites that lead to the SmartApeSG script.

***The Infection***

Sites compromised through this campaign display pages with a hidden injected script. Given the right conditions, this script kicks off a SmartApeSG chain of events. The image below shows an example.

[![](https://isc.sans.edu/diaryimages/images/2025-11-12-ISC-diary-image-01.png)](https://isc.sans.edu/diaryimages/images/2025-11-12-ISC-diary-image-01.png)
*Shown above: Injected SmartApeSG script in a page from the compromised site.*

In some cases, this injected script does not kick off the infection chain. I've had issues getting an infection chain during certain times of day, or if I try viewing the compromised website multiple times from the same source IP address. I don't know what the conditions are, but if those conditions are right, the compromised site shows a fake CAPTCHA-style "verify you are human" page.

[![](https://isc.sans.edu/diaryimages/images/2025-11-12-ISC-diary-image-02.png)](https://isc.sans.edu/diaryimages/images/2025-11-12-ISC-diary-image-02.png)
*Shown above: Fake CAPTCHA page displayed by the compromised site.*

Clicking the "verify you are human" box does the following:

* Injects malicious content into the Windows host's clipboard
* Generates a pop-up with instructions to open a Run window, paste content into the window, and run it.

The clipboard-injected content is a command string that uses the mshta command to retrieve and run malicious content that will generate a NetSupport RAT infection.

[![](https://isc.sans.edu/diaryimages/images/2025-11-12-ISC-diary-image-03.png)](https://isc.sans.edu/diaryimages/images/2025-11-12-ISC-diary-image-03.png)
*Shown above: Following ClickFix directions to paste content (a malicious command) into the Run window.*

Below is a URL list of the HTTPS traffic directly involved in this infection.

[![](https://isc.sans.edu/diaryimages/images/2025-11-12-ISC-diary-image-04.png)](https://isc.sans.edu/diaryimages/images/2025-11-12-ISC-diary-image-04.png)
*Shown above: HTTPS traffic directly involved in this SmartApe SG activity.*

[![](https://isc.sans.edu/diaryimages/images/2025-11-12-ISC-diary-image-05.png)](https://isc.sans.edu/diaryimages/images/2025-11-12-ISC-diary-image-05.png)
*Shown above: Traffic from the infection filtered in Wireshark.*

The malicious NetSupport RAT package stays persistent on the infected host through a Start Menu shortcut. The shortcut runs a .js file in the user's AppData\Local\Temp directory. That .js file runs the NetSupport RAT executable located in a folder under the C:\ProgramData\ directory.

[![](https://isc.sans.edu/diaryimages/images/2025-11-12-ISC-diary-image-06.png)](https://isc.sans.edu/diaryimages/images/2025-11-12-ISC-diary-image-06.png)
*Shown above: The malicious NetSupport RAT package, persistent on an infected Windows host.*

***Indicators From This Activity***

The following URLs were noted in traffic from this infection:

* hxxps[:]//frostshiledr[.]com/xss/buf.js  <-- injected SmartApeSG script
* hxxps[:]//frostshiledr[.]com/xss/index.php?iArfLYKw
* hxxps[:]//frostshiledr[.]com/xss/bof.js?0e58069bbdd36e9a36  <-- fake CAPCHA page/ClickFix instructions
* hxxps[:]//newstarmold[.]com/sibhl.php  <-- Script retrieved by ClickFix command
* hxxps[:]//www.iconconsultants[.]com/4nnjson.zip  <-- zip archive containing malicious NetSupport RAT package
* hxxp[:]//194.180.191[.]121/fakeurl.htm  <-- NetSupport RAT C2 traffic over TCP port 443

The following is the zip archive containing the malicious NetSupport RAT package:

* SHA256 hash: 1e9a1be5611927c22a8c934f0fdd716811e0c93256b4ee784fadd9daaf2459a1
* File size: 9,192,105 bytes
* File type: Zip archive data, at least v1.0 to extract, compression method=store
* File location: hxxps[:]//www.iconconsultants[.]com/4nnjson.zip
* Saved to disk as: C:\ProgramData\psrookk11nn.zip

Note: These domains change on a near-daily basis, and the NetSupport RAT package and C2 server also frequently change.

---
Bradley Duncan
brad [at] malware-traffic-analysis.net

Keywords: [ClickFix](/tag.html?tag=ClickFix) [NetSupportRAT](/tag.html?tag=NetSupportRAT) [SmartApeSG](/tag.html?tag=SmartApeSG)

[0 comment(s)](/diary/SmartApeSG%2Bcampaign%2Buses%2BClickFix%2Bpage%2Bto%2Bpush%2BNetSupport%2BRAT/32474/#comments)

* [previous](/diary/32468)

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