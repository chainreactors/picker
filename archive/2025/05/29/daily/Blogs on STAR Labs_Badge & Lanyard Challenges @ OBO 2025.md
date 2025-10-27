---
title: Badge & Lanyard Challenges @ OBO 2025
url: https://starlabs.sg/blog/2025/05-badge-lanyard-challenge-at-obo-2025/
source: Blogs on STAR Labs
date: 2025-05-29
fetch_date: 2025-10-06T22:26:19.981401
---

# Badge & Lanyard Challenges @ OBO 2025

[![logo](https://starlabs.sg/logo-white.png)](https://starlabs.sg/ "  (Alt + H)")

* [Home](https://starlabs.sg/ "Home")
* [About](https://starlabs.sg/about/ "About")
* [Advisories](https://starlabs.sg/advisories/ "Advisories")
* [Blog](https://starlabs.sg/blog/ "Blog")
* [Achievements](https://starlabs.sg/achievements/ "Achievements")
* [Publications](https://starlabs.sg/publications/ "Publications")
* [Search](https://starlabs.sg/search/ "Search (Alt + /)")

[Home](https://starlabs.sg/) » [Blogs](https://starlabs.sg/blog/)

# Badge & Lanyard Challenges @ OBO 2025

May 28, 2025 · 14 min · Manzel Seet & Sarah Tan

Table of Contents

* [Introduction](#introduction)
* [Lanyard Challenge](#lanyard-challenge)
* [Badge Design](#badge-design)
* [Hardware Circuit](#hardware-circuit)
* [Hardware CTF Challenges](#hardware-ctf-challenges)
  + [1. Welcome Flag (Category: Welcome)](#1-welcome-flag-category-welcome)
  + [2. Retro Music (Category: Communication)](#2-retro-music-category-communication)
  + [Activities Booth (Category: Communication)](#activities-booth-category-communication)
  + [Diagnostic Mode (Category: Bootloader)](#diagnostic-mode-category-bootloader)
  + [Hidden Partition (Category: Bootloader)](#hidden-partition-category-bootloader)
  + [HMAC Oracle (Category: Bootloader)](#hmac-oracle-category-bootloader)
* [Conclusion](#conclusion)

## Introduction[#](#introduction)

We are back with Round 2 of the Off-By-One conference — where bits meet breadboards and bugs are celebrated! 🐛⚡

If you are into hardware and IoT security, you’ll know one thing’s for sure: the STAR Labs SG badge is not your average conference bling bling. This year’s badge isn’t just a collector’s item — it’s a playground for the curious, packed with new challenges inspired by months’s worth of research and hackery. And yes, the CTF is back, with even more nerdy goodness.

But before we plug into what’s new, let’s do a quick flashback to last year’s Octopus badge. That little guy had personality — literally. With two round screens as eyes, attendees had a blast giving their octo-buddy a range of emotions. Some even got creative and hacked in their own custom graphics. Total respect to those two Canadians.

Unlike the usual plug-it-in, solve-a-riddle USB badges, we are constantly trying to add learning value to it. We turned the badge into a hands-on intro to hardware-hacking — think I2C, SPI, and MicroPython quirks. Oh, and remember the mini voltage glitching challenge? Yup, all on the same board. We hope it sparked a few “Aha!” moments for those digging into hardware for the first time.

Fast forward to 2025: we’ve cranked the nerd 🤓 dial all the way up — channeling a bit of “Back to the Future” energy (which, by the way, is also one of this year’s T-shirt designs). And yes, we’ve officially gone full throttle: the lanyard is now part of the challenge. You heard that right — lanyard hacking is a thing now.

To give you the inside scoop, we’ve got Sarah and Manzel on deck to walk you through the Behind the Scenes — from design choices to the delightful chaos that comes with building hackable hardware. Buckle up. This one’s gonna be a fun ride.

## Lanyard Challenge[#](#lanyard-challenge)

Hi, my name is [Sarah](https://x.com/buttburner), and I’m the creative lead here at STAR Labs :)

I was tasked with creating a lanyard challenge for this year’s Off By One 2025, and to be honest, I had no idea how to go about it. Yes, I’ve heard about encryptions and ciphers, but I’d never actually used them to build a puzzle before.

We wanted a puzzle that required multiple lanyards to be matched up and arranged in the correct order to reveal the key/flag.

There were four lanyard colors in total: attendees, speakers, crew, and sponsors. The tricky part? We didn’t make an equal number of each! Sponsors, who had green lanyards, had the fewest available—and that’s exactly where the final puzzle was hidden.

Only by lining up the lanyards in the right sequence would the correct code appear. This is an earlier version I was initially toying with which features MD5 hash and the nyctograph cipher. At first I wanted to cut up the cipher and have them distributed across the lanyards so people would have to match them up accordingly to get the full text.

![](/blog/2025/images/obo2025-lanyard-3.png)

I reached out to several colleagues, including Jacob, for ideas and eventually settled on using ROT13 instead of the MD5 hash. We also scrapped the plan to chop the cipher up into pieces.

![](/blog/2025/images/obo2025-lanyard-2.png)

We did make sure to field test the design in the office to make sure it was solvable but it did take a little while for the staff to understand what they were looking at; a good number of them thought the ciphers were just part of the design. A bass clef was subtly hidden in the lanyards to help indicate the correct order they were supposed to be in.

It was hilarious (and satisfying) watching students scramble around once they realized the “random” symbols on the lanyards actually meant something. Once they had the flag/key, they could use it to unlock the final key phrase hidden inside this year’s badge.

Fun Facts:
There was a clue buried in the badge—an Alice in Wonderland illustration of the White Rabbit with the words “Follow the White Rabbit.” This was both a hint and an Easter egg, since the nyctograph cipher was invented by Lewis Carroll himself!

![](/blog/2025/images/obo2025-lanyard-1.jpg)

## Badge Design[#](#badge-design)

Now let us discuss and take a look at our brand new badge design as well! Our new design is a robot character incorporating a retro-themed user interface.

![](/blog/2025/images/obo2025-badge-14.png)

In terms of hardware components, we explored LCDs with relatively high-resolution graphics and display update rate. Having this, we were able to include GIF playback support, which allowed us to bring in cute animated facial expressions for our little robot friend.
![GIF](/blog/2025/images/obo2025-badge-2.gif)

As a nice touch, we also added customized name-cards for our speakers.
![](/blog/2025/images/obo2025-badge-3.png)

Now let me pass my time to Manzel, the electronics wizard who created the circuitry and CTF challenges.

## Hardware Circuit[#](#hardware-circuit)

Hi I am [Manzel](https://sg.linkedin.com/in/manzelseet) and I am the Hardware Engineer at STAR Labs SG.

Thinking of a new hardware circuit is always interesting as we aim to incorporate new features that we have previously looked at during the course of our research.

A key feedback from last year is that the badge was too heavy, therefore we decided to reduce to 2 AAA batteries. Effectively cutting the weight by 25%. However, because the battery capacity has been reduced, we changed to the newer ESP32-C3 which is slightly more battery-efficient than the ESP32-S3. It also has a single RISC-V core which is also a good platform to learn about RISC-V architecture.

Internally, we have done 3 prototypes and here is how they look:

![](/blog/2025/images/obo2025-badge-15.jpg)

Our first blue prototype was an LED bit matrix. It received good feedback because it captured the retro theme of the conference well. However, we later discovered a high failure rate as the small LEDs are fragile.

Doing a DIY fix isn’t easy with the plastic LEDs. This means desoldering repair work may risk damaging/overheating the surrounding LEDs as well.

Therefore we decided to pivot to LCD displays. For the green prototypes, we accounted for two different displays.

While the larger rectangular display had better proportions, it has a poor pixel density and contrast ratio, making our artwork look too blurry.

The smaller LCD has a higher pixel density and refresh rate. With little time left to the conference, we decided to settle on the smaller LCD, as we could present GIF animations which is something not commonly done in other conference badges.

Overall this is the timeline

* 23 Jan: Manufacturing of...