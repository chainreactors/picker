---
title: Sandbox_Scryer - Tool For Producing Threat Hunting And Intelligence Data From Public Sandbox Detonation Output
url: https://buaq.net/go-136631.html
source: unSafe.sh - 不安全
date: 2022-11-22
fetch_date: 2025-10-03T23:22:53.432405
---

# Sandbox_Scryer - Tool For Producing Threat Hunting And Intelligence Data From Public Sandbox Detonation Output

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

![](https://8aqnet.cdn.bcebos.com/59f6f6e36f8e05321fee01cf563e714a.jpg)

Sandbox\_Scryer - Tool For Producing Threat Hunting And Intelligence Data From Public Sandbox Detonation Output

The Sandbox Scryer is an open-source tool for producing threat hunting and intelligence da
*2022-11-21 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-136631.htm)
阅读量:24
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhEkO_7BLm2yIe2Fg8yqCr8240TtKpuXiqbBiPpcj2nEHt3TMqh5bx4C4zXmnbiAKy5Qyvx2PWJnKoJLjX5dfLD4mLRIvPZYq6pjCUiGFMd4WQZJGMQ_B1eagaeSPZ3AnsDpJVnmSJoTYvHZ5WwCRJbQeTpWFlGHqXjK5iSLfJ3rq5-er0iA7hyhbNQyg/w640-h472/h33.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhEkO_7BLm2yIe2Fg8yqCr8240TtKpuXiqbBiPpcj2nEHt3TMqh5bx4C4zXmnbiAKy5Qyvx2PWJnKoJLjX5dfLD4mLRIvPZYq6pjCUiGFMd4WQZJGMQ_B1eagaeSPZ3AnsDpJVnmSJoTYvHZ5WwCRJbQeTpWFlGHqXjK5iSLfJ3rq5-er0iA7hyhbNQyg/s551/h33.png)

The Sandbox Scryer is an open-source tool for producing [threat hunting](https://www.kitploit.com/search/label/Threat%20Hunting "threat hunting") and [intelligence](https://www.kitploit.com/search/label/Intelligence "intelligence") data from public sandbox detonation output The tool leverages the MITRE ATT&CK Framework to organize and prioritize findings, assisting in the assembly of IOCs, understanding attack movement and in threat hunting By allowing researchers to send thousands of samples to a sandbox for building a profile that can be used with the ATT&CK technique, the Sandbox Scryer delivers an unprecedented ability to solve use cases at scale The tool is intended for [cybersecurity](https://www.kitploit.com/search/label/Cybersecurity "cybersecurity") professionals who are interested in threat hunting and attack analysis leveraging sandbox output data. The Sandbox Scryer tool currently consumes output from the free and public Hybrid Analysis [malware analysis](https://www.kitploit.com/search/label/Malware%20Analysis "malware analysis") service helping analysts expedite and scale threat hunting

[root] **version**.txt - Current tool version LICENSE - Defines license for source and other contents README.md - This file

[root\bin] \Linux - Pre-build binaries for running tool in Linux. Currently supports: Ubuntu x64 \MacOS - Pre-build binaries for running tool in MacOS. Currently supports: OSX 10.15 x64 \Windows - Pre-build binaries for running tool in Windows. Currently supports: Win10 x64

[root\presentation\_video] Sandbox\_Scryer\_\_BlackHat\_Presentation\_and\_demo.mp4 - Video walking through slide deck and showing demo of tool

[root\screenshots\_and\_videos] Various backing screenshots

[root\scripts] Parse\_report\_set.\* - Windows PowerShell and DOS Command Window batch file scripts that invoke tool to parse each HA Sandbox report summary in test set Collate\_Results.\* - Windows PowerShell and DOS Command Window batch file scripts that invoke tool to collate data from parsing report summaries and generate a MITRE Navigator layer file

[root\slides] BlackHat\_Arsenal\_2022\_\_Sandbox\_Scryer\_\_BH\_template.pdf - PDF export of slides used to present the Sandbox Scryer at Black Hat 2022

[root\src] Sandbox\_Scryer - Folder with source for Sandbox Scryer tool (in c#) and Visual Studio 2019 solution file

[root\test\_data] (SHA256 filenames).json - Report summaries from submissions to Hybrid Analysis enterprise-attack\_\_062322.json - MITRE CTI data TopAttackTechniques\_\_High\_\_060922.json - Top MITRE ATT&CK techniques generated with the MITRE calculator. Used to rank techniques for generating heat map in MITRE Navigator

[root\test\_output] (SHA256)\_report\_\_summary\_Error\_Log.txt - Errors (if any) encountered while parsing report summary for SHA256 included in name (SHA256)\_report\_\_summary\_Hits\_\_Complete\_List.png - Graphic showing tecniques noted while parsing report summary for SHA256 included in name (SHA256)\_report\_\_summary\_MITRE\_Attck\_Hits.csv - For collation step, techniques and tactics with select metadata from parsing report summary for SHA256 included in name (SHA256)\_report\_\_summary\_MITRE\_Attck\_Hits.txt - More human-readable form of .csv file. Includes ranking data of noted techniques

\collated\_data collated\_080122\_MITRE\_Attck\_Heatmap.json - Layer file for import into MITRE Navigator

The Sandbox Scryer is intended to be invoked as a command-line tool, to facilitate scripting

Operation consists of two steps:

* Parsing, where a specified report summary is parsed to extract the output noted earlier
* Collation, where the data from the set of parsing results from the parsing step is collated to produce a Navigator layer file

Invocation examples:

* Parsing
* Collation

If the parameter "-h" is specified, the built-in help is displayed as shown here Sandbox\_Scryer.exe -h

```
        Options:
```

Once the Navigator layer file is produced, it may be loaded into the Navigator for viewing via [https://mitre-attack.github.io/attack-navigator/](https://mitre-attack.github.io/attack-navigator/ "https://mitre-attack.github.io/attack-navigator/")

Within the Navigator, techniques noted in the sandbox report summaries are highlighted and shown with increased heat based on a combined scoring of the technique ranking and the count of hits on the technique in the sandbox report summaries. Howevering of techniques will show select metadata.

Sandbox\_Scryer - Tool For Producing Threat Hunting And Intelligence Data From Public Sandbox Detonation Output
![Sandbox_Scryer - Tool For Producing Threat Hunting And Intelligence Data From Public Sandbox Detonation Output](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhEkO_7BLm2yIe2Fg8yqCr8240TtKpuXiqbBiPpcj2nEHt3TMqh5bx4C4zXmnbiAKy5Qyvx2PWJnKoJLjX5dfLD4mLRIvPZYq6pjCUiGFMd4WQZJGMQ_B1eagaeSPZ3AnsDpJVnmSJoTYvHZ5WwCRJbQeTpWFlGHqXjK5iSLfJ3rq5-er0iA7hyhbNQyg/s72-w640-c-h472/h33.png)
Reviewed by Zion3R
on
9:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2022/11/sandboxscryer-tool-for-producing-threat.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)