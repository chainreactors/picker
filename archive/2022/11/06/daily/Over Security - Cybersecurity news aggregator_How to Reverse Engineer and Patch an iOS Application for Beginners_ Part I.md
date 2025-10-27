---
title: How to Reverse Engineer and Patch an iOS Application for Beginners: Part I
url: https://www.inversecos.com/2022/06/how-to-reverse-engineer-and-patch-ios.html
source: Over Security - Cybersecurity news aggregator
date: 2022-11-06
fetch_date: 2025-10-03T21:50:33.565376
---

# How to Reverse Engineer and Patch an iOS Application for Beginners: Part I

[Skip to main content](#main)

### Search This Blog

# [@inversecos](https://www.inversecos.com/)

my research :D

### How to Reverse Engineer and Patch an iOS Application for Beginners: Part I

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

-
[June 06, 2022](https://www.inversecos.com/2022/06/how-to-reverse-engineer-and-patch-ios.html "permanent link")

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjCvd7hlTQEINMUYmwIe3wPXmZOjZpRHApA7A7bTzuFnUtfWkVr8rwF7Wm34KfcwShmDNILjbq4Qx27YsFB39wbP9Vx5Cl2ffVs2dnYRxmsH2MK7SQ_77FjJ2rnDl97geikVxKWeDqwfYdN4X0TKYRcBmVITVVBzk0OJIpHefOI0vcnTQMmw5kmI_dfow/s16000/mac12.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjCvd7hlTQEINMUYmwIe3wPXmZOjZpRHApA7A7bTzuFnUtfWkVr8rwF7Wm34KfcwShmDNILjbq4Qx27YsFB39wbP9Vx5Cl2ffVs2dnYRxmsH2MK7SQ_77FjJ2rnDl97geikVxKWeDqwfYdN4X0TKYRcBmVITVVBzk0OJIpHefOI0vcnTQMmw5kmI_dfow/s1446/mac12.png)

**So you want to reverse and patch an iOS application? I got you >\_<**

If you’ve missed the blogs in the series, check them out below ^\_^
[Part 1: How to Reverse Engineer and Patch an iOS Application for Beginners](https://www.inversecos.com/2022/06/how-to-reverse-engineer-and-patch-ios.html)
[Part 2: Guide to Reversing and Exploiting iOS binaries: ARM64 ROP Chains](https://www.inversecos.com/2022/06/guide-to-reversing-and-exploiting-ios.html)
[Part 3: Heap Overflows on iOS ARM64: Heap Spraying, Use-After-Free](https://www.inversecos.com/2022/07/heap-overflows-on-ios-arm64-heap.html)

This blog is focused on reversing an iOS application I built for the purpose of showing beginners how to reverse and patch an iOS app. No fancy tools are required (IDA O.o), it's just you, me & a debugger <3

The app is a simple, unencrypted Objective-C application that just takes in a password and the goal of this is to bypass the password mechanism and get the success code. This blog post will focus on reversing/debugging the application and will not cover aspects of static analysis. The reason I wanted to write this is because I realised this topic is confusing for a lot of people and I wanted to try and write a blog that attempts to explain it in a more beginner-friendly way.

Originally, I planned this content to be a TikTok video, but I am sick of TikTok’s community guidelines and rules against any “offensive” security content. So… as a result, I’m probably going to be writing more blogs now.

The screenshot below shows you what my cute app looks like – it is called “breakmedaddy” and the left shows you attempting to put in passwords – and the right shows you the desired bypass screen.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhFCMIsgN7bX5DzjLz8NL3IFO22pek9h3V9AgHCW4x1WhwKGQXp8HZlMrKuX7pFPb7bWFBgVRxfYsu8VA2ew1Ewn74th7lgS5UcpU55DCL7cZkzcY8TAdsDWNCe1aTpltMJQDRqER3wIxxqWnTXUKbEx3zt9A3M81QcBxCsi64sOpi0IZyTCwNozB4brw/w630-h640/Screen%20Shot%202022-06-05%20at%201.08.59%20pm.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhFCMIsgN7bX5DzjLz8NL3IFO22pek9h3V9AgHCW4x1WhwKGQXp8HZlMrKuX7pFPb7bWFBgVRxfYsu8VA2ew1Ewn74th7lgS5UcpU55DCL7cZkzcY8TAdsDWNCe1aTpltMJQDRqER3wIxxqWnTXUKbEx3zt9A3M81QcBxCsi64sOpi0IZyTCwNozB4brw/s1478/Screen%20Shot%202022-06-05%20at%201.08.59%20pm.png)

Why did I build this in Objective-C and not Swift? Because your girl is a qt and a masochist :)! But also because Objective-C allows you to modify methods during run time which means it’s easier to hook into functions than if the app was built in Swift.

 If you want to follow along with this blog post, the app is available on my [GitHub](https://github.com/inversecos/ios-breakmedaddy) (the first thing I’ve ever uploaded publicly because I am shy >\_<):

* <https://github.com/inversecos/ios-breakmedaddy>

To make this as easy to understand as possible, I have broken the blog into three parts so you can skip to whatever part you are interested in:

* High level steps we will take (this is to demonstrate the logic behind how to perform something like this)
* Tools we will use for the analysis
* Reverse engineering and patching the application

**HIGH-LEVEL STEPS**

This is the logic we are going to follow in this tutorial:

1. Jailbreak an iOS device (I am using an old phone I had around which is running iOS 14.1).
2. Upload the application onto the jailbroken device via SSH and SFTP by unzipping the IPA file into the /Applications directory.
3. Restart Springboard (you can do this via CLI through SSH or through Respring which you can find in Cydia).
4. Open the application and keep it in the foreground with your phone unlocked
5. Using SSH find the PID of the application.
6. Hook into the running app process by using Cycript to allow you to look at instances from the runtime.
7. Use otool to review libraries present in the application.
8. Use pagestuff to review the structure of a Mach-o file (this will show you segments, headers, code signatures, symbol tables etc).
9. Locate any interesting method names and variable names.
10. Reverse and debug the Mach-O file through running debugserver on the iOS device and connecting to the running application process via LLDB.

**TOOLS WE'LL USE**

There are a lot of tools you can use to perform this, however, for the purpose of keeping this walkthrough lean, here are the analysis tools we will use:

* Otool Command – <https://www.unix.com/man-page/osx/1/otool/>
* Pagestuff Command - <https://www.unix.com/man-page/osx/1/pagestuff/>
* Cycript - <http://www.cycript.org/>
* LLDB - <https://lldb.llvm.org/>

**REVERSE ENGINEERING IOS GUIDE**

**Step 1: Jailbreak an iOS device and set up SSH,SFTP**I am not going to cover how to jailbreak a device as there are plenty of write-ups and videos about it. The phone I tested this on and built the application for was running iOS 14.1 and I used the unc0ver jailbreak here: <https://unc0ver.dev/>. The website for unc0ver explains in detail how to perform the jailbreak :)

Once the jailbreak is completed, go into Cydia and set up SSH. This is as simple as performing a search for “openssh” and installing it.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjcgWdyTXldNVe0JyY2DQR7rekgvfyb3glzCyZGa1qm7O89_KPF88iI0AbcL92Oi_5HpLMtjkZoK_BCSFUVT6OOBQkxcHeOTeqaAMFYUBxHtCXs5OBd2Vym1B_0sFj4So-2Kp3dUdaUkoRtshrDo5Omv_Gl9GKLqHYyShNSowDk2ldlQZUwFFOtO4veoA/w358-h640/Screen%20Shot%202022-06-05%20at%201.19.50%20pm.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjcgWdyTXldNVe0JyY2DQR7rekgvfyb3glzCyZGa1qm7O89_KPF88iI0AbcL92Oi_5HpLMtjkZoK_BCSFUVT6OOBQkxcHeOTeqaAMFYUBxHtCXs5OBd2Vym1B_0sFj4So-2Kp3dUdaUkoRtshrDo5Omv_Gl9GKLqHYyShNSowDk2ldlQZUwFFOtO4veoA/s1338/Screen%20Shot%202022-06-05%20at%201.19.50%20pm.png)

**Step 2: Upload the application onto the jailbroken device via SFTP and unzip it into the Applications directory**

You can do this by SFTPing the file into your iOS device /Applications directory and then unzipping it. The format of the file is a “.ipa” file which has been built in XCode. The .ipa file is a zipped file which you can unzip directly onto the phone. Just download the IPA file from my Github and don’t peep the source code because you are not a cheater!

Download: <https://github.com/inversecos/ios-breakmedaddy>

The result is something like this:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiE9EOsl38pRyi9RhNObhMsmgiT8JflrIq9A4yfxINUFQavmXQ0ra-BvibiLKW1AP9wzGJCx9BCvN7fVj6eRQ1tf8jIxe91yJDKhIlXDH_8X5RG0ZSHGoYRD_xfnYmq9r-RBds4eRzZAgayLnd65YVy01TxtsnpG5Kb2MMByQl6YXlywQ5-Pwok37WXHQ/s16000/loadapp.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiE9EOsl38pRyi9RhNObhMsmgiT8JflrIq9A4yfxINUFQavmXQ0ra-BvibiLKW1AP9wzGJCx9BCvN7fVj6eRQ1tf8jIxe91yJDKhIlXDH_8X5RG0ZSHGoYRD_xfnYmq9r-RBds4eRzZAgayLnd65YVy01TxtsnpG5Kb2MMByQl6YXlywQ5-Pwok37WXHQ/s720/loadapp.png)

**Step 3: Restart Springboard to make the app appear**

You can do this one of two ways – either kill SpringBoard via the CLI, or you can download ReSpring in Cydia and run it that way. For some conte...