---
title: Detecting the Presence of a Debugger in Linux, (Tue, Nov 19th)
url: https://isc.sans.edu/diary/rss/31450
source: SANS Internet Storm Center, InfoCON: green
date: 2024-11-20
fetch_date: 2025-10-06T19:19:50.191214
---

# Detecting the Presence of a Debugger in Linux, (Tue, Nov 19th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31446)
* [next](/diary/31452)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Detecting the Presence of a Debugger in Linux](/forums/diary/Detecting%2Bthe%2BPresence%2Bof%2Ba%2BDebugger%2Bin%2BLinux/31450/)

**Published**: 2024-11-19. **Last Updated**: 2024-11-19 05:12:58 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Detecting%2Bthe%2BPresence%2Bof%2Ba%2BDebugger%2Bin%2BLinux/31450/#comments)

Hello from Singapore where I'm with Johannes and Yee! This week, I'm teaching FOR710[[1](https://www.sans.org/cyber-security-courses/reverse-engineering-malware-advanced-code-analysis/)]. I spotted another Python script that looked interesting because, amongst the classic detection of virtualized environments, it also tries to detect the presence of a debugger. The script has been developed to target both environments: Windows & Linux.

On Windows, it's pretty easy to detect if a debugger has been attached to a process. The microsoft ecosystems has many ways to check this: A stealthy method is to check the PEB ("Process Environment Block")[[2](https://learn.microsoft.com/en-us/windows/win32/api/winternl/ns-winternl-peb)] that provides a "BeingDebugged" member in its structure. Another easy way is to use the Microsoft API call IsDebuggerPresent()[[3](https://learn.microsoft.com/en-us/windows/win32/api/debugapi/nf-debugapi-isdebuggerpresent)]. Note that they are a lot of alternative techniques but I won't cover them here.

But how does it work in Linux? Because the malicious script is compatible with Linux, let's check the code:

```

def check_debugging():
    if True:
        try:
            if CURRENT_OS == "Windows":
                if ctypes.windll.kernel32.IsDebuggerPresent():
                    return True
            else:
                import re
                with open('/proc/self/status') as f:
                    status = f.read()
                    if re.search(r'TracerPid:\s+(?!0\n)', status):
                        return True
                except:
                    pass
    return False
```

If the script is executed on Windows, IsDebuggerPresent() will be called otherwise, the script will search for an interesting string in /proc/self/status:

```

xavier@rog:/proc/self$ cat status
Name:   bash
Umask:  0022
State:  S (sleeping)
Tgid:   352
Ngid:   0
Pid:    352
PPid:   351
TracerPid:      0
Uid:    1000    1000    1000    1000
Gid:    1000    1000    1000    1000
FDSize: 256
Groups: 4 20 24 25 27 29 30 44 46 116 1000
NStgid: 352
NSpid:  352
NSpgid: 352
NSsid:  352
VmPeak:     6216 kB
VmSize:     6216 kB
VmLck:         0 kB
VmPin:         0 kB
VmHWM:      5076 kB
VmRSS:      5076 kB
RssAnon:            1724 kB
RssFile:            3352 kB
RssShmem:              0 kB
VmData:     1736 kB
VmStk:       132 kB
VmExe:       892 kB
VmLib:      1864 kB
VmPTE:        48 kB
VmSwap:        0 kB
HugetlbPages:          0 kB
CoreDumping:    0
THP_enabled:    1
Threads:        1
SigQ:   1/30158
SigPnd: 0000000000000000
ShdPnd: 0000000000000000
SigBlk: 0000000000010000
SigIgn: 0000000000384004
SigCgt: 000000004b813efb
CapInh: 0000000000000000
CapPrm: 0000000000000000
CapEff: 0000000000000000
CapBnd: 000001ffffffffff
CapAmb: 0000000000000000
NoNewPrivs:     0
Seccomp:        0
Seccomp_filters:        0
Speculation_Store_Bypass:       thread vulnerable
SpeculationIndirectBranch:      conditional enabled
Cpus_allowed:   ffff
Cpus_allowed_list:      0-15
Mems_allowed:   1
Mems_allowed_list:      0
voluntary_ctxt_switches:        91
nonvoluntary_ctxt_switches:     1
```

The highlighted "TracerPid" line with the "0" indicates that no process is "tracing" this one. In Linux, a common technique used to analyze the behavious of a process is to use a tool like strace[[4](https://man7.org/linux/man-pages/man1/strace.1.html)] to log all the activity performed at system calls level:

```

xavier@rog:/proc/self$ strace -f -p 352
```

Let's recheck the /proc/self/status now that it's being "traced":

```

xavier@rog:/proc/self$ cat status|grep TracerPid
TracerPid:      9731
```

The script (SHA256a9ba5856b97327cc6c68d461e903569e30d5bd507405b5ecb34b0c513c42d50e)[[5](https://www.virustotal.com/gui/file/a9ba5856b97327cc6c68d461e903569e30d5bd507405b5ecb34b0c513c42d50e/detection)] remains undetected by most AV (VT score: 2/64) but its final purpose remains unknown because the bytecode passed to exec() does not seems to work! I'm still investigating it...

[1] <https://www.sans.org/cyber-security-courses/reverse-engineering-malware-advanced-code-analysis/>
[2] <https://learn.microsoft.com/en-us/windows/win32/api/winternl/ns-winternl-peb>
[3] <https://learn.microsoft.com/en-us/windows/win32/api/debugapi/nf-debugapi-isdebuggerpresent>
[4] <https://man7.org/linux/man-pages/man1/strace.1.html>
[5] <https://www.virustotal.com/gui/file/a9ba5856b97327cc6c68d461e903569e30d5bd507405b5ecb34b0c513c42d50e/detection>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Antidebugging](/tag.html?tag=Antidebugging) [Debugger](/tag.html?tag=Debugger) [Linux](/tag.html?tag=Linux) [Malware](/tag.html?tag=Malware) [Python](/tag.html?tag=Python)

[0 comment(s)](/diary/Detecting%2Bthe%2BPresence%2Bof%2Ba%2BDebugger%2Bin%2BLinux/31450/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/31446)
* [next](/diary/31452)

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