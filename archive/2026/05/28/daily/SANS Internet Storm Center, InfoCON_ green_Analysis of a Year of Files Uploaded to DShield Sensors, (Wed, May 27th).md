---
title: Analysis of a Year of Files Uploaded to DShield Sensors, (Wed, May 27th)
url: https://isc.sans.edu/diary/rss/33026
source: SANS Internet Storm Center, InfoCON: green
date: 2026-05-28
fetch_date: 2026-05-29T06:06:30.042089
---

# Analysis of a Year of Files Uploaded to DShield Sensors, (Wed, May 27th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/33024)

Click HERE to learn more about classes Guy is teaching for SANS

# [Analysis of a Year of Files Uploaded to DShield Sensors](/forums/diary/Analysis%2Bof%2Ba%2BYear%2Bof%2BFiles%2BUploaded%2Bto%2BDShield%2BSensors/33026/)

**Published**: 2026-05-27. **Last Updated**: 2026-05-28 19:41:55 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/Analysis%2Bof%2Ba%2BYear%2Bof%2BFiles%2BUploaded%2Bto%2BDShield%2BSensors/33026/#comments)

Using the data collected over the past year and using Kibana these two ES|QL query to summarize the data, this shows the list of the most uploaded threat to two DShield sensors (local and cloud) over the past year. I have sorted the activity by months that shows the evolution of files uploaded to the sensors each month. The activity peaked during the winter months (Dec 2025 - Feb 2026) and started decreasing in March 2026 for each sensor.

![](https://isc.sans.edu/diaryimages/images/malware_1year_activity.png)

**ES|QL Query by Sensor**

FROM cowrie\*
| WHERE threat.indicator.provider == "virustotal"
| WHERE related.hash IS NOT NULL
| WHERE threat.indicator.file.type IS NOT NULL
| WHERE threat.software.name IS NOT NULL
| SORT @timestamp DESC
| STATS Total=COUNT(related.hash) BY FileType=threat.indicator.file.type, agent.name=BUCKET(@timestamp, 50, ?\_tstart, ?\_tend)

**Past Year of Files Uploaded to Dshield Sensors**

This example displays the activity by file type (8) for a one-year period. The file type uploaded or downloaded to the sensor are ELF, Shell script, Powershell, HTML, Text, unknown, DOS batch file and JavaScript.

![](https://isc.sans.edu/diaryimages/images/malware_1year_activity_by_filetype.png)

**ES|QL Activity by File Type**

FROM cowrie\*
| WHERE threat.indicator.provider == "virustotal"
| WHERE related.hash IS NOT NULL
| WHERE threat.indicator.file.type IS NOT NULL
| WHERE threat.software.name IS NOT NULL
| WHERE  threat.indicator.name IS NOT NULL
| SORT @timestamp DESC
| STATS Total=COUNT(related.hash) BY agent.name, threat.indicator.name=BUCKET(@timestamp, 50, ?\_tstart, ?\_tend)

To monitor the type of files uploaded or downloaded to the sensor, using the cowrie\_vt.sh [[3](http://https://github.com/bruneaug/DShield-Sensor/blob/main/sensor_scripts/cowrie_vt.sh)] Python [Jesse's](https://isc.sans.edu/handler_list.html#jesse-lagrew) script [[4](https://raw.githubusercontent.com/jslagrew/cowrieprocessor/main/cowrie_malware_enrichment.py)], it provides a daily list of hash files that are stored on the sensor and can be monitored within the DShield SIEM [[2](https://github.com/bruneaug/DShield-SIEM)].

[1] https://isc.sans.edu/tools/honeypot/
[2] https://github.com/bruneaug/DShield-SIEM
[3] https://github.com/bruneaug/DShield-Sensor/blob/main/sensor\_scripts/cowrie\_vt.sh
[4] https://raw.githubusercontent.com/jslagrew/cowrieprocessor/main/cowrie\_malware\_enrichment.py

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My GitHub Page](https://github.com/bruneaug/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [DShield sensor](/tag.html?tag=DShield sensor) [DShield SIEM](/tag.html?tag=DShield SIEM) [Malware Analysis](/tag.html?tag=Malware Analysis) [Statistics](/tag.html?tag=Statistics) [Virustotal](/tag.html?tag=Virustotal)

[0 comment(s)](/diary/Analysis%2Bof%2Ba%2BYear%2Bof%2BFiles%2BUploaded%2Bto%2BDShield%2BSensors/33026/#comments)

Click HERE to learn more about classes Guy is teaching for SANS

* [previous](/diary/33024)

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