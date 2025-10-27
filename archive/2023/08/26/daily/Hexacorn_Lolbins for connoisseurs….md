---
title: Lolbins for connoisseurs…
url: https://www.hexacorn.com/blog/2023/08/25/lolbins-for-connoisseurs/
source: Hexacorn
date: 2023-08-26
fetch_date: 2025-10-04T11:59:39.671547
---

# Lolbins for connoisseurs…

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

[← Previous](https://www.hexacorn.com/blog/2023/07/14/how-to-start-your-own-threat-intel-company/)
[Next →](https://www.hexacorn.com/blog/2023/08/26/writing-better-yara-rules-in-2023/)

# Lolbins for connoisseurs…

Posted on [2023-08-25](https://www.hexacorn.com/blog/2023/08/25/lolbins-for-connoisseurs/ "11:05 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

We are all quite fixated on a purity of lolbins. Best if it is a hidden/undocumented/unexpected behavior of a native OS binary that can be abused for some nefarious purposes. I, obviously, love these the most, too.

However…

Living Off The land’s scope should be wide.

Take a compression utility as an example: zip, bzip2, 7z and their variations. It’s a lame example, but it serves the purpose of demonstration well. There are many software packages out there today. There is a subset of them that are being quite popular. And there is a subset of software packages that are quite popular that install a compression utility…

Let’s have a look at a sample of ‘interesting’ paths:

* %program files%\2printer\7z.exe
* %program files%\advanced system optimizer 3\updater\extract\7z.exe
* %program files%\aiseesoft studio\aiseesoft ipad transfer\7z.exe
* %program files%\aunsoft\aunsoft dvd ripper\zip.exe
* %program files%\aunsoft\aunsoft transmxf\zip.exe
* %program files%\aunsoft\aunsoft video converter\zip.exe
* %program files%\auntec\ifonebox\7z.exe
* %program files%\docufreezer\7z.exe
* %program files%\driver tuneup\dp\7z.exe
* %program files%\driver updater\dp\7z.exe
* %program files%\dvdfab media player 3\7za.exe
* %program files%\dvdfab passkey\7za.exe
* %program files%\epson\sl-d700\common\7za.exe
* %program files%\fastneuron inc\backupchain\7za.exe
* %program files%\fengtao software inc.\ifonerestore\7z.exe
* %program files%\filetiger\zip.exe
* %program files%\getnzb\7z.exe
* %program files%\gimp\*\bin\bzip2.exe
* %program files%\gimp\*\bin\minigzip.exe
* %program files%\git\usr\bin\bzip2.exe
* %program files%\git\usr\bin\gzip.exe
* %program files%\git\mingw64\bin\bzip2.exe
* %program files%\globalshareware\ifonemate\7z.exe
* %program files%\greatis\regrunsuite\7za.exe
* %program files%\imyfone\imyfone tunesfix\7z.exe
* %program files%\intelligent converters\demos\zip.exe
* %program files%\intel\phone flash tool\7z.exe
* %program files%\kingo root\tools\7z.exe
* %program files%\moyea\dvd4web converter\7z.exe
* %program files%\my-bp\zip.exe
* %program files%\my-pf\zip.exe
* %program files%\ospeedy batch photo processor\7za.exe
* %program files%\pa file sight\7za.exe
* %program files%\pa storage monitor\7za.exe
* %program files%\radarsync\updater\extract\7z.exe
* %program files%\radioboss\7za.exe
* %program files%\raxco\perfectupdater\updater\extract\7z.exe
* %program files%\systweak\netbook optimizer\updater\extract\7z.exe
* %program files%\tenorshare ibackupunlocker\7z\7z.exe
* %program files%\unhackme\7za.exe
* %program files%\winzip driver updater\updater\extract\7z.exe
* %program files%\wise\wise driver care\7z.exe
* %program files%\wondershare\dr.fone\addins\recovery\extractor\7z.exe

While most of these are not necessarily the most popular ever, there are people downloading and installing these…

And compression utilities are not the only tools we may find, f.ex. some software install curl.exe and wget.exe – how cool is that?

* %program files%\git\mingw64\bin\curl.exe
* %program files%\hp\pfp\_guide\wget.exe
* %program files%\pa file sight\wget.exe
* %program files%\pa storage monitor\wget.exe
* %program files%\printfil\wget.exe
* %program files%\wondershare\dr.fone\addins\recovery\wget.exe

Need a mysql dump? here it is:

* %program files%\memberties\server\bin\mysqldump.exe

VNC?

There you go:

* %localappdata%\crossloop\winvnc.exe
* %program files%\crossloop\winvnc.exe
* %program files%\hammer software\metalan administrator 2\vnc\tightvnc3\winvnc.exe
* %userappdata%\design master software\remote support\vnc.exe
* c:\tcafe\tcvnc.exe

And if you need any more examples, remember my [NVIDIA Uninstallers](https://www.hexacorn.com/blog/2017/11/10/reusigned-binaries-living-off-the-signed-land/) post from 2017.

This entry was posted in [Compromise Detection](https://www.hexacorn.com/blog/category/compromise-detection/), [Living off the land](https://www.hexacorn.com/blog/category/living-off-the-land/), [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/), [Reusigned Binaries](https://www.hexacorn.com/blog/category/living-off-the-land/reusigned-binaries/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2023/08/25/lolbins-for-connoisseurs/ "Permalink to Lolbins for connoisseurs…").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")