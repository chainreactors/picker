---
title: Carving
url: http://windowsir.blogspot.com/2025/01/carving.html
source: Instapaper: Unread
date: 2025-01-08
fetch_date: 2025-10-06T20:26:48.129225
---

# Carving

# [Windows Incident Response](http://windowsir.blogspot.com/)

The Windows Incident Response Blog is dedicated to the myriad information surrounding and inherent to the topics of IR and digital analysis of Windows systems. This blog provides information in support of my books; "Windows Forensic Analysis" (1st thru 4th editions), "Windows Registry Forensics",
as well as the book I co-authored with Cory Altheide, "Digital Forensics with Open Source Tools".

## Monday, January 06, 2025

### Carving

Recovering deleted data, or "carving", is an interesting digital forensics topic; I say "interesting" because there are a number of different approaches and techniques that may be valuable, depending upon your goals.

For example, I've used X-Ways to recover deleted archives from the unallocated space of a web server. A threat actor had moved encrypted archives to the web server, and we'd captured the password they used via EDR telemetry. The carving revealed about a dozen archives, which we opened using the captured password, which allowed our customer to understand what data had been exfil'd, and their risk and exposure.

But carving can be about more than just recovering files from unallocated space. We can carve files and records from unstructured data, or we can treat 'structured' data as unstructured and attempt to recover records. We did this quite a bit during PCI forensic investigations, and found a much higher level of accuracy/fidelity when we carved for track 1 and 2 data, rather than just credit card numbers.

We can also carve within files themselves. Several common file formats are essentially databases, and some are described as a "file system within a file". As such, deleted records and data can be recovered from such file formats, if necessary.

I recently ran across a fascinating [post from TheDFIRJournal](https://thedfirjournal.com/posts/file-carving-encrypted-virtual-disks/) recently, regarding file carving encrypted virtual disks. The premise of the post is that some file encryption/ransomware software does not encrypt entire files, just rather just part of it, for the sake of speed. In the case of virtual disks, a partially encrypted file may mean that, while the disk itself is useable, there may be valuable evidence available within the virtual disk file itself.

I should note that I did recently see a ransomware deployment that used a "--mode fast" switch at the command line, possibly indicating that the *entire* file would not be encrypted, but rather only a specific number of bytes of the file. As such, with larger files, such as virtual disks, WEVT files, etc., there might be an opportunity to recover valuable data, so file and record carving techniques would be valuable, depending upon your specific investigative goals.

The premise raised in the article is not unique; in fact, I've run into it before. In 2017, when [NotPetya](https://www.crowdstrike.com/en-us/blog/petrwrap-technical-analysis-part-2-further-findings-and-potential-for-mbr-recovery/) hit, we received a number of system images from customers where the MBR was overwritten. We had someone on our team who could reconstruct the MBR, and we also ran carving for WEVTX records, recovering Security-Auditing/4688 records indicating process creation. The customers had not enabled full command lines being recorded, but we were able to reconstruct enough data to illustrate the sequence of processes specific to the infection and impact. So, having a disk image where the MBR and/or the MFT is overwritten is not a new situation, simply one we haven't encountered recently.

[TheDFIRJournal article](https://thedfirjournal.com/posts/file-carving-encrypted-virtual-disks/) covers a number of tools, including [PhotoRec](https://www.cgsecurity.org/wiki/PhotoRec), [scalpel](https://github.com/sleuthkit/scalpel) (not currently being maintained), and [Willi Ballenthin's EVTXtract](https://github.com/williballenthin/EVTXtract). The article also covers Simson Garfinkel's bulk\_extractor, but looking at the bulk\_extractor Github, there do [not appear to be releases for Windows](https://github.com/simsong/bulk_extractor?tab=readme-ov-file#bulk_extractor-20-release-notes) starting with version 2.0. While some folks have stated that [bulk\_extractor-rec](https://github.com/4n6ist/bulk_extractor-rec)'s capabilities have been added to bulk\_extractor, that's kind of a moot point, and the [latest release of bulk\_extractor-rec](https://github.com/4n6ist/bulk_extractor-rec/releases/tag/rec03) will have to suffice.

***Addendum, 7 Jan 2025***: Thanks to [Brian Maloney](https://www.linkedin.com/in/viralcomputers/) for sharing that the bulk\_extractor 2.0 for Windows CLI tool [can be found here](https://github.com/simsong/bulk_extractor/wiki/Installing-bulk_extractor).

Also from the article, the author mentioned the use of a customer EVTXParser script, which [can be found here](https://github.com/TheDFIRJournal/EVTXCarver/blob/main/evtx-carver.py). I like this approach, as I'd done something similar with the WinXP/2003 EVT files, where I'd [written lfle.pl](https://github.com/keydet89/Tools/blob/master/source/lfle.pl) to parse EVT records from unstructured data, which could include a .EVT file. I wrote this script (a 'compiled' Windows EXE is also available) after finding two complete records embedded in an .EVT file that were not "visible" via the Event Viewer, nor any other tools that started off by reading the file header to determine where the records were located. The script then evolved into something you could run against any data source. While not the fastest tool, at the time it was the only tool available that would take this approach.

In the past, I've done carving on unallocated space within a disk image, using something like [blkls](https://www.sleuthkit.org/sleuthkit/man/blkls.html) to get the uallocated space into on contiguous file of unstructured data. From there, running tools like bulk\_extractor allow for record carving.

I've also has pretty good success running bulk\_extractor across memory dumps; this is something I talked about/walked through in my book, *[Investigating Windows Systems](https://www.amazon.com/Investigating-Windows-Systems-Harlan-Carvey/dp/0128114150)*.

Carving can also be done on individual files. For example, in 2013, Mari DeGrazia published a great [blog post on recovering deleted data from SQLite databases](https://az4n6.blogspot.com/2013/11/python-parser-to-recover-deleted-sqlite.html), and carving Registry hive files for deleted keys and values, as well as examining unallocated space within hive files is something I've been a fan of for quite some time. My thanks go to Jolanta Thomassen for 'cracking the code' on deleted cells within Registry hive files!

[Here's a presentation](https://www.dfir.training/writings/registry/732-secrets-of-registry-analysis/file) I put together a while back that includes information regarding unallocated space within Registry hive files.

***Addendum, 13 Jan***: Damien Attoe [released his first blog post](https://digital4n6withdamien.blogspot.com/2025/01/introducing-sqbite-alpha-python-tool.html) regarding a tool he's working on called "sqbite"; the alpha functionality is what's currently available, and Damien plans to release additional functionality in March. Reading through his blog post, it appears that Damien is working toward something similar to what [Mari talked about and released](https://az4n6.blogspot.com/2013/11/python-parser-to-recover-deleted-sqlite.html). It's going to be interesting to see what he develops!

Posted by
H. Carvey

at
[2:18 PM](http://windowsir.blogspot.com/2025/01/carving.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/9518042/3046661434988119254 "Email Post")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=9518042&postID=3046661434988119254&from=pencil "Edit Pos...