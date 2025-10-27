---
title: LABScon Replay | Does This Look Infected 2 (APT41)
url: https://buaq.net/go-163976.html
source: unSafe.sh - 不安全
date: 2023-05-19
fetch_date: 2025-10-04T11:37:56.623639
---

# LABScon Replay | Does This Look Infected 2 (APT41)

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

LABScon Replay | Does This Look Infected 2 (APT41)

Does This Look Infected 2: this mp4 audio file was automatically transcribed by Sonix with the bes
*2023-5-18 21:25:1
Author: [www.sentinelone.com(查看原文)](/jump-163976.htm)
阅读量:34
收藏*

---

Does This Look Infected 2: [this mp4 audio file](https://sonix.ai/speech-to-text-all-supported-file-formats?utm_source=embed "Sonix's converts the most popular audio file formats to text") was [automatically transcribed by Sonix](https://sonix.ai/transcribe-audio?utm_source=embed "Sonix is the best way to transcribe audio files in 2023") with the [best speech-to-text algorithms.](https://sonix.ai/automated-transcription?utm_source=embed "The best speech-to-text algorithms") This transcript may contain errors.

**Van Ta:**

**Van Ta:**
All right. So in March of this year, we published research on a persistent, months long APT41 campaign to gain access to state government networks. Between May 2021 to February of 2022, APT41 compromised at least six state government victims, primarily through exploitation of deserialization vulnerabilities in Internet facing web applications.

**Van Ta:**
Now, throughout the roughly ten month time frame, APT41 used two different zero days. The first was in an animal health management application known as USA Herds, which at the time of our analysis was used by 18 different states. Now the nature of this vulnerability was in a static machine key that was present in all default installations of the USA Herds application. And so APT41 in possession of this key could then compromise any server on the internet running this specific application. Now, in December of 2021, APT41 quickly shifted gears to operationalize the then fresh zero day in log4j. Now in the months prior APT41 and our research revealed a number of net new malware variants and that remained the same with log4j.

**Van Ta:**
What we were observing was apt 41 was exploiting victims with log4j to then deploy the Linux variant of a backdoor that we call KEYPLUG. Now this is notable for a number of reasons. Number one, this was the first time we had observed a Linux port of this backdoor for a piece of malware that’s been around since at least 2019. And number two, the Windows version of this backdoor was heavily used during the government intrusions in the months prior. So not only are they able to shift gears, switch up and operationalize a new zero day, but they’re able to deploy a new malware capability while still simultaneously operating at state government networks. So a lot of tenacity there.

**Van Ta:**
Now, throughout all this, it was pretty clear that APT41 put the P in APT. Right. They it was frequent that we would begin response at one state government agency only to find APT41 was active in a separate unrelated agency in the same state. And not only that but upon eradication APT41 would quickly recompromise their targets. And that’s something that we observed five different times.

**Van Ta:**
And so with this research, we were able to unveil quite a bit. But one burning question that we still had that we couldn’t really answer was “Why?”. And that will be the focus of our conversation today.

**Van Ta:**
So at the time, there were a couple of safe conclusions that we could make. These are state governments. There are treasures within these networks that would be valuable to any adversary. And the evidence of a deliberate, adamant campaign, based on the evidence that I talked about in the previous slide, supported some level of a targeted collection mission. But even then, although we had evidence to support these things, we still don’t really have an answer to why.

**Van Ta:**
Now, at the time we had a couple of hunches, but nothing really conclusive. But let’s take a look at what that really looked like. So at one state, victim, 41 had deployed the passive version of a backdoor that we call LOWKEY on a server responsible for the state’s financial benefits application. Now being a passive backdoor, it was configured to listen to traffic, to specific URLs, and in this case it was configured to listen or I’m sorry to listen for traffic to a URL in which one of the strings matched that specific benefits server application.

**Van Ta:**
Now APT41 matching their configurations to kind of blend in with the environment, blend in traffic with these different applications. That’s not something that’s net new. But it did show that APT41 wanted to maintain access to this server and this part of the network. Now, upon seeing something like this, one of the first questions that we would ask is, okay, how many states use this particular application? Do you guys like my breadsticks? Right there. Okay. And so to get a quick and dirty answer, we turn to scan data looking specifically for servers that would elicit a similar response to this particular benefits application. Now, while Rufus was poking around, one server stood out one because it was the only server not in the United States, and two, it was located in China. And so being nosy like we are, we wanted to inspect it a little bit further. So let’s see what we found.

**Van Ta:**
So. So we found a what appeared to be some sort of custom web app running on an ephemeral port that was leaking PII data for US citizens belonging to one particular state. And digging a little bit further, we found something else that was pretty interesting. We found what appeared to be a custom Baidu map with custom pins located somewhere in China. And so again, being very nosy, we zoomed in a little bit further and we could see that all of the pins are located in the Chengdu province of Chengdu and in particular were four kindergartens in that area. Do you all remember Chengdu 404? That was the front company that was detailed in the September 2020 indictments of APT41 members.

**Van Ta:**
Now, at this point, we have some loose ties to operations at state government victims. But because we did not directly observe this server in relation to that particular operation, we couldn’t attribute this to APT41 And so at that time, although we had some hunches, we were still back at square one, not really knowing the answer to why. It wasn’t until we completed investigations at two additional victims that we were able to collect the evidence to get us closer to that answer.

**Rufus Brown:**
All right. Thank you, Van. So for the rest of the presentation, I want to try and focus on these. Two new state government victims. So specifically, new data we haven’t talked about and specifically came from these two new state government victims. So starting out around last summer of June 2021, this is where we saw APT41 first gain initial access at State D, So this was through a proprietary Internet facing web application, which no other state had. Shortly after in August, this is where we saw APT41 gain initial access at the second state. Similar thing, proprietary web application, but this time it was a ASP.NET.

**Rufus Brown:**
Starting out around August. This is where we first saw the group conduct lateral movement and reconnaissance activities for around 4 to 5 months. So this is a really long time for a technically capable actor such as APT41 to remain active in environment and also really gain a better understanding of the network architecture as well as gain a stronger foothold on many systems across the network.

**Rufus Brown:**
At the beginning of the year. This is where we saw them first, laterally moved to the state benefits such as state benefit servers and also really conduct some hands on activity. So they started modifying with different ...