---
title: Critical Sudo Vulnerabilities Let Local Users Gain Root Access on Linux, Impacting Major Distros
url: https://thehackernews.com/2025/07/critical-sudo-vulnerabilities-let-local.html
source: The Hacker News
date: 2025-07-05
fetch_date: 2025-10-06T23:28:31.924637
---

# Critical Sudo Vulnerabilities Let Local Users Gain Root Access on Linux, Impacting Major Distros

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Critical Sudo Vulnerabilities Let Local Users Gain Root Access on Linux, Impacting Major Distros](https://thehackernews.com/2025/07/critical-sudo-vulnerabilities-let-local.html)

**Jul 04, 2025**Ravie LakshmananVulnerability / Linux

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh97thht71NecxTeOepPLuzmf5uuYK2L47qCImdfzGW3PGMYB6mXrcEVDPkfUJj2HLLehHhYSuzsGXJU23RbFdNqUqgjX5xWXfV1Eiuw_t0OQ0enc6JXhDzr-jExEmGOznBJ76ooGwfK96MOZBNY25jZUm5FifjuOCqNigdZWeHVGXQIW0_ROLSblW29GJi/s790-rw-e365/linux.jpg)

Cybersecurity researchers have disclosed two security flaws in the Sudo command-line utility for Linux and Unix-like operating systems that could enable local attackers to escalate their privileges to root on susceptible machines.

A brief description of the vulnerabilities is below -

* **[CVE-2025-32462](https://nvd.nist.gov/vuln/detail/CVE-2025-32462)** (CVSS score: 2.8) - Sudo before 1.9.17p1, when used with a sudoers file that specifies a host that is neither the current host nor ALL, allows listed users to execute commands on unintended machines
* **[CVE-2025-32463](https://nvd.nist.gov/vuln/detail/CVE-2025-32463)** (CVSS score: 9.3) - Sudo before 1.9.17p1 allows local users to obtain root access because "[/etc/nsswitch.conf](https://man7.org/linux/man-pages/man5/nsswitch.conf.5.html)" from a user-controlled directory is used with the --chroot option

Sudo is a [command-line tool](https://www.sudo.ws/docs/man/sudo.man/) that allows low-privileged users to run commands as another user, such as the superuser. By executing instructions with sudo, the idea is to enforce the principle of least privilege, permitting users to carry out administrative actions without the need for elevated permissions.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The command is [configured](https://www.digitalocean.com/community/tutorials/how-to-edit-the-sudoers-file) through a file called "/etc/sudoers," which [determines](https://help.ubuntu.com/community/Sudoers) "who can run what commands as what users on what machines and can also control special things such as whether you need a password for particular commands."

Stratascale researcher Rich Mirch, who is credited with discovering and reporting the flaws, [said](https://www.stratascale.com/vulnerability-alert-CVE-2025-32462-sudo-host) CVE-2025-32462 has managed to slip through the cracks for over 12 years. It is rooted in the Sudo's "-h" (host) option that makes it possible to list a user's sudo privileges for a different host. The feature was enabled in September 2013.

However, the identified bug made it possible to execute any command allowed by the remote host to be run on the local machine as well when running the Sudo command with the host option referencing an unrelated remote host.

"This primarily affects sites that use a common sudoers file that is distributed to multiple machines," Sudo project maintainer Todd C. Miller [said](https://www.sudo.ws/security/advisories/host_any/) in an advisory. "Sites that use LDAP-based sudoers (including SSSD) are similarly impacted."

CVE-2025-32463, on the other hand, leverages Sudo's "-R" (chroot) option to run arbitrary commands as root, even if they are not listed in the sudoers file. It's also a critical-severity flaw.

"The default Sudo configuration is vulnerable," Mirch [said](https://www.stratascale.com/vulnerability-alert-CVE-2025-32463-sudo-chroot). "Although the vulnerability involves the Sudo chroot feature, it does not require any Sudo rules to be defined for the user. As a result, any local unprivileged user could potentially escalate privileges to root if a vulnerable version is installed."

In other words, the flaw permits an attacker to trick sudo into loading an arbitrary shared library by creating an "/etc/nsswitch.conf" configuration file under the user-specified root directory and potentially run malicious commands with elevated privileges.

Miller [said](https://www.sudo.ws/security/advisories/chroot_bug/) the chroot option will be removed completely from a future release of Sudo and that supporting a user-specified root directory is "error-prone."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Following responsible disclosure on April 1, 2025, the vulnerabilities have been addressed in Sudo version 1.9.17p1 released late last month. Advisories have also been issued by various Linux distributions, since Sudo comes installed on many of them -

* **CVE-2025-32462** - [AlmaLinux 8](https://errata.almalinux.org/8/ALSA-2025-10110.html), [AlmaLinux 9](https://errata.almalinux.org/9/ALSA-2025-9978.html), [Alpine Linux](https://security.alpinelinux.org/vuln/CVE-2025-32462), [Amazon Linux](https://explore.alas.aws.amazon.com/CVE-2025-32462.html), [Debian](https://security-tracker.debian.org/tracker/CVE-2025-32462), [Gentoo](https://security.gentoo.org/glsa/202507-01), [Oracle Linux](https://linux.oracle.com/errata/ELSA-2025-10110.html), [Red Hat](https://access.redhat.com/security/cve/cve-2025-32462), [SUSE](https://www.suse.com/security/cve/CVE-2025-32462.html), and [Ubuntu](https://ubuntu.com/security/CVE-2025-32462)
* **CVE-2025-32463** - [Alpine Linux](https://security.alpinelinux.org/vuln/CVE-2025-32463), [Amazon Linux](https://explore.alas.aws.amazon.com/CVE-2025-32463.html), [Debian](https://security-tracker.debian.org/tracker/CVE-2025-32463), [Gentoo](https://security.gentoo.org/glsa/202507-01), [Red Hat](https://access.redhat.com/security/cve/cve-2025-32463), [SUSE](https://www.suse.com/security/cve/CVE-2025-32463.html), and [Ubuntu](https://ubuntu.com/security/CVE-2025-32463)

Users are advised to apply the necessary fixes and ensure that the Linux desktop distributions are updated with the latest packages.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twit...