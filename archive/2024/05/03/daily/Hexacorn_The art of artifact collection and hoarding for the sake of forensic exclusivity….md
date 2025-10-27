---
title: The art of artifact collection and hoarding for the sake of forensic exclusivity…
url: https://www.hexacorn.com/blog/2024/05/02/the-art-of-artifact-collection-and-hoarding-for-the-sake-of-forensic-exclusivity/
source: Hexacorn
date: 2024-05-03
fetch_date: 2025-10-06T17:15:05.864111
---

# The art of artifact collection and hoarding for the sake of forensic exclusivity…

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

[← Previous](https://www.hexacorn.com/blog/2024/04/26/a-license-metadata-to-kill-for/)
[Next →](https://www.hexacorn.com/blog/2024/05/03/the-art-of-artifact-collection-and-hoarding-for-the-sake-of-forensic-exclusivity-part-2/)

# The art of artifact collection and hoarding for the sake of forensic exclusivity…

Posted on [2024-05-02](https://www.hexacorn.com/blog/2024/05/02/the-art-of-artifact-collection-and-hoarding-for-the-sake-of-forensic-exclusivity/ "12:18 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

This post is going to blow your mind – I am going to demonstrate that the piracy is good! (sometimes)

I like to challenge the forensic processes *du jour*. At least in my head.

Today we often use *this* forensic suite/tool, or *that* forensic script (or their set) to read and process the forensic evidence in its native form: NTFS, extX, APFS file systems, OS folders and files of interest, Event Logs, Memory Dumps, Cloud logs, Server logs, any other available Telemetry, etc. and then we do some spelunking, bookmarking, filtering, and of course we do a surgical artifact of interest identification, parsing, normalization and cross-referencing, and finally supertimelining it all in no time. In many cases… the available, well tested, generic forensic data processing and automation processes are doing so well, and doing such a phenomenal work, and yes, we have progressed so much, and on so many fronts over last decade, that the actual act of old school forensic process is getting kinda lost today… BUT the good news is that we close cases faster than ever…

One may ask: is there still any reason out there to think of better forensic methods to analyze data today?

YES!

While many ‘cyber’ cases are truly benefiting from these fast, targeted, surgical, and automated artifact analysis and processing pipelines… we still have many cases where the forensic exam must be done in the ‘beyond a reasonable doubt’ way. In my first forensic job I was primarily working non-LE cases but sometimes was supporting the team that was analyzing CSAM and other criminal content. I must say that their attention to detail shaped my professional life in many positive ways. But at that time I had a lot of questions: f.ex. I was very perplexed that they were insisting on a very mundane, one-by-one, manual analysis of all media files on the devices they were examining. In my eyes, they were wasting a lot of time (many of the pictures were just small icons, many shipped by default as a part of OS), and should have been optimizing this process… Only later the reason for their approach became more apparent to me: any miss on their side would mean a compromise of their forensic expert profile and integrity that the other side (in court) could exploit.

Hmm but I still think browsing all these tiny, built-in media files was a waste of time…

In some other job I did, I worked closely with the DFIR team that did a lot of e-discovery work. Again, I was perplexed that they were spending hours browsing through peoples’ mailboxes looking for any sign of ‘bad’. Very, very boring and poor ROI. BUT IT HAD TO BE DONE RIGHT.

It’s safe to say that every forensic exam has its own objectives. And because of this, while many of these objectives appear to be achievable only via a brute-force approach, I do believe there are still many research avenues out there that – if successful – could benefit these forensic processes and in the end make these objectives faster to achieve – both in general, and more specific, targeted cases.

A good example is my (sorry for an ego trip) [filighting](https://www.hexacorn.com/blog/2015/04/11/introducing-filighting-and-the-future-of-dfir-tools-part-3-more-examples/) idea that can be used to reduce the amount of evidence we need to process… and it’s thanks to a simple observation: a legitimate software will consist of files and resources that are being referenced from the inside of the software itself.

We can also entertain more ‘horizontal’ data reduction techniques like the idea of targeting specific, function-specific files f.ex. [license files](https://www.hexacorn.com/blog/2024/04/26/a-license-metadata-to-kill-for/). But there is more…

If we look at a random instance of a Windows system, we can observe a number of patterns:

* Windows OS files — often protected from deletion and signed (nowadays often via catalogue signing), includes lots of subfolders — many of which have been exploited by threat actors
* Program Files — existing in many localized versions, and many architecture-specific versions mostly contain files belonging to legitimate software packages (and sometimes supply-chain attack files too, though)
* Common Files — as above, for many software packages
* TMP/TEMP folders — both c:\windows\temp and user-specific temporary folders
* USERPROFILE folder — a lot is going on here, definitely a subject to further analysis
* ProgramData folder — as above, lots is going here
* Dedicated Dev folders — where devs develop and test their code
* Portable Apps — usually stored in dedicated, separated folders
* Local or Legacy apps — often saved in c:\<appfolder>\ directories
* Shared folders — often just a wrong configuration problem
* etc.

When you look at the file system-based evidence from the perspective of file clusters it may become apparent that many of these ‘default’ directories start their existence with a very predetermined, baseline-like list of files inside them.

For instance:

* c:\windows\notepad.exe
* c:\windows\System32\kernel32.dll
* c:\windows\System32\KernelBase.dll
* c:\windows\SysWow64\kernel32.dll
* c:\windows\SysWow64\KernelBase.dll
* and hundreds, if not thousands of other file names like this

These are HARD to modify today.

Imagine getting a Windows OS-based image as an evidence. You first exclude all files that have the hash matching your ‘clean hash’ list, then you exclude all files that are 100% OS files (based on their paths AND/OR signatures, including catalogue signing), then you exclude all that have the corresponding symbol file on Microsoft symbol servers (but be mindful of SigFlip attack), then you exclude clusters of files that are installed as a part of dedicated program installation event, then you exclude filighted files, then you exclude all media files that are size 100×100 or less, then you go a bit higher level and exclude less-recognizable clusters of software\*, then you exclude… yes, you name it. With a lot of ideas like these we can beat down an ‘attack surface’ for manual analysis to a substantially smaller subset of evidence!

\*And it’s time to prove that piracy is good (sometimes).

Many paid software packages are heavily guarded and can’t be accessed/downloaded without paying a licensee fee. Now, pirated files don’t have these restrictions and one could download them temporarily, look at their folder structures and file lists (even extract hashes of each file), and if the archive includes a parseable installer or archive – extract and analyze their content, preserve their file listing for the future, and continue adding them to a ‘known file’ database (both by hash and absolute/relative path and or file name/file size). With a large number of such clustered filelists one could potentially remove a lot of noise from the examined evidence.

If you are worried about piracy, it was just a clickbait. You can find many of the very same files available for download on many popular ‘upload your file and we will tell you if it is bad’ legitimate sites…

Now, ...