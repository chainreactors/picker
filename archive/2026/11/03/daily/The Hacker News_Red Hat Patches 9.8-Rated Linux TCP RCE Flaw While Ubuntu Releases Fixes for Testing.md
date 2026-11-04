---
title: Red Hat Patches 9.8-Rated Linux TCP RCE Flaw While Ubuntu Releases Fixes for Testing
url: https://thehackernews.com/2026/11/red-hat-patches-98-rated-linux-tcp-rce.html
source: The Hacker News
date: 2026-11-03
fetch_date: 2026-11-04T08:19:20.830799
---

# Red Hat Patches 9.8-Rated Linux TCP RCE Flaw While Ubuntu Releases Fixes for Testing

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

# [Red Hat Patches 9.8-Rated Linux TCP RCE Flaw While Ubuntu Releases Fixes for Testing](https://thehackernews.com/2026/11/red-hat-patches-98-rated-linux-tcp-rce.html)

**Swati Khandelwal**Nov 03, 2026Vulnerability / Linux

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjdf8UfDHsjH9VaJGtYT5WgjtJ1G5YRMkjPWNeKn-hw05sM9ny0kW9L2eIc3UCiIQ7qmc_TmfrenS1WH8KiRBjln2hQS0X7DUlykxdHrzDgg4uoiHpiOf3fVTOnUuOt4618z3PN7hw1AfUch_y0Tot3ubTga5LEfyWnATkzegfQBSWxMbzNzJaGY18QqC8/s1700-nu-rw-lo-l85-e365/linux-rce.jpg)

Fixed kernels for a use-after-free vulnerability in the Linux kernel's IPv4 TCP code are now available for Red Hat Enterprise Linux 8, 9, and 10, while Ubuntu's fixes for its three newest long-term-support releases remain in its opt-in testing channel with no date for a regular update.

The flaw, tracked as **[CVE-2026-98432](https://thehackernews.com/2026/10/linux-kernel-tcp-flaw-with-98-cvss.html)**, can be reached by a remote, unauthenticated attacker and can lead to remote code execution, [Red Hat](https://access.redhat.com/security/vulnerabilities/RHSB-2026-016) and [Canonical](https://ubuntu.com/blog/fixes-available-in-proposed-pocket-for-cve-2026-98432) said.

The Linux kernel's own CVE team rates the flaw 9.8 out of 10 on the CVSS scale. Red Hat, which initially rated it Moderate at 5.9, has raised its score to 9.8 and now calls it Critical. The bug has been present since Linux 4.4, and the upstream fix landed in October.

### What the Flaw Is

When a server accepts an IPv4 TCP connection, the kernel passes IP options from the incoming request to the new socket without copying them. If the client retransmits its connection request while another processor still reads those options, the kernel can read memory it has already freed.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

An attacker triggers the race by sending connection requests that carry IPv4 Record Route or Timestamp options to any listening TCP port. No login is needed. IPv6 is not affected on the main path.

Red Hat shipped [RHSA-2026:93414](https://access.redhat.com/errata/RHSA-2026%3A93414) (RHEL 8), [RHSA-2026:93412](https://access.redhat.com/errata/RHSA-2026%3A93412) (RHEL 9), and [RHSA-2026:93413](https://access.redhat.com/errata/RHSA-2026%3A93413) (RHEL 10) on November 1. A reboot is needed after installing the update.

| RHEL Version | Fixed Kernel | Errata |
| --- | --- | --- |
| 8.10 | `4.18.0-553.182.1.el8_10` | RHSA-2026:93414 |
| 9.8 | `5.14.0-687.64.1.el9_8` | RHSA-2026:93412 |
| 10.2 | `6.12.0-211.72.1.el10_2` | RHSA-2026:93413 |

Canonical [said on November 2](https://ubuntu.com/blog/fixes-available-in-proposed-pocket-for-cve-2026-98432) that fixes for Ubuntu 22.04 LTS, 24.04 LTS, and 26.04 LTS are in its *-proposed* pocket, an opt-in testing channel. Packages there do not install automatically.

Canonical tests kernel updates across more than 2,000 certified servers and devices before releasing them to the regular update channel, and no release date has been given.

| Ubuntu Release | -proposed Kernel | Status |
| --- | --- | --- |
| 22.04 LTS (Jammy) | `5.15.0-203.213` | In -proposed |
| 24.04 LTS (Noble) | `6.8.0-149.149` | In -proposed |
| 26.04 LTS (Resolute) | `7.0.0-43.43` | In -proposed |
| 20.04 / 18.04 / 16.04 | Pending |  |

Administrators who need the fix before it reaches the regular channel can enable -proposed and install the kernel update by running:

```
sudo add-apt-repository --component main --pocket proposed https://archive.ubuntu.com/ubuntu
dpkg-query -W -f '${source:Package}\t${binary:Package}\n' | awk '$1 ~ "^linux-meta" { print $2 }' | xargs sudo apt install -t $(. /etc/os-release && echo $VERSION_CODENAME)-proposed --only-upgrade
sudo reboot
```

To check whether a system is running a fixed kernel, compare the output of uname -r against the versions in the tables above.

Ubuntu 20.04, 18.04, and 16.04 have no fix yet. Older releases require Expanded Security Maintenance through Ubuntu Pro.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

Cloud, FIPS, and real-time kernel variants for Ubuntu are listed as work in progress on the [Ubuntu CVE page](https://ubuntu.com/security/CVE-2026-98432) with target versions, but Canonical's blog post covers only the generic kernel.

### Interim Mitigation

Red Hat published an [nftables rule](https://access.redhat.com/security/vulnerabilities/RHSB-2026-016) on October 30 that drops inbound IPv4 TCP packets carrying IP options. The rule blocks the known trigger for the race but cannot fully prevent exploitation and may break workloads that depend on IPv4 options, Red Hat said.

```
table inet cve_2026_98432 {
    chain input {
        type filter hook input priority -310; policy accept;
        ip protocol tcp ip hdrlength > 5 counter drop
    }
}
```

The filter applies only to the host where it is loaded. Traffic between containers on the same host can bypass it, a member of the CIQ kernel team noted on the oss-security mailing list.

Several sources have recommended disabling Multipath TCP (MPTCP) as a workaround. The flaw is in the IPv4 TCP path, not in MPTCP, and that advice alone is not enough, Canonical said. "The Ubuntu Security Team believes that security updates are the only appropriate mitigation."

### Exploitation Status

No vendor, CERT, or the kernel CVE team has reported attacks using this flaw. It was not listed in CISA's Known Exploited Vulnerabilities catalog as of the catalog's October 30 release.

[Anthropic said on October 27](https://thehackernews.com/2026/10/anthropics-unreleased-ai-model-chains.html) that an unreleased, internal Claude research model wrote a remote root exploit for the flaw that works against Linux servers with an MPTCP listener, with no credentials and no user interaction. In its proof of concept, leaking a kernel address took 48 minutes and reaching a root shell took another 5 minutes. A...