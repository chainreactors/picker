---
title: Artifacts Jump Lists
url: http://windowsir.blogspot.com/2025/01/artifacts-jump-lists.html
source: Instapaper: Unread
date: 2025-01-22
fetch_date: 2025-10-06T20:13:15.797677
---

# Artifacts Jump Lists

# [Windows Incident Response](http://windowsir.blogspot.com/)

The Windows Incident Response Blog is dedicated to the myriad information surrounding and inherent to the topics of IR and digital analysis of Windows systems. This blog provides information in support of my books; "Windows Forensic Analysis" (1st thru 4th editions), "Windows Registry Forensics",
as well as the book I co-authored with Cory Altheide, "Digital Forensics with Open Source Tools".

## Monday, January 20, 2025

### Artifacts: Jump Lists

In order to fully understand digital analysis, we need to have an understanding of the foundational methodology, as well as the various constituent artifacts on which a case may be built. The foundational methodology starts with your goals...what are you attempting to prove or disprove...and once you understand the goals of your analysis, you can assemble the necessary artifacts to leverage in pursuit of those goals.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiIc8z10Qn26HPd_DbGNrYXfHh-1Ga_OVKbMXXDy-YdNHOz2jGpXq5Xs-8lojmcvxdukigs1zjySvHmQic0wp__Y-6oSe9ePIoi-mFLt41ydPomjHlmaQfz_3pI7NIM_Uqldc6uVJswLszLWdrKeiJBifxybLhXYHMwy-HajXVcg0K6eDxamQ/s1600/jump.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiIc8z10Qn26HPd_DbGNrYXfHh-1Ga_OVKbMXXDy-YdNHOz2jGpXq5Xs-8lojmcvxdukigs1zjySvHmQic0wp__Y-6oSe9ePIoi-mFLt41ydPomjHlmaQfz_3pI7NIM_Uqldc6uVJswLszLWdrKeiJBifxybLhXYHMwy-HajXVcg0K6eDxamQ/s259/jump.jpg)

Like many of the artifacts we might examine on a Windows system, Jump Lists can provide useful information, but they are most useful when viewed in conjunction with other artifacts. Viewing artifacts in isolation deprives the analyst of valuable context.

Dr. Brian Carrier recently published an article on [Jump List Forensics](https://www.cybertriage.com/blog/jump-list-forensics-2025/) over on the CyberTriage blog. In that article, he goes into a good bit of depth regarding both the Automatic and Custom Jump Lists, and for the sake of this article, I'm going to cover just the Automatic Jump Lists.

As Brian stated in his article, Jump Lists have been around since Windows 7; I'd published several [articles on Jump Lists](https://windowsir.blogspot.com/2011/08/jump-list-analysis.html) going back almost 14 years at this point. Jump Lists are valuable to analysts because they're (a) created as a result of user interaction via the Windows Explorer shell, (b) evidence of program execution, and (c) evidence of data or file access.

Automatic Jump Lists follow the old Windows OLE "structured storage" format. Microsoft refers to this as the "[compound file binary](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-cfb/50708a61-81d9-49c8-ab9c-43c98a795242)" format and has thoroughly documented the format structures. Some folks who've been around the industry for a while will remember that the OLE format is what Office documents used to use, and that there was a good bit of metadata associated with these documents. In fact, a good way to find the old school "OG" analysts still hanging around the industry is to mention [the Blair document](https://dfir.com.br/wp-content/uploads/2014/02/blair.htm). And the format didn't disappear when Office was updated to the newer style format; rather, the format is used an other areas, such as Jump Lists, and at one point was used for Sticky Notes.

[Here's my code](https://github.com/keydet89/Tools/blob/master/source/JumpList.pm) for parsing the "structured storage" format; this was specifically developed for Windows 7 Automatic Jump Lists, but the basic code can be repurposed for OLE files, in general, or specifically updated for specific field (i.e., the DestList stream) in newer versions of Windows.

As you saw in Brian's article, Automatic Jump Lists are specific to each user, and are found within the user's profile path. Each Automatic Jump List is named using an "application identifier" or "AppID". This is a value that identifies the application used to open the target files (Notepad, Notepad++, MSWord, etc.), and is consistent across platforms. This means that an AppID that refers to a particular application on a Windows system will remain the same on other Windows systems.

Microsoft has referred to the "structured storage" format as a "file system within a file"; if you do a study of the format, you'll see why. This structure results in various 'streams' being within the file, and for Automatic Jump Lists, there two types of streams. Most of the streams in a Automatic Jump List file contain a stream structure that follows the Windows shortcut/LNK file format.

The other type of stream is referred to as the "DestList" stream, and the structure of this stream on Windows 7 systems [was first documented](https://windowsir.blogspot.com/2011/06/meetup-tools-and-other-stuff.html) about 14 yrs ago. The following figure illustrates an Automatic Jump List opened in the [Structured Storage Viewer](https://www.mitec.cz/ssv.html), with the DestList stream highlighted.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhj89418Mq9JgSfsexQcfxMSaW7NQX7ZBk4cmrST1AhhjnugUn1hn0FR5ZY9hi9g4FVT8tFU8wuHgd7ZxvSKTCl5BXuxx5avTorUGuDj1AdKff6aTSZ8TlhsDOdmWuMGNe2DJ2Jr6XLiPl7m1d_7EBthl4N3vLfqjQidTu2zNxvB8f0HkEcGg/w400-h235/destlist.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhj89418Mq9JgSfsexQcfxMSaW7NQX7ZBk4cmrST1AhhjnugUn1hn0FR5ZY9hi9g4FVT8tFU8wuHgd7ZxvSKTCl5BXuxx5avTorUGuDj1AdKff6aTSZ8TlhsDOdmWuMGNe2DJ2Jr6XLiPl7m1d_7EBthl4N3vLfqjQidTu2zNxvB8f0HkEcGg/s1031/destlist.png)

The structure of the DestList stream changed slightly between Windows 7 and 10 (and maybe again with Windows 11, I haven't looked yet...), but the overall structure of the Automatic Jump List files remains essentially the same.

*Summary*
Automatic Jump Lists help analysts validate that a user was active on the system via the Windows shell (as well as when), that they launched applications (program execution), and that they used those applications to open files (file/data access), and when they did so. As such, parsing Jump Lists and including the data in a timeline can add a good deal of granularity and context to the timeline, particularly as it pertains to user activity.

As always, Automatic Jump Lists should be used in conjunction with other artifacts, such as Prefetch, UserAssist, RecentDocs, etc., and should not be viewed in isolation, pursuant to the analyst's investigative goals.

Something else to remember is this...Automatic Jump Lists are generated by the operating system as the user interacts with the environment. As such, if an application is added, the user uses that application and Automatic Jump Lists are generated, and then the user removes the application, the Automatic Jump Lists remain. The same thing happens with other artifacts, such as Recents shortcuts/LNK files, Registry values, etc. So, as with other artifacts, Automatic Jump Lists can provide indications of applications previously installed or files that previously existed on (or were accessed from) the endpoint.

Posted by
H. Carvey

at
[1:58 PM](http://windowsir.blogspot.com/2025/01/artifacts-jump-lists.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/9518042/1832896506554320601 "Email Post")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=9518042&postID=1832896506554320601&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=9518042&postID=1832896506554320601&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=9518042&postID=1832896506554320601&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=9518042&postID=1832896506554320601&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=9518042&postID=1832896506554320601&target=facebook "Share to Facebook")[Share to Pinter...