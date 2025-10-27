---
title: Increased Elasticsearch Recognizance Scans, (Tue, Aug 19th)
url: https://isc.sans.edu/diary/rss/32212
source: SANS Internet Storm Center, InfoCON: green
date: 2025-08-20
fetch_date: 2025-10-07T00:50:23.537985
---

# Increased Elasticsearch Recognizance Scans, (Tue, Aug 19th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32208)
* [next](/diary/32216)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Increased Elasticsearch Recognizance Scans](/forums/diary/Increased%2BElasticsearch%2BRecognizance%2BScans/32212/)

**Published**: 2025-08-19. **Last Updated**: 2025-08-19 18:16:29 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Increased%2BElasticsearch%2BRecognizance%2BScans/32212/#comments)

I noticed an increase in scans that appear to try to identify Elasticsearch instances. Elasticsearch is not a new target. Its ability to easily store and manage JSON data, combined with a simple HTTP API, makes it a convenient tool to store data that is directly accessible from the browser via JavaScript. Elasticsearch has, in particular, been popular for consolidating log data, and the "ELK" (Elasticsearch, Logstash, Kibana) platform has been a very successful standard for open source log management.

Call me old fashioned, but the idea of exposing my database directly to the user has always been a bit "frightening" to me. But the kids like to do dangerous things, and as a result we have plenty of exposed Elasticsearch instances. No surprise that attackers are looking for them.

The particular query I have been seeing these last couple days is "/\_cluster/settings ". Running this against my own Elasticsearch instance:

> $ curl -isku $ELASTIC\_USERNAME:$ELASTIC\_PASSWORD https://localhost:9200/\_cluster/settings/
> HTTP/1.1 200 OK
> X-elastic-product: Elasticsearch
> content-type: application/json
> content-length: 32
>
> {"persistent":{},"transient":{}}

does not really retrieve any concerning details, but it easily proves that we have a running Elasticsearch instance.

Without authentication, a 401 error is returned, but again, there are no details about what version I am running. It is, however, possible that the formatting or the details of the error message can be used for fingerprinting.

> `curl -isk https://localhost:9200/_cluster/settings/
> HTTP/1.1 401 Unauthorized
> WWW-Authenticate: Basic realm="security", charset="UTF-8"
> WWW-Authenticate: Bearer realm="security"
> WWW-Authenticate: ApiKey
> content-type: application/json
> content-length: 497`
>
> `{"error":{"root_cause":[{"type":"security_exception","reason":"missing authentication credentials for REST request [/_cluster/settings/]","header":{"WWW-Authenticate":["Basic realm=\"security\", charset=\"UTF-8\"","Bearer realm=\"security\"","ApiKey"]}}],"type":"security_exception","reason":"missing authentication credentials for REST request [/_cluster/settings/]","header":{"WWW-Authenticate":["Basic realm=\"security\", charset=\"UTF-8\"","Bearer realm=\"security\"","ApiKey"]}},"status":401}`

My best guess is that this actor is just looking for possible instances of Elasticsearch to come back later for details. Elasticsearch is always somewhat scanned for, but the request for /\_cluster/settings/ is new. The graph below compares all requests for Elasticsearch with requests for /\_clustser/settings

![graph of elasticsearch related requests over the last 30 days](https://isc.sans.edu/diaryimages/images/Screenshot%202025-08-19%20at%202_10_48%E2%80%AFPM.png)

This weekend, a blog post by cyberNK regarding an "Elastic EDR Zero-Day" made headlines [1]. I do not think these requests are related, and Elastic disputed the blog post [2].

[1] https://infosecilluminati.medium.com/elastic-edr-zero-day-bypass-detection-execute-malware-and-trigger-bsod-what-happened-and-how-to-363ca11062b9
[2] https://discuss.elastic.co/t/elastic-response-to-blog-edr-0-day-vulnerability/381093

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [elasticsearch](/tag.html?tag=elasticsearch)

[0 comment(s)](/diary/Increased%2BElasticsearch%2BRecognizance%2BScans/32212/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/32208)
* [next](/diary/32216)

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