---
title: New Linux Flaws Enable Full Root Access via PAM and Udisks Across Major Distributions
url: https://thehackernews.com/2025/06/new-linux-flaws-enable-full-root-access.html
source: The Hacker News
date: 2025-06-20
fetch_date: 2025-10-06T22:59:25.200525
---

# New Linux Flaws Enable Full Root Access via PAM and Udisks Across Major Distributions

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

# [New Linux Flaws Enable Full Root Access via PAM and Udisks Across Major Distributions](https://thehackernews.com/2025/06/new-linux-flaws-enable-full-root-access.html)

**Jun 19, 2025**Ravie LakshmananLinux / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXov8Cx_igQW4qij-AsFmuK3PvE_68RZF_35cguvWlQV8pWKAVOOf1DIWk6ZpL8eriWkF1Pdwlkx7GmolL2yQeknbGs1F7QwEdF6Bu3dvIl6t7CatxuL7USxwGjM166GTEcOq-XK3g_bteqdnY27DijtddyJhVZ3M8PVBoXN5cqb7_h9UVwKBs0h1O3omK/s790-rw-e365/Linux-LPE.jpg)

Cybersecurity researchers have uncovered two local privilege escalation (LPE) flaws that could be exploited to gain root privileges on machines running major Linux distributions.

The [vulnerabilities](https://www.openwall.com/lists/oss-security/2025/06/17/4), discovered by Qualys, are listed below -

* **CVE-2025-6018** - LPE from unprivileged to allow\_active in SUSE 15's Pluggable Authentication Modules ([PAM](https://www.redhat.com/en/blog/pluggable-authentication-modules-pam))
* **CVE-2025-6019** - LPE from allow\_active to root in [libblockdev](https://github.com/storaged-project/libblockdev) via the [udisks](https://wiki.archlinux.org/title/Udisks) daemon

"These modern 'local-to-root' exploits have collapsed the gap between an ordinary logged-in user and a full system takeover," Saeed Abbasi, Senior Manager at Qualys Threat Research Unit (TRU), [said](https://blog.qualys.com/vulnerabilities-threat-research/2025/06/17/qualys-tru-uncovers-chained-lpe-suse-15-pam-to-full-root-via-libblockdev-udisks).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"By chaining legitimate services such as udisks loop-mounts and PAM/environment quirks, attackers who own any active GUI or SSH session can vault across polkit's allow\_active trust zone and emerge as root in seconds."

The cybersecurity company said CVE-2025-6018 is present in the PAM configuration of openSUSE Leap 15 and SUSE Linux Enterprise 15, enabling an unprivileged local attacker to elevate to the "allow\_active" user and call [Polkit](https://thehackernews.com/2022/01/12-year-old-polkit-flaw-lets.html) actions that are otherwise reserved for a physically present user.

CVE-2025-6019, on the other hand, affects libblockdev and is exploitable via the [udisks daemon](https://linux.die.net/man/8/udisks-daemon) included by default on most Linux distributions. It essentially permits an "allow\_active" user to gain full root privileges by chaining it with CVE-2025-6018.

"Although it nominally requires 'allow\_active' privileges, udisks ships by default on almost all Linux distributions, so nearly any system is vulnerable," Abbasi added. "Techniques to [gain 'allow\_active,'](https://u1f383.github.io/linux/2025/05/25/dbus-and-polkit-introduction.html) including the PAM issue disclosed here, further negate that barrier."

Once root privileges are obtained, an attacker has carte blanche access to the system, allowing them use it as a springboard for broader post-compromise actions, such as altering security controls and implanting backdoors for covert access.

Qualys said it has developed proof-of-concept (PoC) exploits to confirm the presence of these vulnerabilities on various operating systems, including Ubuntu, Debian, Fedora, and openSUSE Leap 15.

To mitigate the risk posed by these flaws, it's essential to apply patches provided by the Linux distribution vendors. As temporary workarounds, users can modify the Polkit rule for "org.freedesktop.udisks2.modify-device" to require administrator authentication ("auth\_admin").

## Flaw Disclosed in Linux PAM

The disclosure comes as maintainers of Linux PAM resolved a high-severity path traversal flaw (**CVE-2025-6020**, CVSS score: 7.8) that could also allow a local user to escalate to root privileges. The issue has been fixed in version 1.7.1.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The module [pam\_namespace](https://man7.org/linux/man-pages/man8/pam_namespace.8.html) in linux-pam <= 1.7.0 may access user-controlled paths without proper protections, which allows a local user to elevate their privileges to root via multiple symlink attacks and race conditions," Linux PAM maintainer Dmitry V. Levin [said](https://github.com/linux-pam/linux-pam/security/advisories/GHSA-f9p8-gjr4-j9gx).

Linux systems are vulnerable if they use pam\_namespace to set up [polyinstantiated directories](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/6/html/security-enhanced_linux/polyinstantiated-directories) for which the path to either the polyinstantiated directory or instance directory is under user-control. As workarounds for CVE-2025-6020, users can disable pam\_namespace or ensure it does not operate on user-controlled paths.

ANSSI's Olivier Bal-Petre, who reported the flaw to the maintainers on January 29, 2025, [said](https://seclists.org/oss-sec/2025/q2/258) users should also update their namespace.init script if they do not use the one provided by their distribution to ensure that the either of two paths are safe to operate on as root.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[cybersecuri...