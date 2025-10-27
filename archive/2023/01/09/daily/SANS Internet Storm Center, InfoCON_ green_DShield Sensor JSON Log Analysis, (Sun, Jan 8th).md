---
title: DShield Sensor JSON Log Analysis, (Sun, Jan 8th)
url: https://isc.sans.edu/diary/rss/29412
source: SANS Internet Storm Center, InfoCON: green
date: 2023-01-09
fetch_date: 2025-10-04T03:22:01.126570
---

# DShield Sensor JSON Log Analysis, (Sun, Jan 8th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29410)
* [next](/diary/29416)

# [DShield Sensor JSON Log Analysis](/forums/diary/DShield%2BSensor%2BJSON%2BLog%2BAnalysis/29412/)

**Published**: 2023-01-08. **Last Updated**: 2023-01-08 21:15:29 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[2 comment(s)](/diary/DShield%2BSensor%2BJSON%2BLog%2BAnalysis/29412/#comments)

This is a review and analysis of some of my json DShield logs for a 9-day period. For this, I created some parsers using jq [[1](https://stedolan.github.io/jq/download/)] and MS PowerBI which I described here to parse GeoIP [[2](https://powerbi.microsoft.com/en-us/downloads/)] with the script previously posted [here](https://isc.sans.edu/diary/28872). This is the highlights from this timeframe 5 - 13 Dec 2022:

**Top IP Overall**

![](https://isc.sans.edu/diaryimages/images/top_ip_overall.PNG)
**Top IP by Day**

![](https://isc.sans.edu/diaryimages/images/top_ip_day.PNG)

The most popular username/password in this 9-day period is knockknockwhosthere:

**Successful Login by Username/Password**

![](https://isc.sans.edu/diaryimages/images/password_success.PNG)

**Failed Login by Username/Password**

![](https://isc.sans.edu/diaryimages/images/password_failed.PNG)

Comparing the usernames and passwords by IP address, the results were interesting. Several of the sources attempted multiple times to login without using any passwords.

![](https://isc.sans.edu/diaryimages/images/password_activity_by_ip.PNG)

Reviewing top IP [193.105.134.95](https://isc.sans.edu/ipinfo.html?ip=193.105.134.95) has been reported over 150K to DShield since March 10, 2022 and was seen daily by the honeypot:

![](https://isc.sans.edu/diaryimages/images/top_ip_by_day.PNG)

**Initial Connection to Honeypot (Connect)**

Here is an example of parsing cowrie logs using jq for the initial connection to the sensor

cat cowrie.json.2022-12-05 | jq 'select (.eventid == "cowrie.session.connect")' | jq '.src\_ip  + "," + (.src\_port|tostring)+ "," + (.dst\_port|tostring) + "," + .session + "," + .protocol + "," + .timestamp + ",1"' | tr -d '"'\
| tr -d '"' \
| sed '1i\SrcIP,SrcPort,DstPort,Session,Protocol,Timestamp,Total' >> connect.csv

Next time I will explore in details the commands, ssh versions and files sent to the DShield sensor.

[1] https://stedolan.github.io/jq/download/
[2] https://powerbi.microsoft.com/en-us/downloads/
[3] https://isc.sans.edu/diary/29370
[4] https://isc.sans.edu/diary/28872
[5] https://isc.sans.edu/ipinfo.html?ip=193.105.134.95
[6] https://handlers.sans.edu/gbruneau/scripts/process\_geoip.sh

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My Handler Page](https://handlers.sans.org/gbruneau/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [sensor](/tag.html?tag=sensor) [PowerBI](/tag.html?tag=PowerBI) [logs analysis](/tag.html?tag=logs analysis) [json](/tag.html?tag=json) [infosec](/tag.html?tag=infosec) [dshield](/tag.html?tag=dshield) [detection](/tag.html?tag=detection) [analysis](/tag.html?tag=analysis)

[2 comment(s)](/diary/DShield%2BSensor%2BJSON%2BLog%2BAnalysis/29412/#comments)

* [previous](/diary/29410)
* [next](/diary/29416)

### Comments

Of course, the ISC site itself already generates some nice graphs and statistics of submitted SSH logs, among other things. The honeypot system I've been working on in the past year also generates some statistics for SSH and web attempts (submitted to ISC), mostly running on PHP and MariaDB.

#### Vincent T

#### Jan 9th 2023 2 years ago

This is interesting! The GeoIP regions seem to differ a lot from Spamhaus bot countries. Sure, the US and CN will be at the top due to the sheer number of IP addresses in those regions but I was not expecting CL to be so high. I hope this data is helping make some blocklist somewhere. Personally, I like to use something more dynamic such as fail2ban for open ports with logins but a lot of people seem to like blocklists these days.

#### Sam

#### Jan 9th 2023 2 years ago

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