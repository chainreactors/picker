---
title: It isn't always defaults: Scans for 3CX usernames, (Mon, Nov 10th)
url: https://isc.sans.edu/diary/rss/32464
source: SANS Internet Storm Center, InfoCON: green
date: 2025-11-10
fetch_date: 2025-11-11T03:14:26.788603
---

# It isn't always defaults: Scans for 3CX usernames, (Mon, Nov 10th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32460)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [It isn't always defaults: Scans for 3CX usernames](/forums/diary/It%2Bisnt%2Balways%2Bdefaults%2BScans%2Bfor%2B3CX%2Busernames/32464/)

**Published**: 2025-11-10. **Last Updated**: 2025-11-10 15:23:31 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[2 comment(s)](/diary/It%2Bisnt%2Balways%2Bdefaults%2BScans%2Bfor%2B3CX%2Busernames/32464/#comments)

Today, I noticed scans using the username "FTP\_3cx" showing up in our logs. 3CX is a well-known maker of business phone system software [1]. My first guess was that this was a default user for one of their systems. But Google came up empty for this particular string. The 3CX software does not appear to run an FTP server, but it offers a feature to back up configurations to an FTP server [2]. The example user used in the documentation is "3cxftpuser", not "FTP\_3cx". Additionally, the documentation notes that the FTP server can run on a different system from the 3CX software. For a backup, it would not make much sense to have it all run on the same system.

The scans we are seeing likely target FTP servers users set up to back up 3CX configurations, and not the 3CX software itself. I am not familiar enough with 3CX to know precisely what the backup contains, but it most likely includes sufficient information to breach the 3CX installation.

The credentials we observe with our Cowrie-based honeypots are collected for telnet and ftp. In particular, on Linux systems, you often use a system user to connect via FTP. Any credentials working via FTP will also work for telnet or SSH. Keep that in mind when configuring a user for FTP access, and of course, FTP should not be your first choice for backing up sensitive data, but we all know it does happen.

Here are the passwords attacks are attempting to use:

| Password | Count |
| --- | --- |
| 3CXBackup | 4 |
| 3CXbackups | 4 |
| telecom | 1 |
| testbackup | 1 |
| backup3cx | 1 |
| ebsftpuser | 1 |
| ftp\_cxn | 1 |
| ftp\_inx | 1 |

Here are some other "3cx" related usernames we have seen in the past:

| Username |
| --- |
| 3cx |
| 3CXBackup |
| 3cxbackups |
| backup3cx |
| ftp3cx |
| FTP\_3cx |

If anyone with more 3CX experience reads this, is there a reason for someone to use these usernames? Or are there any defaults I didn't find?

[1] https://www.3cx.com
[2] https://www.3cx.com/docs/ftp-server-pbx-backups-linux/

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [3cx](/tag.html?tag=3cx)

[2 comment(s)](/diary/It%2Bisnt%2Balways%2Bdefaults%2BScans%2Bfor%2B3CX%2Busernames/32464/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/32460)

### Comments

I have used 3CX for many years. I think the names you mention are a simple product of human nature.

If using Veeam, I see veeambak or veeambackup, and Proxmox proxmoxbak, etc.

I just see these names as commonly selected, and I confess used by me too. But I my case never publicly accessible.

#### Steven

#### Nov 10th 2025 5 hours ago

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