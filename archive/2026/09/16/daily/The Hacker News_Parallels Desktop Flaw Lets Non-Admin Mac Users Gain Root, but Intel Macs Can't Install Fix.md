---
title: Parallels Desktop Flaw Lets Non-Admin Mac Users Gain Root, but Intel Macs Can't Install Fix
url: https://thehackernews.com/2026/09/parallels-desktop-flaw-lets-non-admin.html
source: The Hacker News
date: 2026-09-16
fetch_date: 2026-09-17T06:59:41.031776
---

# Parallels Desktop Flaw Lets Non-Admin Mac Users Gain Root, but Intel Macs Can't Install Fix

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Parallels Desktop Flaw Lets Non-Admin Mac Users Gain Root, but Intel Macs Can't Install Fix](https://thehackernews.com/2026/09/parallels-desktop-flaw-lets-non-admin.html)

**Swati Khandelwal**Sep 16, 2026Vulnerability / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjExQfYsCTPbCiUrkVUWdKhrZNgpAVRtutRYt2c4x-f5ClJdNYjERcet4Fctan3gEOl0DPk64GUGZv5IK3Cd_pi3Jk1cyH3tdYig9mpc2XTLjJaK0KM3aiqE6W1OeGiKr_kRWNRmty1u4Cwf_9-S1KrKdqUeL25YwL6tt5Z-nUcvzj0F8NemzMbSUmvTJ4/s1700-nu-rw-lo-l85-e365/parashells.jpg)

Parallels Desktop for Mac has a flaw that lets an ordinary local account run code as root, the highest level of access on a Mac, software company JFrog said this week.

The attack needs code already running on the machine as a normal user, so it does not work over the network. JFrog says the fix is in Parallels Desktop 27, a version that Intel Macs cannot install.

Yuval Moravchick, who leads JFrog's vulnerability research team, [published the finding](https://jfrog.com/blog/parallels-desktop-turns-appliance-install-into-root-shell/) on Tuesday and calls it ParaShells. The flaw is tracked as [CVE-2026-90894](https://www.cve.org/CVERecord?id=CVE-2026-90894), an identifier JFrog assigned itself, and JFrog rates it 7.8 out of 10.

Parallels Desktop runs Windows and Linux inside virtual machines on a Mac. It installs a background service called prl\_disp\_service that runs as root, because its work includes setting up host networking and unpacking virtual machine packages.

The flaw is on the Mac side of the product, so the machine at risk is the Mac itself rather than the virtual machines on it.

On the machine JFrog tested, the socket that the service listens on was world-writable, meaning any program on the Mac could connect to it. The login call that follows, PrlSrv\_LoginLocal, checks only the credentials the kernel reports for the connecting process. It needs no Parallels code signature and works for an account that is not an administrator.

To install a virtual machine appliance, the service builds its unpack command as one line of text, tar -xf "%1" -C "%2". It then splits that text back into separate arguments using Qt's QProcess::splitCommand.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The caller chooses part of that text, because it picks the folder the new virtual machine goes into. A double quote inside the folder name closes the quoting early, so whatever the attacker put after it becomes extra options for tar instead of part of a path.

The option JFrog used was --use-compress-program, which tells macOS tar to hand the archive to another program first. Because tar is running as root here, that program runs as root too. JFrog's test script wrote a passwordless sudo rule and opened a root shell.

JFrog demonstrated this on Parallels Desktop 26.4.0, build 57513, on a Mac with an Apple silicon chip. It says a normal install already provides everything the attack needs: the product installed, the service running with its socket present, and a low-privileged local account. No virtual machine has to be running.

The company did not check every build. "We did not regression-test every older build for this writeup," it said, telling readers instead: "Treat any Desktop install that still exposes the same InstallAppliance extract template and world-writable dispatcher socket as in scope."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgtNKvv0IHDLZJYdxhh14A4vtvf284aZri2FUqmDvn_1-QcBnfKFDNIzu00j8ETyVka4GWvB_rMFieL3lt3XoZxSftGxwAvnV7OzmnN5UW3uEL7tWbcIXgJAOe0aR6huvN29boeyVdJW_u84S7xAAXs4YcT6zDrNuNg0osdvmkicrGHBBZrv1qyPVUBmpk/s1700-nu-rw-lo-l85-e365/para.jpg)

JFrog also said the App Store edition may start its services differently, while describing the underlying risk as the same kind of problem. It reports no attacks using the flaw, and Parallels has published nothing about it.

The reason a local flaw matters here, JFrog said, is that code running as a normal user is common on these machines. A malicious Homebrew formula, a poisoned npm install script, or a compromised build job would each qualify, as would one weak account on a shared lab or training Mac.

### The Fix, and Which Build Has It

JFrog says the change that fixes the flaw is in Parallels Desktop 27. Its [advisory](https://research.jfrog.com/vulnerabilities/parallels-desktop-is-vulnerable-to-a-local-privilege-escalation-via-appliance-extract-argument-injection-cve-2026-90894/) lists everything below 27.0.0 as affected, its writeup names 27.0.0 as the fixed version, and the CVE record lists 27.0.0 as unaffected.

The dates do not line up. JFrog's own disclosure timeline gives 1 September 2026 as the day the fix shipped in 27.0.0, but Parallels' [release notes](https://kb.parallels.com/en/131168) put 27.0.0 on 25 August 2026 and 27.0.1 on 1 September 2026.

Installing the newest release on that line covers both readings, because 27.0.1, build 58670, shipped after both dates. Parallels has not published a statement about CVE-2026-90894, so there is no vendor record indicating which build incorporates the change.

Parallels says it does not discuss vulnerabilities until a fix has been released publicly. Its [list of security fixes](https://kb.parallels.com/en/125013), which maps each flaw to the version that repairs it, has not been reviewed since May 2025 and does not include this one.

### Who Cannot Install It

Parallels Desktop 27 needs a Mac with an Apple silicon chip. Its [system requirements](https://kb.parallels.com/en/124223) list Apple silicon only for the processor and macOS Sonoma 14.7 or newer for the operating system. On earlier releases of macOS, including Ventura 13, the installer sets up an older version of the product instead.

Parallels removed Intel Mac support in version 27 and says the change follows Apple's plans rather than its own. macOS 26 Tahoe was the ...