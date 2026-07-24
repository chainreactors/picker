---
title: Nine-Year-Old RefluXFS Linux Flaw Gives Local Users Root on Default RHEL Installs
url: https://thehackernews.com/2026/07/nine-year-old-refluxfs-linux-flaw-gives.html
source: The Hacker News
date: 2026-07-23
fetch_date: 2026-07-24T05:05:42.260665
---

# Nine-Year-Old RefluXFS Linux Flaw Gives Local Users Root on Default RHEL Installs

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

# [Nine-Year-Old RefluXFS Linux Flaw Gives Local Users Root on Default RHEL Installs](https://thehackernews.com/2026/07/nine-year-old-refluxfs-linux-flaw-gives.html)

**Swati Khandelwal**Jul 23, 2026Linux / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_70wKHw_bPdJz-ZYXpwrH7FBXem8uWKNtuBUyXDLbMld4PaBtBkw7Gpt9lRrVnki_eC21aw6sUezqM3-oFiTEviDqZECD20lmV3enwh0lDkRLAx38JlJYMoLzRpn-Ai4q1UbiIo8DTVjp4_blU5CM6AnW97jYgIblggBYgNIHdTE6t2Ec7by-N0Ly8YY/s1700-e365/linux-root.jpg)

[RefluXFS](https://blog.qualys.com/vulnerabilities-threat-research/2026/07/22/refluxfs-a-linux-kernel-local-privilege-escalation-to-root-in-xfs-cve-2026-64600), a Linux kernel flaw disclosed on July 22 and tracked as `CVE-2026-64600`, lets an unprivileged local user overwrite root-owned files on an XFS filesystem and gain persistent root access.

Qualys said default installations of Red Hat Enterprise Linux and its derivatives, Fedora Server, and Amazon Linux can meet the conditions for exploitation.

The company demonstrated the race against `/etc/passwd` and setuid-root binaries. The overwrite lands at the block layer. It survives a reboot and leaves the target's ownership, permissions, timestamps, and setuid bit untouched, so a modified setuid-root binary still runs as root.

The fix was merged on July 16, and Linux vendors have begun shipping backported kernels. The patch traces the bug to Linux 4.11 in 2017: a `Fixes:` tag naming commit `3c68d44a2b49` and a stable backport request marked `# v4.11`.

## Who is exposed

Exploitation requires three conditions:

* The system runs Linux 4.11 or later without the RefluXFS fix.
* The XFS filesystem was created with `reflink=1`.
* The readable target and an attacker-writable directory are on the same XFS filesystem.

Qualys said to patch exposed and multi-tenant systems first, which means any reflink-enabled XFS host where untrusted code can run locally, whether through a shell, a CI job, or a compromised service.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The advisory lists the default installations that can meet those conditions: Red Hat Enterprise Linux 8, 9, and 10 and their downstream derivatives, Fedora Server 31 and later, Amazon Linux 2023, and Amazon Linux 2 images from December 2022 onward. RHEL 7 filesystems are not affected because they predate XFS reflink support.

Debian, Ubuntu, SLES, and openSUSE do not generally use XFS for the root filesystem by default. They are exposed only if an administrator chose XFS with reflink enabled at install time.

Check the root filesystem:

`xfs_info / | grep reflink=`

`reflink=1` means condition two is met. Run the same check on any other mounted XFS volume where a protected file and an attacker-writable directory share the filesystem.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSOtzb-RU1l4DJuFC1KaC_ZVpUoDdlhm6S9AHnp_hFCP5DgVr_o6_w8HR2cFq7FltgnCg_IeSvmsNiEOweZk96f4LLj4NmHCOoeSLLV2yERh-3aIZFTSNLWhpUf2_IhcgVlBJi8_i0KibBgVLuqa_13moq0240oiz659NEtpa8nzKCuUatGIPButHh028/s1700-e365/redhat.jpg)

## The Stale Mapping

An attacker clones a root-owned file into a scratch file with `FICLONE`, which needs only read access on the source, then races concurrent `O_DIRECT` writes against the clone. XFS reflinks use copy-on-write, so both files initially reference the same physical disk blocks.

The kernel reads the data-fork mapping under the inode lock and hands it to `xfs_reflink_fill_cow_hole()`, which cycles that lock to reserve transaction space.

A second writer can complete the copy-on-write operation during that gap and remap the cloned file to a new block. When the first writer reacquires the lock, it refreshes the copy-on-write fork but continues using the old data-fork mapping.

The [upstream patch](https://github.com/torvalds/linux/commit/2f4acd0fcd862e22eab45690ec2c08c80b6ef2e7) describes the failure plainly: "the mappings are stale as soon as we reacquire the ILOCK."

That stale address now points to a block owned only by the original protected file. XFS sees the block as unshared and permits the direct write, so data intended for the attacker's clone lands in the target instead.

It is a check-then-use error across a lock cycle. The shared-status query itself is correct; what it queries is a block address captured before the lock was released.

The Hacker News found the patch touches two helpers, `xfs_reflink_fill_cow_hole()` and `xfs_reflink_fill_delalloc()`. The second carries the same lock-cycle pattern and does not appear in the Qualys advisory.

Saeed Abbasi, who heads the Qualys Threat Research Unit, told The Hacker News the model found both paths at the same time, because they are so similar. In both, the fix snapshots `ip->i_df.if_seq` before the lock is dropped and re-reads the data fork with `xfs_bmapi_read()` if the counter moved.

Direct I/O skips the page cache and has no revalidation hook, so the write lands on disk. Because it bypasses the target inode entirely, the metadata never changes, and the researchers said their tests produced no kernel warning or log entry.

On the test machine, the race usually won in under ten seconds. The published demo strips the root password on a default RHEL 10.2 box.

Qualys said an AI model found the flaw. The company pointed [Claude Mythos Preview](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html), Anthropic's restricted-access frontier model, at the kernel and, per its [technical advisory](https://cdn2.qualys.com/advisory/2026/07/22/RefluXFS.txt), "asked it to find a vulnerability similar to [Dirty COW](https://thehackernews.com/2016/10/linux-kernel-exploit.html)."

The model located the race, wrote a working root exploit, and drafted the advisory. Researchers then reproduced it on a stock Fedora Server 44 install, checked the model's reasoning, and coordinated disclosure upstream.

Abbasi said the team changed...