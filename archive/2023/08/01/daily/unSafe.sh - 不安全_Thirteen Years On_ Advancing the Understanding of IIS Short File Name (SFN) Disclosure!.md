---
title: Thirteen Years On: Advancing the Understanding of IIS Short File Name (SFN) Disclosure!
url: https://buaq.net/go-173326.html
source: unSafe.sh - 不安全
date: 2023-08-01
fetch_date: 2025-10-06T16:59:34.534725
---

# Thirteen Years On: Advancing the Understanding of IIS Short File Name (SFN) Disclosure!

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

![](https://8aqnet.cdn.bcebos.com/ab44f81a45dff3660b9ee140bd01631e.jpg)

Thirteen Years On: Advancing the Understanding of IIS Short File Name (SFN) Disclosure!

The topic of IIS Short File Name (SFN, also known as 8.3) disclosure has been explored across vario
*2023-7-31 23:59:20
Author: [soroush.me(查看原文)](/jump-173326.htm)
阅读量:21
收藏*

---

The topic of IIS Short File Name (SFN, also known as 8.3) disclosure has been explored across various platforms in the past. In this blog post, I’ll take a look at the insights I presented at [SteelCon 2023](https://www.steelcon.info/), which extended the scope of the original research.

The presentation can be downloaded from: <https://github.com/irsdl/IIS-ShortName-Scanner/blob/master/presentation/Steelcon-2023-Beyond_Microsoft_IIS_Short_File_Name_Disclosure.pdf>

The original research can be seen here: <https://soroush.me/downloadable/microsoft_iis_tilde_character_vulnerability_feature.pdf>

If you’re particularly keen on diving straight into the latest insights, feel free to navigate to the final two sections of this post.

## Happy Birthday

First thing first, I originally identified the IIS Short File Name (SFN, also known as 8.3) Disclosure on August 1, 2010 – meaning it’s now entered its teenage years!

[![](https://i0.wp.com/soroush.me/blog/wp-content/uploads/2023/07/image-3.png?resize=293%2C354&ssl=1)](https://i0.wp.com/soroush.me/blog/wp-content/uploads/2023/07/image-3.png?ssl=1)

## **A Quick Look at the History of Short File Names**

Originally, the FAT file systems were somewhat limited and could only support short names. These short file or directory names contain a maximum of 8 characters. If an extension is present, it requires a dot, followed by up to 3 more characters. Therefore, the maximum total length of these names, including the extension, is 12 characters.

[![](https://i0.wp.com/soroush.me/blog/wp-content/uploads/2023/07/image-4.png?resize=360%2C122&ssl=1)](https://i0.wp.com/soroush.me/blog/wp-content/uploads/2023/07/image-4.png?ssl=1)

With the introduction of VFAT, support for long file names began with Windows 95. In the NTFS system, short file names aren’t necessary, but Windows still creates them for the sake of backwards compatibility. This happens when file names don’t conform to the rules for short file names, such as when they exceed the character limit, contain unsupported characters, or feature more than one dot.

[![](https://i0.wp.com/soroush.me/blog/wp-content/uploads/2023/07/image-5.png?resize=470%2C224&ssl=1)](https://i0.wp.com/soroush.me/blog/wp-content/uploads/2023/07/image-5.png?ssl=1)

## **SFN Rules**

SFNs, or Short File Names, are case-insensitive and utilize uppercase characters exclusively. They consist of alphanumerical characters and a select few special characters. Spaces are not included, and there should only be one dot character used, which is followed by an extension.

Windows uses certain rules when creating short file names for file names. Typically, the short name begins with the first six characters of the actual file name, followed by a tilde (~) character and a number. If the file name includes an extension, the first three characters of the extension are appended after a dot.

During this process, Windows also eliminates disallowed characters, additional dots, and space characters. It will also substitute a plus sign (+) with an underscore (\_).

In cases where a short name equivalent already exists for a different file, the system increments the number following the tilde. If you’re curious to see the short names that have been generated in Windows, you can use the ‘dir /x’ or ‘dir /-n’ commands to view them.

As you might imagine, due to the constraints on character length, many long names can result in identical short names. Prior to Windows 2000, Windows permitted the number following the tilde character to go as high as 9. However, starting from Windows 2000, this number has been capped at 4. This raises the question: what happens if there are more than four files resulting in the same short name, given that Windows no longer uses ~5?

Well, the formula for generating short names changes. Now it utilizes the first two (or less if any exists) characters of the file name, followed by four hexadecimal characters produced by an algorithm. If the file name contains just one character, that single character is used. Thomas Galvin has done extensive research on this hexadecimal algorithm, and I highly recommend reading his work if you’re interested. I’d also suggest checking out these resources and their references for a more in-depth exploration.

Recently, [@bitquark](https://twitter.com/bitquark) has also explored this feature further using the [leaked Windows 2003 source code](https://github.com/selfrender/Windows-Server-2003). He has implemented his findings in his IIS short name scanner tool coded in the Go language, which you can find here: <https://github.com/bitquark/shortscan>

## What’s Affected?

As of the time of this writing, all IIS versions are susceptible to this issue. However, this might not be the case if the SFN feature was disabled on Windows prior to the creation of the web directory.

## Usefulness

While the risk associated with uncovering short file names on its own is quite low (mostly informational), it often proves useful by accelerating penetration testing or providing quick insights during bug bounty hunts.

Leveraging this vulnerability, I’ve discovered numerous sensitive files and even managed to download databases in the past. I’ve also identified several files with inadequate access control, including admin control panels leading to high risk issues.

## Automation

* <https://github.com/bitquark/shortscan> (implementation in Go with checks to find the real file name)
* <https://github.com/irsdl/IIS-ShortName-Scanner> (the original tool in Java)
* <https://github.com/sw33tLie/sns> (another Go one)
* <https://github.com/cyberaz0r/Burp-IISTildeEnumerationScanner> (burp suite extension)
* <https://github.com/0xRTH/IISRecon/> (bash script to find real file names too)

## Manual Checks in 2023

If you’re interested in checking this manually, I’ll share my approach. I typically choose several HTTP methods and suffixes, to target a short file name that should exist (such as web.config or default.aspx) and one that should not. If the HTTP response differs, then I know I’ve hit the jackpot.

Initially, I select the OPTIONS HTTP method and pair it with the /~1/.rem pattern for the suffix. If this doesn’t yield results, I switch the HTTP method to POST, DEBUG, GET, or PATCH. I also experiment with different suffixes such as /~1.rem, /~1.aspx, /~1.svc, /~1.xamlx, or /~1.soap.

This process can be automated using Burp Suite Intruder, as follows:

[![](https://i0.wp.com/soroush.me/blog/wp-content/uploads/2023/07/image-6.png?resize=625%2C299&ssl=1)](https://i0.wp.com/soroush.me/blog/wp-content/uploads/2023/07/image-6.png?ssl=1)

## Tips and Tricks for Manual Checks

* Don’t solely rely on the response status code—make sure to compare the entire response.
* Don’t confuse Kestrel or HTTP.SYS with IIS. Recent versions of .NET, such as 6, 7, and Core, might be running on Kestrel.
* Web Forms that use the .NET Framework can be served with or without extensions.
* This process won’t work on virtual files or IIS virtual/app paths.
* Note that wildcards can be replaced:
  + ? can be replaced with >
  + \* can be replaced with <
  + ” can be replaced with .
* URL encoding may be crucial in certain instances.
* Web Application Firewalls (WAFs) can lead to anomalies, so be aware of that.
* Space...