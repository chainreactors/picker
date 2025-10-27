---
title: New Release: Tor Browser 11.5.5 (Android, Windows, macOS, Linux)
url: https://blog.torproject.org/new-release-tor-browser-1155/
source: Tor Project blog
date: 2022-10-26
fetch_date: 2025-10-03T20:57:11.315577
---

# New Release: Tor Browser 11.5.5 (Android, Windows, macOS, Linux)

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tor Browser 11.5.5 (Android, Windows, macOS, Linux)

by [richard](/author/richard)
| October 25, 2022

![](/new-release-tor-browser-1155/lead.png)

Tor Browser 11.5.5 is now available from the [Tor Browser download page](https://www.torproject.org/download/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/11.5.5/).

Tor Browser 11.5.5 backports the following security updates from Firefox ESR 102.4 to to Firefox ESR 91.13 on Windows, macOS and Linux:

* [CVE-2022-40674: libexpat before 2.4.9 has a use-after-free in the doContent function in xmlparse.c](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40674)
* [CVE-2022-42927: Same-origin policy violation could have leaked cross-origin URLs](https://www.mozilla.org/en-US/security/advisories/mfsa2022-45/#CVE-2022-42927)
* [CVE-2022-42928: Memory Corruption in JS Engine](https://www.mozilla.org/en-US/security/advisories/mfsa2022-45/#CVE-2022-42928)
* [CVE-2022-42929: Denial of Service via window.print](https://www.mozilla.org/en-US/security/advisories/mfsa2022-45/#CVE-2022-42929)
* [CVE-2022-42932: Memory safety bugs fixed in Firefox 106 and Firefox ESR 102.4](https://www.mozilla.org/en-US/security/advisories/mfsa2022-45/#CVE-2022-42932)

Tor Browser 11.5.5 updates GeckoView on Android to 102.4.0esr and includes [important security updates](https://www.mozilla.org/en-US/security/advisories/mfsa2022-45/). There were no Android-specific security updates to backport from the Firefox 106 release.

The full changelog since [Tor Browser 11.5.4](https://gitweb.torproject.org/builders/tor-browser-build.git/plain/projects/tor-browser/Bundle-Data/Docs/ChangeLog.txt?h=maint-11.5) is:

* All Platforms
  + Update Translations
  + [Bug tor-browser-build#40649](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40649): Update meek default bridge
  + [Bug tor-browser-build#40654](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40654): Enable uTLS and use the full bridge line for snowflake
* Windows + macOS + Linux
  + Update Manual
  + [Bug tor-browser#40465](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40465): Onion Authentication fails when connecting to a subdomain
  + [Bug tor-browser#41355](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41355): Amends to YEC 2022 Takeover Desktop Stable 11.5.5
  + [Bug tor-browser#41359](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41359): Backport ESR 102.4 security fixes to 91.13-based Tor Browser
  + [Bug tor-browser#41364](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41364): Continued amends to YEC 2022 Takeover Desktop Stable 11.5.5
* Android
  + [Bug tor-browser-build#40650](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40650): Rebase geckoview-102.3.0esr-11.5-1 to ESR 102.4
  + [Bug tor-browser#41360](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41360): Backport Android-specific Firefox 106 to ESR 102.4-based Tor Browser
  + [Bug tor-browser#41365](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41365): Amends to YEC 2022 Takeover on Android
* Build
  + Windows + macOS + Linux
    - Update Go to 1.18.7
    - [Bug tor-browser-build#40464](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40464): go 1.18 fails to build on macOS

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-release-tor-browser-1155/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-release-tor-browser-1155/&text=Tor%20Browser%2011.5.5%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-release-tor-browser-1155/&text=Tor%20Browser%2011.5.5%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Bluesky](https://bsky.app/intent/compose?text=Tor%20Browser%2011.5.5%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.%0Ahttps%3A//blog.torproject.org/new-release-tor-browser-1155/)

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