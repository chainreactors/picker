---
title: New Release: Tails 7.15.1
url: https://blog.torproject.org/new-release-tails-7_15_1/
source: Tor Project blog
date: 2026-10-23
fetch_date: 2026-10-24T06:48:03.478223
---

# New Release: Tails 7.15.1

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tails 7.15.1

by [tails](/author/tails)
| October 23, 2026

![](/new-release-tails-7_15_1/lead.jpg)

This release is an emergency release to remove a compromised certificate
authority.

## Changes and updates

* Update *Tor Browser* to [15.0.26](https://blog.torproject.org/new-release-tor-browser-15026/), which fixes [CVE-2026-113470](https://app.opencve.io/cve/CVE-2026-113470).

  On [October 17](https://www.mozilla.org/en-US/security/advisories/mfsa2026-112/), *Mozilla* blocked the certificates of [eMudhra, a certificate authority that had its intermediate certificates compromised](https://en.wikipedia.org/wiki/EMudhra). *Tor Browser* 15.0.26 now blocks all eMudhra certificates as well.

  Using one of the compromised intermediate certificates, an attacker could
  impersonate any website, even if the connection is secured with HTTPS.

  This attack could be performed by a Tor exit node, the Internet service
  provider of an exit node, or a government. Onion sites are not vulnerable.

  We are not aware of this attack being used by exit nodes so far.
* Update the certificate authorities to block all eMudhra certificates in other applications.

  In addition to *Tor Browser* , other applications rely on the certificate authorities included in Tails with the `ca-certificates` Debian package to secure their connections.

## Get Tails 7.15.1

### To upgrade your Tails USB stick and keep your Persistent Storage

* Automatic upgrades are available from Tails 7.0 or later to 7.15.1.
* If you cannot do an automatic upgrade or if Tails fails to start after an automatic upgrade, please try to do a [manual upgrade](https://tails.net/doc/upgrade/#manual).

### To install Tails 7.15.1 on a new USB stick

Follow our [installation instructions](https://tails.net/install/).

The Persistent Storage on the USB stick will be lost if you install instead of
upgrading.

### To download only

If you don't need installation or upgrade instructions, you can download Tails
7.15.1 directly:

* [For USB sticks (USB image)](https://tails.net/install/download/)
* [For DVDs and virtual machines (ISO image)](https://tails.net/install/download-iso/)

## Support and feedback

For support and feedback, visit the [Support
section](https://tails.net/support/) on the Tails website.

* [tails](/category/tails)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-release-tails-7_15_1/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-release-tails-7_15_1/&text=This%20release%20is%20an%20emergency%20release%20to%20remove%20a%20compromised%20certificate%20authority.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-release-tails-7_15_1/&text=This%20release%20is%20an%20emergency%20release%20to%20remove%20a%20compromised%20certificate%20authority.)
[Bluesky](https://bsky.app/intent/compose?text=This%20release%20is%20an%20emergency%20release%20to%20remove%20a%20compromised%20certificate%20authority.%0Ahttps%3A//blog.torproject.org/new-release-tails-7_15_1/)

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

## Upcoming Events

October 28, 2026 – October 30, 2026

## [Mozilla Festival 2026 (MozFest), Barcelona](/event/mozfest-2026/)

November 2, 2026

## [Ethereum Cypherpunk Congress Mumbai](/event/Ethereum-Cypherpunk-Congress-Mumbai/)

November 3, 2026 – November 6, 2026

## [Devcon 8 (Mumbai)](/event/devcon8/)

## Recent Updates

## [New Release: Tails 7.15.1](/new-release-tails-7_15_1/)

by [tails](/author/tails)
| October 23, 2026

This release is an emergency release to remove a compromised certificate authority.

## [New Release: Tor Browser 15.0.26](/new-release-tor-browser-15026/)

by [ma1](/author/ma1)
| October 21, 2026

Tor Browser 15.0.26 is now available from the Tor Browser download page and also from our distribution directory.

## [New Alpha Release: Tor Browser 16.0a14](/new-alpha-release-tor-browser-160a14/)

by [ma1](/author/ma1)
| October 15, 2026

Tor Browser 16.0a14 is now available from the Tor Browser download page and also from our distribution directory.

### Download Tor Browser

Download Tor Browser to experience real private browsing without tracking, surveillance, or censorship.

[Download Tor Browser](https://download.torproject.org/)

### Subscribe to our Newsletter

Get monthly updates and opportunities from the Tor Project:

[Sign up](https://donate.torproject.org/subscribe/)

####

####

####

####

####

####

####

####

Trademark, copyright notices, and rules for use by third parties can be found in our [FAQ](https://www.torproject.org/about/trademark/).