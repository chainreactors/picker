---
title: Understanding SSH Honeypot Logs: Attackers Fingerprinting Honeypots, (Thu, Jul 11th)
url: https://isc.sans.edu/diary/rss/31064
source: SANS Internet Storm Center, InfoCON: green
date: 2024-07-12
fetch_date: 2025-10-06T17:45:19.791699
---

# Understanding SSH Honeypot Logs: Attackers Fingerprinting Honeypots, (Thu, Jul 11th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31058)
* [next](/diary/31066)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Understanding SSH Honeypot Logs: Attackers Fingerprinting Honeypots](/forums/diary/Understanding%2BSSH%2BHoneypot%2BLogs%2BAttackers%2BFingerprinting%2BHoneypots/31064/)

**Published**: 2024-07-11. **Last Updated**: 2024-07-11 18:03:38 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Understanding%2BSSH%2BHoneypot%2BLogs%2BAttackers%2BFingerprinting%2BHoneypots/31064/#comments)

Some of the commands observed can be confusing for a novice looking at ssh honeypot logs. Sure, you have some obvious commands like "uname -a" to fingerprint the kernel. However, other commands are less intuitive and are not commands a normal user would use. I am trying to summarize some of the more common ones here, focusing on commands attackers use to figure out if they are inside a honeypot.

> `busybox dd if=$SHELL bs=22 count=1||dd if=/proc/self/exe bs=22 count=1||while read i;do busybox echo -n $i;done</proc/self/exe||cat /proc/self/exe`

There is a lot going on with this line. Let's take it apart one command at a time:

busybox: Busybox is a special binary found on many IoT style systems. It fulfills the role of various other Linux utilities in one small package. It is often symlinked from other names like "ls".

dd: "dd" (disk dump) is often used to copy disk images. But it can be used to read/write any binary file. Here the attacker reads the first 22 bytes of the "$SHELL" binary, usually something like "/bin/bash". A typical output would be " ELF>" for an ELF binary.

Next, the attacker is doing the same to the current binary (/proc/self/exe). I believe the purpose of this command line may be to eliminate some honeypots as this command will not work in simulations like cowrie.

I have seen variations of this like for example:

> `dd bs=52 count=1 if=.s || cat .s || while read i; do echo $i; done < .s`
>
> `/bin/busybox dd if=/bin/busybox bs=22 count=1||while read i;do /bin/busybox echo -n $i;done</bin/busybox||cat /proc/self/exe`

The next line uses a slightly different trick to figure out if the attacker is inside a honeypot:

> `cd /dev/shm; cat .s || cp /bin/echo .s; /bin/busybox ZRKTA`

/dev/shm is the "ramdisk", a special file system found on most Linux systems. Here the attacker just copies a file to it to see if the copy succeeds. The attacker first views the content of the file ".s", and later copies the echo command to .s just to see if there are any errors. The busybox command at the end just serves as a simple marker to note that the commands completed.

Next a partial command I see a lot:

> `(/bin/busybox echo -e \"\\x44\\x49\\x52\"||echo -e \"\\x44\\x49\\x52\")`

"echo -e" will output the text identified by he ASCII hex codes. The exact output may vary a bit from system to system as "-e" is not a standard option. But you will get something like

> `$ echo -e \"\\x44\\x49\\x52\"
> "DIR"`

Adding this as an argument to busybox is an attempt to execute a "DIR" command. The goal is not to execute the "DIR" command (it does not exist in Linux). Instead, seeing the "DIR" output will tell the attacker that the command succeeded.

Seen any other tricks used by attackers lately? Any questions about an odd command logged by cowrie? Let me know! :)

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords:

[0 comment(s)](/diary/Understanding%2BSSH%2BHoneypot%2BLogs%2BAttackers%2BFingerprinting%2BHoneypots/31064/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31058)
* [next](/diary/31066)

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