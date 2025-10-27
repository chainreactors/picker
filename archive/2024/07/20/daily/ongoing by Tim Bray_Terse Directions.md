---
title: Terse Directions
url: https://www.tbray.org/ongoing/When/202x/2024/07/19/Short-Directions
source: ongoing by Tim Bray
date: 2024-07-20
fetch_date: 2025-10-06T17:42:33.408235
---

# Terse Directions

# Terse Directions

Search

This post describes a service I want from my online-map provider.
I’d use it all the time. Summary: When I’m navigating an area I already know about, don’t give me turn-by-turn, just
give me a short list of the streets to take.

I’ve been living in Vancouver for decades and, driving or cycling, know how to get almost anywhere. It helps that, like most
North American cities, we have a fairly regular north-south-east-west grid.
These days, when I’m going any distance by car, I get directions from Google Maps because it knows where the traffic is bad, and
the traffic is usually bad somewhere. But it gives me way more directions than I need. Let’s look at a concrete example.

[![Part of central and east Vancouver](vancouver-streets.png "Part of central and east Vancouver")](-big/vancouver-streets.jpg.html)

To follow the narrative, you’ll probably have to click to expand, and it’s pretty big. It may be easier
just to open
[the map](https://www.openstreetmap.org/#map=14/49.2698/-123.0918) in another window.
Map credit:
OpenStreetMap.

My place is near the bottom edge of this map off to the west, between Cambie and Main streets. I occasionally attend a meetup
at New Brighton Park, which is the little splodge of green at the very top right corner of the map, across the highway
from Hastings Racecourse. It’s on McGill street.
To get there, I have to go quite a distance both east and north. Candidates for north/south travel include
Main, Clark, Nanaimo, and Renfrew streets. Candidates for east/west include 12th, Broadway, 1st, and Hastings.

Right now, Google Maps insists on turn-by turn, with three warnings for each turn. It’s dumb and annoying and interrupts
whatever music or show I’m listening to.

What I want is to get in the car and say “Short directions to New Brighton Park” and have it say “Take Main to 12th to Nanaimo to
1st to Renfrew to McGill.” Then when I’m driving, I’d get one vocal warning a block out from each turn,
like “Next left on Nanaimo” or some such.

Of course, when I’m navigating in a strange place, I’d want the traditional turn-by-turn. Don’t know about you, but the bulk
of my navigation is in territory I know and mostly about avoiding traffic.

The OpenStreetMap data is public and good. Traffic data is… a problem. But for anyone who has it, you can have me for a
customer. Just learn to be terse.

---

**Updated: 2024/07/19**

---

## Contributions

Comment feed for ongoing:[![Comments feed](/ongoing/Feed.png)](/ongoing/comments.atom)

From: [Duncan Ellis](https://dunx.org)  (Jul 19 2024, at 16:52)

A similar feature I would like is "full directions after this point" when you drop a way point, because often I will know how to take the freeway to get to the right part of town but will need much more specific instructions closer to my destination if it's an unfamiliar place. Being able to choose the verbosity of directions to that point would be great - terse or none would be good there.

*[[link](#c1721433167.860285)]*

From: [DinoCats](http://Https://dinocats.org) (Jul 19 2024, at 17:39)

I feel your pain! I find myself commonly muting the voice instructions on google maps now, and just glancing at the screen to know what turn is coming up next. It’s works pretty well, with a well mounted phone location. Google maps also has an “alerts only” audio setting, which I feel should do what you’re looking for, but in practice it doesn’t seem to in my experience 🤷‍♂️

*[[link](#c1721435981.581035)]*

From: [Murray](http://jayshal.com) (Jul 19 2024, at 20:32)

OMG yes! I'd like this option and another that only gives me directions at the far end of the journey - I quite often find I can get across the city to the suburb just fine on my own but want some help once I get there.

*[[link](#c1721446364.387661)]*

From: [Carlana](http://) (Jul 19 2024, at 21:33)

The flip side of Duncan’s comment, I often wish I could mark the route between the highway and my house as a “just turn yourself off” zone. I know how to get from the highway to home, tyvm!

*[[link](#c1721449993.565330)]*

From: [David Singer](https://readthisblog.net) (Jul 19 2024, at 22:10)

I would love to be able to have terse directions on the screen, too. It’s annoying when I get onto a freeway on-ramp and the only information on the screen tells me to “merge in 400 feet” - I don’t really have a lot of choice at that point, do I?

I’d much rather know what to expect AFTER I have made the mandatory merge - will I be staying on the highway for a few exits or getting off right away?

*[[link](#c1721452202.199128)]*

From: [Karl Voit](https://karl-voit.at) (Jul 21 2024, at 07:35)

I always wanted an option in OSM And (<https://osmand.net/>) to omit all voice messages in a radius I'd like to define.

For example, I don't want any message within 5km of range of my home (or a set of coordinates).

Maybe I'll write down a feature request for that ...

*[[link](#c1721572511.263522)]*

From: [Henrique Koehler](http://www.volksnav.de) (Jul 25 2024, at 01:50)

The article didn't consider imaginary clocks, see

- video www.volksnav.de/aSimpleCircle

- www.volksnav.de/Vancouver.

I'd appreciate if you would publish this alternative which soldiers, boy scouts, the blind, pilots etc. use for more than 100 years.

Henrique / Munich Orientation Convention

volksnav@volksnav.de

*[[link](#c1721897415.111404)]*

From: [AlanL](http://) (Jul 30 2024, at 05:55)

I sometimes have the opposite problem: the directions assume familiarity with somewhere I've never been before in my life. "In three hundred metres turn left onto Presidente Alvarez Boulevard (which you've never heard of before in your life, and the nameplate, even if visible, might be in a script you can't even read)", where "take the third left in three hundred metres" would actually be useful.

The problem is compounded by the fact that I don't live in an English speaking country, and many navigation apps' pronunciation of non-English street names is comically bad.

*[[link](#c1722344127.450051)]*

From: [Nik](http://) (Aug 18 2024, at 13:17)

Totally agree, honestly I think there's lots of missing innovation in mapping, but I've got to assume that the features like the one you've suggested are simply not "killer" enough that you might use an upstart new mapping service that had worse base mapping data but fancy features.

Other features I'd love:

\* I'm going somewhere new or driving on unfamiliar roads. I'll happily take a longer route if it's "simpler", where simpler might mean fewer turns or fewer "complex turns" where a complex turn invokes a squirrely intersection or a five way intersection.

\* Similarly, some tradeoff between how much longer I'm willing to wait for a less complex route. E.g. I'm willing for a route to take up to 10 mins longer if it just goes in a straight line instead of dodging through back streets.

\* Conversely, sometimes I don't want to get stuck in traffic and I'd prefer the backstreets so that I can just keep moving.

\* No/reduced left (for right side driving, right for left side driving countries) turn mode for peak hour where turning left across traffic can be a nightmare.

\* Also for driving on unfamiliar roads: extra notice mode, which will remind me well ahead of time which turn is next and in which direction so that I can get in the correct lane.

*[[link](#c1724012249.477069)]*

[ongoing](https://www.tbray.org/ongoing/)

[What this is](/ongoing/WhatItIs) ·
[![Subscribe to ongoing](/ongoing/Feed.png "Subscribe to ongoing")](/ongoing/ongoing.atom)
[Truth](/ongoing/Truth) ·
[Biz](/ongoing/Biz) ·
[Tech](/ongoing/Tech)

[author](/ongoing/misc/Tim) ·
[Dad](http://www.textuality.com/BillBray/)
[colophon](/ongoing/misc/Colophon) ·
[rights](/ongoing/misc/Copyright)

---

[July](/ongoing/When/202x/2024/07/) [19](/ongoing/When/202x/2024/07/19/), [2024](/ongoing/When/202x/2024/)
 · [Technology](/ongoing/What/Technology) (90 fragments)

 · · [Software](/ongoing/What/Technology/Software...