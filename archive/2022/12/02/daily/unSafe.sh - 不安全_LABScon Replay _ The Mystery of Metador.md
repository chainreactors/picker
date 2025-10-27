---
title: LABScon Replay | The Mystery of Metador
url: https://buaq.net/go-138112.html
source: unSafe.sh - 不安全
date: 2022-12-02
fetch_date: 2025-10-04T00:15:48.183662
---

# LABScon Replay | The Mystery of Metador

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

LABScon Replay | The Mystery of Metador

The Mystery of Metador.mp4: this mp4 audio file was automatically transcribed by Sonix with the be
*2022-12-1 22:18:59
Author: [www.sentinelone.com(查看原文)](/jump-138112.htm)
阅读量:19
收藏*

---

The Mystery of Metador.mp4: [this mp4 audio file](https://sonix.ai/speech-to-text-all-supported-file-formats?utm_source=embed "Sonix's converts the most popular audio file formats to text") was [automatically transcribed by Sonix](https://sonix.ai/transcribe-audio?utm_source=embed "Sonix is the best way to transcribe audio files in 2022") with the [best speech-to-text algorithms.](https://sonix.ai/automated-transcription?utm_source=embed "The best speech-to-text algorithms") This transcript may contain errors.

**Juan Andres Guerrero-Saade:**

So first and foremost, I'm Juan Andres Guerrero-Saade, Jags, your host, you are very familiar with me, Alex, here over at SentinelLabs with me and Amitai, who was actually part of our internal research team with Brian Bartholomew and Chris Saint Myers. And this has been like a big joint research effort that we've been doing across our different research teams together. Our Metador friends would probably refer to us as fellow hackers. But we'll get into that in a little bit.

So I just wanted to set a little bit of context, Right. Thomas was up here. He talked about the equation group drop Regen. There's been a lot of discussions about these big APTs. And frankly, it's always fascinating to me because I'm obsessed with that side of the house. I love the big flashy APTs and the things nobody knows about and understanding what big intelligence agencies are doing and the capabilities they've developed that we could only dream of. And among those, I mean, right, we talked about Equation Group, we talked about Regin. We talk about DuQu one and two, but Barr, Project, Sauron, REM, sex, Strider, whatever you want to call them, Kirito, Wild Neutron Flame, one and two.

**Juan Andres Guerrero-Saade:**
And the truth is that these are all amazing discoveries, each one of them redefining what we thought was possible, how we understood the threat landscape. But beyond redefining what's possible, I think they also showed us a sort of weakness, a giant blind spot. Not only did we not know what they were doing before, the fact that they were discovered and published on doesn't mean that we know where they are now. It doesn't mean that we actually know where these apex predators are at any given moment.

And I think the truth is that we've accepted a form of partial blindness. We've said, you know, these are the one percenters. We'll catch a glimpse from time to time. And it's kind of okay that we don't see them. Maybe because you ideologically agree with them, maybe because you think they're not in your target area or frankly, because it's hard, because a lot of security products are not being developed in the right way because a lot of visibility keeps sort of fraying for us and things that we used to rely on, like VT don't have the same level of samples that they had anymore. And there's so many ways that things are getting more difficult for us, and we've accepted that partial blindness.

The question that I want to press here is do we still think that those one percenters are the sole proprietors of that level of capabilities? And with that nagging thought. I'll hand over to Amitai.

**Amitai Ben Shushan Ehrlich:**
So our story begins like many other interesting stories. It appears with a magnet, a magnet of threats and networks that was interesting enough to draw the attention of several state sponsored actors. When we got there, it was very much compromised and the first thing we noticed when we got there was actually traces of the muddy paws of Kitten. Muddy Water were very much active in that network, deploying their powerful backdoors, registering schedule tasks, and also moving laterally, using a WMI exec like a lot of other actors. And when we started monitoring their activity over WMI exec, we noticed something weird.

There is this big cluster of activity here related to Muddy Water and with a WMI exec, But there is another actor here also running a lot of stuff with WMI exec. And that's when we realized we also have to deal with pandas roaming around the network and not just one. Over the time that we looked at this magnet of threats, we found over four different clusters of Chinese espionage activity, very much active in the network.

At this point, we realized we have we were dealing with a very interesting network, a very interesting target, and we started actively monitoring and hunting for new threats. And we did find a lot of unattributed activity, a lot of new activities. But above all of them, one stood out and it wasn't a kitten, nor a panda, but. A bull. And when I say a bull, you guys probably imagine this magnificent animal with its horns and robotic features.

**Amitai Ben Shushan Ehrlich:**
But this is not our our bull. Looks like our bull actually looked like this. The actual bull in the room was actually execution of the Microsoft console debugger, a legitimate debugging tool of by Microsoft executed with the debugging script stored in CDB.ini. Debugging the legitimate Windows process defrag.exe. And we noticed this activity looked quite suspicious, quite malicious. And knowing that the Microsoft console debugger is a legitimate process and also defrag is a legitimate process, we understood whatever is causing this malicious activity is probably stored in the debugging script in CDB.ini.

So we started looking into that and when we opened it, we saw like this huge string of hexadecimal values and we were like, okay, that's interesting. It's it's a cut here. But it was very, very long and we started looking into the actual contents of the script. What it does, it reads the long hexadecimal string as quad word values. That's the eq and runs them at the entry point of the binary, that's the X entry and then detaches. Effectively what it means is actually run this shell code stored in this long string at the start of the binary. Now the usage of the Microsoft console debugger is documented and read information about it online as a tool to use as a LOL bin.

**Amitai Ben Shushan Ehrlich:**
But that was quite unusual and interesting. So we try to take this long hexadecimal string and turn it into a shell code. Look how it actually looked like and this is how it looked like.

Quite a standard shell code. And what it does is reads an additional file stored in speech02.db and load it into memory and run it. At this point we realized, okay, we have this long chain of staging a very interesting malware and we started reconstructing the entire image and this is what we got to.

So as you can see, we have the cdb.exe, the Microsoft console debugger, running the injector script, injecting the shell code into defrag.exe. This in turn will load speech02.db. This is a reflective loader which will load speech03.db. Surprisingly, speech03.db is actually a fully comprehensive implant that we call meta main. This entire framework that I just talked about is the persistent mechanism behind meta main.

And interestingly enough, in this context, Meta main was used to load an additional implant called Mafalda. Mafalda is a second implant which was used in the same chain. And those two implants are very much interesting and very much unusual in today's landscape. They contain a lot of interesting functionality and Alex here reversed the hell out of them and is going to talk about what's so interesting about it.

**Aleksandar Milenkoski:**
So i...