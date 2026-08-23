---
title: Burp-Recordadora
url: https://kitploit.com/en/tools/github/hackwarts12/burp-recordadora
source: Kitploit
date: 2026-08-22
fetch_date: 2026-08-23T02:57:24.855349
---

# Burp-Recordadora

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

Burp-Recordadora — Persists BurpSuite proxy history, Repeater requests, and Intruder payloads across sessions; exports and imports .log files for web pentesting context. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/hackwarts12/burp-recordadora

![](https://assets.kitploit.com/production/public/tools/50635/bd0d69c611b73b5e2b51930306524afe6e38e5848e23ccfeebff060644c147ce-display-v1.webp)

[Web Proxies & Interception](/en/categories/web-proxies-interception)[Web Security](/en/categories/web-security)[Penetration Testing](/en/categories/penetration-testing)[Utilities & Frameworks](/en/categories/utilities-frameworks)

![GitHub](/providers/github.png)hackwarts12/burp-recordadora

# Burp-Recordadora

Persists BurpSuite proxy history, Repeater requests, and Intruder payloads across sessions; exports and imports .log files for web pentesting context.

[View Repository](https://github.com/hackwarts12/burp-recordadora)

9 months ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

![Recordadora Logo](https://assets.kitploit.com/production/public/readmes/50635/bd0d69c611b73b5e2b51930306524afe6e38e5848e23ccfeebff060644c147ce/f9607c406957e8c58dae819ac2081dd38a039ecbc822e1bc822abe4433a4e7a8-display-v1.webp)

# 🧙‍♂️ Recordadora

**Recordadora** is a **BurpSuite** extension inspired by Harry Potter.
Like Neville's Remembrall, it helps you **not to forget** or lose context of your tests.

## ✨ Features

* Save and restore **Proxy history**
* Export and import **Repeater** requests
* Persist **Intruder** payloads
* Support for `.log` files to share sessions
* Context menu integration (right-click → send to Recordadora)
* Compatible with BurpSuite Community and Professional

## 📥 Installation

### Option 1: Use the pre-compiled `.jar`

1. Download the latest version from [Releases](https://github.com/Hackwarts12/Burp-Recordadora/releases).
2. Open **BurpSuite** → *Extender* → *Extensions* → *Add*.
3. Select the `recordadora.jar` file.
4. Done! You'll see **Recordadora** active in Burp.

### Option 2: Compile from source code

⚠️ This repository **does not include the source code**, only the ready-to-use `.jar`.
In future versions, releasing the code for open collaboration will be evaluated.

## 🔍 Comparison with other extensions

**Summary:** Logger++ and Flow are useful for live analysis with filters.
**Recordadora** focuses on **saving/restoring** your work between sessions.

## 📌 Status

Initial version – in development 🚀

* Real-time filters (pending)
* Additional export to CSV/JSON (pending)
* Improved UI for large volumes (pending)

## 📝 License

This project is distributed under the license included in the repository.

---

Made with 🪄 by [Hackwarts12](https://github.com/Hackwarts12)

[Download Tool](https://github.com/hackwarts12/burp-recordadora)

| Feature | Logger++ | Flow | Request Highlighter | Recordadora |
| --- | --- | --- | --- | --- |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Saves **Proxy** traffic | ✅ | ✅ | ❌ | ✅ |
| **Repeater** logging | ❌ | ❌ | ❌ | ✅ |
| **Intruder** logging | ❌ | ❌ | ❌ | ✅ |
| Exports to file (`.log`, `.csv`, etc.) | ✅ (CSV/SQL) | ✅ | ❌ | ✅ (`.log` format) |
| **Imports** sessions from file | ❌ | ❌ | ❌ | ✅ |
| Persistence after closing Burp | ❌ | ❌ | ❌ | ✅ |
| Advanced real-time filters | ✅ | ✅ | ❌ | 🚧 Pending |
| Table-like interface | ✅ | ✅ | ✅ | ✅ (simpl.) |
| Focus on **persistence and restoration** | ❌ | ❌ | ❌ | ✅ |