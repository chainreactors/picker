---
title: A Survey of Scans for GeoServer Vulnerabilities, (Tue, Aug 6th)
url: https://isc.sans.edu/diary/rss/31148
source: SANS Internet Storm Center, InfoCON: green
date: 2024-08-07
fetch_date: 2025-10-06T18:05:51.736808
---

# A Survey of Scans for GeoServer Vulnerabilities, (Tue, Aug 6th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31144)
* [next](/diary/31150)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [A Survey of Scans for GeoServer Vulnerabilities](/forums/diary/A%2BSurvey%2Bof%2BScans%2Bfor%2BGeoServer%2BVulnerabilities/31148/)

**Published**: 2024-08-06. **Last Updated**: 2024-08-06 14:20:15 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/A%2BSurvey%2Bof%2BScans%2Bfor%2BGeoServer%2BVulnerabilities/31148/#comments)

A little bit over a year ago, I wrote about scans for GeoServer [1][2]. GeoServer is a platform to process geographic data [3]. It makes it easy to share geospatial data in various common standard formats. Recently, new vulnerabilities were discovered in GeoServer, prompting me to look again at what our honeypots pick up [4].

Let's first look at the "big picture": How many scans did we see? The total number of requests for URLs starting with "/geoserver" was 211,143 since the beginning of the year.

![number of geoserver scans from 2023 to today, ](https://isc.sans.edu/diaryimages/images/Screenshot%202024-08-06%20at%209_43_47%E2%80%AFAM.png)

Interest in GeoServer started in 2023. It ceased after August but then came back early this year. After the latest SQL exploit was discovered (July 5th), scans for GeoServer surged.

When I wrote about the GeoServer scans last year, a reader noted that Shadowserver had just started scanning for GeoServer. Indeed, most of the time, all GeoServer scans on particular days can be attributed to researchers. In addition to Shadowserver, Internet Census (associated with BitSight) is scanning for GeoServer instances. Personally, I think this is a good thing. Shadowserver will notify ISPs who host insecure instances, and they will find them before the bad guys.

![scnas from researchers vs total scans showing that most of the time all scans come from researchers.](https://isc.sans.edu/diaryimages/images/Screenshot%202024-08-06%20at%209_58_48%E2%80%AFAM.png)

If you are interested, you can retrieve a list of research IPs from our API [5]

Once we remove the scans we identified as "research," these are the top countries from which scans originate:

Top Countries

| Country | Count |
| --- | --- |
| China | 26,844 |
| South Korea | 2,890 |
| USA | 2,549 |
| Germany | 1,685 |
| Sweden | 1,593 |
| Russia | 1,516 |
| Canada | 1,417 |
| Brazil | 1,137 |
| Hong Kong | 984 |
| Indonesia | 729 |

The most common URLs scanned:

| URL | Count |
| --- | --- |
| /geoserver/web/ | 37654 |
| /geoserver/web/wicket/bookmarkable/org.geoserver.web.AboutGeoServerPage?lang=en | 4811 |
| /geoserver/wms | 1651 |
| /geoserver | 1432 |
| /geoserver/web/wicket/bookmarkable/org.geoserver.web.AboutGeoServerPage | 333 |
| /geoserver/ | 37 |
| /geoserver/bad397/ | 37 |
| /geoserver/TestWfsPost | 26 |
| /geoserver/web/wicket/bookmarkable/org.geoserver.web.demo.MapPreviewPage | 25 |
| /geoserver/ows | 17 |

"/geoserver/web" is the default "Home Page" of GeoServer. "/geoserver/wms" URLs is what we have seen in the past. Current exploits for CVE-2024-36401 use "/geoserver/wfs". These URLs didn't make the top 10.

[1] https://isc.sans.edu/diary/Geoserver+Attack+Details+More+Cryptominers+against+Unconfigured+WebApps/29936
[2] https://isc.sans.edu/diary/Ongoing+scans+for+Geoserver/29926
[3] https://geoserver.org/
[4] https://medium.com/@knownsec404team/geoserver-sql-injection-vulnerability-analysis-cve-2023-25157-413c1f9818c3
[5] https://isc.sans.edu/api
[6] https://github.com/bigb0x/CVE-2024-36401/blob/main/cve-2024-36401.py

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords:

[0 comment(s)](/diary/A%2BSurvey%2Bof%2BScans%2Bfor%2BGeoServer%2BVulnerabilities/31148/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31144)
* [next](/diary/31150)

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