---
title: tmate - Instant Terminal Sharing (or How To Backdoor a Linux Server)
url: https://dfir.ch/posts/tmate_as_a_backdoor/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-07
fetch_date: 2025-10-06T18:52:24.417490
---

# tmate - Instant Terminal Sharing (or How To Backdoor a Linux Server)

[Home](https://dfir.ch/)
[ ]

Menu

* [Home](/)
* [Posts](/posts/)
* [Talks](/talks/)
* [Tweets](/tweets/)
* |

LIGHT

DARK

# tmate - Instant Terminal Sharing (or How To Backdoor a Linux Server)

6 Oct 2024

**Table of Contents**

* [Introduction](#introduction)
* [Installation](#installation)
* [Demonstration](#demonstration)
* [Traces](#traces)

## Introduction

Over the last three years, various cyber security companies wrote about TeamTNT TTPs, notably about the use of tmate as their tool of choice for backdooring Linux servers after a compromise:

* [TeamTNT: Cryptomining Explosion (Intezer, 2021)](https://intezer.com/wp-content/uploads/2021/09/TeamTNT-Cryptomining-Explosion.pdf)
* [Attackers Abusing Various Remote Control Tools (ASEC, 2022)](https://asec.ahnlab.com/en/40263/)
* [TeamTNT Reemerged with New Aggressive Cloud Campaign (Aqua, 2023)](https://www.aquasec.com/blog/teamtnt-reemerged-with-new-aggressive-cloud-campaign/)

In this short blog post, we examine the traces left behind from a tmate installation and some hints on where to find traces when actively looking for backdoored Linux servers with an active tmate instance running. To showcase the installation and configuration of tmate during a real attack, the shell script `tmate.sh`, as mentioned by Aqua, is available on [VirusTotal](https://www.virustotal.com/gui/file/2531b25cb663c445991b71e3f03ff3d759e55725022a209c8a0ca5255751c6e2).

![Official tmate website](/images/tmate/tmate.png "Official tmate website")

Figure 1: tmate.io - Official website

## Installation

We can download the tmate binary from [GitHub](https://github.com/tmate-io/tmate) or install it via a package manager (e.g., `apt-get install tmate`). TeamTNT, however, downloaded standalone tmate binaries onto the compromised servers. This steps here are just for the sake of demonstrating. After installing tmate, we must create an API key on the official website (<https://tmate.io/>) to map our sessions with the tmate infrastructure.

```
Dear tmate user,

Your API key is: tmk-tA31l2eN8jzFdfirrocks

You can use it to name sessions as such:

From the CLI:
tmate -k tmk-tA31l2eN8jzFdfirrocks -n testname
```

## Demonstration

We start tmate in our lab environment:

```
# tmate -F -k tmk-tA31l2eN8jzFdfirrocks -n dfir.ch
To connect to the session locally, run: tmate -S /tmp/tmate-0/NF23EY attach
Connecting to ssh.tmate.io...
web session read only: https://tmate.io/t/ro-3ShtmE2wWrugJ2PXSTauDjxyJ
ssh session read only: ssh ro-3ShtmE2wWrugJ2PXSTauDjxyJ@lon1.tmate.io
web session: https://tmate.io/t/BBFyj2WU4JxCg4AYAGkwKQV6y
ssh session: ssh BBFyj2WU4JxCg4AYAGkwKQV6y@lon1.tmate.io
The session name may only contain alphanumeric characters or single hyphens and cannot begin or end with a hyphen
```

Whereas the parameter `-F` only starts the server side of tmate and outputs its log on stdout (as opposed to showing the session shell, which is useful for pair programming). This makes it easy to integrate into a service manager like systemd or kubernetes. It ensures the session never dies by respawning a shell when it exits.

The parameter `-k`Â is the API Key, andÂ `-n`Â is the session name we can choose.

Circling back to the output above, when tmate was started, we saw different options for connecting back to our server. Next to the classic SSH access, there is also a web access over the browser, which works surprisingly well:

![tmate Web Access](/images/tmate/web_tmate.png "tmate Web Access")

Figure 2: Web Access

## Traces

As an Incident Responder or Theat Hunter, how do we find traces of an old tmate usage and or installation or how we find traces of an ongoing session sharing with tmate? One of the more obvious ways to find a running tmate instance is looking at the running processes on the system with a tool like `ps`. Yes - it would certainly be possible to “hide” this process from the output of `ps`. However, there are other techniques we could use to find such hidden processes (which we will discuss in an upcoming blog post).

```
# ps aux | grep tmate
root 1981  0.0  1.9  15020  9088 pts/0 S+ 05:21 0:00 tmate -F -k tmk-tA31l2eN8jzFdfirrocks -n dfir.ch
```

In the public documented intrusions from TeamTNT, they downloaded a compiled version of tmate to the compromised hosts, circumventing the package manager. However, there might be cases where we could find traces in the package manager log files, here from our Ubuntu lab host:

`/var/log/apt/history.log`

```
Commandline: apt-get install tmate
Install: tmate:amd64 (2.4.0-2build3), libmsgpackc2:amd64 (4.0.0-3build1, automatic), libevent-2.1-7t64:amd64 (2.1.12-stable-9ubuntu2, automatic)
```

`/var/log/apt/term.log`

```
Selecting previously unselected package tmate.
Preparing to unpack .../tmate_2.4.0-2build3_amd64.deb ...
Unpacking tmate (2.4.0-2build3) ...
Setting up tmate (2.4.0-2build3) ...
```

Because tmate is connecting back to a remote server, and this server will be responsible for tunneling all commands back to the compromised server, there is no successful login recorded inside the various log files. However, I found an interesting edge case while leaving my session running for a longer period. Ubuntu kept complaining about outdated binaries because I hadnât upgraded my packages swiftly after the setup of the new lab machine. These messages ended up in theÂ `unattended-upgrades-dpkg.log` file, hinting that somebody is connected via a tmate session.

`/var/log/unattended-upgrades/unattended-upgrades-dpkg.log`

```
[..]

User sessions running outdated binaries:
 root @ session #1: tmate[1981]
 root @ user manager service: systemd[1067]

No VM guests are running outdated hypervisor (qemu) binaries on this host.
Log ended: 2024-09-24  07:02:04
```

As explained in the paper [tmate: A scalable UNIX terminal sharing/management tool](https://viennot.com/tmate.pdf), a session token, and a read-only session token are generated through `/dev/urandom`. These tokens are comprised of 25 alphanumeric characters. The tmux server is set to operate on the `/tmp/tmate/session token.sock` unix socket, and a symbolic link to the file `/tmp/tmate-session token.sock` is created to point to the real unix socket. We find this file not only in the `/tmp` directory but also in the `/proc` directory:

`/proc/net/unix`

```
ffff920887dbbb80: 00000002 00000000 00010000 0001 01 33334 /tmp/tmate-0/FJbmgn
```

Last but not least, incoming SSH connections might be normal in some environments (depending on the scenario and the placement of the server(s)), but outgoing SSH connections from your servers to an IP address hosted on a VPS hoster should at least raise some eyebrows, or even better, an alert. `lsof`, when pointing to the tmate process, shows the established outgoing SSH session (last line).

`lsof`

```
# lsof -p 13453
COMMAND   PID USER  FD TYPE DEVICE SIZE/OFF   NODE NAME
tmate   13453 root cwd DIR 252,1 4096 258081 /root/tmate-2.4.0-static-linux-amd64
tmate   13453 root rtd DIR 252,1 4096 2 /
tmate   13453 root txt REG 252,1 3135320 258153 /root/tmate-2.4.0-static-linux-amd64/tmate
[..]
tmate   13453 root 7u unix 0xffff990909178440 0t0 176928 /tmp/tmate-0/bjmAnh type=STREAM
tmate   13453 root 8u unix 0xffff990909178880 0t0 176922 type=STREAM
[..]
tmate   13453 root 12u IPv4 176947 0t0 TCP foobar:55686->206.189.246.93:ssh (ESTABLISHED)
```

Â© 2025 .
Powered by [Hugo blog awesome](https://github.com/hugo-sid/hugo-blog-awesome).