---
title: Recent DShield SIEM Update, (Tue, Jul 14th)
url: https://isc.sans.edu/diary/rss/33156
source: SANS Internet Storm Center, InfoCON: green
date: 2026-07-15
fetch_date: 2026-07-16T04:58:56.626977
---

# Recent DShield SIEM Update, (Tue, Jul 14th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Manuel Humberto Santander Pelaez](/handler_list.html#manuel-humberto-santander-pelaez "Manuel Humberto Santander Pelaez")

Threat Level: [green](/infocon.html)

* [previous](/diary/33154)

Click HERE to learn more about classes Guy is teaching for SANS

# [Recent DShield SIEM Update](/forums/diary/Recent%2BDShield%2BSIEM%2BUpdate/33156/)

**Published**: 2026-07-14. **Last Updated**: 2026-07-15 01:38:43 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/Recent%2BDShield%2BSIEM%2BUpdate/33156/#comments)

The last update to the DShield SIEM [[4](https://isc.sans.edu/diary/DShield%2BSIEM%2BDocker%2BUpdates/32276)] was in Sep 2025 which contained some minor tweaks. This update currently is using ELK stack version 8.19.15, contains some additional dashboards and new logs.

The following have been added to the [DShield SIEM](https://github.com/bruneaug/DShield-SIEM/tree/main) to provide additional information about what the DShield sensor [[1](https://isc.sans.edu/honeypot.html)] is receiving. These 2-addition installed in the DShield sensor provide direct collection of TTY logs [[2](https://github.com/bruneaug/DShield-SIEM/blob/main/AddOn/TTYLogs_To_DShield-SIEM.md)] and Suricata [[3](https://github.com/bruneaug/DShield-SIEM/blob/main/AddOn/Configure_Suricata.md)] which are now reported to the DShield SIEM. The TTY logs are parsed and uploaded daily at 23:58Z which can be reviewed in the DShield - Traffic Analysis tab to match the TTY Log Hashes and shows which actor ran any series of commands while logged in the sensor.

The TTY logs are base64 encoded before they are sent to the SIEM and decoded by Kibana upon review. TTY logs in base64 format:

transaction.id: 021d88f11b09defc8756e1bd6eabaea8113b3fbf917c9bd4fef4f546a1c9512a
event.hash: ZWNobyAtZSAieCFcbjBPc0NsT21WU0JGOVxuME9zQ2xPbVZTQkY5InxwYXNzd2R8YmFzaC1iYXNoOiBFbnRlcjogY29tbWFuZCBub3QgZm91bmQK
transaction.id: 02caa940d3e30057af8235125c8376b2394622118344516895b045a6fe9b5ecb
event.hash: ZWNobyAtZSAiMTIzXG53QjV1clY4NXFxa1dcbndCNXVyVjg1cXFrVyJ8cGFzc3dkfGJhc2gtYmFzaDogRW50ZXI6IGNvbW1hbmQgbm90IGZvdW5kCg==
transaction.id: 052b36a73707754c7d49814cdc1f32fef3f72d334a7479f78f11c3229c1599d9
event.hash: ZWNobyAtZSAieCFcbkNLbGFOS0lOdWlYalxuQ0tsYU5LSU51aVhqInxwYXNzd2R8YmFzaC1iYXNoOiBFbnRlcjogY29tbWFuZCBub3QgZm91bmQK

The TTY logs are parsed once per day and uploaded directly into DShield SIEM with filebeat. The BASH script needs to be installed and configure according to the GitHub page [[2](https://github.com/bruneaug/DShield-SIEM/blob/main/AddOn/TTYLogs_To_DShield-SIEM.md)] to provide a transcript of the activity reviewed in Kibana.

![](https://isc.sans.edu/diaryimages/images/ttylogs_pic.png)

The addition of Suricata [[3](https://github.com/bruneaug/DShield-SIEM/blob/main/AddOn/Configure_Suricata.md)] is also available in the DShield dashboards and linked to all other logs.

![](https://isc.sans.edu/diaryimages/images/suricata_events_pic.png)
![](https://isc.sans.edu/diaryimages/images/suricata_alerts_pic.png)

An updated dashboard now contains these changes to reflect the ability to share between sub-dashboard most of the queries selected (i.e. selecting an IP will replicate everywhere).

![](https://isc.sans.edu/diaryimages/images/dashboard_pic.png)

The dashboard also has a Threat Map that can be used to view the logs traffic activity in "*movement*".

![](https://isc.sans.edu/diaryimages/images/threat_map.png)

[Jesse](https://isc.sans.edu/handler_list.html#jesse-lagrew) and I are at SANSFIRE, if you are onsite, come tonight at the **SANSFIRE 2026 Honeypot Workshop in Independence A - West (Level 5B) at 6:45 PM.**

[1] https://isc.sans.edu/honeypot.html
[2] https://github.com/bruneaug/DShield-SIEM/blob/main/AddOn/TTYLogs\_To\_DShield-SIEM.md
[3] https://github.com/bruneaug/DShield-SIEM/blob/main/AddOn/Configure\_Suricata.md
[4] https://isc.sans.edu/diary/DShield+SIEM+Docker+Updates/32276
[5] https://github.com/bruneaug/DShield-SIEM/tree/main

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My GitHub Page](https://github.com/bruneaug/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [DShield](/tag.html?tag=DShield) [ELK](/tag.html?tag=ELK) [Sensor Data](/tag.html?tag=Sensor Data) [SIEM](/tag.html?tag=SIEM) [Suricata](/tag.html?tag=Suricata) [TTY Logs](/tag.html?tag=TTY Logs)

[0 comment(s)](/diary/Recent%2BDShield%2BSIEM%2BUpdate/33156/#comments)

Click HERE to learn more about classes Guy is teaching for SANS

* [previous](/diary/33154)

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