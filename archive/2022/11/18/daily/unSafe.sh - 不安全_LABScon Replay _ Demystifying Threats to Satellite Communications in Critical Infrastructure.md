---
title: LABScon Replay | Demystifying Threats to Satellite Communications in Critical Infrastructure
url: https://buaq.net/go-136109.html
source: unSafe.sh - 不安全
date: 2022-11-18
fetch_date: 2025-10-03T23:05:16.920958
---

# LABScon Replay | Demystifying Threats to Satellite Communications in Critical Infrastructure

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

LABScon Replay | Demystifying Threats to Satellite Communications in Critical Infrastructure

Demystifying threats to satellite communications in critical infrastructure | MJ Emanuel: this mp4
*2022-11-17 22:23:28
Author: [www.sentinelone.com(查看原文)](/jump-136109.htm)
阅读量:27
收藏*

---

Demystifying threats to satellite communications in critical infrastructure | MJ Emanuel: [this mp4 audio file](https://sonix.ai/speech-to-text-all-supported-file-formats?utm_source=embed "Sonix's converts the most popular audio file formats to text") was [automatically transcribed by Sonix](https://sonix.ai/transcribe-audio?utm_source=embed "Sonix is the best way to transcribe audio files in 2022") with the [best speech-to-text algorithms.](https://sonix.ai/automated-transcription?utm_source=embed "The best speech-to-text algorithms") This transcript may contain errors.

**MJ Emanuel:**

I think this is something that we don't really fully understand. And so we just kind of like, say, that's scary, that's bad.

You know, there's a lot of, there is a lot of news and headlines about the wind turbine disruption after the ViaSat compromise.

But, you know, the wind turbines didn't actually stop producing energy. So I think we need to talk a little bit more about the nuance of when are data flows just interrupted and when is it visibility that's interrupted? And that's what I'm gonna try to do in this talk.

So my name is MJ Emanuel. I am on the ICS incident response team at CISA in the threat hunting subdivision, and I did kind of a mix of forensics and threat intelligence. I also will be teaching at the The Alperovitch Institute next semester about critical infrastructure and cyber.

So as I said, my you know, my goals for this talk are kind of to structure it around an incident response we had earlier this year at CISA for a SATCOM service provider. But I'm really going to be talking more about how data is generated in critical infrastructure and how it flows, because I think we need to understand like what's normal to talk about what how can we derive impacts from that? And then consequent driven impact analysis is really, really the key to this.

So this is something that's really been pushed by INL for the past couple of years. If you've heard of CCE, that's cyber. What is it, cyber-enabled, consequence-driven engineering? So it's something that's being talked about when we were talking about how do we design these systems. But I think it's something that we also need to bring about when we're analyzing these systems and thinking about threat intelligence for critical infrastructure.

So our incident kicked off just from an outside tip that there was suspicious activity in a telecommunications environment. So we initially attempted to perform victim notification to this telecom provider, and then we quickly realized that the impacted entity wasn't the telecommunications provider, it wasn't the owner of the IP, but it was who they are releasing it to and who they are releasing to was a satellite communications provider.

I think this was like a perfect "oh, no, what did we just get into?" example that kind of highlighted what happened later in this case, because I don't think anyone, any of us really can appreciate how convoluted the satellite services industry is.

There's been an insane amount of consolidation and an insane amount of mergers that make it really opaque, and it makes it really hard to drive change because there are so many players on the back end that are never, ever interacting with the end users that are subscribing to the services.

So just an example, we're going to be talking mostly about Inmarsat BGANs for this talk because that was the type of service that was impacted in the incident.

I'm going to talk about. So this is just one of the many different types of satellite services that people can use. And just for this specifically, basically, the satellites are owned by Inmarsat. There are basically only four of them. And the current generation, runs on the L band. And basically, like any of the data that's flowing, it is going to go to one of those satellites and then come back down to only six ground stations around the world.

So something that's always going to happen when you're talking about using satellite services is how does that data flow from one of those six access stations back to the end users?

Because I think a lot of us kind of think about satellites like radios. We think the data is just going to go up and then down, but that's absolutely not how it happens. And then that when that data is in transmission, there's a lot of opportunities for there to be risk. And then there's also just only three terminal manufacturers. So I'm not really going to talk about this, but when we talk about like, supply chain issues because there are so many vendors in this space, there's just also a lot of opportunity there for there to be risk.

So after we initially started talking to the actual entity that was impacted by this incident, we quickly learned that they did have customers in critical infrastructure.

**MJ Emanuel:**
So CISA has both the ICS cert and US Cert and Legacy Incident Response teams. That means that we're responsible for both critical infrastructure or really any private sector companies that want to come to us as well as federal agencies. And I think that kind of gives us a little bit of a bias because when a federal agency comes to us with an incident, it's very easy to realize that something we want to resource. But when a random service provider comes to us or we come to them, it's not something that's always going to be a priority.

One of the really big, I will say, lively debates about this incident was a lot of people thought that the service that was being provided was just going to be satellite phones, that it was just the phones and just talk communication that was being transmitted by these networks. Those absolutely not the case.

So I'm going to talk a little bit about like what is SCADA so we can kind of think about what exactly was being like, what was actually flowing through those environments. So I think we kind of interchanged a lot of terminology like like it's all the same, but actually, ICS and SCADA are not interchangeable.

So ICS Industrial Control Systems is kind of the larger like a bucket of term. And then SCADA: supervisory control and data acquisition really refers to a specific type. It refers to data or refers to systems that are over a large geographic area. The opposite of that would be a DCS system, a distributed control system. And that's really more like one specific location. So look at DCS is something you might see at like a specific power generation facility, something that like it's local, probably all wired. And then a SCADA system might be like power transmission, like lines over like millions of miles or not millions but miles of of data.

So and then this communication, it really is up to whoever engineered the system. You know, I've seen people lay fiber. I've seen people use migrate cellular satellite. It's really up to whoever designed the system. And then let's talk a little bit about what kind of data is being generated.

So if you look on the right side, these are kind of like the field devices that are going to be like the lowest level when we talk about like these are these are dumb systems, These are just like your temperature sensors, your pressure systems, like maybe a valve that opens or close.

And then the control of that system is going to be from the PLC, the programmable logic controller. So the data is either...