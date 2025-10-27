---
title: LABScon Replay | Blasting Event-Driven Cornucopia: WMI-based User-Space Attacks Blind SIEMs and EDRs
url: https://buaq.net/go-145138.html
source: unSafe.sh - 不安全
date: 2023-01-12
fetch_date: 2025-10-04T03:38:23.676181
---

# LABScon Replay | Blasting Event-Driven Cornucopia: WMI-based User-Space Attacks Blind SIEMs and EDRs

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

![]()

LABScon Replay | Blasting Event-Driven Cornucopia: WMI-based User-Space Attacks Blind SIEMs and EDRs

Blasting Event-Driven Cornucopia: WMI-based User-Space Attacks Blind SIEMs and EDRs: this mp4 audi
*2023-1-11 22:33:23
Author: [www.sentinelone.com(查看原文)](/jump-145138.htm)
阅读量:34
收藏*

---

Blasting Event-Driven Cornucopia: WMI-based User-Space Attacks Blind SIEMs and EDRs: [this mp4 audio file](https://sonix.ai/speech-to-text-all-supported-file-formats?utm_source=embed "Sonix's converts the most popular audio file formats to text") was [automatically transcribed by Sonix](https://sonix.ai/transcribe-audio?utm_source=embed "Sonix is the best way to transcribe audio files in 2023") with the [best speech-to-text algorithms.](https://sonix.ai/automated-transcription?utm_source=embed "The best speech-to-text algorithms") This transcript may contain errors.

**Claudiu Teodorescu:**

**Claudiu Teodorescu:**
So who is Binarly? So Binarly a startup in LA focused on device security and monitoring threats below the operating system and see how they're moving up the stack into the operating system kernel and user land and then deploy their next level components. Unfortunately, Andrei and Igor, which contributed to this research, could not make the trip to LABScon. But I'll take the credit for them and then maybe have a drink when we first meet in person.

So let's go a little bit into the agenda. So I'll present a little touch, a little bit brief on the architecture and features of WMI. Just a primer for for people that are not familiar with WMI. And also show some artifacts, forensic artifacts that I was deeply involved while reversing the format five, six, seven years ago. Then I'll show how WMI is leveraged for formal policy orchestration. And next one moving into actually the meat of the discussion on attacks on WMI, how WMI is leveraged for evil, how that will present a threat model WMI threat model and the different attack vectors. And then we'll move to present the two new attacks that I already advertised.

**Claudiu Teodorescu:**
So WMI architecture, it's a pretty comprehensive image. But in short, WMI is the Windows implementation of two standards WBEM, which is web based enterprise management and the CIM, which is a common information model. It's available systemwide in all operating systems and doesn't have to be installed, and it offers a standardized framework to produce and consume events that are represented as WMI objects.

And in short, the architecture consists of the producers, WMI producers, which produce device telemetry as WMI objects, clients that consume those devices do those events to get device telemetry. One good example is PowerShell, which can be used to gather this type of telemetry both remotely and locally. Next is the CIM standard, the Common Common Information Module standard, which consists of the repository itself that stores the class definitions and namespace definitions as well as persistent WMI objects. Then we have the MOF, which is an object oriented language used to specify WMI artifacts to extend the frame the the standard. Next we have the query language, which is the WQL. It's a SQL like query to filter events and DICOM and and when a RAM are used to remotely connect, to transmit and receive data. And last but not least, not the least is the WMI service, which is implemented as the services host DLL service in the Net VCS Group.

WMI providers. We already touched on this. Just a little reminder, it's an instance of \_\_Win32 provider, which is a standard class since providers are implemented as common com based the DLLs. That identifiable class ID and all the information of the column is in the interfaces, is in the registry, and the Windows 11 are more than 4000 built in WMI providers.

So one of the main ability of WMI is to act on events that cover pretty much any operating system event. And another ability that is very is used by in the wild by attackers is the ability to to register permanent event subscriptions which survive system reboots. We'll see an example of that.

There are two types of events intrinsic events and existing events. I left here the definition of both for future reference. Now event filters specify which events should be should be transmitted to the bound consumer to act on those. The main the main properties of of of event filter is the namespace in which it operates the query language that is used mostly the WQL and the last but not the least is the the query itself that specify how to filter the events and send it to the bound consumer. And here we have the syntax, the general syntax of WQL for, for a for filtering. And then two examples. One is the first is the intrinsic event example that triggers whenever, notepad.exe is launched. The other one is an example of extrinsic event which monitors the run key for registry key for malware persistence.

And now we talk about the consumers. So the consumer specify the action that should be taken when when an event filter triggers. And as we can see that the the standard defines already five or six default consumers to log files, to log events, to run scripts or command lines or send notifications. And let's go a little bit more into detail. I mentioned the persistence, the permanent event subscription that's that's actually done for persistence and code execution is the method. How you do it and how you do it is just define the filter, which specify which event to trigger the action that is defined by the by the event consumer and then binding bind them into an instance of filter to consumer binding.

So now let's talk a little bit about the repository. So repository is the WMI repository. It's a path and files can be found in the registry and consists of three types of files. First is the INDEX.BTR, which is the index file for the for the WMI repository implemented as a B-Tree on disk and stores the the search path strings in pages. Then is OBJECTS.DATA which consists actually the the which contains actually the namespace definitions, class definitions and persistent WMI objects. And then again stored in pages and consisting of records.

**Claudiu Teodorescu:**
And then the last not the least is the historic versioning of three three historic versions of mapping.map, which contains the mapping records. Because in in WMI there is abstraction logic to to physical logic, page number to physical page number. So the mappings are used to actually translate the logical page number to its physical correspondent.

So let's look in in practice how this will should work. So we have the INDEX.BTR. First we need to create the search path string for the WMI object that we're looking for so that how it's done, you get the identifier for the namespace class, an instance name, you concatenate them using some prefixes that are there mention and then the index that is search for that for that path string. And then the index record is identified. And what's important in that, the first the first number is the logical page number of the record we are looking for in OBJECT.DATA file. Then the other one is the record identifier, and the third one is the the size of the record. So in order to do the translation, to find out where the physical offset is, we have to use the the mapping map, which actually consists of two arrays of Dwords, one for OBJECT.DATA, the other one for INDEX.BTR and how it works. The logical number actually represents the index in the array. The value of that index is the corresponding physical page number.

The same thing the same algorithm can be used for for parsing the INDEX.BTR, it...