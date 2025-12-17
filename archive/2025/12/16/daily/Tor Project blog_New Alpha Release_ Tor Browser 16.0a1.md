---
title: New Alpha Release: Tor Browser 16.0a1
url: https://blog.torproject.org/new-alpha-release-tor-browser-160a1/
source: Tor Project blog
date: 2025-12-16
fetch_date: 2025-12-17T03:20:31.128754
---

# New Alpha Release: Tor Browser 16.0a1

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 16.0a1

by [ma1](/author/ma1)
| December 16, 2025

![](/new-alpha-release-tor-browser-160a1/lead.png)

Tor Browser 16.0a1 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/16.0a1/).

This is **the first Tor Browser Alpha release based on Firefox Rapid Release**: read more about this important change in [The Future of Tor Browser Alpha](https://blog.torproject.org/future-of-tor-browser-alpha/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

â ï¸ **Reminder**: Tor Browser Alpha release channel is for [testing only](https://community.torproject.org/user-research/become-tester/). If you are at risk or need strong anonymity, stick with the [stable release channel](https://www.torproject.org/download/).

## Full changelog

The [full changelog](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) since Tor Browser 15.0a4 is:

* All Platforms
  + Updated NoScript to 13.5.1.90101984
  + [Bug tor-browser#43792](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43792): Determine whether noscript\_persist users need to have their NoScript settings migrated
  + [Bug tor-browser#43998](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43998): Rebase Tor Browser Alpha onto 141.0
  + [Bug tor-browser#44118](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44118): Decide how to deal with upstream feature gates in a RR world
  + [Bug tor-browser#44280](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44280): Test stream isolation
  + [Bug tor-browser#44333](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44333): Add the "No AI" version of DuckDuckGo to available search engines
  + [Bug tor-browser#44365](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44365): Fix CSS linting errors introduced for firefox 145
  + [Bug tor-browser#44391](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44391): Restrictions cascade blocks every capability in subframes (e.g. captchas)
  + [Bug tor-browser#44408](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44408): Fix TorDomainIsolator in 146
  + [Bug tor-browser#44418](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44418): Update built-in obfs4 bridges
  + [Bug tor-browser-build#41609](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41609): Move back to CDN77 for default snowflake bridge
  + [Bug tor-browser-build#41646](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41646): Update lyrebird version to v0.7.0
  + [Bug mullvad-browser#483](https://gitlab.torproject.org/tpo/applications/mullvad-browser/-/issues/483): Add the "No AI" version of DuckDuckGo to available search engines
  + [Bug mullvad-browser#487](https://gitlab.torproject.org/tpo/applications/mullvad-browser/-/issues/487): Search engines are sorted alphabetically rather than the desired order
* Windows + macOS + Linux
  + Updated Firefox to 146.0a1esr
  + [Bug tor-browser#44302](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44302): Fix the flags of some about pages
  + [Bug tor-browser#44310](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44310): Default zoom always resets to 100%
  + [Bug tor-browser#44411](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44411): DownloadsTorWarning.sys.mjs fails to load
  + [Bug tor-browser#44419](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44419): Re-add the moz-toggle title attribute patch
* Linux
  + [Bug tor-browser#44273](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44273): Restore Noto CJK as Jigmo has a too low readability
  + [Bug tor-browser#44315](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44315): Font/text issue with self-upgrade window
* Android
  + Updated GeckoView to 146.0a1esr
  + [Bug tor-browser#44303](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44303): Extension update job might never work on Android
  + [Bug tor-browser#44324](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44324): Refactor the NSS no proxy-bypass patch on A-S to avoid -Wunreachable-code
* Build System
  + All Platforms
    - [Bug tor-browser#43951](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43951): Include product with the component in triage CSVs
    - [Bug tor-browser-build#40903](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40903): Make xz multi-threaded
    - [Bug tor-browser-build#41445](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41445): Better handle bugzilla "Web Compatibility" issues in generate-bugzilla-triage-csv
    - [Bug tor-browser-build#41607](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41607): Fix regression from #41373 in tools/count-mar-downloads
    - [Bug tor-browser-build#41608](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41608): Add per-platform numbers for incrementals in count-mar-downloads
    - [Bug tor-browser-build#41643](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41643): Update toolchains for Firefox 146
    - [Bug tor-browser-build#41644](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41644): Self-hosted browser extensions support in relprep.py
    - [Bug tor-browser-build#41647](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41647): Add a XZ\_DEFAULTS to set\_default\_env
    - [Bug tor-browser-build#41648](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41648): Add a mozconfig to projects/geckoview
    - [Bug tor-browser-build#41654](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41654): Make relprep.py update Moat settings
  + Windows + macOS + Linux
    - [Bug tor-browser-build#41662](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41662): Add python-zstandard to desktop containers
  + Windows + Linux + Android
    - [Bug tor-browser-build#41580](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41580): Update Go major to 1.25.x
    - Updated Go to 1.25.5
  + macOS
    - [Bug tor-browser-build#41665](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41665): Update macos signing wrapper for new executable gpu-helper.app
  + Linux
    - [Bug tor-browser-build#41601](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41601): Upstream droppped Linux i686 support
    - [Bug tor-browser-build#41627](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41627): Firefox build system needs a more recent version of OpenSSL on Linux
    - [Bug tor-browser-build#41632](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41632): Ship Linux aarch64 builds in Alpha Release Channel
    - [Bug tor-browser-build#41639](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41639): Remove linux-arm target
    - [Bug tor-browser-build#41640](h...