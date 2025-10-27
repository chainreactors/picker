---
title: The strange case of disappearing Russian servers, (Mon, Nov 25th)
url: https://isc.sans.edu/diary/rss/31476
source: SANS Internet Storm Center, InfoCON: green
date: 2024-11-26
fetch_date: 2025-10-06T19:23:01.323251
---

# The strange case of disappearing Russian servers, (Mon, Nov 25th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31474)
* [next](/diary/31480)

# [The strange case of disappearing Russian servers](/forums/diary/The%2Bstrange%2Bcase%2Bof%2Bdisappearing%2BRussian%2Bservers/31476/)

**Published**: 2024-11-25. **Last Updated**: 2024-11-25 13:34:45 UTC
**by** [Jan Kopriva](/handler_list.html#jan-kopriva) (Version: 1)

[0 comment(s)](/diary/The%2Bstrange%2Bcase%2Bof%2Bdisappearing%2BRussian%2Bservers/31476/#comments)

Few months ago, I noticed that something strange was happening with the number of servers seen by Shodan in Russia...

In order to identify any unusual changes on the internet that might be worth a closer look, I have put together a simple script few years ago. It periodically goes over data that was gathered from the Shodan search engine by my TriOp tool[[1](https://isc.sans.edu/diary/27034)], and looks for significant changes in the number of public IP addresses with various services enabled on them. This script alerts me any time there seems to be something unusual – i.e., if Shodan detects more than a 10 % increase in the number of HTTPS servers during the course of a week, or if there is more than a 20 % decrease in the number of e-mail servers in a specific country in the course of a month.

Around the beginning of August, the script started alerting me to a decrease in the number of basically all types of servers that Shodan detected in Russia.

Since internet-wide scanning and service identification that is performed by Shodan, Censys and similar search engines, is hardly an exact science, the number of systems that they detect can oscillate significantly in the short term, and a single alert by my script therefore seldom means that a real change is occurring. Nevertheless, the alerts kept coming for multiple days and weeks in a row, and so I decided to take a closer look at the underlying data… And, indeed, from the point of view of Shodan, it looked as if significant portions of the Russian internet were disappearing.

My theory was that it might have been caused by introduction of some new functionality into the internet filtering technology that is used by Russia in order to censor internet traffic and block access to various external services[[2](https://en.wikipedia.org/wiki/Internet_censorship_in_Russia)], which started interfering with Shodan probes. And while I still believe that this might be the case, looking at the data now, when the number of Russian servers has been more or less stable for about 6 weeks, it seems that the cause for the decrease was at least partially different.

[![](https://isc.sans.edu/diaryimages/images/24-11-25-russia.png)](https://isc.sans.edu/diaryimages/images/24-11-25-russia.png)

Although it is true that the decrease was spread over basically all types of services and ports (i.e., there was a significant drop in the number of accessible HTTP/S servers, SSH servers, DNS servers etc.), and some overall filtering affecting Shodan therefore seems to be in place, there was one port on which the drop was much more significant than on any of the others.

That port was TCP/7547[[3](https://trends.shodan.io/search?query=country%3A%22RU%22#facet/port)].

[![](https://isc.sans.edu/diaryimages/images/24-11-25-ports.png)](https://isc.sans.edu/diaryimages/images/24-11-25-ports.png)

The aforementioned port is associated with the CPE WAN Management Protocol (CWMP), which is sometimes also called TR-069[[4](https://en.wikipedia.org/wiki/TR-069)]. The CWMP is a HTTP-based protocol, which enables ISPs to perform remote management and provisioning of routers and other devices that offer their clients direct access to the internet (e.g., SOHO routers that are provided to customers by ISPs).

This protocol is used by many ISPs around the world, and although it has not always been implemented securely and some vulnerable implementations of it (well, mostly of it and TR-064) have been historically used in successful attacks[[5](https://censys.com/the-most-common-protocol-youve-never-heard-of/)], it is – in general – considered secure.

Nevertheless, it seems that Russian ISPs either suddenly decided to stop using it, or – much more likely – decided to severely limit access to the corresponding port. This was most significantly visible in IP ranges that are part of AS12389, which is assigned to the national Russian ISP, Rostelecom[[6](https://trends.shodan.io/search?query=ASN%3AAS12389#facet/port),[7](https://ipinfo.io/AS12389)].

[![](https://isc.sans.edu/diaryimages/images/24-11-25-as.png)](https://isc.sans.edu/diaryimages/images/24-11-25-as.png)

While CWMP accounts for significant portion of the overall decrease in the number of Russian servers seen by Shodan, it is far from being its only cause, as we can see from the second chart.

And since it is unlikely that large amounts of servers of various types would have been suddenly removed from the internet, it is much more likely that Shodan has lost some visibility into Russian IP space in the past few months due to some increase in filtering of network traffic. In any case, it will certainly be interesting to see how things develop in the future… Especially given the continued Russian attempts at creating a “sovereign internet”[[8](https://www.scientificamerican.com/article/russia-is-trying-to-leave-the-internet-and-build-its-own/)].

[1] <https://isc.sans.edu/diary/27034>
[2] <https://en.wikipedia.org/wiki/Internet_censorship_in_Russia>
[3] <https://trends.shodan.io/search?query=country%3A%22RU%22#facet/port>
[4] <https://en.wikipedia.org/wiki/TR-069>
[5] <https://censys.com/the-most-common-protocol-youve-never-heard-of/>
[6] <https://trends.shodan.io/search?query=ASN%3AAS12389#facet/port>
[7] <https://ipinfo.io/AS12389>
[8] <https://www.scientificamerican.com/article/russia-is-trying-to-leave-the-internet-and-build-its-own/>

-----------
Jan Kopriva
[@jk0pr](https://twitter.com/jk0pr) | [LinkedIn](https://www.linkedin.com/in/jan-kopriva/)
[Nettles Consulting](https://www.nettles.cz/)

Keywords:

[0 comment(s)](/diary/The%2Bstrange%2Bcase%2Bof%2Bdisappearing%2BRussian%2Bservers/31476/#comments)

* [previous](/diary/31474)
* [next](/diary/31480)

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