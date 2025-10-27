---
title: New Linux Flaws Allow Password Hash Theft via Core Dumps in Ubuntu, RHEL, Fedora
url: https://thehackernews.com/2025/05/new-linux-flaws-allow-password-hash.html
source: The Hacker News
date: 2025-06-01
fetch_date: 2025-10-06T22:53:37.764938
---

# New Linux Flaws Allow Password Hash Theft via Core Dumps in Ubuntu, RHEL, Fedora

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

# [New Linux Flaws Allow Password Hash Theft via Core Dumps in Ubuntu, RHEL, Fedora](https://thehackernews.com/2025/05/new-linux-flaws-allow-password-hash.html)

**May 31, 2025**Ravie LakshmananVulnerability / Linux

[![Linux Flaws](data:image/png;base64... "Linux Flaws")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEivbL-iametIvu-Hc9mExtP_3I3U5aJAGCbher8RkZIyosedvj2_NGiw7uCj-Fuw2dpP9sBPUOilhooYKLKOoRfq-itHvR7BwCvauCtITnD8gujc3Ft3KMc5Vd4NxtUGXjRpP12NvK_9Ul7oW-0i_Ti43cX7Yis_C2R8ZCJ9p7vv24oqZP8KGLmeuMZ3WAK/s790-rw-e365/linux.jpg)

Two information disclosure flaws have been identified in [apport](https://wiki.ubuntu.com/Apport) and [systemd-coredump](https://www.freedesktop.org/software/systemd/man/latest/systemd-coredump.html), the [core dump](https://en.wikipedia.org/wiki/Core_dump) handlers in Ubuntu, Red Hat Enterprise Linux, and Fedora, according to the Qualys Threat Research Unit (TRU).

Tracked as [CVE-2025-5054 and CVE-2025-4598](https://www.openwall.com/lists/oss-security/2025/05/29/3), both vulnerabilities are race condition bugs that could enable a local attacker to obtain access to access sensitive information. Tools like Apport and systemd-coredump are designed to handle crash reporting and core dumps in Linux systems.

"These race conditions allow a local attacker to exploit a SUID program and gain read access to the resulting core dump," Saeed Abbasi, manager of product at Qualys TRU, [said](https://blog.qualys.com/vulnerabilities-threat-research/2025/05/29/qualys-tru-discovers-two-local-information-disclosure-vulnerabilities-in-apport-and-systemd-coredump-cve-2025-5054-and-cve-2025-4598).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

A brief description of the two flaws is below -

* **[CVE-2025-5054](https://nvd.nist.gov/vuln/detail/CVE-2025-5054)** (CVSS score: 4.7) - A race condition in Canonical apport package up to and including 2.32.0 that allows a local attacker to leak sensitive information via PID-reuse by leveraging namespaces
* **[CVE-2025-4598](https://nvd.nist.gov/vuln/detail/CVE-2025-4598)** (CVSS score: 4.7) - A race condition in systemd-coredump that allows an attacker to force a SUID process to crash and replace it with a non-SUID binary to access the original's privileged process coredump, allowing the attacker to read sensitive data, such as /etc/shadow content, loaded by the original process

SUID, short for Set User ID, is a [special](https://en.wikipedia.org/wiki/Setuid) [file permission](https://www.redhat.com/en/blog/suid-sgid-sticky-bit) that allows a user to execute a program with the privileges of its owner, rather than their own permissions.

"When analyzing application crashes, apport attempts to detect if the crashing process was running inside a container before performing consistency checks on it," Canonical's Octavio Galland [said](https://ubuntu.com/blog/apport-local-information-disclosure-vulnerability-fixes-available).

"This means that if a local attacker manages to induce a crash in a privileged process and quickly replaces it with another one with the same process ID that resides inside a mount and pid namespace, apport will attempt to forward the core dump (which might contain sensitive information belonging to the original, privileged process) into the namespace."

Red Hat said CVE-2025-4598 has been rated Moderate in severity owing to the high complexity in pulling an exploit for the vulnerability, noting that the attacker has to first win the race condition and be in possession of an unprivileged local account.

As mitigations, Red Hat said users can run the command "echo 0 > /proc/sys/fs/suid\_dumpable" as a root user to disable the ability of a system to generate a core dump for SUID binaries.

The "/proc/sys/fs/suid\_dumpable" parameter essentially controls whether SUID programs can produce core dumps following a crash. By setting it to zero, it disables core dumps for all SUID programs and prevents them from being analyzed in the event of a crash.

"While this mitigates this vulnerability while it's not possible to update the systemd package, it disables the capability of analyzing crashes for such binaries," Red Hat [said](https://access.redhat.com/security/cve/CVE-2025-4598).

Similar advisories have been issued by [Amazon Linux](https://explore.alas.aws.amazon.com/CVE-2025-4598.html), [Debian](https://security-tracker.debian.org/tracker/CVE-2025-4598), and [Gentoo](https://bugs.gentoo.org/show_bug.cgi?id=CVE-2025-4598). It's worth noting that Debian systems aren't susceptible to CVE-2025-4598 by default, since they don't include any core dump handler unless the systemd-coredump package is manually installed. CVE-2025-4598 does not affect Ubuntu releases.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Qualys has also developed proof-of-concept (PoC) code for both vulnerabilities, demonstrating how a local attacker can exploit the coredump of a crashed unix\_chkpwd process, which is used to verify the validity of a user's password, to obtain password hashes from the /etc/shadow file.

Canonical, in an alert of its own, said the impact of CVE-2025-5054 is restricted to the confidentiality of the memory space of invoked SUID executables and that the PoC exploit can leak hashed user passwords has limited real-world impact.

"The exploitation of vulnerabilities in Apport and systemd-coredump can severely compromise the confidentiality at high risk, as attackers could extract sensitive data, like passwords, encryption keys, or customer information from core dumps," Abbasi said.

"The fallout includes operational downtime, reputational damage, and potential non-compliance with regulations. To mitigate these multifaceted risks effectively, enterprises should adopt proactive security measures by prioritizing patches and mitigations, enforcing robust monitoring, and tightening access controls."

Found this article interesting? Follow us on [Google News](https://news....