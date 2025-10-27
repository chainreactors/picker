---
title: A Journey From `sudo iptables` To Local Privilege Escalation
url: https://www.shielder.com/blog/2024/09/a-journey-from-sudo-iptables-to-local-privilege-escalation/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-21
fetch_date: 2025-10-06T18:30:55.121464
---

# A Journey From `sudo iptables` To Local Privilege Escalation

[![shielder logo homepage](https://www.shielder.com/img/logoshielder.svg)](https://www.shielder.com/ "homepage")

* [Home](https://www.shielder.com/ "Home")
* [Company](https://www.shielder.com/company "Company")
* [Services](https://www.shielder.com/services "Services")
* [Advisories](https://www.shielder.com/advisories "Advisories")
* [Blog](https://www.shielder.com/blog "Blog")
* [Careers](https://www.shielder.com/careers "Careers")
* [Contacts](https://www.shielder.com/contacts "Contacts")
* ENG

  [ENG](https://www.shielder.com/blog/2024/09/a-journey-from-sudo-iptables-to-local-privilege-escalation/ "ENG")
  [ITA](https://www.shielder.com/it/blog/2024/09/a-journey-from-sudo-iptables-to-local-privilege-escalation/ "ITA")

# A Journey From `sudo iptables` To Local Privilege Escalation

![](/img/blog/sudo_iptables_og.jpg)

## TL;DR

A low-privileged user on a Linux machine can obtain the `root` privileges if:

* They can execute `iptables` and `iptables-save` with `sudo` as they can inject a fake `/etc/passwd` entry in the comment of an `iptables` rule and then abusing `iptables-save` to overwrite the legitimate `/etc/passwd` file.
* They can execute `iptables` with `sudo` and the underlying system misses one of the kernel modules loaded by `iptables`. In this case they can use the `--modprobe` argument to run an arbitrary command.

## Intro

If you’ve ever played with *boot2root* CTFs (like Hack The Box), worked as a penetration tester, or just broke the law by infiltrating random machines (NO, DON’T DO THAT), chances are good that you found yourself with a low-privileged shell - `www-data`, I’m looking at you - on a Linux machine.

Now, while shells are great and we all need to be grateful when they shine upon us, a low-privileged user typically has a limited power over the system. The path ahead becomes clear: we need to escalate our privileges to `root`.

![](/img/blog/why_root.png)

When walking the path of the Privilege Escalation, a hacker has [a number of tricks](https://book.hacktricks.xyz/linux-hardening/privilege-escalation) at their disposal; one of them is using `sudo`.

## superuser do…substitute user do…just call me sudo

As the reader might already know well, the `sudo` command can be used to run a command **with the permissions of another user** – which is commonly `root`.

> Ok, but what’s the point? If you can `sudo <command>` already, privilege escalation is complete!

Well, yes, but actually, no. In fact, there are two scenarios (at least, two that come to mind right now) where we can’t simply leverage `sudo` to run arbitrary commands:

1. Running `sudo` requires the password of the user, and even though we have a shell, we don’t know the password. This is quite common, as the initial access to the box happens via an exploit rather than regular authentication.
2. We may know the password for `sudo`, but the commands that the user can run with `sudo` are restricted.

In the first case, there’s only one way to leverage `sudo` for privilege escalation, and that is `NOPASSWD` commands. These are commands that can be launched with `sudo` by the user **without a password prompt**. Quoting from `man sudoers`:

> NOPASSWD and PASSWD
>
> By default, sudo requires that a user authenticate him or herself before running a command. This behavior can be modified via the NOPASSWD tag. Like a Runas\_Spec, the NOPASSWD tag sets a default for the commands that follow it in the Cmnd\_Spec\_List. Conversely, the PASSWD tag can be used to reverse things. For example:
>
> ray rushmore = NOPASSWD: /bin/kill, /bin/ls, /usr/bin/lprm
> would allow the user ray to run /bin/kill, /bin/ls, and /usr/bin/lprm as root on the machine rushmore without authenticating himself.

The second case is a bit different: in that scenario, even though we know the password, there will be only a limited subset of commands (and possibly arguments) that can be launched with `sudo`. Again, the way this works you can learn by looking at `man sudoers`, asking ChatGPT or wrecking your system by experimenting.

In both cases, there is a quick way to check what are the “rules” enabled for your user, and that is running `sudo -l` on your shell, which will help answering the important question: *CAN I HAZ SUDO?*

## $ sudo run-privesc

Now, back to the topic of privilege escalation. The bad news is that, when `sudo` is restricted, we cannot run arbitrary commands, thus the need for some more ingredients to obtain a complete privilege escalation. How? This is the good news: we can leverage side-effects of allowed commands. In fact, Linux utilities, more often than not, support a plethora of flags and options to customize their flow. By using and chaining these options in creative ways, even a simple text editor can be used as a trampoline to obtain arbitrary execution!

For a simple use case, let’s consider the well-known `tcpdump` command, used to listen, filter and display network packets traveling through the system. Administrators will oftentimes grant low-privileged users the capability to dump traffic on the machine for debugging purposes, so it’s perfectly common to find an entry like this when running `sudo -l`:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` (ALL) NOPASSWD: /usr/bin/tcpdump ``` |

Little do they know about the power of UNIX utilities! In fact, `tcpdump` automagically supports *log rotation*, alongside a convenient `-z` flag to supply a `postrotate-command` that is executed after every rotation. Therefore, it is possible to leverage `sudo` coupled with `tcpdump` to execute arbitrary commands as root by running the following sequence of commands:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` COMMAND='id' # just replace 'id' with your evil command TF=$(mktemp) echo "$COMMAND" > $TF chmod +x $TF tcpdump -ln -i lo -w /dev/null -W 1 -G 1 -z $TF ``` |

The good folks at [GTFOBins](https://gtfobins.github.io/) maintain a curated list of these magic tricks (including the one just shown about `tcpdump`), so please bookmark it and make sure to look it up on your Linux privilege escalation quests!

## Starting Line ð¦

Recently, during a penetration test, we were looking for a way to escalate our privileges on a Linux-based device. What we had was a shell for a (very) low-privileged user, and the capability to run a certain set of commands as `sudo`. Among these, two trusted companions for every network engineer: `iptables` and `iptables-save`.

Sure there must be an entry for one of these two guys in GTFOBins, or so we thought … which lead in going once more for the extra mileâ¢.

## Pepperidge Farm Remembers

Back in the 2017 we organized an in-person CTF in Turin partnering with the [PoliTO University](https://www.polito.it), [JEToP](https://jetop.com), and [KPMG](https://kpmg.com/).

The CTF was based on a set of boot2root boxes where the typical entry point was a web-based vulnerability, followed by a local privilege escalation. One of the privilege escalations scenarios we created was exactly related to `iptables`.

The technique needed to root the box has been documented in a [CTF writeup](https://jbz.team/turinctf2017/turinctf_finals#6) and used to [root a PAX payment device](https://git.lsd.cat/g/pax-pwn/src/master/Readme.md#privilege-escalation-cve-2020-28046).

### Modeprobing Our Way To Root

`iptables` has a `--modprobe`, which purpose we can see from its `man` page:

```
--modprobe=command
When adding or inserting rules into a chain, use command to load any necessary modules (targets, match extensions, etc).
```

Sounds like an interesting way for to run an arbitrary command, doesn’t it?

By inspecting the [`iptables` source code](https://github.com/cernekee/iptables/blob/upstream/libxtables/xtables.c#L403) we can see that if the `--modprobe` flag has been specifies, then the `int xtables_load_ko(const char *modprobe, bool quiet)` function is called with as first parameter the modprobe command specified by the user.

As a first step the `xtables_load_ko` f...