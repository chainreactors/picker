---
title: Low-latency VR desktop with Immersed
url: https://clevcode.org/low-latency-vr-desktop-with-immersed/
source: ClevCode
date: 2022-10-28
fetch_date: 2025-10-03T21:06:23.578057
---

# Low-latency VR desktop with Immersed

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

# Low-latency VR desktop with Immersed

2022-10-27
[0](https://clevcode.org/low-latency-vr-desktop-with-immersed/#respond)
[Joel Eriksson](https://clevcode.org/author/je/ "Posts by Joel Eriksson")
[VR/XR/MR](https://clevcode.org/category/vr-xr-mr/)

Immersed (<https://immersed.com>) is a multi-platform solution (Linux/macOS/Windows) for sharing your monitors (including a couple of virtual ones) to a VR environment. It currently supports the popular Quest and Quest 2 headsets, as well as the VIVE Focus 3, and a version for Pico 4 as well as the Quest Pro will be released shortly.

It can be used completely wireless, and under ideal conditions the latency is low enough for most purposes. My current wireless setup at home (802.11ac/WiFi 5-based) usually has a 5ms latency, even when I’m sharing an equivalent of 7 x 1920×1080 screens (3 x 1920×2160 + 1 x 1920×1080).

Here is a video of one of my first experiences with Immersed, where I used 3 x 1920×1080 screens and 2 x 1920×360 above and below the rest:

In some cases, getting a low latency setup might require a bit of work though, and it might not always be possible. Especially if you are using it in an environment that you don’t have any control over, such as a hotel-WiFi or maybe just using your phone as a hotspot on the road.

In those cases, it might be preferable to tether your headset to your laptop/computer over a USB cable. I was able to do this in two different ways. First of all, you can set up “reverse USB tethering” to share your internet connection from your computer to your headset, with the following project:

* <https://github.com/Genymobile/gnirehtet>

The disadvantage with this is that all traffic will be routed through two usermode applications, one on the headset and one on your computer, which adds overhead and latency. The latency will most likely be good-enough for most intents and purposes, but let’s take this one step further, because why not? ;)

1. First of all, you need to enable developer-mode and allow USB debugging. This step is required if you’re going for the “gnirehtet” based soluton as well, btw. For the Quest 2, follow the steps here:

* <https://developer.oculus.com/documentation/native/android/mobile-device-setup/>

On the Pico 4, it is even easier. Just activate developer mode with these steps:

* <https://vr-expert.com/kb/how-to-activate-developer-mode-on-the-pico-4/>

Then go into Developer Options and enable “Allow USB debugging”.

2. Next step, edit ~/.ImmersedConf (~/Library/Preferences/team.Immersed.plist on macOS). Change “ForceIPAddress”: “” to “ForceIPAddress:”127.0.0.1” within the JSON data in the Data-field.

Note that .ImmersedConf is overwritten when the agent exits, and possibly on startup, so your changes may possibly disappear. To avoid this, I personally used a very crude workaround, by setting the “immutable” flag in the file attributes:

`sudo chattr +i ~/.ImmersedConf`

Or in macOS:

`chflags uchg ~/Library/Preferences/team.Immersed.plist`

I think it might be enough to just make sure to close the agent before you modify the file though.

3. Connect your headset to your computer with a USB cable, and run the following from a command prompt on your computer:

`adb reverse tcp:21000 tcp:21000`

Note that you will have to do this again every time you plug in the headset after unplugging it. Verify with “`adb reverse --list`” that the port forwarding is active if you have any issues.

Here is a guide on how to install ADB on Windows, macOS and Linux:

* <https://www.xda-developers.com/install-adb-windows-macos-linux/>

4. Next, a very important step for this to work right now. At the moment the ForceIPAddress setting will only be used if the agent side is not responding to broadcast UDP packets, so we need to block that from happening.

UPDATE! The Immersed developer team has now confirmed that UDP broadcast blocking will not be necessary in the next release, so in the future this step can be skipped! :)

First, look up your IP and the broadcast address for your subnet. In Linux, use “ifconfig” or “ip -o a” to determine that. The broadcast address is usually just your IP address but with the last number replaced with 255. For instance, it might be 192.168.1.255, so in this case you can block UDP packets to this address in Linux with the following command:

`sudo iptables -I INPUT -p udp -d 192.168.1.255 -j DROP`

In macOS you can edit /etc/pf.conf and add the following rule:

`block in proto udp from any to 192.168.1.255`

Then enable PF with “sudo pfctl -e” and “sudo pfctl -f /etc/pf.conf” to load the new configuration.

And in Windows I think the following command should do it:

`netsh advfirewall firewall add rule name="BlockUDPBroadcast" protocol=UDP dir=in localip=192.168.1.255 action=block`

In each case, change 192.168.1.255 to the broadcast address of your WiFi subnet.

5. Follow these steps in exactly this order:

* Close the Immersed app on your headset.
* Close the Immersed agent on your computer.
* Verify that ForceIPAddress is still set to 127.0.0.1 in .ImmersedConf/team.Immersed.plist
* Start the Immersed app on your headset, and go to the list of computers.
* Start the Immersed agent on your computer.
* Connect to your computer in the Immersed app.

The reason we do things in this order is to ensure that the Immersed app doesn...