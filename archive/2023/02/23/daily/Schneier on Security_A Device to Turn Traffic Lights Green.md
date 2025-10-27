---
title: A Device to Turn Traffic Lights Green
url: https://www.schneier.com/blog/archives/2023/02/a-device-to-turn-traffic-lights-green.html
source: Schneier on Security
date: 2023-02-23
fetch_date: 2025-10-04T07:54:20.076285
---

# A Device to Turn Traffic Lights Green

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

## A Device to Turn Traffic Lights Green

Here’s a [story](https://www.thedrive.com/news/hacker-uncovers-how-to-turn-traffic-lights-green-with-flipper-zero) about a hacker who reprogrammed a device called “Flipper Zero” to mimic Opticom transmitters—to turn traffic lights in his path green.

> As mentioned earlier, the Flipper Zero has a built-in sub-GHz radio that lets the device receive data (or transmit it, with the right firmware in approved regions) on the [same wireless frequencies as keyfobs and other devices](https://www.thedrive.com/tech/i-tried-the-honda-keyfob-hack-on-my-own-car-it-totally-worked). Most traffic preemption devices intended for emergency traffic redirection don’t actually transmit signals over RF. Instead, they use optical technology to beam infrared light from vehicles to static receivers mounted on traffic light poles.
>
> Perhaps the most well-known branding for these types of devices is called [Opticom](https://www.gtt.com/). Essentially, the tech works by detecting a specific pattern of infrared light emitted by the Mobile Infrared Transmitter (MIRT) installed in a police car, fire truck, or ambulance when the MIRT is switched on. When the receiver detects the light, the traffic system then initiates a signal change as the emergency vehicle approaches an intersection, safely redirecting the traffic flow so that the emergency vehicle can pass through the intersection as if it were regular traffic and potentially avoid a collision.

This seems easy to do, but it’s also very illegal. It’s called “impersonating an emergency vehicle,” and it comes with hefty penalties if you’re caught.

Tags: [cars](https://www.schneier.com/tag/cars/), [impersonation](https://www.schneier.com/tag/impersonation/), [police](https://www.schneier.com/tag/police/), [radio](https://www.schneier.com/tag/radio/)

[Posted on February 22, 2023 at 7:30 AM](https://www.schneier.com/blog/archives/2023/02/a-device-to-turn-traffic-lights-green.html) •
[25 Comments](https://www.schneier.com/blog/archives/2023/02/a-device-to-turn-traffic-lights-green.html#comments)

### Comments

Winter •
[February 22, 2023 8:09 AM](https://www.schneier.com/blog/archives/2023/02/a-device-to-turn-traffic-lights-green.html/#comment-418185)

> It’s called “impersonating an emergency vehicle,” and it comes with hefty penalties if you’re caught.

And it rightfully does!

aserraric •
[February 22, 2023 8:28 AM](https://www.schneier.com/blog/archives/2023/02/a-device-to-turn-traffic-lights-green.html/#comment-418188)

As the article points out, this is not something particular to the Flipper Zero (which is a neat little device), but could have just as well haven been built with an Arduino board or even some discreet logic, if one was so inclined.

I’m afraid that the take away for far too many people will not be “It’s too easy to spoof being a emergency vehicle” and instead turn to “this hacking device should be made illegal!”

Count0 •
[February 22, 2023 8:42 AM](https://www.schneier.com/blog/archives/2023/02/a-device-to-turn-traffic-lights-green.html/#comment-418190)

Of course this system isn’t perfect. There was a case in Minneapolis where light rail trains use this technology to keep from stopping at grade crossings but there was confusion on the part of emergency responders about who had priority at any given light if they used theirs at the same time a train did. They thought emergency vehicles took priority. They were wrong and an ambulance got hit by the train.

Peter A. •
[February 22, 2023 9:15 AM](https://www.schneier.com/blog/archives/2023/02/a-device-to-turn-traffic-lights-green.html/#comment-418195)

There are a lot of systems which use unauthenticated “secret” signals to perform automatic actions. The assumption was that the system shall be simple so it “always works”, but shall be kept secret so it won’t be abused by unintended persons. There might be also an assumption that nobody (or very few people) would be competent enough to construct a device emitting such signals, or that persons who are competent would be ethical enough not to use it and not to disseminate or leak the information. In the age of Internet and easy access to technology all such assumptions are false.

Two examples from my corner of the woods.

Many city tram systems here use IR signals to operate rail switches. The driver has a “magic box” with two buttons: left and right. A few years ago there were many tram derailments resulting from someone operating the switch (using a self-made device) while the tram was passing over it. In one case a pedestrian was killed by a tram car skidding sideways while negotiating a curve and crushing the person against a building wall.

The railroads had an emergency stop system operating via FM radio normally used for voice communication between crewmembers and dispatchers. A special signal (a particular sequence of tones and a voice message in a loop) could be send by any driver spotting an emergency by hitting emergency button on the radio. All locomotives within range will apply emergency braking automatically after a few seconds of such signal. Older locomotives did not have the system, but the driver should apply braking himself after hearing the characteristic signal and voice message. It has been abused quite a few times, disrupting traffic. There were no casualties as far as I know. The system may have been phased out already in favor of private GSM network but I am not 100% sure.

Clive Robinson •
[February 22, 2023 10:10 AM](https://www.schneier.com/blog/archives/2023/02/a-device-to-turn-traffic-lights-green.html/#comment-418200)

@ Bruce, ALL,

Re : Engineered OUT security.

There are thousands of different “short range” systems using the EM spectrum not quite from “DC to Daylight” but VHF-UHF using “Private Mobile Radiom(PMR) and unforgivably the unlicensed “Industrial Scientific Medical”(ISM) bands. Some realy cheap ones use “InfraRed”(IR) and even visable light. As well as some “piggy-backing” on existing EM systems such as using X-Band that the automatic traffic lights use for Doppler RADAR these days rather than coils in the road. However “rail roads” also still use LF signalling like a “big daddy” version of the “Near Field Communications”(NFC) systems you find in “contactless cards”, “Passports” and these days “Smart Devices”.

Way to many use commercially available chips almost the same as either “Key Fobs”, “Garage Door Openers”, and “TV Remote Controls”

In essence they are read the data sheet put the “suggested circuit” on PCB buy the chip and LED mount on PCB and flog it to a customer…

Most do not use any form of security sending the equivalent of plaintext. The reason this is the easiest to design…

So in the UK we have “streat pillars” that use ~450MHz UHF PMR frequencies to control valves for Gas, Water, and even electricity. The employee “drives by” and presses a button in h...