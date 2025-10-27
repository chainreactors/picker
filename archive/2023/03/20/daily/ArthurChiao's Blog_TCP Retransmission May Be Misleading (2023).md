---
title: TCP Retransmission May Be Misleading (2023)
url: https://arthurchiao.github.io/blog/tcp-retransmission-may-be-misleading/
source: ArthurChiao's Blog
date: 2023-03-20
fetch_date: 2025-10-04T10:03:55.030515
---

# TCP Retransmission May Be Misleading (2023)

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# TCP Retransmission May Be Misleading (2023)

Published at 2023-03-19 | Last Update 2023-03-19

## TL; DR

Modern kernels by default enable a TCP option called **Tail Loss Probe (TLP)**,
which actively sends the so-called “probe” packets to achieve TCP fast
recovery. A side effect is that a large part of those probe packets is
classified into TCP retransmissions (in good quality networks such as data center networks),
which may be misleading for networking stack monitoring and troubleshooting, and
leaving “TCP retransmission” a less useful indicator to network quality.

![](/assets/img/tcp-retransmission-may-be-misleading/retrans-types-and-scope.png)

---

* [TL; DR](#tl-dr)
* [1 Problem statement](#1-problem-statement)
* [2 Kernel stats for TCP retransmission](#2-kernel-stats-for-tcp-retransmission)
  + [2.1 Standard MIBs and `/proc/net/snmp`](#21-standard-mibs-and-procnetsnmp)
  + [2.2 Linux extended MIBs and `/proc/netstat`](#22-linux-extended-mibs-and-procnetstat)
  + [2.3 Userspace tool: `netstat`](#23-userspace-tool-netstat)
  + [2.4 Retransmission stats in `netstat` output](#24-retransmission-stats-in-netstat-output)
* [3 Differentiate three types of TCP retransmissions](#3-differentiate-three-types-of-tcp-retransmissions)
  + [3.1 RTO-based retransmission](#31-rto-based-retransmission)
    - [RTO range: `[200ms, 120s]`, per-connection, updated by RTT](#rto-range-200ms-120s-per-connection-updated-by-rtt)
    - [Initial RTO and backoff](#initial-rto-and-backoff)
    - [Effective RTO/RTT of a TCP connection: `ss -i`](#effective-rtortt-of-a-tcp-connection-ss--i)
    - [Drawback](#drawback)
  + [3.2 Optimization: fast retransmission](#32-optimization-fast-retransmission)
    - [Dependency: SACK (Selective ACK)](#dependency-sack-selective-ack)
    - [Rational](#rational)
    - [Statistics in `netstat` output](#statistics-in-netstat-output)
    - [Kernel code: where the counter is updated](#kernel-code-where-the-counter-is-updated)
    - [Summary](#summary)
  + [3.3 Optimiaztion: tail loss probe (kernel `3.10+`)](#33-optimiaztion-tail-loss-probe-kernel-310)
    - [Dependency: SACK](#dependency-sack)
    - [Rational](#rational-1)
    - [`sysctl` parameter](#sysctl-parameter)
    - [Statistics in `netstat` output](#statistics-in-netstat-output-1)
    - [Kernel code: where the counter is updated](#kernel-code-where-the-counter-is-updated-1)
  + [3.4 Retransmission-related counters relationship](#34-retransmission-related-counters-relationship)
  + [3.5 Comparison of 3 types of retransmits](#35-comparison-of-3-types-of-retransmits)
* [4 Back to question](#4-back-to-question)
  + [4.1 Will TLP increase the counter of total retransmitted segments?](#41-will-tlp-increase-the-counter-of-total-retransmitted-segments)
  + [4.2 Where does the `5ms` timeout comes from?](#42-where-does-the-5ms-timeout-comes-from)
* [5 Issues and advanced topics](#5-issues-and-advanced-topics)
  + [5.1 SYN retransmits](#51-syn-retransmits)
  + [5.2 k8s/cadvisor and pod metrics](#52-k8scadvisor-and-pod-metrics)
* [References](#references)

---

# 1 Problem statement

The problem starts from an observation:
on monitoring kernel networking stack, we noticed that almost all pods
in our on-premises k8s clusters have continuous TCP retransmissions,

![](/assets/img/tcp-retransmission-may-be-misleading/tcp-metrics.png)

The data source of this metric comes from kernel TCP statistics for this pod
(we’ll detail this in the next section).

On capturing the traffic, we noticed that lots of TCP retransmissions are
**triggered in a very short time window**, e.g. **`5ms`**,
as shown below:

![](/assets/img/tcp-retransmission-may-be-misleading/packets-capture.png)

A quick analysis:

* `#30`: client send request to server
* `#31`: server ACK #30
* `#32`: client send request to server
* `#33`: server ACK #32
* **`#34 ~ #37`**: client send request to server
* `#38`: client retransmit `#37`, two weird phenomenons:

  + `#34 ~ #36` **not ACK-ed by server** either, but the client
    skipped them and retransmitted the last segment (`#38`) directly;
  + Elasped time between `#38` and `#37/#36/#35/#34` is about 5ms.

Besides, we could also conclude that `#38` is not **fast retransmission**,
which should be triggered by duplicated ACKs. Then, according to textbooks,
the minimum waiting interval before retransmitting a packet should be
`RTOmin`, which is a hard limit (kernel
macro) **`200ms`** for most modern kernels and
doesn’t fit our observation.

So, the question is: **what's the mechanism of this retransmission, and
how does it work**?

To understand this problem, we need some background knowledge of kernel
TCP stack.

# 2 Kernel stats for TCP retransmission

Linux kernel maintains tons of statistic counters for TCP, among which
several are used for retransmission purposes. Users can get these statistics
via **`SNMP`** protocol or `/proc` file system.

Two kinds of MIBs (Management information base):

* **`TCP_MIB_*`**: a small set of TCP metrics counters defined by RFC 1213 & RFC 2012;
* **`LINUX_MIB_*`**: an extension defined by Linux, which
  provides more counters related to the Linux TCP implementation.

## 2.1 Standard MIBs and `/proc/net/snmp`

Types definition:

```
// https://github.com/torvalds/linux/blob/v5.10/include/uapi/linux/snmp.h#L120

// tcp mib definitions
// RFC 1213:  MIB-II TCP group
// RFC 2012 (updates 1213):  SNMPv2-MIB-TCP
enum {
    TCP_MIB_NUM = 0,
    TCP_MIB_RTOALGORITHM,       /* RtoAlgorithm */
    TCP_MIB_RTOMIN,             /* RtoMin */
    TCP_MIB_RTOMAX,             /* RtoMax */
    TCP_MIB_MAXCONN,            /* MaxConn */
    TCP_MIB_ACTIVEOPENS,        /* ActiveOpens */
    TCP_MIB_PASSIVEOPENS,       /* PassiveOpens */
    TCP_MIB_ATTEMPTFAILS,       /* AttemptFails */
    TCP_MIB_ESTABRESETS,        /* EstabResets */
    TCP_MIB_CURRESTAB,          /* CurrEstab */
    TCP_MIB_INSEGS,             /* InSegs */
    TCP_MIB_OUTSEGS,            /* OutSegs */
    TCP_MIB_RETRANSSEGS,        /* RetransSegs */
    TCP_MIB_INERRS,             /* InErrs */
    TCP_MIB_OUTRSTS,            /* OutRsts */
    TCP_MIB_CSUMERRORS,         /* InCsumErrors */
    __TCP_MIB_MAX
};
```

Access these counters from userspace via `/proc` file system:

```
$ cat /proc/net/snmp | grep Tcp
Tcp: RtoAlgorithm RtoMin RtoMax MaxConn ActiveOpens PassiveOpens AttemptFails EstabResets CurrEstab InSegs OutSegs RetransSegs InErrs OutRsts InCsumErrors
Tcp: 1 200 120000 -1 22432878 9645244 1320167 4077672 2501 7823669861 9712198857 8493997 10 18640759 5
```

Note that there are also stats for other protocols in `/proc/net/snmp`, such as UDP, ICMP, IP.

## 2.2 Linux extended MIBs and `/proc/netstat`

The Linux extended MIBs (a fairly long list):

```
// https://github.com/torvalds/linux/blob/v5.10/include/uapi/linux/snmp.h#L120

/* linux mib definitions */
enum {
    LINUX_MIB_NUM = 0,
    ...
    LINUX_MIB_TCPLOSTRETRANSMIT,        /* TCPLostRetransmit */
    ...
    LINUX_MIB_TCPFASTRETRANS,           /* TCPFastRetrans */
    LINUX_MIB_TCPSLOWSTARTRETRANS,      /* TCPSlowStartRetrans */
    LINUX_MIB_TCPTIMEOUTS,              /* TCPTimeouts */
    LINUX_MIB_TCPLOSSPROBES,            /* TCPLossProbes */
    LINUX_MIB_TCPLOSSPROBERECOVERY,     /* TCPLossProbeRecovery */
    ...
    __LINUX_MIB_MAX
};
```

Retrieve corresponding stats from userspace:

```
$ cat /proc/net/netstat | grep "^Tcp"
TcpExt: SyncookiesSent SyncookiesRecv SyncookiesFailed EmbryonicRsts PruneCalled RcvPruned OfoPruned OutOfWindowIcmps LockDroppedIcmps ArpFilter TW TWRecycled TWKilled PAWSActive PAWSEstab DelayedACKs DelayedACKLocked DelayedACKLost ListenOverflows ListenDrops TCPHPHits TCPPureAcks TCPHPAcks TCPRenoRecovery TCPSackRecovery TCPSACKReneging TCPFACKReorder TCPSACKReorder TCPRenoReorder TCPTSReorder TCPFull...