---
title: DShield SIEM Docker Updates, (Wed, Sep 10th)
url: https://isc.sans.edu/diary/rss/32276
source: SANS Internet Storm Center, InfoCON: green
date: 2025-09-12
fetch_date: 2025-10-02T20:03:05.622066
---

# DShield SIEM Docker Updates, (Wed, Sep 10th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jesse La Grew](/handler_list.html#jesse-la-grew "Jesse La Grew")

Threat Level: [green](/infocon.html)

* [previous](/diary/32274)
* [next](/diary/32282)

# [DShield SIEM Docker Updates](/forums/diary/DShield%2BSIEM%2BDocker%2BUpdates/32276/)

**Published**: 2025-09-10. **Last Updated**: 2025-09-11 00:26:25 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/DShield%2BSIEM%2BDocker%2BUpdates/32276/#comments)

Since the last update [[5](https://isc.sans.edu/diary/DShield%2BSIEM%2BDocker%2BUpdates/31680)], over the past few months I added several enhancements to DShield SIEM and webhoneypot sensor collection that included an update to the interface to help with DShield sensor analysis. I updated the main dashboard to have all the main analytic tools listed on the left for quick access to all the sub-dashboards.

![](https://isc.sans.edu/diaryimages/images/DShield_Main_Page.png)

**ELK Update**

* Removed from the interface the usage of TCP 5601, now just **https://IP**
* Updated all Elastic packages to version 8.19.3
* Updated the webhoneypot logstash parser based on [Mark](https://isc.sans.edu/handler_list.html#mark-baggett)'s update
* Updated the DShield - Web Analytic page to reflect new content
* ELK monitoring with Metricbeat
* 2 Treat Intel feeds (run from ELK server via cronjob)
* Inclusion of ISC web activity detection rules
* Updated cowrie and docker troubleshooting pages [[2](https://github.com/bruneaug/DShield-SIEM/blob/main/Troubleshooting/docker_useful_commands..md)][[3](https://github.com/bruneaug/DShield-SIEM/blob/main/Troubleshooting/Troubleshooting_SIEM_and_Sensor.md)]
* List of previous SANS.edu [BACS](https://www.sans.edu/cyber-security-programs/bachelors-degree/) internships students’ scripts [[4](https://github.com/bruneaug/DShield-SIEM/blob/main/README.md#dshield-analysis-scripts-and-code-by-students)]

![](https://isc.sans.edu/diaryimages/images/DShield_Webhoneypot_Activity.png)

I tested and added two additional applications in the Kibana DShield Main Page Activity to help with analysis. These are installed via docker when installing or updating docker to the current version:

**Analysis Tools**

* CyberChef
* Mitre ATT&CK - Attack Navigator

**How to upgrade to the current version?**

* cd DShield-SIEM
* sudo docker compose stop
* git pull --autostash
* sudo docker compose rm -f -v
* sudo docker compose up --build -d

**Load new templates into Kibana**:

* sudo docker exec -ti filebeat bash
* ./filebeat setup -e

[1] https://github.com/bruneaug/DShield-SIEM/blob/main/README.md
[2] https://github.com/bruneaug/DShield-SIEM/blob/main/Troubleshooting/docker\_useful\_commands..md
[3] https://github.com/bruneaug/DShield-SIEM/blob/main/Troubleshooting/Troubleshooting\_SIEM\_and\_Sensor.md
[4] https://github.com/bruneaug/DShield-SIEM/blob/main/README.md#dshield-analysis-scripts-and-code-by-students
[5] https://isc.sans.edu/diary/DShield+SIEM+Docker+Updates/31680
[6] https://www.sans.edu/cyber-security-programs/bachelors-degree/

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My GitHub Page](https://github.com/bruneaug/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [Attack Navigator](/tag.html?tag=Attack Navigator) [ATTCK](/tag.html?tag=ATTCK) [CyberChef](/tag.html?tag=CyberChef) [Docker](/tag.html?tag=Docker) [DShield](/tag.html?tag=DShield) [ELK](/tag.html?tag=ELK) [SIEM](/tag.html?tag=SIEM)

[0 comment(s)](/diary/DShield%2BSIEM%2BDocker%2BUpdates/32276/#comments)

* [previous](/diary/32274)
* [next](/diary/32282)

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