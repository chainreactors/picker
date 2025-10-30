---
title: How to collect memory-only filesystems on Linux systems, (Wed, Oct 29th)
url: https://isc.sans.edu/diary/rss/32432
source: SANS Internet Storm Center, InfoCON: green
date: 2025-10-29
fetch_date: 2025-10-30T03:12:44.508404
---

# How to collect memory-only filesystems on Linux systems, (Wed, Oct 29th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jim Clausing](/handler_list.html#jim-clausing "Jim Clausing")

Threat Level: [green](/infocon.html)

* [previous](/diary/32428)

My next class:

|  |  |  |
| --- | --- | --- |
| [LINUX Incident Response and Threat Hunting](https://www.sans.org/event/dfircon-miami-2025/course/linux-threat-hunting-incident-response) | Coral Gables | Nov 17th - Nov 22nd 2025 |

# [How to collect memory-only filesystems on Linux systems](/forums/diary/How%2Bto%2Bcollect%2Bmemoryonly%2Bfilesystems%2Bon%2BLinux%2Bsystems/32432/)

**Published**: 2025-10-29. **Last Updated**: 2025-10-29 04:53:31 UTC
**by** [Jim Clausing](/handler_list.html#jim-clausing) (Version: 1)

[0 comment(s)](/diary/How%2Bto%2Bcollect%2Bmemoryonly%2Bfilesystems%2Bon%2BLinux%2Bsystems/32432/#comments)

I've been doing Unix/Linux IR and Forensics for a long time. I logged into a Unix system for the first time in 1983. That's one of the reasons I love teaching [FOR577](https://www.sans.org/cyber-security-courses/linux-threat-hunting-incident-response)[1], because I have stories that go back to before some of my students were even born that are still relevant today.

In recent years, I've noticed a lot of attackers try to hide their tools or stage their data exfiltration in memory-only filesystems like /dev/shm or other tmpfs locations.

![](https://isc.sans.edu/diaryimages/images/2025-10-29%2012_37_22-newton-ovpn%20-%20SecureCRT.png)

Unfortunately, you can't just dd these tmpfs filesystems. There is no block device backing it that will let you take a forensically sound image. So, if I want to get all of the metadata and the contents of any files the attacker may have stashed there, I'm going to need to try something else. Fortunately, after thinking about it a bit, I came up with a method that worked for me. I even talked it over briefly with Hal Pomeranz and we couldn't come up with anything better. When I was thinking about this about a year ago, I did a quick Google search and didn't see anyone else having talked about this, but I'd be surprised if others haven't come up with the same idea.

The basic idea is to first collect the metadata (inode contents), then collect the file contents, since doing it in the other order would cause the access timestamp in the inode to be updated. Since I came up with this technique, I've used it on dozens (probably 100+) of systems with pretty good success. I have run into a handful that didn't have the stat command, so I could only collect the contents, but not the inode metadata. You deal with what the system has available.

`# find /dev/shm -exec $(which stat) -c '0|%N|%i|%A|%u|%g|%s|%X|%Y|%Z|%W' {} \; | sed -e 's/|W$/|0/' -e s'/|?$/|0/' | ssh foo@system "cat - > $(hostname)-dev-shm-bodyfile"`

This commandline will use the find command to walk the tmpfs filesystem (in this example, /dev/shm) and run the stat command against every file and directory it finds. The sed command is to compensate for versions of the stat command that don't understand the %W format string to print out the creation time (b-time). Then, I pipe the output to ssh to send to a remote system where I collect the evidence (you could, of course, save it off to a USB drive or some other mounted filesystem if you wish). Versions of the Linux coreutils package prior to, I believe, version 8.32 don't have/use the statx() system call to access the creation timestamp even though it is usually in the inode on recent systems. The output is in bodyfile format which can then be fed to the mactime program from [The Sleuth Kit (TSK)](https://sleuthkit.org/)[2] that can convert it into the classic filesystem timeline format.

Once the metadata is collected, it is safe to collect the file contents (understanding that some file contents may have changed in the interval between the commands). The command that I usually use is as follows.

`#`find /dev/shm -type f -print | tar czvO -T - | ssh foo@system "cat - > $(hostname)-dev-shm-fs.tgz"

This will use the find command to print out the names of all of the regular files (I've never found a need to collect any other type) and pipe them to the tar command which will collect the contents (printing out the file names to stderr so I can see the progress) and output the (compressed because of the z switch) tarball to stdout to be piped to ssh to be collected on the same collection system. I then hash the tarball on the receiving system. I could, maybe should, hash the files on the live system I'm collecting from, but to this point, it hasn't been an issue.

As mentioned above, I've used this technique and many systems and even had it work on other Unix-ish systems like Juniper routers (that run FreeBSD under the hood) and even an ancient Solaris 9 system or two.

My last run of FOR577 for the year is in a few weeks at [DFIRCon](https://www.sans.org/cyber-security-training-events/dfircon-miami-2025)[3] in Miami where we will talk about this technique and lots of others. Join me.

References:

[1] <https://www.sans.org/cyber-security-courses/linux-threat-hunting-incident-response>

[2] <https://sleuthkit.org/>

[3] <https://www.sans.org/cyber-security-training-events/dfircon-miami-2025>

---------------
Jim Clausing, GIAC GSE #26
jclausing --at-- isc [dot] sans (dot) edu

Keywords: [tmpfs](/tag.html?tag=tmpfs) [linux](/tag.html?tag=linux)

[0 comment(s)](/diary/How%2Bto%2Bcollect%2Bmemoryonly%2Bfilesystems%2Bon%2BLinux%2Bsystems/32432/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [LINUX Incident Response and Threat Hunting](https://www.sans.org/event/dfircon-miami-2025/course/linux-threat-hunting-incident-response) | Coral Gables | Nov 17th - Nov 22nd 2025 |

* [previous](/diary/32428)

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