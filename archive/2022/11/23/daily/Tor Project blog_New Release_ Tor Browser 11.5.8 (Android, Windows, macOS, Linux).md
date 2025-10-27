---
title: New Release: Tor Browser 11.5.8 (Android, Windows, macOS, Linux)
url: https://blog.torproject.org/new-release-tor-browser-1158/
source: Tor Project blog
date: 2022-11-23
fetch_date: 2025-10-03T23:35:52.993578
---

# New Release: Tor Browser 11.5.8 (Android, Windows, macOS, Linux)

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tor Browser 11.5.8 (Android, Windows, macOS, Linux)

by [richard](/author/richard)
| November 22, 2022

![](/new-release-tor-browser-1158/lead.png)

Tor Browser 11.5.8 is now available from the [Tor Browser download page](https://www.torproject.org/download/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/11.5.8/). This release will not be published on Google Play due to their target [API level requirements](https://developer.android.com/google/play/requirements/target-sdk). Assuming we do not run into any major problems, Tor Browser 11.5.9 will be an Android-only release that fixes this issue.

Tor Browser 11.5.8 backports the following security updates from Firefox ESR 102.5 to Firefox ESR 91.13 on Windows, macOS and Linux:

* [CVE-2022-43680: In libexpat through 2.4.9, there is a use-after free caused by overeager destruction of a shared DTD in XML\_ExternalEntityParserCreate in out-of-memory situations.](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-43680)
* [CVE-2022-45403: Service Workers might have learned size of cross-origin media files](https://www.mozilla.org/en-US/security/advisories/mfsa2022-48/#CVE-2022-45403)
* [CVE-2022-45404: Fullscreen notification bypass](https://www.mozilla.org/en-US/security/advisories/mfsa2022-48/#CVE-2022-45404)
* [CVE-2022-45405: Use-after-free in InputStream implementation](https://www.mozilla.org/en-US/security/advisories/mfsa2022-48/#CVE-2022-45405)
* [CVE-2022-45406: Use-after-free of a JavaScript Realm](https://www.mozilla.org/en-US/security/advisories/mfsa2022-48/#CVE-2022-45406)
* [CVE-2022-45408: Fullscreen notification bypass via windowName](https://www.mozilla.org/en-US/security/advisories/mfsa2022-48/#CVE-2022-45408)
* [CVE-2022-45409: Use-after-free in Garbage Collection](https://www.mozilla.org/en-US/security/advisories/mfsa2022-48/#CVE-2022-45409)
* [CVE-2022-45410: ServiceWorker-intercepted requests bypassed SameSite cookie policy](https://www.mozilla.org/en-US/security/advisories/mfsa2022-48/#CVE-2022-45410)
* [CVE-2022-45411: Cross-Site Tracing was possible via non-standard override headers](https://www.mozilla.org/en-US/security/advisories/mfsa2022-48/#CVE-2022-45411)
* [CVE-2022-45412: Symlinks may resolve to partially uninitialized buffers](https://www.mozilla.org/en-US/security/advisories/mfsa2022-48/#CVE-2022-45412)
* [CVE-2022-45416: Keystroke Side-Channel Leakage](https://www.mozilla.org/en-US/security/advisories/mfsa2022-48/#CVE-2022-45416)
* [CVE-2022-45420: Iframe contents could be rendered outside the iframe](https://www.mozilla.org/en-US/security/advisories/mfsa2022-48/#CVE-2022-45420)
* [CVE-2022-45421: Memory safety bugs fixed in Firefox 107 and Firefox ESR 102.5](https://www.mozilla.org/en-US/security/advisories/mfsa2022-48/#CVE-2022-45421)

Tor Browser 11.5.8 updates GeckoView on Android to Firefox ESR 102.5 and includes [important security updates](https://www.mozilla.org/en-US/security/advisories/mfsa2022-48/). Tor Browser 11.5.8 backports the following security updates from Firefox 107 to Firefox ESR 102.5 on Android:

* [CVE-2022-45413: SameSite=Strict cookies could have been sent cross-site via intent URLs](https://www.mozilla.org/en-US/security/advisories/mfsa2022-47/#CVE-2022-45413)

The full changelog since [Tor Browser 11.5.7](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/maint-11.5/projects/tor-browser/Bundle-Data/Docs/ChangeLog.txt) is:

* All Platforms
  + Update Translations
  + Update OpenSSL to 1.1.1s
  + Update NoScript to 11.4.12
  + Update tor to 0.4.7.11
  + Update zlib to 1.2.13
  + [Bug tor-browser-build#40622](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40622): Update obfs4proxy to 0.0.14 in Tor Browser
* Windows + macOS + Linux
  + [Bug tor-browser#31064](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/31064): Letterboxing is enabled in priviledged contexts too
  + [Bug tor-browser#32411](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/32411): Consider adding about:tor and others to the list of pages that do not need letterboxing
  + [Bug tor-browser#41105](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41105): Tor Does Not Clear CORS Preflight Cache despite creating a "New Identity"
  + [Bug tor-browser#41413](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41413): Backup intl.locale.requested in 11.5.x
  + [Bug tor-browser#41434](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41434): Letterboxing bypass through secondary tab (popup/popunder...)
  + [Bug tor-browser#41456](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41456): Backport ESR 102.5 security fixes to 91.13-based Tor Browser
  + [Bug tor-browser#41460](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41460): Migrate new identity and security level preferences in 11.5.8
  + [Bug tor-browser#41463](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41463): Backport fix for CVE-2022-43680
* Android
  + Update GeckoView to 102.5.0esr
  + [Bug tor-browser#41461](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41461): Backport Android-specific 107-rr security fixes to 102.5-esr based Geckoview
* Build
  + All Platforms
    - Update Go to 1.18.8
    - [Bug tor-browser-build#40658](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40658): Create an anticensorship team keyring
    - [Bug tor-browser-build#40690](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40690): Revert fix for zlib build break

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-release-tor-browser-1158/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-release-tor-browser-1158/&text=Tor%20Browser%2011.5.8%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-release-tor-browser-1158/&text=Tor%20Browser%2011.5.8%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Bluesky](https://bsky.app/intent/compose?text=Tor%20Browser%2011.5.8%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.%0Ahttps%3A//blog.torproject.org/new-release-tor-browser-1158/)

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

We are very excit...