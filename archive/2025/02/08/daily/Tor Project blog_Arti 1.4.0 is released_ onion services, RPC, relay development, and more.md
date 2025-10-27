---
title: Arti 1.4.0 is released: onion services, RPC, relay development, and more
url: https://blog.torproject.org/arti_1_4_0_released/
source: Tor Project blog
date: 2025-02-08
fetch_date: 2025-10-06T20:51:06.089565
---

# Arti 1.4.0 is released: onion services, RPC, relay development, and more

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Arti 1.4.0 is released: onion services, RPC, relay development, and more

by [Diziet](/author/diziet)
| February 7, 2025

![](/static/images/lead.png)

Arti is our ongoing project to create a next-generation Tor client in
Rust. Now we're announcing the latest release, Arti 1.4.0.

This release offers a new [RPC interface](https://gitlab.torproject.org/tpo/core/arti/-/tree/main/doc/dev/rpc-book/src), which is Arti's replacement for
C Tor's [control port](https://spec.torproject.org/control-spec/index.html) with many improvements.

There has also been a lot of preparatory work for relay support,
bugfixes, and work towards
service-side onion service denial-of-service resistance.

For full details on what we've done, and for information about
many smaller and less visible changes as well,
please see the [CHANGELOG](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/CHANGELOG.md#arti-140--7-february-2025).

For more information on using Arti, see our top-level [README](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/README.md), and the
documentation for the [`arti` binary](https://gitlab.torproject.org/tpo/core/arti/-/tree/main/crates/arti).

With this release, we are happy to announce that our [Arti website](https://arti.torproject.org/) has
received an extensive overhaul. This website will be used to find general information
about the Arti project, such as example code, documentation, and more.
A big thanks to our friends from DocumentWrite for helping us with the new
website design and implementation!

## Dedication

The Arti 1.4.0 release is dedicated to the memory of JÃ©rÃ©my Bobbio (1982-2024), known
in our community as Lunar. Lunar was a Tor volunteer, free software hacker, and
community organizer.

Inside Tor, Lunar will be remembered for leading the efforts around Tor's old Weekly
News newsletter, but also for caring deeply about both the organization the people
around the organization.

Outside of Tor, Lunar worked on highly successful free software projects such as the
Debian project and helped build the infrastructure and tooling around the Reproducible
Builds project, a project that continues to benefit the broader ecosystem.

Lunar will be deeply missed, both in our community and in the many other communities he
participated in.

See also what other projects are writing about Lunar:

* [The Debian Project](https://www.debian.org/News/2024/20241119)
* [lunar.anargeek.net](https://lunar.anargeek.net/)
* [Linux Weekly News](https://lwn.net/Articles/997775/)
* [The Reproducible Builds Project](https://reproducible-builds.org/news/2024/11/14/reproducible-builds-mourns-the-passing-of-lunar/)

## New RPC Interface

With this release, Arti's [RPC interface](https://gitlab.torproject.org/tpo/core/arti/-/tree/main/doc/dev/rpc-book/src) is now ready for use.

Arti RPC takes the place of the [control port](https://spec.torproject.org/control-spec/index.html)
in the C Tor implementation,
with several improvements:

* The protocol is based on JSON,
  to reduce the need for custom-built parsers and encoders.
* The protocol uses a capabilities-based design to prevent applications
  from accidentally interfering with one another's use of Arti.
* The protocol is more explicitly extensible,
  with clear specifications of how clients and Arti
  must handle unexpected messages, parameters, and data.
* There is a specified mechanism for [discovery](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/doc/dev/rpc-book/src/rpc-connect-spec.md) to simplify the task
  of configuring applications to find and use the RPC port.
* The protocol allows multiple simultaneous requests on a single connection.
* We provide a default [client library],
  with [C](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/crates/arti-rpc-client-core/arti-rpc-client-core.h?ref_type=heads) and [Python](https://gitlab.torproject.org/tpo/core/arti/-/tree/main/python/arti_rpc?ref_type=heads) wrappers,
  to save application developers
  from having to implement this logic themselves.

At present the supported functionality is limited:
applications can use the RPC API
to connect to Arti,
check the bootstrap process,
and open data streams.
Coming releases will add more functionality based on developers' needs.
(We already have wish-lists from [Tails](https://forum.torproject.org/t/defining-an-interface-to-arti/6432/7) and [Tor Browser](https://gitlab.torproject.org/tpo/core/arti/-/issues/1303).)

We hope that developers will experiment with using the API and client library
so that we can use their feedback to guide priorities for the upcoming work.

This is a major milestone in making it easier for developers to integrate Arti
in their own applications and services without directly embedding the Arti Rust
library itself. We hope this will open up opportunities for external developers and
allowing a growing community of privacy conscious users to benefit from the
strong online protections Tor offers.

We do not expect to make breaking changes in the RPC API or the client library,
though we will wait for
a little more developer experience before we declare it officially stable.

Thanks to everybody who's contributed to this release, including
Dimitris Apostolou, hhamud, Neel Chauhan and tidely.

And as always, our deep thanks to
[Zcash Community Grants](https://zcashcommunitygrants.org/),
the [Bureau of Democracy, Human Rights and Labor](https://www.state.gov/bureaus-offices/under-secretary-for-civilian-security-democracy-and-human-rights/bureau-of-democracy-human-rights-and-labor/),
and our [other sponsors](https://www.torproject.org/about/sponsors/)
for funding the development of Arti!

* [announcements](/category/announcements)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/arti_1_4_0_released/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/arti_1_4_0_released/&text=Arti%201.4.0%20is%20released%20and%20ready%20for%20download.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/arti_1_4_0_released/&text=Arti%201.4.0%20is%20released%20and%20ready%20for%20download.)
[Bluesky](https://bsky.app/intent/compose?text=Arti%201.4.0%20is%20released%20and%20ready%20for%20download.%0Ahttps%3A//blog.torproject.org/arti_1_4_0_released/)

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

## [New Alpha Release: Tor Browser 15.0a3](/new-alpha-release-tor-browser-150a3/)

by [boklm](/author/boklm)
| September 22, 2025

Tor Browser 15.0a3 is now available from the Tor Browser download page and also from our distribution directory.

## [New Release: Tails 7.0](/new-release-tails-7_0/)

by [tails](/author/tails)
| September 18, 2025

We are very excited to present you Tails 7.0, the first version of Tails based
on Debian 13 (Trixie) and GNOME 48 (Bengaluru). Tails 7.0 brings new versions
of many applications included in Tails.

## [New Release: Tor Browser 14.5.7](/new-release-tor-browser-1457/)

by [ma1](/author/ma1)
| September 16, 2025

Tor Browser 14.5.7 is n...