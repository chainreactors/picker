---
title: Tor VPN Beta: What we've learned building our own VPN for Android from scratch
url: https://blog.torproject.org/tor-vpn-beta/
source: Tor Project blog
date: 2026-09-09
fetch_date: 2026-09-10T06:52:44.005468
---

# Tor VPN Beta: What we've learned building our own VPN for Android from scratch

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Tor VPN Beta: What we've learned building our own VPN for Android from scratch

by [pavel](/author/pavel)
| September 9, 2026

![](/tor-vpn-beta/lead.png)

**For years, Tor Browser has been one of the most effective tools for protecting privacy and bypassing censorship online. But most people don't experience the internet through a browser anymore. They connect to it via their favorite apps. Wouldn't it be nice to extend the same privacy protections to messaging apps, social media, email, and other services?**

And for years, we heard this again and again in our user research. People wanted a simple way to protect their entire device, which inspired the idea for Tor VPN back in 2021. We focused on Android first, where the need was greatest and where we could reach the most users in censored regions. We built Tor VPN Beta as a first version, with the expectation that we would learn from real-world use. And when we first launched Tor VPN Beta for Android in a limited release last fall, the primary use case quickly became much clearer: unblock the internet. This has shaped how we've prioritized development and user support in the time since the initial launch, and how we think about the product moving forward.

![Image app isolation feature](/tor-vpn-beta/per-app-routing.png)

## What makes Tor VPN different

Unlike commercial VPNs, Tor VPN Beta is built on a fundamentally different model. It is our first step into device-level network protection on mobile to extend Tor's protections beyond the browser. Each mobile app on your device gets its own Tor circuit, rather than sharing a single tunnel. That means activity from one app can't easily be linked to another. This type of app isolation is a design choice heavily inspired by the cross-site tracking protections in Tor Browser[1](#fn-nested). It's a different model from most VPNs, and one that's designed to reduce cross-tracking by default.

As Tor VPN Beta has matured, we've also worked on making that app-level control easier to use. The Apps screen is now searchable, so people can more quickly find a specific app and decide whether it should be routed through Tor.

![Image App screen searchbar](/tor-vpn-beta/apps-screen-searchbar.png)

## Rethinking how we design for circumvention

While Tor VPN Beta includes features commonly associated with VPNs, such as exit selection, those aren't always the right approach for users trying to bypass censorship. This was one of the most important lessons that came from usability testing and early feedback during the development stage.

We originally explored giving users more control over exit selection, which, on paper, sounded great. But in practice, this introduced confusion. Users trying to bypass censorship were selecting exit locations when they should have been using bridges instead. There was a mismatch between how Tor works and how people expected it to work. This is why the current design required connecting the app to the Tor network first before selecting an exit. Exit selection is still something we want to explore more fully in the future, but it needs to be introduced in a way that doesn't create user error in high-risk situations.

## Used where it's needed most

Early on, we saw strong adoption in highly censored regions, including Iran and Turkmenistan. This stood in contrast to Tor Browser for Android, which tends to skew more toward users in the Global North. With Tor VPN Beta, we're seeing much deeper engagement from users in the Global South, people dealing with network restrictions as a daily reality.

Because of how people are using Tor VPN Beta, we've doubled down on improving its circumvention capabilities. One example was prioritizing the addition of WebTunnel bridges with one of the early releases (1.4.0 beta), which helps Tor traffic look like regular encrypted web traffic. This makes it harder for censors to detect and block connections. We have also fixed several bugs and made quality-of-life improvements across bridge support more generally, with the goal of making bridge use more reliable.

## Stability and reliability matter just as much as features

In fact, a significant amount of work since the early release has gone into improving stability. Tor VPN is built on [Arti, our next-generation Tor implementation written in Rust](https://blog.torproject.org/announcing-arti/). Under the hood, that means a new, solid technical foundation rather than patching around legacy architecture. One of the immediate benefits is improved reliability, including fewer crashes and better handling of network conditions. We have also invested in making our builds reproducible and getting the app onto F-Droid. Reproducible builds let anyone verify that the binary you're running matches the published source code, while F-Droid availability gives users a way to install and update the app without relying on Google Play, both of which matter for a privacy and security-focused tool.

While Tor VPN Beta doesn't behave like a commercial VPN optimized for speed, [the Tor network has become more performant](https://blog.torproject.org/congestion-contrl-047/) over time, and [we're continuing to bring those improvements into the mobile experience](https://gitlab.com/guardianproject/tormobile/arti-mobile). There are still performance features from Tor's C implementation, like congestion control, that are not yet available in Arti. Bringing those capabilities over is part of what comes next.

> *We set out to extend Tor beyond the browser to close a gap in mobile protection, but the project was quickly being shaped by how people actually use it, especially those who need reliable, device-wide circumvention. So we focused on building the right foundation for Tor on mobile with a modular Tor stack centered on Arti and [Onionmasq](https://gitlab.torproject.org/ahf/onionmasq) that can evolve with real-world use. These components are now reusable across multiple applications, reducing ecosystem fragmentation and long-term maintenance risk.
> -- Duncan, UX-Team Lead/ Product Manager, Tor VPN*

There's more work to do here. Tor Browser still sets the standard for what's possible, and part of our goal is to bring Tor VPN closer to that level over time.

## What's next?

Tor VPN Beta is the result of a collaborative, multi-year effort. Thank you to [The Guardian Project](https://guardianproject.info/) for their guidance and critical low-level mobile libraries, and the LEAP Encryption Access Project for their quality work, without both the app would have never seen the light of day. We're [continuing to build Tor VPN Beta](https://blog.torproject.org/code-audit-tor-vpn/) in the open, shaped by how people are actually using it.

That means improving circumvention in restrictive environments, bringing more performance features into Arti, and refining the user experience to reduce confusion and risk.

And most importantly, continuing to learn from the people who rely on it. If that includes you, and you want to help shape the development of Tor VPN Beta, please visit our [refreshed download pages](https://download.torproject.org/). In addition to downloading the app as an APK or from the Google Play Store, you can now use F-Droid to access Tor VPN Beta.

---

1. For more detail on Tor VPN's current security properties and known limitations, please refer to the [threat model](https://support.torproject.org/tor-vpn/security/threat-model/).[↩](#fnref-nested)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/tor-vpn-beta/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/tor-vpn-beta/&text=Last%20fall%2C%20we%20soft...