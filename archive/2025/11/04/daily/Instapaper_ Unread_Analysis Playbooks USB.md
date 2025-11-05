---
title: Analysis Playbooks USB
url: http://windowsir.blogspot.com/2025/11/analysis-playbooks-usb.html
source: Instapaper: Unread
date: 2025-11-04
fetch_date: 2025-11-05T03:12:43.130063
---

# Analysis Playbooks USB

# [Windows Incident Response](http://windowsir.blogspot.com/)

The Windows Incident Response Blog is dedicated to the myriad information surrounding and inherent to the topics of IR and digital analysis of Windows systems. This blog provides information in support of my books; "Windows Forensic Analysis" (1st thru 4th editions), "Windows Registry Forensics",
as well as the book I co-authored with Cory Altheide, "Digital Forensics with Open Source Tools".

## Monday, November 03, 2025

### Analysis Playbooks: USB

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEijvmOUqvZ7cmPGnPFUigIel_4tSXk9_Rq7ARUNwHzOMX2htBRGirfAybo7tBUpRax3CiBGvxEjMWnUty5UODCVkjdhGih4OLPNY4IqCD6xNbFdhVGcGQnHzgodId-aUI-T3RrM0JHQ4S3l5OSM38RF_Tr-oweFzvL3Zv-K1vPVG8E1cf-k9g/w200-h150/thumb.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEijvmOUqvZ7cmPGnPFUigIel_4tSXk9_Rq7ARUNwHzOMX2htBRGirfAybo7tBUpRax3CiBGvxEjMWnUty5UODCVkjdhGih4OLPNY4IqCD6xNbFdhVGcGQnHzgodId-aUI-T3RrM0JHQ4S3l5OSM38RF_Tr-oweFzvL3Zv-K1vPVG8E1cf-k9g/s640/thumb.jpg)

In 2005, Cory Altheide and I published the [first peer-reviewed paper](https://www.sciencedirect.com/science/article/abs/pii/S1742287605000320) to address tracking USB devices on Windows systems. Over the years, it's been pretty amazing to see not only the artifacts expand and evolve, but to also see folks pick up the baton and carry on with describing what amounts to a "playbook" for developing this information as part of an investigation. Not only did malware such as [Raspberry Robin](https://www.checkpoint.com/cyber-hub/threat-prevention/what-is-malware/raspberry-robin-malware/) propagate via USB devices, but with the rise of other devices that could be attached via a USB connection, but use different protocols, it became more important to operationalize this analysis in a playbook.

After all, why not take the inefficient, error-prone, purely manual aspects out of the parsing by automating it?

[Morad R.](https://www.linkedin.com/in/morad-rawashdeh/) put together a series of posts that outline different data/artifact sources you can examine to identify USB devices that had been connected to the endpoint, as well as attribute the use of the devices to a particular user. This series of posts illustrates some steps that begin the process of pulling back the veil, if you will, to unraveling the use of USB devices on Windows systems. While there is definitely more to be done and shared, the important common factor across the posts is the use of timelines.

[USB Forensics, pt 1: Unmasking the connected device](https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A7385564679512961024/) - Focuses on the System Registry hive, and extracting time stamps from Properties key values. The focus on a timeline is great way to get started on this, as doing so takes the analyst directly to context.

However, by focusing on just USB and USBStor keys in the System hive, [other devices](https://windowsir.blogspot.com/2022/03/the-misuse-of-artifact-categories-pt-ii.html) (smartphones, digital cameras) are missed. However, that's not really an issue, per se, as the same playbook can be applied to the appropriate Registry keys.

[USB Forensics, pt 2: Mapping device to user & drive letter](https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A7388103261481750528/) - focuses on the user's NTUSER.DAT, but doesn't mention other artifacts, such as shellbags, RecentDocs, UserAssist, etc., that could be used to correlate additional user activity with the device, particularly via a timeline.

[RegRipper](https://github.com/keydet89/RegRipper4.0) still makes use of "[profiles](https://windowsir.blogspot.com/2011/09/stuffand-whatnot.html)", which is the term I used to describe what became known as "playbooks". Or, another way to look at it is that you can implement playbooks through these profiles.

[USB Forensics, pt 3: The Event Log timeline](https://www.linkedin.com/posts/morad-rawashdeh_usbforensics-dfir-eventloganalysis-ugcPost-7390644720336654336-gw_L/) - focus on a timeline continues, which is good. However, the logs are technically referred to as "Windows Event Logs"; "Event Logs" refer to the Windows 2000, XP, and 2003 era logs. I understand, I 'get it', that this is a distinction without a difference for most analysts, particularly those who've never had to work with Event Log records from older systems, and are only familiar with the new format implemented as of Windows Vista.

All three of these posts, together, serve as a good foundation, and a great first step toward addressing USB-connected devices on Windows endpoints. Just as the field has grown and expanded since 2005, it will continue to do so in the future. In addition to providing the data sources, the underlying reliance on (or at least pointing in the direction of) timelines is, I believe, foundational. *Start with* a timeline, do not let a timeline be something you assemble manually, after everything else is done. We can always add or remove data sources, create new RegRipper or Events Ripper plugins, etc., but creating a timeline should be "first principles".

In my current role, I don't have a need to determine things such as USB devices connected to a Windows system, but if I did, I'd definitely have [Events Ripper](https://github.com/keydet89/Events-Ripper) plugins to extract that information, maybe even correlate it, into an easy-to-view manner.

This is just some of the content from my blog that explicitly addresses USB devices:

[Something old, something new...with USB](https://windowsir.blogspot.com/2006/09/something-old-something-newwith-usb.html) - 2006-09-26

[From the Lab: Mapping USB devices via LNK files](https://windowsir.blogspot.com/2007/04/from-lab-mapping-usb-devices-via-lnk.html) - 2007-04-09

[HowTo: USB Thumb Drives](https://windowsir.blogspot.com/2022/03/the-misuse-of-artifact-categories-pt-ii.html) - 2012-02-04

[HowTo: Correlate an Attached Device to a User](https://windowsir.blogspot.com/2013/07/howto-correlate-attached-device-to-user.html) - 2013-07-01

[USB device redux, with timelines](https://windowsir.blogspot.com/2022/05/usb-device-redux-with-timelines.html) - 2022-05-26

Posted by
H. Carvey

at
[1:28 PM](http://windowsir.blogspot.com/2025/11/analysis-playbooks-usb.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/9518042/890834753388522326 "Email Post")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=9518042&postID=890834753388522326&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=9518042&postID=890834753388522326&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=9518042&postID=890834753388522326&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=9518042&postID=890834753388522326&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=9518042&postID=890834753388522326&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=9518042&postID=890834753388522326&target=pinterest "Share to Pinterest")

#### No comments:

[Post a Comment](https://www.blogger.com/comment/fullpage/post/9518042/890834753388522326)

[Older Post](http://windowsir.blogspot.com/2025/10/registry-analysis.html "Older Post")
[Home](http://windowsir.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](http://windowsir.blogspot.com/feeds/890834753388522326/comments/default)

## Pages

* [Home](http://windowsir.blogspot.com/)
* [Timelines](http://windowsir.blogspot.com/p/timelines.html)
* [Books](http://windowsir.blogspot.com/p/books.html)
* [Malware](http://windowsir.blogspot.com/p/malware.html)
* [FOSS Tools](http://windowsir.blogspot.com/p/foss-tools.html)

## Subscribe To WindowsIR

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)
![](https://resources.b...