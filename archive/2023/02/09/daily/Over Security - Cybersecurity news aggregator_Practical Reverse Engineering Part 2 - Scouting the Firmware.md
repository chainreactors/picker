---
title: Practical Reverse Engineering Part 2 - Scouting the Firmware
url: https://jcjc-dev.com/2016/04/29/reversing-huawei-router-2-scouting-firmware/
source: Over Security - Cybersecurity news aggregator
date: 2023-02-09
fetch_date: 2025-10-04T06:09:16.477417
---

# Practical Reverse Engineering Part 2 - Scouting the Firmware

# [Hack The World](https://jcjc-dev.com)

Projects and learnt lessons on Systems Security, Embedded Development, IoT and anything worth writing about

[Archive](/archive/)
[Consulting](/consulting/)
[Juan Carlos Jimenez](https://uk.linkedin.com/in/juan-carlos-jim%C3%A9nez-bba49033/en)
[Twitter](https://twitter.com/Palantir555)
[GitHub](https://github.com/Palantir555)
e-mail

# Practical Reverse Engineering Part 2 - Scouting the Firmware

29 Apr 2016

* [Part 1](https://jcjc-dev.com/2016/04/08/reversing-huawei-router-1-find-uart/):
  Hunting for Debug Ports
* **Part 2**: Scouting the Firmware
* [Part 3](https://jcjc-dev.com/2016/05/23/reversing-huawei-3-sniffing/):
  Following the Data
* [Part 4](https://jcjc-dev.com/2016/06/08/reversing-huawei-4-dumping-flash/):
  Dumping the Flash
* [Part 5](https://jcjc-dev.com/2016/12/14/reversing-huawei-5-reversing-firmware/):
  Digging Through the Firmware

In part 1 we found a debug UART port that gave us access to a Linux shell. At
this point we’ve got the same access to the router that a developer would use to
debug issues, control the system, etc.

This first overview of the system is easy to access, doesn’t require expensive
tools and will often yield very interesting results. If you want to
do some hardware hacking but don’t have the time to get your hands too dirty,
this is often the point where you stop digging into the hardware and start
working on the higher level interfaces: network vulnerabilities, ISP
configuration protocols, etc.

These posts are hardware-oriented, so we’re just gonna use this access to gather
some random pieces of data. Anything that can help us understand the system or
may come in handy later on.

Please check out the
[legal disclaimer](https://gist.github.com/Palantir555/de23c2ceb5355efe6ec105a8d2d73486)
in case I come across anything sensitive.

*Full disclosure: I’m in contact with Huawei’s security team; they’ve had time
to review the data I’m going to reveal in this post and confirm there’s nothing
too sensitive for publication. I tried to contact TalkTalk, but their security
staff is nowhere to be seen.*

## Picking Up Where We Left Off

![Picture of Documented UARTs](https://jcjc-dev.com/assets/practical-reversing/znXRocn.jpg)

We get our serial terminal application up and running in the computer and power
up the router.

![Boot Sequence](https://jcjc-dev.com/assets/practical-reversing/t43E8dm.jpg)

We press `enter` and get the login prompt from `ATP Cli`; introduce the
credentials `admin:admin` and we’re in the ATP command line. Execute the command
`shell` and we get to the BusyBox CLI (more on BusyBox later).

```
-------------------------------
-----Welcome to ATP Cli------
-------------------------------
Login: admin
Password:    #Password is ‘admin'
ATP>shell
BusyBox vv1.9.1 (2013-08-29 11:15:00 CST) built-in shell (ash)
Enter 'help' for a list of built-in commands.
# ls
var   usr   tmp   sbin  proc  mnt   lib   init  etc   dev   bin
```

At this point we’ve seen the 3 basic layers of firmware in the Ralink IC:

1. U-boot: The device’s bootloader. It understands the device’s memory map,
   kickstarts the main firmware execution and takes care of some other low level
   tasks
2. Linux: The router is running Linux to keep overall control of the hardware,
   coordinate parallel processes, etc. Both ATP CLI and BusyBox run on top of it
3. Busybox: A small binary including reduced versions of multiple linux
   commands. It also supplies the `shell` we call those commands from.

Lower level interfaces are less intuitive, may not have access to all the data
and increase the chances of bricking the device; it’s always a good idea to
start from BusyBox and walk your way down.

For now, let’s focus on the boot sequence itself. The developers thought it would
be useful to display certain pieces of data during boot, so let’s see if there’s
anything we can use.

## Boot Debug Messages

We find multiple random pieces of data scattered across the boot sequence. We’ll
find useful info such as the compression algorithm used for some flash segments:

![boot msg kernel lzma](https://jcjc-dev.com/assets/practical-reversing/9pRc2mP.jpg)

Intel on how the external flash memory is structured will be very useful when we
get to extracting it.

![ram data. not very useful](https://jcjc-dev.com/assets/practical-reversing/OmDkAxX.jpg)

![SPI Flash Memory Map!](https://jcjc-dev.com/assets/practical-reversing/ODnxzJY.jpg)

And more compression intel:

![root is squashfs'd](https://jcjc-dev.com/assets/practical-reversing/Qw6Z08z.jpg)

We’ll have to deal with the compression algorithms when we try to access the raw
data from the external Flash, so it’s good to know which ones are being used.

## What Are ATP CLI and BusyBox Exactly? [Theory]

The Ralink IC in this router runs a Linux kernel to control memory and parallel
processes, keep overall control of the system, etc. In this case, according to
the Ralink’s
[product brief](https://wikidevi.com/files/Ralink/RT3352%20product%20brief.pdf),
they used the `Linux 2.6.21 SDK`. `ATP CLI` is a CLI running either on top of
Linux or as part of the kernel. It provides a first layer of authentication into
the system, but other than that it’s very limited:

```
ATP>help
Welcome to ATP command line tool.
If any question, please input "?" at the end of command.
ATP>?
cls
debug
help
save
?
exit
ATP>
```

`help` doesn’t mention the `shell` command, but it’s usually either `shell` or
`sh`. This ATP CLI includes less than 10 commands, and doesn’t support any kind
of complex process control or file navigation. That’s where BusyBox comes in.

BusyBox is a single binary containing reduced versions of common unix
commands, both for development convenience and -most importantly- to save memory.
From `ls` and `cd` to `top`, System V init scripts and pipes, it allows us to
use the Ralink IC somewhat like your regular Linux box.

One of the utilities the BusyBox binary includes is the shell itself, which has
access to the rest of the commands:

```
ATP>shell
BusyBox vv1.9.1 (2013-08-29 11:15:00 CST) built-in shell (ash)
Enter 'help' for a list of built-in commands.
# ls
var   usr   tmp   sbin  proc  mnt   lib   init  etc   dev   bin
#
# ls /bin
zebra        swapdev      printserver  ln           ebtables     cat
wpsd         startbsp     pppc         klog         dns          busybox
wlancmd      sntp         ping         kill         dms          brctl
web          smbpasswd    ntfs-3g      iwpriv       dhcps        atserver
usbserver    smbd         nmbd         iwconfig     dhcpc        atmcmd
usbmount     sleep        netstat      iptables     ddnsc        atcmd
upnp         siproxd      mount        ipp          date         at
upg          sh           mldproxy     ipcheck      cwmp         ash
umount       scanner      mknod        ip           cp           adslcmd
tr111        rm           mkdir        igmpproxy    console      acl
tr064        ripd         mii_mgr      hw_nat       cms          ac
telnetd      reg          mic          ethcmd       cli
tc           radvdump     ls           equipcmd     chown
switch       ps           log          echo         chmod
#
```

You’ll notice different BusyBox quirks while exploring the filesystem, such
as the symlinks to a `busybox` binary in
[/bin/](https://gist.github.com/Palantir555/443168b4f1c0b34bab5b28bb1845d10e).
That’s good to know, since **any commands that may contain sensitive data will
not be part of the BusyBox binary**.

## Exploring the File System

Now that we’re in the system and know which commands are available, let’s see if
there’s anything useful in there. We just want a first overview of the system,
so I’m not gonna bother exposing every tiny piece of data.

The `top` command will help us identify which processes are consuming the most
resources. This can be an extremely good indicator of whether some processes are
important or not. It doesn’t say much while the router’s idle, though:

![top](ht...