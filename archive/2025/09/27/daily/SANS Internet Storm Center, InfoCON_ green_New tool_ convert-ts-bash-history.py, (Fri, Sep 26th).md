---
title: New tool: convert-ts-bash-history.py, (Fri, Sep 26th)
url: https://isc.sans.edu/diary/rss/32324
source: SANS Internet Storm Center, InfoCON: green
date: 2025-09-27
fetch_date: 2025-10-02T20:47:45.763355
---

# New tool: convert-ts-bash-history.py, (Fri, Sep 26th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jesse La Grew](/handler_list.html#jesse-la-grew "Jesse La Grew")

Threat Level: [green](/infocon.html)

* [previous](/diary/32320)
* [next](/diary/32328)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Malware Analysis Tools and Techniques](https://www.sans.org/event/tokyo-autumn-2025/course/reverse-engineering-malware-malware-analysis-tools-techniques) | Online | Japan Standard Time | Oct 20th - Oct 25th 2025 |

# [New tool: convert-ts-bash-history.py](/forums/diary/New%2Btool%2Bconverttsbashhistorypy/32324/)

**Published**: 2025-09-26. **Last Updated**: 2025-09-26 22:26:21 UTC
**by** [Jim Clausing](/handler_list.html#jim-clausing) (Version: 1)

[0 comment(s)](/diary/New%2Btool%2Bconverttsbashhistorypy/32324/#comments)

In [SANS FOR577](https://www.sans.org/cyber-security-courses/linux-threat-hunting-incident-response)[1], we talk about timelines on day 5, both filesystem and super-timelines. but sometimes, I want something quick and dirty and rather than fire up plaso, just to create a timeline of .bash\_history data, it is nice to just be able to parse them and, if timestamps are enabled, see them in a human-readable form. I've had some students in class write scripts to do this and even had one promise to share it with me after class, but I never ended up getting it so I decided to write my own. This script takes the path to 1 or more .bash\_history files and returns a PSV (pipe separated values) list (on stdout) in the form: `<filename>|<datetime>|<command>` where the <datetime> is in ISO-8601 format (the one true date time format, but only to 1 sec resolution since that his the best that the .bash\_history file will give us). In a future version I will probably offer an option to change from PSV to CSV.

One of the ways I have used it is by piping the output through sort, in particular `| sort -t '|' -k 2` to take a bunch of bash history files and sort them in time order. I've gone back and forth on whether or not to swap the first 2 columns, but since I encounter so many more history files without timestamps than with, having the path to the particular file that contains the command first has been quite useful. I might also add a switch to leave the file path off. I welcome comments/thoughts from others out there who might use it. There is a reason that this is v0.9, not yet v1.0.

The script (as seen in the title) is called [convert-ts-bash-history.py](https://github.com/clausing/scripts/blob/master/convert-ts-bash-history.py)[2], and here are a couple of screenshots to show its usage. You can find it in my github [scripts repo](https://github.com/clausing/scripts)[3].

![usage info](https://isc.sans.edu/diaryimages/images/2025-09-26%2016_36_19-leibnitz-nat%20-%20SecureCRT.png)

And, the following 2 show the bash history before and after I turned on timestamps

![screenshot of script run on bash history without timestamps](https://isc.sans.edu/diaryimages/images/2025-09-26%2016_32_44-leibnitz-nat%20-%20SecureCRT.png)

and

![screenshot of tool run against bash history file with timestamps enabled](https://isc.sans.edu/diaryimages/images/2025-09-26%2016_33_27-leibnitz-nat%20-%20SecureCRT.png)

Finally, a reminder, as we point out in class, the bash history files are written when the shell exits, so if you are grabbing a triage on a live system and a shell is still open, the history will only be in memory, not on the disk (yet). If you want to learn more about Linux incident response and forensics, I'm teaching FOR577 one more time this year at one of my favorite conferences, [SANS DFIRCON](https://www.sans.org/cyber-security-training-events/dfircon-miami-2025)[4] in Miami in Nov, I'd love to see you there.

### References:

[1] <https://www.sans.org/cyber-security-courses/linux-threat-hunting-incident-response>

[2] <https://github.com/clausing/scripts/blob/master/convert-ts-bash-history.py>

[3] <https://github.com/clausing/scripts>

[4] <https://www.sans.org/cyber-security-training-events/dfircon-miami-2025>

---------------
Jim Clausing, GIAC GSE #26
jclausing --at-- isc [dot] sans (dot) edu

Keywords: [bash](/tag.html?tag=bash) [timeline](/tag.html?tag=timeline) [tool](/tag.html?tag=tool)

[0 comment(s)](/diary/New%2Btool%2Bconverttsbashhistorypy/32324/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Malware Analysis Tools and Techniques](https://www.sans.org/event/tokyo-autumn-2025/course/reverse-engineering-malware-malware-analysis-tools-techniques) | Online | Japan Standard Time | Oct 20th - Oct 25th 2025 |

* [previous](/diary/32320)
* [next](/diary/32328)

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