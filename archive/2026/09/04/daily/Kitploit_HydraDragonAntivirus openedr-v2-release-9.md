---
title: HydraDragonAntivirus openedr-v2-release-9
url: https://kitploit.com/en/posts/github-hydradragonantivirus-hydradragonantivirus-openedr-v2-release-9
source: Kitploit
date: 2026-09-04
fetch_date: 2026-09-05T06:28:49.883093
---

# HydraDragonAntivirus openedr-v2-release-9

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/13337/40f6e2506024e9599cf09df84771efc1c44355b0ae16ba0ca2a5e4dc506d67cf.png)

New releaseSep 4, 2026

# HydraDragonAntivirus openedr-v2-release-9

Dynamic and static analysis with Real Time Malware Analysis with Antivirus for Windows, including open-source XDR (3 EDR projects), ClamAV, YARA-X, machine learning AI, behavioral analysis, Unpacker, Deobfuscator, Decompiler, website signatures, Ghidra, Suricata, Sigma, Kernel, Hypervisior based protection and much more than you can imagine.

Share

# Hydra Dragon Antivirus

![Hydra Dragon Antivirus](https://assets.kitploit.com/production/public/readmes/13337/82126691b8b244b141aa22bd1f39df598655e8da05b07100c69a6586074c65dd.png)

![HydraDragon Antivirus — retro mark](https://assets.kitploit.com/production/public/readmes/13337/17eaff9aa6c292036f29741270ebe115ee24829b173816efdf22871493803eb4.png)

[![Project Wiki](https://img.shields.io/badge/Wiki-Hydra%20Dragon-red?style=for-the-badge&logo=github)](https://github.com/HydraDragonAntivirus/HydraDragonAntivirus/wiki)

📚 For detailed documentation, architecture diagrams, and component guides, visit our [Project Wiki](https://github.com/HydraDragonAntivirus/HydraDragonAntivirus/wiki).

![Hydra Dragon GUI](https://assets.kitploit.com/production/public/readmes/13337/40f6e2506024e9599cf09df84771efc1c44355b0ae16ba0ca2a5e4dc506d67cf.png)

![Sanctum EDR](https://assets.kitploit.com/production/public/readmes/13337/0ac70b050b8b3356539d22c6644ee41f80803b7c36f44e894afaa02d37135887.webp)

![OpenEDR](https://assets.kitploit.com/production/public/readmes/13337/1bdee9b06a0f1606aa1a6ce56e3495706c9c362a8898cf6c8a7eaded0b2e2ac6.jpg)

# WARNING: ACTIVE DEVELOPMENT IN PROGRESS

This project is not production-ready.
Breaking changes, bugs, and incomplete features should be expected.

⚠️ NOTICE: This repository is intended strictly for EXPERT MALWARE ANALYSTS and SECURITY RESEARCHERS.
It contains low-level system components and experimental security drivers that require professional knowledge to handle safely.

> [!CAUTION]
>
> ### 🛑 USER LIABILITY & SAFEGUARD LIMITATIONS
>
> HydraDragon is designed to protect against **malicious automated threats**, not human error or intentional system modifications.
>
> 1. **Manual Deletion**: The antivirus **WILL NOT** stop you from running commands like `rd C: /s /q` or manually deleting your own files. It recognizes that if you (the Administrator) are explicitly deleting something, it is a **real user mistake** rather than a malware intrusion. The system is designed to permit intentional administrative decisions without interference.
> 2. **Driver/System Misconfiguration**: The software does not protect against manual installation of incompatible drivers or incorrect system settings. A "Inaccessible Boot Device" or other system failures caused by manual registry edits or driver experiments are **NOT** considered malware behavior and are not blocked.
> 3. **Experimental Nature**: You are responsible for any data loss or system instability caused by using this experimental software. **Always test in a Virtual Machine (VM) first.**

## One Man Project

* HydraDragon is a three-year independent open-source antivirus/EDR project built primarily by one developer.

## TODO

* Add HydraDragonIDE to project (static analyzer).
* Remove Npcap since it's not really open source and replace with custom Suricata build.

## About Feature Of Project

* I said this about month ago: NOTE: This project is become far more complex than you think so I switched to Android to join AV-Test to become first open source antivirus which going to join professional tests: <https://github.com/HydraDragonAntivirus/HydraDragonAV-Mobile>
* Then this UPDATE: I was planning to use only best signatures and remove a lot of dynamic analysis based antivirus with only Owlyshield + OpenEDR + Firewall because in real world we need to focus real-time-protection without heavy signatures.
* So this going to be very complex task yet again. Good Luck for me.

## Compatibility with PCs

* **Platform Support**: This project is strictly for **x86-64 Windows** only. aarch64 and other architectures are not supported.
* This installer is designed to be used on clean or freshly formatted Windows PCs.
* For best results, install HydraDragon Antivirus only on systems where the required third-party components have not already been installed manually.

### Important Notice

Please do not run this installer if any of the following programs are already installed on your PC:

* Python 3.12
* Node.js
* Npcap
* ClamAV
* Suricata
* OpenEDR or related EDR components

Installing HydraDragon Antivirus on a system where these components are already installed may cause version conflicts, path issues, service conflicts, or unexpected installer behavior.

### Recommended Usage

Use this installer on:

* Fresh Windows installations
* Clean test machines
* Virtual machines
* PCs without existing antivirus engine dependencies

If you already have any of the required components installed, uninstall them first or use a clean Windows environment before installing HydraDragon Antivirus.

## Important Notes & Limitations

### Project Scope

HydraDragon is a local antivirus (except Xcitium cloud) project currently under active and experimental development.

* It operates locally on the system.
* It is intended for research, learning, and malware analysis experimentation.

This project does not aim to replace your primary daily antivirus solution.

---

### Detection Philosophy

* False positives may occur.
* The system assumes the machine is in a clean state (not post-infection).
* The project prioritizes deeper analysis over speed.
* The goal is long-term detection improvement rather than quick but shallow detection.
* This does NOT mean the project achieves a 99% detection rate — it reflects the development philosophy only.
* This antivirus not only uses his best signatures but almost every new signatures. That's why it's heavy.

---

### Experimental Status

* This is a highly experimental project.
* Some architectural decisions in earlier versions were not optimal and affected stability.
* The project is actively being improved and refined.
* Use with caution.

---

### Known Limitations

* Files larger than **2 GB** are skipped by the scanner and are not scanned. Do not treat a skipped file as clean.
* Transparent TLS Proxy/Inspector may install a local **HydraDragon Firewall CA** certificate when certificate installation consent is enabled. The firewall GUI can add/remove it manually, and the uninstaller removes it on a best-effort basis.

---

### Sample Detection Policy

* Very old malware samples may not be detected.
* Signature retirement reference:
  <https://blog.clamav.net/2025/12/clamav-signature-retirement.html>
* **Boot-Critical Filters**: `MBRFilter` is now configured as a **SERVICE\_BOOT\_START (0)** UpperFilter. This ensures the Master Boot Record is protected from the very first moment the disk stack initializes, providing hardware-level resistance against bootkits and Petya-style ransomware.
* Files that appear as junk or fully unknown data may be ignored intentionally.
* If a PE header is removed, some detection engines may no longer flag the file.
* YARA detections may still trigger depending on rule logic (for example, rules that do not verify file type).

Example:

PE header removed sample:
<https://www.virustotal.com/gui/file/9b7e921e971fe7523ba83a4599b4006ad214854eb043372129e4f5a68c5a427f>

Original sample:
<https://www.virustotal.com/gui/file/1ef6c1a4dfdc39b63bfe650ca81ab89510de6c0d3d7c608ac5be80033e559...