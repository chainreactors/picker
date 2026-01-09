---
title: Analysis using Gephi with DShield Sensor Data, (Wed, Jan 7th)
url: https://isc.sans.edu/diary/rss/32608
source: SANS Internet Storm Center, InfoCON: green
date: 2026-01-08
fetch_date: 2026-01-09T03:32:01.751140
---

# Analysis using Gephi with DShield Sensor Data, (Wed, Jan 7th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/32606)

# [Analysis using Gephi with DShield Sensor Data](/forums/diary/Analysis%2Busing%2BGephi%2Bwith%2BDShield%2BSensor%2BData/32608/)

**Published**: 2026-01-07. **Last Updated**: 2026-01-08 00:13:26 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/Analysis%2Busing%2BGephi%2Bwith%2BDShield%2BSensor%2BData/32608/#comments)

I'm always looking for new ways of manipulating the data captured by my DShield sensor [[1](https://isc.sans.edu/diary/Analysis%2Bof%2BSSH%2BHoneypot%2BData%2Bwith%2BPowerBI/28872)]. This time I used Gephi [[2](https://gephi.org)] and Graphiz [[3](https://www.graphviz.org/download/)] a popular and powerful tool for visualizing and exploring relationships between nodes, to examine the relationship between the source IP, filename and which sensor got a copy of the file. I queried the past 30 days of data stored in my ELK [[4](https://github.com/bruneaug)] database in Kibana using ES|QL [[5](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/esql-using.html)][[6](https://isc.sans.edu/diary/Using%2BESQL%2Bin%2BKibana%2Bto%2BQueries%2BDShield%2BHoneypot%2BLogs/31704)] to query and export the data and import the result into Gephi.

This is the query I used to export the data I needed. Notice the field event.reference == "no match" which is a tag that filters all the know researchers [7] added by Logstash as a tag.

**Kibana ES|QL Query from Analytics → Discover**

FROM cowrie\*
| WHERE event.reference == "no match"
| KEEP related.ip, file.name, host.name
| WHERE file.name IS NOT NULL
| LIMIT 10000

![](https://isc.sans.edu/diaryimages/images/gephi_srcip_file_sensor_pic2.png)

This second example exports the source IP, file hash and filename. This query exported 2685 records for a period of 30 days of data.

FROM cowrie\*
| WHERE event.reference == "no match"
| KEEP related.ip, related.hash, file.name
| WHERE file.name IS NOT NULL
| LIMIT 10000

This screenshot shows one of the 2 groups of malware activity that contains various files. This is the first grouping of the files with multiple hashes and IP addresses for the same filename.

![](https://isc.sans.edu/diaryimages/images/gephi_malware_hash_pic3.png)

The second grouping of IPs, filename and hashes are all related to redtail malware.

![](https://isc.sans.edu/diaryimages/images/gephi_malware_hash_selection_overall_pic6.png)

One of the nice things with Gephi is where you can put the cursor on a specific type of activity to show the overall relationship from that point view and push the unselected data into the background. Using this graph and selecting with the cursor on IP 130.12.180.51 that uploaded several times (large blue arrow) shows the redtail malware by IP 130.12.180.51 over the past 30 days and the with all the files matching hashes.

![](https://isc.sans.edu/diaryimages/images/gephi_malware_hash_selection_group2_pic5.png)

**Indicators**

45.132.180.51
130.12.180.51
193.32.162.157
213.209.143.51

783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59
59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5
048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7
dbb7ebb960dc0d5a480f97ddde3a227a2d83fcaca7d37ae672e6a0a6785631e9
d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e
3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f

[1] https://isc.sans.edu/diary/Analysis+of+SSH+Honeypot+Data+with+PowerBI/28872
[2] https://gephi.org/
[3] https://www.graphviz.org/download/
[4] https://github.com/bruneaug
[5] https://www.elastic.co/guide/en/elasticsearch/reference/8.19/esql-using.html
[6] https://isc.sans.edu/diary/Using+ESQL+in+Kibana+to+Queries+DShield+Honeypot+Logs/31704
[7] https://isc.sans.edu/api/threatcategory/research?json
[8] https://gephi.org/quickstart/

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My GitHub Page](https://github.com/bruneaug/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [Kibana](/tag.html?tag=Kibana) [ELK](/tag.html?tag=ELK) [ESQL](/tag.html?tag=ESQL) [node analysis](/tag.html?tag=node analysis) [Graphiz](/tag.html?tag=Graphiz) [Gephi](/tag.html?tag=Gephi) [Relationship](/tag.html?tag=Relationship)

[0 comment(s)](/diary/Analysis%2Busing%2BGephi%2Bwith%2BDShield%2BSensor%2BData/32608/#comments)

* [previous](/diary/32606)

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