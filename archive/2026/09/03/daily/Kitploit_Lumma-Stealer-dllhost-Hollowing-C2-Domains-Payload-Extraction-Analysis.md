---
title: Lumma-Stealer-dllhost-Hollowing-C2-Domains-Payload-Extraction-Analysis
url: https://kitploit.com/en/tools/github/kaandemir993/lumma-stealer-dllhost-hollowing-c2-domains-payload-extraction-analysis
source: Kitploit
date: 2026-09-03
fetch_date: 2026-09-04T06:42:35.813937
---

# Lumma-Stealer-dllhost-Hollowing-C2-Domains-Payload-Extraction-Analysis

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

Lumma-Stealer-dllhost-Hollowing-C2-Domains-Payload-Extraction-Analysis — In-depth reverse engineering analysis of Lumma Stealer, an info-stealer using process hollowing, Native API calls, and C2 communication. Includes payload extraction, clipboard hijacking, keylogging, and C2 domain identification. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/kaandemir993/lumma-stealer-dllhost-hollowing-c2-domains-payload-extraction-analysis

![](https://assets.kitploit.com/production/public/tools/53876/b8584db27554a95234b62a5343481110d9d76f671df7158d2b0e2525301315a7-display-v1.webp)

[Privilege Escalation](/en/categories/privilege-escalation)[Persistence Mechanisms](/en/categories/persistence-mechanisms)[Reverse Engineering](/en/categories/reverse-engineering)[Data Exfiltration](/en/categories/data-exfiltration)[Malware Analysis](/en/categories/malware-analysis)[Command and Control](/en/categories/command-and-control)[Binary Analysis](/en/categories/binary-analysis)

![GitHub](/providers/github.png)kaandemir993/lumma-stealer-dllhost-hollowing-c2-domains-payload-extraction-analysis

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# Lumma-Stealer-dllhost-Hollowing-C2-Domains-Payload-Extraction-Analysis

In-depth reverse engineering analysis of Lumma Stealer, an info-stealer using process hollowing, Native API calls, and C2 communication. Includes payload extraction, clipboard hijacking, keylogging, and C2 domain identification.

[View Repository](https://github.com/kaandemir993/lumma-stealer-dllhost-hollowing-c2-domains-payload-extraction-analysis)

362 days ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

## 1. Setup.exe – Privacy, Driver & Memory Strings

Process Hacker memory analysis of the `setup.exe` dropper reveals that Lumma Stealer targets privacy settings, installs drivers, and manages memory.

### Key Strings Observed:

* **`Privacy Camera`** – Attempts to access or disable camera privacy settings.
* **`Privacy Microphone`** – Attempts to access or disable microphone privacy settings.
* **`PreinstallDriver`** – Indicates driver installation for persistence or evasion.
* **`MapMemoryB0000`** – Memory mapping operation (likely for injection).

### Why This Matters:

* **Privacy Bypass:** The malware may disable camera/microphone privacy settings.
* **Driver Installation:** `PreinstallDriver` suggests kernel-level access.
* **Memory Mapping:** `MapMemoryB0000` indicates memory manipulation for injection.

### Visual Reference:

![Lumma Stealer Setup.exe Strings](https://assets.kitploit.com/production/public/readmes/53876/16d2a924b13a2a5017f97cd4b911eef6f49527460422cfe120880c79f78c95c4/3c11b5da229e12fd6fa524646572f3db68880c7580e1f9841e6ff2b5e25fe405-display-v1.webp)
*Process Hacker view showing setup.exe strings with `Privacy Camera`, `Privacy Microphone`, `PreinstallDriver`, and `MapMemoryB0000`.*

## 2. Setup.exe – C2 Domain List

Process Hacker memory analysis of the `setup.exe` dropper reveals a list of domains that are likely used for C2 communication.

### Key Domains Observed:

* **`zhtytomyr.ua`** – Potential C2 domain.
* **`pvt.k12.ma.us`** – Potential C2 domain.
* **`adobeaemcloud.com`** – Legitimate-looking domain (abused for C2).
* **`adobeaemcloud.net`** – Legitimate-looking domain (abused for C2).
* **`us-east-1.amazonaws.com`** – AWS domain (abused for hosting).
* **`elasticbeanstalk.com`** – AWS Elastic Beanstalk (abused for hosting).
* **`alwaysdata.net`** – Hosting provider (abused for C2).
* **`altervista.org`** – Hosting provider (abused for C2).

### Why This Matters:

* **C2 Communication:** These domains are used to exfiltrate stolen data.
* **Abuse of Legitimate Services:** Domains like `amazonaws.com` and `elasticbeanstalk.com` are used to evade detection.
* **Redundancy:** Multiple domains ensure the malware remains operational if some are blocked.

### Visual Reference:

![Lumma Stealer Setup.exe C2 Domains](https://assets.kitploit.com/production/public/readmes/53876/2195caa249749988759de67c1c148ee093103fbdd224c818614401a66080f415/14eda589311983e676ac4fa8d2da04364cafe2700aa9a15ba519899c544d35e3-display-v1.webp)
*Process Hacker view showing setup.exe strings with C2-like domains.*

## 3. C2 Address – Vagrancy.virus.cc (ALPC Connection)

Binary Ninja analysis of the `.bin` file extracted from the ALPC-related strings in `dllhost.exe` reveals a potential C2 address: `Vagrancy.virus.cc`.

### Key Observations:

* **`Vagrancy.virus.cc`** – Potential C2 server.
* **Source:** Extracted from the `.bin` dump of `dllhost.exe` (ALPC strings).
* **Context:** Found alongside `NtConnectPort` (inter-process communication).

### Why This Matters:

* **C2 Communication:** The malware likely uses this domain to exfiltrate stolen data.
* **ALPC Usage:** The connection may be established via ALPC for stealth.
* **Detection:** This domain can be blocked to disrupt the malware's communication.

### Visual Reference:

![Lumma Stealer C2 – Vagrancy.virus.cc](https://assets.kitploit.com/production/public/readmes/53876/3a0053dedd4f272a5448d66e2403c637473ce69c5ca43536269c73fa83e94168/4a88a3dc29714d664e65917e624934fe70772674eb0ae59829abf5a74881d47a-display-v1.webp)
*Binary Ninja view showing `Vagrancy.virus.cc` extracted from ALPC-related `.bin` data.*

## 4. dllhost.exe – Process Hollowing & Native API Usage

Process Hacker memory analysis of the injected `dllhost.exe` process reveals that Lumma Stealer uses **Process Hollowing** techniques with Native API calls.

### Key Native APIs Observed:

* **`NtCreateThreadEx`** – Creates a thread in a remote process (injection).
* **`NtWriteVirtualMemory`** – Writes data into another process's memory.
* **`NtTerminateProcess`** – Terminates processes (e.g., security tools).
* **`NtShutdownSystem`** – Shuts down or reboots the system.
* **`NtSetInformationProcess`** – Modifies process information (evasion).
* **`NtAdjustPrivilegesToken`** – Adjusts token privileges (escalation).
* **`NtSystemDebugControl`** – Performs system debug operations.
* **`SetClipboardData`** – Manipulates clipboard data.

### Why This Matters:

* **Process Hollowing:** The malware injects its payload into `dllhost.exe`.
* **Native API Usage:** Bypasses user-mode hooks (EDR/AV).
* **Privilege Escalation:** `NtAdjustPrivilegesToken` enables higher access.

### Visual Reference:

![Lumma Stealer dllhost.exe Strings](https://assets.kitploit.com/production/public/readmes/53876/d9d730080668f93dbbe88c2a667a294e0a74f5d28d0a4fcaf1f977e07cf8e626/4c3b73fc43e4f2f65b525d5973e180cd35138ca7e45371de28741f138b1a1f4b-display-v1.webp)
*Process Hacker view showing dllhost.exe strings with Native APIs (NtCreateThreadEx, NtWriteVirtualMemory, etc.).*

## 5. Lumma Stealer – Clipboard & Keylogger Capabilities

Binary Ninja analysis of the extracted `.bin` file from `dllhost.exe` reveals that Lumma Stealer has clipboard hijacking and keylogging capabilities.

### Key Functions Observed:

* **`SetClipboardData`** – Writes data to the clipboard (hijacking).
* **`NtUserGetClipboardData`** – Reads data from the clipboard.
* **`NtUserGetKeyState`...