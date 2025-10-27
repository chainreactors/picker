---
title: Program Execution The ShimCacheAmCache Myth
url: http://windowsir.blogspot.com/2024/11/program-execution-shimcacheamcache-myth.html
source: Instapaper: Unread
date: 2024-11-29
fetch_date: 2025-10-06T19:20:27.555639
---

# Program Execution The ShimCacheAmCache Myth

# [Windows Incident Response](http://windowsir.blogspot.com/)

The Windows Incident Response Blog is dedicated to the myriad information surrounding and inherent to the topics of IR and digital analysis of Windows systems. This blog provides information in support of my books; "Windows Forensic Analysis" (1st thru 4th editions), "Windows Registry Forensics",
as well as the book I co-authored with Cory Altheide, "Digital Forensics with Open Source Tools".

## Tuesday, November 26, 2024

### Program Execution: The ShimCache/AmCache Myth

I recently saw another LinkedIn post from someone [supporting and sending readers to a site](https://evids.dfir.tips/) that was reportedly started using the [SANS DFIR poster](https://www.sans.org/blog/updated-windows-forensic-analysis-poster/) as a reference. As illustrated in figure 1, this site references the ShimCache artifact as providing evidence of program execution, and does the same for the AmCache artifact, as well.

|  |
| --- |
| [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi7NU_pnV-D71ymDNMYfEWn9H0DQR4lvwzGL0nVuMlrAq5_RCedmVytyMPWY_ZxHCLGWRrEe0izC1tJ9Nqm5_xWNF79-QTTDbngAJ19SJF8BzZhYccUwa5jmNFWU9w9aWxXFFjqvRrHb1l4MF0ELpUADbU81_RcTpMQ8l61HZSNl5YV9Jl2Pw/w400-h31/shim.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi7NU_pnV-D71ymDNMYfEWn9H0DQR4lvwzGL0nVuMlrAq5_RCedmVytyMPWY_ZxHCLGWRrEe0izC1tJ9Nqm5_xWNF79-QTTDbngAJ19SJF8BzZhYccUwa5jmNFWU9w9aWxXFFjqvRrHb1l4MF0ELpUADbU81_RcTpMQ8l61HZSNl5YV9Jl2Pw/s532/shim.png) |
| *Figure 1: ShimCache Entry* |

Now, while yes, it is true that these artifacts *can* provide evidence of program execution, that is not always the case, and this needs to be understood throughout the community.

What I'm going to do with this blog post is provide the resources to show why these artifacts do not solely provide evidence of "program execution", so that others in the community can reference these resources.

*ShimCache*Mandiant's [article regarding ShimCache](https://cloud.google.com/blog/topics/threat-intelligence/caching-out-the-val/) includes the statement illustrated in figure 2.

|  |
| --- |
| [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjwTvP5zfS6I5dfcirXmTAC62euTW55IWoGjJLur4Ats3c6J0peKHwmzDT0NzIv7beSEnKEiba6CVle5e9jlpAZpGjlqG26Ih_t4v0NVTKWyY7yTcX6sjpXrO-szOmYQAV9GhfsNcLplvxCMzTwJrvjWZXGURWVIUMwWe6yqdf8mXBASzZTMg/w400-h124/shim.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjwTvP5zfS6I5dfcirXmTAC62euTW55IWoGjJLur4Ats3c6J0peKHwmzDT0NzIv7beSEnKEiba6CVle5e9jlpAZpGjlqG26Ih_t4v0NVTKWyY7yTcX6sjpXrO-szOmYQAV9GhfsNcLplvxCMzTwJrvjWZXGURWVIUMwWe6yqdf8mXBASzZTMg/s858/shim.png) |
| *Figure 2: Article excerpt* |

Notice the highlighted section in figure 2, which states, "...*that were not actually executed*.", and then goes on to say that entries can be added if a user browses to a folder. The ShimCache value is written to the System hive, and does not provide a reference to the user who may have browsed to a folder. As such, this is something that would need to be resolved through user profile analysis, via artifacts such as JumpLists, recently accessed files, shellbags, etc.

However, the important thing to understand here is that this reductionist approach of saying that ShimCache is evidence solely of program execution is incorrect.

We also need to remember that the ShimCache is written to the Registry value at shutdown; this is trivial to demonstrate via a timeline.

*AmCache*Blanche Lagney's *[Analysis of AmCache v2](https://cyber.gouv.fr/sites/default/files/2019/01/anssi-coriin_2019-analysis_amcache.pdf)* paper is the definitive reference for *all things AmCache*. The research is thorough, and presented in a manner that, while it does require some reading to address specific questions, should remove all doubt as to the value of the artifact on specific Windows builds.

If you're looking at *just* the AmCache.hve file as an artifact to determine program execution, you're going to need to find the closest match to the Windows build and libraries, based on the keys you're looking at, to better understand the nature of the artifacts you're seeing.

*Analysis Process*
The key here is ***not*** to try to memorize the "value" of individual artifacts in isolation, but to have an analysis process where multiple data sources and artifacts are viewed together, so that through this process you can 'see' the context of the events in question. For example, when it comes to program execution, we might look to JumpLists, Security (if configured) and/or Sysmon (if installed) Event Logs, UserAssist entries, and on workstation platforms, Prefetch files. On Windows 11, we might also look to [data within the PCA folder](https://windowsir.blogspot.com/2024/02/pcaparse.html). To validate that a program executed, we might look to impacts in the Registry and/or file system, or to the Application Event Log to determine if the program generated an error or crashed.

For teaching/instructional purposes, it would be extremely valuable to start by describing one data source, such as the file system, and then show how that data source can be viewed via a timeline. Then, add another data source, such as the Windows Event Log or the Registry, and add that data source to the timeline. When discussing the Registry (as well as the ShimCache and AmCache artifacts), it will be important for analysts to understand the value of time-based metadata (key LastWrite times), as well as time-based data embedded within individual values, all of which can help better address analysis categories such as "program execution".

*Conclusion*
While it is valuable to have an understanding of various artifacts, the most important takeaway from this article is that analysts should not consider artifacts in isolation during an investigation, but should instead look to multiple data sources and artifacts, viewed together, to determine the nature and context of events in question.

Posted by
H. Carvey

at
[12:53 PM](http://windowsir.blogspot.com/2024/11/program-execution-shimcacheamcache-myth.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/9518042/1331546872667174517 "Email Post")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=9518042&postID=1331546872667174517&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=9518042&postID=1331546872667174517&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=9518042&postID=1331546872667174517&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=9518042&postID=1331546872667174517&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=9518042&postID=1331546872667174517&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=9518042&postID=1331546872667174517&target=pinterest "Share to Pinterest")

#### 1 comment:

[![](//www.blogger.com/img/blogger_logo_round_35.png "Ken Pryor")](https://www.blogger.com/profile/06777221347861058406) [Ken Pryor](https://www.blogger.com/profile/06777221347861058406) said...
:   I've been more active on LinkedIn lately due to my work situation. I've gotten some good things out of it but there are so many people who seem to be re-posting things mostly for the attention it brings them. I don't think it even matters sometimes how useful the information they're re-posting actually is. Not recently, but in the past I've seen outright theft of e-books with people posting the full book to LinkedIn.
    Regarding the Shimcache/Amcache information: That's definitely an area I need to get smarter on. Time to set up a VM and see what I can learn.
:   [11:20 AM](http://windowsir.blogspot.com/2024/11/program-execution-shimcacheamcache-myth.html?showComment=1732724444899#c8778877009366732430 "comment permalink")

    [![]...