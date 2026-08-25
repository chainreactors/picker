---
title: The underscore that destroyed a life, and what it says about us
url: https://andreafortuna.org/2026/08/19/underscore-that-destroyed-a-life/
source: Instapaper: Unread
date: 2026-08-24
fetch_date: 2026-08-25T03:00:51.404368
---

# The underscore that destroyed a life, and what it says about us

[Andrea Fortuna](/)
[ ]

[About](/about/)[Search](/search/)

Tools

[DFIR Toolkit](https://dfir-toolkit.andreafortuna.org)
[OSINT Toolkit](https://osint-toolkit.andreafortuna.org)

# The underscore that destroyed a life, and what it says about us

Aug 19, 2026

by [Andrea Fortuna](/about/)

I read the story of Brandon Klayme twice, and the second time I found myself doing something I rarely do while reading about a legal case: I opened my own list of old accounts and started deleting things. Not because I was scared of ending up in an interrogation room. Because the case reminded me, with an almost physical discomfort, of how thin the thread is between “identified” and “convicted” once a chain of digital custody starts moving, and how little control any of us actually have over that thread once we’ve handed it to someone else years earlier.

![cover](/assets/2026/underscore-wrongful-conviction.jpg)

Klayme is a Canadian man from Dartmouth, Nova Scotia who spent eighteen months in prison and six years fighting an accusation of child luring and possession of child sexual abuse material. He was innocent. On July 23, 2026, the Nova Scotia Court of Appeal didn’t just quash his conviction, it went further and declared him “factually innocent,” ruling that he “should never have been charged, let alone convicted,” as the [New York Times reported](https://www.nytimes.com/2026/07/30/world/canada/wrongful-conviction-kik-username-underscore.html). The entire case against him rested on a single artifact: a username. And that username had one underscore too many, or too few, depending on which account you were looking at.

## In brief

* A Wisconsin investigation into a predator using the Kik username *“fus\_\_ro\_dah”* (two underscores) was misrecorded, and a subpoena went out for *“fus\_ro\_dah”* (one underscore) instead, according to the [CBC’s reporting on the court decision](https://www.cbc.ca/news/canada/nova-scotia/how-a-single-underscore-led-to-an-innocent-halifax-man-s-conviction-9.7283149).
* That single-underscore account belonged to Brandon Klayme, who had opened it years earlier and said he stopped using it around 2012.
* Kik answered the request accurately for the account it was actually asked about, and the identification chain (username to email to IP to subscriber) pointed straight at an innocent man.
* Klayme was arrested, tried, convicted, and imprisoned, with, as the [Halifax Examiner put it](https://www.halifaxexaminer.ca/morning-file/brandon-klaymes-wrongful-conviction-is-the-second-for-crown-prosecutor-melanie-perry/), “zero evidence against Klayme, none, not one iota.”
* His appeal lawyer, Zeb Brown, is the one who finally spotted the discrepancy and traced the real offender to an account tied to California, per [Gizmodo’s account of the ruling](https://gizmodo.com/how-a-single-typo-in-a-username-cost-an-innocent-man-18-months-of-his-life-2000792325).
* The case is a sharp reminder that closing dormant accounts is not just decluttering, it is a small but real way to reduce your exposure to this exact kind of error.

## When the chain of custody has no custodian

Every digital investigation textbook describes the same idealized workflow: identify the online handle, request subscriber data from the platform, correlate the email with an IP address, correlate the IP address with a physical subscriber, arrive at a name. I’ve walked this exact chain more times than I can count, usually from the other side, trying to attribute an intrusion or trace a threat actor. In my [FACT Attribution Framework](https://andreafortuna.org/2026/06/15/fact-attribution-framework/) I make a point of drawing a hard line between identification (device, account, action) and attribution (person, accountability), and treating any conflation of the two as an error, not a shortcut. Klayme’s case is that error playing out with a human being’s freedom on the line.

Wisconsin police found a Kik account, “fus\_\_ro\_dah”, exchanging illegal material with a minor. Somewhere between reading that username off a phone and typing it into a legal request to Kik, one underscore vanished. Kik, doing exactly what it was supposed to do, handed over subscriber data for the account it was actually asked about. Google supplied an IP address tied to that account’s email. Canadian police in Halifax subpoenaed the ISP for the subscriber behind that IP. Every single step in that chain was executed correctly, against the wrong input.

Nobody along that entire path stopped to ask an obvious question: does this identified person actually match anything else we know about the suspect? According to the Halifax Examiner’s detailed account, the search of Klayme’s devices found “no evidence found of any Kik account activity by Mr. Klayme during the time frame of the offences,” nor anything linking his Google account to the victim. No clever forgery, no sophisticated technical failure. Just a system that had every opportunity to catch a discrepancy and declined to look, the exact institutional failure I described in [The technology trap](https://andreafortuna.org/2025/10/01/confirmation-bias/), where confirmation bias lets an investigator stop looking the moment the first plausible answer arrives.

## Why a username is such a fragile anchor

There’s a detail in this case that deserves more attention than it usually gets: *“fus\_ro\_dah”* is not a random string. It’s a direct reference to the Unrelenting Force shout from *The Elder Scrolls V: Skyrim*, a game with tens of millions of players. To anyone unfamiliar with gaming culture, a string like that looks arbitrary enough to assume it would never be chosen independently by two different people. To anyone who has actually played Skyrim, it’s about as generic as choosing “admin” or “test123”. Cultural references get reused constantly, and the punctuation people insert around them (one underscore, two, a hyphen, nothing at all) is exactly the kind of low-entropy detail a human transcriber glosses over and an investigator should never treat as unique proof of identity on its own.

I’ve written before about how messy attribution gets even among professionals who are supposed to be rigorous about it. In [Threat actor naming conventions: a big mess](https://andreafortuna.org/2023/07/17/threat-actor-naming-conventions-a-big-mess/) I described how different vendors assign wildly different labels to the same intrusion set, and how easily that confusion propagates once it’s written into a report. Usernames in criminal investigations deserve at least the same skepticism that CTI analysts are trained to apply to a threat actor label, and in Klayme’s case they got none.

There’s also a darker footnote worth flagging: some legal commentators, including a [University of Calgary Faculty of Law analysis](https://ablawg.ca/wp-content/uploads/2026/08/Blog_GC_Wrongful_Conviction.pdf) of the ruling, have pointed out that as courts increasingly explore AI-assisted case review to cut through backlogs, this case previews a failure mode we haven’t solved yet: models built on statistical text similarity are excellent at finding patterns but not automatically good at noticing the one character that matters most.

## The part where I make you check your old accounts

Multiple outlets covering this story, from the New York Times to [news.com.au](https://www.news.com.au/technology/online/should-never-have-been-charged-innocent-man-thrown-behind-bars-over-an-underscore-mark/news-story/bf8b431276848eaf7a637f94715cd3e3), noted the same detail: Klayme said he had stopped using Kik around 2012, years before the offense even took place. The account had been dormant for the better part of a decade by the time it became the sole evidence in a criminal case against him.

A dormant account is not neutral. It’s a live data point sitting in someone else’s database, permanently associable with your email and your registration history, and you don’t control how long it’s retained or whether re...