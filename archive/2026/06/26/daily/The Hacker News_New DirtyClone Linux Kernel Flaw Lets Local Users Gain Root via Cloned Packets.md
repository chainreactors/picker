---
title: New DirtyClone Linux Kernel Flaw Lets Local Users Gain Root via Cloned Packets
url: https://thehackernews.com/2026/06/new-dirtyclone-linux-kernel-flaw-lets.html
source: The Hacker News
date: 2026-06-26
fetch_date: 2026-06-27T05:52:31.056809
---

# New DirtyClone Linux Kernel Flaw Lets Local Users Gain Root via Cloned Packets

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [New DirtyClone Linux Kernel Flaw Lets Local Users Gain Root via Cloned Packets](https://thehackernews.com/2026/06/new-dirtyclone-linux-kernel-flaw-lets.html)

**Swati Khandelwal**Jun 26, 2026Linux / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidrcFiZh5KSQ9sYpF7Fafoy8kYny6olyD5WlY_oaAdYt0krMeOL8eNiTItqYmEmJ55wueKdZJlhIKMun7kwQR8AbbFPKTw0Nv-qJbPiaKA1n2J1rUHBV3YuRmdJHQpOTlsKctFMXoO8ogpgHC8rXls3FGamF7p7K1gxc-7dmU2va58Es1c40FV8AZFR-w/s1700-e365/dirtyclone.jpg)

**DirtyClone** is a new Linux kernel privilege escalation in the **DirtyFrag** family. JFrog Security Research published a working exploit walkthrough for the flaw on June 25, the first public demonstration for this variant.

Tracked as [CVE-2026-43503](https://ubuntu.com/security/CVE-2026-43503) (CVSS 8.8), it lets a local user corrupt file-backed memory through a cloned network packet and gain root. The patch landed in mainline on May 21; if your kernel does not have it, update now.

When the kernel copies a network packet internally, two helper functions drop a safety flag that marks the packet's memory as shared with a file on disk. That missing flag is the entire vulnerability.

The attacker loads a privileged binary like /usr/bin/su into memory, wires those memory pages into a network packet, and forces the kernel to clone it. The cloned packet passes through an IPsec tunnel that the attacker controls, and the decryption step overwrites the binary's login checks with attacker-chosen bytes. The next time anyone runs su, it hands over root.

The file on disk never changes. The modification lives only in the kernel's in-memory copy, so file-integrity tools miss it, the attack leaves no audit trail, and a reboot restores the original binary. The attacker already has root by the time anyone might think to check.

Exploitation requires **CAP\_NET\_ADMIN**to configure the loopback IPsec tunnel. On Debian and Fedora, unprivileged user namespaces are enabled by default, so a local user can obtain that capability inside a new namespace.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

Ubuntu 24.04 and later restrict namespace creation via AppArmor, blocking the default exploit path. Page cache is shared at the host level, so modifications made inside a namespace affect every process on the machine.

The exposed systems are multi-tenant servers, CI runners, container hosts, and Kubernetes clusters where untrusted users can create namespaces. JFrog [confirmed the exploit](https://research.jfrog.com/post/dissecting-and-exploiting-linux-lpe-variant-dirtyclone-cve-2026-43503/) on Debian, Ubuntu, and Fedora systems with default namespace configurations.

## Fourth in a Series

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIuQInZh-F35gDp-vAdiEuyjisOqLw-DDtUSMpX0ZfSJSbmaM1OS7mjfWGlRxt5VbWjJpm4F1PLStyCQl3uqKEAGsjHMQ81pVHy42md3zA8zYAl1t4bdymQHPjkz-Mkc17rb39H8lcYnnkd2NjCg0tU4KPdRL6iYDqnX-o0uF3cIr_pYRjTAeYcG1UjEo/s1700-e365/dirty.png)

This is the fourth recent privilege escalation with the same failure mode: file-backed memory gets treated as packet data, then an in-place network operation writes where it should have copied.

* [Copy Fail](https://thehackernews.com/2026/04/new-linux-copy-fail-vulnerability.html) (CVE-2026-31431) came first in late April, exploiting the algif\_aead module for a four-byte page-cache write.
* [DirtyFrag](https://thehackernews.com/2026/05/linux-kernel-dirty-frag-lpe-exploit.html) (CVE-2026-43284 and CVE-2026-43500) followed on May 7, chaining IPsec ESP and RxRPC paths for a full write primitive.
* [Fragnesia](https://thehackernews.com/2026/05/new-fragnesia-linux-kernel-lpe-grants.html) (CVE-2026-46300) appeared on May 13, bypassing the DirtyFrag patch through a flag-dropping bug in skb\_try\_coalesce().

Each fix closed one code path and left others open. DirtyClone's demonstrated exploit centers on \_\_pskb\_copy\_fclone(), with skb\_shift() also affected; the broader CVE fix covers additional frag-transfer helpers where the same flag could be lost.

The underlying problem is not one bad helper function. It is a contract problem: every code path that moves skb fragments has to preserve the shared-frag bit, every time.

The kernel's zero-copy networking lets file-backed memory serve as packet data, and a single dropped flag anywhere in the chain turns a performance optimization into a write primitive. Each variant found a path where the contract was not honored.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

The original DirtyFrag researcher, Hyunwoo Kim, had submitted a broader [multi-site patch](https://lore.kernel.org/netdev/ageeJfJHwgzmKXbh%40v4bel/) covering several remaining frag-transfer helpers on May 16. The combined fix was merged on May 21 (commit 48f6a5356a33), assigned CVE-2026-43503 on May 23, and shipped in Linux v7.1-rc5 on May 24.

## What to Do

Install your distribution's kernel update. The fix landed upstream in v7.1-rc5 and has been backported to stable and LTS branches. [Ubuntu](https://ubuntu.com/security/notices/USN-8373-1), [Debian](https://security-tracker.debian.org/tracker/CVE-2026-43503), and [SUSE](https://www.suse.com/security/cve/CVE-2026-43503.html) have published advisories; [Red Hat has a Bugzilla tracking entry](https://bugzilla.redhat.com/show_bug.cgi?id=2480902).

If you cannot patch today, two workarounds reduce the attack surface. Restrict unprivileged user namespaces: on Debian and Ubuntu, set kernel.unprivileged\_userns\_clone=0 (other distributions use different mechanisms).

Alternatively, blacklist the esp4, esp6, and rxrpc kernel modules, though that breaks IPsec and AFS and only works when those features are loadable modules rather than compiled into the kernel. Both are temporary controls, not fixes.

The DirtyFrag class is probably not done. Any function that moves fragment descriptors without pr...