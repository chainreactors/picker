---
title: DumpBrowserSecrets – Browser Credential Harvesting with App-Bound Encryption Bypass
url: https://www.darknet.org.uk/2026/03/dumpbrowsersecrets-browser-credential-harvesting-with-app-bound-encryption-bypass/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-12
fetch_date: 2026-03-13T04:07:50.836411
---

# DumpBrowserSecrets – Browser Credential Harvesting with App-Bound Encryption Bypass

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![darknet.org.uk logo](data:image/svg+xml...)![darknet.org.uk logo](https://www.darknet.org.uk/wp-content/uploads/2026/03/darknet_header_hacking_cybersec_vF-scaled.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

You are here: [Home](https://www.darknet.org.uk/) / [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/) / DumpBrowserSecrets – Browser Credential Harvesting with App-Bound Encryption Bypass

# DumpBrowserSecrets – Browser Credential Harvesting with App-Bound Encryption Bypass

March 9, 2026

Views: 707

DumpBrowserSecrets is a post-exploitation credential-harvesting tool from Maldev Academy that extracts secrets across all major browsers from a single Windows executable. It is the successor to their earlier DumpChromeSecrets project, which is now deprecated, and extends coverage from Chrome alone to the full range of Chromium-based and Gecko-based browsers in common enterprise use.

![DumpBrowserSecrets – Browser Credential Harvesting with App-Bound Encryption Bypass](data:image/svg+xml...)![DumpBrowserSecrets – Browser Credential Harvesting with App-Bound Encryption Bypass](https://www.darknet.org.uk/wp-content/uploads/2026/03/DumpBrowserSecrets-–-Browser-Credential-Harvesting-App-Bound-Encryption-Bypass-SM-640x335.png)

Modern browsers are credential vaults. Chrome, Microsoft Edge, Firefox, Opera, Opera GX, and Vivaldi all store saved passwords, session cookies, OAuth refresh tokens, credit card numbers, autofill data, and full browsing history in local SQLite databases and JSON files on disk. On a compromised Windows host, that data is frequently the fastest path to lateral movement, cloud account takeover, or persistent access to enterprise SaaS platforms without ever touching LSASS.

Where tools like [Mimikatz](https://www.darknet.org.uk/2015/07/mimikatz-gather-windows-credentials/) target Windows credential stores such as LSASS and the Security Account Manager (SAM), DumpBrowserSecrets focuses entirely on the browser layer, where credentials are increasingly stored as enterprises adopt SSO, OAuth, and browser-based SaaS workflows. The threat model has shifted: a developer’s browser session today may hold active tokens for GitHub, AWS consoles, Okta, Slack, and internal tooling simultaneously.

## How It Works

DumpBrowserSecrets consists of two components that work together: a compiled executable (`DumpBrowserSecrets.exe`) and a DLL (`DllExtractChromiumSecrets.dll`).

For Chromium-based browsers using App-Bound Encryption (Chrome, Brave, and Microsoft Edge), the challenge is that Google introduced App-Bound Encryption in Chrome 127, tying cookie and credential encryption keys to the Chrome application identity. The encryption key, stored as `app_bound_encrypted_key` in the browser’s `Local State` file, can only be decrypted via Chrome’s elevation service through the `IElevator` COM (Component Object Model) interface.

DumpBrowserSecrets handles this by spawning a headless Chromium process, then injecting the DLL into it via Early Bird APC (Asynchronous Procedure Call) injection, a technique that queues shellcode execution before the target process’s main thread begins. The DLL runs inside the Chromium process context, uses the `IElevator` COM interface to decrypt the App-Bound Encryption key, and returns the decrypted key to the executable via a named pipe. The executable then parses the browser’s on-disk SQLite databases and decrypts stored data locally.

For Opera, Opera GX, and Vivaldi, which use DPAPI (Data Protection API) keys rather than App-Bound Encryption, the same injection approach retrieves DPAPI keys instead.

For Firefox, which uses Mozilla’s NSS (Network Security Services) library with AES-256-CBC or 3DES-CBC encryption for logins, the executable handles all extraction and decryption directly with no DLL injection required.

The tool includes several evasion features relevant to operational use: compile-time string obfuscation, API hashing to defeat static analysis, PPID (Parent Process ID), and argument spoofing via `NtCreateUserProcess` with manual CSRSS registration, handle duplication to bypass file locks held by running browsers, and a custom SQLite3 file format parser (SQLoot, introduced in v1.1.1) that replaces the sqlite-amalgamation dependency to reduce the static footprint.

## Extracted Data

The following data types are extracted per browser. Encryption models vary: Chrome, Brave, and Edge use App-Bound Encryption (V20); Opera, Opera GX, and Vivaldi use DPAPI (V10); Firefox uses NSS-based encryption for logins and stores other data types unencrypted.

* **Chrome, Brave, Microsoft Edge (App-Bound / V20):** cookies, saved logins, credit cards, OAuth tokens, autofill entries, browsing history, bookmarks.
* **Opera, Opera GX, Vivaldi (DPAPI / V10):** cookies, saved logins, credit cards, OAuth tokens (V10 + Base64 for Opera/Opera GX), autofill entries, browsing history, bookmarks.
* **Firefox (NSS):** cookies, saved logins (AES-256-CBC or 3DES-CBC encrypted), OAuth tokens from `signedInUser.json`, autofill form history, browsing history, bookmarks.

Output is written as JSON to a file named `<browser>Data.json` by default, or to a path specified with the `/o` flag.

## Installation

DumpBrowserSecrets is distributed as a pre-compiled Windows executable. No installation is required. Download the compiled binaries from the GitHub Releases page, copy `DumpBrowserSecrets.exe` and `DllExtractChromiumSecrets.dll` to the target host, and execute.

For operators who need to compile from source, the repository provides a Visual Studio solution file (`DumpBrowserSecrets.sln`) with three projects: `Common`, `DllExtractChromiumSecrets`, and `DumpBrowserSecrets`. Build in Visual Studio targeting x64 Release.

## Usage

This repository does not provide a global `--help` flag in the traditional sense. The following usage block is reproduced verbatim from the README:

```
Usage: DumpBrowserSecrets.exe [options]

Options:
  /b:<browser> Target Browser: chrome, edge, brave, opera, operagx, vivaldi, firefox, all
               (default: system default browser)
  /o <file>    Output JSON File (default: <browser>Data.json)
  /all         Export All Entries (default: max 16 per category)
  /?           Show This Help Message

Examples:
  DumpBrowserSecrets.exe                            Extract 16 Entries From The Default Browser
  DumpBrowserSecrets.exe /b:chrome                  Extract 16 Entries From Chrome
  DumpBrowserSecrets.exe /b:firefox /all            Export All Entries From Firefox
  DumpBrowserSecrets.exe /b:brave /o Output.json    Extract 16 Entries From Brave To Output.json
  DumpBrowserSecrets.exe /b:all /all                Extract All From All Installed Browsers
```

By default, the tool extracts up to 16 entries per data category. The `/all` flag removes this cap. The `/b:all` flag targets every installed browser in a single run.

## Attack Scenario

An operator lands on a developer workstation during a Windows assumed-breach engagement. The user is authenticated in Chrome to GitHub, an AWS console, Okta, and the company’s internal GitLab instance. LSASS is protected by Credential Guard and y...