---
title: Scanning Webserver with /&#x24;(pwd)/ as a Starting Path, (Sun, Jan 25th)
url: https://isc.sans.edu/diary/rss/32654
source: SANS Internet Storm Center, InfoCON: green
date: 2026-01-26
fetch_date: 2026-01-27T03:39:16.619610
---

# Scanning Webserver with /&#x24;(pwd)/ as a Starting Path, (Sun, Jan 25th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Mark Baggett](/handler_list.html#mark-baggett "Mark Baggett")

Threat Level: [green](/infocon.html)

* [previous](/diary/32650)

# [Scanning Webserver with /$(pwd)/ as a Starting Path](/forums/diary/Scanning%2BWebserver%2Bwith%2Bpwd%2Bas%2Ba%2BStarting%2BPath/32654/)

**Published**: 2026-01-25. **Last Updated**: 2026-01-26 00:59:32 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/Scanning%2BWebserver%2Bwith%2Bpwd%2Bas%2Ba%2BStarting%2BPath/32654/#comments)

Based on the sensors reporting to ISC, this activity started on the 13 Jan 2026. My own sensor started seeing the first scan on the 21 Jan 2026 with limited probes. So far, this activity has been limited to a few scans based on the reports available in ISC [[5](https://isc.sans.edu/weblogs/urlhistory.html?url=LyQocHdkKS8uCg==)] (select Match Partial URL and Draw):

![](https://isc.sans.edu/diaryimages/images/isc_pwd_activity.png)

This is a sample list of the directories actors are scanning for using the following patterns:

/$(pwd)/.env.staging
/$(pwd)/.env.development
/$(pwd)/.env.production
/$(pwd)/.env.local
/$(pwd)/.env
$(pwd)/terraform.tfstate
/$(pwd)/docker-compose.yml
/$(pwd)/netlify.toml

This [Gephi](https://gephi.org/) graph shows the relationship of each probed URL by the two IP addresses:

![](https://isc.sans.edu/diaryimages/images/pwd_scanning_activity.png)

**Kibana ES|QL Query**

FROM cowrie\*
| WHERE event.reference == "no match"
| KEEP related.ip,http.request.body.content
| WHERE http.request.body.content IS NOT NULL
| WHERE http.request.body.content RLIKE ".\*\\/\\$\\(pwd\\).\*"
| STATS COUNT(http.request.body.content) BY related.ip, http.request.body.content

**Indicators**

By selecting one of these two indicators, it shows their scanning activity for the /$(pwd)/ pattern in the ISC web logs.

[185.177.72.52](https://isc.sans.edu/weblogs/sourcedetails.html?date=2026-01-21&ip=185.177.72.52)
[185.177.72.23](https://isc.sans.edu/weblogs/sourcedetails.html?date=2026-01-25&ip=185.177.72.23)

We also appreciate feedback and suggestions about what tool is used to perform these scans. Please use our [contact](https://isc.sans.edu/contact.html) page to provide feedback.

[1] https://www.elastic.co/guide/en/elasticsearch/reference/8.19/esql-using.html
[2] https://gephi.org/
[3] https://isc.sans.edu/weblogs/sourcedetails.html?date=2026-01-21&ip=185.177.72.52
[4] https://isc.sans.edu/weblogs/sourcedetails.html?date=2026-01-25&ip=185.177.72.23
[5] https://isc.sans.edu/weblogs/urlhistory.html?url=LyQocHdkKS8uCg==

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My GitHub Page](https://github.com/bruneaug/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [pwd](/tag.html?tag=pwd) [DShield sensor](/tag.html?tag=DShield sensor) [DShield SIEM](/tag.html?tag=DShield SIEM) [Gephi](/tag.html?tag=Gephi) [Web Scanning](/tag.html?tag=Web Scanning) [research](/tag.html?tag=research)

[0 comment(s)](/diary/Scanning%2BWebserver%2Bwith%2Bpwd%2Bas%2Ba%2BStarting%2BPath/32654/#comments)

* [previous](/diary/32650)

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