---
title: New Alpha Release: Tor Browser 16.0a10
url: https://blog.torproject.org/new-alpha-release-tor-browser-160a10/
source: Tor Project blog
date: 2026-08-27
fetch_date: 2026-08-28T13:38:09.647265
---

# New Alpha Release: Tor Browser 16.0a10

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 16.0a10

by [morgan](/author/morgan)
| August 27, 2026

![](/new-alpha-release-tor-browser-160a10/lead.png)

Tor Browser 16.0a10 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/16.0a10/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

â ï¸ **Reminder**: The Tor Browser Alpha release-channel is for [testing only](https://community.torproject.org/user-research/become-tester/). As such, Tor Browser Alpha is not intended for general use because it is more likely to include bugs affecting usability, security, and privacy.

Moreover, Tor Browser Alphas are now based on Firefox's betas. Please read more about this important change in the [Future of Tor Browser Alpha](https://blog.torproject.org/future-of-tor-browser-alpha/) blog post.

If you are an at-risk user, require strong anonymity, or just want a reliably-working browser, please stick with the [stable release channel](https://www.torproject.org/download/).

## â¨ New Features which need attention!

### ð Updated Built-in manual on Desktop Tor Browser

The Tor Project's old support page and content has been updated. Starting with Tor Browser 16.0a10, this updated design and content is now baked into the browser and replaces the legacy manual. You can access the manual directly by navigating to `about:manual` in the URL bar or by clicking on the various "Learn more" links found in the browser's UI.

### âï¸ Settings Redesign now enabled by default

With Tor Browser 16.0a10, we have enabled the new `about:preferences` designs from Mozilla by default. Our additional settings (connectivity, letterboxing, security level, etc) should now all be migrated over and using the new design language. Please file an issue if you find any regressions!

### ðª Generic Window Titles

On most (all?) desktop operating systems, applications have the ability to programmatically set and update the title of their windows.
Normally, this is very useful as it allows the names of your applications to appear in the desktop UI in the title bar or as entries in application switchers (e.g. when you alt-tab between applications).

Historically, web browsers have dynamically updated their application's window title to the contents of the current web page's `<title>` element.
For example, the window name for the browser window you are currently using is very likely some variant of `New Alpha Release: Tor Browser 16.0a10 | The Tor Project â Tor Browser`.
If you were to navigate away from this page (please don't), the title would be updated to some variant of that page's `<title>` element contents.

While this process provides convenient usability to end-users, these title changes are generally detectable and readable by 3rd party applications or the operating system itself. This is typically not a privileged action, meaning software does not typically require special permissions to do this. These same APIs which allow programs to enumerate open windows also allow them to record browsing history using window title changes as a side-channel.

To counteract this, we've developed (and [upstreamed](https://bugzilla.mozilla.org/show_bug.cgi?id=1849186)) an opt-in feature disabling these window title changes and instead replacing them with just the the name of the browser. You can try this feature out by going to `about:preferences`, clicking on `Privacy and security` in the navigation panel, clicking on `Advanced settings` within the `Connection and software security` group, and checking `Use generic window titles` in the `Protections from third-party applications` group. With this setting enabled, all Tor Browser window titles should now simply read `Tor Browser Alpha`.

For any vanilla Firefox users out there, you can enable this feature by going to `about:config` and setting the `privacy.exposeContentTitleInWindow` (for normal-browsing windows) and `privacy.exposeContentTitleInWindow.pbm` (for private-browsing windows) boolean options to `false`.

We had hoped to enable this feature by default in the 16.0 series, but it is a bit late in the release cycle to push out such a feature with potentially unseen side-effects (e.g. causing breakage with a11y software, specific desktop environments, or other custom configurations) without user testing.
Please give this feature a go (especially if your desktop environment is non-standard) and report back any issues or incompatibilities you find.

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The [full changelog](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) since Tor Browser 16.0a9 is:

* All Platforms
  + Updated NoScript to 13.6.31.90301984
  + Updated OpenSSL to 3.5.8
  + [Bug tor-browser#44257](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44257): Disable locale-based font rules as a defense-in-depth
  + [Bug tor-browser#45161](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45161): Drop TorProviderBuilder.firstWindowLoaded
  + [Bug tor-browser#45205](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45205): Rebase Tor Browser onto 153.1.0esr
  + [Bug tor-browser#45219](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45219): Backport Security Fixes from Firefox 154
* Windows + macOS + Linux
  + Updated Firefox to 153.1.0esr
  + [Bug tor-browser#43570](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43570): Report errors in about:torconnect when tor daemon crashes (Desktop)
  + [Bug tor-browser#43640](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43640): Poor screen reader experience when opening preferences and scrolling to element
  + [Bug tor-browser#43939](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43939): Update Bridge settings when connection failed
  + [Bug tor-browser#44247](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44247): Adapt Tor Browser manual to use the new support pages
  + [Bug tor-browser#44511](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44511): Make sure new search suggest features are disabled for 16.0
  + [Bug tor-browser#44629](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44629): Add a search suggestion warning in the settings
  + [Bug tor-browser#44699](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44699): Amend commit message for "BB 43322: Customize the font visibility lists"
  + [Bug tor-browser#44802](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44802): Hide the "safe browsing" settings
  + [Bug tor-browser#44830](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44830): Migrate our home page adjustments to the settings config
  + [Bug tor-browser#44831](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44831): Misleading banner in "Search engine suggestions" settings
  + [Bug tor-browser#44855](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44855): Use `ariaNotify` for bridge updates
  + [Bug tor-browser#44959](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44959): Integrate the new Tor Browser manual into Tor Browser
  + [Bug tor-browser#44998](https://gitlab.torproject.org/...