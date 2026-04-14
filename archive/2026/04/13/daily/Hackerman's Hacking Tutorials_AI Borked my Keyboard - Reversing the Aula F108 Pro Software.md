---
title: AI Borked my Keyboard - Reversing the Aula F108 Pro Software
url: https://parsiya.net/blog/ai-borked-keyboard/
source: Hackerman's Hacking Tutorials
date: 2026-04-13
fetch_date: 2026-04-14T04:44:50.919278
---

# AI Borked my Keyboard - Reversing the Aula F108 Pro Software

# [Hackerman's Hacking Tutorials](https://parsiya.net/)

## The knowledge of anything, since all things have causes, is not acquired or complete unless it is known by its causes. - Avicenna

Navigate…» About Me!» Cheat Sheet» My Clone» Source Repo» Manual Work is a Bug» The Other Guy from Wham!

* [About Me!](https://parsiya.net/about/ "About Me!")
* [Cheat Sheet](https://parsiya.net/cheatsheet/ "Cheat Sheet")
* [My Clone](https://parsiya.io/ "My Clone")
* [Source Repo](https://github.com/parsiya/parsiya.net "Source Repo")
* [Manual Work is a Bug](https://queue.acm.org/detail.cfm?id=3197520 "Manual Work is a Bug")
* [The Other Guy from Wham!](https://www.google.com/search?q=andrew+ridgeley "The Other Guy from Wham!")

Apr 12, 2026
- 18 minute read - [AI](https://parsiya.net/categories/ai/) [Hardware](https://parsiya.net/categories/hardware/) [Reverse Engineering](https://parsiya.net/categories/reverse-engineering/)

# AI Borked my Keyboard - Reversing the Aula F108 Pro Software

* [.nfo](#nfo)
  + [[greetz]](#greetz)
  + [[anti-greetz]](#anti-greetz)
* [Background](#background)
  + [Keyboard Software](#keyboard-software)
* [Setup](#setup)
  + [GhidraMCP Setup](#ghidramcp-setup)
  + [Attaching the Keyboard to WSL2](#attaching-the-keyboard-to-wsl2)
  + [Model Difference](#model-difference)
  + [LLM Usage and Hand Holding](#llm-usage-and-hand-holding)
* [The Fails](#the-fails)
  + [The LCD](#the-lcd)
    - [The Upload Protocol](#the-upload-protocol)
    - [Validating the File](#validating-the-file)
    - [A Subtle Difference: Control vs. Interrupt Transfers](#a-subtle-difference-control-vs-interrupt-transfers)
    - [Don't Trust the ~~Tool~~ Fool](#dont-trust-the-tool-fool)
    - [What Didn't Fix This Mess](#what-didnt-fix-this-mess)
    - [Partial Recovery](#partial-recovery)
  + [Side "Gas Lights" or How I was Gaslit by My Keyboard](#side-gas-lights-or-how-i-was-gaslit-by-my-keyboard)
    - [Related Documentation](#related-documentation)
  + [Two Bytes Walk Into a Buffer in the Wrong Order](#two-bytes-walk-into-a-buffer-in-the-wrong-order)
    - [The Root Cause](#the-root-cause)
* [What Did We Learn Here Today](#what-did-we-learn-here-today)
* [Appendix 1: Copium](#appendix-1-copium)

I used GPT-5.4 and Claude Opus 4.6 to reverse engineer the Aula F108 Pro
keyboard's software using Ghidra MCP. This is how I did it, what setbacks I had,
and how (A)I borked the keyboard's screen despite constant supervision and
review. A common issue with the keyboard is that it ACKs bad messages, then
silently drops them. Did Gene Wolfe write this firmware?

I also introduce the novel wording of `(A)I`, meaning both I and AI did
something, because everyone is making things up, why not me? I assume I need to
give it a name, a logo, and a website to become an AIfluencer?

* Code: <https://github.com/parsiya/f108-pro>
* ai-docs: <https://github.com/parsiya/f108-pro/tree/main/ai-docs>

# .nfo

## [greetz]

* [Adam from MORSE](https://hackback.zip/) for review and feedback.
  + Yes, we're allowed to talk to other teams.
* LaurieWired for [GhidraMCP](https://github.com/lauriewired/ghidramcp).
* Song: [Mina Deris - Iranam](https://www.youtube.com/watch?v=s55-4MDf_w4).
* Book: [Alastair Reynolds - Anthology - Beyond The Aquila Rift](https://parsiya.io/literature/bookreviews/#aquilarift).
  + Diamond Dogs is phenomenal. I didn't like the ending, but OMG, the setting!

## [anti-greetz]

* Web pages that hijack any and all shortcut keys like `ctrl+f/n`
* Infosec LinkedIn:
  + "If you want a picture of the future, imagine vendor ~~security research~~ marketing blogs rehashed by LLMs — forever."

![In other news, Mythos was released recently!](i-am-hacker.webp "In other news, Mythos was released recently!")
In other news, Mythos was released recently!

# Background

I bought a new mechanical keyboard, the Aula F108 Pro. I got it for $40 (retails
for $90) via Amazon renewed mainly because it's pink! The refurbished versions
of other colors were $60. Here it is beside my Chilkey ND104. Yes, I like cyan
backlights.

![Aula F108 Pro and Chilkey ND104](01.webp "Aula F108 Pro and Chilkey ND104")
Aula F108 Pro and Chilkey ND104

I quite like the sound and it's hot swap (can change the switches without
soldering) so I can put some silent switches for the office and annoy my
coworkers by dragging a pink keyboard around. I love the color.

It's nowhere close to my ND104, but for $40 vs. $200, it's 60-70% of the way
there. My only problem (apart from the software and what you see below) is the
knob. It's too sensitive and kind of useless for configuring the keyboard with
the screen. Pressing the knob will rotate it most of the time.

## Keyboard Software

The software is, well, not that trustworthy. Not that I think they want to hack
me, but in general, peripheral software is not great. I ran the application on
an old desktop and configured my keyboard, but that is not practical. So I
decided to see if I could use LLMs to reverse engineer it and make my own tool.

You can find different versions of their software.

* This page lets you download version `1.0.0.1`.
  + <https://aulagear.com/blogs/software/aula-f108-pro-driver>
* This one has version `1.0.0.3` and has a new firmware release:
  + <https://aulakeyboard.com/download/f108-pro-drive/>

The software is actually perfect for this experiment because all the UI and
functionality is in a small 3 MB executable. Pretty neat. You know it's a
Chinese company because an American company would have shipped a 300 MB Electron
wrapper :).

You can also find the software on the Epomaker website because it's built by
them: <https://epomaker.com/products/epomaker-x-aula-f108-pro>

# Setup

* Debian 12 in WSL2: That's where I do most of my dev work.
* GitHub Copilot Chat in VS Code: In my free token (at work and home) era!
* [Ghidra MCP by LaurieWired](https://github.com/lauriewired/ghidramcp)
* Models: Claude Opus 4.6 and GPT-5.4 (on High reasoning).

## GhidraMCP Setup

I followed the instructions in the readme to install the extension and got the
Python bridge.

I created `.vscode/mcp.json` in my workspace as follows:

```
{
  "servers": {
    "ghidra": {
      "type": "stdio",
      "command": "~/aula-reverse/f108-pro/GhidraMCP-release-1-4/.venv/bin/python",
      "args": [
        "~/aula-reverse/f108-pro/GhidraMCP-release-1-4/bridge_mcp_ghidra.py",
        "--ghidra-server",
        "http://127.0.0.1:8080/"
      ]
    }
  },
  "inputs": []
}
```

Then I opened `DeviceDriver.exe` in Ghidra and started the analysis. This is the
main binary and the analysis should be quick. I got an error in the middle of
the analysis but that's not a blocker. Although as we will see later, it's good
to copy the entire installation directory to the workspace for the AI to access.

## Attaching the Keyboard to WSL2

I installed and used [usbipd-win](https://github.com/dorssel/usbipd-win) to connect the keyboard to WSL2. I
used it in Wired mode but apparently it's also possible to use the utility to
configure the keyboard using the 2.4 GHz dongle. See the instructions at
<https://github.com/parsiya/f108-pro?tab=readme-ov-file#wsl2>.

**This makes the keyboard unresponsive in Windows (even inside WSL2)** which is
why I am using two keyboards in the picture above.

## Model Difference

I did not see a lot of difference between Claude Opus 4.6 and GPT-5.4 for these
tasks. GPT-5.4 was set to high reasoning from the default medium and Claude Opus
4.6 was on default high. This might not be a great benchmark because this is
simple reversing.

I am sure people have their own favorites, but for my use cases at work and home
these two are very close. At work I mostly use GPT-5.4 in our own subscription,
and at home I use Claude Opus 4.6 via GitHub Copilot. GPT-5.4 yaps more, but I
have instructions to cut the talking and summaries to a minimum.

## LLM Usage and Hand Holding

I oversaw every step and read the (decompiled) code along with the LLM
reasoning. Both models were v...