---
title: PrivEsc on a production-mode POS
url: https://labs.yarix.com/2023/03/privesc-on-a-production-mode-pos/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-31
fetch_date: 2025-10-04T11:16:20.557086
---

# PrivEsc on a production-mode POS

[![YLabs](//labs.yarix.com/wp-content/uploads/2025/01/Logo_Yarix.png)![YLabs](//labs.yarix.com/wp-content/uploads/2021/01/yarix_logo.png)![YLabs](//labs.yarix.com/wp-content/uploads/2025/01/Logo_Yarix.png)](https://labs.yarix.com/ "YLabs - Research & Development")

* [Home](https://labs.yarix.com/)
* [Blog](https://labs.yarix.com/category/blog/)
* [Advisories](https://labs.yarix.com/advisories/)
* [Careers](https://www.yarix.com/job-opportunity/)

# PrivEsc on a production-mode POS

* [Home](https://labs.yarix.com "Go to Home Page")
* PrivEsc on a production-mode POS

[Back to Posts](https://labs.yarix.com)

![](https://labs.yarix.com/wp-content/uploads/2023/03/pos-1024x445.jpg)

30Mar30/03/2023

## PrivEsc on a production-mode POS

[Ylabs](https://labs.yarix.com/author/ylabs/ "Posts by Ylabs")2023-03-31T09:05:11+02:00

By
[Ylabs](https://labs.yarix.com/author/ylabs/ "Posts by Ylabs")

Reading Time:   8 minutes

Earlier this year, we were involved in the security assessment of a mobile application that included the use and verification of a POS, a Pax D200. An Internet search aimed at identifying any known vulnerabilities about it, led us to [this](https://git.lsd.cat/g/pax-pwn/src/master) post called *pax-pwn* and written by *lsd.cat* where three CVEs were reported and described (CVE-2020-28044, CVE-2020-28045, CVE-2020-28046). The vulnerabilities description were quite detailed, however there were some differences between the POS used in their case and the one in our possession, as well as some details that were not thoroughly explored. In our case, ours was a production POS and not a development one (i.e., debug level 0 and thus no shell available). As a result, many of the steps described by the author, which were necessary to complete the path to privilege escalation, were not directly applicable.

This post will describe how, by adapting the previous vulnerabilities to our case, we were able to execute code on our production device and how we obtained root privileges on it. In particular, we will show how to replace the application libraries in order to execute a shell on the device via WiFi.

## Compiling USB drivers

Since the compiled driver was available directly in a repository mentioned in the *pax-pwn* post, we decided to start using the serial connection via USB cable to communicate with the device. However, this driver had been compiled for an older version of the Linux kernel and was not valid to be used on a up-to-date one.

![Old drivers not working](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x15.jpg)

*Figure 01 – Old drivers not working*

In the same repository the driver source code was also available, so we tried to compile it. Unfortunately, since its upload in 2020, the major release 6.0 of the Linux kernel was distributed, which included many changes with respect to the previous one. For this reason, once we started compiling, we immediately received some errors in the output, starting from the *Makefile*.

![Error in Makefile](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x18.jpg)

*Figure 02 – Error in Makefile*

As can be seen from the previous image, the correction to the error was described directly in the output. In fact, in the line of code `$(MAKE) modules -C $(KERNEL_DIR) SUBDIRS=$(shell pwd)` it was enough to replace SUBDIRS with M. This worked, but many other errors appeared.

![Errors in ttyPos.c](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x45.jpg)

*Figure 03 – Errors in ttyPos.c*

From here on, we are using *ttyPos.c* row numbers shown in the previous image as errors reference.
Errors at rows 986 and 992 were quite simple to correct. Sometime between 2020 and 2022, the `tty_operations` struct definition (form Linux kernel header file *tty\_driver.h*) changed and data types `write_room` and `chars_in_buffer` moved from *int* to *unsigned int*. So, changing the return type of the functions `pos_write_room` and `pos_chars_in_buffer` from *int* to *unsigned int* did the trick.
Errors at rows 1245, 1299 and 1310 were also due to changes to the Linux kernel `tty_driver` infrastructure. Digging around we came across some commits that referred these very changes:

1. [tty: stop using alloc\_tty\_driver](https://github.com/torvalds/linux/commit/39b7b42be4a82f036c392abc71724b4b7752ac03)
2. [tty: drop put\_tty\_driver](https://github.com/torvalds/linux/commit/9f90a4ddef4e4d3aa4229f6b117d4e57231457b3)

In short, interfaces `alloc_tty_driver` and `put_tty_driver` were dropped respectively in favor of `tty_alloc_driver` and `tty_driver_kref_put`. While for the latter the change was, at least for us, as simple as changing the interface name, the former required a new formal parameter. This parameter is a flag that tells the kernel how to register new devices discovered in the system. There were many flags available for it but, following a change from [this thread](https://lore.kernel.org/lkml/20210723074317.32690-1-jslaby%40suse.cz/T/), we set it to *0*. Apparently, this was enough to solve the error but, after recompiling, a new one appeared.

![Errors in ttyPos.c](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x23.jpg)

*Figure 04 – Error about do\_exit function in ttyPos.c*

The `do_exit(long error_code)` function is used to terminate a process properly, performing the operations necessary to clean up the resources used by the process. Now, following a Linux kernel 2021 [commit](https://github.com/torvalds/linux/commit/eb55e716ac1aa0de13ef5abbf1479d995582d967), this function is no longer exported. To quickly fix this, we replaced it with a return statement and eventually we successfully compiled the driver. Now, by connecting the POS via USB, it was correctly recognized by the system as a *tty* device.

![Device correctly recognized](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x32.jpg)

*Figure 05 – Device correctly recognized*

To summarize, below is the list of changes, described above, that were necessary in order to correctly compile the driver on the version 6.0.x of the Linux kernel.

![List of all changes](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x58.jpg)

*Figure 06 – List of all changes*

Later on, we also tried the POS network connection (which uses WiFi) and, after verifying that the functionalities were the same for both methods, we decided to continue using the latter as we found it more convenient.
All of this was not wasted time, however, but an excellent review of the Linux kernel and the *C* language.

## Exploiting CVE-2020-28044

By having a connection to the POS, we could try to exploit the three known vulnerabilities. As described in the *pax-pwn* post, however, we first had to enable the debugging service on the device and, to do so, we had to access the management interface. Here we were presented with a first slight difference from what was reported in the post: even for our D200, to enter that interface, we had to continuously press the *“2”* key (as for the S900 in the post) and not the *“F2”* key as reported.
Pax provides a command-line tool for developers called *XCB* (Xos Communication Bridge) which is a modified version of *ADB* (Android Debug Bridge) but with limited functionalities. To bypass these limitations, lsd.cat has written and made available on one of its [repositories](https://git.lsd.cat/g/prolin-xcb-client) a *Python* script that re-implements some of the basic functionality of *ADB* including the ability to list, read and write files on the device. The only modification that needed to be made in order to use this script was to change the IP address hardcoded into it.

![Device file system listing via client.py](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x49.jpg)

*Figure 07 – Device file system listing via client.py*

By exploring the system with the commands made available by the client.py script, we were able to dump all the files and dir...