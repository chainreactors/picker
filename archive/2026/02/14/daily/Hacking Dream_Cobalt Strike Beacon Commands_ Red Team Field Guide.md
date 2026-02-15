---
title: Cobalt Strike Beacon Commands: Red Team Field Guide
url: https://www.hackingdream.net/2026/02/cobalt-strike-beacon-commands-red-team-field-guide.html
source: Hacking Dream
date: 2026-02-14
fetch_date: 2026-02-15T04:25:33.170726
---

# Cobalt Strike Beacon Commands: Red Team Field Guide

* [Home](http://www.hackingdream.net)
* [About Author](http://www.hackingdream.net/p/about-author.html)
* [Contact US](http://www.hackingdream.net/p/contact-us.html)

[# ![Hacking Dream](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgI3MZul9awsB7xmLlAs9J9xDOsiYxbMQoa4EQkvg9T9oe4q5zkZRqV0W4UN2KhrQQWPLveTvQ9kkuHu2HfrahqY0Gc53G1cVCwQNY2G3MVkEOJoDvLIK9lFtBUc-HhRciiteWdHYV4SaE/s1600/Size-Modified.png)](https://www.hackingdream.net/)

Main menu

close

* [Home](http://www.hackingdream.net)
* [AI Sec](https://www.hackingdream.net/search/label/AI)
* [AI Pentest](http://www.hackingdream.net/search/label/AI%20Attacks)
* [Cheatsheets](https://www.hackingdream.net/search/label/Cheatsheet)
* [Pentest](https://www.hackingdream.net/search/label/Pentest)
* [\_Active Directory](https://www.hackingdream.net/search/label/Active%20Directory)
* [\_Linux](http://www.hackingdream.net/search/label/Kali%20Linux)
* [\_Wireless](http://www.hackingdream.net/search/label/Wifi%20Hacking)
* [\_Target Hacking](http://www.hackingdream.net/search/label/Target%20Hacking)
* [Purple Team](https://www.hackingdream.net/search/label/Purple%20Team)
* [Bin Exp](https://www.hackingdream.net/search/label/Exploitation)
* How To
* [\_Blogging](http://www.hackingdream.net/search/label/Blogging)
* [\_Solved Problems](http://www.hackingdream.net/search/label/Solved%20Problems)
* [\_Money Making](http://www.hackingdream.net/search/label/Money%20Making)
* [\_Top Ten](http://www.hackingdream.net/search/label/Top%20Ten)
* [\_Gaming](http://www.hackingdream.net/search/label/Games)

### Cobalt Strike Beacon Commands: Red Team Field Guide

[February 15, 2026](https://www.hackingdream.net/2026/02/cobalt-strike-beacon-commands-red-team-field-guide.html "permanent link")

Cobalt Strike Beacon Commands: Red Team Field Guide

# Cobalt Strike Beacon Commands: Red Team Field Guide

*Updated on February 15, 2026*

**Table of Contents**

* [The Philosophy of "Low and Slow"](#philosophy)
* [Situational Awareness (Without Breaking Things)](#situational-awareness)
* [Execution Strategy: The "Fork and Run" Dilemma](#execution-strategy)
* [Advanced Injection & Custom Tooling](#advanced-injection)
* [Advanced OPSEC: Process Manipulation](#opsec-manipulation)
* [Credential & Token Manipulation](#credential-manipulation)
* [Lateral Movement & Pivoting](#lateral-movement)
* [File System Operations](#file-system)
* [Post-Exploitation: The Modern Way (.NET & BOFs)](#post-exploitation)
* [Conclusion](#conclusion)

Let's be real for a second. If you're working in red teaming or advanced penetration testing, [Cobalt Strike](https://www.cobaltstrike.com/) is isn't just a tool it's practically the industry standard for Command and Control (C2). It's the Ferrari of C2 frameworks. But just like a Ferrari, if you don't know how to drive it, you're going to crash into a wall (or in our case, trip every EDR on the network).

I've been on countless engagements where I've seen junior operators burn a solid foothold simply because they got impatient or didn't understand what was happening under the hood when they typed a command. They treat Beacon like a standard netcat shell, and that is a one-way ticket to getting kicked out of the network.

In this guide, I'm going to walk you through the most critical **Cobalt Strike Beacon commands** and techniques that I use on almost every engagement. We're going to move beyond the basics and look at this from an operational security (OPSEC) perspective.

[![Cobalt Strike Beacon Commands: Red Team Field Guide](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjXa1ugvcDDf5HQTGIkzE1Jc37g7OGApHLRaxuw0HfRWjnVl9hOeJ__OHt6zVhwU7EqVNVyezMZdJInYUtT0vUAp8ui4TmLqncJDbTjXi40Sf8zHE9FArqccgT4Ulxqb4TYrL3gC7-yK1teaFjddPaG00imUvCM0ON8LOiv0ueKpenUs5DqgHPdk7VK7sbY/w640-h358/Cobalt-Strike-Beacon-Commands-Red-Team-Field-Guide.jpg "Cobalt Strike Beacon Commands: Red Team Field Guide")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjXa1ugvcDDf5HQTGIkzE1Jc37g7OGApHLRaxuw0HfRWjnVl9hOeJ__OHt6zVhwU7EqVNVyezMZdJInYUtT0vUAp8ui4TmLqncJDbTjXi40Sf8zHE9FArqccgT4Ulxqb4TYrL3gC7-yK1teaFjddPaG00imUvCM0ON8LOiv0ueKpenUs5DqgHPdk7VK7sbY/s1024/Cobalt-Strike-Beacon-Commands-Red-Team-Field-Guide.jpg)

## The Philosophy of "Low and Slow"

Before we type a single command, you need to understand that Beacon is designed to be asynchronous. It's not a constant connection. It checks in, grabs tasks, executes them, and goes back to sleep. This is its greatest strength and your biggest test of patience.

### Sleep and Jitter

The very first thing I do when I land a new beacon? I check the sleep time. By default, your profile might have it set to something aggressive.

```
# Check current settings
sleep

# Set sleep to 60 seconds with 20% jitter
# This means it will sleep anywhere between 48s and 72s
sleep 60 20

# Go interactive (DANGEROUS - noisy network traffic)
# Only do this if you are tunneling or need instant feedback
sleep 0
```

**Senior Tip:** Never use a flat sleep cycle (e.g., `sleep 60 0`). EDRs and network appliances love consistent patterns. That 20-30% jitter is your best friend for blending in with background noise.

## Situational Awareness (Without Breaking Things)

Once you're stable, you need to know where you are. But be careful. Running loud commands like `net user /domain` immediately is rookie behavior.

### Process & User Discovery

Instead of spawning `cmd.exe` to run `whoami`, use Beacon's native APIs which are far stealthier.

```
# Get your current user context (Native API, no process spawn)
getuid

# Check your privileges
getprivs

# List processes (Use this to find security products or targets for injection)
ps
```

**OPSEC Warning:** Avoid `shell whoami` or `shell ipconfig`. The `shell` command spawns `cmd.exe` as a child process, which is a massive red flag for any decent SOC. Always prefer Beacon native commands or Beacon Object Files (BOFs). You can learn more about OPSEC safe practices in our [Active Directory Lateral Movement & Persistence](https://www.hackingdream.net/2021/05/ad-pentest-cheatsheet-lateral-movement-persistence.html).

## Execution Strategy: The "Fork and Run" Dilemma

This is where the magic happens. Cobalt Strike uses a technique often called "Fork and Run" for many post-exploitation tasks. It spawns a temporary process, injects your capability into it, executes it, and then kills the process.

If you don't configure this, you're going to be spawning `rundll32.exe` every time you run a command, which looks incredibly suspicious.

### Spawnto

You can and should change what process Beacon spawns for these temporary jobs.

```
# Check current spawnto settings
spawnto

# Change the temporary process to something legitimate for the environment
# targeting syswow64 (x86) or sysnative (x64)
spawnto x64 %windir%\sysnative\gpupdate.exe
spawnto x86 %windir%\syswow64\gpupdate.exe
```

By changing this to `gpupdate.exe` or `werfault.exe`, your malicious traffic looks like standard Windows background activity.

### The Execution Hierarchy

Here is how I prioritize execution methods to stay under the radar:

1. **`inline-execute` (BOFs):** Runs in your current process memory. No child process. Safest.
2. **`execute-assembly`:** Runs .NET assemblies in a temporary process. Powerful but creates a new process.
3. **`powerpick`:** Runs PowerShell commands without spawning `powershell.exe`. Uses the unmanaged PowerShell automation DLLs.
4. **`execute`:** A "fire and forget" command. It executes a program on the target but **does not** capture output. Useful if you want to launch a background task or if capturing output might hang the beacon.
5. **`run`:** Executes a program and captures output.
6. **`shell`:** Spawns `cmd.exe /c`. **Avoid this unless absolutely necessary.**

```
# Good: Using PowerPick to run a quick PS command
powerpick Get-Process

# Fire and Forget: Launch a tool without waiting for it
execute C:\Windows\System32\calc.exe

# Better: Using a BOF to enumera...