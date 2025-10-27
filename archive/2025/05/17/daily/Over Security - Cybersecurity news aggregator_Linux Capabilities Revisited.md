---
title: Linux Capabilities Revisited
url: https://dfir.ch/posts/linux_capabilities/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-17
fetch_date: 2025-10-06T22:28:00.616196
---

# Linux Capabilities Revisited

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

# Linux Capabilities Revisited

16 May 2025

**Table of Contents**

* [Introduction](#introduction)
* [Understanding Capabilities](#understanding-capabilities)
* [Backdooring Python](#backdooring-python)
* [Testing](#testing)
* [Hunting](#hunting)
* [LinPeas](#linpeas)
* [Elastic rule: Process Capability Set via setcap Utility](#elastic-rule-process-capability-set-via-setcap-utility)
* [security.capability](#securitycapability)
* [Conclusion](#conclusion)
* [References](#references)

## Introduction

**Notes to kernel developers**: *The goal of capabilities is divide the power of superuser into pieces, such that if a program that has one or more capabilities is compromised, its power to do damage to the system would be less than the same program running with root privilege.* [Capabilities(7) â Linux manual page](https://man7.org/linux/man-pages/man7/capabilities.7.html)

`Capabilities` are a fine-grained access control mechanism in Linux, allowing more granular permissions than the traditional superuser (`root`) model. Capabilities divide the privileges typically associated with the root user into distinct units that can be independently enabled or disabled for different processes. This allows for more secure and controlled privilege management.

For example, a process may need permission to bind to privileged ports but not require any other elevated permissions.

## Understanding Capabilities

To see how many capabilities our Linux host is aware of, we can query the file `cap_last_cap` inside the `/proc` directory:

```
# cat /proc/sys/kernel/cap_last_cap
40
```

The `capsh --print` command displays the current capabilities and related settings of the shell or the process invoking the command. When executing this command on our Linux host, we see the full list of capabilities.

```
# capsh --print
Current: =ep
Bounding set =cap_chown,cap_dac_override,cap_dac_read_search,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_linux_immutable,cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw,cap_ipc_lock,cap_ipc_owner,cap_sys_module,cap_sys_rawio,cap_sys_chroot,cap_sys_ptrace,cap_sys_pacct,cap_sys_admin,cap_sys_boot,cap_sys_nice,cap_sys_resource,cap_sys_time,cap_sys_tty_config,cap_mknod,cap_lease,cap_audit_write,cap_audit_control,cap_setfcap,cap_mac_override,cap_mac_admin,cap_syslog,cap_wake_alarm,cap_block_suspend,cap_audit_read,cap_perfmon,cap_bpf,cap_checkpoint_restore
```

Each capability corresponds to a specific privileged action.

## Backdooring Python

The command `setcap` sets file capabilities on an executable. The `cap_setuid` capability allows a process to make arbitrary manipulations of user IDs (UIDs), including setting the UID to a value that would otherwise be restricted (i.e. `UID 0`, the root user). `setcap` takes a set of parameters, where

* `e`: Effective means the capability is activated
* `p`: Permitted means the capability can be used/is allowed.

Putting this together, we’re adding the `cap_setuid` capabilities to the Python binary:

```
# setcap cap_setuid+ep /usr/bin/python3.12
```

One can find a list of supported capabilities here:

```
# cat /usr/include/linux/capability.h
```

## Testing

For testing purposes, we created a new user (`malmoeb`) and switched to the context of this user (`useradd && su`):

```
# useradd -m malmoeb
# su malmoeb
$ id
uid=1000(malmoeb) gid=1000(malmoeb) groups=1000(malmoeb)
```

Using the following command line, we set the UID of the bash shell we are calling with Python to 0 (`UID 0 == root`), effectively spawning a root shell:

```
$ /usr/bin/python3 -c 'import os;os.setuid(0);os.system("/bin/bash")'
# id
uid=0(root) gid=1000(malmoeb) groups=1000(malmoeb)
```

The exciting thing about this technique is that we have not set a suid bit on a binary, or changed the Python binary. By setting the capabilities, we, as attackers, can build a powerful backdoor.

## Hunting

Traditionally, system administrators and security professionals have focused on finding `SUID` (Set User ID) and `SGID` (Set Group ID) files, because these files can be used to escalate privileges under certain conditions. However, with the introduction of POSIX capabilities, it is now equally important to hunt for files with capabilities set, as demonstrated above.

Enumerating all binaries with capabilities set is possible with the command `getcap -r`:

```
# getcap -r / 2>/dev/null
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper cap_net_bind_service,cap_net_admin,cap_sys_nice=ep
/usr/bin/mtr-packet cap_net_raw=ep
/usr/bin/ping cap_net_raw=ep
/usr/bin/python3.12 cap_setuid=ep
```

Inside the /proc directory:

```
# cat /proc/1143966/status | grep Cap
```

where:

* `CapInh` = Inherited capabilities
* `CapPrm` = Permitted capabilities
* `CapEff` = Effective capabilities
* `CapBnd` = Bounding set
* `CapAmb` = Ambient capabilities set

Utilising the command `capsh`, we decode the capabilities as follows:

```
# capsh --decode=0000000000000080
0x0000000000000080=cap_setuid
```

Or with the command `getpcaps`, passing the PID as an argument:

```
# getpcaps 1143966
Capabilities for `1143966': = cap_setuid+ep
```

Remove the capabilities from a binary with `setcap -r`

```
# setcap -r /usr/bin/python3.12
```

## LinPeas

[LinPEAS](https://github.com/peass-ng/PEASS-ng/tree/master/linPEAS), the *Linux Privilege Escalation Awesome Script*, also performs some checks to find (interesting) capabilities. Following the commands taken directly from the relevant [script](https://github.com/peass-ng/PEASS-ng/blob/516aafff276ce486866e30e9553146cf912f591d/linPEAS/builder/linpeas_parts/8_interesting_perms_files/4_Capabilities.sh):

* **Current shell capabilities:** `cat "/proc/$$/status"`
* **Parent process capabilities:** `cat "/proc/$PPID/status"`
* **Files with capabilities:** `getcap -r / 2>/dev/null`

Besides checking for `suid` files, LinPEAS does an excellent job here for searching for (hidden) capabilities discussed so far.

## Elastic rule: Process Capability Set via setcap Utility

Elastic “*detects the use of the setcap utility to set capabilities on a process.*” See [here](https://www.elastic.co/docs/reference/security/prebuilt-rules/rules/linux/persistence_process_capability_set_via_setcap) for the full description.

```
process where host.os.type == "linux" and event.type == "start" and event.action in ("exec", "exec_event", "start") and
process.name == "setcap" and not (
  process.parent.executable == null or
  process.parent.executable : ("/var/lib/dpkg/*", "/var/lib/docker/*", "/tmp/newroot/*", "/var/tmp/newroot/*") or
  process.parent.name in ("jem", "vzctl")
)
```

## security.capability

Extended permissionsâsuch as `access control lists` (ACLs) set with [setfacl](https://dfir.ch/posts/today_i_learned_setfacl/) and capability flags set with `setcap` are stored in the same location as traditional permission bits and setuid/setgid flags configured via chmod: the fileâs inode.

The `ls` command does not display capability flags set by `setcap`. To view them, use `getcap`. To list all extended attributes, you can use `getfattr -d -m -`. The attribute `setcap` uses isÂ `security.capability`, and itâs stored in a binary format that `getcap` conveniently decodes for you.

```
# getfattr -d -m - /usr/bin/python3.12
getfattr: Removing leading '/' from absolute path names
    # file: usr/bin/python3.12
security.capability=0sAQAAAoAAAAAAAAAAAAAAAAAAAAA=
```

## Conclusion

While traditional SUID/SGID checks are still crucial, modern security practices must include hunting for files with specific capabilities set. Capabilities provide a more granular and potentially stealthy way to grant necessary privileges, and if not monitored, they can introduce significant security risks. Using tools likeÂ `getcap`Â to search the file system for these capabilities recursiv...