---
title: Analysis Process
url: http://windowsir.blogspot.com/2024/10/analysis-process.html
source: Instapaper: Unread
date: 2024-10-18
fetch_date: 2025-10-06T18:56:27.423610
---

# Analysis Process

# [Windows Incident Response](http://windowsir.blogspot.com/)

The Windows Incident Response Blog is dedicated to the myriad information surrounding and inherent to the topics of IR and digital analysis of Windows systems. This blog provides information in support of my books; "Windows Forensic Analysis" (1st thru 4th editions), "Windows Registry Forensics",
as well as the book I co-authored with Cory Altheide, "Digital Forensics with Open Source Tools".

## Tuesday, October 15, 2024

### Analysis Process

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZyNXlGmn8X6LQ2JxfiSPmNTGojInmoLdNXi8eWEujEpiP9mBjiVrUUG21krCXFDg6zQJJiB3r3ahbo-qudvdi3GRrDnrHtct_P63vV5ioHUxp_ay_6gmNxQTCPG1_wDgkjRUeCGpXYjmVpJ6ylZRsxGjmaepc-maHlf5pqRThJUVWFmcrWw/s320/iws.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZyNXlGmn8X6LQ2JxfiSPmNTGojInmoLdNXi8eWEujEpiP9mBjiVrUUG21krCXFDg6zQJJiB3r3ahbo-qudvdi3GRrDnrHtct_P63vV5ioHUxp_ay_6gmNxQTCPG1_wDgkjRUeCGpXYjmVpJ6ylZRsxGjmaepc-maHlf5pqRThJUVWFmcrWw/s439/iws.png)

Now and again, someone will ask me, "...how do you do analysis?" or perhaps more specifically, "...how do you use RegRipper?"

This is a tough question to answer, but not because I don't have an answer. I've already published a book on that very topic, and it seems that my process for *doing analysis* is apparently very different from the way most people do analysis.

Now, I can't speak to how everyone else goes about analyzing an endpoint, but when I share my process, it seems that that's the end of the conversation.

My analysis process, laid out in books like "[Investigating Windows Systems](https://www.amazon.com/Investigating-Windows-Systems-Harlan-Carvey/dp/0128114150/)", is, essentially:

**1. Document investigative goals.** These become the basis for everything you do in the investigation, including the report.

Always start with the goals, and always start documentation by having those goals right there at the top of your case notes file. When I was active in DFIR consulting, I'd copy the investigative goals into the Executive Summary of the report, and provide 1-for-1 answers. So, three goals, three answers. After all, the Executive Summary is a summary for executives, meant to stand on it's own.

**2. Collect data sources.**

This one is pretty self-explanatory, and very often based on your response process (i.e., full images vs "triage" data collections). Very often, collection processes will include the least amount of data extracted from a system for the biggest impact, based upon the predominance of business needs, leaving other specific sources for later/follow-on collection, if needed.

**3. Parse, normalize, decorate, enrich those data sources.**

Basically, create a timeline, from as many data sources as I can or makes sense, based on my investigative goals. Easy-peasy.

Timelines are not something left to the end of the investigation, to be assembled manually into a spreadsheet. Rather, creating a timeline as a means of initiating an investigation provides for much needed context.

**4. Identify relevant pivot points.**

[RegRipper](https://github.com/keydet89/RegRipper4.0) and [Events Ripper](https://github.com/keydet89/Events-Ripper) are great tools for this step. Why is that? Well, within the Registry, often items of interest are encoded in some manner, such as binary, hex, ROT-13, or some folder or other resource represented by a GUID; many of the RegRipper plugins extract and display that info in human-readable/-searchable format. So, running RegRipper TLN plugins to incorporate the data into a timeline, and then run "regular output" plugins to develop pivot points.
Events Ripper is great for extracting items of interest from events files with (hundreds of) thousands of lines.

**5. Identify gaps, if any, and loop back to #2.**

Based on the investigative goals, what's missing? What else do you need to look for, or at? You may already have the data source, such as if you need to look for deleted content in Registry hives,

**6. Complete when goals are met, which includes being validated.**

An issue we face within the industry, and not just in DFIR, is validation. If a SOC analyst sees a "net user /add" command in EDR telemetry, do they report that a "user account was created" without (a) checking the audit configuration of Security Event Log, and (b) looking for Security-Auditing event records that demonstrate that a user account was created? If it was a local account, is the SAM checked?

Or, if msiexec.exe is seen (via EDR telemetry) running against an HTTP/HTTPS resource, is the Application Event Log checked for MsiInstaller events?

My point is, are we just *saying* that something happened, or are we validating via the available data sources that it actually happened?

**7. Anything "new" gets baked back in**

The great thing about timelines and other tools is that very often, you'll find something new, something you hadn't seen before, and was relevant (or could be) to your investigation. This is where most of the Events Ripper plugins have originated; I'll see something "new", often based on an update to Windows, or some installed application, and I'll "bake it back into" the process by creating a plugin.

Yes, documenting it is a good first step, but adding it back into your automation is taking action. Also, this way, I don't have to remember to look for it...it's already there.

For example, several years ago, another analyst mentioned seeing something "new" during a response; looking into it, this new thing was a [Microsoft-Windows-TaskScheduler/706](https://technet.microsoft.com/en-us/library/cc774959%28v%3Dws.10%29.aspx) event record, so once I got a little more info about it, and dug into the investigation myself just a bit, I added it to [eventmap.txt](https://github.com/keydet89/Tools/blob/master/exe/eventmap.txt). After that, I never had to remember to look for it, and I had the necessary references to support the finding already documented.

Posted by
H. Carvey

at
[1:08 PM](http://windowsir.blogspot.com/2024/10/analysis-process.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/9518042/8748808457670866474 "Email Post")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=9518042&postID=8748808457670866474&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=9518042&postID=8748808457670866474&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=9518042&postID=8748808457670866474&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=9518042&postID=8748808457670866474&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=9518042&postID=8748808457670866474&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=9518042&postID=8748808457670866474&target=pinterest "Share to Pinterest")

#### No comments:

[Post a Comment](https://www.blogger.com/comment/fullpage/post/9518042/8748808457670866474)

[Newer Post](http://windowsir.blogspot.com/2024/10/artifact-tracking-workstation-names.html "Newer Post")

[Older Post](http://windowsir.blogspot.com/2024/10/rundown.html "Older Post")
[Home](http://windowsir.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](http://windowsir.blogspot.com/feeds/8748808457670866474/comments/default)

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

[![](https://resources.blogblog.com/img/widgets/subsc...