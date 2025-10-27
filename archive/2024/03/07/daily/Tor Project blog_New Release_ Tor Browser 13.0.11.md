---
title: New Release: Tor Browser 13.0.11
url: https://blog.torproject.org/new-release-tor-browser-13011/
source: Tor Project blog
date: 2024-03-07
fetch_date: 2025-10-06T17:11:30.303530
---

# New Release: Tor Browser 13.0.11

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tor Browser 13.0.11

by [richard](/author/richard)
| March 6, 2024

![](/new-release-tor-browser-13011/lead.png)

Tor Browser 13.0.11 is now available from the [Tor Browser download page](https://www.torproject.org/download/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/13.0.11/).

This is an emergency release which updates our the domain fronting configuration for the Snowflake pluggable transport and the moat connection to the rdsys backend used by the censorship circumvention system.

A known issue is that the source archives do not match likely due to a change in xz-utils (the underlying source in the archive is identical, only the compressed archive differs). This is not considered a blocker for this release and is being tracked here:

* <https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41102>

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The full changelog since [Tor Browser 13.0.10](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/maint-13.0/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) is:

* All Platforms
  + [Bug tor-browser#42435](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42435): Update moat domain fronting configuration
* Build System
  + All Platforms
    - [Bug tor-browser-build#41085](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41085): kick\_devmole\_build script prints wrong URL for Mullvad's build hashes
    - [Bug tor-browser-build#41097](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41097): authenticode-timestamping.sh fails to run again because tmp-timestamp already exists

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-release-tor-browser-13011/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-release-tor-browser-13011/&text=Tor%20Browser%2013.0.11%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-release-tor-browser-13011/&text=Tor%20Browser%2013.0.11%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Bluesky](https://bsky.app/intent/compose?text=Tor%20Browser%2013.0.11%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.%0Ahttps%3A//blog.torproject.org/new-release-tor-browser-13011/)

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