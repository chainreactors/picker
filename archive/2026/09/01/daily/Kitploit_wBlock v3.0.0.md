---
title: wBlock v3.0.0
url: https://kitploit.com/en/posts/github-0xcub3-wblock-300
source: Kitploit
date: 2026-09-01
fetch_date: 2026-09-02T06:40:09.717805
---

# wBlock v3.0.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/9565/4c10c91d9e188bdeaa488c6a4596e3eb119057d460c4e1e8f4eda155149c19af.png)

New releaseSep 1, 2026

# wBlock v3.0.0

The next-generation ad blocker for Safari.

Share

![wBlock Logo](https://assets.kitploit.com/production/public/readmes/9565/f9be27527e40a78f4f25d3a7763a377ffb492bc1891f8645f0214792a89cf548.png)

# wBlock

**The end of Safari ad-blocking B.S.**

[![Download on the App Store](https://toolbox.marketingtools.apple.com/api/v2/badges/download-on-the-app-store/black/en-us?releaseDate=1760313600)](https://apps.apple.com/us/app/wblock/id6746388723?itscg=30200&itsct=apps_box_badge&mttnsubad=6746388723)

![Version](https://img.shields.io/github/v/release/0xCUB3/wBlock?style=flat&label=version&color=gray)
![Platform](https://img.shields.io/badge/macOS_12.3+_%7C_iOS_15.4+_%7C_visionOS_2.0+-gray?style=flat&logo=apple&logoColor=white)
![License](https://img.shields.io/badge/GPL--3.0-gray?style=flat&label=license)

[![Join Discord](https://img.shields.io/badge/Join-Discord-5865F2?style=flat&logo=discord&logoColor=white)](https://discord.gg/Y3yTFPpbXr)

[![Mentioned in Open-Source iOS Apps](https://awesome.re/mentioned-badge.svg)](https://github.com/dkhamsing/open-source-ios-apps)

![wBlock Filters for macOS in light and dark appearances](https://raw.githubusercontent.com/0xcub3/wblock/HEAD/docs/media/img/hero_image.png)

A Safari content blocker for macOS, iOS, iPadOS, and visionOS.
750,000 rules across 5 extensions, Protocol Buffer storage, LZ4 compression, and iCloud sync.

> [!NOTE]
> **Looking for a detailed comparison?** Check out my [comparison guide](https://github.com/0xcub3/wblock/blob/HEAD/Adblock_Comparison.md) to see how wBlock stacks up against other Safari content blockers.

## Features

|  |  |
| --- | --- |
| Performance  * **750,000 rule capacity** across 5 Safari content blocking extensions per platform (150k each) * **~40 MB RAM** at idle — Safari's native content blocking API runs rules out-of-process * **Protocol Buffers + LZ4** for filter storage; streaming I/O keeps memory low during compilation * **HTTP conditional requests** (If-Modified-Since/ETag) so updates only download what changed * **iCloud sync** for filter selections, custom lists, userscripts, and whitelist across devices  Content modification  * **Element Zapper** (macOS, iOS, iPadOS, visionOS) — visually select and hide page elements in Safari * **No Autoplay** (macOS, iOS, iPadOS, visionOS) — keeps videos and audio paused until you tap or click them, stopping muted feed/scroll autoplay; enable it globally from the Safari toolbar popup and allow autoplay per site when a page needs it * **Tube Cleaner & Player Cleaner** — optional remote userscript defaults downloaded from the wBlock-userscripts repository; they turn existing media elements into native Safari players before first paint, restoring Picture-in-Picture and background playback. They update independently of the app version; wBlock's content-blocking rules handle ads separately * **Userscript engine** with Greasemonkey API (GM\_getValue, GM\_setValue, GM\_xmlhttpRequest) * **Userstyle support** — install UserCSS themes (.user.css) applied natively as CSS, no JS wrapper needed * **Custom filter lists** via URL, paste, or file import — supports any AdGuard-syntax blocklist * **Toolbar search** for quickly finding filters and userscripts * **Automatic rule distribution** across all 5 content blocker slots for maximum coverage | Blocking  * **Network request blocking** — ads, trackers, cookie banners, annoyances * **CSS injection** for cosmetic filtering and element hiding * **Script blocking** for unwanted JavaScript * **Pop-up and redirect prevention** * **URL tracking-parameter stripping** — removes UTM and other tracking params, unwraps shortener/redirect URLs (enabled by default via wBlock Scripts)  Configuration  * **Auto-updates** from every hour to every 7 days, or manual. macOS can keep checking through a bundled launch agent and background update service, iOS background checks are best-effort * **Per-site controls** — disable blocking on specific sites from the Safari toolbar * **Blocked request logger** (macOS) — see what's being blocked on each page * **Per-site settings** — whitelist trusted domains, toggle userscripts per site, and switch element zapper rules on or off per domain * **Regional filters** with auto-detection based on your locale * **Homebrew cask** for macOS: `brew tap 0xcub3/wblock && brew install --cask wblock` |

---

## Screenshots

|  |
| --- |
| ![Userscript Management Screenshot](https://assets.kitploit.com/production/public/readmes/9565/0a43bfebcee0c1168a4d27d03874a69ff837c625d6a3ec37b9834126f1760d3f.png)   **Userscript Management**  *Manage paywalls, YouTube Dislikes, and more* |
| ![Settings Screenshot](https://assets.kitploit.com/production/public/readmes/9565/34551e39e45c30e4a70cbd7600583229103edb5608582a2f01e68b99493a69cf.png)   **Settings & Customization**  *Configure auto-updates, notifications, and preferences* |
| ![iOS Screenshot](https://assets.kitploit.com/production/public/readmes/9565/4c10c91d9e188bdeaa488c6a4596e3eb119057d460c4e1e8f4eda155149c19af.png)    **iOS Interface**  *Full-featured blocking on iPhone* |
| ![iPadOS Screenshot](https://assets.kitploit.com/production/public/readmes/9565/b313e8f2cedd9bd7ec96ccbfd24f7175f78133d52ce26f455ae7b99efe4f8a66.png)    **iPadOS Interface**  *Full-featured blocking on iPad* |

---

## Technical Implementation

|  |  |
| --- | --- |
| **Core Architecture**   * Protocol Buffers (libprotobuf) with LZ4 compression for filter serialization * Asynchronous I/O with Swift concurrency (async/await, Task, Actor isolation) * Streaming serialization to disk minimizes peak memory usage during compilation * 5 Safari content blocking extensions per platform (maximum Safari API capacity) * SafariServices framework integration for declarative content blocking | **Dependencies & Standards**   * SafariConverterLib v4.3.0 for AdGuard to Safari rule conversion * Bundled AdGuard scriptlet engine for advanced blocking techniques * Swift concurrency (async/await, Task, Actor isolation) with project-level Swift 5 settings * VoiceOver and Dynamic Type support throughout the SwiftUI app * SwiftProtobuf for cross-platform filter storage format |

---

## Support Development

wBlock is free and open source.
If you want to support the project:

[![Donate Button](https://assets.kitploit.com/production/public/readmes/9565/888185d078b1763d0469847749dec546281355c97b40f1aeea46a80665c78d92.png)](https://opencollective.com/skula/projects/wblock)

---

## FAQ

**How does wBlock compare to other ad blockers?**

Check out our [comparison guide](Adblock_Comparison.md) vs uBlock Origin Lite, Wipr 2, and AdGuard's Safari apps.

**Should I install wBlock from the App Store or the DMG/Homebrew release?**

The App Store version is usually preferred because it handles app updates automatically. The DMG/Homebrew release has the same features and is available for users who prefer installing outside the App Store.

**Should I use wBlock alongside another ad blocker?**

**No. Use one general-purpose content blocker at a time.**

There is no controlled study proving that every possible combination of ad blockers harms every page. However, browser architecture and extension documentation support avoiding overlapping blockers:

* **Extensions can make conflicting changes.** Mozilla documents that when two extensions attempt conflicting modifications to the same response header, only one change may succeed. Multiple blockers can therefore produce order-dependent behavior rat...