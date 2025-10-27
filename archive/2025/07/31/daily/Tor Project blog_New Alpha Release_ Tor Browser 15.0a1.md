---
title: New Alpha Release: Tor Browser 15.0a1
url: https://blog.torproject.org/new-alpha-release-tor-browser-150a1/
source: Tor Project blog
date: 2025-07-31
fetch_date: 2025-10-07T00:03:25.190614
---

# New Alpha Release: Tor Browser 15.0a1

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 15.0a1

by [morgan](/author/morgan)
| July 30, 2025

![](/new-alpha-release-tor-browser-150a1/lead.png)

Tor Browser 15.0a1 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/15.0a1/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

## It's ESR transition season again!

Once again, it is the time of year where the Applications Team (mostly) de-prioritises feature-work and instead focuses on updating Tor Browser and Tor Browser for Android to the latest and greatest version of Firefox ESR ([Extended Support Release](https://support.mozilla.org/en-US/kb/firefox-esr-release-cycle)) . For a general overview of this process, please do see our [14.0a1 release post from last year](https://blog.torproject.org/new-alpha-release-tor-browser-140a1/).

Fortunately, we're in a much better place than we were this time last year. Following lessons learned from last year, we have again performed and reviewed iterative rebases from Firefox 128 up to Firefox 140 and finally onto Firefox ESR 140. Tor Browser 15.0a1 is available for all our supported platforms (Windows, macOS, Linux, and Android) unlike last year where we had to delay our Android release.

We have also completed our annual Bugzilla Triage and have flagged for further review myriad issues resolved upstream by Mozilla over the past year. These are issues which may have privacy or security implications if they were to be shipped in Tor Browser, or they may simply be somehow interesting to us and warrant further attention. The bulk of the remaining work for us this release cycle is to review the remainder of these issues, develop any necessary patches needed to fix any found problems, and to fix any other bugs we find.

## Challenges and Triumphs

### Android build-reproducibility Issues

Every major rebase typically introduces a few difficulties around build-reproducibility. This major rebase was no exception and we had to resolve some problems with our Tor Browser Android build-system. For now the solution seems to be to disable compiler optimisations for the affected modules. You can read more about this in [tor-browser-build#41495](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41495).

### Android APKs too big

The Google Play Store has a strict size limit of about 100 megabytes for Android applications. Left to its own devices, software also seems to have a tendency to grow, so we have to do some digging and carve out some space to hit our size budget. Fortunately, this time around it was a relatively simple matter of modifying some compiler flags. You can read more about this in [tor-browser-build#41500](http://gitlab.torproject.org/tpo/applications/tor-browser-build/-/work_items/41500).

### Upstream source migrations

Historically, Mozilla has used Mercurial internally for its source control and then mirrored this repository to a GitHub project called [gecko-dev](https://github.com/mozilla/gecko-dev). Mozilla decided [recently](https://groups.google.com/a/mozilla.org/g/firefox-dev/c/l61EZcU4i64/m/mgGSyBbEBgAJ) to change this mirroring to a GitHub project called [firefox](https://github.com/mozilla-firefox/firefox). Unfortunately, these two git repositories share no common history which means our own Tor Browser forks nearly doubled in size which has caused some headaches for both our developers (who have had to deal with downloading/uploading gigabytes of commit history when pulling/pushing branches) and our system administrators (who have had to handle this unplanned scaling). One nice side-effect of all of this at least is that we no longer have to tag Firefox commits ourselves. You can read more about this in [tpo/tpa/team#42129](https://gitlab.torproject.org/tpo/tpa/team/-/issues/42129).

## Current Status

We have:

* rebased Tor Browser and Tor Browser for Android to Firefox ESR 140 from Firefox ESR 128
* updated the build systems with the latest dependencies and fixed a few reproducibility issues
* triaged all of the upstream changes from the past year and flagged over 170 issues for further review
* resolved 17 of these triaged issue

For the remainder of this release cycle, we will be focusing on auditing these issues and fixing bugs until the 15.0 alpha series is ready to become Tor Browser Stable 15.0.

## Known Issues

### Source Archive Reproducibility

We publish a source archive with each our releases (e.g. `src-firefox-tor-browser-140.1.0esr-15.0-1-build3.tar.xz`). These contain all of the code and assets used to build the browser portion of Tor Browser (i.e. excluding tor and the pluggable-transports). One would think that such data should be trivially deterministic, but this is sometimes not the case. For example, [during the Tor Browser 13.0 release cycle](https://blog.torproject.org/new-alpha-release-tor-browser-130a4/), we had a similar issue with generated headers on Windows.

This time around, the `git archive` process used to generate these source archives is generating a different `.git-archive.txt` metadata file in one of the browser's vendored dependencies. This file has no effect on the build process (which we can concretely know since the generated binaries users actually download and run are identical), so this non-determinism did not block this release. This issue is being tracked in [tor-browser-build#41528](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41528).

## Send us your feedback

Now is a great time to [become an alpha tester](https://blog.torproject.org/vounteer-as-an-alpha-tester/)! If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The full changelog since [Tor Browser 14.5a6](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) is:

* All Platforms
  + Updated NoScript to 13.0.8
  + Updated OpenSSL to 3.5.1
  + [Bug tor-browser#43397](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43397): Click to play should override "Any capability blocked in the top document must be blocked in its subdocuments too"
  + [Bug tor-browser#43772](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43772): Do not use official branding for BB/TB/MB
  + [Bug tor-browser#43783](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43783): Tighten up the SecurityLevel module to enforce new UX flow
  + [Bug tor-browser#43784](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43784): Get confirmation from NoScript that settings are applied
  + [Bug tor-browser#43853](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43853): DomainFrontedRequests: setData is no longer a function
  + [Bug tor-browser#43880](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43880): Update moat's domain front url
  + [Bug tor-browser#43993](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43993): Backport Security Fixes from Firefox 141
  + [Bug tor-browser#44000](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44000): Rebase Tor Browse Alpha onto 140.1.0esr
  + [Bug tor-browser-build#41502](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41502): Application services build is failing on isNetworkAllowed()
  + [Bug tor-browser-build#41508](https://gitlab.torproject.org/tpo/appl...