---
title: New Alpha Release: Tor Browser 16.0a9
url: https://blog.torproject.org/new-alpha-release-tor-browser-160a9/
source: Tor Project blog
date: 2026-07-23
fetch_date: 2026-07-24T05:05:40.824764
---

# New Alpha Release: Tor Browser 16.0a9

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 16.0a9

by [morgan](/author/morgan)
| July 23, 2026

![](/new-alpha-release-tor-browser-160a9/lead.png)

Tor Browser 16.0a9 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/16.0a9/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

â ï¸ **Reminder**: The Tor Browser Alpha release-channel is for [testing only](https://community.torproject.org/user-research/become-tester/). As such, Tor Browser Alpha is not intended for general use because it is more likely to include bugs affecting usability, security, and privacy.

Moreover, Tor Browser Alphas are now based on Firefox's betas. Please read more about this important change in the [Future of Tor Browser Alpha](https://blog.torproject.org/future-of-tor-browser-alpha/) blog post.

If you are an at-risk user, require strong anonymity, or just want a reliably-working browser, please stick with the [stable release channel](https://www.torproject.org/download/).

## It's ESR transition season again!

Well actually, it has been ESR transition season throughout this entire release cycle! As described in the aforementioned [Future of Tor Browser Alpha](https://blog.torproject.org/future-of-tor-browser-alpha/) blog post, we have been incrementally rebasing our Alpha channel on Firefox betas since December of last year. As a result, we now stand before you with Tor Browser 16.0a9 which is based on Firefox ESR 153.

We will continue rebasing Tor Browser 17.0 Alpha branches on Firefox betas throughout the remainder of the Tor Browser 16.0 release cycle. However, new feature-work for now must be put on hold for a few reasons:

* We must focus our attention on resolving our Bugzilla Audit issues to ensure the features we have inherited from upstream comply Tor Browser's [threat model](https://gitlab.torproject.org/tpo/applications/wiki/-/wikis/Design-Documents/Tor-Browser-Design-Doc) and to patch any changes which do not.
* Feature work targeting 16.0 stable would need to be cherry-pick'd onto our 17.0 Alpha branches to ensure we don't lose any work. The more invasive a feature patch is, the harder it will be to port to newer versions. This would also be a potentially error-prone process and there is some risk we would lose patches along the way.
* We need to finish stabilizing as soon as possible as we have hard external deadlines which cannot be moved: the end-of-life of Firefox ESR 140 on October 13th and the Google Play Minimum Target API Level requirement on November 1st

## Challenges and Triumphs

### ð Sharing the Load

Rebasing the hundreds of Tor Browser patches onto newer versions of Firefox is a challenging task. It is like maintaining the structural stability of sand-castle at high-tide with the waves crashing all around you.

As such, it quickly become clear early in this new process that we would need to do something if we wanted to avoid burning out the few developers typically involved in this work. To mitigate this, we shared the knowledge internally and spread the work out across all eight members of the team. This way, each developer was only responsible for at most two or three rebases throughout the entire release cycle.

### ð¨ UI Code Churn

Over the past year, Firefox has developed and integrated two major changes to the UI in Firefox: a [redesign](https://blog.mozilla.org/en/firefox/firefox-settings/) of about:preferences in Firefox Desktop and a [migration](https://www.androidsage.com/2026/02/24/firefox-browser-updated-with-new-ui-and-material-3-expressive-hint/) from Material 2 to Material 3 in Firefox Android.

Adapting to these types of changes to the frontend are typically rather time-consuming for us, as many (if not the majority) of our patches modify Firefox's UI in some way. For example, we have an entire preferences page on Tor Browser desktop dedicated to configuring how the browser connects to the Tor Network. On Android, we similarly have various additions to the menus, configuration options, and custom UI.

Whenever Mozilla modifies their design systems and Firefox's user interface, we necessarily have to adapt our own custom additions to match. Otherwise, our Tor Browser-specific UI elements would look completely out of place and potentially confuse users (as well as simply looking unprofessional). Therefore, each of these upstream changes requires collaboration with the Tor Project's UX team to update our features' designs and of course development time to implement.

In addition to the time-cost associated with the extra engineering and UX collaboration, very often our old patches simply do not apply cleanly due to the amount of code which has changed. For example, the about:preferences changes on Firefox Desktop are essentially a complete re-write which means we also have to completely re-write our own settings changes without regressing in functionality.

On the plus side, one benefit of our new processes is that we have been able to spread out this work over the entire release cycle. In the past way of doing things, we would have discovered all UX elements which needed to be fixed, updated our designs, and re-implemented in the course of a few months during the old ESR transition season. Under this new way of working, we have been able to incrementally fix things throughout the development cycle.

The benefits of working this way does not just apply to UX of course. It is much easier to find regressions across the entire stack when rebasing between one major Firefox version at a time instead of across 12 or 13. It is also *much* easier for developers to fix individual regressions one at a time compared to diagnosing, disentangling, and fixing multiple bugs concurrently (divide et impera!).

### âï¸ Pending Google Target API Level Requirements

Every year, Google requires new Android app releases to target an updated minimum API level. This means, we would not be able to upload new versions of Tor Browser Stable past a certain date (usually August 1st with an extension to November 1st typically possible) without first updating the app to support the new minimum target API level. Fortunately, we inherit most of the required changes from Mozilla when rebasing to the next major ESR.

However, this requirement does impose a hard deadline for the absolute latest we can responsibly stabilize Tor Browser Alpha and promote it to Stable. We've been fortunate in the past few years to make the deadline with a few days to spare (October 28th for Tor Browser 15, October 22nd for Tor Browser 14, etc). Given how far ahead of the curve we are this year, we are hoping to release about a month earlier in September (fingers crossed!).

### ð¤ Android APKs too big

The Google Play Store has a strict size limit of about 100 megabytes for Android applications. New functionality added to Firefox Android over the past year means a larger application which results in new headaches for Tor Browser developers. This release cycle was no exception to this rule and we have had to get *creative* with our size reductions.

In the past, we have been able reduce our package size though various methods including:

* [Using custom size-reducing compiler flags](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/work_items/41500)
* [Compiling multiple pluggable-transports into a single unified binary to de-duplicate shared dependencies](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/work_items/-41407)
* [Removing unused Firefox assets from the build](http...