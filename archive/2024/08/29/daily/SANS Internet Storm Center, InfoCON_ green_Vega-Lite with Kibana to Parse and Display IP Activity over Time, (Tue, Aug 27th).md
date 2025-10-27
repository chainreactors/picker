---
title: Vega-Lite with Kibana to Parse and Display IP Activity over Time, (Tue, Aug 27th)
url: https://isc.sans.edu/diary/rss/31210
source: SANS Internet Storm Center, InfoCON: green
date: 2024-08-29
fetch_date: 2025-10-06T18:05:47.020772
---

# Vega-Lite with Kibana to Parse and Display IP Activity over Time, (Tue, Aug 27th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31208)
* [next](/diary/31216)

# [Vega-Lite with Kibana to Parse and Display IP Activity over Time](/forums/diary/VegaLite%2Bwith%2BKibana%2Bto%2BParse%2Band%2BDisplay%2BIP%2BActivity%2Bover%2BTime/31210/)

**Published**: 2024-08-27. **Last Updated**: 2024-08-28 00:34:20 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/VegaLite%2Bwith%2BKibana%2Bto%2BParse%2Band%2BDisplay%2BIP%2BActivity%2Bover%2BTime/31210/#comments)

I have been curious for a while looking at Kibana's Vega log parsing options to try to come up with displays and layout that aren't standard in Kibana. A lot of the potential layouts already exists in Kibana but some of the other aren't easily created and using Vega [[2](https://vega.github.io/vega/examples/)] provides some of the building block to create some of the output that I am researching and testing with DShield sensor data captured by cowrie honeypot [[4](https://github.com/DShield-ISC/dshield)].

**Building a Query in the Visualize Library**

In my test query, I wanted to display on the left of the graph the IP List and in the bottom, the date of the activity. This way when I choose to summarize the activity by IP or any of the other fields I happen to select, it will display the activity by date of any IP that was active over time.

A text copy of the JSON code is posted at the bottom. This simple query takes the data from cowrie logs as its input to format the output:

![](https://isc.sans.edu/diaryimages/images/vega_picture1.PNG)

**The Data Output**

Before I zoom in the time of interest to see some of the long-term activity, this is what the up to 10000 records looks like with all the IPs displayed in this picture. It is now easy to see a cluster of activity in this picture, next we need to zoom in the time of the activity to find which IP has this cluster.

![](https://isc.sans.edu/diaryimages/images/vega_picture2.PNG)

After I zoom in the data, the result of a 7-day query provides the following data of a cluster of activity over time. In this picture, you can see that one IP 193.201.9.156 was active for several hours between 22 Aug 06:00 - 22 Aug 21:00.

![](https://isc.sans.edu/diaryimages/images/vega_picture3.PNG)

**DShield SIEM Integration**

The primary goal of this test is to integrate this into the DShield SIEM [[1](https://github.com/bruneaug/DShield-SIEM)] ELK Stack to be able to see overtime which actor are active and how long can they be seen over time in one of the dashboards. Now that we have an IP to look at, the time range can be expended as far as I want, and this picture shows activity of IP 193.201.9.156 over the past 30 days.

![](https://isc.sans.edu/diaryimages/images/vega_picture4.PNG)
**Sample Vega-Lite Query**

This is the code used in the above example:

{
  $schema: https://vega.github.io/schema/vega-lite/v5.json
  title: Cowrie Logs - Actor Activity over Time
  data: {
    url: {
      %context%: true
      %timefield%: @timestamp
      interval: {%autointerval%: true}
      index: cowrie\*
      body: {
        size: 10000
        \_source: ["@timestamp","related.ip", "source.address", "user.name"]
      }
    }
    format: {property: "hits.hits"}
  }

  transform: [
  {calculate: "toDate(datum.\_source['@timestamp'])", as: "Time"},
  {"calculate": "datum.\_source['related.ip']", "as": "IP"},
  {"calculate": "datum.\_source['user.name']", "as": "Name"}
  ]
  mark: square
  encoding: {
    // https://vega.github.io/vega-lite/docs/timeunit.html#input
    // Change timeUnit to display Month Day and Hour of activity
    x: {"timeUnit": "monthdatehours",field: "Time", type: "ordinal", title: "Date/Time" }
    y: {field: "IP", type: "ordinal", title: "Actor IP Address"}
    color: {field: "IP", type: "ordinal", legend: null}
  }
 }

[1] https://www.elastic.co/guide/en/kibana/current/vega.html
[2] https://vega.github.io/vega/examples/
[3] https://github.com/bruneaug/DShield-SIEM
[4] https://github.com/DShield-ISC/dshield

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My Handler Page](https://handlers.sans.org/gbruneau/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [VegaLite](/tag.html?tag=VegaLite) [Threat Hunting](/tag.html?tag=Threat Hunting) [SIEM](/tag.html?tag=SIEM) [SecOps](/tag.html?tag=SecOps) [ELK](/tag.html?tag=ELK) [DShield](/tag.html?tag=DShield) [Cowrie](/tag.html?tag=Cowrie) [Analysis](/tag.html?tag=Analysis)

[0 comment(s)](/diary/VegaLite%2Bwith%2BKibana%2Bto%2BParse%2Band%2BDisplay%2BIP%2BActivity%2Bover%2BTime/31210/#comments)

* [previous](/diary/31208)
* [next](/diary/31216)

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