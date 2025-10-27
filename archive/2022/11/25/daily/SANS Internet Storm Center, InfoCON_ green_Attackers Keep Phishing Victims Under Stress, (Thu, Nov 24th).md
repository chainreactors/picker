---
title: Attackers Keep Phishing Victims Under Stress, (Thu, Nov 24th)
url: https://isc.sans.edu/diary/rss/29270
source: SANS Internet Storm Center, InfoCON: green
date: 2022-11-25
fetch_date: 2025-10-03T23:45:45.196143
---

# Attackers Keep Phishing Victims Under Stress, (Thu, Nov 24th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29268)
* [next](/diary/29272)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Attackers Keep Phishing Victims Under Stress](/forums/diary/Attackers%2BKeep%2BPhishing%2BVictims%2BUnder%2BStress/29270/)

**Published**: 2022-11-24. **Last Updated**: 2022-11-24 08:13:01 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Attackers%2BKeep%2BPhishing%2BVictims%2BUnder%2BStress/29270/#comments)

Phishing campaigns are very common today, we receive many phishing attempts per day. Why attackers are still flooding our mailboxes with such emails? Because it sill works, and the "return on investment" of sending millions is reached even if only a few victims are lured. However, attackers are always looking for new techniques to make people confident that the message is legit. Many phishing campaigns are pretty well prepared, and the fake mail you receive looks exactly like an official one. Multiple times, I was pretty close to click on a link... Yes, we are all poor humans!

Another technique used by attackers is to try to make the victim scared and increase stress. When we are under stress, we are prone to make wrong decisions! That's the technique used by a phishing campaign that I spotted yesterday.

If the victim follows the provided link, a message will ask the user to update his/her email account within 24h (a counter is running), but the funny fact is that the page displays a fake real-time list of disabled accounts. The list is generated with an HTML <marquee> tag:

```

<marquee align="center" style="height:120px; width:320px;" behavior="scroll" scrollamount="20" scrolldelay="0" direction="up">
<font face="arial" size="1" color="#FFF">
<font color="#67CC24">root@[email protected]</font>:~# deleting... estellita68@[email protected]... <br>
<font color="#67CC24">root@[email protected]</font>:~# deleting... an-rickard@[email protected]... <br>
<font color="#67CC24">root@[email protected]</font>:~# deleting... mainhouseantiqu@[email protected]... <br>
<font color="#67CC24">root@[email protected]</font>:~# deleting... gfyeatonantiques@[email protected]... <br>
<font color="#67CC24">root@[email protected]</font>:~# deleting... lizabelstreasure@[email protected]... <br>
... (Long list of fake email addresses) ...
</font>
</marquee>
```

Note that this tag is deprecated[[1](https://www.w3docs.com/learn-html/html-marquee-tag.html)] but is still supported by most browsers.

Here is how it looks:

![](https://isc.sans.edu/diaryimages/images/isc-20221124-1.gif)

If you are located in the United States, Happy Thanksgiving! But keep an eye on your systems because the long weekend (tomorrow is also Black Friday!) is a good opportunity for bad guys to launch waves of attacks...

[1] <https://www.w3docs.com/learn-html/html-marquee-tag.html>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Phishing](/tag.html?tag=Phishing) [Stress](/tag.html?tag=Stress)

[0 comment(s)](/diary/Attackers%2BKeep%2BPhishing%2BVictims%2BUnder%2BStress/29270/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/29268)
* [next](/diary/29272)

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