---
title: Examining the IconCache database
url: https://thinkdfir.com/2025/12/28/examining-the-iconcache-database/
source: Instapaper: Unread
date: 2026-01-05
fetch_date: 2026-01-06T03:28:12.334117
---

# Examining the IconCache database

[Skip to content](#content)

Open Menu

* [About](https://thinkdfir.com/about/)
* [Contact](https://thinkdfir.com/contact/)
* [Find Me](https://thinkdfir.com/find-me/)
* [Posts](http://thinkdfir.com)

* [LinkedIn](https://www.linkedin.com/in/phill-moore-b740b212)
* [Twitter](https://twitter.com/phillmoore)
* [GitHub](http://github.com/randomaccess3)
* [This Week In 4n6](https://www.thisweekin4n6.com)

*Search*

Search for:

 Close

[![](https://thinkdfir.com/wp-content/uploads/2017/07/cropped-cropped-cropped-cropped-cropped-bulb-160207_640.png)](https://thinkdfir.com/)

# [ThinkDFIR](https://thinkdfir.com/)

## random musings on DFIR topics

![](https://thinkdfir.com/wp-content/uploads/2025/12/image-2.png?w=810)

[Uncategorized](https://thinkdfir.com/category/uncategorized/)

# Examining the IconCache database

[December 28, 2025](https://thinkdfir.com/2025/12/28/examining-the-iconcache-database/) [Phill Moore](https://thinkdfir.com/author/randomaccess3/)[Leave a comment](https://thinkdfir.com/2025/12/28/examining-the-iconcache-database/#respond)

Earlier this year I came across a forensic artefact that I didn’t know a whole lot about, and there wasn’t a lot of research on either. I was working on a ransomware case where we picked up a standard KAPE triage collection. As part of that, I ran a keyword search in Xways over the entire package for the names of our malicious executables and some hits caught my eye. Inside the users *localappdata* was a file called IconCache.db that I had seen in passing but never really looked at before. I had just bought a copy of 010 Editor so down the rabbit hole we go!

Special thanks to my former coworkers Cassie and Yogesh for their assistance in picking this apart.

## What is IconCache

The IconCache contains the images associated with an items icon so that Windows can recall it without rebuilding it. Think of it like ThumbCache but for Icons, in fact some of the databases are even in the same spot.

IconCache is made up of a few different files:

```
%localappdata%/IconCache.db
%localappdata%/Microsoft/Windows/Explorer/iconcache_*.db
```

![](https://thinkdfir.com/wp-content/uploads/2025/12/screenshot-2025-12-25-163453.png?w=201)

## Parsing the data

![](https://thinkdfir.com/wp-content/uploads/2025/12/image-2.png?w=1024)

If you have 010 editor and want to parse the data from your IconCache.db file then you can grab the template from [here](https://www.sweetscape.com/010editor/repository/templates/file_info.php?file=IconCache.bt&type=0&sort=). We were able to take the format documentation from [this](https://www.sciencedirect.com/science/article/abs/pii/S1742287614000607) research paper (who did most of the heavy lifting) and identify how the format has changed since their release.

In the current database format (where the version string is 0x0507) you get a lowercase version of the paths, and sometimes you get Shell items which is nice. I’ve also put up a couple of IconCache.db files (not the icon files databases) onto the [DFIR Artifact Museum](https://github.com/AndrewRathbun/DFIRArtifactMuseum/tree/main/Windows/IconCache) that I extracted from two SIFT workstations.

Here’s a [Python script](https://github.com/5ha0/fortools) that parses the earlier version but I haven’t really tested it. Here’s a [CPP program](https://github.com/cereme/FirstSound) as well but this looks like it will only parse the 0x0506 version of the db.

The actual icons are stored in a different database, and I haven’t really done much looking at the format – that said, there’s an 010 template to parse these files and [ThumbCache Viewer](https://thumbcacheviewer.github.io/) works too. The downside of joining these two artifact sets together, which I have not yet been able to do.

## Interesting observations

* Windows 11 doesn’t mean you’ll get the format 0x0507. I’m guessing once the database is there it doesn’t really change format so if you upgrade Win10 to Win11 the database won’t get recreated unless you force it. Either way, the 010 template handles both. There’s earlier formats but I haven’t bothered looking at those so the template doesn’t cover this.
* The database seems to get written on shutdown or reboot so data recorded will only cover everything prior to the last startup.
* This isn’t going to be an evidence of execution artefact, just an evidence of existence.
* I haven’t looked into the circumstances where you get a Shell item but we did incorporate Didier Stevens’ code to parse the data so you can explore that in the 010 template data.
* The actual icon images are stored in individual databases based on the size of the icon, or the referenced DLL (read the paper but that part was less interesting for me). There’s no filenames unfortunately. There’s a CRC hash like with the ThumbCache but as we’ve got the paths in the other database maybe it’s possible as long as the underlying code doesn’t take other values.
  + I haven’t figured out how to join the paths to the images; But that’s something that I think would be super useful in investigations. Tools like Mimikatz, Netscan and the myriad of RMM tools used in ransomware investigations usually have specific icons so even if the program has been renamed it’s another clue.
* When I increased the size of the icons to the maximum size the template dies, so it doesn’t support that yet (ever? who knows).

This is an interesting artefact that I’ll probably keep plugging away at to try and join the dots. But for now, maybe it might be useful for threat hunting.

If you find issues let me know and we can look at updating the template!

### Share this:

* [Click to share on X (Opens in new window)
  X](https://thinkdfir.com/2025/12/28/examining-the-iconcache-database/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://thinkdfir.com/2025/12/28/examining-the-iconcache-database/?share=facebook)

Like Loading...

# Post navigation

[Previous Post

A question about arbitrary values in USB registry keys](https://thinkdfir.com/2025/11/23/a-question-about-arbitrary-values-in-usb-registry-keys/)

### Leave a comment [Cancel reply](/2025/12/28/examining-the-iconcache-database/#respond)

Δ

## Recent Posts

* [Examining the IconCache database](https://thinkdfir.com/2025/12/28/examining-the-iconcache-database/)
* [A question about arbitrary values in USB registry keys](https://thinkdfir.com/2025/11/23/a-question-about-arbitrary-values-in-usb-registry-keys/)
* [Sometimes Windows and PE Version information don’t get along](https://thinkdfir.com/2025/07/28/sometimes-windows-and-pe-version-information-dont-get-along/)
* [Cached screenshots on Windows 11](https://thinkdfir.com/2025/06/13/cached-screenshots-on-windows-11/)
* [Sunday Funday – Searching for searching](https://thinkdfir.com/2025/03/08/sunday-funday-searching-for-searching/)
* [SRUMday Funday!](https://thinkdfir.com/2025/01/13/srumday-funday/)
* [Windows11 Wordwheelquery Woes](https://thinkdfir.com/2024/10/31/windows11-wordwheelquery-woes/)
* [How can I be of WebAssist(ance)?](https://thinkdfir.com/2023/11/09/how-can-i-be-of-webassistance/)
* [CPY JMP](https://thinkdfir.com/2023/05/17/cpy-jmp/)
* [Timestamps in INDX Entries](https://thinkdfir.com/2023/01/13/timestamps-in-indx-entries/)

## Follow Blog via Email

Enter your email address to follow this blog and receive notifications of new posts by email.

Email Address:

Follow

## Archives

Archives

Select Month
 December 2025
 November 2025
 July 2025
 June 2025
 March 2025
 January 2025
 October 2024
 November 2023
 May 2023
 January 2023
 February 2022
 January 2022
 October 2021
 June 2021
 February 2021
 January 2021
 December 2020
 October 2020
 September 2020
 July 2020
 April 2020
 March 2020
 January 2020
 December 2019
 October 2019
 July 2019
 June 2019
 May 2019
 March 2019
 February 2019
 January 2019
 November 2018
 October 2018
 September 2018
 August 2018
 July 2018
 June 2018
 April 2018
 March 2018
 January 2018
 December 2017
 O...