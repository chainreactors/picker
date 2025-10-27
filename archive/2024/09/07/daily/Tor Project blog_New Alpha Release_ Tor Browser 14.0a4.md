---
title: New Alpha Release: Tor Browser 14.0a4
url: https://blog.torproject.org/new-alpha-release-tor-browser-140a4/
source: Tor Project blog
date: 2024-09-07
fetch_date: 2025-10-06T18:30:45.354351
---

# New Alpha Release: Tor Browser 14.0a4

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 14.0a4

by [morgan](/author/morgan)
| September 6, 2024

![](/new-alpha-release-tor-browser-140a4/lead.png)

Tor Browser 14.0a4 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/14.0a4/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

We would like to thank the folowing community members for their contributions this release:

* NoisyCoil for their fixes for [tor-browser#42730](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42730), [tor-browser#43114](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43114), and [tor-browser#43088](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43088)

If you would like to contribute, our contributor guide can be found [here](https://gitlab.torproject.org/tpo/applications/team/-/wikis/Development-Information/Tor-Browser/Contributing-to-Tor-Browser).

## User Agent Spoofing Changes

Historically, Tor Browser has spoofed the browser user agent found in HTTP headers, while not spoofing the user agent returned by the `Navigator.userAgent` property in JavaScript. The logic behind the HTTP header spoofing was to prevent passive tracking of users' operating system by websites (when using the 'Safest' security level) and by malicious exit nodes (or their upstream routers) passively listening in on unencrypted HTTP traffic. We left the JavaScript query intact for the purposes of website compatibility and usability. We also left it enabled because there are already many ways of detecting a user's real operating system when JavaScript is enabled (e.g. via font enumeration).

With Tor Browser 14.0a4, we have introduced the boolean preference `privacy.resistFingerprinting.spoofOsInUserAgentHeader`. When this pref is set to `true` (which is currently the default), Tor Browser will follow the previously described legacy behaviour. However, if you set this preference (accessible in about:config) to `false`, Tor Browser will never spoof the user agent and will report your operating system family (i.e. Windows, macOS, Linux, or Android) when requested. We are considering changing Tor Browser to make this the new default behaviour.

So, *why* are we considering making this change? Basically, asymetrically spoofing the user agent causes website breakage seemingly due to bot-detection scripts. And (in our analysis) it also provides only a negligible amount of benefit to the user in terms of additional linkability (i.e. cross-site tracking, fingerprinting) protections, and only then when JavaScript is disabled. Tor Browser's default HTTPS-Only mode (and much of the web having moved to HTTPS) has also significantly reduced the utility of passively sniffing HTTP traffic for user agents as well.

We would be very curious to hear from users and domain experts as to whether user agent spoofing is providing any other privacy benefits. In the meantime, disabling spoofing is available to users on an opt-in basis. For more information and to join the conversation, please see the Gitlab ticket [tor-browser#42467](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42467).

## Android APK Size Reduction

We have sufficiently reduced our APKs for x86 and x86\_64 releases on Google Play. However, this is at the expense of the conjure pluggable-transport and the (currently unused on Android) GeoIP database. Long-term we will need to find additional savings for feature-complete releases for these platforms.

## Bugzilla Triage and Review

We have 127 remaining upstream Bugzilla issues to review and potentially develop patches for.

This work can be tracked in [this Gitlab query](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/?sort=updated_desc&state=opened&search=Review%20Mozilla&label_name%5B%5D=14.0%20stable&first_page_size=100).

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The full changelog since [Tor Browser 14.0a3](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) is:

* All Platforms
  + Updated NoScript to 11.4.35
  + Updated OpenSSL to 3.0.15
  + [Bug tor-browser#30862](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/30862): 10ms time precision via EXSLT date-time function
  + [Bug tor-browser#42601](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42601): Check Bug 1894779: Allow font-face urls to be resource:// urls and relax CORS for resource:// URLs
  + [Bug tor-browser#42684](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42684): Disable network prefetch
  + [Bug tor-browser#42685](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42685): compat: ESR128: enable textmetrics
  + [Bug tor-browser#42686](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42686): Backport Mozilla 1885101
  + [Bug tor-browser#42730](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42730): Make RemoteSettings use only local dumps
  + [Bug tor-browser#42867](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42867): Disable contentRelevancy component
  + [Bug tor-browser#43100](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43100): Backport security fixes from Firefox 130
* Windows + macOS + Linux
  + [Bug tor-browser#40147](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40147): Re-enable Picture-in-Picture mode
  + [Bug tor-browser#41309](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41309): Re-enable screenshots component
  + [Bug tor-browser#41835](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41835): Review default search engine options
  + [Bug tor-browser#42617](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42617): Restore the HTML form on DDG when using safest in 128
  + [Bug tor-browser#42630](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42630): Review LaterRun in 128
  + [Bug tor-browser#42640](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42640): Disable Firefox Flame button due to unknown interactions with New Identity
  + [Bug tor-browser#42735](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42735): Disable recent search suggestions
  + [Bug tor-browser#42737](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42737): Drop the hash check on updates
  + [Bug tor-browser#42743](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42743): Invalid onion sites are shown as secure in the page info window
  + [Bug tor-browser#42744](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42744): Light theme override for "about:tor" is inherited by chrome error pages.
  + [Bug tor-browser#42745](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42745): Remove some residuals from update scripts
  + [Bug tor-browser#42764](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42764): Unconditionally disable find-bar transition animation
  + [Bug tor-browser#42803](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42803): Lost focus styling for built-in bridges radio options
  + [Bug tor-browser#42891](https://gitlab.torproject.org/tpo/a...