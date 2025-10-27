---
title: Continuous Glucose Monitoring
url: http://www.imperialviolet.org/2025/06/29/cgm.html
source: ImperialViolet
date: 2025-06-30
fetch_date: 2025-10-06T22:54:50.388389
---

# Continuous Glucose Monitoring

# [ImperialViolet](https://www.imperialviolet.org)

### [Continuous Glucose Monitoring](/2025/06/29/cgm.html) (29 Jun 2025)

Continuous glucose monitoring has been a thing for a while. It's a probe that sits just inside your body and measures blood glucose levels frequently. Obviously this is most useful for type 1 diabetics, who need to regulate their blood glucose manually.

(At this point, I would be amiss not to give a nod to the book [Systems Medicine](https://www.amazon.com/Systems-Medicine-Physiological-Circuits-Computational/dp/1032411856), which I think most readers would find fascinating. I can't judge whether it's correct or not, but it is a delightful exploration of a bunch of maladies from the perspective of differential equations.)

But CGMs have been both expensive and prescription-only. And I am not a diabetic, type 1 or otherwise. But technology and, more importantly, regulation have apparently marched on, and even in America I [can now buy a CGM](https://www.stelo.com/) for $50 that lasts for two weeks, over the counter. So CGM technology is now available to the mildly curious, like me.

The device itself looks like a thick guitar pick, and it comes encased inside a much larger lump of plastic that has a pretty serious-looking spring inside. It takes readings every 5 minutes but only transmits every 15 minutes. You need a phone to receive the data and, if the phone is not nearby, it will buffer some number of samples and catch up when it can. The instructions say to keep the phone nearby at all times, so I didn't test how much it will buffer beyond an hour or so.

I've got both an Android and an iPhone, but for this the iPhone was a more convenient device. So everything following probably applies to both ecosystems, but I've only tested it in one.

The app is well made, although you can feel the lawyers & regulators hovering over every part of it. It gives you instructions about how to “install” the sensor, which you do by holding the big lump of plastic with the spring over a suitable spot on your body and then pressing the button.

It's not a *large* needle, but it's not trivial either. There is a soupçon of cyberpunk about applying it to yourself in the bathroom but, honestly, my first thought after pressing the button and hearing the bang of the spring releasing was, “oh, it didn't work.” Because I didn't feel anything at all. But when I lifted the applicator away, there it was. And after a little while it started providing readings.

It's held in place with some sticky plastic, and you can shower with it on. After a week or two the plastic does start to get a bit messed up. Honestly, I would have preferred to have replaced cover every few days, but I only got one in the box.

I placed it on the upper arm as suggested in the instructions. I put it a little bit further around and I didn't have any problems laying down on that side.

What did I learn? In a couple of cases, meals that I thought would be fairly healthy (or at least not terrible) were pretty terrible. There'll be some things that I'll avoid eating more than I had before. In the bucket of “things that should have been obvious but the effect is still stronger than I thought”: exercise really works. Even a brisk walk resets my blood sugar quite significantly. And the [Hawthorne effect](https://en.wikipedia.org/wiki/Hawthorne_effect) works even when you're doing it to yourself.

The app does not seem to let you export the data. However, at least on iOS you can connect it to Apple Health. And Apple Health does let you export all of your data as a big XML file. So a little bit of Go code later, I have a CSV of everything it recorded and per-day averages and variations.

The sensor will stop working after 15 and a half days. It says exactly 15, but I think it will give you another half day to switch over to another sensor. It comes out easily, although the sticky residue takes some effort to get off the skin.

I did not switch to another sensor. I will probably do it again, but I'll give it a while since, as I expected, most of the insights that I think I'm going to get, I got fairly rapidly. Honestly, I think the gamification of not wanting to spike my blood sugar was perhaps the most effective part of it. I still think it's cool that this is a thing now.