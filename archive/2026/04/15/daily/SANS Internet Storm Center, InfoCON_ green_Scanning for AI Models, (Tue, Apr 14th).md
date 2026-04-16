---
title: Scanning for AI Models, (Tue, Apr 14th)
url: https://isc.sans.edu/diary/rss/32896
source: SANS Internet Storm Center, InfoCON: green
date: 2026-04-15
fetch_date: 2026-04-16T04:53:53.656091
---

# Scanning for AI Models, (Tue, Apr 14th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jesse La Grew](/handler_list.html#jesse-la-grew "Jesse La Grew")

Threat Level: [green](/infocon.html)

* [previous](/diary/32892)
* [next](/diary/32898)

Click HERE to learn more about classes Guy is teaching for SANS

# [Scanning for AI Models](/forums/diary/Scanning%2Bfor%2BAI%2BModels/32896/)

**Published**: 2026-04-14. **Last Updated**: 2026-04-15 00:19:53 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/Scanning%2Bfor%2BAI%2BModels/32896/#comments)

Starting March 10, 2026, my DShield sensor started getting probe for various AI models such as claude, openclaw, huggingface, etc. Reviewing the data already reported by other DShield sensors to ISC, the DShield database shows reporting of these probes started that day and has been active ever since.

Based on what we currently have reported, it appears the only source scanning for these models is IP 81.168.83.103. However, my sensor has been actively scanned by this source since January 29, 2026 and is still ongoing today. Beside the AI probe, it has been scanning various ports that are often associated with web content.

![](https://isc.sans.edu/diaryimages/images/81_168_83_103_pic1.png)

Reviewing the scanning activity from this host, it appears this source is the only IP we see reported to DShield performing this activity.

**ES|QL Query** [[1](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/esql-functions-operators.html)]

Using this ES|QL query in Kibana discover, it lists all the URL the actor is looking for. I recorded 52 queries between March 10 to April 13, 2026 where April 3rd, 2026 received the most activity.

FROM cowrie\*
| WHERE event.reference == "no match"
| WHERE http.request.body.content IS NOT NULL
| KEEP @timestamp, http.request.body.content
| WHERE http.request.body.content LIKE "\*openclaw\*" OR http.request.body.content LIKE "\*claude\*" OR  http.request.body.content LIKE "\*huggingface\*" OR  http.request.body.content LIKE "\*openai\*"  OR  http.request.body.content LIKE "\*clawdbot\*"
| SORT @timestamp DESC
| STATS Total=COUNT(http.request.body.content) BY AI\_Scan\_Activity=BUCKET(@timestamp, 50, ?\_tstart, ?\_tend)

![](https://isc.sans.edu/diaryimages/images/81_168_83_103_pic2.png)

This graph shows the start of activity searching for clawbot/moltbot first reported March 10, 2026 ever since then.

![](https://isc.sans.edu/diaryimages/images/81_168_83_103_pic3.png)**Indicators**

81.168.83.103 (AS 20860)
/.openclaw/workspace/db.sqlite
/.openclaw/workspace/chroma.db
/.openclaw/secrets.json
/.clawdbot/moltbot.json
/.claude/settings.json
/.claude/.credentials.json
/.cache/huggingface/token
/openai/env.json
/openai/credentials.json

[1] https://www.elastic.co/guide/en/elasticsearch/reference/8.19/esql-functions-operators.html
[[2](https://isc.sans.edu/weblogs/urlhistory.html?url=Ly5jYWNoZS9odWdnaW5nZmFjZS90b2tlbg==)] https://isc.sans.edu/weblogs/urlhistory.html?url=Ly5jYWNoZS9odWdnaW5nZmFjZS90b2tlbg== (/.cache/huggingface/token)
[[3](https://isc.sans.edu/weblogs/urlhistory.html?url=Ly5jbGF3ZGJvdC9tb2x0Ym90Lmpzb24=)] https://isc.sans.edu/weblogs/urlhistory.html?url=Ly5jbGF3ZGJvdC9tb2x0Ym90Lmpzb24= (/.clawdbot/moltbot.json)
[[4](https://isc.sans.edu/weblogs/urlhistory.html?url=Ly5vcGVuY2xhdy9zZWNyZXRzLmpzb24=)] https://isc.sans.edu/weblogs/urlhistory.html?url=Ly5vcGVuY2xhdy9zZWNyZXRzLmpzb24= (/.openclaw/secrets.json)
[[5](https://www.ox.security/blog/one-step-away-from-a-massive-data-breach-what-we-found-inside-moltbot/)] https://www.ox.security/blog/one-step-away-from-a-massive-data-breach-what-we-found-inside-moltbot/
[[6](http://https://www.virustotal.com/gui/ip-address/81.168.83.103)] https://www.virustotal.com/gui/ip-address/81.168.83.103
[[7](https://www.shodan.io/host/81.168.83.103)] https://www.shodan.io/host/81.168.83.103 (Linux system)

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My GitHub Page](https://github.com/bruneaug/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [openai](/tag.html?tag=openai) [AI Model](/tag.html?tag=AI Model) [moltbot](/tag.html?tag=moltbot) [huggingface](/tag.html?tag=huggingface) [openclaw](/tag.html?tag=openclaw) [claude](/tag.html?tag=claude) [DShield](/tag.html?tag=DShield)

[0 comment(s)](/diary/Scanning%2Bfor%2BAI%2BModels/32896/#comments)

Click HERE to learn more about classes Guy is teaching for SANS

* [previous](/diary/32892)
* [next](/diary/32898)

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