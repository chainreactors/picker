---
title: DShield SIEM Docker Updates, (Thu, Feb 13th)
url: https://isc.sans.edu/diary/rss/31680
source: SANS Internet Storm Center, InfoCON: green
date: 2025-02-14
fetch_date: 2025-10-06T20:39:29.502297
---

# DShield SIEM Docker Updates, (Thu, Feb 13th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31676)
* [next](/diary/31686)

# [DShield SIEM Docker Updates](/forums/diary/DShield%2BSIEM%2BDocker%2BUpdates/31680/)

**Published**: 2025-02-13. **Last Updated**: 2025-02-13 01:23:59 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/DShield%2BSIEM%2BDocker%2BUpdates/31680/#comments)

Over the past several weeks, I have been testing various enhancements to the [DShield SIEM](https://github.com/bruneaug/DShield-SIEM/tree/main), to process [DShield sensor](https://github.com/bruneaug/DShield-Sensor) log from local and cloud sensors with Filebeat and Filebeat modules to easily send [Zeek](https://www.elastic.co/guide/en/integrations/current/zeek.html) and [NetFlow](https://www.elastic.co/guide/en/integrations/current/netflow.html) logs back to a local network ELK stack via home router natting. This is a list of updates and enhancements:

- Upgrade to the current version of Elastic [8.17.2](https://www.elastic.co/guide/en/elasticsearch/reference/current/release-notes-8.17.2.html)
- A single script to configure the base configuration of all the docker files (change\_perms.sh)
- Addition of docker filebeat for cloud DShield sensor collection (Cowrie, Zeek & NetFlow logs)
- Second filebeat to ingest ISC & Rosti Threat Intel IP data [[3](https://github.com/bruneaug/DShield-SIEM/blob/main/AddOn/ISC_threatintel.md)]
- Separation of GitHub DShield SIEM & DShield sensor scripts
- Addition to docker Metricbeat for ELK Stack metric information
- Updated dashboard that includes Zeek in the tab lists
- Query in one dashboard is linked to the others
- Tested the ELK Stack in a LXC Proxmox container [[4](https://github.com/bruneaug/DShield-SIEM/blob/main/AddOn/LXC_Container_DShield-SIEM.md)]
- The addition of ELK Stack monitoring of all the Beats and Logstash
- Configured Logstash to parse logs with Beats pipelines (Zeek & NetFlow)
- Removed and merged multiple steps to simplify the installation (change\_perms.sh)
- Updated some sections of the Troubleshooting document [[5](https://github.com/bruneaug/DShield-SIEM/blob/main/Troubleshooting/Troubleshooting_SIEM_and_Sensor.md)]
- Updated some sections of the docker useful commands [[6](http://Updated some sections of the docker useful commands)]
- Updated the DShield SIEM network flow [[7](https://github.com/bruneaug/DShield-SIEM/blob/main/Troubleshooting/DShield-SIEM-Flow.png)]
- Docker update steps to current version [[8](https://github.com/bruneaug/DShield-SIEM/blob/main/Troubleshooting/docker_useful_commands..md#update-dshield-elk-to-the-latest-version)]

**DShield SIEM Main Dashboard**

![](https://isc.sans.edu/diaryimages/images/DShield_SIEM_12Feb25.png)

[1] https://github.com/bruneaug/DShield-SIEM/tree/main
[2] https://github.com/bruneaug/DShield-Sensor
[3] https://github.com/bruneaug/DShield-SIEM/blob/main/AddOn/ISC\_threatintel.md
[4] https://github.com/bruneaug/DShield-SIEM/blob/main/AddOn/LXC\_Container\_DShield-SIEM.md
[5] https://github.com/bruneaug/DShield-SIEM/blob/main/Troubleshooting/Troubleshooting\_SIEM\_and\_Sensor.md
[6] https://github.com/bruneaug/DShield-SIEM/blob/main/Troubleshooting/docker\_useful\_commands..md
[7] https://github.com/bruneaug/DShield-SIEM/blob/main/Troubleshooting/DShield-SIEM-Flow.png
[8] https://github.com/bruneaug/DShield-SIEM/blob/main/Troubleshooting/docker\_useful\_commands..md#update-dshield-elk-to-the-latest-version
[9] https://www.elastic.co/guide/en/elasticsearch/reference/current/release-notes-8.17.2.html

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My GitHub Page](https://github.com/bruneaug/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [Metricbeat](/tag.html?tag=Metricbeat) [Filebeat](/tag.html?tag=Filebeat) [Netflow](/tag.html?tag=Netflow) [Zeek](/tag.html?tag=Zeek) [Threat Intel](/tag.html?tag=Threat Intel) [SIEM](/tag.html?tag=SIEM) [DShield](/tag.html?tag=DShield) [Cowrie](/tag.html?tag=Cowrie) [Honeypot](/tag.html?tag=Honeypot)

[0 comment(s)](/diary/DShield%2BSIEM%2BDocker%2BUpdates/31680/#comments)

* [previous](/diary/31676)
* [next](/diary/31686)

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