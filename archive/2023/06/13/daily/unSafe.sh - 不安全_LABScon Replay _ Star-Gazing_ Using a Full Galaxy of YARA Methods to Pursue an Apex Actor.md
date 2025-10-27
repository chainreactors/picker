---
title: LABScon Replay | Star-Gazing: Using a Full Galaxy of YARA Methods to Pursue an Apex Actor
url: https://buaq.net/go-168412.html
source: unSafe.sh - 不安全
date: 2023-06-13
fetch_date: 2025-10-04T11:44:22.619222
---

# LABScon Replay | Star-Gazing: Using a Full Galaxy of YARA Methods to Pursue an Apex Actor

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

LABScon Replay | Star-Gazing: Using a Full Galaxy of YARA Methods to Pursue an Apex Actor

Star-Gazing | Using a Full Galaxy of YARA Methods to Pursue an Apex Actor | By Greg Lesnewich (Proo
*2023-6-12 22:16:55
Author: [www.sentinelone.com(查看原文)](/jump-168412.htm)
阅读量:15
收藏*

---

## Star-Gazing | Using a Full Galaxy of YARA Methods to Pursue an Apex Actor | By Greg Lesnewich (Proofpoint): [Audio automatically transcribed by Sonix](https://sonix.ai/?utm_source=embed "Sonix is the best audio transcription service in 2023")

Star-Gazing | Using a Full Galaxy of YARA Methods to Pursue an Apex Actor | By Greg Lesnewich (Proofpoint): [this mp4 audio file](https://sonix.ai/speech-to-text-all-supported-file-formats?utm_source=embed "Sonix's converts the most popular audio file formats to text") was [automatically transcribed by Sonix](https://sonix.ai/transcribe-audio?utm_source=embed "Sonix is the best way to transcribe audio files in 2023") with the [best speech-to-text algorithms.](https://sonix.ai/automated-transcription?utm_source=embed "The best speech-to-text algorithms") This transcript may contain errors.

**Greg Lesnewich:**

**Greg Lesnewich:**
My name is Greg. I work at an email company called Proofpoint. That is, my job is primarily doing what Victor does following me, chasing the L word out of our email data. And today's talk is nothing about that. So before we start, this talk does discuss a bit of a taboo actor, which I track as Bright Constellation. But there are a litany of disclaimers that my wife and our company mandated that I say I do not discuss the incident responses. We do not actively pursue this actor. There are no leaked documents herein; this is personal research and although the actor is something that was a little bit attention grabbing previously, it was mostly sort of a interesting piece of data to explore developing a malware similarity via YARA.

**Greg Lesnewich:**
So there are going to be some musical references scattered throughout here that link to the naming of the malware families themselves. If you can figure them out, you can take a shot after the talk with me. So first, I think that YARA and a lot of parts of this conference only happen from learning through one another and being people being open and willing to share and teaching others. And so the list of humans and robots far exceeds this slide that have helped me to really learn and understand and develop some better ideas for detection ideas.

**Greg Lesnewich:**
A few that I want to call out today are Connor McLaughlin, Arielle and Costin from Kaspersky Xorex and of course, our pal Steve Miller. And so getting to the elephant in the room, our subject today is the Lamberts. Those I think everybody here probably knows who they are because Juan knows who they are. And at least in my time in the Threat Intel space, they have been maybe the highest regarded actor that I'm aware of. Juan has talked on and on and on about their amazing multi framework toolkit and their incredible operational security and their awesome tradecraft. And so I'm building on a lot of the work that Symantec and Kaspersky and previously FireEye had published about. But my interest in them is basically only because I knew that if I submitted about them, Juan was likely to accept my talk.

**Greg Lesnewich:**
So the Lamberts present a little bit of an interesting problem for us as an industry. Kaspersky had this amazing Kaspersky and Symantec really had this amazing series of very interesting actors with white papers getting published about them, like Equation like Project Sauron, like Stuxnet, Dooku, Name one. And they had all these really rich papers discussing the malware and doing all these sorts of deep technical analysis that you could walk away with an understanding of what was happening.

**Greg Lesnewich:**
And Kaspersky has no reason to like, I'm not putting throwing shade on them, but their paper about the Lamberts was noticeably shorter. There weren't a lot of hashes published with it, but they did have this cool chart showing the constellation of the Lamberts toolkit that, you know, there wasn't a white paper to sort of support the linkages or highlight what was going on there, which to me presented a pretty interesting opportunity because if you go on VirusTotal, there is a detection across ESET and Kaspersky that just says Lamberts, but it unfortunately is not linked to any of the colors listed there. So it presented kind of a fun black box for us to play with.

**Greg Lesnewich:**
And so I think like most other threat intel analysts, this is a familiar sight. After another vendor publishes a report, you have a list of files that if they didn't publish a YARA rule or some other form of detection, you just sort of have to figure out detection in your own environment. And so, yeah, this is our starting point, I think like a lot of other investigations.

**Greg Lesnewich:**
And so the initial methodology and what we're going to walk through a few different steps that I took that I thought was decently valuable. I'm going to take a macro view of all of the 50 samples that were available on VirusTotal at the time that I started this.

**Greg Lesnewich:**
And what we're going to do is we're going to rely really heavily on a couple of tools like Yara, particularly its console module. For those of you that aren't familiar with it, it's like a console, like anything else, like Python, whatever else. A script that Steve Miller built to sort of wrap the console module called Ronnie, which is a Ronnie Coleman reference that I think one person in this room gets. And then we're going to use another tool called Binary Refinery to sort of show the evidence of some of the data that we're working with. And given knowing the crowd here at Labs Con, I'm going to use that as an excuse to really roll really quickly through the first section of the content.

**Greg Lesnewich:**
So initially. Like most other analysts, you're looking at samples in bulk. We're going to look for overlaps across the import hash hashes of the sections, the resources, and then more like developer fingerprints. The PDB path, the DLL name, and then sort of looking at the general geometry of all these files. And so if you take this initial surface area, even for this elite, highly apex actor, we can already start to see some overlaps with these DLL names up here at the top and then some import hashes mixed with DLL .dll there at the bottom.

**Greg Lesnewich:**
And so one of the things that I want to really highlight in this talk is the codification of what you can do with a local YARA instance, like on an analyst machine and just plug your ideas into console output rules.

**Greg Lesnewich:**
And so you can have it burp out things like, say, the rich header hash and then use sort and unique to burp out overlaps. And as you work through this and look at at least in this actor in particular, and I think this applies to a lot of them, you can start to start. You can start to see a number of weird overlaps like these DLLs mixed with the A PDB paths. And if you iterate and iterate and iterate and you look at things like the resource and section hashes, ignoring that very obvious empty hash there at the top, you do eventually get to start clustering some of the families, notably the PDB path, the export names and. More like general hashing was really good for us to start to cluster some of these families together. And we actually have our first linkage across the malware families to each other with rationalist and cutting ties, sharing this weird smartcard helper string resour...