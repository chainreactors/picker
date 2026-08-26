---
title: BL00DYM4RY
url: https://kitploit.com/en/tools/gitlab/toxy4ny/bl00dym4ry
source: Kitploit
date: 2026-08-25
fetch_date: 2026-08-26T03:05:11.729789
---

# BL00DYM4RY

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

BL00DYM4RY — Educational trojan simulator for cybersecurity training, simulating phishing attacks with social engineering, system reconnaissance, anti-sandbox evasion, and data exfiltration to raise awareness. | Kitploit

[Tools](/en/tools)/![GitLab](/providers/gitlab.png)GitLab/toxy4ny/bl00dym4ry

![](https://assets.kitploit.com/production/public/tools/51375/2af44d8c636fed91be9eec071c0969a2f258a6a5c9eaab4f457e9783f9c9e624-display-v1.webp)

[Data Exfiltration](/en/categories/data-exfiltration)[Information Gathering](/en/categories/information-gathering)[Phishing](/en/categories/phishing)[Social Engineering](/en/categories/social-engineering)[Learning & Education](/en/categories/education)[Red Teaming](/en/categories/red-teaming)[Payload Development](/en/categories/payload-development)

![GitLab](/providers/gitlab.png)toxy4ny/bl00dym4ry

# BL00DYM4RY

Educational trojan simulator for cybersecurity training, simulating phishing attacks with social engineering, system reconnaissance, anti-sandbox evasion, and data exfiltration to raise awareness.

[View Repository](https://gitlab.com/toxy4ny/bl00dym4ry)

28 days ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

[Website](https://gitlab.com/toxy4ny/BL00DYM4RY)

# 🎭 BloodyMary Trojan Phishing Simulator

## 📋 Description

**BloodyMary** is an educational tool (trojan-virus or Ransomware) for training cybersecurity specialists, simulating realistic phishing attacks with social engineering elements. This project was created to raise awareness about cyber threats and demonstrate the consequences of running suspicious files.

> ⚠️ **WARNING**: This tool is intended EXCLUSIVELY for educational purposes and authorized testing in controlled environments.

---

## 🎯 Project Goals

* **Training** personnel in cybersecurity fundamentals
* **Demonstrating** realistic phishing techniques
* **Raising awareness** about social engineering
* **Testing** readiness for cyber threats

---

## 🔧 Technical Capabilities

### **🕵️ Reconnaissance Techniques**

* ✅ System information gathering (OS, processor, RAM)
* ✅ Network configuration analysis (IP, MAC, adapters)
* ✅ Active process enumeration
* ✅ Username and computer name identification

### **🛡️ Anti-Sandbox**

* ✅ Execution time verification (bypass time acceleration)
* ✅ Process count analysis (sandbox detection)
* ✅ RAM volume checking (VM detection)
* ✅ Activation delay (behavioral analysis evasion)

### **📡 Data Exfiltration**

* ✅ TCP transmission (SSH imitation)
* ✅ HTTP fallback for reliability
* ✅ Network settings obfuscation
* ✅ Unique filename generation

### **🎭 Social Engineering**

* ✅ Realistic visual effects
* ✅ Psychological impact
* ✅ Ransomware behavior imitation
* ✅ Educational messages

---

## 🎬 Gaming Elements

### **🩸 Visual Effects**

* **Realistic Blood**: Physical simulation of drops with gravity
* **Ghostly Messages**: Flickering text with glow effect
* **Fullscreen Animation**: Optimized for Full HD (1920x1080)
* **Double Buffering**: Smooth animation without flickering

### **🎨 Effect Technical Details**

root@kitploit:~

```
// Blood drop physics
drops[i].velocityY += drops[i].acceleration;
drops[i].x += drops[i].velocityX;
drops[i].y += drops[i].velocityY;

// Color gradient creation
COLORREF CreateBloodGradient(int baseRed, int variation, int alpha)
```

### **🎪 Impact Scenario**

1. **Stealth Launch** - No visible signs
2. **Data Collection** - Silent system analysis
3. **Anti-Sandbox** - Virtual environment check
4. **Exfiltration** - Data transmission to "C&C server"
5. **Psychological Effect** - Dramatic visualization
6. **Educational Finale** - Explanation of what happened

---

## 🛠️ Build and Installation

### **Requirements**

* **Arch Linux** (or any Linux with MinGW-w64)
* **MinGW-w64** cross-compiler
* **UPX** for compression (optional)
* **Wine** for testing (optional)

### **Quick Installation**

root@kitploit:~

```
# Install dependencies
sudo pacman -S mingw-w64-gcc mingw-w64-binutils mingw-w64-headers mingw-w64-crt upx wine

# Clone repository
git clone https://github.com/toxy4ny/bl00dym4ry.git
cd bl00dym4ry

# Build
make
# or
./build.sh

# Build both versions (32-bit and 64-bit)
make all
# or
./build.sh all
```

### **Manual Build**

root@kitploit:~

```
# 64-bit version
x86_64-w64-mingw32-gcc -Os -s -static -DWIN32_LEAN_AND_MEAN \
    -ffunction-sections -fdata-sections -fno-ident -fomit-frame-pointer \
    -o bl00dym3ry.exe main.c \
    -Wl,--gc-sections -Wl,--strip-all -Wl,--build-id=none \
    -static-libgcc -static-libstdc++ \
    -lwininet -lws2_32 -liphlpapi -luser32 -lkernel32 -lgdi32 \
    -lshell32 -ladvapi32 -lole32 -loleaut32 -luuid -lmsimg32

# Size optimization
x86_64-w64-mingw32-strip --strip-all bl00dym3ry.exe
upx --best --lzma bl00dym3ry.exe
```

---

## 🎓 Educational Scenarios

### **📧 Phishing Campaigns**

1. **Email Attachment**: Disguised as document or image
2. **USB Drop**: Placed on USB drive with attractive name
3. **Social Media**: Distributed as "interesting file"
4. **Corporate Network**: Test employee awareness

### **🎯 Target Groups**

* **IT Specialists** - Technical threat understanding
* **Managers** - Business risk comprehension
* **Regular Users** - Cybersecurity hygiene basics
* **Students** - Practical learning

---

## 📊 Reporting

### **Automatic Reports**

* **Desktop Report**: `SECURITY_TRAINING_REPORT.txt` on desktop
* **Remote Logging**: Server transmission for analysis
* **Timestamp**: Precise execution time
* **System Fingerprint**: Unique system identification

### **Report Structure**

root@kitploit:~

```
===============================================================
                    CYBERSECURITY TRAINING REPORT
===============================================================

WARNING: This is the result of a phishing training test

YOU SUCCESSFULLY LAUNCHED A SUSPICIOUS FILE!

What happened:
+ System information was collected
+ Data was sent to external server
+ Visual effects were demonstrated
+ Malicious activity was simulated

RECOMMENDATIONS:
1. Don't open suspicious attachments
2. Verify email senders
3. Use antivirus software
4. Regularly update software
5. Be careful with links
```

---

## 🔒 Security and Ethics

### **✅ Legal Usage**

* Authorized testing in own infrastructure
* Educational programs with participant consent
* Threat demonstration in controlled environment
* Corporate cybersecurity training

### **❌ Prohibited Usage**

* Attacks on foreign systems without permission
* Causing real harm or damage
* Violating computer crime legislation
* Commercial use without license

### **🛡️ Safety Measures**

root@kitploit:~

```
// File does NOT cause real harm:
// - Does not encrypt files
// - Does not install backdoors
// - Does not modify system settings
// - Creates only educational report
```

---

## 🎥 Operation Demonstration

### **Phase 1: Stealth Launch**

root@kitploit:~

```
[✓] Anti-sandbox checks passed
[✓] Console window hidden
[✓] Process started successfully
```

### **Phase 2: Reconnaissance**

ro...