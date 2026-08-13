---
title: Linux Kernel Process Accounting, (Wed, Aug 12th)
url: https://isc.sans.edu/diary/rss/33240
source: SANS Internet Storm Center, InfoCON: green
date: 2026-08-12
fetch_date: 2026-08-13T04:05:13.147269
---

# Linux Kernel Process Accounting, (Wed, Aug 12th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/33236)
* [next](/diary/33242)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Linux Kernel Process Accounting](/forums/diary/Linux%2BKernel%2BProcess%2BAccounting/33240/)

**Published**: 2026-08-12. **Last Updated**: 2026-08-12 14:21:10 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Linux%2BKernel%2BProcess%2BAccounting/33240/#comments)

A couple of days ago, Xavier posted about Atuin to gain more insight into the command history. Atuin does a great job of better organizing what is usually handled by "bash\_history" and collecting meaningful additional data. Our reader David commented that this can also be done quite well with Linux's kernel process accounting feature, and I think he is very right. I really like Linux process accounting for a number of reasons, so here is a quick introduction.

Process accounting is a kernel feature. You will not see a specific process responsible for it. Instead, the "accton" command signals the kernel to start logging process data to a specific location (usually /var/log/account/pacct). Once a process terminates, the kernel will log respective details to the binary log file.

### 1 - Installation

I don't think process accounting is enabled by default on any Linux system. It does add a little additional overhead, but some users may shy away from it because it requires additional disk writes to collect the information. Memory and other CPUs should not be significantly impacted by process accounting. On my not very busy Proxmox system, it uses about 50 MB/day of disk space. So nothing that should be noticeable for most systems.

Installation usually comes down to installing the respective package for your distribution. On Debian based distributions, it is just

> `apt install acct`

This will typically also configure the startup scripts, but it can't hurt to run

> `systemctl enable --now acct`

That is it. Wait a little bit, and you will see the log.

### 2 - How to read the logs

Logs are saved in a binary format. The "lastcomm" command can be used to display the log in a readable format. For example:

`ip6tables-save   S     root     __         0.00 secs Wed Aug 12 06:25
iptables-restor  S     root     __         0.00 secs Wed Aug 12 06:25
iptables-save    S     root     __         0.00 secs Wed Aug 12 06:25
check_ssh              100107   __         0.00 secs Wed Aug 12 06:25
cron              F    100000   __         0.00 secs Wed Aug 12 06:25
sh               S     100000   __         0.00 secs Wed Aug 12 06:25
debian-sa1             100000   __         0.00 secs Wed Aug 12 06:25`

These are a few lines from my Proxmox server. It logs the process name, Flags (S=super user, F=forked process, D=generated core dump, X=terminated by signal), User name (or ID), CPU execution time, and finally the timestamp at which the process was started. The output may be modified slightly depending on the command-line arguments used.

### 3 - Remote Logging

Unlike most Linux logs, these logs are not created by syslog. However, you may still read them with syslog to forward them to a central log collector/SIEM. Syslog-ng for example include a "s\_pacct" processor for process accounting logs. You enable it with this configuration:

`source s_pacct {
    pacct(file("/var/log/account/pacct"));
};`

### 4 - Other useful tools

The "sa" command can be used to easily extract summaries from accounting data. For example, a breakdown by CPU time used by different processes

`# sa -c | head -10
  329063  100.00%  259245.37re  100.00%      70.29cp  100.00%         0avio     24320k
     469    0.14%      55.38re    0.02%      52.65cp   74.90%         0avio    124752k   ffmpeg
     488    0.15%       5.43re    0.00%       4.57cp    6.51%         0avio      5338k   apt-get
    2820    0.86%       3.60re    0.00%       3.34cp    4.74%         0avio     13295k   ceph
    1231    0.37%       1.96re    0.00%       1.92cp    2.73%         0avio      1974k   ps
     312    0.09%    1907.83re    0.74%       1.36cp    1.93%         0avio     88176k   named
       7    0.00%   39483.07re   15.23%       0.76cp    1.08%         0avio      6348k   systemd-journal
     123    0.04%   34804.71re   13.43%       0.34cp    0.48%         0avio     20367k   ***other*
       8    0.00%       0.68re    0.00%       0.27cp    0.38%         0avio      3926k   store
     366    0.11%       0.58re    0.00%       0.26cp    0.36%         0avio      2235k   dpkg-deb*`

### 5 - Containers

Process accounting is a kernel feature, and the kernel must be compiled and configured to support process accounting. If you are running Linux containers in Proxmox (the platform I am using), process accounting will not work unless the container is privileged. But it does not have to work. The container processes are logged by the host, which I think is actually better. This way, the logs are more easily centralized, and they can't be tampered with from inside the container.

### 6 - Conclusion

I think Linux kernel process accounting is a very neat and often overlooked feature. You may be able to do more fine-grained inspection with eBPF, but process accounting is "ready to go and useful" with little work. It does not log command line options, which may be an issue in incident response. But it is a very good supplement to other features like bash\_history files, and it captures processes that bash\_history would never see.

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [acct](/tag.html?tag=acct) [kernel](/tag.html?tag=kernel) [linux](/tag.html?tag=linux) [process accounting](/tag.html?tag=process accounting)

[0 comment(s)](/diary/Linux%2BKernel%2BProcess%2BAccounting/33240/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/33236)
* [next](/diary/33242)

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