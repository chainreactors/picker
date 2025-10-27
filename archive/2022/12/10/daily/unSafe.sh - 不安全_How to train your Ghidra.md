---
title: How to train your Ghidra
url: https://buaq.net/go-139385.html
source: unSafe.sh - 不安全
date: 2022-12-10
fetch_date: 2025-10-04T01:05:27.926200
---

# How to train your Ghidra

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

![](https://8aqnet.cdn.bcebos.com/372b798c0a374ecab490bfcfd9b38e91.jpg)

How to train your Ghidra

Getting started with GhidraFor about two decades, being a reverse engineer meant that
*2022-12-9 21:0:23
Author: [securelist.com(查看原文)](/jump-139385.htm)
阅读量:31
收藏*

---

## Getting started with Ghidra

For about two decades, being a reverse engineer meant that you had to master the ultimate disassembly tool, IDA Pro. Over the years, many other tools were created to complement or directly replace it, but only a few succeeded. Then came the era of decompilation, adding even more to the cost and raising the barrier to entry into the RE field.

Then, in 2019, Ghidra was published: a completely open-source and free tool, with a powerful disassembler and a built-in decompiler for each supported platform. However, the first release did not look even close to what us reverse engineers were used to, so many of us tried and then abandoned it.

It may sound anecdotal, but the most popular answer to, “Have you used Ghidra?” I usually hear is, “Yeah, tried it, but I’m used to IDA”, or “I don’t have the time to check it out; maybe later”.  I was like that, too: tried to reverse something, failed miserably, went back to familiar tools. I would still download a newer version every once and then, and try to do some work or play CTF. One day, after making a few improvements to the setup and adding the missing databases, I would not go back.

So, here is my brief introduction to setting up Ghidra, and then configuring it with a familiar UI and shortcuts, so that you would not need to re-learn all the key sequences you have got used to over the years.

## Disclaimer

Ghidra is a complex collection of source code with many third-party dependencies that are known to contain security vulnerabilities. There are no guarantees that the current code base is free from those or that it does not contain any backdoors. Proceed with caution, handle with care.

## Building Ghidra

Of course, the easiest way to obtain Ghidra is to download the current release published on Github. The current code is months behind the master branch, and will most likely be missing all the latest features. So, although this is not the officially recommended approach, I suggest getting the bleeding-edge code from the master branch and building the binaries yourself. In the meantime, we are going to prepare our own build of the master branch and make it available for download.

So, let us begin. First, you need the following prerequisites:

**All OSs:**

* JDK 17 64-bit, [Adoptium Temurin](https://adoptium.net/temurin/releases) is recommended
* [Gradle 7.3+](https://gradle.org/next-steps/?version=7.3.3&format=bin); Ghidra works well with 7.3.3

Additionally, you need the platform-specific compiler for building the native binaries:

* **Windows:** Microsoft Visual Studio (2017 or later; 2022 Community edition works well)
* **Linux:** modern GNU Compiler Collection (9 and 12 work well)
* **macOS:** Xcode build tools

Then, download the latest source code in a [ZIP archive](https://github.com/NationalSecurityAgency/ghidra/archive/refs/heads/master.zip) and extract it, or clone the official Git repository.

### Windows build

Open the command line prompt (CMD.EXE). Set the directory containing the source code as the current one:

Run “bin\gradle.bat” from the Gradle directory to initialize the source tree and download all the dependecies:
`gradle.bat -I .\gradle\support\fetchDependencies.gradle init`

You need an active Internet connection, and it may take 5–10 minutes to download the dependencies.
[![](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/12/08164157/image1.png)](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/12/08164157/image1.png)

In the end, the output should state, “BUILD SUCCESSFUL” and also print clearly that Visual Studio was located (required for further building).
[![](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/12/08164239/image2.png)](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/12/08164239/image2.png)

If there were problems, check your Internet connection—provided that you have Visual Studio, JDK and Gradle properly installed. Once the build succeeds, issue the final command:
`gradle.bat buildGhidra`

It will take more time, you may see lots of warnings printed out, but the final verdict still should be, “BUILD SUCCEESFUL”.
[![](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/12/08164245/image3.png)](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/12/08164245/image3.png)

The complete Ghidra package is written as a ZIP archive to the “build\dist” directory. To run Ghidra, extract the ZIP archive and start “ghidraRun.bat”.
[![](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/12/08164251/image4.png)](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/12/08164251/image4.png)

At the time of writing this, Ghidra 10.3-DEV used the “Windows” UI configuration as the default one, so there was no need to reconfigure the “look and feel” option.
[![](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/12/08164255/image5.png)](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/12/08164255/image5.png)

### Linux build

Use an existing terminal window or open a new one.
Set the directory containing the source code as the current one:
`cd %directory_of_ghidra_source_code%`

Run “bin\gradle” from the Gradle directory to initialize the source tree and download all the dependencies:
`gradle -I ./gradle/support/fetchDependencies.gradle init`

You need an active Internet connection, and it may take 5–10 minutes to download the dependencies. Please note that the task may fail if your locale is different from “en\_US” and GCC uses translated messages:
[![](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/12/08164300/image6.png)](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/12/08164300/image6.png)

This may happen, for example, with the Russian locale, because the version string for GCC is translated:
[![](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/12/08164306/image7.png)](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/12/08164306/image7.png)

As a mitigation, run gradle prefixed with “LANG=C”:
`LANG=C gradle -I ./gradle/support/fetchDependencies.gradle init`

In the end, the output should state, “BUILD SUCCESSFUL”.
[![](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/12/08164311/image8.png)](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/12/08164311/image8.png)

Then, build Ghidra and all the dependencies:
`Gradle buildGhidra`

Once the build succeeds, a ZIP archive can be located in the build/dist directory. Extract it from there.
[![](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/12/08164315/image9.png)](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/12/08164315/image9.png)

To start Ghidra, use the “ghidraRun” shell script in the root directory of the extracted archive:
[![](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/12/08164318/image10.png)](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/12/08164318/image10.png)

At the time of writing this, version 10.3-DEV used the “Nimbus” look and feel as the default:
[![](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/12/08164...