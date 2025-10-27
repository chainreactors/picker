---
title: Hunting for Mastodon Servers, (Mon, Dec 19th)
url: https://isc.sans.edu/diary/rss/29358
source: SANS Internet Storm Center, InfoCON: green
date: 2022-12-20
fetch_date: 2025-10-04T02:01:14.210782
---

# Hunting for Mastodon Servers, (Mon, Dec 19th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29354)
* [next](/diary/29362)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Hunting for Mastodon Servers](/forums/diary/Hunting%2Bfor%2BMastodon%2BServers/29358/)

**Published**: 2022-12-19. **Last Updated**: 2022-12-19 10:02:29 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[1 comment(s)](/diary/Hunting%2Bfor%2BMastodon%2BServers/29358/#comments)

Since Elon Mush took control of Twitter, there has been considerable interest in alternative platforms to the micro-blogging network. Without certainty about Twitter's future, many people switched to the Mastodon[[1](https://joinmastodon.org/servers)] network. Most of the ISC Handlers are now present on this decentralized network. For example, I’m reachable via @[[email protected]](/cdn-cgi/l/email-protection)[[2](https://infosec.exchange/%40xme)]. You can find our addresses on the Contact page[[3](https://isc.sans.edu/handler_list.html)].

A new social network means that it could be interesting to track access to it from corporate networks and/or sensitive systems. If people are afraid about Twitter’s future, attackers too, and there are chances that we will see more and more C2 communications through Mastodon.

However, there is a significant difference with Twitter. Mastodon is a decentralized platform. Mastodon is a free software that allows you to run your instance of the social network. The server owner can join (or not) the federated social network to allow people from different servers to interact (hopefully!). So, someone using the server mastodon.nz will be able to discuss with me, using infosec.exchange.

The problem with this decentralized platform, the number of servers keeps growing, and there are many domain names to track to detect Mastodon traffic. Hopefully, it’s possible to generate the list of servers through an API call.

On instances.social, you can find a free API[[4](https://instances.social/api/doc/)] to query Mastodon servers. Once you created your account, you can easily extract the list of existing servers. The JSON output can be processed using jq to produce a simple list:

```

curl -s --header "Authorization: Bearer <redacted>" 'https://instances.social/api/1.0/instances/list?count=0' | \
jq ".instances[].name" | \
tr -d '"'
```

This command returned 16853 FQDN! Not all servers are active and online. For best results, it could be interesting to filter them out. If you add the filter 'include\_down=false', you will get 14824 hosts. Then, add the filter' include\_closed=false', and the count will drop to 7544. Once you have extracted the list of servers, it's easy to integrate them into your SOC feeds and use them in your hunting rules.

For your convenience, I uploaded a full list of servers on pastebin[[5](https://pastebin.com/ERuM4srn)].

[1] <https://joinmastodon.org/servers>
[2] [https://infosec.exchange/@xme](https://infosec.exchange/%40xme)
[3] <https://isc.sans.edu/handler_list.html>
[4] <https://instances.social/api/doc/>
[5] <https://pastebin.com/ERuM4srn>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Feed](/tag.html?tag=Feed) [Hunting](/tag.html?tag=Hunting) [Mastodon](/tag.html?tag=Mastodon) [Servers](/tag.html?tag=Servers) [API](/tag.html?tag=API) [SOC](/tag.html?tag=SOC)

[1 comment(s)](/diary/Hunting%2Bfor%2BMastodon%2BServers/29358/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/29354)
* [next](/diary/29362)

### Comments

Hi.
The Pastebin link returns the following: "Error, this is a private paste or is pending moderation. If this paste belongs to you, please login to Pastebin to view it."

#### Garibaldi

#### Dec 20th 2022 2 years ago

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