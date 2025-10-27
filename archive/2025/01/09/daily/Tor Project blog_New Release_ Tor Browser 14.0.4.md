---
title: New Release: Tor Browser 14.0.4
url: https://blog.torproject.org/new-release-tor-browser-1404/
source: Tor Project blog
date: 2025-01-09
fetch_date: 2025-10-06T20:15:00.150112
---

# New Release: Tor Browser 14.0.4

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tor Browser 14.0.4

by [morgan](/author/morgan)
| January 8, 2025

![](/new-release-tor-browser-1404/lead.png)

Tor Browser 14.0.4 is now available from the [Tor Browser download page](https://www.torproject.org/download/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/14.0.4/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The full changelog since [Tor Browser 14.0.3](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/maint-14.0/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) is:

* All Platforms
  + Updated NoScript to 12.1.1
  + [Bug tor-browser#42125](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42125): lock RFP part 2
  + [Bug tor-browser#43176](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43176): noscript-marker CSP warnings in the console
  + [Bug tor-browser#43282](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43282): Unable to click/tap/select anything adjacent the WebGL placeholders
  + [Bug tor-browser#43296](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43296): NoScript-blocked video content placeholder is not centered
  + [Bug tor-browser#43338](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43338): Custom zoom + "Zoom text only" breaks pdfjs
  + [Bug tor-browser#43343](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43343): Remove YEC 2024
  + [Bug tor-browser#43352](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43352): Failing connection attempts to multicast IPv6 ff00:::443 logged during NoScript updates
  + [Bug tor-browser#43366](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43366): Do not use system accent color in inputs
  + [Bug tor-browser#43382](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43382): Rebase Tor Browser Stable onto 128.6.0esr
  + [Bug tor-browser#43384](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43384): Backport security fixes from Firefox 134
  + [Bug tor-browser-build#41333](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41333): Update STUN servers in Snowflake builtin bridges
  + [Bug tor-browser-build#41338](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41338): Add CDN77 meek bridge
* Windows + macOS + Linux
  + Updated Firefox to 128.6.0esr
  + [Bug tor-browser#43269](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43269): NoScript localization issue
* Linux
  + [Bug tor-browser-build#41311](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41311): AppArmor profile fails on Debian stable
  + [Bug tor-browser-build#41313](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41313): Show waiting cursor while app opens
* Android
  + Updated GeckoView to 128.6.0esr
* Build System
  + All Platforms
    - Updated Go to 1.22.10
    - [Bug tor-browser-build#41321](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41321): Update PieroV's expired keys
    - [Bug tor-browser-build#41340](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41340): Update kick\_devmole\_build script with Mullvad's new GitHub workflow endpoint
  + macOS
    - [Bug tor-browser-build#41325](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41325): Newer versions of 7z fail to extract our dmg files because of the /Applications symlink
    - [Bug tor-browser-build#41327](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41327): Print more logs when make\_full\_update.sh failed to generate mar file in dmg2mar
  + Android
    - [Bug tor-browser#42690](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42690): Add the commands to produce the APKs to tools/geckoview

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-release-tor-browser-1404/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-release-tor-browser-1404/&text=Tor%20Browser%2014.0.4%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-release-tor-browser-1404/&text=Tor%20Browser%2014.0.4%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Bluesky](https://bsky.app/intent/compose?text=Tor%20Browser%2014.0.4%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.%0Ahttps%3A//blog.torproject.org/new-release-tor-browser-1404/)

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

Trademark, copyright notices, and rules for use by third parties can be found in our [FAQ](https://www.torproject.org/about/trademark/).