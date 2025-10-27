---
title: New Alpha Release: Tor Browser 14.0a7
url: https://blog.torproject.org/new-alpha-release-tor-browser-140a7/
source: Tor Project blog
date: 2024-09-28
fetch_date: 2025-10-06T18:30:45.724444
---

# New Alpha Release: Tor Browser 14.0a7

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 14.0a7

by [morgan](/author/morgan)
| September 27, 2024

![](/new-alpha-release-tor-browser-140a7/lead.png)

Tor Browser 14.0a7 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/14.0a7/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

Tor Browser 14.0a7 is our first release-candidate build for Tor Browser 14.0. Tor Browser 14.0a7 should have full feature-parity with the Tor Browser 13.5 series. After this point, we should primarily be focused on QA and bug-fixes. The current plan is to have another release-candidate build next week followed by the Tor Browser 14.0 release on October 14.

## Volunteer as an alpha tester

Now would be an excellent time to become a tester and ensure that the newest Tor Browser works for you. To learn more, please see our previous blog-post on the subject:

* <https://blog.torproject.org/vounteer-as-an-alpha-tester/>

## Bugzilla triage and review

We have 6 remaining upstream Bugzilla issues to review and potentially develop patches for.

This work can be tracked in [this Gitlab query](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/?sort=updated_desc&state=opened&search=Review%20Mozilla&label_name%5B%5D=14.0%20stable&first_page_size=100).

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The full changelog since [Tor Browser 14.0a6](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) is:

* All Platforms
  + Updated NoScript to 11.4.40
  + [Bug tor-browser#42832](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42832): Download spam prevention should not affect browser extensions
  + [Bug tor-browser#43163](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43163): Disable offscreen canvas until verified it is not fingerprintable
  + [Bug tor-browser#43166](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43166): Rebase Tor Browser alpha onto Firefox 128.3.0esr
* Windows + macOS + Linux
  + Updated Firefox to 128.3.0esr
  + [Bug tor-browser#42070](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42070): Backport Bugzilla 1834307 and hide smooth-scroll UX
  + [Bug tor-browser#42362](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42362): "New window" missing from File menu
  + [Bug tor-browser#42742](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42742): Inconsistent use of "New private window" vs "New window"
  + [Bug tor-browser-build#41248](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41248): Check and update bundled font versions
* Android
  + Updated GeckoView to 128.3.0esr
  + [Bug tor-browser#43172](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43172): remove remote settings and SERPTelemetry
* Build System
  + All Platforms
    - Updated Go to 1.23.1
    - [Bug tor-browser-build#41236](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41236): Remove binutils when not needed
  + Windows + macOS + Linux
    - [Bug tor-browser-build#41246](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41246): Add updater rewriterules to make 13.5a10 a watershed

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-alpha-release-tor-browser-140a7/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-alpha-release-tor-browser-140a7/&text=Tor%20Browser%2014.0a7%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-alpha-release-tor-browser-140a7/&text=Tor%20Browser%2014.0a7%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Bluesky](https://bsky.app/intent/compose?text=Tor%20Browser%2014.0a7%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.%0Ahttps%3A//blog.torproject.org/new-alpha-release-tor-browser-140a7/)

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