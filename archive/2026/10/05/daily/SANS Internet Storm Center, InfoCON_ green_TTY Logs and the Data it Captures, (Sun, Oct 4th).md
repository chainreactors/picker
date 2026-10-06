---
title: TTY Logs and the Data it Captures, (Sun, Oct 4th)
url: https://isc.sans.edu/diary/rss/33396
source: SANS Internet Storm Center, InfoCON: green
date: 2026-10-05
fetch_date: 2026-10-06T08:25:34.311973
---

# TTY Logs and the Data it Captures, (Sun, Oct 4th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/33394)

Click HERE to learn more about classes Guy is teaching for SANS

# [TTY Logs and the Data it Captures](/forums/diary/TTY%2BLogs%2Band%2Bthe%2BData%2Bit%2BCaptures/33396/)

**Published**: 2026-10-04. **Last Updated**: 2026-10-05 00:15:00 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/TTY%2BLogs%2Band%2Bthe%2BData%2Bit%2BCaptures/33396/#comments)

For an experiment, I created a script [[1](https://github.com/bruneaug/DShield-Sensor/blob/main/sensor_scripts/daily_tty.sh)] that parses and send the TTY logs collected from actors or bots activity that run various commands after they successfully login the DShield sensor. Those TTY logs are sent daily at the end of each day to the DShield SIEM [[2](https://github.com/bruneaug/DShield-SIEM)] to be correlated with all the data.

The following [ES|QL](https://www.elastic.co/docs/reference/query-languages/esql) query provides a summary of all contab commands matching a TTYLog hash performed by different actors while logged in the sensor over a 90 day period.

**TTYLogs Correlation**

FROM cowrie\*
| WHERE transaction.id == "f904275333aeac48d7df6cf53fe5fb9212c7d132a7d37253d2ab9321ba2690d8"
| WHERE event.hash IS NOT NULL
| KEEP transaction.id, event.hash
| STATS Total=COUNT(event.hash) BY event.hash, transaction.id
| SORT Total DESC

This transaction ID captured 5 similar crontab commands that are translated from its hash equivalent into this list executed by more than 3130 different actors (IPs):

![](https://isc.sans.edu/diaryimages/images/TTYLogs_decoded.png)

**TTYLogs Sources**

transaction.id: f904275333aeac48d7df6cf53fe5fb9212c7d132a7d37253d2ab9321ba2690d8 over a 90 day period

![](https://isc.sans.edu/diaryimages/images/transaction_ID_90days.png)

Other example of Event Hash decoded and sent to DShield SIEM for analysis

![](https://isc.sans.edu/diaryimages/images/Example_Even_Hash.png)

**Top 10 Indicators**

      IP                      ASN
102.88.137.80        29465
42.96.20.16            131423
182.253.221.210    38482
46.188.119.26         8334
159.223.97.218       14061
185.158.22.150       210022
193.233.48.169       207713
209.99.190.200       402253
45.64.74.51              55933
202.152.148.27        23951

[1] https://github.com/bruneaug/DShield-Sensor/blob/main/sensor\_scripts/daily\_tty.sh
[2] https://github.com/bruneaug/DShield-SIEM
[3] https://www.elastic.co/docs/reference/query-languages/esql

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My GitHub Page](https://github.com/bruneaug/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [Analysis](/tag.html?tag=Analysis) [DShield sensor](/tag.html?tag=DShield sensor) [DShield SIEM](/tag.html?tag=DShield SIEM) [ESQL](/tag.html?tag=ESQL) [TTYLog](/tag.html?tag=TTYLog)

[0 comment(s)](/diary/TTY%2BLogs%2Band%2Bthe%2BData%2Bit%2BCaptures/33396/#comments)

Click HERE to learn more about classes Guy is teaching for SANS

* [previous](/diary/33394)

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