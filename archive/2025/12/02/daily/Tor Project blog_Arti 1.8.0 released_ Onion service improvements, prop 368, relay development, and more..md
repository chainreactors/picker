---
title: Arti 1.8.0 released: Onion service improvements, prop 368, relay development, and more.
url: https://blog.torproject.org/arti_1_8_0_released/
source: Tor Project blog
date: 2025-12-02
fetch_date: 2025-12-03T03:17:17.897071
---

# Arti 1.8.0 released: Onion service improvements, prop 368, relay development, and more.

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Arti 1.8.0 released: Onion service improvements, prop 368, relay development, and more.

by [gabi](/author/gabi)
| December 2, 2025

![](/arti_1_8_0_released/lead.png)

Arti is our ongoing project to create a next-generation Tor implementation in Rust.
We're happy to announce the latest release, Arti 1.8.0.

This release introduces a new, usage-based, timeout for strongly isolated circuits,
as specified in [proposal 368](https://spec.torproject.org/proposals/368-cdt-rethink.html).

Arti now has experimental [`tokio-console`](https://crates.io/crates/tokio-console) support for development and debugging purposes.
To use this feature, you will need to build Arti
with the experimental `tokio-console` cargo feature **and** `--cfg tokio_unstable`,
and enable the [`tokio_console` option](https://gitlab.torproject.org/tpo/core/arti/-/blob/arti-v1.8.0/crates/arti/src/arti-example-config.toml#L119-129) in the config.

This release also brings some of quality of life improvements for onion services,
with the new experimental [`arti hsc ctor-migrate`](https://gitlab.torproject.org/tpo/core/arti/-/blob/arti-v1.8.0/doc/hsc.md#migrating-from-c-tor-to-arti) command
for migrating C Tor client restricted discovery keys
(previously known as "client authorization keys")
to Arti's keystore, and a [configuration option](https://gitlab.torproject.org/tpo/core/arti/-/blob/arti-v1.8.0/crates/arti/src/arti-example-config.toml#L561-565)
for controlling which onion services to launch.

Behind the scenes, we have continued development of functionality
required to support relays and directory authorities.
This development has focused on the routing architecture and protocol implementation (circuits and channels),
parsing and generating Tor network documents,
directory cache support,
and on implementing the OR port listener and the associated configuration.

For full details on what we've done, including API changes,
and for information about many more minor and less visible changes,
please see the [CHANGELOG](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/CHANGELOG.md?ref_type=heads#arti-170--30-october-2025).

For more information on using Arti, see our top-level [README](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/README.md),
and the documentation for the [`arti` binary](https://gitlab.torproject.org/tpo/core/arti/-/tree/main/crates/arti).

Thanks to everybody who's contributed to this release, including
Dimitris Apostolou, hashcatHitman, hjrgrn, Mynacol, Neel Chauhan,
nield, Nihal, NoisyCoil.

Also, our deep thanks to our [sponsors](https://www.torproject.org/about/sponsors/) for funding the development of Arti!

* [announcements](/category/announcements)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/arti_1_8_0_released/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/arti_1_8_0_released/&text=Arti%201.8.0%20is%20released%20and%20ready%20for%20download.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/arti_1_8_0_released/&text=Arti%201.8.0%20is%20released%20and%20ready%20for%20download.)
[Bluesky](https://bsky.app/intent/compose?text=Arti%201.8.0%20is%20released%20and%20ready%20for%20download.%0Ahttps%3A//blog.torproject.org/arti_1_8_0_released/)

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

December 10, 2025

## [State of the Onion 2025](/event/state-of-the-onion-2025/)

## Recent Updates

## [Arti 1.8.0 released: Onion service improvements, prop 368, relay development, and more.](/arti_1_8_0_released/)

by [gabi](/author/gabi)
| December 2, 2025

Arti 1.8.0 is released and ready for download.

## [The Future of Tor Browser Alpha](/future-of-tor-browser-alpha/)

by [morgan](/author/morgan)
| December 1, 2025

Starting with Tor Browser 16.0a1, the Tor Browser Alpha release channel will be based on Firefox Rapid Release rather than Firefox Extended Support Release. If you are an at-risk user, concerned about your privacy, or just need a web-browser that works reliably, you should not use Tor Browser Alpha and instead stick with Tor Browser Stable.

## [Keeping the internet free together: State of the Onion Community Day](/community-day-state-of-the-onion-2025/)

by [arturom](/author/arturom)
| November 26, 2025

Join us for part 2 of **State of the Onion: Community Day**. Building on this year's theme, we've invited other members of the Tor community to share insights from their work and how they are supporting the fight to FREE THE INTERNET.

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