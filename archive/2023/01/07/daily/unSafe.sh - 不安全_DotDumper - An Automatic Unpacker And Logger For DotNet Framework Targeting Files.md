---
title: DotDumper - An Automatic Unpacker And Logger For DotNet Framework Targeting Files
url: https://buaq.net/go-144468.html
source: unSafe.sh - 不安全
date: 2023-01-07
fetch_date: 2025-10-04T03:13:38.408099
---

# DotDumper - An Automatic Unpacker And Logger For DotNet Framework Targeting Files

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

![](https://8aqnet.cdn.bcebos.com/bf1be9cfde9e52da8d28d121e0f4e651.jpg)

DotDumper - An Automatic Unpacker And Logger For DotNet Framework Targeting Files

An automatic unpacker and logger for DotNet Framework targeting files! This tool has been un
*2023-1-6 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-144468.htm)
阅读量:31
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh4da3FI8kjcBqH7VE0hkUIM_ErL97m_alt-IswglIbr0X-_AgxAfcKyIKDr0fTQXhpO9CagR33Jr3Gu1YTCChYguigB3WzpVdeRHc5XxhZB7Joisg6r3NwslqIZt2xID6tfuRVGZvOGdQLPWgrANouVHrcOhAH5H04E1j2vsCTSFYTL_tpBV8ftpg-1g/w640-h434/DotDumper_1_DotDumper.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh4da3FI8kjcBqH7VE0hkUIM_ErL97m_alt-IswglIbr0X-_AgxAfcKyIKDr0fTQXhpO9CagR33Jr3Gu1YTCChYguigB3WzpVdeRHc5XxhZB7Joisg6r3NwslqIZt2xID6tfuRVGZvOGdQLPWgrANouVHrcOhAH5H04E1j2vsCTSFYTL_tpBV8ftpg-1g/s813/DotDumper_1_DotDumper.png)

An automatic unpacker and logger for DotNet Framework targeting files! This tool has been unveiled at [Black Hat USA 2022](https://www.blackhat.com/us-22/arsenal/schedule/index.html#dotdumper-automatically-unpacking-dotnet-based-malware-27846 "Black Hat USA 2022").

The automatic detection and classification of any given file in a reliable manner is often considered the holy grail of malware analysis. The trials and tribulations to get there are plenty, which is why the creation of such a system is held in high regard. When it comes to DotNet targeting binaries, our new open-source tool DotDumper aims to assist in several of the crucial steps along the way: logging (in-memory) activity, dumping interesting memory segments, and extracting characteristics from the given sample.

## Why DotDumper?

In brief, manual unpacking is a tedious process which consumes a disproportional amount of time for analysts. Obfuscated binaries further increase the time an analyst must spend to unpack a given file. When scaling this, organizations need numerous analysts who dissect malware daily, likely in combination with a scalable sandbox. The lost valuable time could be used to dig into interesting campaigns or samples to uncover new threats, rather than the mundane generic malware that is widely spread. Afterall, analysts look for the few needles in the haystack.

So, what difference does DotDumper make? Running a DotNet based malware sample via DotDumper provides log files of crucial, contextualizing, and common function calls in three formats (human readable plaintext, JSON, and XML), as well as copies from useful in-memory segments. As such, an analyst can skim through the function call log. Additionally, the dumped files can be scanned to classify them, providing additional insight into the malware sample and the data it contains. This cuts down on time vital to the triage and [incident response](https://www.kitploit.com/search/label/Incident%20Response "incident response") processes, and frees up SOC analyst and researcher time for more sophisticated analysis needs.

## Features

To log and dump the contextualizing function calls and their results, DotDumper uses a mixture of reflection and managed hooks, all written in pure C#. Below, key features will be highlighted and elaborated upon, in combination with excerpts of DotDumper’s results of a packed AgentTesla stealer sample, the hashes of which are below.

| Hash type | Hash value |
| --- | --- |
| SHA-256 | b7512e6b8e9517024afdecc9e97121319e7dad2539eb21a79428257401e5558d |
| SHA-1 | c10e48ee1f802f730f41f3d11ae9d7bcc649080c |
| MD-5 | 23541daadb154f1f59119952e7232d6b |

### Using the command-line interface

DotDumper is accessible through a command-line interface, with a variety of arguments. The image below shows the help menu. Note that not all arguments will be discussed, but rather the most used ones.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgZW43JFDdgoptK1nkc7EjMYcVMchf8eRhsQgek2mXCHoaDxkLA9mDcR5a9d8OoY9ltYApN_DjzWe7AfqpEo9KAnYV2bgi-l-djiGfAKxmWZlAFYTr0S9jW5uTnqxom7kPGWbgJ4P441QOqRnAXxXiiAbQZmoSS50Pt8V0Rm1-O7fFD9M8gg_7k39_CvQ=w640-h422)](https://blogger.googleusercontent.com/img/a/AVvXsEgZW43JFDdgoptK1nkc7EjMYcVMchf8eRhsQgek2mXCHoaDxkLA9mDcR5a9d8OoY9ltYApN_DjzWe7AfqpEo9KAnYV2bgi-l-djiGfAKxmWZlAFYTr0S9jW5uTnqxom7kPGWbgJ4P441QOqRnAXxXiiAbQZmoSS50Pt8V0Rm1-O7fFD9M8gg_7k39_CvQ)

The minimal requirement to run a given sample, is to provide the “-file” argument, along with a file name or file path. If a full path is given, it is used. If a file name is given, the current working directory is checked, as well as the folder of DotDumper’s executable location.

Unless a directory name is provided, the “-log” folder name is set equal to the file name of the sample without the extension (if any). The folder is located in the same folder as DotDumper resides in, which is where the logs and dumped files will be saved in.

In the case of a library, or an alternative entry point into a binary, one must override the entry point using “-overrideEntry true”. Additionally, one has to provide the fully qualified class, which includes the name space using “-fqcn My.NameSpace.MyClass”. This tells DotDumper which class to select, which is where the provided function name (using “-functionName MyFunction”) is retrieved.

If the selected function requires arguments, one has to provide the number of arguments using “-argc” and the number of required arguments. The argument types and values are to be provided as “string|myValue int|9”. Note that when spaces are used in the values, the argument on the command-line interface needs to be encapsulated between quotes to ensure it is passed as a single argument.

Other less frequently used options such as “-raceTime” or “-deprecated” are safe in their default settings but might require tweaking in the future due to changes in the DotNet Framework. They are currently exposed in the command-line interface to easily allow changes, if need be, even if one is using an older version of DotDumper when the time comes.

### Logging and dumping

Logging and dumping are the two core features of DotDumper. To minimize the amount of time the analysis takes, the logging should provide context to the analyst. This is done by providing the analyst with the following information for each logged function call:

* A stack trace based on the function’s caller
* Information regarding the assembly object where the call originated from, such as the name, version, and cryptographic hashes
* The parent assembly, from which the call originates if it is not the original sample
* The type, name, and value of the function’s arguments
* The type, name, and value of function’s return value, if any
* A list of files which are dumped to disk which correspond with the given function call

Note that for each dumped file, the file name is equal to the file’s SHA-256 hash.

To clarify the above, an excerpt of a log is given below. The excerpt shows the details for the aforementioned AgentTesla sample, where it loads the second stage using DotNet’s Assembly.Load function.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjwIF2fyNtHGGRyUiLWQA1mBMn8kCJggjJrEckeajXuay4SOaMOKWFZXNmJ5hcF9D_ScTFlMaz2UW0SHTnISVE3bMBjKYZMMelRAs7U7mXhk7A2dn6aUivmKdk8fWQSB_FveRB7RgM9cOBr1GwT7LMTueeK8ChYg0tE9s9JnufSB_CtGYrRZbMkDDwczA=w640-h486)](https://blogger.googleusercontent.com/img/a/AVvXsEjwIF2fyNtHGGRyUiLWQA1mBMn8kCJggjJrEckeajXuay4SOaMOKWFZXNmJ5hcF9D_ScTFlMaz2UW0SHTnISVE3bMBjKYZMMelRAs7U7mXhk7A2dn6aUivmKdk8fWQSB_FveRB7RgM9cOBr1GwT7LMTueeK8ChYg0tE9s9JnufSB_CtGYrRZbMkDDwczA)

First, the local system time is given, together with the original function’s return type, name, and argument(s). Se...