---
title: Detecting and Monitoring OpenClaw (clawdbot, moltbot), (Tue, Feb 3rd)
url: https://isc.sans.edu/diary/rss/32678
source: SANS Internet Storm Center, InfoCON: green
date: 2026-02-03
fetch_date: 2026-02-04T04:08:21.721105
---

# Detecting and Monitoring OpenClaw (clawdbot, moltbot), (Tue, Feb 3rd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32674)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/sans-2026/course/application-security-securing-web-apps-api-microservices) | Orlando | Mar 29th - Apr 3rd 2026 |

# [Detecting and Monitoring OpenClaw (clawdbot, moltbot)](/forums/diary/Detecting%2Band%2BMonitoring%2BOpenClaw%2Bclawdbot%2Bmoltbot/32678/)

**Published**: 2026-02-03. **Last Updated**: 2026-02-03 12:41:53 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[2 comment(s)](/diary/Detecting%2Band%2BMonitoring%2BOpenClaw%2Bclawdbot%2Bmoltbot/32678/#comments)

Last week, a new AI agent framework was introduced to automate "live". It targets office work in particular, focusing on messaging and interacting with systems. The tool has gone viral not so much because of its features, which are similar to those of other agent frameworks, but because of a stream of security oversights in its design.

If you are looking to detect the use of OpenClaw in your environment, Knostic has created scripts to detect It, and, if you do want to use OpenClaw, to collect telemetry about its use.

### openclaw-detect <https://github.com/knostic/openclaw-detect>

This script searches the system for filenames commonly associated with OpenClaw. For example, the presence of the state directory ~/.openclaw or for a Docker container running openclaw. If you have decent endpoint monitoring, this tool may not be needed, but it can give you some hints on which files to look for.

### openclaw-telemetry <https://github.com/knostic/openclaw-telemetry>

If you do run OpenClaw, openclaw-detect will add additional meaningful logging. The tool captures "every tool call, LLM request, and agent session — with built-in redaction, tamper-proof hash chains, syslog/SIEM forwarding, and rate limiting". It is an OpenClaw plugin and installs like any other OpenClaw plugin

In addition, there are a few additional security tools and tips:

* The OpenClaw documentation now has a dedicated security section: <https://docs.openclaw.ai/gateway/security>
* OpenClaw's documentation explains how to set up OpenClaw inside a Docker sandbox: <https://docs.openclaw.ai/cli/sandbox>.
* Do not provide OpenClaw with access to accounts you intend to lose.
* Do not expose OpenClaw to the Internet
* ACIP, the "Advanced Cognitive Inoculation Prompt", has a version for OpenClaw that intends to limit prompt injection. <https://github.com/Dicklesworthstone/acip/tree/main/integrations/clawdbot>

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [OpenClaw](/tag.html?tag=OpenClaw)

[2 comment(s)](/diary/Detecting%2Band%2BMonitoring%2BOpenClaw%2Bclawdbot%2Bmoltbot/32678/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/sans-2026/course/application-security-securing-web-apps-api-microservices) | Orlando | Mar 29th - Apr 3rd 2026 |

* [previous](/diary/32674)

### Comments

Is it possible to detect this on the network?

#### AT

#### Feb 3rd 2026 13 hours ago

no. At least not easily. There is no central 'hub' OpenClaw connects to. It just connects to the configured services and possibly to various online models. Will try to work on a way to identify it on the network, but I doubt it will work too well without TLS interception.

#### Johannes

#### Feb 3rd 2026 6 hours ago

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