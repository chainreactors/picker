---
title: New Alpha Release: Tor Browser 14.0a8
url: https://blog.torproject.org/new-alpha-release-tor-browser-140a8/
source: Tor Project blog
date: 2024-10-08
fetch_date: 2025-10-06T18:55:02.032195
---

# New Alpha Release: Tor Browser 14.0a8

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 14.0a8

by [morgan](/author/morgan)
| October 7, 2024

![](/new-alpha-release-tor-browser-140a8/lead.png)

Tor Browser 14.0a8 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/14.0a8/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The full changelog since [Tor Browser 13.5a11](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) is:

* All Platforms
  + [Bug 1607032 + 1918202#30543](https://gitlab.torproject.org/tpo/applications/1607032%20%2B%201918202/-/issues/30543): compat: make spoofed orientation reflect spoofed screen dimensions [tor-browser]
  + [Bug tor-browser#42054](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42054): ESR128: investigate - thorin's list
  + [Bug tor-browser#42716](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42716): Disable unwanted about:\* pages
  + [Bug tor-browser#43170](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43170): Disable user-agent spoofing in HTTP header
  + [Bug tor-browser#43173](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43173): Backport security fixes from Firefox 131
  + [Bug tor-browser#43178](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43178): Audit fingerprinting overrides (MozBug 1834274)
* Windows + macOS + Linux
  + Updated Firefox to 128.3.0esr
  + [Bug tor-browser#43098](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43098): YEC 2024 Takeover for Desktop Stable
  + [Bug tor-browser#43149](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43149): Update donate URL in YEC 2024 desktop
  + [Bug tor-browser#43164](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43164): Prevent search-bar from being auto-hidden when not used for awhile
  + [Bug tor-browser#43169](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43169): compat: align userAgent in navigator + HTTP Header
* Android
  + Updated GeckoView to 128.3.0esr
  + [Bug tor-browser#42660](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42660): Review the patch on Android's ProxySelector
  + Bug 43102: Android notifications tell to make Firefox your default browser
  + [Bug tor-browser#43151](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43151): MOZ\_DATA\_REPORTING, MOZ\_TELEMETRY\_REPORTING, MOZ\_CRASHREPORTER, and MOZ\_BACKGROUNDTASKS enabled on Android
* Build System
  + All Platforms
    - Updated Go to 1.23.2
    - [Bug tor-browser#43156](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43156): Update translation CI to account for the extended 13.5 release
    - [Bug tor-browser#43157](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43157): Move tb-dev to base-browser
    - [Bug tor-browser#43181](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43181): Run translation CI if there is a change in a string.xml file
  + Windows + macOS + Linux
    - [Bug tor-browser-build#41247](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41247): Adapt tools/update-responses/update\_responses to support multiple versions in the same xml files
    - [Bug tor-browser-build#41256](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41256): tools/signing/upload-update\_responses-to-staticiforme should regenerate update-responses when it already exists
    - [Bug tor-browser-build#41259](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41259): Skip versions which don't set incremental\_from when generating incrementals

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-alpha-release-tor-browser-140a8/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-alpha-release-tor-browser-140a8/&text=Tor%20Browser%2014.0a8%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-alpha-release-tor-browser-140a8/&text=Tor%20Browser%2014.0a8%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Bluesky](https://bsky.app/intent/compose?text=Tor%20Browser%2014.0a8%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.%0Ahttps%3A//blog.torproject.org/new-alpha-release-tor-browser-140a8/)

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