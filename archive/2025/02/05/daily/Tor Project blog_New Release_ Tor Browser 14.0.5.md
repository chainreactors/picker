---
title: New Release: Tor Browser 14.0.5
url: https://blog.torproject.org/new-release-tor-browser-1405/
source: Tor Project blog
date: 2025-02-05
fetch_date: 2025-10-06T20:53:43.315313
---

# New Release: Tor Browser 14.0.5

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tor Browser 14.0.5

by [pierov](/author/pierov)
| February 4, 2025

![](/new-release-tor-browser-1405/lead.png)

Tor Browser 14.0.5 is now available from the [Tor Browser download page](https://www.torproject.org/download/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/14.0.5/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The [full changelog](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/maint-14.0/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) since Tor Browser 14.0.4 is:

* All Platforms
  + [Bug tor-browser#41065](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41065): navigator.storage "best effort" + "persistent" leak partitionSize/totalSpace entropy
  + [Bug tor-browser#43386](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43386): Extension requests expose Firefox's minor version and custom app name
  + [Bug tor-browser#43447](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43447): Backport stable and legacy: Some .tor.onion sites are not displaying the underlying V3 onion address in alpha
  + [Bug tor-browser#43448](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43448): Rebase Tor Browser release onto 128.7.0esr
  + [Bug tor-browser#43451](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43451): Backport security fixes from Firefox 135
  + [Bug tor-browser-build#41328](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41328): Exclude tor dependencies from LD\_LIBRARY\_PATH
* Windows + macOS + Linux
  + Updated Firefox to 128.7.0esr
  + [Bug tor-browser#43312](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43312): Download popup panel progress bar overflows
* Linux
  + [Bug tor-browser#43236](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43236): High refresh rate detectable by websites when Wayland (MOZ\_ENABLE\_WAYLAND=1) is used
  + [Bug tor-browser#43326](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43326): Launching tor-browser on gentoo fails with "version `OPENSSL\_3.2.0' not found"
* Android
  + Updated GeckoView to 128.7.0esr
* Build System
  + All Platforms
    - Updated Go to 1.22.11
    - [Bug tor-browser-build#41324](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41324): Improve build signing ergonomics
    - [Bug tor-browser-build#41343](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41343): Add signing step to clean some files such as test artifacts
    - [Bug tor-browser-build#41345](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41345): Go autoupdates in 1.23 so add env var to prevent it in any step that has network access
    - [Bug tor-browser-build#41350](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41350): Increase timeout in rcodesign-notary-submit
    - [Bug tor-browser-build#41357](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41357): keyring/anti-censorship.gpg is in `GPG keybox database version 1` format

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-release-tor-browser-1405/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-release-tor-browser-1405/&text=Tor%20Browser%2014.0.5%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-release-tor-browser-1405/&text=Tor%20Browser%2014.0.5%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Bluesky](https://bsky.app/intent/compose?text=Tor%20Browser%2014.0.5%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.%0Ahttps%3A//blog.torproject.org/new-release-tor-browser-1405/)

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