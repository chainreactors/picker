---
title: New Release: Tails 7.10.1
url: https://blog.torproject.org/new-release-tails-7_10_1/
source: Tor Project blog
date: 2026-08-05
fetch_date: 2026-08-06T05:03:01.872859
---

# New Release: Tails 7.10.1

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tails 7.10.1

by [tails](/author/tails)
| August 5, 2026

![](/new-release-tails-7_10_1/lead.jpg)

This release is an emergency release to fix critical security vulnerabilities
in the *Linux* kernel and the *expat* XML library.

## Changes and updates

* Update the *Linux* kernel to 6.12.100, which fixes [CVE-2026-64560](https://www.cve.org/CVERecord?id=CVE-2026-64560), a vulnerability that could allow *Tor Browser* in Tails to gain administrator privileges.

For example, if a malicious website that you visit is able to exploit
CVE-2026-64560, they might take full control of your Tails and deanonymize
you.

This attack is very unlikely but could be performed by a strong attacker, such
as a government or a hacking firm. We are not aware of this attack being used
in practice until now.

* Update the *expat* XML library to 2.8.2, which fixes [DSA-6404-1](https://security-tracker.debian.org/tracker/DSA-6404-1), a set of vulnerabilities that could allow different applications in Tails to gain administrator privileges.

For example, if an attacker tricks you into opening a malicious file in an
application that uses *expat* , such as *LibreOffice* , *Audacity* , or *Git*
, they might then use one of these vulnerabilities to take full control of
your Tails and deanonymize you.

This attack is very unlikely but could be performed by a strong attacker, such
as a government or a hacking firm. We are not aware of this attack being used
in practice until now.

* Compress automatic upgrades with `zstd` for a faster startup, as we already did for the USB image in [Tails 7.0](https://tails.net/news/version_7.0/).
* Make USB images and automatic upgrades 70 MB smaller by removing unused firmware.

For more details, read our
[changelog](https://gitlab.tails.boum.org/tails/tails/-/blob/master/debian/changelog).

## Get Tails 7.10.1

### To upgrade your Tails USB stick and keep your Persistent Storage

* Automatic upgrades are available from Tails 7.0 or later to 7.10.1.
* If you cannot do an automatic upgrade or if Tails fails to start after an automatic upgrade, please try to do a [manual upgrade](https://tails.net/doc/upgrade/#manual).

### To install Tails 7.10.1 on a new USB stick

Follow our [installation instructions](https://tails.net/install/).

The Persistent Storage on the USB stick will be lost if you install instead of
upgrading.

### To download only

If you don't need installation or upgrade instructions, you can download Tails
7.10.1 directly:

* [For USB sticks (USB image)](https://tails.net/install/download/)
* [For DVDs and virtual machines (ISO image)](https://tails.net/install/download-iso/)

## Support and feedback

For support and feedback, visit the [Support
section](https://tails.net/support/) on the Tails website.

* [tails](/category/tails)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-release-tails-7_10_1/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-release-tails-7_10_1/&text=This%20release%20is%20an%20emergency%20release%20to%20fix%20critical%20security%20vulnerabilities%20in%20the%20Linux%20kernel%20and%20the%20expat%20XML%20library.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-release-tails-7_10_1/&text=This%20release%20is%20an%20emergency%20release%20to%20fix%20critical%20security%20vulnerabilities%20in%20the%20Linux%20kernel%20and%20the%20expat%20XML%20library.)
[Bluesky](https://bsky.app/intent/compose?text=This%20release%20is%20an%20emergency%20release%20to%20fix%20critical%20security%20vulnerabilities%20in%20the%20Linux%20kernel%20and%20the%20expat%20XML%20library.%0Ahttps%3A//blog.torproject.org/new-release-tails-7_10_1/)

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

August 6, 2026 – August 9, 2026

## [DEF CON 34, Las Vegas](/event/defcon-2026/)

October 28, 2026 – October 30, 2026

## [Mozilla Festival 2026 (MozFest), Barcelona](/event/mozfest-2026/)

## Recent Updates

## [New Release: Tails 7.10.1](/new-release-tails-7_10_1/)

by [tails](/author/tails)
| August 5, 2026

This release is an emergency release to fix critical security vulnerabilities in the *Linux* kernel and the *expat* XML library.

## [Arti 2.5.1 released](/arti_2_5_1_released/)

by [opara](/author/opara)
| August 4, 2026

Arti 2.5.1 is released and ready for download.

## [Snowflake Volunteer, an Android app to help people bypass censorship](/snowflake-volunteer-standalone-app-to-help-people-bypass-censorship/)

by [pavel](/author/pavel)
| August 3, 2026

There are many ways to help people bypass censorship with Snowflakeâa browser extension, using Orbot or Tor Browser, website embedding etc. We set out to experiment with a new mechanism and test an Android app called [Snowflake Volunteer](https://f-droid.org/en/packages/io.bloco.snowflake/) for those willing to help people reach the Tor network and circumvent censorship from their mobile devices. It was built open-source by [Bloco](https://www.bloco.io/), an Android app studio from Portugal.

### Download Tor Browser

Download Tor Browser to experience real private browsing without tracking, surveillance, or censorship.

[Download Tor Browser](https://www.torproject.org/download/)

### Subscribe to our Newsletter

Get monthly updates and opportunities from the Tor Project:

[Sign up](https://newsletter.torproject.org/)

####

####

####

####

####

####

####

####

Trademark, copyright notices, and rules for use by third parties can be found in our [FAQ](https://www.torproject.org/about/trademark/).