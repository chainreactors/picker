---
title: How to perform a DDoS attack simulation
url: https://www.rtcsec.com/article/how-to-perform-ddos-simulation/
source: Real-time communications security on Communication Breakdown - Real-Time Communications Security
date: 2022-11-30
fetch_date: 2025-10-04T00:05:03.184706
---

# How to perform a DDoS attack simulation

[Skip to main content](#content)

[![Enable Security logo](https://www.enablesecurity.com/assets/img/logo-header-white.min.ac2c259ad95c9e369b3d7e44d9986a07c2c45fec663fbceaefe184e92011793a.svg)](/)

* [Get in touch](/contact/)

* Security Testing
  + [VoIP Penetration Testing](/voip-penetration-testing/)
  + [WebRTC Penetration Testing](/penetration-testing/)
  + [VoIP Security Assessment](/voip-security-assessment/)
  + [DDoS Resilience Testing](/ddos-testing/)
  + [Code & Config Analysis](/code-and-config-analysis/)
  + [Fuzz Testing](/fuzz-testing/)
* [SIPVicious](/sipvicious/)
* [Consultancy](/consultancy/)
* [Research](/research/)
* [Blog](/blog/)
* [Newsletter](/newsletter/)
* [About](/about/)
* [Contact](/contact/)

![Sandro Gauci](https://www.enablesecurity.com/assets/img/sandro-thumb_hubedf31446211def026ce81cb6e7c2636_36362_60x60_resize_q75_box.jpg)

[**Sandro Gauci**](#author-sandrogauci), Enable Security

# How to perform a DDoS attack simulation

Published on Nov 29, 2022
in
*[denial of service](https://www.enablesecurity.com/tags/denial-of-service/)*,
*[voip security](https://www.enablesecurity.com/tags/voip-security/)*

### TL;DR

A DDoS simulation is a practical exercise that various organisations are capable of doing. Understand the reasons why you would want to do this, then combine custom with off-the-shelf attack tools. Follow the best practices, apply solutions and mitigation; and you can finally answer: *what if we got attacked*?

### Introduction

In this post, we give an overview of how you too can perform your own distributed denial of service (DDoS) simulation exercises. We focus on attacking real-time communications systems because this is an area where DoS attacks can really cause damage. But the instructions and ideas outlined in this text will apply to any system in general that you might need to test. Even if in this article we do not really focus on the defensive side of protecting against DoS, ultimately the goal is to design and implement solutions that actually work for the systems and applications that need to be protected.

If you would rather watch a presentation or go through the slides, we gave a talk on this very topic at TADSummit 2023 in Portugal. The video can be watched on [Youtube](https://www.youtube.com/watch?v=gaVBOuwyON0), and the slides are also available [here](https://www.slideshare.net/sandrogauci/tadsummit-2022-how-to-bring-your-own-rtc-platform-down).

## Why would you want to attack your own services?

The answer surely has to be that this is a great way to have some dangerous fun! It is indeed an entertaining thing to do and can lead to some interesting and often unexpected results.

![Pinky and the Brain](pinky-and-the-brain.png)

Seriously though, the real reason tends to be that of finding out how your critical services are going to react during a DDoS attack. The exercise that we are about to describe might be an important part of the answer to the question: *what if we got attacked*? The aim is to create a system that can, within reasonable effort, withstand most attacks that might be launched against your business.

If no security protection is in place for DoS, then you might want to see how dangerous this is for your particular business. *How bad does it get*? A [DDoS simulation exercise](https://www.enablesecurity.com/ddos-testing/) will give you an answer.

In many cases where service availability is critical, organisations will have some form of protection mechanism. Either that, or they will rely on technologies that are able to withstand such attacks. It is often a matter of a hybrid approach with some things being better protected than others. In such cases, you will want to do such an exercise to find out which protection mechanisms actually work. Protection mechanisms are often in place but rarely ever properly tested. Until you test, you should really not make any assumptions as to their robustness. What often happens, unfortunately, is that service providers find out about their weaknesses during an actual attack. This is far from ideal - you can certainly do better by simulating such attacks.

Another very good reason is to evaluate a security solution that claims to protect against DDoS attacks. How well does it work? Perhaps you are comparing two or more solutions - which one works better in your situation? A DDoS simulation will provide some important answers there.

Finally, almost all DoS protection mechanisms fail at some point. Perhaps the security solution looks for particular patterns, but the attacks can be modified slightly leading to a bypass. Or network traffic bursts are not handled well by the security mechanisms in place. Or the attack can be slow enough to bypass protection mechanisms that rely on blocking high packet rates. Every organisation has limitations - bandwidth, system resources, application efficiency and bugs. The point is to understand if your current protection level is sufficient against the current state of affairs. And also - to understand how well your people can handle such an attack. What sort of incident response capabilities do you have?

A threat modelling approach can help here. You need to identify:

* what are your most critical services?
* are they exposed to DDoS attacks?
* what do we need to do to protect against these attacks?

## Preparing for destruction

Once you have convinced yourself as to why you should simulate a DDoS attack, it is time to start making preparations for such a test.

Firstly, one has to decide what to attack and what sort of attacks to simulate. For example, you are likely to have to choose between or combine the following:

* bandwidth saturation
* protocol specific attacks
* application attacks

If you are attacking specific applications you will want to do some initial tests to explore which parts of that application should be attacked. In general, you may want to look for:

* errors, especially if generated during fuzzing
* slow responses
* increase in memory consumption (even if it is a slight increase)

For example, if your target is an API or even a SIP server, you are very likely to simply flood the target with POST or REGISTER messages. But if you are testing a specific application, you will want to make sure that the targeted functionality is being reached. With an API target, it might be that you are testing an API call which triggers a callback. You will want to have the full workflow fully functional and set up a callback handler. In the case of a SIP server, perhaps there is a voicemail application - you will want to call a specific number, and often will need to authenticate that call.

Next thing you’ll need is some attack tools. If your aim is to see how bandwidth saturation affects you, or to do generic protocol attacks, then standard or simple tools are often enough. What is important is that the attack tools are more efficient than the target application. Often such applications simply generate traffic, perhaps replaying messages. Two useful features to look for in terms of attack tools are:

* rate limiting
* concurrency (especially for handling multiple sockets or connections)

It is also nice to have the ability to distribute the source IP for systems that have more than one IP assigned to them. And it is great when tools offer flexibility, through the combination of different techniques. For example, a tool can offer the option of closing the connection on sending (or receiving) each message versus keeping the connection open. Such a tool may also have the ability to use various different SIP or HTTP methods.

The following is an example of such a tool, written in Go that floods a SIP target with OPTIONS messages:

```
package main

import (
	"log"
	"net"
)

func flood() {
	payload := "OPTIONS sip:demo.sipvicious.pro SIP/2.0\r\n" +
		"Content-Length: 0\r\n\r\n"
	b := make([]byte, 1024)

	for {
		c, err := net.Dial("udp", "demo.sipvicious.pro:5060")
		if err != nil { log.Fatal(err) ...