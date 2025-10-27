---
title: Introduction
url: https://cellguard.seemoo.de/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-15
fetch_date: 2025-10-06T18:53:37.349777
---

# Introduction

[ ]
[ ]

## [![Logo](/logo.webp)CellGuard](/)

* [Device Support](/docs/devices/)
* [Install](/docs/install/)
* [Study](/docs/study/)
* [Source Code](/docs/source-code/)
* [Changelog](/docs/changelog/)
* [Report Issues](/docs/report-issues/)
* [Privacy Policy](/docs/privacy-policy/)

* [Legal Note](https://www.tu-darmstadt.de/impressum/index.de.jsp)

![Menu](/svg/menu.svg)

### Introduction

![Table of Contents](/svg/toc.svg)

* [What is a rogue base station?](#what-is-a-rogue-base-station)
* [How does rogue base station detection work?](#how-does-rogue-base-station-detection-work)
* [How does CellGuard work on a more technical level?](#how-does-cellguard-work-on-a-more-technical-level)
* [How to react to rogue base station warnings?](#how-to-react-to-rogue-base-station-warnings)
* [I want to try CellGuard!](#i-want-to-try-cellguard)

# CellGuard [#](#cellguard)

CellGuard is a research project that analyzes how cellular networks are operated and possibly surveilled.
The CellGuard app for iOS can uncover cellular attacks targeting your iPhone.
It observes baseband packets and analyzes them for suspicious activities, hinting at rogue base stations.
Let’s catch them all!

![Three screenshots of the CellGuard app showing its summary, map, and packet views.](home-light-750.webp)

## What is a rogue base station? [#](#what-is-a-rogue-base-station)

A rogue base station, also called a fake base station, is a malicious network cell that tricks your phone into connecting to it. An attacker can use rogue base stations for various purposes, such as tracking a user’s location, intercepting network traffic, or even launching remote code execution attacks against the baseband chip’s firmware.

Depending on the radio technology, rogue base stations can be very easy for attackers to set up. In 2G networks, phones connect to them without further verificationâsimilar to an open Wi-Fi network. As this issue is intrinsic to the 2G specification, the best defense is to turn off 2G connectivity on a phone. Recent iPhones support this feature as a setting in [Lockdown Mode](https://support.apple.com/en-us/105120).

Since 3G, networks authenticate towards a phone. Theoretically, this should prevent attackers from setting up rogue base stations with extended capabilities, such as intercepting network traffic. However, state-sponsored attackers, who can coerce mobile network operators to collaborate, can still set up rogue base stations that authenticate through roaming infrastructure. Such attacks have already been [reported](https://securitylab.amnesty.org/latest/2023/10/technical-deep-dive-into-intellexa-alliance-surveillance-products/).

## How does rogue base station detection work? [#](#how-does-rogue-base-station-detection-work)

A perfect rogue base station is indistinguishable from a real one. However, attackers face a couple of challenges in their setup. This project aims to identify such challenges and build detection metrics on top of these. In the initial version, the CellGuard app detects rogue base stations using the following metrics:

* *Existence of a cell in Apple’s Location Services (ALS) database.* This metric detects rogue base stations that are put up for a short period of time.
* *Distance between ALS cell and actual user location.* This metric detects rogue base stations that were set up with the wrong parameters.
* *Comparison of a cell’s frequency channel and physical cell ID with ALS.* This metric also detects rogue base stations that were set up with the wrong parameters.
* *Bandwidth.* This metric detects rogue base stations that use low-cost or deprecated hardware.
* *Network reject packets.* This metric uncovers network authentication failures.
* *Signal strength.* This metric shows if a rogue base station tried to force users to connect to it by sending a significantly stronger signal than other base stations.

In real-world testing across Europe and the US, we found that all these metrics can also trigger for legitimate reasons.
Some anomalies are to be expected.
For example, if a mobile network operator sets up a new cell, it takes 2-3 days for it to appear in the ALS database. Some cells reduce per-user bandwidth, especially when they face high traffic.
Network rejection packets are received in any situation where an iPhone connects to a network for which it doesn’t have a valid SIM. This includes SIMs that are not allowed roaming and situations where the intended network provider has no coverage but other networks are available.
Also, signal strength might vary.

Combining multiple metrics and assigning different weights to them makes CellGuard more reliable. However, CellGuard might still warn you about legitimate cells. Given that rogue base station attacks are rare, most warnings the average user sees are false alarms.

## How does CellGuard work on a more technical level? [#](#how-does-cellguard-work-on-a-more-technical-level)

CellGuard captures packets exchanged between an iPhone’s cellular baseband chip and iOS. It then analyses these packets for the anomalies described above and your location history. More details on how this works are contained in our [CCC talk](https://media.ccc.de/v/37c3-11868-what_your_phone_won_t_tell_you).

## How to react to rogue base station warnings? [#](#how-to-react-to-rogue-base-station-warnings)

Given that there is a high likelihood of false positives due to regular network anomalies, you should not have to worry if CellGuard reports rogue base stations to you.
With our opt-in [study](/docs/study/ "Study"), we aim to improve our detection algorithm, leading to more accurate future warnings.

Depending on your threat model, receiving warnings could mean different things.
Even if you were connected to a real rogue base station, this does not mean you’re being surveilled or hacked. It also does not mean that there is mass surveillance. Due to how rogue base stations work, it is expected that users other than the intended targets might see and connect to rogue base stations.

Immediate actions to take from a user perspective are highly limited.
Receiving a warning over CellGuard means that you are already connected to a suspicious cell.
You can enable flight mode or turn your phone off when expecting a rogue base station within wireless reach. For further investigation, especially if the connection to a rogue base station was paired with other unexpected behavior, please keep a copy of the sysdiagnose in a separate storage.

## I want to try CellGuard! [#](#i-want-to-try-cellguard)

That’s great! We’re currently in an early beta phase, testing our detection metrics on a broader audience of users. You can [install](docs/install) CellGuard on your primary iPhone, even with Lockdown Mode enabled, or on a jailbroken iPhone as a sensor. Details on when to use which mode and why can be found in our [devices](docs/devices) section.

* [What is a rogue base station?](#what-is-a-rogue-base-station)
* [How does rogue base station detection work?](#how-does-rogue-base-station-detection-work)
* [How does CellGuard work on a more technical level?](#how-does-cellguard-work-on-a-more-technical-level)
* [How to react to rogue base station warnings?](#how-to-react-to-rogue-base-station-warnings)
* [I want to try CellGuard!](#i-want-to-try-cellguard)