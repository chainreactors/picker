---
title: OpenSSH Issues Emergency Fix for Flaw Letting Long Passwords Bypass SSH Auth on Alpine Linux
url: https://thehackernews.com/2026/11/openssh-issues-emergency-fix-for-flaw.html
source: The Hacker News
date: 2026-11-05
fetch_date: 2026-11-06T08:41:47.470432
---

# OpenSSH Issues Emergency Fix for Flaw Letting Long Passwords Bypass SSH Auth on Alpine Linux

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg98jBiF1GNyn9ReXVuuNzrDrJ8-mdCvE5IhR6dUbEnucAAvmCW-lbjZmzjJx0EhFV2R6xhfph0uQ-cz4IO46xmarphU8oOZmuqbdHxTeosFZTJ45LN6VEQOAdLCFB_iwlP3t9_i9qiQqQua1oJMGmp5wILrYvUWRBTMAVJphcDt7Qo0Yi5gK9pIHhW5pAb/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/appsec-ai-readiness-d)

# [OpenSSH Issues Emergency Fix for Flaw Letting Long Passwords Bypass SSH Auth on Alpine Linux](https://thehackernews.com/2026/11/openssh-issues-emergency-fix-for-flaw.html)

**Swati Khandelwal**Nov 05, 2026Linux / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEieaHvS5baW_XG1eAsBsoSp9qRzV179f0WwXoj9k6rUeX4Qa4sxpi3hvpGkgkYNMPzZQH0mvvVAoTooEAgl1G3SyFksmhqNEbDEIEWM83RH47u8qvNyIYclA7z7GUdPJGx8WfJd556iCvvtvsitAYp9M-T46OvuwkaSWwnyhlynEpYax2qyTCACsPbtQLw/s1700-nu-rw-lo-l85-e365/ssh-linux.jpg)

Attackers can log in to accounts that have no password, such as SSH key-only accounts, on some Alpine Linux servers running the standard openssh-server package. They need network access to the server, an account name, and a password between 257 and 1,024 bytes long.

OpenSSH, which rates the flaw critical, released version 10.6p2 today to block it. Alpine has published fixed packages for every release back to 3.16.

The attack works when the OpenSSH server (sshd) checks passwords without the Pluggable Authentication Module (PAM) interface, password logins are enabled, and at least one other account on the machine has a password. Alpine's openssh-server package is built without PAM, and password logins are on by default.

The flaw comes from how sshd works with musl, the C library that Alpine is built on. Non-Linux systems, Linux systems built on glibc, and systems that check passwords through PAM are not affected, said Damien Miller of the OpenSSH project.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

He told anyone running an affected system to "set PasswordAuthentication=no or disable SSH for these systems IMMEDIATELY." No attacks using the flaw have been reported.

### Who Is Exposed

Alpine's [security advisory](https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/) lists four conditions. A server is exposed when all four are true:

* It runs the `openssh-server` package, which is built without PAM, or runs `openssh-server-pam` with `UsePAM no`.
* `PasswordAuthentication` is `yes`, which is the OpenSSH default.
* An account has `*` as its password field, which means no password is set.
* At least one other local account has a password hash starting with `$5$` or `$6$`.

The attacker also needs the name of an account with no password. One account with a password is enough to expose every account without one. The attack succeeds on every try with a single connection, according to the advisory.

On Alpine, accounts with no password set include:

* key-only users created with `adduser` without a password, or with `usermod -p '*'`
* users who come from a directory service through musl-nscd, since they have no shadow entry
* `root`, which has shipped as `root:*` in the base image since about Alpine 3.16
* the `alpine` user in the official cloud images built with tiny-cloud

Root is protected by the default `PermitRootLogin prohibit-password` setting and can be reached directly only if `PermitRootLogin yes` is set. That protection does not help if an exposed account can become root, for example through `doas`.

The tiny-cloud images from 3.18.11 through 3.24.3 give the `alpine` user passwordless `doas`. They are safe at first boot but become open to attack once any `$6$` hash exists on the machine, for example after an admin sets a console password. An attacker can then log in as `alpine` and use `doas` to become root.

Containers that do not run sshd, systems with `PasswordAuthentication no`, and cloud images set up through cloud-init, which writes that setting, are not affected. Accounts locked with `!` in `/etc/shadow` are not affected either, and neither are machines where no account has a `$`-style password hash.

The flaw is not limited to Alpine. Özgün Kültekin of Wakefield, who reported it, names OpenWrt, Buildroot and Yocto in his [technical write-up](https://sshhole.com/) as other musl-based systems to check.

OpenWrt handles SSH with Dropbear by default, as its [Dropbear documentation](https://openwrt.org/docs/guide-user/base-system/dropbear) shows, and Kültekin says Dropbear is not affected. On OpenWrt, the flaw can matter only where an admin has installed the OpenSSH server.

### How to Fix It

On Alpine, the fix is a package update followed by a restart, because upgrading the package does not restart the running sshd:

1. Update the packages: `apk upgrade -U -a`
2. Restart the server: `rc-service sshd restart`

Point releases 3.21.10, 3.22.8, 3.23.8 and 3.24.4 already include the fixed package. Branches 3.16 to 3.21 are past their end of support but also got fixed packages.

Cloud instances started from tiny-cloud images older than those point releases still need the update, or the setting below.

If you build OpenSSH yourself, version 10.6p2 includes the change, as its [release notes](https://www.openssh.org/releasenotes.html#10.6p2) describe.

If you cannot update yet, turning off password logins also stops the attack. First make sure your SSH key login works, and keep your current session open until a new login succeeds. Then set `PasswordAuthentication no`, check the configuration with `sshd -t`, and restart sshd.

The advisory gives commands that add the setting in a drop-in file in `/etc/ssh/sshd_config.d`, which Alpine's default configuration reads from 3.19 onward. They also change every `PasswordAuthentication` line in `/etc/ssh/sshd_config` from `yes` to `no`, including lines inside a `Match` block. Afterward, `sshd -T | grep -i passwordauthentication` should print `passwordauthentication no`.

The advisory suggests looking in `/var/log/messages` for sshd lines reading `Accepted password for` an account that has no password, such as `alpine`, `root` or a key-only user. On exposed machines, also review `doas` use, recently created users, files and authorized keys.

"If you cannot rule out a login, treat the machine as compromised," it says.

### Why Long Passwor...