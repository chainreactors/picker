---
title: Designing a Passive LiDAR Detector Device - Firmware
url: https://www.atredis.com/blog/2025/12/1/designing-a-passive-lidar-detector-device-firmware
source: Blog - Atredis Partners
date: 2025-12-12
fetch_date: 2025-12-13T03:14:26.317192
---

# Designing a Passive LiDAR Detector Device - Firmware

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

# Designing a Passive LiDAR Detector Device - Firmware

Dec 12

Written By [Sam](/blog?author=680a6cb7a8e4bb451b126b93)

# Welcome back!

In [the last post](/blog/2025/11/20/designing-a-passive-lidar-detection-sensor) I described the process of examining the iPhone Pro TrueDepth LiDAR and developing concepts for hardware to detect it. Here I will describe the firmware for this device, the concepts employed in it, and the approaches taken to implementing these concepts on the tiny SAMD21.

Let’s start by revisiting a key point from the previous post:

> “LiDAR is a Flashy Light, How Do We Measure a Flashy Light”

1. **See a signal as light spread into beams over an area**
2. **Sense and convert those beams into analog signals**
3. **Convert the signals from analog to digital**
4. **Measure them**

As it turns out, it is not just detecting *a flashy light*, its detecting *multiple discrete beams of flashy light* **and differentiating them from other noise**. The hardware described in the last post provides super fast digital signals from 4 discrete photodiodes. We can use those signals to perform several different measurements to differentiate the characteristics of the iPhone Pro TrueDepth LiDAR from other signal sources or noise. The firmware I designed for the device employs the following measurements:

* **Frequency (Goertzel):**

  + Target 60hz and optionally harmonics at 30hz and 120hz
  + *Note that including harmonics increases susceptibility to false positives*
* **Pulse Repetition Frequency (PRF):**

  + We expect the LiDAR signal to appear steady when present, with uniform edges, while things like IR Remotes are more often in bursts
* **Burstlikeness (Interquartile Range of Magnitude):**

  + Again, we expect the signal to appear steady when present, so an analysis of the recent measurements is performed to judge whether they represent a steady or burstlike signal
  + Comparing the top and bottom quartiles of Hann Window Smoothed, detrended signal energy
  + I do not really understand this very well, but I web searched and StackExchanged my way through it.
* **Spatial Coincidence (Discrete Beams versus Wide Flood):**

  + A record of Exponential Moving Average Peaks per channel is kept and checked to determine whether some-but-not-all sensors fired at the same time or not.
* **TSOP IR-Decode Veto (Sometimes Brute Force *is* the Elegant Solution):**

  + Consider signal source highly unlikely to be LiDAR when remote codes are successfully decoded by the TSOP within a measurement window
* **Periodic Blink (Detectable Duty Cycle):**

  + The iPhone Pro TrueDepth LiDAR seems to blink on and off in a way that is detectable, though this is less reliable as the signal is likely to move in and out of detection from simple movement by the person holding the source during a measurement window.

In order to accomplish all of this, the firmware leverages a few simple concepts to abstract and organize the measurements from the designed hardware, and analyze them in a useful manner.

* **Scoring System:**

  + In order to meaningfully analyze the measurements and programmatically decide whether a given signal is or is not the sought LiDAR device, the firmware utilizes a weighted scoring system. A score greater than a given amount must be achieved within a measurement window in order to trigger a detection.

    - Positive detection of sought measurements such as the desired dominant frequency, some-but-not-all sensors firing within a measurement window, and others are given a positive score of some amount
    - Positive IR remote code decode by the TSOP would grant a significant negative score.
* **Measurement Bucketing (Sampling):**

  + Measurement events are stored into fixed-time 4ms samples or “Buckets”
* **Ring Buffers (Fast Read, Fast Write):**

  + Measurement samples, or “Buckets”, are written and read using ring buffers. This is fast! It needs to be fast so it doesn’t end up wasting the hardware capability.
* **Interrupt Driven Signal Acquisition (Fast Edge Capture):**

  + The SAMD21 can do microsecond precision on Interrupt Timers. That’s fast *and this needs fast!*
* **Latching Hysteresis (No-Flappy Bird):**

  + In the earlier models, I noticed the detection would either snap on and then never turn off, or be near impossible to get to stay triggered and only observable via serial output rather than via the LED signal. This was not fun, it needs to be cute and light up. To fix this, I use counters to measure:

    - How many positive detections have been achieved in a given period of time
    - How many it has not triggered in the same period of time
  + Based on these counts, the “detection” indicator is fired and latched when detection has been achieved long enough, and unlatches when detection has not been achieved for long enough. This prevents some false positives and helps smooth the indication of a successful detection.

That sure is a lot, and I was not familiar with a lot of it before starting this project, so allow me to go into a bit more detail about some of these concepts.

## Frequency (FRE)

Before we talk about things FRE, we need to talk about *math* (im sorry, I didn’t like this either). To get our **FRE** measurement in software we need to use the **Goertzel** algorithm. Before we can effectively do this though, **Detrending** and **Hann Smoothing** are performed on the measured signals first.

### **Detrending** / DC Offset Removal / whatever why are there so many names for things

What does this even mean? I had to look it up, which felt embarrassing because I do this for recording audio in a DAW but somehow did not make the connection here before looking it up, and learning about it from the audacity website of all places.

> “DC offset is an offsetting of a signal from zero. On the Audacity waveform it would mean that the waveform in default view appears not to be centered on the 0.0 horizontal line, as in the upper track in this image:”

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/977e5720-dffc-4ec3-8396-5409ad50aaf0/dc_offset.png)

https://manual.audacityteam.org/man/dc\_offset.html

This is needed to remove the DC component from the signal to prevent the 0hz baseline from interfering with measurements of the 60hz signal in the noise. I really don’t understand this well, this required a lot of recursive web searches on how to measure and analyze signals. It seems like it works, but my understanding of it is pretty shallow.

To do this, **mean removal** is performed, which sounds positive! **Mean removal** (**detrending**) is done in most simple way by computing the average of all samples in the window then subtracting that from every sample, like so:

```
float mu = 0.0f;
for (int i=0; i<N; i++) {
 mu += prep[i];
}
mu /= N;
for (int i=0; i<N; i++) {
 prep[i] -= mu;
}
```

After detrending, **Hann Smoothing** is applied to the measurement.

### **Hann Smoothing**

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/f9285f59-669...