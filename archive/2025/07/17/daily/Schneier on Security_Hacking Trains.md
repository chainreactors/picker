---
title: Hacking Trains
url: https://www.schneier.com/blog/archives/2025/07/hacking-trains.html
source: Schneier on Security
date: 2025-07-17
fetch_date: 2025-10-06T23:54:57.872856
---

# Hacking Trains

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Hacking Trains

Seems like an old system [system](https://gizmodo.com/hackers-can-tamper-with-train-breaks-using-just-a-radio-feds-warn-2000629522) that predates any care about security:

> The flaw has to do with the protocol used in a train system known as the End-of-Train and Head-of-Train. A Flashing Rear End Device (FRED), also known as an End-of-Train (EOT) device, is attached to the back of a train and sends data via radio signals to a corresponding device in the locomotive called the Head-of-Train (HOT). Commands can also be sent to the FRED to apply the brakes at the rear of the train.
>
> These devices were first installed in the 1980s as a replacement for caboose cars, and unfortunately, they lack encryption and authentication protocols. Instead, the current system uses data packets sent between the front and back of a train that include a simple BCH checksum to detect errors or interference. But now, the CISA is warning that someone using a software-defined radio could potentially send fake data packets and interfere with train operations.

Tags: [hacking](https://www.schneier.com/tag/hacking/), [infrastructure](https://www.schneier.com/tag/infrastructure/), [transportation](https://www.schneier.com/tag/transportation/)

[Posted on July 16, 2025 at 12:57 PM](https://www.schneier.com/blog/archives/2025/07/hacking-trains.html) •
[12 Comments](https://www.schneier.com/blog/archives/2025/07/hacking-trains.html#comments)

### Comments

wiredog •
[July 16, 2025 1:39 PM](https://www.schneier.com/blog/archives/2025/07/hacking-trains.html/#comment-446553)

“To exploit this issue, a threat actor would require physical access to rail lines, deep protocol knowledge, and specialized equipment”

All of which are easy to acquire. Physical access to rail lines? There are thousands of miles of rail lines without even a fence. Deep protocol knowledge? Probably published somewhere. Specialized equipment? Software defined radio boards are not hard to get, especially for raspberry pi devices.

humho •
[July 16, 2025 2:09 PM](https://www.schneier.com/blog/archives/2025/07/hacking-trains.html/#comment-446555)

And none of this is likely to be fixed until someone has died first. Because capitalism prioritizes profit over safety, and profits are only affected by a lawsuit. Which is why death is needed.

And BTW that “deep protocol knowledge” is unlikely to be any deeper than a “deep” knowledge of TCP/IP. In other words attainable to anyone with some patience and at least one working eyeball.

Clive Robinson •
[July 16, 2025 2:25 PM](https://www.schneier.com/blog/archives/2025/07/hacking-trains.html/#comment-446556)

@ Bruce, Wiredog, ALL,

With regards,

> “But now, the CISA is warning that someone using a software-defined radio could potentially send fake data packets and interfere with train operations.”

First of suitable “Software Defined Radios”(SDR) can be obtained for well less than $100 even with the madness that is tariffs.

But you can get suitable Boefang or similar 10Watt output hand helds covering much of the VHF and UHF bands these sorts of systems use for well less than $50.

You can get a directional Yagi or LPDA antenna with significant forward gain for less than $200

Then all you need is a laptop computer or smart device like a mobile phone and an appropriate application.

We already know that finding and exploiting protocols has already been done from the issues in Europe especially the one in Poland that stopped a lot of trains.

> *“In fact, the saboteurs appear to have sent simple “radio-stop” commands via radio frequency to the trains they targeted. Because the trains use a radio system that lacks encryption or authentication for those commands, Olejnik says, anyone with as little as $30 of off-the-shelf radio equipment can broadcast the command to a Polish train—sending a series of three acoustic tones at a 150.100 megahertz frequency—and trigger their emergency stop function.”*

<https://www.wired.com/story/poland-train-radio-stop-attack/>

The same is true for many other places not just the EU.

But it gets more fun when you know that old 2G GSM mobile radio is considered a standard for much automatic control not just of trains, but road signals, mobile cranes and much other industrial plant equipment…

None of it has encryption or sensible authentication and most of it is “plain text messages” with the only attempt at safety being using a simple “Cyclic Redundancy Checks”(CRC) and “Forward Error Correcting”(FEC) protocols…

SocraticGadfly •
[July 16, 2025 4:02 PM](https://www.schneier.com/blog/archives/2025/07/hacking-trains.html/#comment-446557)

“Shock me” that the railroad industry is that cheap. It’s shown this is the case for decades. Look at its continued fighting against safety-updating oil tank cars.

Train Of Fools •
[July 16, 2025 6:40 PM](https://www.schneier.com/blog/archives/2025/07/hacking-trains.html/#comment-446559)

I work in a closely related industry and can tell you this is just the tip of the freakin iceberg. Not just in the US (which is bad) but the world (which is worse). The attempts at retrofitting security into the protocols have been half-hearted due to limitations of legacy devices in the field, and the desire to squeeze ever increasing years of life out of them. There’s at least one part of the world that has a sizable fleet of heavy locomotives on a consumer cell data network running public accessible ancient ssh servers on them for mission/safety critical functionality

Clive Robinson •
[July 16, 2025 9:11 PM](https://www.schneier.com/blog/archives/2025/07/hacking-trains.html/#comment-446562)

@ humho, ALL,

When you said,

> “And BTW that “deep protocol knowledge” is unlikely to be any deeper than a “deep” knowledge of TCP/IP. In other words attainable to anyone with some patience and at least one working eyeball.”

You left off,

“The pocket change to buy a book or standard that gives the knowledge in a way specific to making it easily and viably usable…”

In practice I tend to “buy a book” first as in most cases it’s a lot less expensive and gives a much smoother journey and a better return on investment, not just of money but time as well.

Chris •
[July 17, 2025 11:19 AM](https://www.schneier.com/blog/archives/2025/07/hacking-trains.html/#comment-446572)

There’s a buried lede here from the CISA Threat Report Itself (emphasis mine):

“Cybersecurity researcher Neil Smith discovered the vulnerability back in 2012 while doing research for Industrial Control Systems Cyber Emergency Response Team (now a part of CISA). ***Due to a dispute over the validity of the vulnerability with the Association of American Railroads (AAR), the vulnerability did not get shared with the railway industry.*** Eric Reuter, the second researcher credited by CISA for finding the vulnerability, discovered the issue in ***2018*** and disclosed technical details at th...