---
title: No Internet Access&#x3f; SSH to the Rescue&#x21;, (Thu, May 8th)
url: https://isc.sans.edu/diary/rss/31932
source: SANS Internet Storm Center, InfoCON: green
date: 2025-05-09
fetch_date: 2025-10-06T22:30:10.938106
---

# No Internet Access&#x3f; SSH to the Rescue&#x21;, (Thu, May 8th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31928)
* [next](/diary/31940)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [No Internet Access? SSH to the Rescue!](/forums/diary/No%2BInternet%2BAccess%2BSSH%2Bto%2Bthe%2BRescue/31932/)

**Published**: 2025-05-08. **Last Updated**: 2025-05-08 13:08:13 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/No%2BInternet%2BAccess%2BSSH%2Bto%2Bthe%2BRescue/31932/#comments)

This quick diary is a perfect example of why I love Linux (or UNIX in general) operating system. There is always a way to "escape" settings imposed by an admin...

Disclaimer: This has been used for testing purpose in the scope of a security assessment project. Don't break your organization security policies!

To perform some assessments on a remote network, a Customer provided me a VM running Ubuntu and reachable through SSH (with IP filtering, only SSH key authentication, etc). Once logged on the system, I started to work but I was lacking of some tools and decided to install them. Bad news... The VM had no Internet access. No problem, we have an SSH access!

Let's assume the following enrivonment:

* server.acme.org is the VM. SSH listening on port 65022.
* client.sans.edu is my workstation with SSH listening on port 22.

![](https://isc.sans.edu/diaryimages/images/isc-20250508-1.png)

Step 1: From client.sans.edu, connect to the server via one terminal and create a reverse tunnel ("-R" option)

```

ssh -p 65022 -i .ssh/privatekey -R 2222:localhost:22 [email protected]
```

Step 2: Start a second session to the server, from a second terminal

```

ssh -p 65022 -i .ssh/privatekey [email protected]
```

Step 3: From the second session, connect back to the client and setup a dynamic port forwaring ("-D")

```

ssh -p 2222 -D 1080 xavier@localhost
```

Step 4: From the fist session, create environment variables:

```

export http_proxy=socks5h://127.0.0.1:1080
export https_proxy=socks5h://127.0.0.1:1080
curl https://ipinfo.io/
```

Curl should tell you that your IP address is the one of client.sans.edu!

Now, all tools handling these variables will have access to the Interneet through your client! Slow but effective!

They are for sure many other ways to achieve this but... that's the magic of UNIX, always plenty of way to solve issues... Please share your idea or techiques!

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Proxy](/tag.html?tag=Proxy) [SSH](/tag.html?tag=SSH) [Tunnel](/tag.html?tag=Tunnel) [SOCKS](/tag.html?tag=SOCKS) [Internet Access](/tag.html?tag=Internet Access) [Linux](/tag.html?tag=Linux)

[0 comment(s)](/diary/No%2BInternet%2BAccess%2BSSH%2Bto%2Bthe%2BRescue/31932/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/31928)
* [next](/diary/31940)

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