---
title: Scans for Solana (Surfpool&#x3f;) Endpoints, (Mon, Aug 10th)
url: https://isc.sans.edu/diary/rss/33230
source: SANS Internet Storm Center, InfoCON: green
date: 2026-08-10
fetch_date: 2026-08-11T03:31:59.347075
---

# Scans for Solana (Surfpool&#x3f;) Endpoints, (Mon, Aug 10th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/33226)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Scans for Solana (Surfpool?) Endpoints](/forums/diary/Scans%2Bfor%2BSolana%2BSurfpool%2BEndpoints/33230/)

**Published**: 2026-08-10. **Last Updated**: 2026-08-10 16:24:45 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Scans%2Bfor%2BSolana%2BSurfpool%2BEndpoints/33230/#comments)

Solana is a crypto platform known for speed. Developers like it to develop distributed applications or to implement crypto payments. To interact with the blockchain, APIs are provided for developers. These APIs will either "speak" JSON or gRPC. One implementation often used for development is "surfpool," which is used to test programs before deploying them to a Solana network.

The requests that we are observing right now look like:

> `POST /solana HTTP/1.1
> Host: [redacted]
> User-Agent: HelloScan/1.0
> Accept: */*
> Connection: keep-alive
> Content-Type: application/json
> Content-Length: 45`
>
> `{"jsonrpc":"2.0","id":1,"method":"getHealth"}`

A typical response from Surfpool to this request:

> `HTTP/1.1 200 OK
> content-type: application/json; charset=utf-8
> content-length: 39
> date: Mon, 10 Aug 2026 15:20:54 GMT`
>
> `{"jsonrpc":"2.0","result":"ok","id":1}`

A classical fingerprint request of someone attempting to enumerate Solana API endpoints. The "/solana" path is not required and should just be ignored. Usually, the API listens on port 8899, a port our honeypots are not listening on. The requests we are seeing are going to port 80. But they are likely assuming some form of proxy (for example an API gateway) that will map /solana to the backend API.

Other payloads that were used:

> `{"jsonrpc":"2.0","method":"eth_chainId","params":[],"id":1}
> ???????{"jsonrpc":"2.0","id":1,"method":"getVersion"}`

The same scanner hitting the "/solana" endpoint also scans for "/jsonrpc", "/rpc", "/v1" and '/' which could possibly be related. It also looks for a few URLs associated with credentials (for example,/.env, /.env.bak /.env.local, and others)

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords:

[0 comment(s)](/diary/Scans%2Bfor%2BSolana%2BSurfpool%2BEndpoints/33230/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/33226)

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