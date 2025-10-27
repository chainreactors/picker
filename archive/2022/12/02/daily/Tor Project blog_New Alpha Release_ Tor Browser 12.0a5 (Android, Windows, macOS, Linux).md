---
title: New Alpha Release: Tor Browser 12.0a5 (Android, Windows, macOS, Linux)
url: https://blog.torproject.org/new-alpha-release-tor-browser-120a5/
source: Tor Project blog
date: 2022-12-02
fetch_date: 2025-10-04T00:20:47.868819
---

# New Alpha Release: Tor Browser 12.0a5 (Android, Windows, macOS, Linux)

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 12.0a5 (Android, Windows, macOS, Linux)

by [richard](/author/richard)
| December 1, 2022

![](/new-alpha-release-tor-browser-120a5/lead.png)

Tor Browser 12.0a5 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/12.0a5/).

Tor Browser 12.0a5 updates Firefox on Android, Windows, macOS, and Linux to 102.5.0esr.

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/mfsa2022-48/) to Firefox and GeckoView.

Tor Browser 12.0a5 backports the following security updates from Firefox 107 to Firefox ESR 102.5 on Android:

* [CVE-2022-45413: SameSite=Strict cookies could have been sent cross-site via intent URLs](https://www.mozilla.org/en-US/security/advisories/mfsa2022-47/#CVE-2022-45413)

## Major Changes since 11.5

This is the final planned alpha release before 12.0 stable. We have made a lot of changes over the past several months both large and small, and would like to encourage alpha users to test the following features and [report any issues you discover](https://community.torproject.org/user-research/become-tester/).

### Universal macOS packages

This is the first universal package release of Tor Browser for macOS. Now Tor Browser should run natively for macOS users, regardless of whether they are running on older x86\_64 devices or on newer Apple M1 aarch64 devices.

**What to test:** Users with existing x86\_64 macOS installs should receive an automatic update to the new universal package without any loss of functionality. The universal dmg downloaded from the Tor Project website should continue to work for macOS users on both x86\_64 and aarch64 platforms. We would also appreciate if macOS users attempted a build-to-build upgrade from an [older version of Tor Browser Alpha](https://archive.torproject.org/tor-package-archive/torbrowser/12.0a3/) to help us validate this update path.

Once installed, macOS users using aarch64-based Macs (i.e. those with Apple Silicon) can verify whether Tor Browser is running natively by following these steps:

1. Open the Activity Monitor application.
2. Search for "Tor Browser" within the CPU tab.
3. Should Tor Browser read "Apple" under the Kind column, you are successfully running the native Apple Silicon build.

### Multi-locale bundles (Desktop)

As of Tor Browser 12.0a4, all supported languages are now included in a single bundle, and can be changed without requiring additional downloads via the Language menu in General settings on the about:preferences page.

**What to test:** Tor Browser Alpha should default to your system language on first launch if it matches [a language we support](https://support.torproject.org/tbb/tbb-37/). Alpha testers are also encouraged to test changing language within about:preferences#general, and to report any new bugs with localization in general (in particular instances of 'Firefox' appearing instead of 'Tor Browser' or other similar branding issues).

We would also appreciate if users on all our Desktop platforms attempted a build-to-build upgrade from an [older version of Tor Browser Alpha](https://archive.torproject.org/tor-package-archive/torbrowser/12.0a3/) to help us validate the update path.

### Unified EspaÃ±ol locale (Desktop and Android)

Previous versions of Tor Browser Alpha were available in both "es" and "es-AR" (EspaÃ±ol Argentina) locales. As of Tor Browser, 12.0a4 these have been unified into a single Spanish locale instead.

**What to test:** Alpha testers who use the "es-AR" locale should be automatically switched to "es-ES" after updating.

### New supported locales (Ukranian and Albanian)

We have added support for both Ukranian and Albanian languages.

**What to test:** Alpha testers who use the "uk" and "sq" locales should try them on both Desktop (using the language picker in about:preferences#general) and Android (using the options in Settings > Language).

### tor-launcher migration (Desktop)

Parts of the code that power tor-launcher â which starts tor within Tor Browser â have been refactored. Although this work doesn't include any changes to the user experience, those who run non-standard Tor Browser setups are encouraged to test 12.0a5 on their systems.

**What to test:** Alpha testers who run non-standard Tor Browser setups (including, but not limited to, those who use system tor in conjunction with Tor Browser and those with specific network and bridge settings) should test starting and connecting to Tor, and report any unexpected error messages they encounter. All of the previously supported environment variables should still behave the same way as in the stable series.

### Onion Auth fixes (Desktop)

Tor Browser 12.0a4 included two fixes to Onion Service client authorization:

1. A fix to the auth window itself, which was broken in Alpha due to a regression caused by the esr102 transition: [tor-browser#41344](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41344)
2. Another fix to a longstanding issue with Onion Auth failing on subdomains, which has also been backported to 11.5.5: [tor-browser#40465](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40465)

**What to test:** Accessing client authorized Onion Services on both top-level and subdomains.

### Always prioritize .onion sites (Android)

Android users can now enable automatic Onion-Location redirects by switching "Prioritize .onion sites" within Privacy and Security settings. However, we have not yet implemented the url bar UI which we have in Tor Browser for Desktop.

**What to test:** Enable "Prioritize .onion sites" within settings, visit a website that supports Onion-Location, and verify that you were redirected to the website's .onion address.

The full changelog since [Tor Browser 12.0a4](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs/ChangeLog.txt) is:

* All Platforms
  + Update Translations
  + Update OpenSSL to 1.1.1s
  + Update NoScript to 11.4.13
  + Update tor to 0.4.7.11
  + Update zlib to 1.2.13
  + [Bug tor-browser#17228](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/17228): Consideration for disabling/trimming referrers within TBB
  + [Bug tor-browser#27258](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/27258): font whitelist means we don't have to set gfx.downloadable\_fonts.fallback\_delay
  + [Bug tor-browser#40183](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40183): Consider disabling TLS ciphersuites containing SHA-1
  + [Bug tor-browser-build#40622](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40622): Update obfs4proxy to 0.0.14 in Tor Browser
  + [Bug tor-browser-build#40674](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40674): Add Secondary Snowflake Bridge
  + [Bug tor-browser#40783](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40783): Review 000-tor-browser.js and 001-base-profile.js for 102
  + [Bug tor-browser#41406](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41406): Do not define `--without-wasm-sandboxed-libraries` if `WASI_SYSROOT` is defined
  + [Bug tor-browser#41420](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41420): Remove brand.dtd customization on nightly
  + [Bug tor-browser#41457](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41457): Remove more Mozilla permissions
  + [Bug tor-browser#41460](https://gitlab.torproject.org/tpo/application...