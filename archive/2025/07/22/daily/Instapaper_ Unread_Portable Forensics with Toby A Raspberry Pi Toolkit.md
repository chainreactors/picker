---
title: Portable Forensics with Toby A Raspberry Pi Toolkit
url: https://bakerstreetforensics.com/2025/07/20/portable-forensics-with-toby-a-raspberry-pi-toolkit/
source: Instapaper: Unread
date: 2025-07-22
fetch_date: 2025-10-06T23:52:23.005182
---

# Portable Forensics with Toby A Raspberry Pi Toolkit

[Skip to content](#content)

[Baker Street Forensics](https://bakerstreetforensics.com/)

Where Irregulars are part of the Game

Menu

* [Blog](https://bakerstreetforensics.com/blog/)
* [Links, Resources & Swag](https://bakerstreetforensics.com/resources/)

[![](https://bakerstreetforensics.com/wp-content/uploads/2022/05/output-onlinepngtools-4.png)](https://bakerstreetforensics.com/)

![](https://bakerstreetforensics.com/wp-content/uploads/2025/07/toby_icon.png?w=924&h=0&crop=1)

# Portable Forensics with Toby: A Raspberry Pi Toolkit

[DFIR](https://bakerstreetforensics.com/category/dfir/), [DIY](https://bakerstreetforensics.com/category/diy/), [Forensic Imaging](https://bakerstreetforensics.com/category/forensic-imaging/), [Forensics](https://bakerstreetforensics.com/category/forensics/), [Malware](https://bakerstreetforensics.com/category/malware/), [Memory Analysis](https://bakerstreetforensics.com/category/memory-analysis/), [Raspberry Pi](https://bakerstreetforensics.com/category/raspberry-pi/), [Triage](https://bakerstreetforensics.com/category/triage/), [yara](https://bakerstreetforensics.com/category/yara/)

Whether teaching, investigating, or tinkering on the road, there’s an undeniable appeal to a device that’s self-contained, headless, and versatile enough to support forensic analysis, malware triage, and field acquisition. That idea became the seed for Toby — a Raspberry Pi Zero 2 W–based micro-rig that can be managed from an iPad or mobile device.

It started off with a “what could I do with at Raspberry Pi” and the final result: a fully functional, go-anywhere forensics toolkit that fits in the palm of your hand, carefully packed into a Grid-It travel kit and loaded with purpose.

---

## **Why Build Toby?**

Toby wasn’t born from necessity. It came from a blend of curiosity, constraint, and the spirit of joyful overengineering. The goal wasn’t just to get Kali Linux running on a Pi — [that’s been done](https://bakerstreetforensics.com/2023/07/01/raspberry-pi-forensics-hacking-gadget/). The challenge was in *how much capability* could be packed into a minimalist footprint without compromising on control, security, or style.

Some driving goals from the outset:

* **Headless-first**: Must be operable via SSH, or VNC — no screen needed.
* **Kali-based**: Full access to familiar forensic and pentest tooling.
* **Discreet and functional**: Everything should be secure, practical, and stowable.
* **Modular connectivity**: USB OTG, video capture, remote keyboard/mouse, and VPN support all needed to be viable.
* **Portable power**: Run from a battery pack for field ops or demo use without dependency on AC power.

![](https://bakerstreetforensics.com/wp-content/uploads/2025/07/toby_cli.png?w=1024)

---

## **Hardware Selection**

**Raspberry Pi Zero 2 W**

The Pi Zero 2 W hits a sweet spot. It has enough power to run full Kali and perform triage analysis, especially with swap and careful headless tuning. It supports USB OTG and can be powered over micro-USB, making it ideal for lightweight builds.

**Grid-It Travel Kit: The Physical Layout**

Instead of housing the components in a fixed enclosure, I opted for flexibility: a Grid-It organizer sleeve. It allows each cable and tool to remain accessible and secured via elastic straps — perfect for quick swaps or field reconfiguration.

The current loadout includes:

* **Raspberry Pi Zero 2 W**
* **HDMI mini to full adapter** (for display recovery if needed)
* **USB micro to USB-C adapter combo** (for powering Pi from laptop, iPad, or battery pack)
* **Anker battery pack** (portable, long runtime)
* **Wireless keyboard** (compact; paired via Bluetooth or USB receiver)
* **USB capture device** (used for teaching, demoing webcam/VNC sessions)
* **Short USB OTG cable**

The setup is light, self-contained, and TSA-friendly — a true digital go-bag for the forensically inclined.

![](https://bakerstreetforensics.com/wp-content/uploads/2025/07/img_0977.jpeg?w=787)

---

## Portable Power

Toby can be powered from the USB port of an iPad or from a battery pack or AC adapter, making it extremely flexible for field use.

![](https://bakerstreetforensics.com/wp-content/uploads/2025/07/img_0986.jpeg?w=722)

*Toby powered from iPad Pro*

![](https://bakerstreetforensics.com/wp-content/uploads/2025/07/img_0987.jpeg?w=1024)

*Toby powered from portable battery*

## **Software**

The OS is a clean, headless Kali Linux image configured specifically for ARM on the Pi Zero 2 W. Rather than trying to turn it into a desktop experience (even though it can), it boots fast, runs lean, and drops me directly into a terminal where I can get to work — whether over SSH or local keyboard.

**Core Components:**

• **Base image**: Raspbian (Debian-based) with Kali tools manually installed

**Metapackages**:

* kali-linux-forensic
* kali-linux-desktop
* core/default Kali utilities and command-line tools, incrementally layered until the system was functionally equivalent to a full Kali install (minus unnecessary services)

**Additional Software Intstalled:**

* [MalChela](https://bakerstreetforensics.com/2025/06/20/malchela-v3-0-case-management-fileminer-and-smarter-triage/) (CLI and GUI)
* Toby-find

![](https://bakerstreetforensics.com/wp-content/uploads/2025/07/screenshot-2025-07-20-at-10.37.53-am.png?w=1024)

*MalChela (CLI) running on Toby*

![](https://bakerstreetforensics.com/wp-content/uploads/2025/07/toby_kali_forensics.png?w=1024)

*Kali Forensics tools on Toby*

![](https://bakerstreetforensics.com/wp-content/uploads/2025/07/screenshot-2025-07-20-at-10.31.01-am.png?w=1024)

*MalChela GUI running on Toby*

---

## 🔍 **Toby-find: Your On-Device Forensics Cheat Sheet**

One of Toby’s handiest features isn’t a tool you run—it’s a tool *to remember tools*. **toby-find** is a simple but powerful command-line helper built into the system. It gives you fast access to a curated list of CLI forensics tools available on Toby, along with short descriptions and usage tips.

It’s like having a searchable cheat sheet, always available—perfect for field use when memory is fuzzy or connectivity is limited.

![](https://bakerstreetforensics.com/wp-content/uploads/2025/07/screenshot-2025-07-20-at-10.33.19-am.png?w=1024)

*toby-find utility*

**What It Does**

When you run:

```
toby-find [keyword]
```

it will search the help file for any tool(s) mentioning the keyword in name or description, and provide back a simple command syntax for each tool.

Example:

```
dwmetz@toby:~$ toby-find strings

Tool:        mstrings
Description: Extracts printable strings from files and maps them to MITRE ATT&CK techniques.
Example:     mstrings suspicious.exe
Category:    Malware
--------------------------------------------------
Tool:        strings_to_yara
Description: Generates a basic YARA rule from strings gathered manually or via mstrings.
Example:     strings_to_yara
Category:    Malware
--------------------------------------------------
Tool:        floss
Description: Extracts obfuscated strings from malware binaries.
Example:     floss suspicious.exe
Category:    Forensics
--------------------------------------------------
Tool:        rephrase
Description: Analyzes and reformats strings from documents or binaries.
Example:     rephrase input.txt
Category:    Forensics
--------------------------------------------------
```

### Installed Tools:

Many of the tools are native to Kali, but some, including MalChela, were compiled manually or added through custom scripts. (**Bold** == MalChela tools or custom scripts.)

| Tool Name | Description |
| --- | --- |
| bat | Cat replacement with syntax highlighting and Git integration. |
| binwalk | Scans binaries for embedded files and executable code. |
| bulk\_extractor | Extracts artifacts like emails and credit card numbers from disk images. |
| **combine\_yara** | Combines multiple YARA rule files into a single merged rule set. |
| dff | Digital Forensics Framework with CLI and GUI modes. |
| dig | ...