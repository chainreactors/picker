---
title: Android HID device forwarding
url: https://clevcode.org/android-hid-device-forwarding/
source: ClevCode
date: 2022-10-29
fetch_date: 2025-10-03T21:12:50.633776
---

# Android HID device forwarding

[Skip to content](#page)

[ClevCode](https://clevcode.org/)

Vulnerability Research, Exploit Development, Reverse-Engineering

### Recent Posts

* [Ashley Madison Post-Mortem](https://clevcode.org/ashley-madison-post-mortem/)
* [Android HID device forwarding](https://clevcode.org/android-hid-device-forwarding/)
* [Low-latency VR desktop with Immersed](https://clevcode.org/low-latency-vr-desktop-with-immersed/)
* [31C3 CTF: Maze write-up](https://clevcode.org/31c3-ctf-maze-write-up/)
* [Ghost in The Shellcode 2015 Teaser: Citadel solution](https://clevcode.org/ghost-in-the-shellcode-2015-teaser-citadel-solution/)

### Categories

* [Ashley Madison](https://clevcode.org/category/ashley-madison/) (1)
* [Codegate](https://clevcode.org/category/codegate/) (1)
* [CTF](https://clevcode.org/category/ctf/) (13)
* [Exploit Development](https://clevcode.org/category/exploit-development/) (7)
* [GCHQ](https://clevcode.org/category/gchq/) (3)
* [Mentorship](https://clevcode.org/category/mentorship/) (1)
* [Plaid CTF](https://clevcode.org/category/plaidctf/) (12)
* [Research](https://clevcode.org/category/research/) (4)
* [Reverse-Engineering](https://clevcode.org/category/reverse-engineering/) (1)
* [Team](https://clevcode.org/category/team/) (3)
* [VR/XR/MR](https://clevcode.org/category/vr-xr-mr/) (2)
* [Work](https://clevcode.org/category/work/) (1)
* [Writeup](https://clevcode.org/category/ctf/writeup/) (15)

### People

* [Gynvael Coldwind](http://gynvael.coldwind.pl/)
* [Halvar Flake](http://addxorrol.blogspot.com/)
* [j00ru](http://j00ru.vexillium.org/)
* [Joshua J. Drake](http://twitter.com/jduck)
* [Michal Zalewski](http://lcamtuf.blogspot.com/)
* [Rolf Rolles](http://twitter.com/rolfrolles)
* [Sean Heelan](http://seanhn.wordpress.com/)

### Tools

* [BinaryNinja](https://binary.ninja/)
* [GDB](http://www.gnu.org/software/gdb/)
* [Ghidra](https://ghidra-sre.org/)
* [IDA Pro](http://www.hex-rays.com/idapro/)
* [Neovim](https://neovim.io/)
* [OllyDbg](http://www.ollydbg.de/)
* [Vim](http://www.vim.org/)
* [x64dbg](https://x64dbg.com/)

Expand Menu

* [ClevCode](https://clevcode.org/)
* [About](https://clevcode.org/about/)
* [Team](https://clevcode.org/team/)
* [Solving Cicada 3301](https://clevcode.org/cicada-3301/)
* [GCHQ](https://clevcode.org/canyoucrackit-co-uk-gchq-challenge-solution/)
* [pCTF](https://clevcode.org/pctf/)
* [Contact](https://clevcode.org/contact/)

![](https://clevcode.org/wp-content/uploads/2022/10/profile.jpg)

Joel Eriksson

Vulnerability researcher, exploit developer and reverse-engineer. Have spoken at BlackHat, DefCon and the RSA conference. CTF player. Puzzle solver (Cicada 3301, Boxen)

# Android HID device forwarding

2022-10-28
[0](https://clevcode.org/android-hid-device-forwarding/#respond)
[Joel Eriksson](https://clevcode.org/author/je/ "Posts by Joel Eriksson")
[VR/XR/MR](https://clevcode.org/category/vr-xr-mr/)

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

If you wan...