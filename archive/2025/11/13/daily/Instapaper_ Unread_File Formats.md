---
title: File Formats
url: http://windowsir.blogspot.com/2025/11/file-formats.html
source: Instapaper: Unread
date: 2025-11-13
fetch_date: 2025-11-14T03:13:40.663833
---

# File Formats

# [Windows Incident Response](http://windowsir.blogspot.com/)

The Windows Incident Response Blog is dedicated to the myriad information surrounding and inherent to the topics of IR and digital analysis of Windows systems. This blog provides information in support of my books; "Windows Forensic Analysis" (1st thru 4th editions), "Windows Registry Forensics",
as well as the book I co-authored with Cory Altheide, "Digital Forensics with Open Source Tools".

## Wednesday, November 12, 2025

### File Formats

I'm a huge fan of MS file formats, mostly because they provide for the possibility of an immense (and often untapped, unexploited) amount of metadata. Anyone who's followed me for any length of time, or has read my blog, knows that I'm a huge fan of file formats such as Registry hives (and non-Registry files with the same structure), as well as LNK files.

Historically, lots of different MS file formats have contained significant, and often damning, metadata. Anyone remember the issue of [MSWord metadata](https://seclists.org/politech/2003/Jun/105) that the Blair administration encountered over two decades ago? I [shared some information](https://windowsir.blogspot.com/2006/09/metadata-and-ediscovery.html) related to coding, using the file as an exemplar, in the [WindowsIR](https://windowsir.blogspot.com/) blog.

I ran across [a LinkedIn post](https://www.linkedin.com/posts/mauricefielenbach_malwareanalysis-threatresearch-evilai-activity-7386837743198171139-G-aS/) from [Maurice Fielenbach](https://www.linkedin.com/in/mauricefielenbach/), where he talked about an infostealer bundled in an MSI file. Interestingly enough, MSI files are structured storage files, following the OLE format, albeit with different streams, the same as MSWord docs and [JumpList files](https://windowsir.blogspot.com/2025/01/artifacts-jump-lists.html).

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh-dWNRPnL0Sgg2jHw568emyAsNAUTyBw9YMV9C0LszBpJmlPdOxg7ueCh-k72MSY1lk1gQMFzlWB48WRrmskGWmSrQPdWZESUftm1whatJcIt0BDejRs_yqH8gtMrUYqsAgCMQzojMk7M4e2p0rCu82LOOLQscRbtBteMKBEttH1TaUjKZ3w/w400-h116/malware.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh-dWNRPnL0Sgg2jHw568emyAsNAUTyBw9YMV9C0LszBpJmlPdOxg7ueCh-k72MSY1lk1gQMFzlWB48WRrmskGWmSrQPdWZESUftm1whatJcIt0BDejRs_yqH8gtMrUYqsAgCMQzojMk7M4e2p0rCu82LOOLQscRbtBteMKBEttH1TaUjKZ3w/s1025/malware.png)

I'm not a malware RE guy, so I don't have a specialized tool set for parsing these kinds of files. I generally start with the MiTeC [Structured Storage Viewer](https://www.mitec.cz/wp/mssv/), something I've used before. In the image to the left, you can see the SummaryInformation block parsed and visible in MSSV.

If you read through the comments, M[alCat](https://malcat.fr/) is recommended as a tool to use to run or click through the structure of this file format, and others. This looks like a great possibility, and to be honest, if you're into malware analysis, the [MalCat blog](https://malcat.fr/blog.html) looks really informative, as well. If you're interested in a sample to work with yourself, I found one at [MalwareBazaar](https://bazaar.abuse.ch/sample/fde67ba523b2c1e517d679ad4eaf87925c6bbf2f171b9212462dc9a855faa34b/).

In his LinkedIn post, Maurice said, "I highly recommend taking a deeper look at the MSI file format itself and familiarizing yourself with common installer frameworks such as WiX." I'd agree, particularly given that the test.msi image shows that the creating application was the "WiX Toolset".

Regardless of the tools you use, and the area of cybersecurity that you're in or focused on, information like this can expand your knowledge base as to what's possible, or by providing new directions for study or skill expansion. This is not only valuable as a malware or DF analyst, but also for threat intel analysts, as this information can add context and granularity to the intel you're developing.

Posted by
H. Carvey

at
[9:46 AM](http://windowsir.blogspot.com/2025/11/file-formats.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/9518042/3248916280506055866 "Email Post")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=9518042&postID=3248916280506055866&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=9518042&postID=3248916280506055866&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=9518042&postID=3248916280506055866&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=9518042&postID=3248916280506055866&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=9518042&postID=3248916280506055866&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=9518042&postID=3248916280506055866&target=pinterest "Share to Pinterest")

#### No comments:

[Post a Comment](https://www.blogger.com/comment/fullpage/post/9518042/3248916280506055866)

[Newer Post](http://windowsir.blogspot.com/2025/11/images.html "Newer Post")

[Older Post](http://windowsir.blogspot.com/2025/11/what-we-value.html "Older Post")
[Home](http://windowsir.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](http://windowsir.blogspot.com/feeds/3248916280506055866/comments/default)

## Pages

* [Home](http://windowsir.blogspot.com/)
* [Timelines](http://windowsir.blogspot.com/p/timelines.html)
* [Books](http://windowsir.blogspot.com/p/books.html)
* [Malware](http://windowsir.blogspot.com/p/malware.html)
* [FOSS Tools](http://windowsir.blogspot.com/p/foss-tools.html)

## Subscribe To WindowsIR

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)
![](https://resources.blogblog.com/img/icon_feed12.png)
Posts

[![](https://resources.blogblog.com/img/widgets/subscribe-netvibes.png)](https://www.netvibes.com/subscribe.php?url=http%3A%2F%2Fwindowsir.blogspot.com%2Ffeeds%2Fposts%2Fdefault)
[![](https://resources.blogblog.com/img/widgets/subscribe-yahoo.png)](https://add.my.yahoo.com/content?url=http%3A%2F%2Fwindowsir.blogspot.com%2Ffeeds%2Fposts%2Fdefault)
[![](https://resources.blogblog.com/img/icon_feed12.png)
Atom](http://windowsir.blogspot.com/feeds/posts/default)

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)

![](https://resources.blogblog.com/img/icon_feed12.png)
Posts

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)
![](https://resources.blogblog.com/img/icon_feed12.png)
Comments

[![](https://resources.blogblog.com/img/widgets/subscribe-netvibes.png)](https://www.netvibes.com/subscribe.php?url=http%3A%2F%2Fwindowsir.blogspot.com%2Ffeeds%2F3248916280506055866%2Fcomments%2Fdefault)
[![](https://resources.blogblog.com/img/widgets/subscribe-yahoo.png)](https://add.my.yahoo.com/content?url=http%3A%2F%2Fwindowsir.blogspot.com%2Ffeeds%2F3248916280506055866%2Fcomments%2Fdefault)
[![](https://resources.blogblog.com/img/icon_feed12.png)
Atom](http://windowsir.blogspot.com/feeds/3248916280506055866/comments/default)

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)

![](https://resources.blogblog.com/img/icon_feed12.png)
Comments

## WindowsIR Blog List

* ![]()

  [Brett Shavers](https://brettshavers.com/brett-s-blog)

  [Perfect seizure or total loss? DFIR has the ideal world. Patrol has the
  real one.](https://brettshavers.com/brett-s-blog/entry/perfect-seizure-or-total-loss-you-decide)

  1 week ago
* ![]()

  [The Philosophy of DFIR](https://dfirphilosophy.blogspot.com/)

  [Selling the Science: Marketing of DF/IR Services](https://dfirphilosophy.blogspot.com/2025/11/selling-science-marketing-of-dfir.html)

  1 week ago
* ![]()

  [c-APT-ure](https://c-apt-ure.blogspot.com/)

  [Using NetBIOS names for pivoting and threat clustering](https://c-apt-ure.blogspot.com/2025/10/using-netbios-names-for-pivoting-and.html)

  1 month ago
* ![]()

  [Open Source DFIR](https://osd...