---
title: Arsenal-NG: A Terminal Cheat-Sheet Launcher for Faster Penetration Testing
url: https://www.hackingarticles.in/arsenal-ng-pentest-cheat-sheet/
source: Hacking Articles
date: 2026-08-01
fetch_date: 2026-08-02T05:10:32.678647
---

# Arsenal-NG: A Terminal Cheat-Sheet Launcher for Faster Penetration Testing

[Skip to content](#content)

# [Hacking Articles](https://www.hackingarticles.in/)

Raj Chandel’s Blog

Menu

* [Courses We Offer](https://www.hackingarticles.in/courses-we-offer/)
* [CTF Challenges](https://www.hackingarticles.in/ctf-challenges-walkthrough/)
* [Penetration Testing](https://www.hackingarticles.in/penetration-testing/)
* [Web Penetration Testing](https://www.hackingarticles.in/web-penetration-testing/)
* [Red Teaming](https://www.hackingarticles.in/red-teaming/)
* [Donate us](https://www.hackingarticles.in/donate-us/)

* [Home](https://www.hackingarticles.in/)
»* [Penetration Testing](https://www.hackingarticles.in/category/penetration-testing/)
»* [Arsenal-NG: A Terminal Cheat-Sheet Launcher for Faster Penetration Testing](https://www.hackingarticles.in/arsenal-ng-pentest-cheat-sheet/)
»

[Penetration Testing](https://www.hackingarticles.in/category/penetration-testing/)

# Arsenal-NG: A Terminal Cheat-Sheet Launcher for Faster Penetration Testing

[August 1, 2026August 1, 2026](https://www.hackingarticles.in/arsenal-ng-pentest-cheat-sheet/) by [raj](https://www.hackingarticles.in/author/admin/)

### Overview

Arsenal-NG is an interactive, terminal-based launcher that turns a sprawling collection of offensive-security tools into a single searchable command cheat-sheet. Instead of memorising flags or hunting through scattered notes, you search for a task, fill in your target details through guided prompts, and let the tool drop the finished command straight into your shell. This article demonstrates the complete workflow, from installation through executing a live Active Directory enumeration command against a lab domain controller.

### Table of Contents:

* Introduction
* Installing Arsenal-NG
* Launching the Interface
* Browsing the Command Library
* Listing Every Available Tool
* Reading the Tools Table
* Inspecting a Single Tool
* Selecting a Command with a Live Preview
* Filling In the Arguments
* Executing the Command Against a Target
* Searching by Task Instead of by Tool
* Help and Global Variables
* Conclusion

### Introduction

Penetration testers juggle hundreds of command-line tools, and each one carries its own syntax, flags, and quirks. Memorising every switch waste time and copying commands from scattered notes invites typos that break an engagement or, worse, hit the wrong target. Arsenal-NG attacks this problem head-on by acting as a fast, keyboard-driven front end that remembers the commands, so you do not have to.

At its core, Arsenal-NG maintains a large library of ready-to-run commands drawn from across the offensive-security toolset, spanning reconnaissance, enumeration, exploitation, wireless attacks, web testing, and Active Directory abuse. Each entry pairs a real command template with a plain-language description and a set of colour-coded tags, so you can locate the right technique by tool name or by intent. Templates use placeholder variables such as target, username, and password, which the tool resolves for you through an interactive argument form before execution.

The workflow stays entirely in the terminal. You search the catalogue in real time, highlight a command, review its live preview, supply the arguments once, and press Enter to run it in your active shell. Global variables push this further: you set a value like an IP address a single time, and Arsenal-NG auto-fills it everywhere that placeholder appears. Because the project ships as a standard package in the Kali Linux repositories, installation takes one command and pulls in the many tools it wraps. The sections below walk through that process step by step.

### Installing Arsenal-NG

Arsenal-NG ships as a standard package in the Kali Linux repositories, so a single APT command installs it along with the many offensive-security tools it wraps. Run the command below as root, and APT resolves and pulls in every dependency automatically.

```
apt install arsenal-ng
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhD-koZfgU46Lm18SpA-hpYTbG7rYJbDsXLXR2Gpcjn7bU9AO9xysi1zHKXFsveAvt911f4XCYO4uVc4iDsfz4ZGnLrMPI_HQi-7ZwanVg1t65ejybsSQNLIVMp9l1gJ8DGjlM9_-km529OVSQvAX5rcUdi7_ecNdcnGqN32J36o7ojGBCno_YPi6Ie35r/s1600/1.png)

### Launching the Interface

Once the installation finishes, you launch the tool by typing its name at the prompt. Arsenal-NG loads its command database and opens a full-screen interactive interface inside your terminal.

```
arsenal-ng
```

**![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjkSfVsQcTpaMgXoONdFF-ItTXJwjnJZSnqaHOgAZClcVRFmZcbI0ARqTq6QDnJWMVyAgpTsY4ekg_OFFlYGhgts6ydQN3XH_x3PYtR1AR4Lr55ojErQdJ8srHxYtuyCtt5PyYB4qBDiCM5RB8nQVXUI-QBPeu0-lBCuLgxHMTcek_NYTpEeUfqS_vV5osF/s1600/2.png)**

### Browsing the Command Library

The main screen greets you with the Arsenal-NG banner and a search field at the top. Below it, the tool lists its entire command catalogue in real time. Each row shows the parent tool, a short description of the specific command, and a set of colour-coded tags such as web, security, pentest, reconnaissance, and enumeration. As you type in the search field, the list filters instantly, so you can narrow hundreds of entries down to the exact command you need within seconds. The screenshot below shows entries for 403bypasser, ad-miner, and aircrack-ng, each expanded into its distinct command variants.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhzSJyCtSRfa83ShU6fyPmJBuc_5LN_pwL9CsVcFMIL-1YLQe5yDFpTKhneZOmIL6LoBhJs8NKtsT6gIGKzod3tn4YH_hQLl9aN4PUTA69nQSYF_H7X4AuHpt_8dDO7lI2xlBEWbNGW3L0gEFodgkKtbRzmGPUizt5Ihh3Mve0osV3PRhHqC28ercCSldaQ/s1600/3.png)

### Listing Every Available Tool

Rather than scrolling through commands one by one, you can view the complete inventory of supported tools. Type the keyword below into the search field, and Arsenal-NG prompts you to press Enter to reveal the full tool list. The status bar at the bottom also exposes the core keyboard shortcuts: arrow keys to navigate, set and unset for variables, and quick access to the tools, variables, and help screens.

```
tools
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEirlQKldjQoIIro9cBdHHxaZuLDvKjaiaM46IpDOzRUyJCZT14MfQTS2eoQwb0XYlG05bXhf87jcuqOba59it0Lq-hpfRc53f2XAOmJS1GevSNXOmJ1IHcJ0_5nJq6zdeIRIX1C8NMUYNWApzObkLy0LXERO2JPkQd3kXNLY4kLVdK53R6Vx5PYZT_UE7PX/s1600/4.png)

### Reading the Tools Table

Pressing Enter renders a clean two-column table titled Available Tools. The left column names each tool, and the right column reports how many individual commands Arsenal-NG stores for it. This overview helps you gauge coverage at a glance. In the example below, bloodyad appears with fourteen commands, confirming strong support for that Active Directory attack utility.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnJhk1kxfS7S_Tn4grTJZrWaHtxxg4A14VcDr0dYNKGRLa1zjzCjgqTcU1ettRcunJxGmSqetioAOyAooBdztS76HFIaNFh3iqC5TSn2cMde-46cMmnQcNEkBjkf69K_TeM2e1rd2-K413IY2IK785eh36qGLBajGmXEkq6Ej8VORqwi2GtFGHiYowk6M1/s1600/5.png)

### Inspecting a Single Tool

To study one tool in depth, type its name into the search field. Arsenal-NG then displays every command it holds for that tool. Searching for bloodyad reveals its full range of LDAP-based Active Directory operations, including NTLM and Kerberos authentication, pass-the-hash, listing group members, adding a user to a group, setting a user password, and abusing shadow credentials. Each entry carries the privilege-escalation and authentication tags that describe its purpose.

```
bloodyad
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5sY304JCxPU-xYO6E1YbHn6ScEUYjc-XN-tDq5WW6OPkVApbMVX0wGk-9jmpwjC3hGdz_HuEfIuoUvPfSpA9-rjhIHAZZIpgIWAJmJhN_tLWLTSyeQGBNyZBygGKRdOGZCsqDYubEQTx3hKL0kaKS5xSVWBb3ahkpsYXUwDUApJ00m6jxXV46CY8l7S2j/s1600/6.png)

### Selecting a Command with a Live Preview

Arsenal-NG shines when you drill into a specific command. Searching for the NetExec LDAP module lists its many actions, from b...