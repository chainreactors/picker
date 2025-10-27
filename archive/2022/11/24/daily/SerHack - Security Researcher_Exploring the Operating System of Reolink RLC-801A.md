---
title: Exploring the Operating System of Reolink RLC-801A
url: https://serhack.me/articles/operating-system-reolink-rlc-810-a/
source: SerHack - Security Researcher
date: 2022-11-24
fetch_date: 2025-10-03T23:41:34.574711
---

# Exploring the Operating System of Reolink RLC-801A

[![SerHack logo](https://serhack.me/images/serhack-120.png)

SerHack Security Research](https://serhack.me/)

[ ]

[About](https://serhack.me/about/ "About")
[Blog](https://serhack.me/blog/ "Blog")
[Books](https://serhack.me/books/ "Books")
[EN](https://serhack.me/articles/operating-system-reolink-rlc-810-a/ "en version")
[IT](https://serhack.me/it/articles/sistema-operativo-reolink-rlc-810-a/ "it version")

# Exploring the Operating System of Reolink RLC-810A

Published at November 23, 2022 – 16 min read – 3232 words

![Exploring the Operating System of Reolink RLC 801A](https://serhack.me/images/articles/reolink-firmware/reolink_5_800px.jpg)

In [Part 4](https://serhack.me/articles/understanding-ubi-file-system-embedded-devices-reolink/) of our series, we focused on the file system and before concluding, we were able to extract files from two UBIFS images contained within the firmware. Here in Part 5, we will try to better understand the structure of the root file system by introducing some basic concepts of the operating system used by Reolink RLC-810A, namely Linux.

## Why Linux?

Linux kernel is one of the most widely used operating systems in the world, if not the first by popularity. You might think that commercial operating systems such as Windows or macOS are the most widely used, but on the other hand a whole army of embedded devices (such as the camera in this series) have based their firmware on Linux.

Created in the early 1990s by Linus Torvalds, the Linux kernel is a monolithic, modular, multitasking kernel primarily developed in response to the commercialization of the Unix operating system maintained by AT&T. The Linux kernel and the entire ecosystem above it is largely open-source — every person on the planet is free to be able to consult the sources and modify them.

The choice of Linux as the basis for embedded device firmware stems from a number of features that are essential for development. First among them is the flexibility of Linux — i.e, through being modular, it is possible to load additional components at runtime that enrich Linux with new features. The second is given by the stability of the kernel, thanks to Linux’s dedicated developer community and the wide dissemination of the kernel that has allowed more eyes on code development. The third reason is perhaps one of the most important — it is free. When you market a device, there are a number of licenses that the company has to pay for (hardware, various devices, etc.). For companies that use Linux in their products, there is no cost.

Before we begin to analyze the various folders, it is important to note that almost all operating systems used for embedded devices are a distribution based on the Linux kernel. The characteristics of being open-source, having extensive online support, and being a fairly stable kernel have made the entire family of Linux/Unix-based operating systems the ideal operating system for this type of device.

## The Folders of the File System.

Let’s continue our analysis and explore in detail the structure of the operating system. First, we change the directory to `rootfs`. Then, we run `ls` to get a more complete overview of the directories.

```
bin dev etc init lib linuxrc mnt proc root sbin sys tmp usr var
```

As we might expect, this is the FileSystem Hierarchy Standard feature used for file systems in Unix-like operating systems. In fact, the standard defines which folders and virtual file systems are to be mounted at boot time by the operating system and what each folder contains. This standard is shared among all Unix-like operating systems to ensure compatibility between programs on different platforms.

Let’s explore each folder and file in more detail:

* `bin`: contains binary files shared by all users. In this folder we find the shell, cat, ls, cp, and many others.
* `dev`: contains files for peripherals (devices). Most Unix-like operating systems adopt the “Everything as a file” approach where each peripheral is described by some special files that allow manipulating the state of a device. It also contains other pseudo-virtual devices such as `/dev/null` which produces no output or `/dev/random` which generates pseudo-random numbers.
* `etc`: contains system configuration files. It is a very interesting folder that allows you to understand how the manufacturer configured the camera.
* `init`: the executable that U-Boot loads and executes at the beginning of booting.
* `lib`: contains essential libraries for binaries in /bin/ and /sbin/.
* `linuxrc`: file that is executed by init to start populating and mounting some virtual file systems (such as dev, proc).
* `mnt`: destination used to mount additional file systems (temporarily).
* `proc`: virtual file system that contains information about active processes (mainly readable as text files).
* `root`: the root folder for the “root” or “supervisor” user.
* `sbin`: folder similar to sbin, differing only in the binaries it contains. In this case, they are binaries that must be run by root for system administration.
* `sys`: file system that allows interfacing directly with hardware devices.
* `tmp`: temporary folder. The files inside are generally deleted when the system is rebooted.
* `usr`: contains applications and files used by users. Applications such as browsers, instant messaging, and anything not used by the system are put in this folder.
* `var`: files with variable data. In particular, we have `/var/log` which contains the logs produced by the various system components and applications.

Now that we have introduced the different folders, we can begin to explore their contents one by one. Over the course of the next few articles, we will be looking at getting to the bottom of some of the folders to better understand their meaning.

## Bin Folder

The bin folder contains the essential binary files for the operating system. Inside we find executables such as `ls` (to get a list of files), `cp` (to copy a file), `echo` (to print a string to the screen), etc.

In our case, we can proceed to see the various binaries in more detail using `ls`.

```
ash      chmod     date           echo     fgrep   hostname  linux64  mkdir   netstat       ping           rc_profile    setarch    su        umount      zcat
busybox  chown     dd             ed       fsync   hush      ln       mknod   nice          ping6          rev           setserial  sync      uname
cat      conspy    df             egrep    getopt  iostat    login    more    nvtrtspd      pq_video_rtsp  rm            sh         tar       uncompress
catv     cp        dmesg          false    grep    ipcalc    ls       mount   nvtrtspd_2ch  printenv       rmdir         sleep      test_vos  usleep
chattr   cpio      dnsdomainname  fatattr  gunzip  kill      lsattr   mpstat  nvtrtspd_ipc  ps             scriptreplay  stat       touch     vi
chgrp    cttyhack  dumpkmap       fdflush  gzip    linux32   lzop     mv      pidof         pwd            sed           stty       true      watch
```

Many of these are commands routinely found in any operating system. The `mkdir` (make directory) command in Linux/Unix allows users to create or make new directories. With `mkdir`, you can also set permissions, create multiple directories (folders) at once, etc. What is immediately eye-catching, however, are some particular binary files that are not customarily found in Unix-like distributions, such as `nvtrtspd` or `pq_video_rtsp`. We will return to these because they seem to be interesting binaries.

Let’s then proceed to identify the shell. The shell is a command-line interface used to interface with the operating system — you can execute commands, request programs to start, and change settings. Along with the kernel, it is a fundamental component of an operating system.

There are several popular textual shells — with Bash being the most famous. Bash is used for GNU/Linux systems, but also cmd.exe for Windows, Z Shell for macOS. For Reolink ...