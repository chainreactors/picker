---
title: New Alpha Release: Tor Browser 16.0a8
url: https://blog.torproject.org/new-alpha-release-tor-browser-160a8/
source: Tor Project blog
date: 2026-07-02
fetch_date: 2026-07-03T05:48:52.220975
---

# New Alpha Release: Tor Browser 16.0a8

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 16.0a8

by [ma1](/author/ma1)
| July 2, 2026

![](/new-alpha-release-tor-browser-160a8/lead.png)

Tor Browser 16.0a8 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/16.0a8/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

â ï¸ **Reminder**: The Tor Browser Alpha release-channel is for [testing only](https://community.torproject.org/user-research/become-tester/). As such, Tor Browser Alpha is not intended for general use because it is more likely to include bugs affecting usability, security, and privacy.

Moreover, Tor Browser Alphas are now based on Firefox's betas. Please read more about this important change in the [Future of Tor Browser Alpha](https://blog.torproject.org/future-of-tor-browser-alpha/) blog post.

If you are an at-risk user, require strong anonymity, or just want a reliably-working browser, please stick with the [stable release channel](https://www.torproject.org/download/).

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The [full changelog](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) since Tor Browser 16.0a7 is:

* All Platforms
  + Updated NoScript to 13.6.25.90301984
  + Updated Tor to 0.4.9.11
  + Updated OpenSSL to 3.5.7
  + [Bug tor-browser#44857](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44857): Drop `browser.display.use_system_colors` from our preference list
  + [Bug tor-browser#44896](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44896): Review Mozilla 2030929: Remove unused pref privacy.partition.network\_state
  + [Bug tor-browser#45018](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45018): resistfingerprinting not available in appearance.mjs in 152
  + [Bug tor-browser#45019](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45019): ReportBrokenSite startup error in 152
  + [Bug tor-browser#45047](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45047): Cross-site oracle via worklet rejection error in Safer Mode
  + [Bug tor-browser#45072](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45072): Disable XSLT already for 16.0
* Windows + macOS + Linux
  + Updated Firefox to 152.0a1
  + [Bug tor-browser#44528](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44528): Make sure desktop IP Protection is disabled on desktop
  + [Bug tor-browser#44795](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44795): Revert BB 27604 patch as not needed anymore
  + [Bug tor-browser#44844](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44844): Use new urlbar CSS variables
  + [Bug tor-browser#44888](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44888): Use `--button-opacity-disabled` for disabled styling.
  + [Bug tor-browser#44955](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44955): Use `context-fill` for `about-wordmark.svg`
  + [Bug tor-browser#44956](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44956): Switch colours in letterboxing setting icons to match the tab-alignment icons
  + [Bug tor-browser#45016](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45016): Several errors about EngineProcess.sys.mjs in 152
  + [Bug tor-browser#45017](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45017): Wrong letterboxing background in 152
  + [Bug tor-browser#45037](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45037): Potential runtime errors in the search service when changing JS status
  + [Bug tor-browser#45043](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45043): Re-add missing changes to settings after 151/152 rebase
  + [Bug tor-browser#45083](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45083): Error in about:preferences due to ipprotection missing
* macOS
  + [Bug tor-browser#44728](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44728): Bundled fonts are broken on macOS when the GPU process is enabled
* Linux
  + [Bug @ libfontconfig.so.1#45048](https://gitlab.torproject.org/tpo/applications/%40%20libfontconfig.so.1/-/issues/45048): Backport Bugzilla 2041887: Crash in after users upgraded to fontconfig 2.18.0 [tor-browser]
* Android
  + Updated GeckoView to 152.0a1
  + [Bug tor-browser#43856](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43856): Fix onBackPressed() deprecation
  + [Bug tor-browser#44091](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44091): Add frequent regions to tor connection assist for android
  + [Bug tor-browser#44175](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44175): Remove all default browser functionality (Android)
  + [Bug tor-browser#44769](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44769): TBA crash screen has firefox asset as well as a "Send crash report" button
  + [Bug tor-browser#45052](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45052): Initialise Tor modules on android in the same order as desktop
* Build System
  + All Platforms
    - [Bug tor-browser-build#41802](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41802): Remove the tor daemon requirement for signing
    - [Bug tor-browser-build#41809](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41809): Update toolchains for Firefox 152
    - [Bug tor-browser-build#41813](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41813): Disable build artifacts in `make generate_gradle_dependencies_list-geckoview`
    - [Bug tor-browser-build#41821](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41821): Update gpg subkeys for boklm
    - [Bug tor-browser-build#41823](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41823): Add versions information to the toolchain list update
    - [Bug tor-browser-build#41827](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41827): Update morgan's keychain with renewed key
  + Windows + Linux + Android
    - Updated Go to 1.26.4
  + Windows
    - [Bug tor-browser-build#41810](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41810): Define GetAddrInfoExCancel on mingw
  + Android
    - [Bug tor-browser#45086](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45086): Compress omni.ja with xz on Android
    - [Bug tor-browser-build#41830](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41830): Update the browser project to change omni.ja.xz

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-alpha-release-tor-browser-160a8/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-alpha-release-tor-browser-160a8/&text=Tor%20Browser%2016.0a8%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Mastodon](https://mastodonshare.com/?url=ht...