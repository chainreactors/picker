---
title: Experimental Suspicious Domain Feed, (Sun, Jul 13th)
url: https://isc.sans.edu/diary/rss/32102
source: SANS Internet Storm Center, InfoCON: green
date: 2025-07-14
fetch_date: 2025-10-06T23:24:15.932916
---

# Experimental Suspicious Domain Feed, (Sun, Jul 13th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32100)
* [next](/diary/32108)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Experimental Suspicious Domain Feed](/forums/diary/Experimental%2BSuspicious%2BDomain%2BFeed/32102/)

**Published**: 2025-07-13. **Last Updated**: 2025-07-13 23:33:36 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[3 comment(s)](/diary/Experimental%2BSuspicious%2BDomain%2BFeed/32102/#comments)

We have had a "newly registered domain" feed for a few years. This feed pulls data from ICANN's centralized zone data service ([https://czds.icann.org](https://czds.icann.org/home)) and TLS certificate transparency logs.

The ICANN CZDS is a good start, but it only offers data from top-level domains collaborating with ICANN. Missing are in particular country-level domains. Country-level zone files can be hard to come by, so we use TLS certificate transparency logs as a "cheap" alternative. Pretty much all domain registrars will, by default, create a "parked" website, and with that, they will make a certificate. Even if they do not, any halfway self-respecting phishing site will use TLS and register a certificate with a public certificate authority at one point. The TLS certificate transparency logs also help capture older domains.

Each day, we capture around 250,000 new domains using this system. But of course, we want to know which domains are used for malicious purposes. However, as the sample below shows, there are a lot of "odd" domain names.

| domainname |
| --- |
| jgcinversiones.com |
| h20manager.net |
| 1sbrfreebet.com |
| stability.now |
| mdskj.top |
| internationalone19.com |
| clistrict196.org |
| agenteinsider.com |
| 720airpano.com |
| dhofp.tax |
| bos228btts.lol |
| japansocialmarketing.org |
| mummyandimedia.com |
| 1dyzfd.buzz |
| oollm.shop |
| snapztrailk.store |
| perumice.com |
| nrnmy.sbs |
| commaexperts.com |
| softfragments.com |

So I searched for some commonly used criteria to identify "bad" domain names, and found these:

* A domain name is very short or very long
* The entropy of the domain name (is it just random characters?)
* Does it contain a lot of numbers or hyphens?
* Is it an international domain name, and if so, is it valid? Does it mix different scripts (=languages)?
* Does it contain keywords like "bank" or "login" that are often used with phishing sites, or brand names like "Apple" or "Google"?

We have now added a score to each domain name that can be used to rank them based on these criteria. You can find a daily report [here](https://isc.sans.edu/data/domains.html), and the score was added to our "recentdomain" API feed. This is experimental, and the exact algorithm we use for the score will change over time.

We used to have an "old" supicous domain feed that was mostly based on correlating a few third party feeds, but over time these feeds went away or became commercial and we could no longer use them.

Feedback is very welcome.

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [domains](/tag.html?tag=domains)

[3 comment(s)](/diary/Experimental%2BSuspicious%2BDomain%2BFeed/32102/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/32100)
* [next](/diary/32108)

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