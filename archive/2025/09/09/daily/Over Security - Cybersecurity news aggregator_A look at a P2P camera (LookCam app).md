---
title: A look at a P2P camera (LookCam app)
url: https://palant.info/2025/09/08/a-look-at-a-p2p-camera-lookcam-app/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-09
fetch_date: 2025-10-02T19:52:07.849692
---

# A look at a P2P camera (LookCam app)

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# A look at a P2P camera (LookCam app)

2025-09-08
 [Security](/categories/security/)/[IoT](/categories/iot/)
 24 mins
 [1 comment](/2025/09/08/a-look-at-a-p2p-camera-lookcam-app/#comments)

Iâve got my hands on an internet-connected camera and decided to take a closer look, having already read about security issues with similar cameras. What I found far exceeded my expectations: fake access controls, bogus protocol encryption, completely unprotected cloud uploads and firmware riddled with security flaws. One could even say that these cameras are Murphyâs Law turned solid: everything that could be done wrong has been done wrong here. While there is considerable prior research on these and similar cameras that outlines some of the flaws, I felt that the combination of severe flaws is reason enough to publish an article of my own.

My findings should apply to any camera that can be managed via the LookCam app. This includes cameras meant to be used with less popular apps of the same developer: tcam, CloudWayCam, VDP, AIBoxcam, IP System. Note that the LookCamPro app, while visually very similar, is technically quite different. It also uses the PPPP protocol for low-level communication but otherwise doesnât seem to be related, and the corresponding devices are unlikely to suffer from the same flaws.

![A graphic with the LookCam logo in the middle. Around it are arranged five devices with the respective camera locations marked: a radio clock, a power outlet, a light switch, a USB charger, a bulb socket.](/2025/09/08/a-look-at-a-p2p-camera-lookcam-app/devices.jpg)

There seems to be little chance that things will improve with these cameras. I have no way of contacting either the hardware vendors or the developers behind the LookCam app. In fact, it looks like masking their identity was done on purpose here. But even if I could contact them, the cameras lack an update mechanism for their firmware. So fixing the devices already sold is impossible.

I have no way of knowing how many of these cameras exist. The LookCam app is currently listed with almost 1.5 million downloads on Google Play however. An iPhone and a Windows version of the app are also available but no public statistics exist here.

#### Contents

* [The highlights](#the-highlights)
* [The hardware](#the-hardware)
* [The LookCam app](#the-lookcam-app)
* [The PPPP protocol](#the-pppp-protocol)
  + [The basics](#the-basics)
  + [The âencryptionâ](#the-encryption)
  + [The threat model](#the-threat-model)
* [The firmware](#the-firmware)
* [The cloud](#the-cloud)
* [How safe are device IDs?](#how-safe-are-device-ids)
* [Recommendations](#recommendations)
* [Further reading](#further-reading)

## The highlights

The camera cannot be easily isolated from unauthorized access. It can either function as a WiFi access point, but setting a WiFi password isnât possible. Or it can connect to an existing network, and then it will insist on being connected to the internet. If internet access is removed the camera will go into a reboot loop. So you have the choice of letting anybody in the vicinity access this camera or allowing it to be accessed from the internet.

The communication of this camera is largely unencrypted. The underlying PPPP protocol supports âencryptionâ which is better described as obfuscation, but the LookCam app almost never makes use of it. Not that it would be of much help, the proprietary encryption algorithms being developed without any understanding of cryptography. These rely on static encryption keys which are trivially extracted from the app but should be easy enough to deduce even from merely observing some traffic.

The camera firmware is riddled with buffer overflow issues which should be trivial to turn into arbitrary code execution. Protection mechanisms like DEP or ASLR might have been a hurdle but these are disabled. And while the app allows you to set an access password, the firmware doesnât really enforce it. So access without knowing the password can be accomplished simply by modifying the app to skip the password checks.

The only thing preventing complete compromise of any camera is the âsecretâ device ID which has to be known in order to establish a connection. And by âsecretâ I mean that device IDs can generally be enumerated but they are âsecuredâ with a five letter verification code. Unlike with some similar cameras, the algorithm used to generate the verification code isnât public knowledge yet. So somebody wishing to compromise as many cameras as possible would need to either guess the algorithm or guess the verification codes by trying out all possible combinations. I suspect that both approaches are viable.

And while the devices themselves have access passwords which a future firmware version could in theory start verifying, the corresponding cloud service has no authentication beyond knowledge of the device ID. So any recordings uploaded to the cloud are accessible even if the device itself isnât. Even if the camera owner hasnât paid for the cloud service, anyone could book it for them if they know the device ID. The cloud configuration is managed by the server, so making the camera upload its recordings doesnât require device access.

## The hardware

Most cameras connecting to the LookCam app are being marketed as âspy camâ or ânanny cam.â These are made to look like radio clocks, USB chargers, bulb sockets, smoke detectors, even wall outlets. Most of the time their pretended functionality really works. In addition they have an almost invisible pinhole camera that can create remarkably good recordings. Iâve seen prices ranging from US$40 to hundreds of dollars.

The marketing spin says that these cameras are meant to detect when your house is being robbed. Or maybe they allow you to observe your baby while it is in the next room. Of course, in reality people are far more inventive in their use of tiny cameras. Students [discovered them for cheating in exams](https://theconversation.com/students-are-using-smart-spy-technology-to-cheat-in-exams-59241). Gamblers use them to [get an advantage at card games](https://www.wired.com/story/miniature-camera-poker-cheating/). And then there is of course the matter of non-consentual video recordings. So next time you stay somewhere where you donât quite trust the host you might want to search for âLookCamâ on YouTube, just to get an idea of how to recognize such devices.

The camera I had was based on the [Anyka AK39Ev330 hardware platform](http://anyka.net/en/productInfo.aspx?id=123), essentially an ARM CPU with an attached pinhole camera. Presumably, other cameras connecting to the LookCam app are similar, even though there are some provisions for hardware differences in the firmware. The device looked very convincing, its main giveaway being unexpected heat development.

All LookCam cameras Iâve seen were strictly noname devices, it is unclear who builds them. Given the variety of competing form factors I suspect that a number of hardware vendors are involved. Maybe there is one vendor producing the raw camera kit and several others who package it within the respective casings.

## The LookCam app

The LookCam app can manage a number of cameras. Some people demonstrating the app on YouTube had around 50 of them, though I suspect that these are camera sellers and not regular users.

![App screenshot, a screen titled âMy Device.â It lists a number of cameras with stills on the left side. The cameras are titled something like G000001NRLXW. At the bottom of the screen are the options Video (selected), Photo, Files and More.](/2025/09/08/a-look-at-a-p2p-camera-lookcam-app/screenshot.png)

LookCam app as seen in the example screenshot

While each camera can be given a custom name, its unique ID is always visible as well. For exampl...