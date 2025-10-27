---
title: Inside Cridex – Memory Analysis Case Study
url: https://memoryforensic.com/inside-cridex-memory-analysis-case-study/
source: Instapaper: Unread
date: 2024-10-04
fetch_date: 2025-10-06T18:55:56.543515
---

# Inside Cridex – Memory Analysis Case Study

[Skip to content](#content)

Search for:

* [Home](https://memoryforensic.com)
* [Tutorials](https://memoryforensic.com/category/tutorials/)
* [Challenges](https://memoryforensic.com/category/challenges/)
* [Write-ups](https://memoryforensic.com/category/write-ups/)
* [Samples](https://memoryforensic.com/category/samples/)
* [Tools](https://memoryforensic.com/category/tools/)
* [Reviews](https://memoryforensic.com/category/reviews/)

[![memory forensic logo](data:image/gif;base64...)](https://memoryforensic.com/)

* [Home](https://memoryforensic.com)
* [Tutorials](https://memoryforensic.com/category/tutorials/)
* [Challenges](https://memoryforensic.com/category/challenges/)
* [Write-ups](https://memoryforensic.com/category/write-ups/)
* [Samples](https://memoryforensic.com/category/samples/)
* [Tools](https://memoryforensic.com/category/tools/)
* [Reviews](https://memoryforensic.com/category/reviews/)

Analyze Memory
[Our Services](/services)

[Memory Forensic](https://memoryforensic.com)

Master the Art of Memory Forensics

[Memory Forensic](https://memoryforensic.com)

Master the Art of Memory Forensics

[![memory forensic logo](data:image/gif;base64...)](https://memoryforensic.com/)

* [Home](https://memoryforensic.com)
* [Tutorials](https://memoryforensic.com/category/tutorials/)
* [Challenges](https://memoryforensic.com/category/challenges/)
* [Write-ups](https://memoryforensic.com/category/write-ups/)
* [Samples](https://memoryforensic.com/category/samples/)
* [Tools](https://memoryforensic.com/category/tools/)
* [Reviews](https://memoryforensic.com/category/reviews/)

[Our Services](/services)

[Resources](https://memoryforensic.com/category/resources/)[Samples](https://memoryforensic.com/category/samples/)[Write-ups](https://memoryforensic.com/category/write-ups/)

# Inside Cridex – Memory Analysis Case Study

[Husam Shbib](https://memoryforensic.com/author/hoxed/)[Oct 2, 2024Sep 30, 2024](https://memoryforensic.com/inside-cridex-memory-analysis-case-study/)

![Analyzing Cridex Malware in Memory](https://memoryforensic.com/wp-content/uploads/2024/09/malware-cridex.webp)

## Introduction

Cridex, also known as Dridex, is a banking worm (evolved over the year to be full-featured banking malware) that employs advanced techniques to evade detection and facilitate the theft of financial information. Memory forensics is crucial in analyzing Cridex due to its ability to operate in memory and evade traditional file-based detection methods.

Keep in mind that this study case is not a full walk-through investigation, instead, it gives you just an idea on analyzing memory dumps. It will be beneficial, especially for beginners to get started.

As MemoryForensic is a collaborative blue team platform, we are sharing valuable community-contributed resources like this one – Cridex case study.

**Note**: Fileless malware or memory-resident malware don’t necessarily mean that all stages of the cyber kill chain occur entirely in memory. While certain steps, such as execution and command-and-control communication, may happen in memory, other stages like initial infection, persistence mechanisms, or lateral movement might involve writing to disk, using registry keys, or dropping small files as triggers.

## Credit

This work is done by [Diyar Saadi](https://www.linkedin.com/in/ACoAAEwS6boBtYE7q950XcvMIfFXXKkoP_G3OGI), and this article is based on his work and analysis.

## Downloading the Cridex Memory Dump / Running on the Cloud Lab

> Attention: the sample you are about to download may include malicious files and malware samples. To protect your system, please analyze it on a completely isolated virtual machine if it is not running on cloud

You can download the memory dump directly from [here](https://ics.muni.cz/~valor/pv204/images/cridex.vmem.bz2).

## Used Tools

* [Volatility2](https://github.com/volatilityfoundation/volatility/releases)
* [**Volatility WorkBench**2](https://www.osforensics.com/downloads/VolatilityWorkbench.zip)
* [VirusTotal](http://virustotal.com)

## Cridex Analysis Steps

* Using Volatility:
  + Load the memory dump into a forensics tool like Volatility.
  + Use plugins to extract information about running processes, network sockets, and loaded DLLs.
* Identifying Malicious Processes:
  + Look for processes that exhibit suspicious behavior, such as unusual names or those running from unexpected locations.
  + Check for injected code or modified processes that may indicate Cridex activity.
* Checking Network Connections:
  + Analyze active network connections to identify communications with known Cridex command and control servers.
  + Use the netscan or connscan plugins to identify any abnormal network activity.
* Recovering Artifacts:
  + Extract artifacts like clipboard content, which might contain stolen information, or passwords saved in memory.
  + Use the cmdscan or consoles plugins to examine command history that might reveal user interactions with the malware.
* Detecting Persistence Mechanisms:
  + Analyze the registry keys and services that might indicate how Cridex maintains persistence on the infected system.
  + Look for unusual entries that may have been created by the malware.

## The Case Study Document

[Cridex-Malware-Memory-Analysis](https://memoryforensic.com/wp-content/uploads/2024/09/Cridex-Malware-Memory-Analysis.pdf)[Download](https://memoryforensic.com/wp-content/uploads/2024/09/Cridex-Malware-Memory-Analysis.pdf)

## Conclusion

We briefly analyzed Cridex malware residing in a memory dump, provided some tips and tricks, that will give you a start in analyzing memory dumps.

We hope that you download the memory dump in safe environment, try analyzing it before the case study file to better enhance your memory analysis skills.

~ Cya till the next one ðŸ™‚

## <span class="nav-subtitle screen-reader-text">Page</span>

[![Certified CyberDefenders Husam Shbib](data:image/gif;base64...)

Previous PostMy Review on Certified CyberDefender Certification](https://memoryforensic.com/my-review-on-certified-cyberdefender-certification/)

[![13cubed Linux Memory Forensics Challenge](data:image/gif;base64...)

Next PostLinux Memory Forensics Challenge](https://memoryforensic.com/linux-memory-forensics-challenge/)

### Related Posts

[![13cubed Linux Memory Forensics Challenge](data:image/gif;base64...)](https://memoryforensic.com/linux-memory-forensics-challenge/)

#### [Linux Memory Forensics Challenge](https://memoryforensic.com/linux-memory-forensics-challenge/)

A Linux Memory Forensics Challenge by 13Cubed

[Oct 5, 2024Oct 1, 2024](https://memoryforensic.com/linux-memory-forensics-challenge/)

[![General Overview of Random Access Memory (RAM) - The Heartbeat of Digital Devices](data:image/gif;base64...)](https://memoryforensic.com/ram-101-what-it-is-and-why-it-matters/)

#### [RAM 101 – What it is and Why it Matters](https://memoryforensic.com/ram-101-what-it-is-and-why-it-matters/)

General Overview of Random Access Memory (RAM) - The Heartbeat of Digital Devices

[Sep 26, 2024Sep 26, 2024](https://memoryforensic.com/ram-101-what-it-is-and-why-it-matters/)

[![DFIR Science How to Collect and Analyze Random Access Memory](data:image/gif;base64...)](https://memoryforensic.com/my-review-on-how-to-collect-and-analyze-random-access-memory-course-from-dfir-science/)

#### [My Review on How to Collect and Analyze Random Access Memory Course from DFIR Science](https://memoryforensic.com/my-review-on-how-to-collect-and-analyze-random-access-memory-course-from-dfir-science/)

My modest opinion about the Memory Forensics course from DFIR Science

[Aug 7, 2024Aug 8, 2024](https://memoryforensic.com/my-review-on-how-to-collect-and-analyze-random-access-memory-course-from-dfir-science/)

Search

Search

## Newsletter

## Recent Posts

* [My Review on 13Cubed Investigating Windows Memory Course](https://memoryforensic.com/my-review-on-13cubed-investigating-windows-memory-course/)
* [Akira Challenge](https://memoryforensic.com/akir...