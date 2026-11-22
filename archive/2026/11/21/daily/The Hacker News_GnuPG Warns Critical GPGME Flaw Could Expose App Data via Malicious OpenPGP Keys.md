---
title: GnuPG Warns Critical GPGME Flaw Could Expose App Data via Malicious OpenPGP Keys
url: https://thehackernews.com/2026/11/gnupg-warns-critical-gpgme-flaw-could.html
source: The Hacker News
date: 2026-11-21
fetch_date: 2026-11-22T09:02:52.538582
---

# GnuPG Warns Critical GPGME Flaw Could Expose App Data via Malicious OpenPGP Keys

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [GnuPG Warns Critical GPGME Flaw Could Expose App Data via Malicious OpenPGP Keys](https://thehackernews.com/2026/11/gnupg-warns-critical-gpgme-flaw-could.html)

**Ravie Lakshmanan**Nov 21, 2026Vulnerability / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiTmX4ayWzvM0EzPttZ610B2837FppeU5AEmQmztLH2lai78EDQtjrp4wVI_bubSe2c2NGBE5sqBT9Py1mKkHQKN2faBkOzU70d7FntrpYD7Et2eeBxLNy2gzByAo1i8Aaw_VMBZD62RnBMY2md3iNfegK9M_NR5qTRDBw8s0uwKy1w7JoTV0zkDS_17Lse/s1700-nu-rw-lo-l85-e365/pgp.jpg)

A malicious **OpenPGP** key with an unusually long user ID can trigger a critical memory bug in **GPGME**, the standard library that programs use to work with GnuPG.

The GnuPG project warned yesterday that the flaw could be used to steal data from affected applications and has released fixed versions.

The bug, tracked as **CVE-2026-129975**, affects all software that uses GPGME before version 2.3.0, whether the library is loaded as a shared library, a Windows DLL, or statically linked into the program.

Examples the project gives include most mail clients, many XMPP clients, Samba, and its own Gpg4win, GnuPG Desktop, and GnuPG VS-Desktop packages.

The project has not reported any attacks exploiting the flaw, and it notes that remote code execution cannot be ruled out.

Its example of a path to the bug is signed data sent to an application. Which programs pass such material to the library without a manual key import is not something the advisory says.

The flaw is a double free, meaning the same memory is released twice. It sits in two routines, read\_status() and read\_colon\_line(), that read status lines and key listings coming back from GnuPG.

When the input runs long, the routines move the data to a larger buffer but record the new address only if they finish without errors. An error in between leaves a pointer to memory that was already freed, and cleanup then frees it a second time, as the project's [tracker entry](https://static.dev.gnupg.org/T8557.html) details.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

The flaw was found by Johan Carlsson and reported to the project by GitLab last week. Disclosure was set for November 25, the advisory says, and moved up because the new Ruby2Shell bug forced the company to update earlier.

### What to Update

The fixed library version is GPGME 2.3.1, released this week. A version 2.3.0 was never publicly available.

What to install depends on where the library sits:

* **Shared library or DLL**: update to GPGME 2.3.1, available from the project's [official downloads](https://gnupg.org/download/) and detailed in its [security advisory](https://lists.gnupg.org/pipermail/gnupg-announce/2026q4/000517.html).
* **Windows**: Gpg4win 5.1.2 bundles the fixed library. Its [release notes](https://www.gpg4win.org/change-history.html) call the issue severe and say to update as soon as possible.
* **Older versions that cannot move to 2.3.1**: the advisory carries a patch, and the legacy branch has its own fixed release, 1.24.4, whose [legacy release notes](https://dev.gnupg.org/T7659.html) say the project cannot guarantee that the branch will see every security patch.
* **Bundled and statically linked copies**: these are affected too, and updates to the system's shared library do not reach them, so the applications that contain them need their own rebuilt releases.
* **GPGMEPP and GPGMEQT**: no update is needed.

The advisory offers no interim workaround for software that cannot update yet.

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

[Application Security](https://thehackernews.com/search/label/Application%20Security), [GnuPG](https://thehackernews.com/search/label/GnuPG), [Memory Corruption](https://thehackernews.com/search/label/Memory%20Corruption), [OpenPGP](https://thehackernews.com/search/label/OpenPGP), [Software Security](https://thehackernews.com/search/label/Software%20Security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

WhatsApp Patches 3 Security Flaws, Including Android Bug Suspected of Use in Scams](https://thehackernews.com/2026/11/whatsapp-patches-3-security-flaws.html)

[![The Hacker News](data:image/svg+xml;base64...)

Linux KVM Flaw CVE-2026-99312 Lets Guest VMs Access Host Memory on AMD Hosts](https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html)

[![The Hacker News](data:image/svg+xml;base64...)

Hackers Exploit Critical Cisco Expressway Flaw, Breach Four Devices and Reach Internal Network](https://thehackernews.com/2026/11/hackers-exploit-critical-cisco.html)

[![The Hacker News](data:image/svg+xml;base64...)

New Unpatched Windows 0-Day FastUnlock Lets Someone Holding a Locked PC Run Programs on It](https://thehackernews.com/2026/11/new-unpatched-windows-0-day-fastunlock.html)

[![The Hacker News](data:image/svg+xml;base64...)

ThreatsDay: GPT-6.2 Jailbreak Flaws, BubbleLoader PNG Malware, $500M Ransom Demands + 17 More Stories](https://thehackernews.com/2026/11/threatsday-gpt-62-jailbreak-flaws.html)

[![The Hacker News](data:ima...