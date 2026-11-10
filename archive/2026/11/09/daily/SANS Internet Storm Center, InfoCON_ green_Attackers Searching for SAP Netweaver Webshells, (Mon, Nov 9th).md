---
title: Attackers Searching for SAP Netweaver Webshells, (Mon, Nov 9th)
url: https://isc.sans.edu/diary/rss/33502
source: SANS Internet Storm Center, InfoCON: green
date: 2026-11-09
fetch_date: 2026-11-10T09:03:18.452607
---

# Attackers Searching for SAP Netweaver Webshells, (Mon, Nov 9th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/33498)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Attackers Searching for SAP Netweaver Webshells](/forums/diary/Attackers%2BSearching%2Bfor%2BSAP%2BNetweaver%2BWebshells/33502/)

**Published**: 2026-11-09. **Last Updated**: 2026-11-09 18:18:15 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[1 comment(s)](/diary/Attackers%2BSearching%2Bfor%2BSAP%2BNetweaver%2BWebshells/33502/#comments)

Just saw a new (to me) URL in our honeypot data today:

/irj/servlet\_jsp/irj/root/ant.jsp

This request is part of a larger campaign to exploit SAP NetWeaver or to find already installed webshells.

The exploited vulnerability is "old": CVE-2025-31324. A perfect 10 CVSS score and the simple ability to upload files without authentication. Attackers have been using this vulnerability to upload webshells. Usually, these webshells end up in /irj/servlet\_jsp/irj/root/.

One particular attacker, 82.26.72.21, is hitting the following URLs. Not all of these URLs are SAP NetWeaver-related. Also, check the odd misspelling of "upload.aspx" at the end.

| URL Path |
| --- |
| / |
| /\_layouts/15/start.aspx |
| /\_layouts/15/ToolPane.aspx?DisplayMode=Edit&a=/ToolPane.aspx |
| /amp/upload |
| /ant.aspx |
| /ant.jsp |
| /ant.jsp/ |
| /ant.php |
| /api/upload |
| /api/v1/upload |
| /authenticationendpoint/ant.jsp |
| /commandcenter/ant.jsp |
| /commandcenter/deployWebpackage.do |
| /developmentserver/metadatauploader?CONTENTTYPE=MODEL&CLIENT=1 |
| /en-US/static/app/search/ant.php |
| /fileupload/toolsAny |
| /hosted/amp/upload |
| /images/ant.php |
| /images/pagebuilder/ant.php |
| /index.action |
| /index.php?option=com\_baforms&task=uploader.upload |
| /index.php?option=com\_gridbox&task=uploader.upload |
| /index.php?option=com\_jce&task=plugin.display&plugin=browser |
| /index.php?option=com\_sppagebuilder&task=media.directUpload |
| /irj/servlet\_jsp/irj/root/ant.jsp |
| /m/webadmin/upload |
| /MagicInfo/ant.jsp |
| /MagicInfo/servlet/SWUpdateFileUploader |
| /NmConsole/ant.aspx |
| /NmConsole/Wug/Report/ExportReport |
| /Synchronization |
| /te/upload |
| /upload.apsx |
| /upload.aspx |

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [sap netweaver](/tag.html?tag=sap netweaver)

[1 comment(s)](/diary/Attackers%2BSearching%2Bfor%2BSAP%2BNetweaver%2BWebshells/33502/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/33498)

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