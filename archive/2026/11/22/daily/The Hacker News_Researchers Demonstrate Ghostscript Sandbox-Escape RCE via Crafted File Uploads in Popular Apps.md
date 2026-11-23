---
title: Researchers Demonstrate Ghostscript Sandbox-Escape RCE via Crafted File Uploads in Popular Apps
url: https://thehackernews.com/2026/11/researchers-demonstrate-ghostscript.html
source: The Hacker News
date: 2026-11-22
fetch_date: 2026-11-23T10:02:57.594430
---

# Researchers Demonstrate Ghostscript Sandbox-Escape RCE via Crafted File Uploads in Popular Apps

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

# [Researchers Demonstrate Ghostscript Sandbox-Escape RCE via Crafted File Uploads in Popular Apps](https://thehackernews.com/2026/11/researchers-demonstrate-ghostscript.html)

**Swati Khandelwal**Nov 22, 2026Vulnerability / Application Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1BiCJUIrSJXNfKPZEkM46ynK6Rs7gba2xMaTUdoJ7yOK6Y8kcKMqJ_6PhbUIog_U1E8gRCpbj2HrkQ9UEpbPi1HOvkxdxCE5Afa5LbkNhUPvgU7Sa60IVHAWqSvgJaX1p6frMAN335QncL5UTZ3a4v1-agyb8ZXIlMGZTOtzsC0Gll2qRI0NJNMHTsf8/s1700-nu-rw-lo-l85-e365/ghostscript.jpg)

A now-patched flaw in **Ghostscript** allows a crafted file to escape the program's security sandbox and run commands on the server that processes it.

Ghostscript is the interpreter that many Linux servers use to convert uploaded PDFs, PostScript files, and images into other formats, often without the application calling it directly.

Security firm **pwn.ai** showed this week that ordinary upload, preview, and print features in about ten common applications could be tricked into feeding it such a file. The flaw, tracked as **CVE-2026-125396**, was fixed on September 8, and there have been no reports of it being used in attacks.

Getting a crafted file to Ghostscript is easy, because an application does not have to call it directly. A common image or document library such as ImageMagick, Pillow, libvips, or a Qt plugin will hand PostScript or EPS content to Ghostscript to render, even when the file is named .png, .jpg, or .pdf. A routine feature like making a thumbnail or cropping a picture can start the interpreter, and the exact path depends on the libraries the application uses.

The underlying bug is a **use-after-free** in the part of Ghostscript that loads fonts. A crafted document uses it to switch off the checks in -dSAFER, the sandbox that is supposed to stop the document from running commands or reaching files.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

The security firm demonstrated the result by feeding such a document through about ten applications and watching a command run on the server, each time as the low-privilege account that does the rendering.

Several of those paths needed no login: an anonymous print job to a shared Debian 13 queue, an emailed attachment that Roundcube webmail processed the moment the recipient opened the message, and public upload forms in the WordPress plugins Forminator and Essential Addons for Elementor.

WordPress Core itself needed more: an account with the ability to upload files, which Authors and higher roles have by default. Although the CVE is classified as a local flaw, the firm's tests reached Ghostscript from the network via print jobs, email, and web uploads. The tested version and the access needed for each application are set out in its [impact index](https://pwn.ai/upload2shell).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgA_YI3fW4fXSODuopSTSl0HXghgDNJ146VJIpphD0EH0FLIOoBDNYmHkefbs1vJfXYvWvkdClrIIjBBM0_wWsFjC549kSMrNBzQIs1HGcxEjMd5C4rIa2PdVvmkSjZPdNMRZ8IaHZNZsrU4ztHC-h-sf9YXw8zWdKyUWQHyO5l3D_4kZIAZwzjMJLNvPI/s1700-nu-rw-lo-l85-e365/use-after.jpg)

**Artifex**, which develops Ghostscript, fixed the flaw in version 10.08.0 on September 8, and is moving the vulnerable internal step into safer code. Ken Sharp, the developer who handled the fix, called that step "an ancient piece of code well known to be a vulnerability, but difficult to eradicate" in the [bug report](https://bugs.ghostscript.com/show_bug.cgi?id=709684). The CVE was published last week and is scored 8.5 out of 10 in its [security advisory](https://www.vulncheck.com/advisories/ghostscript-before-10.08.0-dsafer-bypass-via-putgstringcopy-forceput-recovery).

WordPress had already closed its own upload path in version 7.0.4 on August 12, under a separate identifier, CVE-2026-65640, as noted in its [release notes](https://wordpress.org/news/2026/08/wordpress-7-0-4-release/). That fix and the Ghostscript fix cover different points in the same chain, so updating one does not remove the need for the other.

### Updating the Renderer

The fix helps only where it reaches the renderer the application actually uses. Updating the host operating system does not update a separate copy of Ghostscript bundled inside a container image or an application, so a document worker can keep running the old code after the host package is replaced.

Coverage across Linux distributions is uneven. As of last week, several still shipped a vulnerable Ghostscript or had a fix pending, according to the firm's survey. The list records package status, not a tested attack path for each system:

* **Debian 12 (Bookworm):** listed as vulnerable
* **Amazon Linux 2, 2023, and 2027 Preview:** fix pending
* **SUSE Linux Enterprise 12 SP5 and parts of 15:** fix in progress
* **SUSE Linux Enterprise Server 16.0 and 16.1:** fix in progress
* **openSUSE Leap 16.0 and 16.1:** affected

The firm did not establish whether current Red Hat, Rocky Linux, AlmaLinux, Oracle Linux, or stable Fedora packages carry the fix.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

Until the renderer is updated, the exposure can be reduced by requiring authentication on print queues and by limiting which file types an image processor accepts. System controls help too, and in one test an AppArmor profile stopped the compromised interpreter from starting a shell.

One published proof-of-concept file, described in its [technical analysis](https://pwn.ai/upload2shell/research.html), shows only the core memory trick. It changes a value inside the running interpreter and sets it back, without running a shell command or touching files on the host, and on the patched 10.08.0 build it fails before that point.

The firm's broader research extended to production services, including Google, which fixed the affected path last week. Its reports of similar proble...