---
title: Tool updates: lots of security and logic fixes, (Mon, Mar 23rd)
url: https://isc.sans.edu/diary/rss/32820
source: SANS Internet Storm Center, InfoCON: green
date: 2026-03-23
fetch_date: 2026-03-24T04:18:04.210429
---

# Tool updates: lots of security and logic fixes, (Mon, Mar 23rd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jim Clausing](/handler_list.html#jim-clausing "Jim Clausing")

Threat Level: [green](/infocon.html)

* [previous](/diary/32816)

My next class:

|  |  |  |
| --- | --- | --- |
| [LINUX Incident Response and Threat Hunting](https://www.sans.org/event/security-west-2026/course/linux-threat-hunting-incident-response) | San Diego | May 11th - May 16th 2026 |

# [Tool updates: lots of security and logic fixes](/forums/diary/Tool%2Bupdates%2Blots%2Bof%2Bsecurity%2Band%2Blogic%2Bfixes/32820/)

**Published**: 2026-03-23. **Last Updated**: 2026-03-23 20:39:05 UTC
**by** [Jim Clausing](/handler_list.html#jim-clausing) (Version: 1)

[0 comment(s)](/diary/Tool%2Bupdates%2Blots%2Bof%2Bsecurity%2Band%2Blogic%2Bfixes/32820/#comments)

So, I've been slow to get on the Claude Code/OpenCode/Codex/OpenClaw bandwagon, but I had some time last week so I asked Claude to review (/security-review) some of my python scripts. He found more than I'd like to admit, so I checked in a bunch of updates. In reviewing his suggestions, he was right, I made some stupid mistakes, some of which have been sitting in there for a long time. It was nothing earth-shattering and it took almost no time for Claude, it took longer for me to read through the updates he wanted to make, figure out what he was seeing, and decide whether to accept them or tweak them. Here are a few of them.

* a logic inversion error with the -f switch, and some unhandled errors in convert-ts-bash-history.py
* a TOCTOU (time of check/time of use) possible race condition, and a comment about some ambiguity with the -c switch when deciding which hash was used based solely on the length of the hash in sigs.py
* some overly permissive permissions, a possible symlink attack, and an encoding issue in ficheck.py
* a possible header injection issue via the -s switch with mail\_stuff.py

Most of these are issues I should have caught myself given how long I've been programming/scripting, but all of these started out as quick and dirty scripts to solve a problem I had, and then I made them available to the public through my github repo without taking any time to really ensure they were ready for public consumption. Taking a few minutes to setup Claude without much in the way of guidance (my CLAUDE.md is still very much a work-in-progress) and the one in my my scripts repo was one I asked Claude to create for me after some back and forth during this review which mostly covers a couple of personal preferences.

I guess the main point is I'm late to the game on using AI on a daily basis, but that needs to change. Even when I'm feeling my age and write my own scripts, I need to have that second pair of *eyes* give it a second look. Some of these scripts run as root out of cron or systemd timers on systems I administer and some of those issues could have been used for privilege escalation by an attacker who managed to get access. Even those of us with more grey than not in our beards need to be spending some time figuring out how to integrate this stuff into our daily routine.

**References**:

[1] <https://github.com/clausing/scripts>

---------------
Jim Clausing, GIAC GSE #26
jclausing --at-- isc [dot] sans (dot) edu

Keywords: [tools](/tag.html?tag=tools)

[0 comment(s)](/diary/Tool%2Bupdates%2Blots%2Bof%2Bsecurity%2Band%2Blogic%2Bfixes/32820/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [LINUX Incident Response and Threat Hunting](https://www.sans.org/event/security-west-2026/course/linux-threat-hunting-incident-response) | San Diego | May 11th - May 16th 2026 |

* [previous](/diary/32816)

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