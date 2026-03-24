---
title: When Data Mining Conti Leaks Leads to Actual Binaries and to a Hardcoded C2 With an Encryption Key on Tripod.com - Part Four
url: https://ddanchev.blogspot.com/2026/03/when-data-mining-conti-leaks-leads-to_23.html
source: Dancho Danchev's Blog - Mind Streams of Information Security Knowledge
date: 2026-03-23
fetch_date: 2026-03-24T04:16:30.869316
---

# When Data Mining Conti Leaks Leads to Actual Binaries and to a Hardcoded C2 With an Encryption Key on Tripod.com - Part Four

# [Dancho Danchev's Blog - Mind Streams of Information Security Knowledge](https://ddanchev.blogspot.com/)

In the overwhelming sea of information, access to timely, insightful and independent open-source intelligence (OSINT) analyses is crucial for maintaining the necessary situational awareness to stay on the top of emerging security threats. This blog covers trends and fads, tactics and strategies, intersecting with third-party research, speculations and real-time CYBERINT assessments, all packed with sarcastic attitude

## Monday, March 23, 2026

### When Data Mining Conti Leaks Leads to Actual Binaries and to a Hardcoded C2 With an Encryption Key on Tripod.com - Part Four

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigeNwLer1kckxVNOgOFcJm8fL0WBfAooL_UCPLJQPXjKuuvge1J91xSHGe4Hr-bh9_1nCYZDL_MnF0hK5L4QPVcdBPyiTmoHWlTvCJ_jXuChT8j9A_3HcQCniHVHZKxdxyFcDP0dkW_LudhkKZEsWVB23E20q80atnNxk1yO5JGdVw-6qf4xYr/s320/Bazaar_Loader_01.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigeNwLer1kckxVNOgOFcJm8fL0WBfAooL_UCPLJQPXjKuuvge1J91xSHGe4Hr-bh9_1nCYZDL_MnF0hK5L4QPVcdBPyiTmoHWlTvCJ_jXuChT8j9A_3HcQCniHVHZKxdxyFcDP0dkW_LudhkKZEsWVB23E20q80atnNxk1yO5JGdVw-6qf4xYr/s765/Bazaar_Loader_01.png)

Dear blog readers,

Continuing the "[When Data Mining Conti Leaks Leads to Actual Binaries and to a Hardcoded C2 With an Encryption Key on Tripod.com - Part Three](https://ddanchev.blogspot.com/2026/03/when-data-mining-conti-leaks-leads-to_029886864.html)" blog post series in this post I'll continue analyzing the next [malicious software](https://ddanchev.blogspot.com/2022/06/a-compilation-of-known-conti-ransomware_21.html) binary which I obtained by [data mining](https://ddanchev.blogspot.com/search?q=conti) [Conti Leaks](https://archive.org/details/rewards-for-justice-01) with a lot of success.

**The actual [malicious software](https://www.virustotal.com/gui/file/7ccd2066aa7194f5ae343eb6fa26ac0db06e3380af47974f86a20f0db98f1230/detection) binary location URL:**

hxxp://www.coalminds.com/Document\_Print.exe
hxxp://www.sonorambc.org/Document\_Print.exe

MD5: fddd22680670b6b905be34d17eddf96c
SHA-1: 1d6a1a36fc0f03d21721fc90c08fe5e46473eed3
SHA-256: 7ccd2066aa7194f5ae343eb6fa26ac0db06e3380af47974f86a20f0db98f1230

What's specifically interesting about this sample is that I obtained it using real-time OSINT by data mining Conti Leaks with a lot of success and this appears to be an interesting case where we have malicious software binaries pushed by Conti Ransomware that in this case are actual Bazaar Loader samples.

What's also specifically interesting about this sample is that next to the hardcoded C2 command and control fallback domain which in this case is (**hxxp://alztwfdicu.bazar**) the sample also generates quite a a lot of DGA domains using the infected system's time settings which also makes it another interesting observation.

Here's the analysis.

This malware uses timer-based execution delay (approximately 2 minutes) before executing its main payload at sub\_14000713c. The binary dynamically resolves API functions using hash-based lookups and contains heavily obfuscated strings that are XOR-decoded at runtime. Multiple functions (sub\_14000974c, sub\_140005410, sub\_1400034b4) resolve Windows API functions from loaded libraries, suggesting process injection or manipulation capabilities.

This is a sophisticated malware sample with multiple anti-analysis and evasion techniques. Key findings:

Initial Behavior:

* Timer-based execution delay (~2 minutes) via message loop
* Dynamic API resolution using hash-based lookups with caching
* Heavy string obfuscation (XOR/arithmetic encoding)

Core Capabilities:

* Creates separate payload thread for main malicious activity
* Performs environment/system checks with retry logic
* Builds command strings and registry paths dynamically
* Appears to perform process injection or manipulation
* Uses COM/OLE automation (based on OLEAUT32.dll imports)

Evasion Techniques:

* API hashing to hide imports
* String obfuscation throughout
* Conditional execution based on system state
* Multiple sleep/delay mechanisms

File: Document\_Print.exe (103.7 KB PE executable)
Architecture: x86\_64 Windows
Classification: Sophisticated Trojan/Backdoor with C2 capabilities

⚠️ Note: Binary Ninja maximum tool call limit was reached. This analysis may be incomplete - additional malicious functionality likely exists that was not fully analyzed.

## Key Malicious Capabilities

### 1. Execution Delay & Anti-Analysis

* Timer-based delay: Sets 60-second timer (SetTimer with 0xEA60 ms) and waits for 2x WM\_TIMER messages before payload execution (~2 minutes total delay)
* Entry point: start\_delayed\_payload\_message\_loop at 0x1400076e4
* Purpose: Evade automated sandbox analysis with time limits

### 2. API Obfuscation

* Dynamic API resolution: Uses hash-based lookup system (resolve\_api\_by\_hash\_cached at 0x140006970)
* Caching mechanism: Stores resolved APIs in global cache at data\_14001a018 (~0x11d0 bytes)
* Evasion: Hides imported functions from static analysis tools

### 3. String Obfuscation

* Technique: Heavy XOR encoding and arithmetic operations on all strings
* Runtime decoding: Strings decoded immediately before use
* Examples: Registry paths, URLs, command strings, API names all obfuscated

### 4. Network C2 Communication

* HTTP-based C2: Performs HTTP requests via check\_network\_and\_cookies (0x14000137c)
* Session management: Extracts and validates session cookies with pattern s\*t-c\*\*kie: SID=
* IP storage: Formats and stores C2 IP addresses in globals data\_140018a30 and data\_140018a70 with XOR 0xFE encoding
* Persistence: Cookie-based session tracking for maintaining C2 connection

### 5. Environment Checks

* Multi-stage validation: check\_environment\_with\_retries (0x140001e64) performs iterative checks
* Registry/file checks: Parses comma-separated paths, validates file existence
* Retry logic: 3 attempts per check with 0x3e8 ms (1 second) delays
* Adaptive delays: Escalates from 0x64 ms to 0x1b7740 ms (30 minutes) based on results

### 6. Command Execution

* Scheduled tasks: execute\_scheduled\_tasks (0x140002640) uses Concurrency::CurrentScheduler::ScheduleTask
* Command construction: Builds "cmd" strings and registry paths dynamically
* Multiple strategies: Tries different command variations if initial attempts fail
* Output validation: Checks command output size (>= 0x2710 bytes)

### 7. Multi-threaded Payload

* Thread creation: create\_payload\_thread (0x140002d5c) spawns separate thread for main payload
* Thread function: payload\_thread\_main (0x140002bbc) orchestrates malicious activity
* State monitoring: Monitors global flags (data\_14001b208, data\_140018070, data\_140018074)

## Technical Indicators

### API Hashes (Partial List)

* 0x6fb89af0 - CreateThread-like function
* 0x3d9972f5 - Sleep function
* 0x2ca5f366, 0x2ca1b5e6 - String/registry operations
* 0x2a7c76e6 - GetProcAddress-like function
* 0x81f0f0df, 0x6b416786 - Additional APIs

### Global Variables

* data\_14001a018 - API resolution cache
* data\_140018070 - State flag (checked for value 0x40)
* data\_140018074 - State flag (checked for value 0x20)
* data\_14001b208 - Execution state flag
* data\_140018a30 / data\_140018a70 - IP address storage (XOR encoded)
* data\_14001b300 - Command buffer (0x400 bytes)

### Timing Patterns

* Initial delay: 0xEA60 ms (60 seconds) × 2 = ~2 minutes
* Short delays: 0x3e8 ms (1 second), 0x7530 ms (30 seconds)
* Long delays: 0x1b7740 ms (~30 minutes)

Complete API Hash to Function Name Mapping

Successfully mapped 44 unique API hashes using the custom ROL7+XOR algorithm:

### Most Critical APIs:

* 0x1fc0eaee → GetProcAddress (57 uses) - Core dynamic API resolution
* 0xd89ad05 → VirtualAllocEx (4 uses) - Process injection memory allocation
* 0x84d25ea → WriteProcessMemory (2 uses) - Payload injection
* 0x9e6fa842 → TerminateProcess (12 uses) - Process termination
* 0x6fb89af0 → C...