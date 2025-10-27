---
title: Smuggling payloads and tools in, using WIM images
url: https://www.hexacorn.com/blog/2024/12/31/smuggling-payloads-and-tools-in-using-wim-images/
source: Hexacorn
date: 2025-01-01
fetch_date: 2025-10-06T20:06:47.683132
---

# Smuggling payloads and tools in, using WIM images

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

[← Previous](https://www.hexacorn.com/blog/2024/12/28/wimmountdata-ads/)
[Next →](https://www.hexacorn.com/blog/2024/12/31/clean-hash-set-12m-rows/)

# Smuggling payloads and tools in, using WIM images

Posted on [2024-12-31](https://www.hexacorn.com/blog/2024/12/31/smuggling-payloads-and-tools-in-using-wim-images/ "12:20 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

We often hear of attackers bringing in their payloads via virtual drive images (f.ex. vhd,vhdx) in an attempt to bypass security solutions. The WIM files can be used to smuggle in tools and payloads to the target, too. In my [previous post](https://www.hexacorn.com/blog/2024/12/28/wimmountdata-ads/) I discussed the $WIMMOUNTDATA Alternate Data Stream that is created by *dism.exe* when we use it to mount a WIM image.

Now, the way the WIM images are mounted is interesting for many reasons:

* they are mounted read-only, so once mounted, can’t delete files they provide access to
* the files they expose to the OS are not ‘created’ in any telemetry sense, so there are no ‘File Created’ events for them – it’s just a file system tunnel
* they are tiny, and can even be easily encrypted/decrypted using available lolbin tools, or powershell
* the .wim files themselves, once mounted, can’t be deleted
* interestingly, when you create .WIM files from sources that include *Zone.Identifier* ADS (typically after downloading the files from the internet), these ADS will make it to the WIM image as well; so, have to be mindful of it

Here’s an example [mimikatz.wim](https://hexacorn.com/d/mimikatz.zip) (pass: mimi) WIM image (it actually has a decent detection rate on [VT](https://www.virustotal.com/gui/file/99c786b6626ed0eb9d31ea8d140edc8ec03abadc54fd934b148d903d9bf1f7f7)). Its file list indicates it was created from a directory that included old mimikatz files downloaded directly from github (hence, ADS are present):

```
mimidrv.sys
mimidrv.sys:Zone.Identifier
mimikatz.exe
mimikatz.exe:Zone.Identifier
mimilib.dll
mimilib.dll:Zone.Identifier
mimispool.dll
mimispool.dll:Zone.Identifier
```

The 7z listing of the archive looks as follows:

```
Listing archive: mimikatz.wim

--
Path = mimikatz.wim
Type = wim
Physical Size = 704059
Size = 1440688
Packed Size = 702019
Method = XPress:15
Cluster Size = 32768
Created = 2024-12-30 22:11:48.7166057
Modified = 2024-12-30 22:11:48.7385760
Comment = <WIM><TOTALBYTES>703241</TOTALBYTES><IMAGE INDEX="1"><DIRCOUNT>0</DIRCOUNT><FILECOUNT>4</FILECOUNT><TOTALBYTES>1440600</TOTALBYTES><HARDLINKBYTES>0</HARDLINKBYTES><CREATIONTIME><HIGHPART>0x01DB5B07</HIGHPART><LOWPART>0xD2354269</LOWPART></CREATIONTIME><LASTMODIFICATIONTIME><HIGHPART>0x01DB5B07</HIGHPART><LOWPART>0xD2389CA0</LOWPART></LASTMODIFICATIONTIME><WIMBOOT>0</WIMBOOT><NAME>mimi</NAME></IMAGE></WIM>
Version = 1.13
Multivolume = -
Volume = 1
Volumes = 1
Images = 1

   Date      Time    Attr         Size   Compressed  Name
------------------- ----- ------------ ------------  ------------------------
2013-01-22 16:50:12 ....A        37208        17078  mimidrv.sys
2022-09-19 15:44:01 ....A        37376        19303  mimilib.dll
2022-09-19 15:43:57 ....A        10752         4973  mimispool.dll
2022-09-19 15:44:39 ....A      1355264       660577  mimikatz.exe
------------------- ----- ------------ ------------  ------------------------
2022-09-19 15:44:39            1440600       701931  4 files
2022-09-19 15:44:39                352          352  4 alternate streams
2022-09-19 15:44:39            1440952       702283  8 streams
```

There are plenty of forensic artefacts present in that file, including the *Comment* field that 7z extracts:

```
<WIM>
 <TOTALBYTES>703241</TOTALBYTES>
 <IMAGE INDEX="1">
  <DIRCOUNT>0</DIRCOUNT>
  <FILECOUNT>4</FILECOUNT>
  <TOTALBYTES>1440600</TOTALBYTES>
  <HARDLINKBYTES>0</HARDLINKBYTES>
  <CREATIONTIME>
   <HIGHPART>0x01DB5B07</HIGHPART>
   <LOWPART>0xD2354269</LOWPART>
  </CREATIONTIME>
  <LASTMODIFICATIONTIME>
   <HIGHPART>0x01DB5B07</HIGHPART>
   <LOWPART>0xD2389CA0</LOWPART>
  </LASTMODIFICATIONTIME>
  <WIMBOOT>0</WIMBOOT>
  <NAME>mimi</NAME>
 </IMAGE>
</WIM>
```

Combining the knowledge from this and previous post, one can start wondering…

If we mount an innocent WIM image first, one that lists only good (or at the very least – dummy) files, and then, we export the mounted directory’s $WIMMOUNTDATA ADS, modify it to point to a different WIM file, the bad one, then we write it back to the directory’s ADS… what will the system see/do?

Turns out, that modifying the ADS alone is NOT ENOUGH to fool the OS to ‘redirect’ the tunnel to a different image 🙁

Looking for other angles, we can search the Registry and we can discover that this whole WIM mounting business is nicely documented here:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/WIMMOUNTDATA_3.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/WIMMOUNTDATA_3.png)

under the following key:

```
HKLM\SOFTWARE\Microsoft\WIMMount\Mounted Images\
```

So, what about we change the *WIM Path* value to point to the *bad*  WIM image, and restart the system?

Nothing.

The ‘mounted’ directory will still list the files from the original ‘neutral’ WIM image only.

Okay, so it’s time we explore the actual $MFT of the C: drive where we mounted our WIM image to. To our surprise, the $MFT does include FILE records for every single file from our neutral WIM image!

Oops. Our original assumption that there are no ‘File Create’ events in our telemetry was wrong!

Literally, the *dism.exe* is reading the WIM image file and then it is recreating its codified directory structure by writing it to a destination folder, recursively; and for each directory or file, or even ADS, it is triggering the “File Create” events:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/dism_subdirs.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/dism_subdirs.png)

And there is one more wrong assumption we need to address:

* the WIM images are mounted as read-only

The *dism.exe* program tells us it is not true when we try to remount the WIM image that is already mounted:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/dism_rw.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/dism_rw.png)

Exploring the mounted directories, you can easily delete files and directories.

Oops.

At this stage, you probably realize that this post is written from a perspective of an unreliable narrator…

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [Forensic Analysis](https://www.hexacorn.com/blog/category/forensic-analysis/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/12/31/smuggling-payloads-and-tools-in-using-wim-images/ "Permalink to Smuggling payloads and tools in, using WIM images").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")