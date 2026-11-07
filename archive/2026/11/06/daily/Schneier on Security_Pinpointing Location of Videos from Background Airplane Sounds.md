---
title: Pinpointing Location of Videos from Background Airplane Sounds
url: https://www.schneier.com/blog/archives/2026/11/pinpointing-location-of-videos-from-background-airplane-sounds.html
source: Schneier on Security
date: 2026-11-06
fetch_date: 2026-11-07T08:02:00.712214
---

# Pinpointing Location of Videos from Background Airplane Sounds

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

## Pinpointing Location of Videos from Background Airplane Sounds

This is [fascinating](https://gizmodo.com/a-youtuber-figured-out-how-to-find-almost-anyone-using-airplane-sounds-2000835861):

> The video describes a technique that can reveal where an otherwise unidentifiable recording was made by analyzing its audio for the faint sounds of passing aircraft. The technique is both fascinating and frightening.
>
> It works by looking at Doppler curves, which plot the way a plane’s sound changes as it passes overhead because of the Doppler effect. This is the same familiar Doppler effect that causes the frequency of a siren to rise as it approaches and then fall as it passes by and moves away. More generally, it’s the phenomenon whereby the frequency of a wave perceived by an observer changes when the observer and the source of the wave are moving in relation to one another.
>
> […]
>
> It’s sound that’s relevant here, though, and specifically the sound of aeroplanes. Early in his video, Colsto brings up a map of the flights that were in the air at the time the video he’s tracing was recorded. Much of this information is publicly available. Aircraft equipped with Automatic Dependent Surveillance–Broadcast (ADS-B) transmit data about their position, velocity, and altitude, which flight-tracking services collect and make available to the public. While not every plane is tracked, the system provides an enormous amount of information about aircraft movements.

Tags: [air travel](https://www.schneier.com/tag/air-travel/), [geolocation](https://www.schneier.com/tag/geolocation/), [videos](https://www.schneier.com/tag/videos/)

[Posted on November 6, 2026 at 9:57 AM](https://www.schneier.com/blog/archives/2026/11/pinpointing-location-of-videos-from-background-airplane-sounds.html) •
[6 Comments](https://www.schneier.com/blog/archives/2026/11/pinpointing-location-of-videos-from-background-airplane-sounds.html#comments)

### Comments

Wicked Lad •
[November 6, 2026 12:16 PM](https://www.schneier.com/blog/archives/2026/11/pinpointing-location-of-videos-from-background-airplane-sounds.html/#comment-459475)

At the risk of stating the obvious, it seems this would also be useful in evaluating the likelihood that a video was taken where and when it is purported to have been taken.

Clive Robinson •
[November 6, 2026 1:03 PM](https://www.schneier.com/blog/archives/2026/11/pinpointing-location-of-videos-from-background-airplane-sounds.html/#comment-459476)

@ ALL,

The idea is not exactly new as the concrete sound mirrors on the UK south coast from WWII will evidence.

But it goes back even further to attempts in WW1 to track submarines around the UK Coast, that has developed into a system to detect Russian subs as they go around various parts of Europe to get into the Atlantic.

But from another aspect there is the use of “mains hum” on recorded audio giving a very precise time indicator.

The problem with the idea is that you need a “starting location” as well as “time”. It’s the same problem that current “Global Navigation Satellite Systems”(GNSS) have,

<https://www.advancednavigation.com/tech-articles/global-navigation-satellite-system-gnss-and-satellite-navigation-explained/>

You have to solve a series of time / distance based “triangles” whilst also allowing for the propagation speed of the signals which is of course variable… Not just due to Doppler Shift but the characteristics of the communications channel.

The technique is generally known as “Trilateration”,

<https://en.wikipedia.org/wiki/Trilateration>

And starts with an assumption of a starting point location and time then iteratively work through untill you get a probable location match then keep refining untill you confirm and get the desired accuracy.

Interestingly you can do similar with VHF and UHF transmissions from broadcast stations or “Private Mobile Radio”(PMR) or “Ham/Amateur Radio”.

Basically the signals bounce of aircraft, and get crossmodulated by the aircraft physical movement with respect to the receiver.

As far as I’m aware this was first demonstrated in Britain by a couple of amateur radio engineers that gave rise to RADAR.

The credit for which was stolen by Robert Watson[1], who later hyphenated Watt to his family name.

The official story is two men were Robert Watson-Watt and Arnold Wilkins, drove into a field near the BBC transmitters at Daventry and set up a couple of antennas and using an oscilloscope detected reflections off of a Bomber flying by.

The reality is others had discovered the effect and talked about it and it got to the ears of Arnold Wilkins who was Watson’s assistant. But the only reason Robert Watson got involved was of his job measuring atmospheric effects we now call “propagation”[2] People in the Air Ministry were informed about the effect of bouncing signals off of aircraft and identifying their direction and they then asked for it to be investigated. Thus the job fell to Watson because he was on the public pay role in the nearest relating research role…

This much can be confirmed because of the flight of the bomber, was “officially arranged” before the supposed “experiment” that was in reality just a “demonstration” of what had been established experimentally by others some time before.

[1] During WWII my mother had the misfortune to work with Robert Watson-Watt… She really did not have a good word to say about him, and had quite a few stories about his appalling behaviours.

[2] Robert Watson does however have one claim to fame, he named the “ionosphere” whilst working for the Met Office in Slough South England that was the early location for the National Physics Laboratory. Where he was supposedly trying to track weather by lightening storm. Something he finally actually succeeded at doing, however it had problems due to the fact “the antenna could not be swung fast enough”. This was solved by the patented in 1919 work of British radio engineer Frank Adcock, who whilst an Army officer in the British Expeditionary Force”(BEF) in France invented what became named “The Adcock aerial / antenna array”. But it was in of it’s self still incapable of getting the direction fast enough. This was solved by acquiring an X/Y display Oscilloscope from the US. It was this system that was taken to the field in Daventry…

Confused •
[November 6, 2026 5:52 PM](https://www.schneier.com/blog/archives/2026/11/pinpointing-location-of-videos-from-background-airplane-sounds.html/#comment-459479)

if one were to wipe all metadata, which includes the time when video was shot, what would then be the indicator of time-frame correlating to any flights?

lurker •
[November 6, 2026 7:27 PM](https://www.schneier.com/blog/archives/2026/11/pinpointing-location-of-videos-from-background-airplane-sounds.html/#comment-459481)

“The technique is both fascinating and frightening.”

Yet another first world problem solved – or is...