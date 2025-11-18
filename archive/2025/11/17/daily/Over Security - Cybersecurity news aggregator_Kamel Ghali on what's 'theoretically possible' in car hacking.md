---
title: Kamel Ghali on what's 'theoretically possible' in car hacking
url: https://therecord.media/car-hacking-interview-kamel-ghali-click-here-podcast
source: Over Security - Cybersecurity news aggregator
date: 2025-11-17
fetch_date: 2025-11-18T03:14:54.596711
---

# Kamel Ghali on what's 'theoretically possible' in car hacking

![](https://recordedfuture.matomo.cloud/matomo.php?idsite=2&rec=1)

[![Cyber Security News  | The Record](https://cms.therecord.media/uploads/The_Record_Centered_9b27d79125.svg)](/)

* [Leadership](/news/leadership)
* [Cybercrime](/news/cybercrime)
* [Nation-state](/news/nation-state)
* [Influence Operations](/news/influence-operations)
* [Technology](/news/technology)

* [Cyber Daily®](https://therecord.media/subscribe)
* [Click Here Podcast](/podcast)

Go

Subscribe to The Record

[✉️ Free Newsletter](/subscribe)

![Click Here podcast art for car hacking episode](https://cms.therecord.media/uploads/format_webp/large_Click_Here_podcast_episode_286_car_software_5daade8b9b.jpg)

Illustration by Megan J. Goff

[Zach Hirsch](/author/zach-hirsch)November 17th, 2025

# Kamel Ghali on what's 'theoretically possible' in car hacking

*Kamel Ghali has spent his career thinking about what happens when a car stops being a car. A veteran “white hat” car hacker and penetration tester, the Japan-based Ghali has trained engineers and regulators in the United States, Japan, and the Middle East on how to spot and fix the kinds of flaws that can turn a vehicle into a rolling vulnerability.*

*He is the chief operating officer of [Kage Corporation](https://kage.engineering/) and director of automotive cybersecurity at AKATSUKI, a Japan-based nonprofit devoted to cyber education. He’s also a board member of the Car Hacking Village and a regular presence at DEF CON.*

*As legacy automakers race to act more like tech companies — pushing remote software updates to tweak performance, patch infotainment systems and add new features — Ghali argues they are being forced to confront security questions that Silicon Valley already has grappled with for years.*

*Ghali says the industry has made significant progress after some early, high-profile missteps. But as more software gets loaded into cars, new weaknesses emerge just as quickly. The Click Here podcast talked to him about that. The interview has been edited for length and clarity.*

**CLICK HERE: Do you remember the first car you ever hacked?**

**KAMEL GHALI:** I worked as a vehicle penetration tester for about three years when I first moved to Japan in 2020, so I did a lot of hacking on earlier Tesla Model 3s. The reverse engineering process is a big part of cybersecurity for cars, so I spent time learning which messages corresponded to what parts of the car and making applications that interact with the car through those network protocols. So the Tesla Model 3 is one that I'm definitely pretty comfortable with.

**CH: And when you say you were hacking Teslas, were you working on whole cars or pieces of it — certain systems?**

**KG:** When you're actually testing on behalf of a client — an automotive manufacturer or one of its suppliers — it’s very rare that you're testing a whole car at once. It's much more common that you'll test one component or one subsystem of a vehicle, because they'll do this testing during development before the full car is ready. So during those three years, I actually never did a full vehicle penetration test. We’d receive a system and we would be given a scope of attacks to perform, and we’d essentially analyze the system and report any vulnerabilities that we find and give the customer recommendations on how they can be remediated. Since those days, I haven't done as much hands-on car hacking with newer cars, just as a matter of the way my career has changed.  I got into management and I don't do as much hands-on stuff as I should anymore.

**CH: So we can’t say, “Kamel cut his teeth on Tesla Model 3s and now he’s hacking Cybertrucks”? [laughs]**

**KG:** I mean, you could say I moved on to paperwork, but that's not so interesting.

**CH: No, that definitely doesn’t sound as cool. But you’re still poking at cars, just in different places?**

**KG:** Yeah, I’ve lost my edge — although lately, I've been getting back into it and looking more at EV chargers and EV charging infrastructure as opposed to just the cars themselves. It’s all connected and there are vulnerabilities that go back and forth between them.

**CH: Let me ask this directly: How worried should drivers be that someone with malicious intent could develop the same hacking skills you have?**

**KG:** There’s good news and there's bad news. The bad news is that there is a lot of damage that can be done through reverse engineering the software in these vehicles, finding vulnerabilities, and then developing exploits. And there are many different damage scenarios that you can put into effect as an attacker, like eavesdropping or taking pictures of someone's home, or stealing their contacts from the head unit.

The absolute worst-case scenario is that, God forbid, someone hacks a car, or multiple cars, and causes them to crash into a building, or commits an act of terrorism or an assassination, God forbid. These are [theoretically very real possibilities](https://therecord.media/white-house-officials-meet-with-nations-industry-connected-cars). Practically very difficult, but still theoretical. But, I would say most criminals aren't interested in hurting people. A lot of cybercrime especially is done for financial gain. People want to make money. They're not as interested in hurting someone they don't know right now.

![kamel-ghali-click-here-podcast-interview.jpg](https://cms.therecord.media/uploads/format_webp/kamel_ghali_click_here_podcast_interview_de6dce5be0.jpg)

*Kamel Ghali. Image: Recorded Future News*

But the nature of the science that is cybersecurity is that people discover vulnerabilities in software and libraries and systems every day. They publish them, and we do our best to repair them. Cybersecurity operations are such a huge part of the automotive industry now because the industry is taking it very seriously. And the other piece of good news is that, to this day, there really has not been a lot of automotive cybercrime.

Now, to be fair, ransomware of a vehicle is a very real threat. When it becomes possible, it'll probably happen at least once, and it has potentially really severe consequences, as I'm sure you can imagine. What if all the ambulances or police cars in the city got ransomware, and couldn't drive unless you paid 200 bitcoin? But at least until now, there have been no confirmed reported incidents of a car being hacked to cause damage to someone's life or property. The examples of cyber crime, or the intelligent systems in vehicles being targeted, are mostly related to vehicle theft. Like the [Kia Boyz](https://www.motortrend.com/features/kia-boyz-tiktok-viral-video-car-theft-history) – they're not interested in hurting someone.

But the reality is that, yeah, these things are theoretically possible when you have a smart system that is connected to the world around it and is also connected to the safety-critical controls of your vehicle. That theoretical reality can never be ignored.

**CH: We’ve heard safety advocates argue for stronger air gaps — clearer separations between safety-critical systems and the “fun stuff,” like your Bluetooth and touchscreen. Does that hold up in practice?**

**KG:** I agree 100 percent. And I think that the change has been a little bit slow, it's taken some time, but over the last few years the automotive industry has come around to sharing that same sentiment.

If you think about traditional cybersecurity from an IT or enterprise perspective, network segmentation is one of the most fundamental security practices you can implement to mitigate the potential damage or the impact that any compromise can lead to. And when you think about things like [zero trust](https://www.gsa.gov/technology/it-contract-vehicles-and-purchasing-programs/it-security/zero-trust-architecture), and making sure that even if something is compromised, you're able to limit the damage — the same principle exists of separating critical networks from those that are exposed to the outside.

So, the infot...