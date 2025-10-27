---
title: Millions of Vehicles Could Be Hacked and Tracked Thanks to a Simple Website Bug
url: https://www.wired.com/story/kia-web-vulnerability-vehicle-hack-track/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-28
fetch_date: 2025-10-06T18:30:34.732005
---

# Millions of Vehicles Could Be Hacked and Tracked Thanks to a Simple Website Bug

[Skip to main content](#main-content)

Menu

[![Wired](/verso/static/wired-us/assets/logo-onenav-reverse.svg)](/)

[SECURITY](/category/security/)

[POLITICS](/category/politics/)

[THE BIG STORY](/category/big-story/)

[BUSINESS](/category/business/)

[SCIENCE](/category/science/)

[CULTURE](/category/culture/)

[REVIEWS](/category/gear/)

Menu

[![Wired](/verso/static/wired-us/assets/logo-onenav-reverse.svg)](/)

Account

Account

[Newsletters](/newsletter?sourceCode=navbar)

[Security](/category/security/)

[Politics](/category/politics/)

[The Big Story](/category/big-story/)

[Business](/category/business/)

[Science](/category/science/)

[Culture](/category/culture/)

[ReviewsChevron](/category/gear/)

MoreExpand

[The Big Interview](/the-big-interview/)[Magazine](/magazine/)[Events](/tag/wired-events/)[WIRED Insider](/collection/wiredinsider/)[WIRED Consulting](/tag/wired-consulting/)

[Newsletters](/newsletter?sourceCode=navbar)

[Podcasts](/podcasts/)

[Video](/video/)

[Merch](https://shop.wired.com/)

[SearchSearch](/search/)

[Sign In](/auth/initiate?redirectURL=%2Fstory%2Fkia-web-vulnerability-vehicle-hack-track%2F&source=VERSO_NAVIGATION)

[Sign In](/auth/initiate?redirectURL=%2Fstory%2Fkia-web-vulnerability-vehicle-hack-track%2F&source=VERSO_NAVIGATION)

By [Andy Greenberg](/author/andy-greenberg/)

[Security](/category/security)

Sep 26, 2024 7:00 AM

# Millions of Vehicles Could Be Hacked and Tracked Thanks to a Simple Website Bug

Researchers found a flaw in a Kia web portal that let them track millions of cars, unlock doors, and start engines at will—the latest in a plague of web bugs that’s affected a dozen carmakers.

![Cars hacking key laptop theft data entry](https://media.wired.com/photos/66f3f6ed689e6a75998adbf2/3:2/w_2560%2Cc_limit/CarHacking%2520(1).gif)

Photo illustration: WIRED Staff; Getty images

Save StorySave this story

Save StorySave this story

When security researchers in the past found ways to hijack vehicles' internet-connected systems, their proof-of-concept demonstrations tended to show, thankfully, that hacking cars is hard. Exploits like the ones that hackers used to remotely take over a [Chevrolet Impala in 2010](https://www.wired.com/2015/09/gm-took-5-years-fix-full-takeover-hack-millions-onstar-cars/#:~:text=7%3A00%20AM-,GM%20Took%205%20Years%20to%20Fix%20a%20Full%2DTakeover%20Hack,known%20remote%20car%20hacking%20technique.) or a [Jeep in 2015](https://www.wired.com/2015/07/hackers-remotely-kill-jeep-highway/) took years of work to develop and required ingenious tricks: reverse engineering the obscure code in the cars’ telematics units, delivering malicious software to those systems via audio tones played over radio connections, or even putting a disc with a malware-laced music file into the car’s CD drive.

This summer, one small group of hackers demonstrated a technique to hack and track millions of vehicles that’s considerably easier—as easy as finding a simple bug in a website.

Today, a group of independent security researchers [revealed](https://samcurry.net/hacking-kia) that they'd found a flaw in a web portal operated by the carmaker Kia that let the researchers reassign control of the internet-connected features of most modern Kia vehicles—dozens of models representing millions of cars on the road—from the smartphone of a car’s owner to the hackers’ own phone or computer. By exploiting that vulnerability and building their own custom app to send commands to target cars, they were able to scan virtually any internet-connected Kia vehicle’s license plate and within seconds gain the ability to track that car’s location, unlock the car, honk its horn, or start its ignition at will.

After the researchers alerted Kia to the problem in June, Kia appears to have fixed the vulnerability in its web portal, though it told WIRED at the time that it was still investigating the group’s findings and hasn’t responded to WIRED’s emails since then. But Kia’s patch is far from the end of the car industry’s web-based security problems, the researchers say. The web bug they used to hack Kias is, in fact, the second of its kind that they’ve reported to the Hyundai-owned company; they found a similar technique for hijacking Kias' digital systems last year. And those bugs are just two among a [slew of similar web-based vulnerabilities they’ve discovered within the last two years](https://samcurry.net/web-hackers-vs-the-auto-industry) that have affected cars sold by Acura, Genesis, Honda, Hyundai, Infiniti, Toyota, and more.

“The more we’ve looked into this, the more it became very obvious that web security for vehicles is very poor,” says Neiko “specters” Rivera, one of the researchers who both found the latest Kia vulnerability and worked with a larger group responsible for the previous collection of web-based car security issues revealed in January of last year.

“Over and over again, these one-off issues keep popping up,” says Sam Curry, another member of the car hacking group, who works as a security engineer for Web3 firm Yuga Labs but says he did this research independently. “It's been two years, there's been a lot of good work to fix this problem, but it still feels really broken.”

## Read a License Plate, Hack a Car

Before they alerted Kia to its latest security vulnerability, the research group tested their web-based technique on a handful of Kias—rentals, friends’ cars, even cars on dealer lots—and found that it worked in every case. They also showed the technique to WIRED, demonstrating it on the 2020 Kia Soul of a security researcher introduced to them just minutes earlier in a parking lot in Denver, Colorado, as seen in the video above.

The group’s web-based Kia hacking technique doesn’t give a hacker access to driving systems like steering or brakes, nor does it overcome the so-called immobilizer that prevents a car from being driven away, even if its ignition is started. It could, however, have been combined with immobilizer-defeating techniques popular among car thieves or used to steal lower-end cars that don't have immobilizers—[including some Kias.](https://www.motortrend.com/news/hyundai-fixing-kia-boys-theft-security-vulnerability-free/)

Even in cases when it didn't allow outright theft of a car, the web flaw could have created significant opportunities for theft of a car's contents, harassment of drivers and passengers, and other privacy and safety concerns.

“If someone cut you off in traffic, you could scan their license plate and then know where they were whenever you wanted and break into their car,” says Curry. “If we hadn’t brought this to Kia’s attention, anybody who could query someone’s license plate could essentially stalk them.” For Kias that come installed with a 360-degree camera, that camera, too, was accessible to hackers. Beyond allowing the hijacking of connected features in cars themselves, Curry says, the web portal flaw also allowed hackers to query a broad range of personal information about Kia customers—names, email addresses, phone numbers, home addresses, and even past driving routes in some cases—a potentially massive data leak.

The Kia hacking technique the group found works by exploiting a relatively simple flaw in the backend of Kia's web portal for customers and dealers, which is used to set up and manage access to its connected car features. When the researchers sent commands directly to the API of that website—the interface that allows users to interact with its underlying data—they say they found that there was nothing preventing them from accessing the privileges of a Kia dealer, such as assigning or reassigning control of the vehicles' features to any customer account they created. “It’s really simple. They weren't checking if a user is a dealer,” says Rivera. “And that's kind of a big issue.”

Kia's web portal allowed lookups of cars based on their vehicle identification number (VIN). But the hackers found they could quickly find a car's VIN after obta...