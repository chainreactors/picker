---
title: Designing a Passive LiDAR Detector Device - Hardware
url: https://www.atredis.com/blog/2025/11/20/designing-a-passive-lidar-detection-sensor
source: Blog - Atredis Partners
date: 2025-12-05
fetch_date: 2025-12-06T03:10:13.089403
---

# Designing a Passive LiDAR Detector Device - Hardware

[0](/cart)

[Skip to Content](#page)

[![Atredis Partners](//images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1566943528908-J56DPCZRQ9SVG4TFPP27/WhiskeyBirdTextOverlayWhite.png?format=1500w)](/)

[About](/)

[Ownership](/ownership)

[Team](/team)

[Pentesting](/pentesting)

[Embedded](/embedded)

[OCP SAFE](/ocp-safe)

[Risk](/risk)

[Contact](/contact)

[Blog](/blog)

Open Menu
Close Menu

[![Atredis Partners](//images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1566943528908-J56DPCZRQ9SVG4TFPP27/WhiskeyBirdTextOverlayWhite.png?format=1500w)](/)

[About](/)

[Ownership](/ownership)

[Team](/team)

[Pentesting](/pentesting)

[Embedded](/embedded)

[OCP SAFE](/ocp-safe)

[Risk](/risk)

[Contact](/contact)

[Blog](/blog)

Open Menu
Close Menu

[About](/)

[Ownership](/ownership)

[Team](/team)

[Pentesting](/pentesting)

[Embedded](/embedded)

[OCP SAFE](/ocp-safe)

[Risk](/risk)

[Contact](/contact)

[Blog](/blog)

# Designing a Passive LiDAR Detector Device - Hardware

Dec 5

Written By [Sam](/blog?author=680a6cb7a8e4bb451b126b93)

At DEF CON 32, Samy Kamkar gave a talk about laser microphones. That was the only talk I made a point to watch live that year. Kamkar never disappoints and I have fond memories of trying to use a laser pointer and photodiode to hear through windows as a kid. During that talk [Kamkar mentioned](https://youtu.be/R5nMqju6crY?t=2231) noticing the LiDAR dot grid projected from the back of his phone in video from a camera without an IR filter. He briefly talked about the potential for detecting when an iPhone Pro had the camera app open before a picture was even taken, because the LiDAR is activated by the default camera app at startup.

This seemed fun, and I started trying to think of ways to do it. At first I was discouraged as fellow hackers at DEF CON suggested a small device would be unable to detect the signal. I left the idea for a long time before coming back to it. After some experiments with IR remote receivers and photodiodes, I decided I would need to come to understand my target better.

iPhone 15 Pro TrueDepth Dot Grid Lattice Recorded in My Closet

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/f8799947-4382-4da0-833e-954fe6c9da82/Dot+Grid+Lattice+Labels)

https://4sense.medium.com/apple-lidar-demystified-spad-vcsel-and-fusion-aa9c3519d4cb

iPhone TrueDepth/FaceID LiDAR systems utilize a 60hz VCSEL with a 15hz SPAD, with a duty cycle which envelopes the signal. These systems are apparent when observed through cameras without IR filters. This LiDAR system is active when an application on the device uses it, including the default camera application. As indicated in Kamkar's talk, it is possible to detect that the camera app has been opened before any image is captured.

Recording of the TrueDepth LiDAR on the back of my iPhone 15 Pro

This same concept could be used to detect when an iPhone with FaceID has the screen open to the lock screen, even when unlocked or when FaceID is not enabled. Similarly, this concept could also be used to identify when there are Pixel 5 or newer devices with off-screens nearby via an infrared-based pocket detection functionality.

![faceidir.gif](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1763669836770-DZ455LACJ4HTD08H1HV2/faceidir.gif)![faceidir.gif](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1763669836770-DZ455LACJ4HTD08H1HV2/faceidir.gif)

![pixelir.gif](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1763669832705-U7VAPYC4SDDREK1K2T1G/pixelir.gif)![pixelir.gif](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1763669832705-U7VAPYC4SDDREK1K2T1G/pixelir.gif)

FaceID and Pocket Detection Sensor on my iPhone 15 Pro and Pixel 5 respectively

The TrueDepth system, present on the back of iPhone Pro models, is my primary target. Thankfully for me, between patents and existing research into this system, learning all of this information about it was a breeze! Here are some text and image excerpts from the various sources I pored over during my efforts.

> “Patents such as US-20200256669 (view PDF) show that Apple uses a sparse array of single photon avalanche diodes (SPADs) to perform a kind of optical stocktake on the whereabouts of the infrared range-finding LiDAR emissions. And the iPhone maker’s True Depth Face ID design also features innovations that allows the hardware to perceive distance more accurately, albeit on different length scales.”

LiDAR on the iPhone Explained https://blog.lidarnews.com/lidar-on-the-iphone-explained/

![0_D8LGz55sr1SAwiOY.WEBP](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1763670009492-AUZCPK5BH5RIMFUY3VGJ/0_D8LGz55sr1SAwiOY.WEBP)![0_D8LGz55sr1SAwiOY.WEBP](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1763670009492-AUZCPK5BH5RIMFUY3VGJ/0_D8LGz55sr1SAwiOY.WEBP)

![0_sLXMiBILMClJFC1Y.WEBP](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1763670009626-XFGMPJ75H6423DKM9ZJ3/0_sLXMiBILMClJFC1Y.WEBP)![0_sLXMiBILMClJFC1Y.WEBP](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1763670009626-XFGMPJ75H6423DKM9ZJ3/0_sLXMiBILMClJFC1Y.WEBP)

![0_XoYVzZ1U70N3EjTT.WEBP](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1763670010484-EWJIJ7EK89Y7A05L73SB/0_XoYVzZ1U70N3EjTT.WEBP)![0_XoYVzZ1U70N3EjTT.WEBP](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1763670010484-EWJIJ7EK89Y7A05L73SB/0_XoYVzZ1U70N3EjTT.WEBP)

https://4sense.medium.com/apple-lidar-demystified-spad-vcsel-and-fusion-aa9c3519d4cb

> “The apparatus according to claim 1, wherein the radiation source comprises at least one vertical-cavity surface-emitting laser (VCSEL). The apparatus according to claim 2, wherein the at least one VCSEL comprises an array of VCSELs. The apparatus according to claim 1, wherein the sensing elements comprise single-photon avalanche diodes (SPADs).”

US20200256669A1 <https://patents.google.com/patent/US20200256669A1/en>

> “The emitter has 16 stacks of 4 vertical cavity surface emitting laser (VCSEL) cells, for 64 in total. The 64 laser pulses are multiplied by a 3 × 3 diffraction optical element (DOE) to make up 576 pulses [6]. The 576 laser pulses rebounded from object surfaces are detected and the individual time elapses are measured by a single-photon avalanche diode (SPAD) image sensor. [...] It was determined that the optimal phone-to-target distance range is between 0.30 m and 2.00 m. Despite an indicated sampling frequency equal to the 60 Hz framerate of the RGB camera, the LiDAR depth map sampling rate is actually 15 Hz, limiting the utility of this sensor for vibration measurement and presenting challenges if the depth map time series is not downsampled to 15 Hz before further processing.”

Characterization of the iPhone LiDAR[…] <https://pmc.ncbi.nlm.nih.gov/articles/PMC10537187/pdf/sensors-23-07832.pdf>

So we know it is a 60hz, 940nm infrared signal. We also know that it can be expected to present as a rotating pattern of lattice grid beams of light. Armed with this information, I began brainstorming different approaches to measuring such a signal in a meaningful way. It was at this point that I realized I actually don't really know how to do that, so I looked it up.

**LiDAR is a Flashy Light, How Do We Measure a Flashy Light**

After a lot of web searching, reading other researchers' existing work, reading a lot of Wikipedia pages, struggling to get good suggestions out of LLMs, and pouring over datasheets, I reached a point where I felt I was beginning to understand the objectives well enough.

1. See a signal as light spread into beams over an area
2. Sense and convert that light to an analog signal
3. Convert the signal from analog to digital
4. Measure it

The iPhone TrueDepth uses a 60hz, 940nm VCSEL DotGrid Lattice LiDAR system. In order to detect this and distinguish it ...