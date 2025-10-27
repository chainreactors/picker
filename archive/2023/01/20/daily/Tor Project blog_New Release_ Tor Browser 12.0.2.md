---
title: New Release: Tor Browser 12.0.2
url: https://blog.torproject.org/new-release-tor-browser-1202/
source: Tor Project blog
date: 2023-01-20
fetch_date: 2025-10-04T04:24:51.243363
---

# New Release: Tor Browser 12.0.2

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tor Browser 12.0.2

by [richard](/author/richard)
| January 19, 2023

![](/new-release-tor-browser-1202/lead.png)

Tor Browser 12.0.2 is now available from the Tor Browser [download page](https://www.torproject.org/download/) and also
from our [distribution directory](https://dist.torproject.org/torbrowser/12.0.2/).

This release updates Firefox to 102.7, including bug fixes, stability improvements
and important [security updates](https://www.mozilla.org/en-US/security/advisories/mfsa2023-02/). There were no Android-specific security updates to backport from the Firefox 109 release.

We use this opportunity to update various components of Tor Browser as well:

* tor 0.4.7.13
* NoScript 11.4.14
* go 1.19.5

We would like to thank user ryotak for identifying a script blocking bypass on local file:// resources.

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The full changelog since [Tor Browser 12.0.1](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/maint-12.0/projects/browser/Bundle-Data/Docs/ChangeLog.txt) is:

* All Platforms
  + Updated tor to 0.4.7.13
  + Updated NoScript to 11.4.14
  + [Bug tor-browser#40565](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40565): do something with security.tls.version.enable-deprecated
  + [Bug tor-browser-build#40713](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40713): Use the new tor-browser l10n branch in Firefox
  + [Bug tor-browser-build#40727](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40727): Update list of Snowflake STUN servers in default bridge line
  + [Bug tor-browser#41506](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41506): Remove TrustCor root certificates
  + [Bug tor-browser#41525](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41525): Drop locales from torbutton, since we will inject them in tor-browser-build
* Windows + macOS + Linux
  + Updated Firefox to 102.7esr
  + [Bug tor-browser#26504](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/26504): Browser version in about:preferences showing the Firefox ESR version
  + [Bug tor-browser#32308](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/32308): Stop inner letterbox jiggling as border is dragged
  + [Bug tor-browser#41375](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41375): Clean unused strings
  + [Bug tor-browser#41393](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41393): about:tbupdate semantic and accessibility problems
  + [Bug tor-browser#41522](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41522): Backport torbutton -> tor-browser migration to 12.0 series
  + [Bug tor-browser#41524](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41524): about:tbupdate needs UTF-8
  + [Bug tor-browser#41539](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41539): Crypto warning weaknesses
  + [Bug tor-browser#41549](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41549): tor freeze when receiving to many http proxy requests on socks port
  + [Bug tor-browser#41561](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41561): Maximize warning is broken (regression)
  + [Bug tor-browser#41563](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41563): Old placeholders used in TorStrings.jsm
* macOS
  + [Bug tor-browser-build#40716](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40716): Unable to update to 12.0.1 on Apple Silicon-based Mac
* Android
  + Updated GeckoView to 102.7esr
  + [Bug tor-browser#41571](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41571): Backport Android-specific Firefox 109 to ESR 102.7-based Tor Browser
* Build System
  + All Platforms
    - Updated Go to 1.19.5
    - [Bug tor-browser-build#40735](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40735): Add command to list which translation components need to be updated
    - [Bug tor-browser-build#40739](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40739): tor-expert-bundle should include ClientTransportPlugin torrc lines for each pluggable transport
  + Windows + macOS + Linux
    - [Bug tor-browser-build#40734](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40734): Backport the translation project
  + macOS
    - [Bug tor-browser-build#40706](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40706): macos-signer-stapler should wait for user interaction before attempting stapling

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-release-tor-browser-1202/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-release-tor-browser-1202/&text=Tor%20Browser%2012.0.2%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-release-tor-browser-1202/&text=Tor%20Browser%2012.0.2%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Bluesky](https://bsky.app/intent/compose?text=Tor%20Browser%2012.0.2%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.%0Ahttps%3A//blog.torproject.org/new-release-tor-browser-1202/)

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

Get monthly updates and opportunities from the Tor Project:

[Sign up](https://newsletter.torproject.org/)

####

####

####

####

####

####

####

####
...