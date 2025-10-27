---
title: LABScon Replay | InkySquid: The Missing Arsenal
url: https://buaq.net/go-144172.html
source: unSafe.sh - 不安全
date: 2023-01-05
fetch_date: 2025-10-04T03:03:31.147994
---

# LABScon Replay | InkySquid: The Missing Arsenal

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

LABScon Replay | InkySquid: The Missing Arsenal

InkySquid: The Missing Arsenal: this mp4 audio file was automatically transcribed by Sonix with th
*2023-1-4 21:28:11
Author: [www.sentinelone.com(查看原文)](/jump-144172.htm)
阅读量:22
收藏*

---

InkySquid: The Missing Arsenal: [this mp4 audio file](https://sonix.ai/speech-to-text-all-supported-file-formats?utm_source=embed "Sonix's converts the most popular audio file formats to text") was [automatically transcribed by Sonix](https://sonix.ai/transcribe-audio?utm_source=embed "Sonix is the best way to transcribe audio files in 2023") with the [best speech-to-text algorithms.](https://sonix.ai/automated-transcription?utm_source=embed "The best speech-to-text algorithms") This transcript may contain errors.

**Speaker1:**

So let's speak about the agenda. I will speak about a macOS malware I worked on on April this year, and I was really excited by working on this case because I don't often work on macOS malware because, you know, malware does not exist on macOS. So I was really excited about that. And the presentation will be about the workflow. So the first stage, the download, the second stage, the malware itself is a different capability and the last part will be more about the attribution and why we linked it to InkySquid and why we think in fact it's a macOS version of RokRAT.

**Speaker1:**
And before starting, I need to mention this thing, so I work on it on April. We published a private report at the beginning of May. Middle of May, I replied to the call for paper and beginning of July I received the mail. I'm accepted. And in middle of July, Marc Etienne published a blog post about the malware I was working on. So I was a little bit sad. I discussed with Juan to know if I need to cancel my talk, if I need to find something else to discuss with my colleagues. And Rene's friend told me something very funny for me. He told me, you know, being scooped by ESET is probably the proof your research is solid. So I decided to do it, and I decided to speak a little bit more about the attribution and why we think it's the macOS version of RokRAT, because it's not mentioned on the ESET publication.

So ESET named the malware CloudMensis, we name it BaDRAT on the presentation. I will use our name because that's the name we use on our report before the publication, but it's the same malware. So. Yeah.

First, let's discuss a little bit about InkySquid. So it's also name at APT 37 by Mandiant, ScarCruft by Kaspersky Group123 by Cisco TALOS. And it's a North Korean threat actor. And mainly from my knowledge many target defectors or people linked to this domain like lawyers and stuff like that. A big issue for for us and when you want to to follow this specific threat actor is most of the time they target a personal computer so they don't target company. They target directly the users.

They are known to use spear phishing and water holing and they often use a couple of N-Day exploits. So I think they use once a zero day for a few years ago, but most of the time it's not zero days its N Days and we will see if they do exactly the same thing on this case and we already published two stuff about this specific threat actor.

Yeah, just for information as ESET already published something, we won't do it. We won't publish anything after the publication. So if you you want something feel free to ping me, I will give you what you need. But I don't think we will publish something. It won't be super interesting after ESET publication.

So why we name it BaDRAT and it simply on the computation path on the sample you have 'BaD' in the name. You also have a name which is LeonWork and you have a system. So here it's version 29. We think it's 2.9 in fact, but it means it's here for for a couple of time. We only discovered it on April this year, but it's it's year four for a long time. So it's macOS malware and it's support x86 architecture and ARM architecture. Also you have both binary compile and. Yeah.

The first stage is a downloader. So as you can imagine, it download something and as a downloader it uses pcloud. So you have an API key in the binary. It download the next stage on pcloud and in fact it download two step, no it download one step the final malware BadRAT and it also drop a persistence file. So.

Here is the persistence file. So it's simply a classical macOS daemon. It's nothing really complicated. But yeah, and the purpose is to execute something named WindowsServer, which is funny for macOS malware.

Something interesting in the downloader so it doesn't do anything except downloading something droppings to file. But the developer forget old code so it's not executed, but it's still here and it's an old exploit from 2017. So I think they remove it because it doesn't work anymore. It's too old, but they remove the code, but they don't remove the the code itself and it's a privilege escalation. So it's something public and it was probably used after the publication on GitHub because you really have a copy paste of a GitHub project. So it's probably an N-day used by this actor.

So if we look at the malware itself, you really have all the capability of something for espionage. So the malware is able to execute arbitrary command to provide a remote share to the attackers, to perform screenshot, to perform killing. I put a screenshot of the of the keylogging, to make some exfiltration based on file extension. So he has a dictionary of file extensions and it will exfiltrate all the files with this extension.

**Speaker1:**
Something interesting is if you plug a USB device, it will use this extension list to exfiltrate all the documents from this USB device.

And there is also an email parsing mechanism. So it passed this user username library email repository and exfiltrate all the attachment received by the user always based on these extensions.

And Zytiga is able to execute Applescript directly on the malware. So something interesting is. There is absolutely no obfuscation. So everything is in text plain. You can almost read it. The only obfuscation is a configuration file, which is kind of more important because you have the API key, etc.. And here I implemented the algorithm as implemented it. Finally, it's a simple XOR, but they make a lot of weird stuff to do XOR. So it's basically XOR implementation.

And on the configuration file, you have the version. 29 in our sample, which means a couple of different versions can live together because each version will have its own configuration file. So yeah.

So configuration file contains a lot of detail on the infected machine, so the malware will connect the IP country username, adware hostname, so a full image of the infected system. This information will be sent to the attackers at the first connection and the API key for the cloud provider and the malware support three cloud providers. So Dropbox, pCloud and Yandex in our sample.

Something interesting is. The cloud provider is identified by an integer and it starts at two. So we assume the past they had one because nobody start counting at two. So they probably supported another provider in the past, but it was removed in this sample.

And from a good point of view, the three cloud provider, the code is here. It's simply the configuration file which say, I will use this code or this that you have the implementation embedded in the file for the three providers. It will also contain a path where the malware put is temporary stuff. The extension, we will see the extension a little bit after so that the extension I mentioned previously and generated ID to identify ...