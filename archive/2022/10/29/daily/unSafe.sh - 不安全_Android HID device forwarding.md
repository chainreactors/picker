---
title: Android HID device forwarding
url: https://buaq.net/go-133132.html
source: unSafe.sh - 不安全
date: 2022-10-29
fetch_date: 2025-10-03T21:11:24.030996
---

# Android HID device forwarding

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

![]()

Android HID device forwarding

As I mentioned in my previous post, Immersed (https://immersed.com) i
*2022-10-28 20:26:38
Author: [clevcode.org(查看原文)](/jump-133132.htm)
阅读量:19
收藏*

---

As I mentioned in my previous post, Immersed (https://immersed.com) is a great multi-platform (Linux/macOS/Windows) solution for sharing your screens to a VR environment. Unlike Virtual Desktop that is focused mostly on gaming (and more importantly, that does not have a Linux version), Immersed is focused on productivity and being a substitute for a real-world multi-monitor workstation setup.

Here is a video of one of my first experiences with Immersed, where I used 3 x 1920×1080 screens and 2 x 1920×360 above and below the rest (since then, I have switched to using 3 x 1920×2160 + 1 x 1920×1080, to get a setup equivalent to 7 x 1920×1080 screens):

One of the issues I had was that I needed to use a keyboard connected directly to my computer, which didn’t allow me to move around within my apartment (for instance, lying down in my bed with my ThinkPad TrackPoint Keyboard II on my lap, for supine computing, while being connected to the workstation in my office area). And of course, if you are working remotely and connected over VPN to the network with the actual computer, it’s an even bigger issue.

Immersed has built-in support for forwarding a keyboard that is connected to the VR headset over bluetooth, but since certain keys (specifically the Windows/Super-key) is being hijacked by Android this is not enough for my purposes. It also has built-in support for forwarding a mouse, but I am personally not a fan of the mouse cursor being part of the VR environment (this is mostly a matter of taste, though), so I wanted to find a way to just transparently forward that as well.

After asking on a few forums whether anyone had a solution to avoid Android hijacking keys, and reading Android sources to figure out where it happens (which is in the WindowManagerPolicy implementation, i.e. the PhoneWindowManager class on a regular Android phone), I finally decided to solve it myself.

My final motivation to solve it myself was a nonsensical reply from someone on a coding forum that said that it wasn’t possible because the “driver” determines how keys should be interpreted (which is obviously not true, since the driver just produces a stream of events to be consumed and processed by something else in the system). Of course, I had to prove him wrong. ;)

Turns out, when connecting to the VR headset (tested on the Quest 2 as well as the Pico 4) over ADB, the shell user has access to the /dev/input/eventX pseudo character devices that represent HID devices such as keyboards and mice. This allows us to get exclusive access to the key presses and/or mouse events for the devices in question, by using the EVIOCGRAB ioctl, and to forward all events as-is to the computer we are connected to over Immersed, or any other Android-based remote-desktop-solution.

On the computer-side, we then need another program to inject the events back into the system. Since I am primarily using Linux, I can simply inject them by leveraging /dev/uinput to simulate the remote device being plugged into the computer and inject the events forwarded from the VR headset as-is. It would be relatively simple to create macOS and Windows-versions of this component to be able to use this solution there as well though.

Linux-users with Immersed are welcome to try my solution out by following these steps, and macOS/Windows-users are more than welcome to implement the “HID writer” component for their respective operating system:

1. First of all, you need to enable developer-mode and allow USB debugging. For the Quest 2, follow the steps here:

* <https://developer.oculus.com/documentation/native/android/mobile-device-setup/>

On the Pico 4, it is even easier. Just activate developer mode with these steps:

* <https://vr-expert.com/kb/how-to-activate-developer-mode-on-the-pico-4/>

Then go into Developer Options and enable “Allow USB debugging”.

2. Install ADB. Here is a guide on how to install ADB on Windows, macOS and Linux:

* <https://www.xda-developers.com/install-adb-windows-macos-linux/>

3. Download the HID-reader component I developed to run on your Android-based VR headset:

* <https://clevcode.org/files/hid-reader>

If you want to compile the HID-reader binary yourself, you can follow these steps:

Download and extract the Android NDK from:

* <https://developer.android.com/ndk/downloads>

Download the HID-reader source from:

* <https://clevcode.org/files/hid-reader.c>

Set the ANDROID\_NDK environment variable to the NDK directory, and run the following (on Linux, to compile on Windows or macOS you need to change the “linux-x86\_64” part):

`$ANDROID_NDK/toolchains/llvm/prebuilt/linux-x86_64/bin/clang --target=aarch64-none-linux-android21 --sysroot=$ANDROID_NDK/toolchains/llvm/prebuilt/linux-x86_64/sysroot -g -DANDROID -o hid-reader hid-reader.c`

4. Download the HID-writer (injector) component I developed to run on your Linux system:

* <https://clevcode.org/files/hid-writer>

It has been statically compiled to avoid any library dependency issues (i.e. different libc versions).

Now make the binary executable with:

`chmod 700 hid-writer`

If you want to compile the HID-writer binary yourself, you can download the source from:

* <https://clevcode.org/files/hid-writer.c>

If someone would take the time to port this part to macOS and Windows, that would be perfect. :) You just need to find a suitable alternative for the Linux-specific uinput subsystem to inject keyboard/mouse events, and map the type/code/value fields of the proxy\_event struct into something appropriate for what you are using to inject the events with.

5. Connect your headset to your computer with a USB cable, and run the following from a command prompt on your computer to upload the HID-reader binary to your VR headset (tested on Quest 2 and Pico 4, but this should work on any Android-based VR headset):

`adb push hid-reader /data/local/tmp`

`adb shell chmod 700 /data/local/tmp/hid-reader`

The first time you run this, you will likely be prompted to allow the ADB connection in your VR headset.

6. To not have to remain plugged into your VR headset with a USB cable, you can now enable ADB over WiFi (this needs to be repeated after restarting your headset, btw):

adb tcpip 5555

adb connect <IP of your VR headset>:5555

After this, feel free to unplug the headset from USB.

7. At this point, I have not implemented any automatic way to determine which of the devices under /dev/input on your VR headset that corresponds to your keyboard and/or mouse, but in general you can follow these steps to determine that. First run the following, before pairing your keyboard and/or mouse:

`adb shell ls -l /dev/input`

You will see a list of eventN-files, where N goes from 0 and up. Now pair your keyboard and/or mouse and run the command again.

For any new eventN-files that has popped up, run the following:

adb exec-out /data/local/tmp/hid-reader /dev/input/eventN | ./hid-writer

You need to run each of these in a separate shell, since the programs will run in the foreground. If you want to run it in the background, I suggest you run it from within a tmux/screen-session.

Now, enjoy moving around with your VR headset and keyboard/mouse, not having to worry about being in physical proximity to the computer you are connected to and not having any issues with keys being intercepted by Android! :)

PS. As an alternative to step 5, you can instead upload an Android version of the Dropbear SSH server to ...