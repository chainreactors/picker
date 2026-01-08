---
title: Backdoors in VStarcam cameras
url: https://palant.info/2026/01/07/backdoors-in-vstarcam-cameras/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-07
fetch_date: 2026-01-08T03:30:38.191005
---

# Backdoors in VStarcam cameras

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# Backdoors in VStarcam cameras

2026-01-07
 [Security](/categories/security/)/[IoT](/categories/iot/)
 21 mins
 [0 comments](/2026/01/07/backdoors-in-vstarcam-cameras/#comments)

VStarcam is an important brand of cameras based on the [PPPP protocol](/2025/11/05/an-overview-of-the-pppp-protocol-for-iot-cameras/). Unlike the [LookCam cameras I looked into earlier](/2025/09/08/a-look-at-a-p2p-camera-lookcam-app/), these are often being positioned as security cameras. And they in fact do a few things better likeâ¦ well, like having a mostly working authentication mechanism. In order to access the camera one has to know its administrator password.

So much for the theory. When I looked into the firmware of the cameras I discovered a surprising development: over the past years this protection has been systematically undermined. Various mechanisms have been added that leak the access password, and in several cases these cannot be explained as accidents. The overall tendency is clear: for some reason VStarcam *really* wants to have access to their customerâs passwords.

A reminder: âP2Pâ functionality based on the PPPP protocol means that these cameras will always communicate with and be accessible from the internet, even when located on a home network behind NAT. Short of installing a custom firmware this can only addressed by configuring the network firewall to deny internet access.

#### Contents

* [How to recognize affected cameras](#how-to-recognize-affected-cameras)
* [Downloading the firmware](#downloading-the-firmware)
* [Caveats of this survey](#caveats-of-this-survey)
* [VStarcamâs authentication approach](#vstarcam-s-authentication-approach)
* [Endpoint protection](#endpoint-protection)
* [Unauthenticated log access](#unauthenticated-log-access)
* [Explicit password leaking via logs](#explicit-password-leaking-via-logs)
* [Log uploading](#log-uploading)
* [Password-leaking backdoor](#password-leaking-backdoor)
* [Establishing a timeline](#establishing-a-timeline)
* [The impact](#the-impact)
* [Coordinated disclosure attempt](#coordinated-disclosure-attempt)
* [Recommendations](#recommendations)

## How to recognize affected cameras

Not every VStarcam camera has âVStarcamâ printed on the side. I have seen reports of VStarcam cameras being sold under the brand names Besder, MVPower, AOMG, OUSKI, and there are probably more.

Most cameras should be recognizable by the app used to manage them. Any camera managed by one of these apps should be a VStarcam camera: Eye4, EyeCloud, FEC Smart Home, HOTKam, O-KAM Pro, PnPCam, VeePai, VeeRecon, Veesky, VKAM, VsCam, VStarcam Ultra.

## Downloading the firmware

VStarcam cameras have a mechanism to deliver firmware updates (LookCam cameras prove that this shouldnât be taken for granted). The app managing the camera will request update information from an address like `http://api4.eye4.cn:808/firmware/1.2.3.4/EN` where `1.2.3.4` is the firmware version. If a firmware update is available the response will contain a download server and a download path. The app sends these to the device which then downloads and installs the updated firmware.

Both requests are performed over plain HTTP and this is already the first issue. If an attacker can produce a manipulated response either on the network that the app or the device are connected to they will be able to install a malicious update on the camera. The former is particularly problematic, as the camera owner may connect to an open WiFi or similarly untrusted networks while being out.

The last part of a firmware version is a build number which is ignored for the update requests. The first part is a vendor ID where only a few options seem relevant (I checked 10, 48 and 66). The rest of the version number can be easily enumerated. Many firmware branches donât have an active update, and when they do some updates wonât download because the servers in question appear no longer operational. Still, I found 380 updates this way.

I managed to [unpack all but one of these updates](/2025/12/15/unpacking-vstarcam-firmware-for-fun-and-profit/). Firmware version 10.1.110.2 wasnât for a camera but rather some device with an HDMI connector and without any P2P functionality â probably a Network Video Recorder (NVR). Firmware version 10.121.160.42 wasnât using PPPP but something called NHEP2P and an entirely different application-level protocol. Ten updates werenât updating the camera application but only the base system. This left 367 firmware versions for this investigation.

## Caveats of this survey

I do not own any VStarcam hardware, nor would it be feasible to investigate hundreds of different firmware versions with real hardware. The results of this article are based solely on reverse engineering, emulation, and automated analysis via running Ghidra in headless mode. While I can easily emulate a PPPP server, doing the same for the VStarcam cloud infrastructure isnât possible, I simply donât know how it behaves. Similarly, the firmwareâs interaction with hardware had to be left out of the emulation. While Iâm still quite confident in my results, these limitations could introduce errors.

More importantly, there are only so many firmware versions that I checked manually. Most of them were checked automatically, and I typically only looked at a few lines of decompiled code that my scripts extracted. There is potential for false negatives here, I expect that there are more issues with VStarcam firmware than whatâs listed here.

## VStarcamâs authentication approach

When an app communicates with a camera, it sends commands like `GET /check_user.cgi?loginuse=admin&loginpas=888888&user=admin&pwd=888888`. Despite the looks of it, these arenât HTTP requests passed on to a web server. Instead, the firmware handles these in function `P2pCgiParamFunction` which doesnât even attempt to parse the request. The processing code looks for substrings like `check_user.cgi` to identify the command (yes, you better donât set `check_user.cgi` as your access password). Parameter extraction works via similar substring matching.

Itâs worth noting that these cameras have a very peculiar authentication system which VStarcam calls âdual authentication.â Here is how the Eye4 application describes it:

> The dual authentication mechanism is a measure to upgrade the whole system security
>
> 1. The device will double check the identity of the visitor and does not support the old version of app.
> 2. Considering the security risk of possible leakage, the plaintext password mode of the device was turned off and ciphertext access was used.
> 3. After the device is added for the first time, it will not be allowed to be added for a second time, and it will be shared by the person who has added it.

Iâm not saying that this description is utter bullshit but there is a considerable mismatch with the reality that I can observe. The VStarcam firmware cannot accept anything other than plaintext passwords. Newer firmware versions employ obfuscation on the PPPP-level but this [hardly deserves the name âciphertextâ](/2026/01/05/analysis-of-pppp-encryption/).

What I can see is: once a device is enrolled into dual authentication, the authentication is handled by function `GetUserPri_doubleVerify` rather than `GetUserPri`. There isnât a big difference between the two, both will try the credentials from the `loginuse`/`loginpas` parameters and fall back to the `user`/`pwd` credentials pair. Function `GetUserPri_doubleVerify` merely checks a *different* password.

From the applications I get the impression that the dual authentication password is automatically generated and probably not even shared with the user but stored in their cloud account. This is an improvement over the regular password that defaults to `888888` and allow...