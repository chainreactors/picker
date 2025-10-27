---
title: New Alpha Release: Tor Browser 15.0a3
url: https://blog.torproject.org/new-alpha-release-tor-browser-150a3/
source: Tor Project blog
date: 2025-09-23
fetch_date: 2025-10-02T20:32:40.490053
---

# New Alpha Release: Tor Browser 15.0a3

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 15.0a3

by [boklm](/author/boklm)
| September 22, 2025

![](/static/images/lead.png)

Tor Browser 15.0a3 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/15.0a3/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

â ï¸ **Reminder**: Tor Browser Alpha release channel is for [testing only](https://community.torproject.org/user-research/become-tester/). If you are at risk or need strong anonymity, stick with the [stable release channel](https://www.torproject.org/download/).

## Full changelog

The full changelog since [Tor Browser 15.0a2](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) is:

* All Platforms
  + Updated Tor to 0.4.9.3-alpha
  + Updated OpenSSL to 3.5.3
  + [Bug tor-browser#43009](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43009): Backport Bug 1973265 - Put WebCodecs API behind RFP Target
  + [Bug tor-browser#43093](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43093): Refactor the patch to disable LaterRun
  + [Bug meta#43745](https://gitlab.torproject.org/tpo/applications/meta/-/issues/43745): Review Mozilla 1842838: HEVC (H265) playback related bugs. See the support status on the User Story. [tor-browser]
  + [Bug tor-browser#44032](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44032): Implement YEC 2025 Takeover for Desktop Stable
  + [Bug tor-browser#44199](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44199): Backport Security Fixes from Firefox 143
  + [Bug tor-browser-build#41429](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41429): Add a note about user safety to Tor Browser Alpha blog posts
  + [Bug tor-browser-build#41563](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41563): Do not copy Noto Color Emoji on Windows
* Windows + macOS + Linux
  + Updated Firefox to 140.3.0esr
  + [Bug tor-browser#42025](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42025): Purple elements (e.g. Tor buttons) need dark theme variants
  + [Bug tor-browser#43664](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43664): Review Mozilla 1842832: Move the private browsing toggle to initial install dialog
  + [Bug tor-browser#43770](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43770): Bugzilla 1958070: More BrowserGlue simplification/splitting
  + [Bug tor-browser#43966](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43966): Notify the user when they are in a custom security level (desktop)
  + [Bug tor-browser#44142](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44142): Missing document\_pdf.svg from our branding directories
  + [Bug tor-browser#44145](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44145): Switch onion connection icons to use --icon-color-critical and --icon-color
  + [Bug tor-browser#44180](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44180): Clear YEC 2024 preference
* Linux
  + [Bug tor-browser#43950](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43950): Review Mozilla 1894818: Support HEVC playback on Linux
  + [Bug tor-browser#43959](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43959): Make Noto Color Emoji the default emoji font on Linux
* Android
  + Updated GeckoView to 140.3.0esr
  + [Bug tor-browser#43755](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43755): Restore functionality of "switch to tab" urlbar suggestion
  + [Bug tor-browser#43943](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43943): Review Mozilla 1928705: Ship Android Font Restrictions as part of FPP
  + [Bug tor-browser#44172](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44172): Fix crash in TorAndroidIntegration.handleMessage()
* Build System
  + All Platforms
    - [Bug tor-browser-build#41064](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41064): Update tools/signing/README and add a tools/signing/machines-setup/README
    - [Bug tor-browser-build#41474](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41474): update README to explain moat-settings project requires `jq` to be installed
  + Windows + Linux + Android
    - Updated Go to 1.24.7
  + Linux
    - [Bug tor-browser-build#41561](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41561): Ship Noto Color Emoji on Linux

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-alpha-release-tor-browser-150a3/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-alpha-release-tor-browser-150a3/&text=Tor%20Browser%2015.0a3%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-alpha-release-tor-browser-150a3/&text=Tor%20Browser%2015.0a3%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Bluesky](https://bsky.app/intent/compose?text=Tor%20Browser%2015.0a3%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.%0Ahttps%3A//blog.torproject.org/new-alpha-release-tor-browser-150a3/)

## Comments

We encourage respectful, on-topic comments. Comments that violate our
[Code of Conduct](https://community.torproject.org/policies/code_of_conduct)
will be deleted. Off-topic comments may be deleted at the discretion of
the moderators. Please do not comment as a way to receive support or to
report bugs on a post unrelated to a release. If you are looking for
support, please see our [FAQ](https://support.torproject.org/),
[user support forum](https://forum.torproject.org/) or ways to
[get in touch with us](https://www.torproject.org/contact).

Join the discussion on the [Tor Project forum](https://forum.torproject.org/c/news/11)!

## Recent Updates

## [New Alpha Release: Tor Browser 15.0a3](/new-alpha-release-tor-browser-150a3/)

by [boklm](/author/boklm)
| September 22, 2025

Tor Browser 15.0a3 is now available from the Tor Browser download page and also from our distribution directory.

## [New Release: Tails 7.0](/new-release-tails-7_0/)

by [tails](/author/tails)
| September 18, 2025

We are very excited to present you Tails 7.0, the first version of Tails based
on Debian 13 (Trixie) and GNOME 48 (Bengaluru). Tails 7.0 brings new versions
of many applications included in Tails.

## [New Release: Tor Browser 14.5.7](/new-release-tor-browser-1457/)

by [ma1](/author/ma1)
| September 16, 2025

Tor Browser 14.5.7 is now available from the Tor Browser download page and also from our distribution directory.

### Download Tor Browser

Download Tor Browser to experience real private browsing without tracking, surveillance, or censorship.

[Download Tor Browser](https://www.torproject.org/download/)

### Subscribe to our Newsletter

Get m...