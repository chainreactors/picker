---
title: Leveraging Landlock telemetry for Linux detection engineering
url: https://blog.sekoia.io/leveraging-landlock-telemetry-for-linux-detection-engineering/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-14
fetch_date: 2026-01-15T03:32:02.223043
---

# Leveraging Landlock telemetry for Linux detection engineering

### Log in

Username or Email Address

Password

[ ]  Remember Me

 [Forgot password?](https://blog.sekoia.io/wp-login.php?action=lostpassword)

### Search the site...

Search for

* All categories
* [Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Detection Engineering](https://blog.sekoia.io/category/detection-engineering/)

####

Reset

[![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

Log in

[Detection Engineering](https://blog.sekoia.io/category/detection-engineering/ "Detection Engineering")
[Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/ "Threat Research & Intelligence")

# Leveraging Landlock telemetry for Linux detection engineering

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/04/TDR-badge.png)](#molongui-disabled-link)

[Sekoia TDR, Erwan Chevalier and Guillaume C.](#molongui-disabled-link)
January 14 2026

0

14 minutes reading

## Introduction

During our daily tracking and analysis routine at **Sekoia** **TDR** team (Threat Detection & Research), we are always searching for new relevant detection opportunities on various perimeters. Given the predominance of Linux-based systems on the server side, we decided to focus the current report on one recent security mechanism called Landlock.

[Landlock](https://landlock.io) is a relatively new Linux Security Module (LSM), integrated into the kernel since version 5.13. Its main differentiators from other LSMs are summarised in the following table from [this Landlock paper](https://landlock.io/talks/2024-06-06_landlock-article.pdf):

![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2026/01/image-5-1024x401.png)

***Figure 1.*** [***Comparison***](https://landlock.io/talks/2024-06-06_landlock-article.pdf) ***of different access control mechanism***

Landlock allows the creation of sandboxes for your applications, on top of the existing system-wide access control mechanisms. Essentially, any process, whether you trust them or not, whether they are privileged processes or unprivileged ones, can be restricted, adding a valuable layer of defence-in-depth.

Despite promising capabilities, the relative novelty of Landlock within the Linux kernel raises a critical question for detection engineering. How widely is it actually used?

To answer that question, Landlock creator [listed](https://landlock.io/talks/2025-09-30_landlock-systemd-asg.pdf) several open source projects already leveraging Landlock: *zathura, pacman, cloud hypervisor, suricata, polkadot, wireproxy, gnome localsearch, xz utils.* Several sandbox tools such as *FireJail* and *setpriv* have integrated Landlock as well. In addition, multiple private companies have already looked into Landlock for their own usage to harden their applications.

## Landlock for detection engineering

Landlock is a great hardening tool that effectively restricts an application’s actions. However, its application is not limited to system hardening, as it also presents significant value for detection engineering.

Landlock has been fully integrated within the Audit system since [Linux kernel 6.15](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=72885116069abdd05c245707c3989fc605632970). No specific audit rule is needed. By default, the execution of new programs via the `execve()` system call does not generate logs; enabling this behaviour requires passing [specific flags](https://docs.kernel.org/userspace-api/landlock.html#c.sys_landlock_restrict_self) to `sys_landlock_restrict_self()`. This default configuration is intended to mitigate false positives, given the inherent lack of control over the execution flow of the new processes. Furthermore, appropriate access rights must be defined during binary compilation, in accordance with the [official documentation](https://docs.kernel.org/userspace-api/landlock.html#access-rights).

A log being raised means two things:

* The application is not used for its original purpose since it was compiled with these Landlock restrictions.
* It should never be a false positive since the application was designed at its core with the Landlock restrictions.

For detection engineers, this new telemetry opens up new possibilities for crafting precise, behaviour-based detections that can identify threats at runtime with a very low false positive rate.

The Landlock [sandboxer example](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/samples/landlock/sandboxer.c) in C helps to understand how it works. The program allows the user to execute a process under several user-defined conditions. We can run elementary tests to validate the logging capabilities.

Every violation attempt of the restrictions applied to a program will be logged if the environment variable `LL_FORCE_LOG` is set to 1. This sets the flag `LANDLOCK_RESTRICT_SELF_LOG_NEW_EXEC_ON`, allowing the execution of new programs via the `execve()` system call.

### Filesystem Landlock rule

We start our “sandboxer” binary with an interactive “bash” shell, and restrict with Landlock the filesystem permissions to be read-only on the “/” path, and read-write on the “/tmp” path.

![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2026/01/image-1-1024x292.png)

***Figure 2. Shell commands testing Landlock filesystem rule***

If we try to write anywhere else other than “/tmp”, the audit logging gives us these raw [documented](https://docs.kernel.org/admin-guide/LSM/landlock.html) Landlock audit messages:

```
type=UNKNOWN[1423] msg=audit(1764079004.833:1261): domain=1266faee0 blockers=fs.make_reg path="/home/user/sandbox_c" dev="sda1" ino=1183972
```

At the time of writing this, the [audit userspace tools](https://github.com/linux-audit/audit-userspace) were not updated with the audit kernel type of messages: the 1423 message code is the following one:

```
#define AUDIT_LANDLOCK_ACCESS   1423    /* Landlock denial */
```

Using the [go-libaudit library](https://github.com/elastic/go-libaudit), audit messages are reassembled and enriched with system context in a single event that could be used for detection or hunting :

```
{"@timestamp":"2025-11-25T13:46:48.03Z","sequence":1228,"category":"mac","record_type":"unknown[1423]","result":"fail","session":"unset","tags":["x86_64"],"summary":{"actor":{"primary":"unset","secondary":"user"},"ob...