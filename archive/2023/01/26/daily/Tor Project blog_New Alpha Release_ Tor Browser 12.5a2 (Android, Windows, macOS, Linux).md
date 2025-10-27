---
title: New Alpha Release: Tor Browser 12.5a2 (Android, Windows, macOS, Linux)
url: https://blog.torproject.org/new-alpha-release-tor-browser-125a2/
source: Tor Project blog
date: 2023-01-26
fetch_date: 2025-10-04T04:55:17.301924
---

# New Alpha Release: Tor Browser 12.5a2 (Android, Windows, macOS, Linux)

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 12.5a2 (Android, Windows, macOS, Linux)

by [richard](/author/richard)
| January 25, 2023

![](/new-alpha-release-tor-browser-125a2/lead.png)

Tor Browser 12.5a2 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/12.5a2/).

This release updates Firefox on Android, Windows, macOS, and Linux to 102.7.0esr. It includes important [security updates](https://www.mozilla.org/en-US/security/advisories/mfsa2023-02/) to Firefox and GeckoView. There were no Android-specific security updates to backport from the Firefox 109 release.

We use this opportunity to update various other components of Tor Browser as well:

* tor 0.4.7.13
* NoScript 11.4.14
* go 1.19.5

We would like to thank user ryotak for identifying a script blocking bypass on local file:// resources. We would also like to thank user cypherpunks1 for their help with [tor-browser#40717](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40717) and [tor-browser#41578](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41578) (among others). If you would like to contribute patches or help diagnose issues, please join us on our [gitlab instance](https://gitlab.torproject.org/tpo/applications/tor-browser)!

The full changelog since [Tor Browser 12.5a1](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs/ChangeLog.txt) is:

* All Platforms
  + Updated tor to 0.4.7.13
  + Updated NoScript to 11.4.14
  + [Bug tor-browser#40565](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40565): do something with security.tls.version.enable-deprecated
  + [Bug tor-browser-build#40727](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40727): Update list of Snowflake STUN servers in default bridge line
  + [Bug tor-browser#41066](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41066): Circuit Isolation should take containers into account
  + [Bug tor-browser#41428](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41428): Check if we can create our own directories for branding
  + [Bug tor-browser#41506](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41506): Remove TrustCor root certificates
* Windows + macOS + Linux
  + Updated Firefox to 102.7esr
  + [Bug tor-browser#32274](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/32274): Bad screen-reader UX for Security Level/Shield button
  + [Bug tor-browser-build#40733](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40733): Use the new branding directories
  + [Bug tor-browser#41393](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41393): about:tbupdate semantic and accessibility problems
  + [Bug tor-browser#41539](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41539): Crypto warning weaknesses
  + [Bug tor-browser#41549](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41549): tor freeze when receiving to many http proxy requests on socks port
  + [Bug tor-browser#41561](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41561): Maximize warning is broken (regression)
  + [Bug tor-browser#41562](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41562): API-triggered fullscreen after F11 causes letterboxing to crop the page
  + [Bug tor-browser#41563](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41563): Old placeholders used in TorStrings.jsm
  + [Bug tor-browser#41572](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41572): Check for userContextId also in the circuit display
  + [Bug tor-browser#41577](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41577): Disable profile migration
* Windows + Linux
  + [Bug tor-browser-build#40714](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40714): Ship NoScript in the distribution directory also for Windows and Linux
* Windows
  + [Bug tor-browser#40717](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40717): UX: hide SSO
  + [Bug tor-browser#41578](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41578): Disable and lock Windows SSO
* macOS
  + [Bug tor-browser-build#28124](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/28124): Show Tor Browser icon as macOS volume (dmg) icon
  + [Bug tor-browser-build#40719](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40719): Allow non-universal macOS builds also on base-browser
  + [Bug tor-browser#41535](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41535): Remove the old, unused and undocumented "-invisible" macOS CLI flag
* Android
  + Updated GeckoView to 102.7esr
  + [Bug tor-browser#40283](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40283): Can't upload files with Tor browser on Android
  + [Bug tor-browser#41571](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41571): Backport Android-specific Firefox 109 to ESR 102.7-based Tor Browser
* Build System
  + All Platforms
    - Updated Go to 1.19.5
    - [Bug tor-browser-build#40720](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40720): Update fetch-changelogs.py scripts to support new Build System label
    - [Bug tor-browser-build#40735](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40735): Add command to list which translation components need to be updated
    - [Bug tor-browser-build#40739](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40739): tor-expert-bundle should include ClientTransportPlugin torrc lines for each pluggable transport
    - [Bug tor-browser#41567](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41567): Build outputs now going to obj-*/dist/torbrower rather than obj-*/dist/firefox
  + Windows + macOS + Linux
    - [Bug tor-browser-build#40732](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40732): Review Bundle-Data and try not to ship the default profile in base browser
  + macOS
    - [Bug tor-browser-build#40706](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40706): macos-signer-stapler should wait for user interaction before attempting stapling
    - [Bug tor-brower-build#40744](https://gitlab.torproject.org/tpo/applications/tor-brower-build/-/issues/40744): HFS DMG are not deterministic
  + Android
    - [Bug tor-browser-build#40738](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40738): Update Android git hashes templates

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-alpha-release-tor-browser-125a2/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-alpha-release-tor-browser-125a2/&text=Tor%20Browser%2012.5a2%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-alpha-release-tor-browser-125a2/&text=Tor%20Browser%2012.5a2%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Bluesky](https://bsky.app/intent/compose?text=Tor%20B...