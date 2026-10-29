---
title: Quickpost: Uranium Glass
url: https://blog.didierstevens.com/2026/10/28/quickpost-uranium-glass/
source: Didier Stevens
date: 2026-10-28
fetch_date: 2026-10-29T07:50:38.622280
---

# Quickpost: Uranium Glass

# [Didier Stevens](https://blog.didierstevens.com/)

## Wednesday 28 October 2026

### Quickpost: Uranium Glass

Filed under: [Hardware](https://blog.didierstevens.com/category/hardware/) — Didier Stevens @ 17:03

I got the opportunity to measure the radiation emitted by [uranium glass](https://en.wikipedia.org/wiki/Uranium_glass). Uranium glass is glass with uranium added to the glass mix for coloration.

My [Bosean FS-5000](https://blog.didierstevens.com/2024/11/22/interfacing-with-a-cheap-geiger-counter/) [meter](https://blog.didierstevens.com/2025/05/29/quickpost-airplanes-radiation/) did not detect any radiation from the uranium glass. The counts per second (CPS) value was around the same on the uranium glass and away from it.

I know it is proper uranium glass (bought at a flea market), because it glows green under ultraviolet light.

![](https://blog.didierstevens.com/wp-content/uploads/2026/10/image-2.png)

My meter uses a [Geiger–Müller tube](https://en.wikipedia.org/wiki/Geiger%E2%80%93M%C3%BCller_tube), so the tube must not be sensitive enough to detect the radiation from the uranium glass.

I also have another meter to measure radiation, a Radiacode 103 meter. It looks like this:

![](https://blog.didierstevens.com/wp-content/uploads/2026/10/image.png)

It reads out a spot value of 9,57 CPS in the above picture: this is the amount of background radiation in that location, since no radioactive sources were nearby.

And here is my Radiacode 103 meter inside a glass made out of uranium glass:

![](https://blog.didierstevens.com/wp-content/uploads/2026/10/image-1.png)

The CPS value is 13,5, that’s noticeably higher than the background value of 9,57. Thus the glass is emitting some radiation that this meter is picking up. Strictly speaking, that doesn’t prove it’s uranium glass, because it could be another element that is the source of radiation.

But this meter is not only more sensitive, it can also differentiate between sources of radiation.

When my Bosean and my Radiacode meters give me a CPS value, for example 10, it means that they detected 10 ionization events per second (average). An ionization event is caused by ionization radiation: a ray or a particle.

My Bosean meter uses a [Geiger–Müller tube](https://en.wikipedia.org/wiki/Geiger%E2%80%93M%C3%BCller_tube), and such a tube can only measure the presence of ionization events. It can not measure the energy of the radiation or particle. It’s a binary measure.

While my Radiacode meter uses a [scintillation crystal](https://en.wikipedia.org/wiki/Scintillator) to measure ionization events. This crystal does not only detect ionization events (like a GM tube does), but it also measures the energy of the ionizing radiation that caused the ionization events. This amount of energy can be expressed in Joules, but since the values are so small, this amount is typically expressed in keV ([kiloelectonvolt](https://en.wikipedia.org/wiki/Electronvolt)).

The Radiacode meter comes with an app that can display a chart like this one:

![](https://blog.didierstevens.com/wp-content/uploads/2026/10/img_9306.jpg)

What you see here are CPS values set out per keV values. I let my meter run for 3 hours (3:02:21 exactly, see top-right corner of the image) while it was sitting inside the glass. For every ionization event, it measures the energy and builds a table of CPS per energy level. On the vertical axis, you have CPS, and on the horizontal axis, you have energy (keV). You can see a couple of peaks in this spectrum. The app has a library of spectra, and you can match that with your spectrum. That’s what I did here: the vertical purple lines come from a spectrum out of the library that I selected, and that is typical for Uranium (see top of image). The first 3 lines match a peak, the last 2 lines don’t match a peak.

Here is the info displayed by the app for the Uranium chain spectrum:

![](https://blog.didierstevens.com/wp-content/uploads/2026/10/img_9302.png)

With the Radiacode meter, when I perform measurements over a long period, I can build up a spectrum of the energy of the ionizing radiations emitted by the sample, and then I can compare that with the app’s library, and when I have a good match, I have identified the element with a good probability.

This glass that I was able to test has a very high probability of being uranium glass: it has the appearance of uranium glass, it glows under UV light, it emits radiation and its radiation spectrum matches the uranium chain spectrum.

For reference, here is a spectrum of background radiation:

![](https://blog.didierstevens.com/wp-content/uploads/2026/10/img_9307.jpg)

In the EU, uranium glass can be bought and sold freely (for example at flea markets). It contains radioactive material, but it is exempt from radiation regulations.

---

[Quickpost info](https://blog.didierstevens.com/2007/11/01/announcing-quickposts/)

---

### Share this:

* [Share on Facebook (Opens in new window)
  Facebook](https://blog.didierstevens.com/2026/10/28/quickpost-uranium-glass/?share=facebook)
* [Share on X (Opens in new window)
  X](https://blog.didierstevens.com/2026/10/28/quickpost-uranium-glass/?share=x)

### *Related*

[Leave a Comment](https://blog.didierstevens.com/2026/10/28/quickpost-uranium-glass/#respond)

## Leave a Comment [»](#postcomment "Leave a comment")

No comments yet.

[RSS feed for comments on this post.](https://blog.didierstevens.com/2026/10/28/quickpost-uranium-glass/feed/) [TrackBack URI](https://blog.didierstevens.com/2026/10/28/quickpost-uranium-glass/trackback/)

### Leave a Reply (comments are moderated)

Comment

Name

Email

Website

Turn on JavaScript to leave a comment.

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

* ## Pages

  + [About](https://blog.didierstevens.com/about/)
  + [Didier Stevens Suite](https://blog.didierstevens.com/didier-stevens-suite/)
  + [Links](https://blog.didierstevens.com/links/)
  + [My Python Templates](https://blog.didierstevens.com/my-python-templates/)
  + [My Software](https://blog.didierstevens.com/my-software/)
  + [Professional](https://blog.didierstevens.com/professional/)
  + [Programs](https://blog.didierstevens.com/programs/)
    - [Ariad](https://blog.didierstevens.com/programs/ariad/)
    - [Authenticode Tools](https://blog.didierstevens.com/programs/authenticode-tools/)
    - [Binary Tools](https://blog.didierstevens.com/programs/binary-tools/)
    - [CASToggle](https://blog.didierstevens.com/programs/castoggle/)
    - [Cobalt Strike Tools](https://blog.didierstevens.com/programs/cobalt-strike-tools/)
    - [Disitool](https://blog.didierstevens.com/programs/disitool/)
    - [EICARgen](https://blog.didierstevens.com/programs/eicargen/)
    - [ExtractScripts](https://blog.didierstevens.com/programs/extractscripts/)
    - [FileGen](https://blog.didierstevens.com/programs/filegen/)
    - [FileScanner](https://blog.didierstevens.com/programs/filescanner/)
    - [HeapLocker](https://blog.didierstevens.com/programs/heaplocker/)
    - [MyJSON Tools](https://blog.didierstevens.com/programs/myjson-tools/)
    - [Network Appliance Forensic Toolkit](https://blog.didierstevens.com/programs/network-appliance-forensic-toolkit/)
    - [Nokia Time Lapse Photography](https://blog.didierstevens.com/programs/nokia-time-lapse-photography/)
    - [oledump.py](https://blog.didierstevens.com/programs/oledump-py/)
    - [OllyStepNSearch](https://blog.didierstevens.com/programs/ollystepnsearch/)
    - [PDF Tools](https://blog.didierstevens.com/programs/pdf-tools/)
    - [Shellcode](https://blog.didierstevens.com/programs/shellcode/)
    - [SpiderMonkey](https://blog.didierstevens.com/programs/spidermonkey/)
    - [Translate](https://blog.didierstevens.com/programs/translate/)
    - [USBVirusScan](https://blog.didierstevens.com/programs/usbvirusscan/)
    - [UserAssist](https://blog.didierstevens.com/programs/userassist/)
    - [VirusTotal Tools...