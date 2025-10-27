---
title: Who's Resolving This Domain&#x3f;, (Mon, Jan 23rd)
url: https://isc.sans.edu/diary/rss/29462
source: SANS Internet Storm Center, InfoCON: green
date: 2023-01-24
fetch_date: 2025-10-04T04:40:30.606322
---

# Who's Resolving This Domain&#x3f;, (Mon, Jan 23rd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29460)
* [next](/diary/29470)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Who's Resolving This Domain?](/forums/diary/Whos%2BResolving%2BThis%2BDomain/29462/)

**Published**: 2023-01-23. **Last Updated**: 2023-01-23 07:22:39 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Whos%2BResolving%2BThis%2BDomain/29462/#comments)

Challenge of the day: To find the process that resolved a specific domain. And this is not always easy!

On Windows, when you search for processes that resolve domain names, you’ll find most of the time the well-known ‘svchost.exe’. The easiest way to get more details is to use Sysmon, which can log processes that perform DNS lookups (via the event ID 22[[1](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventid=90022)]).

But in this diary, I’ll focus on Linux because I faced a situation where a suspicious domain was resolved by a Linux server, and I had no idea about who performed this DNS traffic.

First attempt, if you take a full packet capture, you’ll see the DNS traffic (with all details if you capture the complete packet's payload) but no way to find the suspicious process.

Second attempt, you could try to use the command ‘netstat’ but, again, you’ll see only “established” (note the quotes because UDP traffic is stateless) connections. The process will be listed only when executed with root privileges:

```

$ sudo netstat -aunp
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
udp        0      0 172.28.0.1:34805        172.28.0.4:1514         ESTABLISHED 808/ossec-agentd
udp        0      0 127.0.0.53:53           0.0.0.0:*                           50593/systemd-resol
udp        0      0 0.0.0.0:161             0.0.0.0:*                           1454022/snmpd
udp        0      0 127.0.0.1:323           0.0.0.0:*                           814/chronyd
udp        0      0 0.0.0.0:45739           0.0.0.0:*                           269598/rsyslogd
udp        0      0 127.0.0.1:60485         0.0.0.0:*                           1454022/snmpd
udp6       0      0 ::1:323                 :::*                                814/chronyd
udp6       0      0 fe80::20c:29ff:fee5:546 :::*                                50562/systemd-netwo
```

We can see on this host that an OSSEC client is talking to its server (UDP/1514), but no trace of DNS resolutions. It's so fast that you will probably never see them.

Another good candidate is the tool ‘lsof’. It will list all file handles used by processes and can also be helpful with network connections. However, we have the same issue: you usually won’t have time to capture the process.

```

$ sudo lsof|grep -i udp
ossec-age     808                             ossec    7u     IPv4          287945015       0t0        UDP XXX:60262->XXX:1514
chronyd       814                           _chrony    5u     IPv4              24612       0t0        UDP localhost.localdomain:323
chronyd       814                           _chrony    6u     IPv6              24613       0t0        UDP localhost6.localdomain6:323
systemd-n   50562                   systemd-network   19u     IPv6          269165675       0t0        UDP lab0:dhcpv6-client
systemd-r   50593                   systemd-resolve   12u     IPv4           19871966       0t0        UDP localhost:domain
rsyslogd   269598                            syslog    8u     IPv4           76691370       0t0        UDP *:45739
rsyslogd   269598  269599 in:imuxso          syslog    8u     IPv4           76691370       0t0        UDP *:45739
rsyslogd   269598  269600 in:imklog          syslog    8u     IPv4           76691370       0t0        UDP *:45739
rsyslogd   269598  269601 rs:main            syslog    8u     IPv4           76691370       0t0        UDP *:45739
snmpd     1454022                       Debian-snmp    8u     IPv4          226275818       0t0        UDP *:snmp
snmpd     1454022                       Debian-snmp    9u     IPv4          226275808       0t0        UDP localhost.localdomain:60485
```

But wait, Sysmon is available on Linux[[2](https://github.com/Sysinternals/SysmonForLinux/tree/main/doc)]. Sysmon for Linux is less popular than the Windows version. I have a running Sysmon running in a lab here. I was not able to log any DNS resolution, even if it seems to be correctly configured:

```

# sysmon -c

Sysmon v1.0.0 - Monitors system events
Sysinternals - www.sysinternals.com
By Mark Russinovich, Thomas Garnier and Kevin Sheldrake
Copyright (C) 2014-2021 Microsoft Corporation
Using libxml2. libxml2 is Copyright (C) 1998-2012 Daniel Veillard. All Rights Reserved.

Rule configuration (version 4.70):
 - ProcessCreate                      onmatch: exclude   combine rules using 'Or'
 - NetworkConnect                     onmatch: exclude   combine rules using 'Or'
 - ProcessTerminate                   onmatch: exclude   combine rules using 'Or'
 - RawAccessRead                      onmatch: exclude   combine rules using 'Or'
 - ProcessAccess                      onmatch: exclude   combine rules using 'Or'
 - FileCreate                         onmatch: exclude   combine rules using 'Or'
 - DnsQuery                           onmatch: exclude   combine rules using 'Or'
        QueryName                      filter: end with     value: '.arpa.'
 - FileDelete                         onmatch: exclude   combine rules using 'Or'
```

Let's try to find another solution. A tool that is usually helpful is auditd[[3](https://www.redhat.com/sysadmin/configure-linux-auditing-auditd)]. Installed on many servers, it collects a lot of information about the system activity.

Let's define a filter:

```

# auditctl -a exit,always -F arch=b64 -F a0=2 -F a1\&=2 -S socket -k SOCKET
```

This will log calls to socket(). Filters (-F) refer to SOCK\_DGRAM and SOCK\_NOBLOCK|SOCK\_CLOEXEC. "-k SOCKET" is used to tag matching events.

Now, let's hope that our process will perform more DNS resolutions, and let's try to find them:

```

# ausearch -i -ts today -k SOCKET
```

I executed the command ‘curl https://malicious.com' from a shell and got this result:

```

type=PROCTITLE msg=audit(01/21/23 15:31:51.114:863) : proctitle=curl -v https://malicious.com
type=SYSCALL msg=audit(01/21/23 15:31:51.114:863) : arch=x86_64 syscall=socket success=yes exit=7 a0=inet a1=SOCK_DGRAM a2=ip a3=0xffffffffffffff0d items=0 ppid=470790 pid=3528111 auid=xavier uid=root gid=root euid=root suid=root fsuid=root egid=root sgid=root fsgid=root tty=pts1 ses=2363 comm=curl exe=/usr/bin/curl key=SOCKET
```

In this example, we are lucky because "malicious.com" was part of the command line arguments, but it's not always that easy! If you can't see the process, you will have to correlate the time of the UDP traffic with the resolution of the domain in your resolver logs (because you keep a log of your DNS resolver, right? ;-)

Another tool that deserves to be tested is systemtap[[4](https://sourceware.org/systemtap/)]. This tool is not installed by default, but it does a decent job of recording system activities.

You need to create a rule to instruct systemtap to log some activity:

```

# cat dns_traffic.stp
probe netfilter.ip.local_out {
  if (dport == 53)
      printf(“DNS traffic: %s[%d] %s:%d\n", execname(), pid(), daddr, dport)
}'
```

This will list all DNS resolutions:

```

# stap -v dns_traffic.stp
Pass 1: parsed user script and 476 libra...