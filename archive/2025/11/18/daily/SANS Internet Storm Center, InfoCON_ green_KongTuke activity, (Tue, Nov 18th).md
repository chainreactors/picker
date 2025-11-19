---
title: KongTuke activity, (Tue, Nov 18th)
url: https://isc.sans.edu/diary/rss/32498
source: SANS Internet Storm Center, InfoCON: green
date: 2025-11-18
fetch_date: 2025-11-19T03:14:58.744286
---

# KongTuke activity, (Tue, Nov 18th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Brad Duncan](/handler_list.html#brad-duncan "Brad Duncan")

Threat Level: [green](/infocon.html)

* [previous](/diary/32492)

# [KongTuke activity](/forums/diary/KongTuke%2Bactivity/32498/)

**Published**: 2025-11-18. **Last Updated**: 2025-11-18 07:10:17 UTC
**by** [Brad Duncan](/handler_list.html#brad-duncan) (Version: 1)

[0 comment(s)](/diary/KongTuke%2Bactivity/32498/#comments)

***Introduction***

Today's diary is an example of KongTuke activity using fake CAPTCHA pages for a [ClickFix](https://www.microsoft.com/en-us/security/blog/2025/08/21/think-before-you-clickfix-analyzing-the-clickfix-social-engineering-technique/)-style lure.

Also known as LandUpdate808 or TAG-124 and described as [a sophisticated TDS system](https://malpedia.caad.fkie.fraunhofer.de/details/js.kongtuke), KongTuke has been active since at least May 2024.  I keep track of this campaign through the [infosec.exchange](https://infosec.exchange/tags/Kongtuke) Mastodon instance, which is mostly information from the [@monitorsg](https://infosec.exchange/%40monitorsg) profile.

With [URLscan](https://urlscan.io/search/#*), I can pivot on the information from Mastodon to find compromised sites and generate infection traffic in my lab.

On Monday, 2025-11-17, I found an example of a legitimate website with a KongTuke-injected script, and I generated some infection traffic.

***Details***

The image below shows an example of the fake CAPTCHA page and ClickFix style instructions.

[![](https://isc.sans.edu/diaryimages/images/2025-11-18-ISC-diary-image-01.png)](https://isc.sans.edu/diaryimages/images/2025-11-18-ISC-diary-image-01.png)
*Shown above: Fake CAPTCHA page from a legitimate site with KongTuke-injected script, with the ClickFix style instructions and malicious command.*

The CAPTCHA page hijacks the clipboard, injecting text for a malicious command to download and run PowerShell script. Potential victims would read the instructions and paste this command into Run window.

I tried this on a vulnerable Windows client in an Active Directory (AD) environment, and it ran PowerShell script that retrieved a zip archive containing a malicious Python script, as well as the Windows Python environment to run it.

The malicious Python script generated HTTPS traffic to telegra[.]ph, but I was unable to determine the URL or content of the traffic.

[![](https://isc.sans.edu/diaryimages/images/2025-11-18-ISC-diary-image-02.png)](https://isc.sans.edu/diaryimages/images/2025-11-18-ISC-diary-image-02.png)
*Shown above: Traffic from the infection, filtered in Wireshark.*

[![](https://isc.sans.edu/diaryimages/images/2025-11-18-ISC-diary-image-03.png)](https://isc.sans.edu/diaryimages/images/2025-11-18-ISC-diary-image-03.png)
*Shown above: Initial PowerShell script retrieved by the ClickFix command that was pasted into the Run window.*

[![](https://isc.sans.edu/diaryimages/images/2025-11-18-ISC-diary-image-04.png)](https://isc.sans.edu/diaryimages/images/2025-11-18-ISC-diary-image-04.png)
*Shown above: Final HTTP request from the initial infection traffic returned a zip archive containing a Python environment and a malicious Python script.*

***Post-Infection Forensics***

The malicious Python package was saved to the Windows client under the user account's AppData\Roaming directory under a folder named DATA. A scheduled task kept the infection persistent.

[![](https://isc.sans.edu/diaryimages/images/2025-11-18-ISC-diary-image-05.png)](https://isc.sans.edu/diaryimages/images/2025-11-18-ISC-diary-image-05.png)
*Shown above: The malicious Python script, made persistent on the infected Windows client through a scheduled task.*

***Indicators from the infection***

The following URLs were generated during the initial infection traffic:

* hxxp[:]//64.111.92[.]212:6655/ab
* hxxp[:]//64.111.92[.]212:6655/se
* hxxp[:]//64.111.92[.]212:6655/node
* hxxp[:]//64.111.92[.]212:6655/nada000

For post-infection traffic, telegra[.]ph is a publishing tool that allows people to create and share simple web pages. I don't know the specific URL used for this infection, and the domain itself is not malicious.

The following is the zip archive containing the Windows Python environment and the malicious Python script.

* SHA256 hash: [b2e084a9cab46b01cfa8725c3cc23ef5cc2a4e399d83ff760e4bdb8b028ec6f6](https://bazaar.abuse.ch/sample/b2e084a9cab46b01cfa8725c3cc23ef5cc2a4e399d83ff760e4bdb8b028ec6f6/)
* File size: 24,946,416 bytes
* File type: Zip archive data, at least v2.0 to extract, compression method=deflate
* File location: hxxp[:]//64.111.92[.]212:6655/nada000

***Final Words***

I'm not sure what the script from this malicious Python package actually does.  If anyone knows what this is, feel free to leave a comment.

---
Bradley Duncan
brad [at] malware-traffic-analysis.net

Keywords: [Python](/tag.html?tag=Python) [ClickFix](/tag.html?tag=ClickFix) [KongTuke](/tag.html?tag=KongTuke) [Malware](/tag.html?tag=Malware)

[0 comment(s)](/diary/KongTuke%2Bactivity/32498/#comments)

* [previous](/diary/32492)

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