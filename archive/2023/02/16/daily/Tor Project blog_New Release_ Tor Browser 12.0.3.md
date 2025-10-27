---
title: New Release: Tor Browser 12.0.3
url: https://blog.torproject.org/new-release-tor-browser-1203/
source: Tor Project blog
date: 2023-02-16
fetch_date: 2025-10-04T06:48:44.181306
---

# New Release: Tor Browser 12.0.3

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tor Browser 12.0.3

by [richard](/author/richard)
| February 15, 2023

![](/new-release-tor-browser-1203/lead.png)

Tor Browser 12.0.3 is now available from the Tor Browser [download page](https://www.torproject.org/download/) and also
from our [distribution directory](https://dist.torproject.org/torbrowser/12.0.3/).

This release updates Firefox to 102.8, including bug fixes, stability improvements
and important [security updates](https://www.mozilla.org/en-US/security/advisories/mfsa2023-06/). There were no Android-specific security updates to backport from the Firefox 110 release.

We use this opportunity to update various components of Tor Browser as well:

* NoScript 11.4.16
* OpenSSL 1.1.1t

## Warning for NoScript users

Customized NoScript settings may be reset by the Tor Browser 12.0.3 upgrade.
In order to preserve them, it is advisable to `NoScript Options>Export` before updating and `NoScript Options>Import` afterwards.

## Credits

We would like to thank all of the community volunteers for their contributions this month! Specifically:

* t-m-w from CalyxOS for their fix for [tor-browser#40536](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40536)
* cypherpunks1 for their fixes for [tor-browser#41424](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41424), [tor-browser#41565](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41565), [tor-browser#40717](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40717), and [tor-browser#41578](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41578)
* trinity-1686a for their fix for [tor-browser#41066](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41066)
* p13dz for their fix for [tor-browser#40283](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40283)
* bentham for heads up on [tor-browser#41633](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41633)

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The full changelog since [Tor Browser 12.0.2](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/maint-12.0/projects/browser/Bundle-Data/Docs/ChangeLog.txt) is:

* All Platforms
  + Updated Translations
  + Updated OpenSSL to 1.1.1t
  + Updated NoScript to 11.4.16
  + [Bug tor-browser#40763](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40763): Stop using remote localized files in CFR
  + [Bug tor-browser#41424](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41424): Reduce disk activity by disabling some unnecessary tasks and telemetry
  + [Bug tor-browser#41565](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41565): Gate Telemetry Tasks behind AppConstants.MOZ\_TELEMETRY\_REPORTING
  + [Bug tor-browser#41601](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41601): Apply Snowflake Remove HelloVerify Countermeasure
* Windows + macOS + Linux
  + Updated Firefox to 102.8esr
  + [Bug tor-browser#32274](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/32274): Bad screen-reader UX for Security Level/Shield button
  + [Bug tor-browser#41066](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41066): Circuit Isolation should take containers into account
  + [Bug tor-browser#41561](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41561): Maximize warning is broken (regression)
  + [Bug tor-browser#41572](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41572): Check for userContextId also in the circuit display
  + [Bug tor-browser#41588](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41588): Use better words for the Tor Network description in the onboarding
* Windows
  + [Bug tor-browser#40717](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40717): UX: hide SSO
  + [Bug tor-browser#41578](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41578): Disable and lock Windows SSO
* macOS
  + [Bug tor-browser-build#28124](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/28124): Show Tor Browser icon as macOS volume (dmg) icon
* Android
  + Updated GeckoView to 102.8esr
  + [Bug tor-browser#40283](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40283): Can't upload files with Tor browser on Android
  + [Bug tor-browser#40536](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40536): Proxy Refused if link from other app opens Android TBB
  + [Bug tor-browser#41616](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41616): Backport Android-specific security fixes from Firefox 110 to ESR 102.8-based Tor Browser
* Build System
  + All Platforms
    - [Bug tor-browser-build#40723](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40723): Update upload-update\_responses-to-staticiforme step for new tor-browser-update-responses repository
    - [Bug tor-browser-build#40747](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40747): Remove empty line at the top of sha256sums-unsigned-build.txt
    - [Bug tor-browser-build#40748](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40748): When sha256sums-unsigned-build.txt contains an empty line, tools/dmg2mar prints a warning
  + macOS
    - [Bug tor-browser-build#40744](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40744): HFS DMG are not deterministic
    - [Bug tor-browser-build#40755](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40755): libdmg-hfsplus fails to build on debian stable
  + Android
    - [Bug tor-browser-build#40752](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40752): Wrong urls in download-android-\*.json files

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-release-tor-browser-1203/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-release-tor-browser-1203/&text=Tor%20Browser%2012.0.3%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-release-tor-browser-1203/&text=Tor%20Browser%2012.0.3%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Bluesky](https://bsky.app/intent/compose?text=Tor%20Browser%2012.0.3%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.%0Ahttps%3A//blog.torproject.org/new-release-tor-browser-1203/)

## Comments

We encourage respectful, on-topic comments. Comments that violate our
[Code of Conduct](https://community.torproject.org/policies/code_of_conduct)
will be deleted. Off-topic comments may be deleted at the discretion of
the moderators. Please do not comment as a way to receive support or to
report bugs on a post unrelated to a release. If you are looking for
support, please see our [FAQ](https://support.torproject.org/),
[user support forum](https://forum.torproject.org/) or ways to
[get in touch with us](https://www.torproject.org/contact).

Join the discussion on the [Tor Project forum](https://forum.torproj...