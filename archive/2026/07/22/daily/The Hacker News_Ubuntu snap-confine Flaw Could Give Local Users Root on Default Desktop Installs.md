---
title: Ubuntu snap-confine Flaw Could Give Local Users Root on Default Desktop Installs
url: https://thehackernews.com/2026/07/ubuntu-snap-confine-flaw-could-give.html
source: The Hacker News
date: 2026-07-22
fetch_date: 2026-07-23T05:11:47.353719
---

# Ubuntu snap-confine Flaw Could Give Local Users Root on Default Desktop Installs

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Ubuntu snap-confine Flaw Could Give Local Users Root on Default Desktop Installs](https://thehackernews.com/2026/07/ubuntu-snap-confine-flaw-could-give.html)

**Ravie Lakshmanan**Jul 22, 2026Linux / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidNwrZh7WuJhViXJ0c2i53cRV82jkdqS1FS9vHeNyOd19AITMQIA03JOnpqLyp7eHJoqa8L_V-eimCMZQNyba09AUvDHQ_n1NdAzmMFOg5FPp7gSymlqtjMcJ5UdyHRtK67wQ9hhusynzExbC9AWstVxaR9koev6e0PhySMPElKOFVwmge25lODZfyQkVD/s1700-e365/ubuntu.jpg)

Cybersecurity researchers have disclosed details of a new local privilege escalation (LPE) vulnerability in snap-confine that an unprivileged user can trigger to obtain root access and gain complete control of a target environment.

The high-severity flaw, tracked as **[CVE-2026-8933](https://blog.qualys.com/vulnerabilities-threat-research/2026/07/21/cve-2026-8933-snap-confine-local-privilege-escalation)** (CVSS score: 7.8), impacts default installations of Ubuntu Desktop 24.04, 25.10, and 26.04. The disclosure comes as 442 security flaws in Linux have been [publicized](https://lore.kernel.org/linux-cve-announce/) over the past three days.

"The issue stems from a security hardening change that inadvertently introduced a race condition during sandbox initialization," Saeed Abbasi, head of Threat Research Unit (TRU) and director of product at Qualys, said.

Snap-confine is a program used internally by snapd to construct the execution environment for snap applications. Snapd is the background service or daemon that manages snap packages on Linux systems. Snaps are nothing but a software packaging format devised by Canonical that allows an application to run securely in an isolated sandbox across most Linux distributions.

"Snapd runs a sub-process called snap-confine, which is responsible for creating the necessary confinement for the snap," according to [Canonical](https://snapcraft.io/docs/explanation/security/classic-confinement/).

Although recent Ubuntu releases make use of the set-capabilities model to enforce the principle of least privilege (PoLP) as a way to minimize the attack surface, the changes allow snap-confine to be executed with the effective UID of the calling user, at the same time still retaining near-root capabilities.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

"During sandbox setup, the binary creates temporary directories and files under /tmp that are initially owned by the unprivileged user," Qualys explained. "Ownership is transferred to the root shortly after, but a narrow window remains during which the caller retains full control."

The problem identified by the cybersecurity vendor is the result of two concurrent race conditions -

* An attacker mounts a malicious [FUSE file system](https://www.kernel.org/doc/html/next/filesystems/fuse.html) over the temporary scratch directory immediately after creation, bypassing the mount namespace isolation applied by snap-confine and keeping the directory accessible outside the sandbox.
* The attacker creates a symbolic link (aka symlink) pointing to an arbitrary target file, effectively redirecting file operations to sensitive system locations.

By manipulating file permissions before the system transfers ownership, the attacker can inject malicious rules into system directories and gain root code execution, Qualys noted.

"When snap-confine attempts to create a sandbox file, the open() call follows the symlink and writes to the target," Abbasi said. "A second race condition allows the attacker to widen file permissions to 0666 before snap-confine calls fchown() to transfer ownership to root."

"To bypass AppArmor confinement, the exploit targets the /run/udev/\*\* path, which permits read-write access. By dropping a malicious .rules file in /run/udev/rules.d/ and triggering a FUSE mount/unmount cycle, the attacker forces systemd-udevd to execute arbitrary commands as root."

To counter the risk posed by CVE-2026-8933, organizations must apply the latest snapd updates as soon as possible.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnP2BIJTKZ31v-Y_pyvFqC1s6LD-Bo8UNy3UHgqojpVezgaGWw5-sPe5uRK0dfSm3gmDvoKCdHoJnGx1BiTP6Y0qit7D7TCZU_LckTDpdu9eeyuelmJKndEkOxZP6oNPwzguLBCTkAnNkIEvSYaWamKLqYLrJPjnea1V_lz7UcfQkavBo2g3OEGoLyz7mD/s728-e100/sygnia-d-4.png)](https://thn.news/sygnia-webinar)

"An attacker still needs user-level access or code execution, but CVE-2026-8933 can turn that foothold into full control of the host," Jason Soroko, Senior Fellow at Sectigo, said in a statement. "Its presence on default Ubuntu Desktop installations makes employee workstations, developer systems, and administrative endpoints part of the response scope."

"Ubuntu 24.04 is notable because updated systems can carry the affected snap-confine variant, showing why administrators must verify the installed snapd version instead of relying on release age or prior patch status. With fixes available, rapid deployment and confirmation should take priority."

This is not the first time security flaws have been uncovered in the snap-confine component. In February 2022, Qualys detailed another local privilege escalation flaw dubbed Oh Snap! More Lemmings ([CVE-2021-44731](https://thehackernews.com/2022/02/new-linux-privilege-escalation-flaw.html)) that could be abused to gain root privileges by exploiting a race condition in snap-confine's setup\_private\_mount().

Since then, several other vulnerabilities have come to light, including [CVE-2022-3328](https://thehackernews.com/2022/12/critical-ping-vulnerability-allows.html) (CVSS score: 7.8) and [CVE-2026-3888](https://ubuntu.com/security/CVE-2026-3888) (CVSS score: 7.8).

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/comp...