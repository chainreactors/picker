---
title: Timelines
url: http://windowsir.blogspot.com/2026/06/timelines.html
source: Instapaper: Unread
date: 2026-06-20
fetch_date: 2026-06-21T06:50:21.292645
---

# Timelines

# [Windows Incident Response](http://windowsir.blogspot.com/)

The Windows Incident Response Blog is dedicated to the myriad information surrounding and inherent to the topics of IR and digital analysis of Windows systems. This blog provides information in support of my books; "Windows Forensic Analysis" (1st thru 4th editions), "Windows Registry Forensics",
as well as the book I co-authored with Cory Altheide, "Digital Forensics with Open Source Tools".

## Friday, June 19, 2026

### Timelines

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOfksuuRwrgJCYga65tTT2plp5VPrPRllH2yHnV9EiPV25RKs2BUZcv57z2IMWRjkKEMQpCI6-r8iZPI2rRDWRyx6j9LFZR92lQmskul3nkJDENlJRmjBkIIG1D9uNr9TVQeZY4naJGGs-n_DUFpi5w5jafJaYdSmGOGoDDWaMp3TCbW2qTQ/w136-h200/iron_man.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOfksuuRwrgJCYga65tTT2plp5VPrPRllH2yHnV9EiPV25RKs2BUZcv57z2IMWRjkKEMQpCI6-r8iZPI2rRDWRyx6j9LFZR92lQmskul3nkJDENlJRmjBkIIG1D9uNr9TVQeZY4naJGGs-n_DUFpi5w5jafJaYdSmGOGoDDWaMp3TCbW2qTQ/s640/iron_man.jpg)

I like timelines, particularly when it comes to forensic investigations.

There I said it. The first step to addressing an issue is admitting that you have a problem.

I've been creating timelines since about 2008-ish, or so. I have a series of blog posts specifically on the topic of timeline analysis [starting in Feb 2009](https://windowsir.blogspot.com/2009/02/timeline-analysis.html), where I walk through some of the tools I used at the time to create timelines based on a 5-field "TLN" format that I developed...and still use to this day.

For example, take a look at [this recent Huntress blog post](https://www.huntress.com/blog/muddywater-attack-chain) regarding activity attributed to the group "MuddyWater"; the time-based information in the blog post has the "Z" stripped from the time stamp, and spacing reduced, but when I drafted parts of this blog post, those sections included timeline info.

Another example is [this blog post](https://www.sophos.com/en-us/blog/wmi-persistence) published almost a decade ago when I was with SecureWorks, which is now owned by Sophos. Right there in Figure 1, you see a timeline excerpt in the same format I used for about 8 yrs prior to that point, and still use today.

Yes, things have changed over time. I developed [eventmap](https://github.com/keydet89/Tools/blob/master/exe/eventmap.txt) to help me "tag" event records within a timeline to help separate events of interest from the noise, and I later developed [Events Ripper](https://github.com/keydet89/Events-Ripper) to help develop pivot points within the timeline.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjj0C2LpgU1dgQ1adYdsu1iblOgyvKZ9nZOAG1pG3_k1uZ3opcro5TQvR8q1dWZ8mR3NIIQ0v8arcMYhTsM-OCQCKMX282alIBqegJxOM5hRq-6EJmZMIR4ojekwCs8PW8ZSx1Or6NxE0MIpTKJpz0tX524L5iNmIdcHOK_ce2EJU5nASVEvA/s320/blog.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjj0C2LpgU1dgQ1adYdsu1iblOgyvKZ9nZOAG1pG3_k1uZ3opcro5TQvR8q1dWZ8mR3NIIQ0v8arcMYhTsM-OCQCKMX282alIBqegJxOM5hRq-6EJmZMIR4ojekwCs8PW8ZSx1Or6NxE0MIpTKJpz0tX524L5iNmIdcHOK_ce2EJU5nASVEvA/s1313/blog.png)

More recently, [Lindsey](https://www.linkedin.com/in/lindsey-o-donnell-welch-abb72b4a/) and I [published a Huntress blog](https://www.huntress.com/blog/akira-ransomware-limewire-data-exfiltration) based on an investigation into a threat actor's activities that led up to ransomware being deployed. For my part, the investigation into the virtual machine (provided by the customer) involved many of the very same tools and techniques talked about in my books, going back over a decade and a half, or more. I created [micro-timelines](https://windowsir.blogspot.com/2015/04/micro-mini-timelines.html) and overlays from various data sources (MFT, USN change journal, browser history, etc.), and much like the drawing of the armor from the first IronMan movie, once the individual pieces were aligned and laid over each other, the full picture came into view.

*The Power of Timelines*
The DFIR Spot recently published a blog post discussing [the power of forensic timelines](https://www.thedfirspot.com/post/from-chaos-to-chronology-the-power-of-forensic-timelines); the blog post references [this LinkedIn post](https://www.linkedin.com/posts/cebrewer_introducing-sniper-incident-response-a-faster-activity-7325187584077299712-dW5h/) from [Chris Brewer](https://www.linkedin.com/in/cebrewer/), and the first line of the LinkedIn post mentions "sniper incident response", a clear nod to [Chris Pogue](https://www.linkedin.com/in/christopher-pogue-msis-6148441/)'s "[sniper forensics](https://archives.sector.ca/presentations12/Chris%20Pogue%20-%20Sniper%20Forensics%20Reloaded%20-%20Sector%202012.pdf)".

A timeline is a powerful tool, and *not* something that should be left to the end of the engagement, where an analyst manually fills in a spreadsheet, because they have to. Rather, for me, a timeline has always been the first step in an engagement (yes, \*after\* collecting data sources). Timelines are incredible investigative tools, providing insight into activity and timing, as well as providing context.

A timeline can help direct the analyst to other data sources; if those data sources aren't available, that fact gets documented, as it can apply to control efficacy.

Posted by
H. Carvey

at
[9:51 AM](http://windowsir.blogspot.com/2026/06/timelines.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/9518042/8397599789600874797 "Email Post")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=9518042&postID=8397599789600874797&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=9518042&postID=8397599789600874797&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=9518042&postID=8397599789600874797&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=9518042&postID=8397599789600874797&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=9518042&postID=8397599789600874797&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=9518042&postID=8397599789600874797&target=pinterest "Share to Pinterest")

#### No comments:

[Post a Comment](https://www.blogger.com/comment/fullpage/post/9518042/8397599789600874797)

[Newer Post](http://windowsir.blogspot.com/2026/06/timelines.html "Newer Post")

[Older Post](http://windowsir.blogspot.com/2026/03/lnk-files.html "Older Post")
[Home](http://windowsir.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](http://windowsir.blogspot.com/feeds/8397599789600874797/comments/default)

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

[![](https://resources.blogblog.com/img/widgets/sub...