---
title: Flare-On 12: NTFSM - Solving a Finite State Machine with Binary Ninja
url: https://jhalon.github.io/flare-on-12-ntfsm/
source: Jack Hacks
date: 2025-11-13
fetch_date: 2025-11-14T03:13:49.529583
---

# Flare-On 12: NTFSM - Solving a Finite State Machine with Binary Ninja

* [Jack Hacks](https://jhalon.github.io/)
* [Posts](https://jhalon.github.io/posts.html)
* [Categories](https://jhalon.github.io/categories.html)
* [About](https://jhalon.github.io/about.html)

# Flare-On 12: NTFSM - Solving a Finite State Machine with Binary Ninja

![Jack Halon](https://jhalon.github.io/images/bio_chibi.png)

### Jack Halon

I like to break into things; both physically and virtually.

Follow

* United States
* Email
* [Twitter](https://twitter.com/jack_halon)
* [LinkedIn](https://www.linkedin.com/in/jacek-halon-683912b0)
* [Github](https://github.com/jhalon/)
* [YouTube](https://www.youtube.com/user/../JackHacks)

As the dust settles on this year’s Flare-On challenge, I finally found some time time to sit down and write about one of the more interesting challenges from this year: Challenge 5 - NTFSM. This challenge stood out to me because it not only provided me with an excellent opportunity to refine my reverse engineering skills, but it also allowed me to dig into a specific execution technique used in binaries and malware.

For those unfamiliar with [Flare-On](https://flare-on.com/), it’s basically an annual CTF for reverse engineers hosted by Mandiant’s (now Googles) [FLARE](https://cloud.google.com/security/flare) team. This years CTF had 9 stages of increasingly difficult challenges for single players to solve in sequence. Unfortunately for me, life got in the way and I only made it to Challenge 6 - but even with that, they were a blast.

Initially I solved this challenge using IDA Pro, as I had been using it for years, but I couldn’t shake the desire to try solving it with Binary Ninja instead. Why? Well, I really wanted to get my hands dirty with Binary Ninja’s powerful scripting capabilities, and this seemed like the perfect opportunity to do it.

So in this post, I’ll walk through not only the concepts and techniques behind cracking the NTFSM challenge, but also how I leveraged Binary Ninja’s API to solve it. I’ll break down the process, the logic, and the small “aha!” moments along the way - hopefully in a way that’s easy to follow, even if you’re newer to reverse engineering!

## Overview

Upon accessing the challenge we are provided with the following description:

> I’m not here to tell you how to do your job or anything, given that you are a top notch computer scientist who has solved four challenges already, but NTFS is in the filename. Maybe, I don’t know, run it in windows on an NTFS file system?

After downloading and unzipping the archive, you’ll find a single executable: `ntfsm.exe`. Now, before running any random PE file, I personally like to do some simple static analysis just to see what I’m dealing with. For this I prefer using either [Binary Refinery](https://github.com/binref/refinery), [PE-Bear](https://github.com/hasherezade/pe-bear), or [pestudio](https://www.winitor.com/).

Opening the binary with PE-Bear, we can see it’s a valid C++ executable. Additionally, the strings table contains a lot of interesting strings like `"No seriously, i hope it can not be bruteforced"`, `"Sandboxes hate this one weird trick"`, several rickroll links, and random quotes from Hackers - which makes me believe there is a lot of junk code and it’s most likely obfuscated in some way.

After sorting and filtering out duplicate strings, we find something actually useful:

```
usage: ./ntfsm <password> to reset the binary in case of weird behavior: ./ntfsm -r.
```

So the program clearly expects a password (16 characters, as we’ll see), and it also accepts a `-r` flag that appears to reset the binary. A bit odd, but worth keeping that in mind.

The challenge description mentions NTFS, which immediately makes me think of of [ADS (Alternate Data Streams)](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-fscc/c54dec26-1551-4d3a-a0ea-4fa40f848eb3) as malware tends to use that to hide itself or it’s configurations. If we try to enter a random 16 character password, we’ll notice that the binary spawns a few command windows and text boxes saying “Hello Hacker” before printing `wrong!` in the console. This sort of behavior hints that the binary’s logic and execution path are directly tied to the input… interesting.

After running the binary, let’s check and see if it’s creating any Alternate Data Streams (ADS) by using PowerShell’s [`Get-Item`](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-item?view=powershell-7.5) cmdlet.

```
PS C:\Users\User\Desktop\flare\5_-_ntfsm> Get-Item -Path .\ntfsm.exe -Stream *

PSPath        : Microsoft.PowerShell.Core\FileSystem::C:\Users\User\Desktop\flare\5_-_ntfsm\ntfsm.exe::$DATA
PSParentPath  : Microsoft.PowerShell.Core\FileSystem::C:\Users\User\Desktop\flare\5_-_ntfsm
PSChildName   : ntfsm.exe::$DATA
PSDrive       : C
PSProvider    : Microsoft.PowerShell.Core\FileSystem
PSIsContainer : False
FileName      : C:\Users\User\Desktop\flare\5_-_ntfsm\ntfsm.exe
Stream        : :$DATA
Length        : 20151296

PSPath        : Microsoft.PowerShell.Core\FileSystem::C:\Users\User\Desktop\flare\5_-_ntfsm\ntfsm.exe:input
PSParentPath  : Microsoft.PowerShell.Core\FileSystem::C:\Users\User\Desktop\flare\5_-_ntfsm
PSChildName   : ntfsm.exe:input
PSDrive       : C
PSProvider    : Microsoft.PowerShell.Core\FileSystem
PSIsContainer : False
FileName      : C:\Users\User\Desktop\flare\5_-_ntfsm\ntfsm.exe
Stream        : input
Length        : 16

PSPath        : Microsoft.PowerShell.Core\FileSystem::C:\Users\User\Desktop\flare\5_-_ntfsm\ntfsm.exe:position
PSParentPath  : Microsoft.PowerShell.Core\FileSystem::C:\Users\User\Desktop\flare\5_-_ntfsm
PSChildName   : ntfsm.exe:position
PSDrive       : C
PSProvider    : Microsoft.PowerShell.Core\FileSystem
PSIsContainer : False
FileName      : C:\Users\User\Desktop\flare\5_-_ntfsm\ntfsm.exe
Stream        : position
Length        : 8

PSPath        : Microsoft.PowerShell.Core\FileSystem::C:\Users\User\Desktop\flare\5_-_ntfsm\ntfsm.exe:state
PSParentPath  : Microsoft.PowerShell.Core\FileSystem::C:\Users\User\Desktop\flare\5_-_ntfsm
PSChildName   : ntfsm.exe:state
PSDrive       : C
PSProvider    : Microsoft.PowerShell.Core\FileSystem
PSIsContainer : False
FileName      : C:\Users\User\Desktop\flare\5_-_ntfsm\ntfsm.exe
Stream        : state
Length        : 8

PSPath        : Microsoft.PowerShell.Core\FileSystem::C:\Users\User\Desktop\flare\5_-_ntfsm\ntfsm.exe:transitions
PSParentPath  : Microsoft.PowerShell.Core\FileSystem::C:\Users\User\Desktop\flare\5_-_ntfsm
PSChildName   : ntfsm.exe:transitions
PSDrive       : C
PSProvider    : Microsoft.PowerShell.Core\FileSystem
PSIsContainer : False
FileName      : C:\Users\User\Desktop\flare\5_-_ntfsm\ntfsm.exe
Stream        : transitions
Length        : 8
```

From the output, we can see that the binary is in fact using ADS to store data in streams named `input`, `position`, `state`, and `transitions`. While these might look meaningless at first glance, the presence of `state` and `transitions` immediately suggests that we’re dealing with a FSM or a [Finite Sate Machine](https://gm0.org/en/latest/docs/software/concepts/finite-state-machines.html) - and that kind of makes sense if you look at the challenge name, NT(FSM). Cheeky.

But, before we can dive into the binary and figure out how to solve it, let’s take a moment to understand what a Finite State Machine is and how it works.

## Finite State Machines (FSM)

So what is a Finite State Machine? Well put simply, an FSM is a computational model used to design systems that can be in one of a limited number of states at any given time. A **state** represents a specific condition the system can be in, such as “idle”, “active” or “waiting for input” for example. The FSM responds to various **inputs** or events, which cause it to **transition** from one state to another. In addition to moving between states, an FSM may produce **outputs** based on the current state or the inputs it receives, allowing it to drive behavior in systems like...