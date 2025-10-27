---
title: Scrcpy - Display And Control Your Android Device
url: https://buaq.net/go-136935.html
source: unSafe.sh - 不安全
date: 2022-11-24
fetch_date: 2025-10-03T23:36:58.152368
---

# Scrcpy - Display And Control Your Android Device

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/f908aae3f64ac62feb85653a524ce4d2.jpg)

Scrcpy - Display And Control Your Android Device

pronounced "screen copy"Read in another languageThis application provides display and contr
*2022-11-23 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-136935.htm)
阅读量:31
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZQ6iUZri26i3AtUuPkyoNqCvuEUC1TI7pJHoNxsqA9UvivOyCACAfbcdEVSETzgmGP1yGpG9CmllKCR5AW44QjADGHsfvf56l4NFQmU5Vu73RZfc7XJ9tBvX_UeGJX4Oi4TZzRU3O1fr7nBXmwqSOX50nH_3go0_KaPa7PtvYotVihwRYP-3fAwmg_Q/s16000/scrcpy_2_screenshot-debian-600.jpeg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZQ6iUZri26i3AtUuPkyoNqCvuEUC1TI7pJHoNxsqA9UvivOyCACAfbcdEVSETzgmGP1yGpG9CmllKCR5AW44QjADGHsfvf56l4NFQmU5Vu73RZfc7XJ9tBvX_UeGJX4Oi4TZzRU3O1fr7nBXmwqSOX50nH_3go0_KaPa7PtvYotVihwRYP-3fAwmg_Q/s600/scrcpy_2_screenshot-debian-600.jpeg)

*pronounced "**scr**een **c**o**py**"*

[Read in another language](https://github.com/Genymobile/scrcpy#translations "Read in another language")

This application provides display and control of Android devices connected via
USB or [over TCP/IP](https://github.com/Genymobile/scrcpy#tcpip-wireless "over TCP/IP"). It does not require any *root* access.
It works on *GNU/Linux*, *Windows* and *macOS*.

It focuses on:

* **lightness**: native, displays only the device screen
* **performance**: 30~120fps, depending on the device
* **quality**: 1920×1080 or above
* **low latency**: [35~70ms](https://github.com/Genymobile/scrcpy/pull/646 "35~70ms")
* **low startup time**: ~1 second to display the first image
* **non-intrusiveness**: nothing is left installed on the Android device
* **user benefits**: no account, no ads, no internet required
* **freedom**: free and open source software

Its features include:

* [recording](https://github.com/Genymobile/scrcpy#recording "recording")
* mirroring with [Android device screen off](https://github.com/Genymobile/scrcpy#turn-screen-off "Android device screen off")
* [copy-paste](https://github.com/Genymobile/scrcpy#copy-paste "copy-paste") in both directions
* [configurable quality](https://github.com/Genymobile/scrcpy#capture-configuration "configurable quality")
* Android device [as a webcam (V4L2)](https://github.com/Genymobile/scrcpy#v4l2loopback "as a webcam (V4L2)") (Linux-only)
* [physical keyboard](https://github.com/Genymobile/scrcpy#physical-keyboard-simulation-hid "physical keyboard") [simulation](https://www.kitploit.com/search/label/Simulation "simulation") (HID)
* [physical mouse simulation (HID)](https://github.com/Genymobile/scrcpy#physical-mouse-simulation-hid "physical mouse simulation (HID)")
* [OTG mode](https://github.com/Genymobile/scrcpy#otg "OTG mode")
* and more…

## Requirements

The Android device requires at least API 21 (Android 5.0).

Make sure you [enable adb debugging](https://developer.android.com/studio/command-line/adb.html#Enabling "enable adb debugging") on your device(s).

On some devices, you also need to enable [an additional option](https://github.com/Genymobile/scrcpy/issues/70#issuecomment-373286323 "an additional option") to
control it using a keyboard and mouse.

## Get the app

### Summary

* Linux: `apt install scrcpy`
* Windows: [download](https://github.com/Genymobile/scrcpy/releases/download/v1.24/scrcpy-win64-v1.24.zip "download")
* macOS: `brew install scrcpy`

Build from sources: [BUILD](https://github.com/Genymobile/scrcpy/blob/master/BUILD.md "BUILD") ([simplified process](https://github.com/Genymobile/scrcpy/blob/master/BUILD.md#simple "simplified process"))

### Linux

On Debian and Ubuntu:

On Arch Linux:

A [Snap](https://en.wikipedia.org/wiki/Snappy_%28package_manager%29 "Snap") package is available: [`scrcpy`](https://snapstats.org/snaps/scrcpy "Display and control your Android device (22)").

For Fedora, a [COPR](https://fedoraproject.org/wiki/Category%3ACopr "COPR") package is available: [`scrcpy`](https://copr.fedorainfracloud.org/coprs/zeno/scrcpy/ "Display and control your Android device (24)").

For Gentoo, an [Ebuild](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") is available: [`scrcpy/`](https://github.com/maggu2810/maggu2810-overlay/tree/master/app-mobilephone/scrcpy "Display and control your Android device (26)").

You can also [build the app manually](https://github.com/Genymobile/scrcpy/blob/master/BUILD.md "build the app manually") ([simplified
process](https://github.com/Genymobile/scrcpy/blob/master/BUILD.md#simple "simplified
process")).

### Windows

For Windows, a prebuilt archive with all the dependencies (including `adb`) is
available:

* [`scrcpy-win64-v1.24.zip`](https://github.com/Genymobile/scrcpy/releases/download/v1.24/scrcpy-win64-v1.24.zip "Display and control your Android device (29)")

It is also available in [Chocolatey](https://chocolatey.org/ "Chocolatey"):

```
choco install scrcpy
choco install adb    # if you don't have it yet
```

And in [Scoop](https://scoop.sh "Scoop"):

```
scoop install scrcpy
scoop install adb    # if you don't have it yet
```

You can also [build the app manually](https://github.com/Genymobile/scrcpy/blob/master/BUILD.md "build the app manually").

### macOS

The application is available in [Homebrew](https://brew.sh/ "Homebrew"). Just install it:

You need `adb`, accessible from your `PATH`. If you don't have it yet:

```
brew install android-platform-tools
```

It's also available in [MacPorts](https://www.macports.org/ "MacPorts"), which sets up `adb` for you:

You can also [build the app manually](https://github.com/Genymobile/scrcpy/blob/master/BUILD.md "build the app manually").

## Run

Plug an Android device into your computer, and execute:

It accepts command-line arguments, listed by:

## Features

### Capture configuration

#### Reduce size

Sometimes, it is useful to mirror an Android device at a lower resolution to
increase performance.

To limit both the width and height to some value (e.g. 1024):

```
scrcpy --max-size 1024
scrcpy -m 1024  # short version
```

The other dimension is computed so that the Android device aspect ratio is
preserved. That way, a device in 1920×1080 will be mirrored at 1024×576.

#### Change bit-rate

The default bit-rate is 8 Mbps. To change the video bitrate (e.g. to 2 Mbps):

```
scrcpy --bit-rate 2M
scrcpy -b 2M  # short version
```

#### Limit frame rate

The capture frame rate can be limited:

This is officially supported since Android 10, but may work on earlier versions.

The actual capture framerate may be printed to the console:

It may also be enabled or disabled at any time with `MOD`+`i`.

#### Crop

The device screen may be cropped to mirror only part of the screen.

This is useful, for example, to mirror only one eye of the Oculus Go:

```
scrcpy --crop 1224:1440:0:0   # 1224x1440 at offset (0,0)
```

If `--max-size` is also specified, resizing is applied after cropping.

#### Lock video orientation

To lock the orientation of the mirroring:

```
scrcpy --lock-video-orientation     # initial (current) orientation
scrcpy --lock-video-orientation=0   # natural orientation
scrcpy --lock-video-orientation=1   # 90° counterclockwise
scrcpy --lock-video-orientation=2   # 180°
scrcpy --lock-video-orientation=3   # 90° clockwise
```

This affects recording orientation.

The [window may also be rotated](https://github.com/Genymobile/scrcpy#rotation "window may also be rotated") independently.

#### Encoder

Some devices have more than one encoder, and some of them may cause issues or
crash. It is possible to select a different encoder:

```
scrcpy --encoder OMX.qcom.video.encoder.avc
```

To list the available encoders, you can p...