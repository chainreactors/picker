---
title: Fantastic clear-text passwords and where to collect them (Part 1 - Linux)
url: https://dfir.ch/posts/fantastic_passwords_linux/
source: Instapaper: Unread
date: 2026-06-30
fetch_date: 2026-07-01T06:24:35.917326
---

# Fantastic clear-text passwords and where to collect them (Part 1 - Linux)

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

# Fantastic clear-text passwords and where to collect them (Part 1 - Linux)

22 Jun 2026

**Table of Contents**

* [1. Introduction](#1-introduction)
* [2. Bash History](#2-bash-history)
  + [Defense & Hardening](#defense--hardening)
* [3. Process Memory Extraction](#3-process-memory-extraction)
  + [Defense & Hardening](#defense--hardening-1)
* [4. Process Command-Line Snooping](#4-process-command-line-snooping)
  + [Defense & Hardening](#defense--hardening-2)
* [5. Backdoor Login Prompt](#5-backdoor-login-prompt)
  + [Defense & Hardening](#defense--hardening-3)
* [6. ssh-grabber / 3snake](#6-ssh-grabber--3snake)
  + [Defense & Hardening](#defense--hardening-4)
* [7. Terminal Input Capture on Linux with pam.d](#7-terminal-input-capture-on-linux-with-pamd)
  + [Defense & Hardening](#defense--hardening-5)
* [8. Conclusion](#8-conclusion)

## 1. Introduction

During Digital Forensics and Incident Response (DFIR) investigations, we frequently observe Threat Actors (TAs) using various methods to harvest clear-text credentials on Linux endpoints. While defense teams focus heavily on Windows credential dumping (like LSASS parsing), Linux infrastructure remains a fertile ground for credential theft.

In many discussions with clients and security experts, the question often arises: *If an attacker has already gained root privileges on a Linux server, why is it still relevant to collect additional plaintext passwords?* The answer comes down to lateral movement and privilege escalation beyond the local host. Compromised Linux servers are often gateways; collecting passwords there can unlock the wider network, cross-platform infrastructure, and cloud environments.

**This post highlights common techniques and artifacts encountered in real-world incidents, mapping out exactly where plaintext credentials leak and how adversaries systematically collect them. In addition, it covers hardened Linux appliances and discusses how credentials may still be exposed despite security controls.** By understanding these potential exposure points, defenders or administrators can implement effective hardening strategies, credential protection mechanisms, and monitoring controls to minimize risk and improve security on those devices.

Note: This blog post includes excerpts from our “Cleartext” presentation at BSides Munich and my BotConf presentation on âLost Signatures." You find the links to the presentations in the [talks](https://dfir.ch/talks/) section.

## 2. Bash History

A classic. If you are shrugging right now and thinking, âHow obvious,â I have a story for you.

In a recent incident investigation (we took over from another company), a Threat Actor hid inside a targeted network for months, stealthily moving around to steal confidential research material. They found out that the attackers had targeted an application server running Siemens software.

This software used a password-protected Java Keystore located at `/opt/siemens/scs_groupware/conf/keystore.jks`. The password to that keystore was sitting in clear-text inside the root user’s Bash history:
`keytool -importkeystore -srckeystore /opt/siemens/scs_groupware/conf/groupware.jks -storepass cleartext_password`

A backup copy of the target keystore was subsequently discovered in `/root/keystore.jks`. The Siemens software also included a feature for reading emails in Exchange Online (via `OpenScape` integration), providing direct access to the customerâs Azure tenant. The attacker extracted the private key and certificate from the keystore; now they only needed the customerâs `Tenant ID` and the `OpenScape app client ID`.

Both values were cleanly laid out in the OpenScape XML config file:

```
<Property name="exchange.auth.oauth.tenantId" value="<redacted>" writable="true"/>
<Property name="exchange.auth.oauth.clientId" value="<redacted>" writable="true"/>
```

This discovery allowed the TA to leverage the client credentials flow with certificate-based authentication on `login.microsoftonline.com` and use the Microsoft Graph API to read corporate emails. This scenario clearly illustrates how a single plaintext password in the Bash history can compromise an entire organization’s cloud email environment.

### Defense & Hardening

* Never pass passwords via command-line arguments. Use interactive prompts or retrieve them dynamically via secrets managers such as HashiCorp Vault.
* While passing secrets via environment variables is better than CLI arguments (since they aren’t written to `.bash_history`), be aware that root users, or the user owning the process, can still read them from `/proc/<pid>/environ` while the process is running.
* Set `HISTCONTROL=ignorespace` in user profiles. This allows administrators to prepend a space to any command containing a secret, preventing it from being logged to the history file.
* Implement `Microsoft Entra Conditional Access for Workload Identities` to protect service principals and restrict certificate-based authentication to trusted locations.

## 3. Process Memory Extraction

An attacker with root privileges can extract clear-text credentials directly from processing memory maps. Tools like **[truffleproc](https://github.com/controlplaneio/truffleproc)** automate this behavior by attaching to running processes via GDB, creating memory dumps, and scanning them for strings matching pattern signatures.

In the following example, an attacker dumps the current process, and truffleproc subsequently sifts through the resulting dump for strings that might be credentials or passwords. As a prerequisite, GDB must be installed on the compromised server.

```
root@passwords:~/truffleproc# ./truffleproc.sh $$
# coredumping pid 20124
Reading symbols from od...
Reading symbols from /usr/bin/bash...
Reading symbols from /lib/x86_64-linux-gnu/libtinfo.so.6...
Reading symbols from /lib/x86_64-linux-gnu/libc.so.6...
Reading symbols from /usr/lib/debug/.build-id/ae/7440bbdce614e0e79280c3b2e45b1df44e639c.debug...
Reading symbols from /lib64/ld-linux-x86-64.so.2...
Reading symbols from /usr/lib/debug/.build-id/20/5841581372e951d18b59e0d3b24c16d2291fef.debug...
# extracting strings to /tmp/tmp.6BkVH3F1TT
# finding secrets
# results in /tmp/tmp.6BkVH3F1TT/results.txt
```

### Defense & Hardening

* Tools like truffleproc rely on `ptrace` to dump memory. You can restrict this system-wide by editing `/etc/sysctl.d/10-ptrace.conf` and setting `kernel.yama.ptrace_scope = 1` (or 2 for stricter admin-only access, or 3 to disable it completely until next reboot).

## 4. Process Command-Line Snooping

If an attacker lacks immediate root privileges but wants to harvest secrets passed via commands, they often turn to [pspy](https://github.com/DominicBreuker/pspy). This command-line utility snoops on executing processes without requiring root access by reading process events directly via the inotify API. It is incredibly effective for capturing automation flags, cron job executions, and plain-text keys passed as runtime parameters.

*pspy is a command line tool designed to snoop on processes without need for root permissions. It allows you to see commands run by other users, cron jobs, etc. as they execute. Great for enumeration of Linux systems in CTFs. **Also great to demonstrate your colleagues why passing secrets as arguments on the command line is a bad idea.***

![pspy](/images/fantastic_passwords/pspy_scanner.png "pspy")

Figure 1: pspy

My colleague, Asger Strunk, and I gave a presentation at BSides Munich, discussing at length how awesome `/proc` is. You might want to watch our talk.

### Defense & Hardening

* Again, never pass passwords via command-line arguments.

## 5. Backdoor Login Prompt

We investigated a compromised network where the EDR detected lateral movement from two different administrator accounts deep within the network, without triggering a single alert...