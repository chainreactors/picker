---
title: Excelling at Excel, Part 3
url: https://buaq.net/go-146478.html
source: unSafe.sh - 不安全
date: 2023-01-23
fetch_date: 2025-10-04T04:35:07.666399
---

# Excelling at Excel, Part 3

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/9fcb3a4577a82890ba9de0eb262d5357.jpg)

Excelling at Excel, Part 3

One of the most common use cases we come across during our malware analysis exercises is
*2023-1-22 08:56:23
Author: [www.hexacorn.com(查看原文)](/jump-146478.htm)
阅读量:40
收藏*

---

One of the most common use cases we come across during our malware analysis exercises is a ROI-driven comparison of features between many samples of the same malware family. Yes, we can use [BinDiff](https://www.zynamics.com/bindiff.html), [Diaphora](https://github.com/joxeankoret/diaphora) (and we should), but if it is a time-sensitive research, we need to take some shortcuts to deliver early results pronto.

Here’s one way to do it.

Note: I have used this approach many times in the past, because it’s simple, easy to understand, and produces a visual that is VERY nice to include in your deliverables. Your customers do not want to see the lengthy reports including all gore metadata and strings extracted from each and every sample. They want to see THE STORY.

A high-level matrix showing a difference between different versions of malware can be often quickly built by looking at, and comparing strings extracted from multiple samples (I simplify it a bit here: yes, in many cases you may need to decrypt these strings first, but it’s a reversing task we are all used to, so I won’t be covering it here).

So, how do we go about it?

After the basic triage, we extract strings selectively from all the samples of malware we have and we put them all in Excel. Like this:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/exc_3_1.png)](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/exc_3_1.png)

We now have a simple database of ‘features’ or unique capabilities of each sample. There are similarities between them that are immediately striking, plus, some features seem to exist across many samples, and some are just one-offs. As a side note: all these one-offs are VERY interesting as they often are examples of bad OPSEC, and/or may reveal some of the additional intentions/motivations of the attackers. In some rare cases, the older compilers embed so-called ‘dead code’ (never executed) in the final executable, so strings extracted from such sample provide a rare intel that may help with attribution. True story: over a decade ago I have analyzed one such sample and the dead code gave away a lot of info about the attacker – that was enough to pinpoint the exact individual responsible for that particular hacking spree.

We now want to build a superset list of all features, and for each sample, put ‘yes’ if the feature is present, and ‘no’ – if it is not.

So, we first add a new column to which we will copy and paste all the filled-in cells from each sample’s column, one by one:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/exc_3_2.png)](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/exc_3_2.png)

We then remove all duplicates from the ‘All’ column by using *Data / Remove Duplicates* function:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/exc_3_3.png)](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/exc_3_3.png)

giving us this as a result:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/exc_3_4.png)](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/exc_3_4.png)

Let me now show you what we want to build from this data: the final product we are after is a matrix of all interesting strings / features (column ‘All’) cross-referenced with each sample’s strings:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/exc_3_5.png)](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/exc_3_5.png)

How do we build it?

We use three functions: VLOOKUP, ISNA and IF.

VLOOKUP helps us to find a given string in a specific column. If it exists, it will simply give us its value, otherwise it will return “N/A” (not available). We then use ISNA function to test the result of VLOOKUP. If it is “N/A”, we output “No”, otherwise we output “Yes”. We then add some basic cell formatting on top of it (add borders to make it look like a table, center text vertically and horizontally within the cells) + add some conditional formatting (if cell contains “Yes”, make it Blue, and if “No”, make it Red) and we get the result shown above.

These are formulas I have used in this example:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/exc_3_6-1024x91.png)](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/exc_3_6.png)

It may look complicated at first, but the logic is brutally simple:

We start by using a VLOOKUP function — we look for a string from a fixed column $E ‘All’ (dollar in front of it is to avoid it changing to F, G, H in subsequent horizontal formula copy via CTRL+R mentioned below), within the A:A column (which is sample1), and if it is found (ISNA returns false) we say ‘Yes’, otherwise, we say ‘No’. We populate this formula with CTRL+D (vertically), and CTRL+R (horizontally) and all the other cells should be now filled in with formulas like on the above picture.

When we build a matrix like this we can immediately spot some interesting bits about the samples:

* sample4 may be the earliest as it includes `written by bored Bob`, possible OPSEC fail and attribution bit here
* sample1 and sample3 seem to be the most advanced, with sample3 being probably the latest as it offers remoteshell capabilities; the ‘screencapture’ feature present in sample1 is not present in sample3 which could be explained as ‘it’s 2023 and video streaming is a thing aka screenshots are so 2010’

Of course, there are million other ways to do the very same task. And after all, it’s a manual and kinda mundane task to do this via Excel, but again, there are some lessons learned here:

* by experimenting like this we build processes that can be then automated with better tools (f.ex. python, perl)
* data presented in tables speaks to customers better than the most comprehensive reverse engineering efforts (none of them want to look at Ida or Ghidra screenshots; they want root-cause analysis, TTPs, IOCs, high-level description of features and capabilities, and what has changed between malware versions found on their systems)
* in many cases I encountered, especially in a Linux world (ELF files), this is more than enough to pinpoint main differences between samples of the same malware family; it’s a great time saver!
* even more interesting is another bit — for many trojanized programs or libraries (again, especially in Linux world), string-based comparisons against their clean versions often yield really great results (somehow, threat actors love to add a lot of extra debugging strings, messages, etc. that immediately stand out)

文章来源: https://www.hexacorn.com/blog/2023/01/22/excelling-at-excel-part-3/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)