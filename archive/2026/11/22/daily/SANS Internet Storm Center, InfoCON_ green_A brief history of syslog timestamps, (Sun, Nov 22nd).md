---
title: A brief history of syslog timestamps, (Sun, Nov 22nd)
url: https://isc.sans.edu/diary/rss/33530
source: SANS Internet Storm Center, InfoCON: green
date: 2026-11-22
fetch_date: 2026-11-23T10:02:57.272498
---

# A brief history of syslog timestamps, (Sun, Nov 22nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jim Clausing](/handler_list.html#jim-clausing "Jim Clausing")

Threat Level: [green](/infocon.html)

* [previous](/diary/33526)
* [next](/diary/33532)

Click [HERE](https://www.sans.org/profiles/jim-clausing) to learn more about classes Jim is teaching for SANS

# [A brief history of syslog timestamps](/forums/diary/A%2Bbrief%2Bhistory%2Bof%2Bsyslog%2Btimestamps/33530/)

**Published**: 2026-11-22. **Last Updated**: 2026-11-22 18:40:18 UTC
**by** [Jim Clausing](/handler_list.html#jim-clausing) (Version: 1)

[0 comment(s)](/diary/A%2Bbrief%2Bhistory%2Bof%2Bsyslog%2Btimestamps/33530/#comments)

BLUF: Debian and Ubuntu dropped a config directive in the rsyslogd package in early 2023.

As any of my FOR577 students will tell you, I'm a fan of ISO-8601 (ok, RFC 3339, too, see below). They'll probably also tell you I'm a firm believer in UTC||GTFO especially on servers (also true, and I've made stickers to prove it). I was also asked recently why the syslog timestamps in newer Ubuntu and Debian systems changed to ISO-8601 (well, probably actually RFC 3339, but I won't got down that rabbithole in this handler's diary) timestamps from the historical `Mmm dd hh:mm:ss` format we've known since the 1980s. I had noticed the same, a few years ago, but never really paid attention to it. Given the question from a student, I decided to do a little research on the subject and this diary is the result.

To back up some, the syslog protocol and syslogd were originally the creation of Eric Allman in 1983 because he needed a way to debug sendmail[[1](https://blog.runreveal.com/the-history-of-centralized-logging/)]. They became part of BSD 4.2 that same year. BSD 4.2 also happened to be my introduction to Unix in 1983. Syslog then made it into AT&T's System V Unix in about 1989 in SVR4 (System V Release 4) through an effort by AT&T and Sun Microsystems to try to merge the features of the 2 major branches of Unix at the time. System V adopted the protocol and routing interfaces but built the daemon on top of System V internals.

The first effort to develop the protocol into an actual standard was an IETF draft in Oct 2000 that evolved into RFC 3164[[2](https://www.rfc-editor.org/info/rfc3164/#section-4)] in 2001, by which time the protocol was actually already 18 years old. This is the syslog message format we've all come to know so well over the years. Meanwhile, around 2005, rsyslogd added the option of outputing RFC 3339 timestamps. In 2009, RFC 3164 was superceded by RFC 5424[[3](https://www.rfc-editor.org/info/rfc5424/#section-6.2.3)] which defined the timestamp to be of the format `YYYY-MM-DDThh:mm:ss[.ssssss]Z` or `YYYY-MM-DDThh:mm:ss[.ssssss](+/-)hh:mm`. Despite the new RFC, the default setting even for rsyslogd in most Linux distros continued to be to write messages to the log files in the older format (referred to as the BSD format, as specified in the title of RFC 3164), by setting a directive in `/etc/rsyslog.conf` (the `RSYSLOG_TraditionalFileFormat` directive).

That brings us to 2023, with the release of Debian 12 (Bookworm) and Ubuntu 23.04 (not a LTS release) both distros stopped installing rsyslogd by default and defaulted to the systemd journal for logging and removed the directive from the default config file for those who did install it.. Many system administrators continue to install rsyslogd because they had infrastructure in place for forwarding syslog to central log servers and/or SIEMs. These are the folks most likely to have noticed the format change. Meanwhile, Fedora and Alma (and presumably the rest of the RedHat family) have left the directive in place when the package is installed.

From a Ubuntu 24.04 system:

![](https://isc.sans.edu/diaryimages/images/2026-11-20%2013_15_59-leibnitz-ovpn%20-%20SecureCRT.png)From a Fedora 44 system:

![](https://isc.sans.edu/diaryimages/images/2026-11-20%2013_19_21-leibnitz-ovpn%20-%20SecureCRT.png)

Meanwhile you can get either one with `journalctl` by setting the output format to either `short` (BSD format) or `short-iso-precise` (ISO format).

![](https://isc.sans.edu/diaryimages/images/2026-11-23%2002_23_10-leibnitz-ts%20-%20SecureCRT.png)

Also, note that rsyslogd is not the only option for a syslog server. I've been using syslog-ng as the syslog server on my home log collector since about 2000. In syslog-ng, the new 'ISO' timestamps can be enabled by setting the following two options in syslog-ng.conf: `ts-format(iso)` and `frac-digits(6)`. Since I have just been upgrading my central log server for years, I haven't done a fresh install lately, so I'm not sure if that is the default. I had to explicitly add it to my config.

References:

1. [The History of Centralized Logging](https://blog.runreveal.com/the-history-of-centralized-logging/)

2. [RFC 3164: The BSD Syslog Protocol](https://www.rfc-editor.org/info/rfc3164/#section-4)

3. [RFC 5424: The Syslog Protocol](https://www.rfc-editor.org/info/rfc5424/#section-6.2.3)

---------------
Jim Clausing, GIAC GSE #26
jclausing --at-- isc [dot] sans (dot) edu

Keywords: [Timestamp](/tag.html?tag=Timestamp) [syslog](/tag.html?tag=syslog)

[0 comment(s)](/diary/A%2Bbrief%2Bhistory%2Bof%2Bsyslog%2Btimestamps/33530/#comments)

Click [HERE](https://www.sans.org/profiles/jim-clausing) to learn more about classes Jim is teaching for SANS

* [previous](/diary/33526)
* [next](/diary/33532)

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