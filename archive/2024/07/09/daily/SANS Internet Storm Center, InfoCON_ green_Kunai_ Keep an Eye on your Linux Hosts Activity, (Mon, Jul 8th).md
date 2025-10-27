---
title: Kunai: Keep an Eye on your Linux Hosts Activity, (Mon, Jul 8th)
url: https://isc.sans.edu/diary/rss/31054
source: SANS Internet Storm Center, InfoCON: green
date: 2024-07-09
fetch_date: 2025-10-06T17:47:19.282296
---

# Kunai: Keep an Eye on your Linux Hosts Activity, (Mon, Jul 8th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31050)
* [next](/diary/31058)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Kunai: Keep an Eye on your Linux Hosts Activity](/forums/diary/Kunai%2BKeep%2Ban%2BEye%2Bon%2Byour%2BLinux%2BHosts%2BActivity/31054/)

**Published**: 2024-07-08. **Last Updated**: 2024-07-08 06:53:56 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Kunai%2BKeep%2Ban%2BEye%2Bon%2Byour%2BLinux%2BHosts%2BActivity/31054/#comments)

Microsoft has a very popular tool (part of the SysInternals) called Sysmon[[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)]. It is a system service and device driver designed to monitor and log system activity, including very useful events like process creations, network connections, DNS requests, file changes, and more. This tool is deployed by many organizations because it’s a great companion to expand the visibility of your Windows environments. Many SOCs rely on it to perform investigations and hunting.

A while ago, Microsoft decided to port Sysmon on Linux and, logically, called it SysmonForLinux[[2](https://github.com/Sysinternals/SysmonForLinux)].  Unfortunately, the tool never gets the same attraction, for multiple reasons. First of all, the core developer left Microsoft after the first release of the tool and it definitively lacks updates and follow-up. A good way to check this is to have a look at the open issues on the GitHub repository. There was a small update a few months ago but without new exciting features. Then, Microsoft tried to reproduce Sysmon for Windows but the two operating systems do not work in the same way. Anyway, I tested SysmonForLinux[[3](https://isc.sans.edu/diary/Whos%2BResolving%2BThis%2BDomain/29462)] (and it’s still running on the server) but I don’t use it in production.

Last week, I attended « Pass The Salt », a conference focussing on open-source software and cybersecurity. I participated in a very interesting workshop about « Kunai ». This tool, developed by Quentin Jérôme from CIRCL (the Luxembourg CERT) aims to replace SysmonForLinux. Its goal is to record and log system activity but in a more «Linux-oriented» flavor. It was presented for the first time at hack.lu in 2023 and it now reaches enough maturity to be tested and deployed on some Linux hosts.

Kunai is developed in Rust and uses eBPF to interact with the kernel (compatible with all the Linux LTS kernels(from 5.4 to 6.6)**.** eBPF programs can be attached to various hooks in the kernel, such as system calls, tracepoints, and network events, allowing them to run in response to specific events or conditions.

Kunai's core features are:

* Single executable (really simple to deploy)
* Events are enriched with a lot of data
* Support for containers, namespaces
* Filtering (to reduce the noise - this is a critical step in your deployment!)
* Hunting (based on an IOC list)
* JSON output to log events

To test it, just run Kunai as root:

```

$ sudo ./kunai | tee -a /var/log/kunai/events.log | jq .
```

This command will launch a Kunai that will log all events without filters. Let’s take a quick test:

```

$ curl https://isc.sans.edu
```

Curl will generate a lot of events (with the default config) but some of them are interesting.

Creation of the process:

```

{
  "data": {
    "ancestors": "/usr/lib/systemd/systemd|/usr/sbin/sshd|/usr/sbin/sshd|/usr/sbin/sshd|/usr/bin/bash",
    "parent_exe": "/usr/bin/bash",
    "command_line": "curl https://isc.sans.edu",
    "exe": {
      "file": "/usr/bin/curl",
      "md5": "25828b12203bb53e5f9bc54d2f8507a7",
      "sha1": "4bfe301715d6564404f6ebd56156c668329cc83b",
      "sha256": "53a2fe036f8def7b4372246ffa7835f97cdeb17268e7c8df9756f42baf28cc0f",
      "sha512": "c01c7298103bd2adaf432a807c65d2eccfbed9ce820d80424d03accdceb9c801167f65cfb93ea1b5677fdbf8235e34de061a449f03fd45d58fd913dce139aa51",
      "size": 260328
    }
  },
  "info": {
    "host": {
      "uuid": "2bb02904-9daa-5be5-adcb-5371b78c1866",
      "name": "ubuntu-vm",
      "container": null
    },
    "event": {
      "source": "kunai",
      "id": 1,
      "name": "execve",
      "uuid": "be8c77c8-ec40-959d-87af-39e19364f277",
      "batch": 161
    },
    "task": {
      "name": "curl",
      "pid": 9301,
      "tgid": 9301,
      "guuid": "09e8471d-730a-0000-c3d5-65bb55240000",
      "uid": 1000,
      "gid": 1000,
      "namespaces": {
        "mnt": 4026531841
      },
      "flags": "0x400000"
    },
    "parent_task": {
      "name": "bash",
      "pid": 9292,
      "tgid": 9292,
      "guuid": "95447ea0-6d0a-0000-c3d5-65bb4c240000",
      "uid": 1000,
      "gid": 1000,
      "namespaces": {
        "mnt": 4026531841
      },
      "flags": "0x400000"
    },
    "utc_time": "2024-07-06T05:27:19.916790817Z"
  }
}
```

The corresponding DNS Request:

```

{
  "data": {
    "ancestors": "/usr/lib/systemd/systemd|/usr/sbin/sshd|/usr/sbin/sshd|/usr/sbin/sshd|/usr/bin/bash|/usr/bin/sudo|/usr/bin/sudo|/usr/bin/bash",
    "command_line": "curl https://isc.sans.edu",
    "exe": {
      "file": "/usr/bin/curl"
    },
    "query": "isc.sans.edu",
    "proto": "udp",
    "response": "45.60.31.34;45.60.103.34",
    "dns_server": {
      "ip": "127.0.0.53",
      "port": 53,
      "public": true,
      "is_v6": false
    }
  },
  "info": {
    "host": {
      "uuid": "2bb02904-9daa-5be5-adcb-5371b78c1866",
      "name": "ubuntu-vm",
      "container": null
    },
    "event": {
      "source": "kunai",
      "id": 61,
      "name": "dns_query",
      "uuid": "5850ea54-ee1f-c38f-3dc6-294d8ae689b0",
      "batch": 3355
    },
    "task": {
      "name": "curl",
      "pid": 2350,
      "tgid": 2349,
      "guuid": "d12e76a0-7e02-0000-b116-fe882d090000",
      "uid": 0,
      "gid": 0,
      "namespaces": {
        "mnt": 4026531841
      },
      "flags": "0x400040"
    },
    "parent_task": {
      "name": "bash",
      "pid": 1709,
      "tgid": 1709,
      "guuid": "2672a103-1100-0000-b116-fe88ad060000",
      "uid": 0,
      "gid": 0,
      "namespaces": {
        "mnt": 4026531841
      },
      "flags": "0x400100"
    },
    "utc_time": "2024-07-06T05:27:19.942717828Z"
  }
}
```

I like the "ancestors" field that reveals the complete process tree!

One of the critical tasks to perform with Kunai is to know what you’re looking for and filter unwanted events (exactly like Sysmon). The simple curl command tested above generated 49 events! Most of them are of the type ‘mmap\_exec’. This event is generated whenever the mmap[[4](https://man7.org/linux/man-pages/man2/mmap.2.html)] syscall is used to map an executable file in memory, with memory execution protection. This syscall is typically related to loading a dynamic library but it may reveal some malicious activity when malware tries to load a shellcode by example.

Logically, you can write filters to reduce the noise and get rid of these events. Here, Kunay and Sysmon work in the same way: try to reduce the noise but not too much or you increase chances of missing interesting events.

Here is a simple filter:

```

$ cat filter.yaml
name: log.interesting_events
params:
    filter: true
match-on:
    events:
        kunai: [ 1,2,61 ]
```

The list is supported events is available in the documentation[[5](https://why.kunai.rocks/docs/category/kunai---events)]. In the example above, we will record only:

* Execve (ID 1)
* Execve script (reports more details about script interpreters) (ID 2)
* Dns query (ID 61)

Now restart Kunai:

```

$ sudo ./kunai -r filter.yaml | tee ...