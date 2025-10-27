---
title: Machine Learning Versus Memory Resident Evil
url: https://buaq.net/go-147397.html
source: unSafe.sh - 不安全
date: 2023-02-01
fetch_date: 2025-10-04T05:17:19.614276
---

# Machine Learning Versus Memory Resident Evil

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

![](https://8aqnet.cdn.bcebos.com/e4de425889239c3ddcd48cd28d4c99c5.jpg)

Machine Learning Versus Memory Resident Evil

Executive SummaryUnit 42 res
*2023-1-31 22:0:26
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-147397.htm)
阅读量:34
收藏*

---

![A pictorial representation of highly evasive malware, including sandbox evasion](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/01/Malware-r3d2.png)

## Executive Summary

Unit 42 researchers discuss a machine learning pipeline we’ve built around memory-based artifacts from our hypervisor-based sandbox, which is part of Advanced WildFire. This alternative approach is one we’ve come up with to boost detection accuracy against malware using a variety of different evasion techniques.

As we discussed in [our first two posts](https://unit42.paloaltonetworks.com/tag/memory-detection/) in this series, malware authors are routinely refining their shenanigans to make strategies like static analysis and sandboxing ineffective. The continual development and permutation of techniques like packing methodologies and sandbox evasions create a continual cat and mouse game that is difficult to stay on top of for any detection team.

To make matters worse, popular detection techniques such as structural analysis, static signatures and many types of dynamic analysis do not fare well against the ever-increasing complexity we encounter in the more prevalent malware families.

| **Related Unit 42 Topics** | [Sandbox](https://unit42.paloaltonetworks.com/tag/sandbox/), [evasive malware](https://unit42.paloaltonetworks.com/tag/evasive-malware/), [machine learning](https://unit42.paloaltonetworks.com/tag/machine-learning/), [AI](https://unit42.paloaltonetworks.com/tag/ai/), [memory detection](https://unit42.paloaltonetworks.com/tag/memory-detection/) |
| --- | --- |

## Table of Contents

[Statically Armored and Full of Evasions](#post-126856-_e3aliopza7nu)

## Statically Armored and Full of Evasions

Malware authors increasingly employ evasion techniques such as obfuscation, packing and execution of dynamically injected shellcode in process memory. Using cues from the file structure for malware detection might not always succeed. Packing techniques modify the file structure sufficiently to eliminate these clues. Thus, machine learning models trained on this class of features alone would not effectively detect such samples.

Another popular alternative to this detection method is to use a machine learning model that predicts maliciousness based on the malware’s execution traces inside a sandbox. However, as detailed in [our previous post in this series](https://unit42.paloaltonetworks.com/sandbox-evasion-memory-detection/), sandbox evasions are extremely prevalent and payloads will often choose not to execute based on any number of clues that would point to a sample being emulated.

Malware can also inadvertently or intentionally corrupt the sandbox environment, overwrite log files or prevent successful analysis for any number of reasons due to the [low-level tricks](https://unit42.paloaltonetworks.com/single-bit-trap-flag-intel-cpu/) it is playing. This means that training our machine learning models on the execution logs is also not going to be enough to catch these evasive types of malware.

## GuLoader Encrypted With NSIS Crypter

In this post, we will analyze one GuLoader downloader that has been encrypted with an Nullsoft Scriptable Install System (NSIS) crypter. NSIS is an open source system to create Windows installers.

|  |  |
| --- | --- |
| **Hash** | cc6860e4ee37795693ac0ffe0516a63b9e29afe9af0bd859796f8ebaac5b6a8c |

### Why Static Analysis Isn’t Going To Help

The GuLoader malware is encrypted, and it is also delivered through a NSIS installer file that is not ideal for static analysis because the file contents must be unpacked first. Once it’s unpacked, we are still left with encrypted data and one NSIS script. The script itself also dynamically decrypts some parts of the code, which is another factor that makes it harder to detect.

However, there are not many structural clues that would identify this as possible malware. Thus, a machine learning model trained on the Portable Executable (PE) file structure would not be effective in differentiating the file from other benign files.

### NSIS Script and Extracting GuLoader Shellcode

To extract the NSIS script, we have to use an older version of 7-Zip, version 15.05. This version of 7-Zip is able to unpack the script, where newer versions have removed the functionality to unpack NSIS scripts. Once we have extracted the file contents and the NSIS script (shown in Figure 1), we can start analyzing the script and see how the GuLoader sample is being executed.

![Image 1 is a screenshot of many lines of code the NSIS script, prepared to analyze.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/01/ML-AWS-F1.png)

Figure 1. The NSIS script.

If we scroll down the script, we quickly notice that the files are being copied into a newly created folder named %APPDATA%\Farvelade\Skaermfeltet. Though it’s not clear why, the file paths used seem to be in Danish. After the copying activity, we have regular installation logic in the script, but there is one interesting function named func\_30.

Before this function is called, the string $INSTDIR\Filterposerne\Malkekvg.Nat is copied into a string variable named $4, as shown in Figures 2 and 3. The function func\_30 reads data from the Programmeludviklinger210.Kon file and builds up code, which it will call immediately after the character Z has been seen.

NSIS gives developers the ability to call any exported function from a Windows DLL, and it also allows developers to save the results directly in NSIS registers/stack. This functionality allows malware authors to dynamically call Windows API functions on runtime and makes static analysis harder because it must be evaluated before being analyzed.

![Image 2 is a screenshot of a few lines of code of the NSIS script as it calls function func_30.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/01/word-image-126856-2.png)

Figure 2. Calling function func\_30.

![Image 3 is a screenshot of many lines of code showing the NSIS code as it is decoded.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/01/word-image-126856-3.png)

Figure 3. Decoding NSIS code.

To decode the dynamic code, we can write a short Python script that reproduces the behavior and extracts the Windows API calls:

|  |  |
| --- | --- |
|  | with open('Programmeludviklinger210.Kon', 'rb') as f:      buf = f.read()  decoded = b''  offset = 3551  while offset < len(buf):      if buf[offset] == ord('Z'):          print(decoded.decode('utf-8'))          decoded = b''      else:          decoded += buf[offset].to\_bytes(1, byteorder='little')      offset += 507 |

Figure 4 shows the decoded data that results from the script above.

![Image 4 is a screenshot of a few lines of code showing the decoded Windows API calls.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/01/word-image-126856-4.png)

Figure 4. Decoded Windows API calls.

The decoded functions together read a shellcode from another file from the NSIS archive, and they execute it using the EnumWindows function. If we had to write this process in pseudo code, it would look something like this:

|  |  |
| --- | --- |
|  | int r5, r3;  void\* r3;  char\* r4 = "$INSTDIR\\Filterposerne\\Malkekvg.Nat"  r5 = kernel32::CreateFileA(r4 , 0x80000000, 0, 0, 4, 0x80, 0)  r3 = kernel32::SetFilePointer(r5, 6078, 0,0)  r1 = kernel32::VirtualAlloc(0, 0x101000, 0x3000, 0x40)  r3 ...