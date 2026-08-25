---
title: frida-ios-dump-modern
url: https://kitploit.com/en/tools/github/jwalker/frida-ios-dump-modern
source: Kitploit
date: 2026-08-24
fetch_date: 2026-08-25T02:59:17.846005
---

# frida-ios-dump-modern

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

frida-ios-dump-modern — An updated Frida iOS dump tool supporting the latest Frida 17.5.2 APIs | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/jwalker/frida-ios-dump-modern

![](https://assets.kitploit.com/production/public/tools/50846/fc6d8343afb9211bc942c6f669dab60fe7d96e6ee76692aa53793e15980039ea-display-v1.webp)

[iOS Security](/en/categories/ios-security)[Mobile App Pentesting](/en/categories/mobile-app-pentesting)[Reverse Engineering](/en/categories/reverse-engineering)[Malware Analysis](/en/categories/malware-analysis)[Mobile Security](/en/categories/mobile-security)[Binary Analysis](/en/categories/binary-analysis)

![GitHub](/providers/github.png)jwalker/frida-ios-dump-modern

# frida-ios-dump-modern

An updated Frida iOS dump tool supporting the latest Frida 17.5.2 APIs

[View Repository](https://github.com/jwalker/frida-ios-dump-modern)

97 months ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# Modern iOS IPA Dumper

A modern iOS application memory decryption tool built for **Frida 17.5.2+** with full support for **iOS 14-16** and multiple jailbreaks.

**Status: ✅ Working and Tested** - Successfully dumps and decrypts iOS apps using Frida 17.5.2 on:

* iOS 14.7.1 + Taurine jailbreak (iPad mini 5)
* iOS 16.7.12 + palera1n jailbreak (iPhone 8)

## Features

* ✅ Compatible with Frida 17.5.2+ (uses NativePointer.readByteArray)
* ✅ Works with Taurine jailbreak (iOS 14.7.1)
* ✅ Works with palera1n jailbreak (iOS 16.7.12)
* ✅ Handles palera1n's `/cores/binpack/` jailbreak paths
* ✅ Fast decryption using memory dump + manual cryptid patching
* ✅ No deprecated API calls
* ✅ Clean, maintainable code
* ✅ Automatic IPA packaging
* ✅ Uses Python paramiko (no external tools needed)
* ✅ Detailed progress reporting

## Why This Tool?

The original `frida-ios-dump` (last updated 2020) uses deprecated Frida APIs that don't work with Frida 17.5.2. This tool is built from scratch using modern Frida APIs and is specifically tested with the Taurine-compatible Frida patches.

## Requirements

### macOS/Host Requirements

* Python 3.8+
* Frida 17.5.2+
* `paramiko` (Python SSH library - installed automatically)
* `iproxy` (for USB connection via libimobiledevice)

### iOS Device Requirements

* Jailbroken iOS device (tested on iOS 14.7.1 + Taurine)
* Patched frida-server running (see Frida patches in `will add my patch repo`)
* SSH access enabled

## Installation

root@kitploit:~

```
cd /Users/username/git/frida-ios-dump-modern

# Create virtual environment with uv:
uv venv
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt

# Make script executable
chmod +x dump.py
```

## Setup USB Connection

root@kitploit:~

```
# Install libimobiledevice if needed
brew install libimobiledevice

# Start USB tunnel (in a separate terminal)
iproxy 2222 22
```

## Usage

### 1. List Installed Apps

root@kitploit:~

```
python dump.py -l
```

### 2. Dump an Application

**Important:** The app must be running before dumping due to Taurine jailbreak restrictions.

root@kitploit:~

```
# 1. Launch the app on your device manually
# 2. Run the dumper:

python dump.py com.example.app

# With custom SSH password:
python dump.py com.example.app -P your_password

# With custom output directory:
python dump.py com.example.app -o /path/to/output
```

### 3. Example: Dump Ventusky

root@kitploit:~

```
# 1. Open Ventusky on your iOS device
# 2. Run:
python dump.py com.in-meteo.ventusky -P mypassword
```

## How It Works

### iOS 16 Compatible Approach (Hybrid Method)

1. **Attach**: Connects to the running app process via Frida
2. **Enumerate**: Lists all loaded modules (binaries) in the app
3. **Read Disk Binary**: Reads the original encrypted binary from device filesystem
   * **Critical for iOS 16**: Preserves LC\_DYLD\_CHAINED\_FIXUPS data
   * Keeps original DATA segments with fixup chains intact
4. **Read Decrypted Segment**: Reads ONLY the encrypted TEXT segment from memory
   * iOS decrypts code at runtime
   * We read just the decrypted portion, not the whole binary
5. **Replace & Patch**:
   * Replace encrypted TEXT segment in disk binary with decrypted memory
   * Set cryptid=0 in LC\_ENCRYPTION\_INFO
   * All DATA segments remain untouched (preserves fixups)
6. **Dump**: Writes hybrid binary to `/tmp` on device
7. **Download**: Transfers files from device via SCP via paramiko
8. **Package**: Creates a decrypted IPA file ready for analysis

**Why this works on iOS 16:**

* iOS 16 uses chained fixups - pointers are stored as "chains" that dyld resolves at runtime
* Dumping from memory gives us resolved pointers, but tools expect fixup chains
* By reading disk binary and replacing only the encrypted TEXT, we preserve original fixups
* This is the same approach bagbak and other modern dumpers use

## Output

The tool creates:

* Individual decrypted binaries
* Complete app bundle with decrypted binaries
* Packaged IPA file ready for analysis

Example output structure:

root@kitploit:~

```
/tmp/Ventusky_decrypted/
├── Payload/
│   └── Ventusky.app/
│       ├── Ventusky (decrypted main binary)
│       ├── Frameworks/
│       │   └── *.framework (decrypted frameworks)
│       └── ... (other app resources)
└── Ventusky_decrypted.ipa
```

## Taurine Jailbreak Compatibility

This tool is designed to work with the Taurine-patched Frida server that includes:

1. **No Thread Suspension on iOS 14**: Prevents kernel panics
2. **No launchd Injection**: Respects Taurine restrictions
3. **Manual App Launch Required**: Apps must be launched manually before dumping

## Troubleshooting

### "No USB device found"

root@kitploit:~

```
# Check frida-server is running on device:
ssh -p 2222 root@localhost "ps aux | grep frida-server"

# Restart frida-server if needed:
ssh -p 2222 root@localhost "killall frida-server; frida-server &"
```

### "App not found"

root@kitploit:~

```
# List apps to find correct bundle ID:
python dump.py -l
```

### "App not running"

root@kitploit:~

```
# Launch the app manually on your device first
# This is required due to Taurine jailbreak restrictions
```

### SSH Authentication Failed

root@kitploit:~

```
# Test SSH connection:
ssh -p 2222 root@localhost

# If password prompt works, use -P flag:
python dump.py com.example.app -P your_password
```

### iOS 16: "Objective-C Metadata looks mangled" in Hopper

If you're getting metadata errors on iOS 16 after patching:

**Diagnose the issue:**

root@kitploit:~

```
# Run diagnostic on dumped binary
./diagnose_ios16.sh /tmp/AppName_decrypted/Payload/AppName.app/AppName

# Compare with working iOS 14 binary
./diagnose_ios16.sh /path/to/working/ios14/binary
```

**Key things to check:**

1. File size matches original binary on disk
2. Look for LC\_DYLD\_CHAINED\_FIXUPS (iOS 16 specific)
3. Verify cryptid is 0 after patching

The tool now reads original file size from disk to avoid dumping runtime-expanded memory regions.

### Post-Dump: Verification

**Good news:** The tool now automatically sets `cryptid=0` during du...