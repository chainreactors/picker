---
title: Arti 2.0.0 released: Relay, directory authority, and RPC development.
url: https://blog.torproject.org/arti_2_0_0_released/
source: Tor Project blog
date: 2026-02-02
fetch_date: 2026-02-03T04:11:07.722722
---

# Arti 2.0.0 released: Relay, directory authority, and RPC development.

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Arti 2.0.0 released: Relay, directory authority, and RPC development.

by [wesleyac](/author/wesleyac)
| February 2, 2026

![](/arti_2_0_0_released/lead.png)

Arti is our ongoing project to create a next-generation Tor implementation in
Rust. We're happy to announce the latest release, Arti 2.0.0.

While "2.0" may sound like an exciting release number, it's actually fairly mundane.
[Semver](https://semver.org) requires us to bump our major version number when making breaking changes,
and we had a couple breaking changes we wanted to make in order to keep our APIs tidy.
These breaking changes are:

* Removing support for the long-deprecated `proxy.socks_port` and `proxy.dns_port` configuration options
  (`proxy.socks_listen` and `proxy.dns_listen` should be used instead).
* Removing support for the old syntax for specifying directory authorities.
  The new syntax can be seen in the [example configuration](https://gitlab.torproject.org/tpo/core/arti/-/blob/df5fba75c61001b07115776518f95bcb4d51681c/crates/arti/src/arti-example-config.toml#L449-484).
* Marking all APIs in the `arti` crate experimental.
  These APIs are likely to get moved into other crates or removed in the future,
  and anyone who uses APIs from the `arti` crate directly
  (as opposed to `arti-client` or other lower-level crates)
  should file an issue explaining their usecase,
  so that it can be considered as we move these APIs elsewhere.

Other than removing deprecated features,
this release adds support for using the `inet-auto` socket type
to automatically pick an unused TCP port for the RPC server.

There is also a significant amount of behind-the-scenes work on relay
and directory authority functionality in this release.

On the relay front, this includes our new generic and modular [circuit reactor architecture](https://gitlab.torproject.org/tpo/core/arti/-/blob/a63c96bdc62fc088affa565be61c0215830b870e/doc/dev/notes/relay-conflux.md),
the ability to launch relay channels, the ability to respond to handshakes,
and the groundwork for relays to act as the server side of a TLS connection.

On the directory authority front, we've done significant work on authority certificate management,
allowing Arti to download, validate, and store authority certificates.

While running Arti as a relay or directory authority is not yet supported,
we're making good progress towards those long-term goals.

For full details on what we've done, including API changes,
and for information about many more minor and less-visible changes,
please see the [CHANGELOG](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/CHANGELOG.md?ref_type=heads#arti-200--2-february-2026).

For more information on using Arti, see our top-level [README](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/README.md),
and the documentation for the [`arti` binary](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/crates/arti/README.md).

Thanks to everybody who's contributed to this release, including
Niel Duysters, carti-it, hjrgrn, and sjcobb!

Also, our deep thanks to our [sponsors](https://www.torproject.org/about/sponsors/) for funding the development of Arti!

* [announcements](/category/announcements)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/arti_2_0_0_released/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/arti_2_0_0_released/&text=Arti%202.0.0%20is%20released%20and%20ready%20for%20download.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/arti_2_0_0_released/&text=Arti%202.0.0%20is%20released%20and%20ready%20for%20download.)
[Bluesky](https://bsky.app/intent/compose?text=Arti%202.0.0%20is%20released%20and%20ready%20for%20download.%0Ahttps%3A//blog.torproject.org/arti_2_0_0_released/)

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

## Recent Updates

## [Arti 2.0.0 released: Relay, directory authority, and RPC development.](/arti_2_0_0_released/)

by [wesleyac](/author/wesleyac)
| February 2, 2026

Arti 2.0.0 is released and ready for download.

## [New Release: Tails 7.4.1](/new-release-tails-7_4_1/)

by [tails](/author/tails)
| January 30, 2026

This release is an emergency release to fix critical security vulnerabilities
in OpenSSL, a network encryption library used by Tor.

## [New Release: Tor Browser 15.0.5](/new-release-tor-browser-1505/)

by [morgan](/author/morgan)
| January 29, 2026

Tor Browser 15.0.5 is now available from the Tor Browser download page and also from our distribution directory.

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