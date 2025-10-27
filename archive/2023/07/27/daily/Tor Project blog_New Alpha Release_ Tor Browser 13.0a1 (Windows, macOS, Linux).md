---
title: New Alpha Release: Tor Browser 13.0a1 (Windows, macOS, Linux)
url: https://blog.torproject.org/new-alpha-release-tor-browser-130a1/
source: Tor Project blog
date: 2023-07-27
fetch_date: 2025-10-04T11:56:48.452324
---

# New Alpha Release: Tor Browser 13.0a1 (Windows, macOS, Linux)

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 13.0a1 (Windows, macOS, Linux)

by [richard](/author/richard)
| July 26, 2023

![](/new-alpha-release-tor-browser-130a1/lead.png)

Tor Browser 13.0a1 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/13.0a1/).

This release updates Firefox to 115.0.2esr, including bug fixes, stability improvements and important [security updates](https://www.mozilla.org/en-US/security/advisories/mfsa2023-26/). This is a Desktop platform only release (Windows, macOS, and Linux), but Android should be available in the coming weeks.

This is our first alpha release in the 13.0 series and represents a transition from Firefox 102-esr to Firefox 115-esr. This builds on a year's worth of upstream Firefox changes, so alpha-testers should expect to run into issues. If you find any issues, please report them on our [gitlab](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/new) or on the [Tor Project forum](https://forum.torproject.org/c/feedback/tor-browser-alpha-feedback/6).

We have started our annual esr transition audit, where we review Mozilla's year's worth of work with an eye for privacy and security issues that would negatively affect Tor Browser users. This will be completed before we transition the 13.0 alpha series to stable. At-risk users should remain on the 102-esr based 12.5 stable series which will continue to receive security updates until 13.0 alpha is promoted to stable.

We would like to thank volunteer contributor cypherpunks1 for their fixes for [tor-browser#26277](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/26277), [tor-browser#33955](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/33955), [tor-browser#41399](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41399), and [tor-browser#41791](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41791). If you would like to contribute, our issue tracker can be found [here](https://gitlab.torproject.org/tpo/applications/tor-browser/-/boards/1243#Platform).

## Full changelog

The full changelog since [Tor Browser 12.5a7](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) is:

* All Platforms
  + Updated Translations
  + Updated NoScript to 11.4.25
  + Updated OpenSSL to 3.0.9
  + Updated Go to 1.20.6
  + Updated tor to 0.4.8.2-alpha
  + [Bug tor-browser#40577](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40577): Add "suggest url" in DDG onion's manifest
  + [Bug tor-browser-build#40885](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40885): Bump version of snowflake to v2.6.0
  + [Bug tor-browser-build#40887](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40887): Update Webtunnel version to 38eb5505
  + [Bug tor-browser#41092](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41092): Enable tracking query parameters stripping
  + [Bug tor-browser#41399](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41399): Update Mozilla's patch for Bug 1675054 to enable brotli encoding for HTTP onions as well
  + [Bug tor-browser#41759](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41759): Rebase Base Browser to 115 nightly
  + [Bug tor-browser#41796](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41796): Rebase Tor Browser to Firefox 115
* Windows + macOS + Linux
  + Updated Firefox to 115.0.2esr
  + [Bug tor-browser#26277](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/26277): When "Safest" setting is enabled searching using duckduckgo should always use the Non-Javascript site for searches
  + [Bug tor-browser#33955](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/33955): Selecting "Copy image" from menu leaks the source URL to the clipboard. This data is often dereferenced by other applications.
  + [Bug tor-browser#41741](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41741): Refactor the domain isolator and new circuit
  + [Bug tor-browser#41834](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41834): Hide "Can't Be Removed - learn more" menu line for uninstallable add-ons
  + [Bug tor-browser#41842](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41842): Remove the old removal logics from Torbutton
  + [Bug tor-browser#41845](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41845): Stop forcing (bad) pref values for non-PBM users
  + [Bug tor-browser#41854](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41854): Download Spam Protection cannot be overridden to allow legitimate downloads
  + [Bug tor-browser#41874](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41874): Visual & A11 regressions in add-on badges
* Build System
  + All Platforms
    - [Bug tor-browser-build#40089](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40089): Clean up usage of get-moz-build-date script
    - [Bug tor-browser-build#40410](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40410): Get rid of python2
    - [Bug tor-browser-build#40487](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40487): Bump Python version
    - [Bug tor-browser-build#40802](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40802): Drop the patch for making WASI reproducible
    - [Bug tor-browser-build#40854](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40854): Update to OpenSSL 3.0
    - [Bug tor-browser-build#40855](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40855): Update toolchains for Mozilla 115
    - [Bug tor-browser-build#40868](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40868): Bump Rust to 1.69.0
    - [Bug tor-browser-build#40886](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40886): Update README with instructions for Arch linux
    - [Bug tor-browser-build#40889](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40889): Add mullvad sha256sums URL to tools/signing/download-unsigned-sha256sums-gpg-signatures-from-people-tpo
    - [Bug tor-browser-build#40894](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40894): Fix format of keyring/boklm.gpg
    - [Bug tor-browser-build#40898](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40898): Add doc from tor-browser-spec/processes/ReleaseProcess to gitlab issue templates
  + Windows
    - [Bug tor-browser-build#40832](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40832): Unify mingw-w64-clang 32+64 bits
  + Linux
    - [Bug tor-browser-build#40102](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40102): Move from Debian Jessie to Debian Stretch for our Linux builds

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-alpha-release-tor-browser-130a1/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-alpha-release-tor-browser-130a1/&text=Tor%20Browser%2013.0a1%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20di...