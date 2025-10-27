---
title: New Tool: ficheck.py, (Thu, Jul 24th)
url: https://isc.sans.edu/diary/rss/32136
source: SANS Internet Storm Center, InfoCON: green
date: 2025-07-25
fetch_date: 2025-10-06T23:52:12.669264
---

# New Tool: ficheck.py, (Thu, Jul 24th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32130)
* [next](/diary/32138)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Malware Analysis Tools and Techniques](https://www.sans.org/event/tokyo-autumn-2025/course/reverse-engineering-malware-malware-analysis-tools-techniques) | Online | Japan Standard Time | Oct 20th - Oct 25th 2025 |

# [New Tool: ficheck.py](/forums/diary/New%2BTool%2Bficheckpy/32136/)

**Published**: 2025-07-24. **Last Updated**: 2025-07-24 03:07:53 UTC
**by** [Jim Clausing](/handler_list.html#jim-clausing) (Version: 1)

[0 comment(s)](/diary/New%2BTool%2Bficheckpy/32136/#comments)

As I mention every time I teach [FOR577](https://www.sans.org/cyber-security-courses/linux-threat-hunting-incident-response), I have been a big fan of file integrity monitoring tools (FIM) since Gene Kim first released Tripwire well over 30 years ago. I've used quite a few of them over the years including tripwire, OSSEC, samhain, and aide, just to name a few. For many years, I used the fcheck Perl script (by Michael A. Gumienny) that was available as an apt package on Ubuntu because it was lightning fast. Unfortunately, sometime between Ubuntu 16.04 and Ubuntu 20.04 (my memory fails me as to exactly when), it slowed down on many of the systems I managed to the point where instead of being able to run it 4-6 times a day, it would now sometimes take more than 24 hours to run. And that was just running it on select directories, not the entire system, the way I run tools like aide. Though I started writing Perl scripts in 1989, I didn't spend any time trying to figure out why fcheck was suddenly having so many issues. I let it go for quite a while, but a few months ago, I started thinking about it again and decided I'd write a look-alike in python. What I'm releasing today is not quite complete, hence the 0.9.0 version number, but I've been using it an about a dozen systems (Debian and Ubuntu, though it shoud run just fine on any Linux with Python 3.9 or newer, probably older, too, but I again haven't tried it on anything older) for about 6 months. I still want to add a couple of things including the ability to include additional config files like the .local.cfg that fcheck had, rather than having to put all the additions into the primary config.

I've named my tool ficheck.py[1] (**F**ile **I**ntegrity **CHECK**) since I didn't want to step on Mr. Gumienny's tool name, but I freely admit this is an homage to his tool that I really liked and used for years. I stole his config file and report formats. The script runs in under 90 seconds on all the systems I've been testing on including some large systems in public cloud and some very small memory VMs. I am also releasing a quick and dirty install script that will install a basic config, install a cron job to run it every 2 hours, and another of my scripts, mail\_stuff.py[[2](https://github.com/clausing/scripts/blob/master/mail_stuff.py)] which will use mailx to send e-mail if it gets any ASCII (or UTF-8) bytes on stdin. Everything needed to install is in my scripts github repo[[3](https://github.com/clausing/scripts/tree/master)]. The tool monitors for file creation and deletion, and inode number change (meaning a new file with same name), plus changes to file size, number of links, ownership, group, permissions, SHA2-256 hash (on files less than 500M, configurable witha  commandline switch), file modification time (MTime), file metadata (inode) change time (CTime), and, if the pystatx module is installed (as described in my [mac\_robber.py update diary](https://isc.sans.edu/diary/31310) last year), file creation time (BTime).

The directories I generally watch are ones where I don't expect a lot of changes unless I'm applying patches. I do tune it to remove some files that get modified regularly during normal operations. I also have added some places (like /dev/shm) where attackers sometimes try to hide their malware. Here is a screenshot of the e-mail received when there are changes found. ![](https://isc.sans.edu/diaryimages/images/Screenshot%202025-07-23%20at%2014_16_50.png)

Check it out. If you run into any problems or have suggestions for improvements, e-mail me at the address below or on the handlers list or open an issue on github.

### References:

1. <https://github.com/clausing/scripts/blob/master/ficheck.py>
2. <https://github.com/clausing/scripts/blob/master/mail_stuff.py>
3. <https://github.com/clausing/scripts/tree/master>

---------------
Jim Clausing, GIAC GSE #26
jclausing --at-- isc [dot] sans (dot) edu

Keywords: [file integrity monitoring](/tag.html?tag=file integrity monitoring)

[0 comment(s)](/diary/New%2BTool%2Bficheckpy/32136/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Malware Analysis Tools and Techniques](https://www.sans.org/event/tokyo-autumn-2025/course/reverse-engineering-malware-malware-analysis-tools-techniques) | Online | Japan Standard Time | Oct 20th - Oct 25th 2025 |

* [previous](/diary/32130)
* [next](/diary/32138)

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