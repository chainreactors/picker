---
title: LEAPPs.org - Latest changes!
url: https://abrignoni.blogspot.com/2026/05/leappsorg-latest-changes.html
source: Instapaper: Unread
date: 2026-06-01
fetch_date: 2026-06-02T06:33:19.076955
---

# LEAPPs.org - Latest changes!

# [Initialization vectors](https://abrignoni.blogspot.com/)

Digital Forensics and Incident Response. All things InfoSec.

## Sunday, May 31, 2026

### LEAPPs.org - Latest changes!

## What's New on LEAPPs.org — A Fresh Round of Updates

We've shipped a set of updates to [leapps.org](https://leapps.org) focused on making the site faster to use, easier to navigate, and more useful for the digital forensics practitioners who rely on it every day. Here's a full rundown of everything that changed.

---

### 🆕 New: Artifact Browser

The biggest addition in this update is the [**Artifact Browser**](https://leapps.org/artifacts) — a new page that lets you browse and search every artifact supported across iLEAPP, ALEAPP, RLEAPP, and VLEAPP, all in one place.

Rather than digging through each tool's GitHub repository to figure out what's supported, you can now:

* Search by artifact name, category, description, or file path pattern
* Filter by tool (iLEAPP, ALEAPP, RLEAPP, VLEAPP)
* Filter by category (Messaging, Location, Device Info, and more)
* See which output types each artifact supports — HTML, TSV, Timeline, or LAVA
* Click any artifact name to jump directly to its source file on GitHub
* Expand file path patterns per artifact to see exactly what files each plugin targets

The data is pulled **live from the source code** every time the page loads. It parses both the modern `__artifacts_v2__` format (used in iLEAPP and newer ALEAPP plugins, with rich metadata including description, author, and output types) and the legacy `__artifacts__` format still found in older ALEAPP files. If any tool fails to load, a per-tool error banner appears with a direct link to that tool's GitHub releases — the rest of the page still renders normally.

A real-time progress bar and file counter are shown during the load so you always know what's happening.

Find it at: [leapps.org/artifacts](https://leapps.org/artifacts)

---

### 🧭 Cleaner Navigation — Tools Dropdown

With the Artifact Browser added, the top navigation bar had grown to seven-plus items — too many to scan quickly. We regrouped the tool-related pages into a new **Tools dropdown**, matching the style of the existing Community dropdown.

**Before:** Tools · LAVA · Releases · Stats · Changelog · Artifacts · Community · GitHub

**After:** Tools ▾ · Stats · Changelog · Community ▾ · GitHub

The Tools dropdown contains:

* **All Tools** — jumps to the tools overview section on the home page
* **LAVA** — jumps to the LAVA section on the home page
* **Releases** — the download page
* **Artifacts** — the new artifact browser

The active state is preserved — if you're on the Releases page, the Releases link inside the dropdown is highlighted gold. Same for the Artifacts page. This change is applied consistently across all pages on the site.

---

### ⚡ Better Loading Experience — Skeleton States

Several pages on the site pull live data from GitHub before they can render. Previously, while that data was loading, pages showed plain text like "Fetching releases…" before the content appeared — causing an abrupt layout shift.

Both the **Stats** and **Changelog** pages now show animated skeleton placeholders while data loads:

* On the **Stats page**, metric cards show shimmer placeholder bars instead of a dash, and the comparison table shows five skeleton rows with widths that match the real column content
* On the **Changelog page**, the loading area shows five skeleton timeline entries — complete with date chip, version bar, and body bar — that match the shape of the real entries

The result is a smoother, more polished feel while the page loads, with no jarring layout shift when data arrives.

---

### 📊 Theme-Aware Charts on the Stats Page

The [Stats page](https://leapps.org/stats) has charts showing downloads and stars per tool. Previously, the chart axis tick colors and grid lines were hardcoded for dark mode — switching to light mode left the axes with poor contrast and near-invisible grid lines.

The charts now respond to the active theme in real time. When you toggle between dark and light mode, both charts update instantly — no page reload needed. Tick colors and grid line opacity are computed from the current theme using a `MutationObserver` watching the `data-theme` attribute on the page.

---

### 🐛 Bug Fixes

#### Broken Download button on the Releases page

The "Download" call-to-action button in the navigation bar on the Releases page was pointing to `#` — clicking it did nothing. It now correctly scrolls to the top of the releases list.

#### Missing back-to-top button on the Scoreboard

The [Scoreboard page](https://leapps.org/scoreboard) renders a long table of contributors. Every other page on the site had a floating back-to-top button — the Scoreboard was the only one missing it. That's been added.

#### Mobile menu couldn't be dismissed on the Resources page

On the [Resources page](https://leapps.org/resources), tapping the hamburger menu opened it correctly — but tapping anywhere outside the menu did nothing. The click-outside-to-close handler that every other page had was missing. Fixed.

#### Inconsistent active nav state on the Scoreboard

The Scoreboard link in the Community dropdown was using an inline style to highlight itself as the current page, while every other page used a CSS class. Standardized to use `class="active"` consistently.

#### Release notes rendered as raw HTML in the Changelog

The [Changelog page](https://leapps.org/changelog) pulls release notes from GitHub and displays a truncated preview. The content was injected directly into the page without escaping, meaning any HTML tags in a GitHub release body would be rendered — a potential XSS vector. The text is now HTML-escaped before injection, so release notes always display as plain text.

---

### Wrapping Up

The core goal of all these changes is the same: make it easier to find what you need, understand what's available, and get back to the actual forensics work. The Artifact Browser in particular is something we hope saves practitioners meaningful time — no more repo-hopping to verify which artifacts a tool supports before committing to an extraction workflow.

As always, everything on leapps.org is free, and all four tools — iLEAPP, ALEAPP, RLEAPP, and VLEAPP — are open source. If you spot an issue or have a suggestion, the GitHub repositories are the right place to raise it.

👉 [Explore the Artifact Browser](https://leapps.org/artifacts)

👉 [Download the latest releases](https://leapps.org/releases)

at
[May 31, 2026](https://abrignoni.blogspot.com/2026/05/leappsorg-latest-changes.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=9011697188395968020&postID=3059375904634116453&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=9011697188395968020&postID=3059375904634116453&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=9011697188395968020&postID=3059375904634116453&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=9011697188395968020&postID=3059375904634116453&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=9011697188395968020&postID=3059375904634116453&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=9011697188395968020&postID=3059375904634116453&target=pinterest "Share to Pinterest")

[Newer Post](https://abrignoni.blogspot.com/2026/05/leappsorg-latest-changes.html "Newer Post")

[Older Post](https://abrignoni.blogspot.com/2025/05/extraction-processing-querying-apple.html "Older Post")
[Home](https://abrignoni.blogspot.com/)

## About Me

* [LinqApp - All Social Media](https://linqapp.com/abrignoni)

## Search This Blog

|  |  |
| --- | --- |
|  |  |

## Blog Archive

* ▼
  [2026](https://abrignoni.blogspot.com/2026/)
  (1)
  + ▼
    [May](htt...