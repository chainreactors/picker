---
title: The Future of Tor Browser Alpha
url: https://blog.torproject.org/future-of-tor-browser-alpha/
source: Tor Project blog
date: 2025-12-01
fetch_date: 2025-12-02T03:19:06.795674
---

# The Future of Tor Browser Alpha

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# The Future of Tor Browser Alpha

by [morgan](/author/morgan)
| December 1, 2025

![](/future-of-tor-browser-alpha/lead.png)

With the recent release of [Tor Browser 15.0](https://blog.torproject.org/new-release-tor-browser-150/), we have come out of yet another ESR-transition season whereby Tor Browser has been updated to the latest version of Firefox Extended Support Release (ESR). Historically, we have spent several months each year on this work. It is a very important and methodical process which ensures Tor Browser remains secure and private through upstream security updates from Mozilla and by testing and updating our own features and customizations. You can find a somewhat detailed overview of this process and why it is so important in our previous [Tor Browser 14.0a1 release blog post](https://blog.torproject.org/new-alpha-release-tor-browser-140a1/).

Starting with Tor Browser 16.0a1, rather than being based on Firefox ESR 140 (as would have been the case in the past), the Tor Browser Alpha release will instead be based on the latest Firefox Rapid Release. The Tor Browser Stable release (starting with 15.0) will remain on the latest Firefox ESR Release. **This change will only affect Tor Browser Alpha users**.

# Release Channels

*NOTE: This is a simplification of the available browser release channels offered both by Mozilla and the Tor Project, but these are by far the most relevant release channels to the majority of users.*

Mozilla has two different release channels for shipping Firefox updates: Rapid Release and Extended Support Release. The basic idea is that the Rapid Release channel receives major features with each new version every four weeks, while the Extended Support Release channel only receives security updates every four weeks while receiving a year's worth of features roughly every 52 weeks (you can read about the differences in [this Mozilla Support article](https://support.mozilla.org/en-US/kb/choosing-firefox-update-channel)).

The Tor Project also has two different release channels for shipping Tor Browser updates: Alpha and Stable. The Alpha channel is where the Tor Browser developers spend most of their time working on new features. To the end-users, this is where most of the visible changes happen throughout the development cycle. The Stable channel typically receives security updates with each release and only occasional new features through targeted backports from the Alpha channel.

Up until now, both of these channels (i.e. Tor Browser Alpha and Stable) have been based on Firefox's Extended Support Release channel. For the next release cycle, we are going to conduct an experiment whereby Tor Browser Stable will continue to be based on Firefox Extended Support Release while Tor Browser Alpha will instead be based on Firefox Rapid Release.

Traditionally, we would now be working on Tor Browser 15.5a1 based on Firefox ESR 140. Instead, we are already working on Tor Browser 16.0a1 and every Alpha from the 16.0aX series will be based on the Firefox Rapid Release channel. Tor Browser 16.0 will stabilize when Firefox 153 is ready next year and, once released, will follow the ESR channel for the remainder of its life-cycle.

# Ramifications for Users and Testers

â ï¸ If you are an at-risk user, concerned about your privacy, or just need a reliably working web-browser, you SHOULD NOT use Tor Browser Alpha and instead stick with [Tor Browser Stable](https://www.torproject.org/download/) â ï¸

If you are an alpha tester running Tor Browser Alpha, you can expect the following changes:

* **Quicker access to new upstream features developed by Mozilla**: Rather than waiting until the next major ESR version for newly shipped features in Firefox, Tor Browser Alpha users will receive these features shortly after they are introduced upstream. This will allow our alpha-testers to evaluate how new upstream features interact with (or break) our privacy and security patches over a much longer development and stabilization period.
* ***Potentially* Less Secure and Private Tor Browser Alpha Releases**: One side-effect of quickly shipping upstream features to users, is that we will also be quickly shipping upstream bugs to users too. These bugs could have security and privacy implications. The upside is that we *should* also get bug reports from users more quickly as well, which will give us more time to develop proper fixes than we would otherwise. Therefore, users should only use Tor Browser Alpha for testing purposes! At-risk users should migrate to and remain on [Tor Browser Stable](https://www.torproject.org/download/).
* **A Less Predictable Release Cadence**: Sometimes the intersection of upstream changes, our build system, and our patches introduce rather difficult problems for us to solve. It is entirely possible resolving such problems may take longer than the available four week window of time between scheduled Rapid Release versions. Therefore, Tor Browser Alpha releases may be delayed relative to Firefox's release schedule. The consequence of this is that Tor Browser Alpha may not receive upstream security updates as promptly as it has in the past.
* **Faster Platform Deprecation**: Because we are following Mozilla directly, we will also be dropping support for platforms in the Alpha release channel sooner than we would have in the past. Previously, Tor Browser Alpha's minimum supported platforms would follow Firefox ESR, which would change on a yearly basis after the ESR Transition. In the general, Tor Browser Alpha will drop support for legacy platforms at the same time as Firefox Rapid Release. Specifically, the following platforms will no longer be supported by Tor Browser Alpha starting with 16.0a1:

  + **x86 Linux and Android**: As described in our [Tor Browser 15.0 blog post](https://blog.torproject.org/new-release-tor-browser-150/), upstream has dropped support for Linux and Android running on 32-bit x86 processors. As such, we will not be releasing builds for these platforms in the Tor Browser Alpha 16.0 series.
  + **Android older than Android 8.0**: Also described in our [Tor Browser 15.0 blog post](https://blog.torproject.org/new-release-tor-browser-150/), upstream has dropped support for Android versions 5.0, 6.0, and 7.0. This means to upgrade to the Tor Browser Alpha 16.0 series you will need a mobile device running at lest Android 8.0.

If you are an end-user running Tor Browser Stable, you can expect the following changes:

* **One major feature release per year**: Previously, we have had two feature releases per year: one in Q2 and one in late Q3. With this new development model, we expect to have only *one* major feature release per year. Therefore, with Tor Browser Stable 15.0 just released, users can expect Tor Browser Stable 16.0 (based on Firefox ESR 153) to be released about halfway through Q3 of 2026 (i.e. there will not be a Tor Browser 15.5).

# Developer Rationale

So why are we changing things? We believe changing our development model in this way will allow us to be both more effective at developing and maintaining Tor Browser while also reducing contributor stress.

For the past several years we have *tried* to divide the annual Tor Browser development cycle into two phases: a six month feature phase and a six month ESR transition phase. During the feature phase, we would work on new developments to be shipped during Q2 in the .5 release. During the ESR transition phase, we would work almost exclusively on ESR transition related work to be shipped during late Q3/early Q4 in the .0 release.

This division of the year into two distinct phases introduces problems:

* **Cascading Delays**: If something is schedul...