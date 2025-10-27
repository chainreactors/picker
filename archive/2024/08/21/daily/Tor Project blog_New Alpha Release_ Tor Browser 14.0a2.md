---
title: New Alpha Release: Tor Browser 14.0a2
url: https://blog.torproject.org/new-alpha-release-tor-browser-140a2/
source: Tor Project blog
date: 2024-08-21
fetch_date: 2025-10-06T18:18:30.792657
---

# New Alpha Release: Tor Browser 14.0a2

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 14.0a2

by [morgan](/author/morgan)
| August 20, 2024

![](/new-alpha-release-tor-browser-140a2/lead.png)

Tor Browser 14.0a2 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/14.0a2/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

## ESR Progress

As discussed in our [previous blog post](https://blog.torproject.org/new-alpha-release-tor-browser-140a1/), we are hard at work updating Tor Browser to the Firefox ESR-128. New in this version we have our first updated Tor Browser Android build, we have completed our Bugzilla issue triage and code-audits, reviewed various upstream changes discovered from this work, and fixed various issues.

### Android

#### Massive Rebase

Tor Browser Android always requiers a bit more extra attention each year to update. One of the reasons for this is that Mozilla has altered the project layout non-trivally on us with each of the major updates.

Firefox Android (and therefore Tor Browser Android) has historically consisted of several separate components spread across multiple git repos: [application-services](https://github.com/mozilla/application-services), [android-components](https://github.com/mozilla-mobile/android-components), [fenix](https://github.com/mozilla-mobile/fenix), and [GeckoView](https://github.com/mozilla/gecko-dev/) (GeckoView is the same codebase used to build desktop Firefox).

Last summer we had to update our patches as upstream's android-components and fenix had been merged into a single [firefox-android](https://github.com/mozilla-mobile/firefox-android/) repo which meant we had to merge all of the patches we had applied to these projects into our own firefox-android fork, on top of *also* updating our patches to work with all the other changes made during the year.

This summer we have had to do a similar thing once more, as Mozilla merged firefox-android into GeckoView in Firefox 126. So again we had to move and update all of our Tor Browser Android patches.

All of this work requires a lot of attention to detail, and has the annoying property that the work cannot be done incrementally. Someone basically has to go do all of this work locally while our users and the rest of the team patiently wait for the end result. That can be a stressful spot to be in, and the fact that we have to do this is outside our control is also rather frustrating.

Fortunately, there is a silver lining. After Tor Browser 14.0 stabilises, almost all of our the code which makes Tor Browser different from Firefox will be in the same repo. This will greatly simplify both maintenance and new feature development because changes which may require updates to multiple components, can now be reviewed in a single merge-request instead of being scattered across multiple repos. It will also make our patchset easier to reason about for this same reason. A single repo also makes it much easier for new developers to become familiar with the codebase since all the source lives in just one place!

The other silver lining from all of this is that we *shouldn't* need to do this again as there are no more components to migrate! Well, almost. The application-services component *could* be next but we have long-term [plans](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42669).

#### Reproducibility Issues

To help protect against various possible threats (release infrastructure compromise, toolchain attacks, rogue developers, etc) we have hard requirement that our releases are [reproducible](https://en.wikipedia.org/wiki/Reproducible_builds). We build our releases multiple times on multiple different machines on different networks and ensure the build outputs match byte-per-byte. Currently we are typically building on 3 different machines:

* a Tor Project build servers
* a Tor Browser developer PC
* a Mullvad build server

If all three machines (which are controlled and adminstered by different parties) build the exact same artifacts, then we sign and publish our builds. You can see this process in action in our 14.0a2 release-prep ticket on our Gitlab:

* <https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41186#note_3060617>

The kind of cool thing about this process is that users don't have to just trust our binaries, since they can be easily(ish) [built locally](https://gitlab.torproject.org/tpo/applications/wiki/-/wikis/Development-Information/Tor-Browser/Building). They can also make our builds and verify the build system does what we claim it does.

The *other* kind of cool thing about this setup is that we don't *need* to be super confident about the integrity of any one individual build machine. If any of the aforementioned machines were somehow compromised and inserting unknown code into our releases, it would be discovered immediately after building since the outputs would be different.

Another layer of assurance we have is that none of the the Tor Browser developers responsible for releases even have administrative access to the Mullvad build-server. We can only request a signed-tag be built and then it tells us the outputs.

As we've come to expect with a year's worth of toolchain updates, we uncovered some reproducibility [problems](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41211) in our Android apk generation. Fortunately, the problem was a well-understood one in the build-reproducibility space.

To summarise, groups of objects are often stored in some unordered set, and then enumerated to a list with a particular order. Depending on *how* these objects were originally stored and the method by which they are enumerated, one can get a differently ordered list (and therefore different build outputs) from run to run.

Fortunately, the solution is generally pretty simple: either sort the list afterward or change the underlying data-structure to be one which enumerates its contents deterministically (e.g. convert a `HashSet<T>` to a `BTreeSet<T>`).

### Bugzilla Triage and Review

We have triaged *all* of upstream Bugzilla issues closed by Mozilla in there releases from Firefox 116 through 128. From this massive list of literally *thousands* of issues, we have identified 256 particular issues developers need to investigate further. Of these we have investigated and potentially patched 56.

This work can be tracked in [this Gitlab query](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/?sort=updated_desc&state=opened&search=Review%20Mozilla&label_name%5B%5D=14.0%20stable&first_page_size=100).

We have also run out automated code-audit scripts on the entire relevant commit range and identified a handful of commits which should be looked at more closely.

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Known Issues

There are a few known issues which we are aware of.

#### No Tor Browser 14.0a2 for x86 and x86\_64 on Google Play Store

Our alpha release exceeds the Google Play Store's limit on APK size for x86 and x86\_64 devices. This is being tracked here:

* <https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42607>

#### Tor Browser Android crashes when searching DuckDuckGo from the toolbar

This issue will be fixed in the next alpha release. It is being tracked here:

* <https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43037>

## Full changelog

The ful...