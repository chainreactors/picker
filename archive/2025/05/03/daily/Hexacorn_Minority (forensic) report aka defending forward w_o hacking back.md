---
title: Minority (forensic) report aka defending forward w/o hacking back
url: https://www.hexacorn.com/blog/2025/05/02/minority-forensic-report-aka-defending-forward-w-o-hacking-back/
source: Hexacorn
date: 2025-05-03
fetch_date: 2025-10-06T22:26:52.161671
---

# Minority (forensic) report aka defending forward w/o hacking back

[Skip to primary content](#content)

# [Hexacorn](https://www.hexacorn.com/blog/)

## Hexacorn

Search

### Main menu

* [Home](https://www.hexacorn.com/)
* [Services](https://www.hexacorn.com/services.html)
* [Products & Freebies](https://www.hexacorn.com/products_and_freebies.html)
* [Case Studies](https://www.hexacorn.com/case_studies.html)
* [Contact Us](https://www.hexacorn.com/contact.html)

### Post navigation

[← Previous](https://www.hexacorn.com/blog/2025/03/30/malware-source-code-string-extraction/)
[Next →](https://www.hexacorn.com/blog/2025/05/18/shell32-dll-44-lolbin/)

# Minority (forensic) report aka defending forward w/o hacking back

Posted on [2025-05-02](https://www.hexacorn.com/blog/2025/05/02/minority-forensic-report-aka-defending-forward-w-o-hacking-back/ "11:28 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

We love to put a wedge between the detection and response. Many of us kinda agree that telemetry analysis is one thing and the actual forensic examination of the evidence is another.

However…

In this post I will try to turn the tables a bit.

**Prefetch files**

All the command line tricks you use to execute your executable, script, load your library, etc. will end up with Prefetch entries created on the victim system.

Look at clusters of Prefetch files created within small time intervals and you will find interesting sets of prefetch file clusters related to a bundle of programs executed one after another – to pivot from.

**Most Recently Used**

[This](https://www.magnetforensics.com/blog/what-is-mru-most-recently-used/) Magnet Forensics article describes a number of forensic artifacts related to Most Recently Used files/commands and RecentDocs that we can track with telemetry.

By careful examination of these, we can detect a lot of user-driven activity that can give us hints about what is happening on a system as a result of user activities, and ignore all the telemetry noise coming from OS and legitimate software activity.

**Jump List App ID analysis**

Again, instead of concentrating on the input (obfuscated command lines leading to execution of many lolbins, executables, often nested), we focus on analysis of files with the following extensions:

* .`automaticDestinations-ms`
* `.customDestinations-ms`

We can use exclusions like this [list](https://www.4n6k.com/2016/03/jump-list-forensics-appid-master-list.html). We can also use techniques like Least Frequency Occurrence (LFO) to focus on outliers. We can pivot from them and see what happens on the investigated system prior to these artifacts being created.

**Application crashes**

Telemetry can tell us about a lot of interesting events. One of them is an application crash.

Anytime we see an invocation of `werfault.exe`, or creation of a `.dmp` file, we should look at the events preceding this event.

**Persistence**

I wrote [a lot](https://www.google.com/search?q=site%3Ahexacorn.com+beyond) about this topic and it still stands true. Collect telemetry related to these generic load points and you will find some ‘bad’ in no time.

**Quarantine files**

My old tool [DeXRAY](http://www.hexacorn.com/blog/category/software-releases/dexray/) is still being used in 2025. I am quite shocked, but also pleased. What it means in practice though is that:

* companies still use antivirus software
* some companies still use more than 1 endpoint security control per endpoint
* detection of a quarantine file being created is a good pivot point for some additional digging

**Lnk files**

Surprisingly, they are not created that often, so they are an interesting artifact to look at.

They may point to an insider threat, they may point to a malware, or make us waste some triage time leading us to nowhere (list of exclusions should be easy to build though: ‘`What's New.lnk'`, ‘`About <program>.lnk`‘, ‘`Uninstall <program>.lnk`‘, ‘`Magnify.lnk`‘, ‘`Narrator.lnk`‘, etc.).

**Background Activity Moderator (BAM)**

This is an obvious candidate for monitoring as it references the user’s SID and can tell us who actually executed that particular program.

Monitoring the entries in this Registry branch can help us to detect anomalies when we start seeing execution of unusual processes.

**Unusual File Creation activity**

In many posts in the past I have highlighted a lot of DLL side-loading techniques that are quite unusual f.ex.:

* [phantom DLLs](https://www.google.com/search?q=site%3Ahexacorn.com+phantom+DLL)
* [Visual Basic localisation DLLs](https://www.hexacorn.com/blog/2015/01/01/beyond-good-ol-run-key-part-20/)
* [MFC localisation DLLs](https://www.hexacorn.com/blog/2015/01/03/beyond-good-ol-run-key-part-21/)
* [statically linked MFC code linking to localisation DLLs](https://www.hexacorn.com/blog/2015/01/28/beyond-good-ol-run-key-part-26/)
* [Delphi localisation DLLs](https://www.hexacorn.com/blog/2015/01/28/beyond-good-ol-run-key-part-25/)

Detecting file operations associated with these unusual side-loading activities is a good way to detect more advanced attackers (and yes, many of them are actively using some of my techniques!).

There are probably more forensic artifacts that we can monitor for some early detections, but the set above should give you some pointers…

This entry was posted in [Forensic Analysis](https://www.hexacorn.com/blog/category/forensic-analysis/), [Threat Hunting](https://www.hexacorn.com/blog/category/threat-hunting/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/05/02/minority-forensic-report-aka-defending-forward-w-o-hacking-back/ "Permalink to Minority (forensic) report aka defending forward w/o hacking back").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")