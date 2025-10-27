---
title: New Alpha Release: Tor Browser 12.5a1 (Android, Windows, macOS, Linux)
url: https://blog.torproject.org/new-alpha-release-tor-browser-125a1/
source: Tor Project blog
date: 2022-12-22
fetch_date: 2025-10-04T02:14:56.328340
---

# New Alpha Release: Tor Browser 12.5a1 (Android, Windows, macOS, Linux)

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 12.5a1 (Android, Windows, macOS, Linux)

by [richard](/author/richard)
| December 21, 2022

![](/new-alpha-release-tor-browser-125a1/lead.png)

Tor Browser 12.5a1 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/12.5a1/).

Tor Browser 12.5a1 updates Firefox on Android, Windows, macOS, and Linux to 102.6.0esr.

We use this opportunity to update various other components of Tor Browser as well:

* tor 0.4.7.12
* go 1.19.4

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/mfsa2022-52/) to Firefox and GeckoView. There were no Android-specific security updates to backport from the Firefox 108 release.

The full changelog since [Tor Browser 12.0a5](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs/ChangeLog.txt) is:

* All Platforms
  + Updated tor to 0.4.7.12
  + [Bug tor-browser-build#40711](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40711): Review and expand the stakeholders we communicate major changes to
  + [Bug tor-browser#41478](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41478): Drop the torbutton submodule in 12.5
  + [Bug tor-browser#41514](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41514): eslint broken since migrating torbutton
* Windows + macOS + Linux
  + Updated Firefox to 102.6esr
  + [Bug tor-browser#26504](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/26504): about:preferences shows Firefox's version instead of Tor Browser's
  + [Bug tor-browser#32308](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/32308): Stop inner letterbox jiggling as border is dragged
  + [Bug tor-browser#40347](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40347): URL bar lock icon says connection is not secure when on "view-source:[...].onion" URLs
  + [Bug tor-browser-build#40678](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40678): Force all 11.5 users to update through 11.5.8 before 12.0
  + [Bug tor-browser#41375](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41375): Clean unused strings
  + [Bug tor-browser#41435](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41435): Add a Tor Browser migration function
  + [Bug tor-browser#41448](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41448): User `danger` style for primary button in new identity modal
  + [Bug tor-browser#41483](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41483): Tor Browser says Firefox timed out, confusing users
  + [Bug tor-browser#41503](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41503): Disable restart in case of reboot and restore in case of crash
  + [Bug tor-browser#41520](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41520): Regression: rearranging bookmarks / place items by drag & drop doesn't work anymore
  + [Bug tor-browser#41524](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41524): about:tbupdate needs UTF-8
  + [Bug tor-browser#41525](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41525): Drop locales from torbutton, since we will inject them in tor-browser-build
* macOS + Linux
  + [Bug tor-browser#41519](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41519): TOR\_SOCKS\_IPC\_PATH environment variable not honored
* Windows
  + [Bug tor-browser-build#40708](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40708): tor.exe in tor-expert-bundle not writing stdout even when run from cmd.exe
* macOS
  + [Bug tor-browser-build#40716](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40716): Unable to update to 12.0.1 on Apple Silicon-based Mac
* Android
  + Updated GeckoView to 102.6esr
  + [Bug tor-browser#41001](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41001): Remove remaining security slider code
* Build System
  + All Platforms
    - Updated Go to 1.19.4
    - [Bug tor-browser-build#40645](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40645): Verify we no longer depend on any signed tags from sysrqb and gk, and remove them from torbutton.gpg
    - [Bug tor-browser-build#40679](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40679): Use the latest translations for nightly builds
    - [Bug tor-browser-build#40681](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40681): Run apt-get clean, after installing packages in projects/container-image/config
    - [Bug tor-browser-build#40683](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40683): Install more packages in the default containers to reduce the number of custom containers
    - [Bug tor-browser-build#40689](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40689): Update Ubuntu version from projects/mmdebstrap-image/config to 22.04.1
    - [Bug tor-browser-build#40717](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40717): Create a script to prepare changelogs
  + Windows + macOS + Linux
    - [Bug tor-browser-build#40707](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40707): Update update\_responses\_config.yml to allow 11.5.8 to update to whatever latest is
    - [Bug tor-browser-build#40713](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40713): Use the new tor-browser l10n branch in Firefox
  + Linux + Android
    - [Bug tor-browser-build#40653](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40653): Build compiler-rt with runtimes instead of the main LLVM build
  + macOS
    - [Bug tor-browser-build#40694](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40694): aarch64 tor-expert-bundle for macOS is not exported as part of the browser build
    - [Bug tor-browser-build#40704](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40704): Building nightly macos incrementals fails
  + Linux
    - [Bug tor-browser-build#40693](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40693): Can't build container-image in main
  + Android
    - [Bug tor-browser-build#40702](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40702): Nightly builds fails with "error: pathspec 'tor-browser-102.5.0esr-12.0-2' did not match any file(s) known to git"

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-alpha-release-tor-browser-125a1/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-alpha-release-tor-browser-125a1/&text=Tor%20Browser%2012.5a1%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-alpha-release-tor-browser-125a1/&text=Tor%20Browser%2012.5a1%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Bluesky](https://bsky.app/intent/compose?text=Tor%20Browser%2012.5a1%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20...