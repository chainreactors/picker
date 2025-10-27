---
title: Pwn2Own Automotive 2024: Hacking the JuiceBox 40
url: https://sector7.computest.nl/post/2024-08-pwn2own-automotive-juicebox-40/
source: Sector 7
date: 2024-08-30
fetch_date: 2025-10-06T18:17:59.959547
---

# Pwn2Own Automotive 2024: Hacking the JuiceBox 40

[![](/images/logo.png)](/)

* [Research](/)
* [About](/about/)
* [Contact](/contact/)
* [Computest](https://computest.nl/)

* [Mastodon](https://infosec.exchange/%40sector7)
* [Bluesky](https://bsky.app/profile/sector7-nl.bsky.social)
* [LinkedIn](https://www.linkedin.com/company/computest)
* [GitHub](https://github.com/sector7-nl)
* [RSS](/index.xml)

August 29, 2024

# Pwn2Own Automotive 2024: Hacking the JuiceBox 40

![](/post/2024-08-pwn2own-automotive-juicebox-40/header.jpg)

During Pwn2Own Automotive 2024 in Tokyo, we demonstrated exploits against three different EV chargers: the [Autel MaxiCharger (MAXI US AC W12-L-4G)](https://sector7.computest.nl/post/2024-08-pwn2own-automotive-autel-maxicharger/), the [ChargePoint Home Flex](https://sector7.computest.nl/post/2024-08-pwn2own-automotive-chargepoint-home-flex/) and the JuiceBox 40 Smart EV Charging Station with WiFi. This is our writeup of the research that we performed on the JuiceBox 40 Smart EV Charging Station. We discovered one vulnerability which has, since the event, been assigned [CVE-2024-23938](https://www.cve.org/CVERecord?id=CVE-2024-23938). During the competition, we were able to exploit CVE-2024-23938 to execute arbitrary code on the charger while requiring only network access for practical reasons at the event. However, being within Bluetooth range of the device is sufficient with a few extra steps.

# Background

We were initially uncertain of which targets made the most sense to focus on at Pwn2Own Automotive. EV chargers in particular were a category that none of us had looked into before. Therefore, we undertook an initial online investigation of the available targets and picked those that we deemed most promising.

As a result of that investigation, we were convinced that the JuiceBox 40 was one of the *juiciest* targets at the event, at least until we had our hands on the rest of the devices we picked. You can check out our other writeups about the Autel MaxiCharger (to be published later) and the [ChargePoint Home Flex](https://sector7.computest.nl/post/2024-08-pwn2own-automotive-chargepoint-home-flex/) to get a better idea for why we believe they ended up being *juicier* than the JuiceBox 40 after all ;)

## Hardware

In terms of hardware, the JuiceBox 40 is relatively straightforward. There are a few main components:

* Silicon Labs WGM160PX22KGA3 application + WiFi processor
* Silicon Labs MGM13S12A Bluetooth/BLE processor
* Atmel ATMega328P MCU - which we suspect is the charging/safety controller
* Atmel M90E36A metering IC

These components were also summarized by [ZDI in an exploratory blog post](https://www.zerodayinitiative.com/blog/2023/11/28/a-detailed-look-at-pwn2own-automotive-ev-charger-hardware). We annotated one of the images from the post to label and highlight the components mentioned above:

![JuiceBox 40 internal view](juicebox40_annotated_hardware.png#center)

We focused on the software hosted by the WGM160P processor as the main target for the competition and did not delve deeply into the MGM13S12A front. Nonetheless, it caught our interest and we believe that it is an interesting attack surface choice for future research.

# Reconnaissance

During our target assessment for the JuiceBox, we found [posts on Reddit](https://www.reddit.com/r/electricvehicles/comments/grzbq3/juicebox_40_wifi_issues/) regarding issues with the charger and how to fix them using a “remote terminal” that was accessible to devices on the same network as the charger. Additionally, we found YouTube videos of owners documenting fixes and modifications that they have made to the device as well as other posts that contained photos of the internals of other models by the same vendor. For example, [a post on iFixit about the JuiceBox EVSE](https://www.ifixit.com/Guide/JuiceBox%2BEVSE%2BRelay%2BReplacement%2B%28UL-front%2BLEDs%2Bversion%29/154411) that explains how to replace a relay in the device gave us hints as to what the main hardware components of the JuiceBox line-up might be. This photo from said article demonstrates the kind of useful information that we were looking for - a large shielded module labelled with “ZENTRI” and “AMW106”:

![JuiceBox EVSE internal components photo](juicebox_evse_internals.png#center)

In short, there was a lot of information to be found. And most interesting of all, there was apparently an open administrative interface that any other device on the network could interact with.

By the end of our little foray, we had the following main takeaways that we could use for further investigation:

1. Older versions of the JuiceBox 40 were based on a WiFi module called the `AMW106`, which was manufactured by Zentri. These versions run ZentriOS.
2. Newer versions of the JuiceBox 40 are perhaps based on a successor WiFi module, the `WGM160P`. These versions run a successor to ZentriOS, called Gecko OS.
3. Development modules and kits for both the `AMW106` and the `WGM160P` platforms were easily sourceable from many resellers.
4. Both ZentriOS and Gecko OS have a plethora of features (e.g. the remote terminal feature) that seem to be accessible in a production setting on the JuiceBox 40.

Therefore, we pulled the trigger on the JuiceBox 40 as a target, ordered the charger and continued to investigate the threads we found while waiting for the device to arrive from the US.

# Getting closer to the firmware

We started perusing the documentation of both ZentriOS and Gecko OS with a focus on how the update procedure is implemented. Besides getting a better idea of how the platforms function, we also wanted to find a way to download a firmware image if possible. We learned quite a bit from the extensive documentation, with the main points being:

1. Both operating systems consist of a core kernel and “built-in plugins” segment, in addition to an optional application that a developer could bundle with a specific build.
2. Both systems had a fully-managed device auth{n,z} and updating mechanism in place, backed by Zentri Device Management Service (DMS).
3. Both operating systems were designed to function both as a development platforms and add-on turn-key solutions. The latter means that the platform can be used as sort of a “connectivity” add-on in combination with a discrete application processor. This design decision explains the choice of exposing a lot of the features from the core kernel and associated plugins through a command line interface. By providing such a simple interface, the platform becomes easier to integrate with new or even existing designs.

We decided to explore Zentri DMS further, and quickly learned that it was possible to register an account and create test firmware bundles for specific platforms without having to have an actual device. We created a test WGM160P module bundle, and set its firmware version to be with the latest stable base image of Gecko OS which (4.2.7 at the time). Afterwards, we could see a listing of the “files” that constituted the firmware, as well as a JSON file specifying how these files were laid out in internal flash:

![file listing for Gecko OS 4.2.7 base image](gecko_os_4.2.7_zentri_listing.png#center)

With these files in hand, we were able to hit the ground running with vulnerability discovery on the base OS much faster than we initially anticipated.

## Development setup

As a rule of thumb, it is always a good idea to have at least one backup device when diving into a piece of hardware. As Andrew “bunnie” Huang put it:

> My rule is to ideally acquire three: one to totally trash and take apart (so this can literally come from a trash heap); one to tweak and tune; and one to keep pristine, so you have a reference to check your results.

Realistically, we wanted to avoid having to buy a second charger to save (potentially) unnecessary costs. However, it would be quite handy to have a second unit to perform tests on in case something goes wrong. For most of the targets we went after doing so was not financially...