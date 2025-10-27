---
title: macOS Frida Setup
url: https://naehrdine.blogspot.com/2022/11/macos-frida-setup.html
source: cat /dev/brain
date: 2022-11-21
fetch_date: 2025-10-03T23:20:04.877834
---

# macOS Frida Setup

[Skip to main content](#main)

### Search This Blog

# [cat /dev/brain](https://naehrdine.blogspot.com/)

Reverse Engineering & Research

### macOS Frida Setup

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

[November 20, 2022](https://naehrdine.blogspot.com/2022/11/macos-frida-setup.html "permanent link")

On an M1 Mac, Frida needs some extra steps to be able to attach to system processes. Mainly writing this down here because it was spread across multiple GitHub issues. Hope it helps some of you who are working with Frida on M1 Macs :)

### Versions

* macOS Ventura 13.0.1
* Frida 16.0.2
* Apple M1 Pro

### Setup

* Disable System Integrity Protection (SIP). Power off Mac, power on with very long press to get the advanced boot options, open the Terminal from the Utilities, enter
  # csrutil disable
  ... and confirm that this bricks your system's security.
* Disable some dialogues popping up and asking for permissions, further reducing the security of your system with
  # sudo security authorizationdb write system.privilege.taskport allow
  ... this might be optional but needed if you use Frida via SSH.
* Change boot arguments as follows:
  sudo nvram boot-args=-arm64e\_preview\_abi
  ... and reboot.

Now you should be able to attach to system services, e.g., run:

# frida identityservicesd

### Update: macOS 14.4 and higher

Since the introduction of macOS 14.4, there are new mitigations that prevent Frida from attaching to macOS processes, even on SIP disabled systems. Following two tweets from CodeColorist and patch1t, here are further NVRAM arguments that need to be set:

# nvram boot-args="-arm64e\_preview\_abi amfi\_get\_out\_of\_my\_way=1 thid\_should\_crash=0 tss\_should\_crash=0"

Without these boot arguments, the target process will crash with an error similar to this:

Crashed Thread:        1  frida-helper-main-loop

Exception Type:        EXC\_GUARD (SIGKILL)

Exception Codes:       GUARD\_TYPE\_MACH\_PORT

Exception Codes:       0x0000000000000000, 0x0000000000000000

Termination Reason:    Namespace GUARD, Code 2305843030688530432

External Modification Warnings:

Process used task\_for\_pid().

### Debugging

The first two steps are currently also described on the [Frida website](https://frida.re/docs/troubleshooting/). Without the adjusted boot arguments, Frida quits with the following error message - apparently on M1 Macs only:

Failed to attach: unexpected error while starting thread (set\_thread\_state returned '(os/kern) protection failure')

Looking for frida in the Console app, there are three matching messages. The first is the command I ran, the next one is a sandbox error for \_frida.abi3.so, and the last one is the one that hints towards the missing boot argument, as it complains about the arm64e preview abi.

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

### Comments

#### Post a Comment

### Popular posts from this blog

### [Reverse Engineering iOS 18 Inactivity Reboot](https://naehrdine.blogspot.com/2024/11/reverse-engineering-ios-18-inactivity.html)

[November 17, 2024](https://naehrdine.blogspot.com/2024/11/reverse-engineering-ios-18-inactivity.html "permanent link")

[![Image](https://blogger.googleusercontent.com/img/a/AVvXsEihQqOut8zLHRxuz_g8ornTF1A-X69IoWpX8lZPnZBisvc1t80zBRGebsCj4x4Vz_6C_i_ImG5AszaaQ-rXnFEJeB1-Dfaj4bSBwajxyKLYoKQNdJ8dZZtaqhexYUc1rZL7w_6yXkMj5APTe30fHOMRlg3da55UCxSZhmTFRLWmBEh_iWVgPSyKuVCEQ_48=w640-h352)](https://naehrdine.blogspot.com/2024/11/reverse-engineering-ios-18-inactivity.html)

Reverse Engineering iOS 18 Inactivity Reboot iOS 18 introduced a new inactivity reboot security feature. What does it protect from and how does it work? This blog post covers all the details down to a kernel extension and the Secure Enclave Processor. Security Before First Unlock / After First Unlock Did you know that entering your passcode for the first time after your phone starts is something very different then entering it later on to unlock your phone? When initially entering your passcode, this unlocks a key store in the Secure Enclave Processor (SEP) that encrypts your data on an iPhone. The state before entering your passcode for the first time is also called Before First Unlock (BFU). Due to the encrypted user data, your iPhone behaves slightly differently to later unlocks. You'll see that Face ID and Touch ID won't work and that the passcode is required. But there's more subtle things you might notice: Since Wi-Fi passwords are encrypted, your iPhone won't co...

[Read more](https://naehrdine.blogspot.com/2024/11/reverse-engineering-ios-18-inactivity.html "Reverse Engineering iOS 18 Inactivity Reboot")

### [Always-on Processor magic: How Find My works while iPhone is powered off](https://naehrdine.blogspot.com/2021/09/always-on-processor-magic-how-find-my.html)

[September 30, 2021](https://naehrdine.blogspot.com/2021/09/always-on-processor-magic-how-find-my.html "permanent link")

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9lNqrrsbcDxLXDljXeOmeFO3UZzfvQL7z33gwC_NMsKtQV2wnVCzXlUKtR6iHO8h0CA-56GMmGGZy-luWlQaHwA1cmCJEmIVGp0zpvWirQKFU99KdKbghcthr4FRWpxidmoyqH0O7Fgk/w185-h400/IMG_6593.PNG)](https://naehrdine.blogspot.com/2021/09/always-on-processor-magic-how-find-my.html)

Update: We wrote a paper with even more technical details :) iOS 15.0 introduces a new feature: an iPhone can be located with Find My even while the iPhone is turned "off". How does it work? Is it a security concern? I saw this feature rather early on one of my iPhones with an iOS 15 beta. Here's a screenshot I took in July. The user interface changed a little bit since then. It took a bit longer until the public realized this feature exists. One needs to update to iOS 15.0, use an iPhone that has location services enabled, a logged in user account, participates in the Find My network, etc. And the weirdest thing nobody does these days: One has to turn the iPhone off. But once Twitter found out, this took off. And so did the rumors how this was implemented. Apple's Always-on Processor (AOP) There's only little public documentation about the AOP. All chips and various embedded devices Apple manufactures run a real-time operating system, called RTKitOS. The AOP on ...

[Read more](https://naehrdine.blogspot.com/2021/09/always-on-processor-magic-how-find-my.html "Always-on Processor magic: How Find My works while iPhone is powered off")

### [BlueZ: Linux Bluetooth Stack Overview](https://naehrdine.blogspot.com/2021/03/bluez-linux-bluetooth-stack-overview.html)

[March 04, 2021](https://naehrdine.blogspot.com/2021/03/bluez-linux-bluetooth-stack-overview.html "permanent link")

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXrhj47IPKRSZYfRORl2vV0ElgcuxFuUy7moHvAMMiadNRkp0iKsNfiwA7skWkvfKX_XbwXC1s32DSmSrkYLdPdk-nyHVZugUapdOFs50q9GnzbRVfktxnmqL1m5CTFi4wZE4MuoOG9pU/w400-h295/image.png)](https://naehrdine.blogspot.com/2021/03/bluez-linux-bluetooth-stack-overview.html)

Found some time for another Bluetooth rant :) This time it's going to be about BlueZ , the Linux Bluetooth stack. Note that there are other Bluetooth stacks for Linux such as BTstack , but I didn't find the time to play around with these, and BlueZ is still what you get these days if you install a normal Linux distribution. This is my view on about BlueZ and a couple of things might be over-simplified. Feel free to add comments to this post if anything is wrong or is better explained elsewhere. However, I found that there is no good overview from a programming and hacking perspective, and often times I get questions about patching certain things within InternalBlue that have a root cause deep down in the Linux kernel. BlueZ is missing documentation. In fact, I ended up using dynamic debugging here and there to understand which functions are still called and which are deprecated. Otherwise, this blog post would not be needed for an open-source project m) Linux Bluetooth stack vs...

[Read more](https://...