---
title: Yet Another ClickFix Campaign, (Wed, Oct 28th)
url: https://isc.sans.edu/diary/rss/33466
source: SANS Internet Storm Center, InfoCON: green
date: 2026-10-29
fetch_date: 2026-10-30T07:56:21.452665
---

# Yet Another ClickFix Campaign, (Wed, Oct 28th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33458)
* [next](/diary/33470)

Click HERE to learn more about classes Brad is teaching for SANS

# [Yet Another ClickFix Campaign](/forums/diary/Yet%2BAnother%2BClickFix%2BCampaign/33466/)

**Published**: 2026-10-28. **Last Updated**: 2026-10-29 00:42:15 UTC
**by** [Brad Duncan](/handler_list.html#brad-duncan) (Version: 1)

[1 comment(s)](/diary/Yet%2BAnother%2BClickFix%2BCampaign/33466/#comments)

***Introduction***

On Wednesday, 2026-10-28, I ran across a ClickFix campaign I haven't seen before. Like several other ClickFix campaigns, this one uses a fake Cloudflare verification page. It targets both macOS and Windows.

I don't yet have a name for this specific activity, but this diary shares some screenshots and indicators.

Unfortunately, I was unable to get the macOS or Windows malware distributed through this particular ClickFix campaign.

***Screenshots of the Activity***

[![](https://isc.sans.edu/diaryimages/images/2026-10-28a-ISC-diary-image-01.png)](https://isc.sans.edu/diaryimages/images/2026-10-28a-ISC-diary-image-01a.png)
*Shown above: Fake verification page with ClickFix instructions when viewed on a Windows host.*

When I ran the command on a Windows host, the server hosting the malware responded with a 403 Forbidden error, and I was unable to proceed any further.

[![](https://isc.sans.edu/diaryimages/images/2026-10-28a-ISC-diary-image-02.png)](https://isc.sans.edu/diaryimages/images/2026-10-28a-ISC-diary-image-02a.png)
*Shown above: Fake verification page with ClickFix instructions when viewed on a macOS host.*

When I ran the ClickFix command on a macOS host, the domain for the server hosting the malware did not resolve, and I was unable to proceed any further.

[![](https://isc.sans.edu/diaryimages/images/2026-10-28a-ISC-diary-image-03c.png)](https://isc.sans.edu/diaryimages/images/2026-10-28a-ISC-diary-image-03d.png)
*Shown above: The domain in the ClickFix command for macOS didn't resolve.*

***Indicators From the Activity on Wednesday, 2026-10-28***

The following is the chain of URLs that I saw from the domain hosting the fake verification page, js-static[.]cfd:

* hxxps[:]//js-static[.]cfd/embed.js?v=24
* hxxps[:]//js-static[.]cfd/api/s/on?site=[information removed].com
* hxxps[:]//js-static[.]cfd/api/s/hit
* hxxps[:]//js-static[.]cfd/api/s/hit
* hxxps[:]//js-static[.]cfd/api/track/event
* hxxps[:]//js-static[.]cfd/api/s/tz
* hxxps[:]//js-static[.]cfd/api/track/event
* hxxps[:]//js-static[.]cfd/embed?site=[information removed].com&
  parent=https%3A%2F%2F[information removed].com&
  path=%2F&
  page\_path=%2F&
  page\_url=https%3A%2F%2F[information removed].com%2F&
  q=&
  lang=en&
  visit\_id=410c7df1-ae6e-43a9-897f-541144bf0b7d
* hxxps[:]//js-static[.]cfd/api/track/event
* hxxps[:]//js-static[.]cfd/static/CF-Logo%201.png
* hxxps[:]//js-static[.]cfd/static/fonts/jetbrains-mono-600.woff2
* hxxps[:]//js-static[.]cfd/static/cf\_dark\_horizontal.png
* hxxps[:]//js-static[.]cfd/c.js?embed=\_\_JNJ\_4\_\_&
  lp=%2F&
  pu=https%3A%2F%2F[information removed].com%2F&
  site=[information removed].com&
  parent=https%3A%2F%2F[information removed].com&
  path=%2F&
  page\_path=%2F&
  q=&
  redirect=
* hxxps[:]//js-static[.]cfd/api/s/geo
* hxxps[:]//js-static[.]cfd/api/s/boot
* hxxps[:]//js-static[.]cfd/api/track/event
* hxxps[:]//js-static[.]cfd/api/s/ip
* hxxps[:]//js-static[.]cfd/api/track/event
* hxxps[:]//js-static[.]cfd/api/s/wait
* hxxps[:]//js-static[.]cfd/api/s/st
* hxxps[:]//js-static[.]cfd/api/s/hit
* hxxps[:]//js-static[.]cfd/api/s/ip
* hxxps[:]//js-static[.]cfd/api/s/hit
* hxxps[:]//js-static[.]cfd/api/s/wait
* hxxps[:]//js-static[.]cfd/api/s/hit
* hxxps[:]//js-static[.]cfd/api/track/event
* hxxps[:]//js-static[.]cfd/api/s/hit
* hxxps[:]//js-static[.]cfd/api/s/hit
* hxxps[:]//js-static[.]cfd/api/s/hit
* hxxps[:]//js-static[.]cfd/api/s/hit
* hxxps[:]//js-static[.]cfd/api/s/hit
* hxxps[:]//js-static[.]cfd/api/s/hit

URL from the ClickFix text seen on a macOS host (domain did not resolve on 2026-10-28):

* hxxps[:]//cf-id[.]com/?ray-id=nz0ovm2jq2g68i

URL from the ClickFix text seen on a Windows host (Returned 403 Forbidden response on 2026-10-28):

* hxxps[:]//api-com[.]cfd/7ge0w58tzzjsv9

***Final Words***

For the diary, I removed information on the legitimate but compromised web site that generated the ClickFix activity. However, we can pivot on js-static[.]cfd in URLscan to find [several sites that will likely generate this traffic](https://urlscan.io/search/#js-static.cfd).

--
Bradley Duncan
brad [at] malware-traffic-analysis.net

Keywords: [ClickFix](/tag.html?tag=ClickFix) [macOS](/tag.html?tag=macOS) [Windows](/tag.html?tag=Windows)

[1 comment(s)](/diary/Yet%2BAnother%2BClickFix%2BCampaign/33466/#comments)

Click HERE to learn more about classes Brad is teaching for SANS

* [previous](/diary/33458)
* [next](/diary/33470)

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