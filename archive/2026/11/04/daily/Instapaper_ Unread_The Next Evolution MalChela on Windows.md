---
title: The Next Evolution MalChela on Windows
url: https://bakerstreetforensics.com/2026/11/02/the-next-evolution-malchela-on-windows/
source: Instapaper: Unread
date: 2026-11-04
fetch_date: 2026-11-05T08:45:18.231199
---

# The Next Evolution MalChela on Windows

[Skip to content](#content)

[Baker Street Forensics](https://bakerstreetforensics.com/)

Where Irregulars are part of the Game

Menu

* [Links, Resources & Swag](https://bakerstreetforensics.com/resources/)
* [Posts](https://bakerstreetforensics.com/blog/)
* [Mind Palace](https://bakerstreetforensics.com/mind-palace-2/)
* [GitHub](https://github.com/dwmetz)

[![](https://bakerstreetforensics.com/wp-content/uploads/2022/05/output-onlinepngtools-4.png)](https://bakerstreetforensics.com/)

![](https://bakerstreetforensics.com/wp-content/uploads/2026/11/gemini_generated_image_q0jzq5q0jzq5q0jz.jpeg?w=924&h=0&crop=1)

# The Next Evolution: MalChela on Windows

[DFIR](https://bakerstreetforensics.com/category/dfir/), [Malware](https://bakerstreetforensics.com/category/malware/), [MITRE ATT&CK](https://bakerstreetforensics.com/category/mitre-attck/), [open-source](https://bakerstreetforensics.com/category/open-source/), [PowerShell](https://bakerstreetforensics.com/category/powershell/), [Rust](https://bakerstreetforensics.com/category/rust/), [Triage](https://bakerstreetforensics.com/category/triage/), [yara](https://bakerstreetforensics.com/category/yara/)

With the v4.5 release, MalChela now runs natively on Windows. Previously, Windows users were limited to running it under WSL. The PWA interface was reachable from Windows, so driving the GUI was easy enough, but everything underneath still lived in Linux. If you’re a native Windows user, you can now skip WSL entirely and get the same toolset, CLI and web interface, that runs on macOS and Linux.

![MalChela v4.5 running natively on Windows](https://bakerstreetforensics.com/wp-content/uploads/2026/11/malchela-on-windows.png?w=1024)

## Getting started on Windows

You’ll need Rust with the MSVC toolchain (rustup will prompt you for the Visual Studio C++ build tools), Git, and Python 3 for the web interface. From the MalChela folder in PowerShell or cmd, run `.\release.ps1` (or `release.cmd`) to build, then `server\start_server.cmd` to launch the PWA. The first run sets up the Python environment for you, and no server config file is needed to get going. Full details are in the [native Windows install guide](https://dwmetz.github.io/MalChela/install/#windows-native). WSL2 still works if you prefer a Linux environment.

## Goodbye YARA, hello yara-x

The biggest hurdle to running natively on Windows was how MalChela was originally built: it required compiling YARA from source. We’ve been moving away from YARA to [yara-x](https://github.com/VirusTotal/yara-x), VirusTotal’s rewrite of YARA in Rust, and with this release that migration is complete. yara-x is compiled in as a Rust crate, so there’s no system YARA library to install and no environment variables to point the build at, on any platform. Much of that groundwork came from [Daniel Iwugo (@elementmerc)](https://github.com/elementmerc), whose PRs built out and hardened the yara-x backend and moved File Analyzer onto it.

If you’re upgrading from v4.3 or earlier, the old YARA, OpenSSL, and GTK packages are no longer used by the build. You can leave them installed, and drop the `YARA_LIBRARY_PATH` and `BINDGEN_EXTRA_CLANG_ARGS` exports from your shell profile. One heads-up if you maintain your own rulesets: yara-x is highly compatible with YARA, but not 100%. Some legacy syntax that YARA tolerated will throw errors under yara-x, so it’s worth test-compiling your custom rules after upgrading.

## TIQuery updates

Thanks to a PR from [Jonas Lejon (@jonaslejon)](https://github.com/jonaslejon), TIQuery has a new URL source: [ScanMalware](https://scanmalware.com). It checks ScanMalware’s public scan archive without ever submitting a new scan, and only the host name leaves your machine; the full URL is matched locally, so tokens or email addresses in a phishing link’s query string stay with you.

That addition also led to a rework of how keyless sources (those that don’t require an API key) are handled. Sources that send your lookups to a third party, currently urlscan.io and ScanMalware, are now off until you opt in, so you stay in complete control of your OPSEC and what gets submitted where. Your choice is saved and shared across the CLI, the web interface, and the Claude plugin.

New in v4.5, TIQuery can also download samples from Triage (tria.ge), alongside the existing MalwareBazaar integration. If MalwareBazaar doesn’t have the sample, TIQuery falls back to Triage, verifies the SHA256 against the hash you requested, and wraps it in the usual password-protected zip before anything touches disk. Check out the [online documentation](https://dwmetz.github.io/MalChela/coretools/tiquery/) for details.

## Thank you

In my less-than-humble opinion, MalChela has come a long way since the early days of 2025, but it wouldn’t be where it is without feedback and contributions from the community. A very big thank you to Daniel, Jonas, and everyone who’s participated! If you run into anything on Windows, or have ideas for what’s next, issues and PRs are always welcome on [GitHub](https://github.com/dwmetz/MalChela).

### Share this:

* [Share on LinkedIn (Opens in new window)
  LinkedIn](https://bakerstreetforensics.com/2026/11/02/the-next-evolution-malchela-on-windows/?share=linkedin)
* [Share on Reddit (Opens in new window)
  Reddit](https://bakerstreetforensics.com/2026/11/02/the-next-evolution-malchela-on-windows/?share=reddit)
* [Share on Bluesky (Opens in new window)
  Bluesky](https://bakerstreetforensics.com/2026/11/02/the-next-evolution-malchela-on-windows/?share=bluesky)
* [Share on Mastodon (Opens in new window)
  Mastodon](https://bakerstreetforensics.com/2026/11/02/the-next-evolution-malchela-on-windows/?share=mastodon)

Like Loading...

### *Related*

[November 2, 2026](https://bakerstreetforensics.com/2026/11/02/the-next-evolution-malchela-on-windows/) [Doug Metz](https://bakerstreetforensics.com/author/dwmetz/)[DFIR](https://bakerstreetforensics.com/tag/dfir/), [Github](https://bakerstreetforensics.com/tag/github/), [MalChela](https://bakerstreetforensics.com/tag/malchela/), [Malware](https://bakerstreetforensics.com/tag/malware/), [PowerShell](https://bakerstreetforensics.com/tag/powershell/), [Windows](https://bakerstreetforensics.com/tag/windows/), [yara](https://bakerstreetforensics.com/tag/yara/), [yara-x](https://bakerstreetforensics.com/tag/yara-x/)

## One thought on “The Next Evolution: MalChela on Windows”

1. Pingback: [DFIR News, 03 Nov 2026 - Forensic Focus](https://www.forensicfocus.com/news/headlines/dfir-news-03-nov-2026/)

## Leave a Reply [Cancel reply](/2026/11/02/the-next-evolution-malchela-on-windows/#respond)

Comment

Name

Email

Website

Turn on JavaScript to leave a comment.

Δ

## Post navigation

[Previous Previous post: Unpacking ATT&CK With MalChela v4.4](https://bakerstreetforensics.com/2026/10/31/unpacking-attck-with-malchela-v4-4/)

Search for:

* [GitHub](https://github.com/dwmetz)
* [LinkedIn](https://www.linkedin.com/in/dwmetz/)
* [Bluesky](https://bsky.app/profile/dwmetz.bsky.social)
* [Mastodon](https://infosec.exchange/%40dwmetz)

## Recent Posts

* [The Next Evolution: MalChela on Windows](https://bakerstreetforensics.com/2026/11/02/the-next-evolution-malchela-on-windows/)
  November 2, 2026
* [Unpacking ATT&CK With MalChela v4.4](https://bakerstreetforensics.com/2026/10/31/unpacking-attck-with-malchela-v4-4/)
  October 31, 2026
* [From Strings to Techniques: Catch Me at ATT&CKcon 7.0](https://bakerstreetforensics.com/2026/10/16/from-strings-to-techniques-catch-me-at-attckcon-7-0/)
  October 16, 2026
* [A Non-DFIR Post: Come Have a Drink at 221B.bar](https://bakerstreetforensics.com/2026/08/31/a-non-dfir-post-come-have-a-drink-at-221b-bar/)
  August 31, 2026
* [MalChela v4.3](https://bakerstreetforensics.com/2026/07/23/malchela-v4-3/)
  July 23, 2026

[Website Powered by WordPress.com](https://wordpress.com/?ref=footer_custom_powered).

* [Comment](https://bakerstreetforensics.com/2026/11/02/the-next-evolution-ma...