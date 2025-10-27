---
title: Arti 1.4.3 is released: Prometheus metrics support, inital work on Counter Galois Onion and congestion control.
url: https://blog.torproject.org/arti_1_4_3_released/
source: Tor Project blog
date: 2025-05-02
fetch_date: 2025-10-06T22:32:49.467038
---

# Arti 1.4.3 is released: Prometheus metrics support, inital work on Counter Galois Onion and congestion control.

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Arti 1.4.3 is released: Prometheus metrics support, inital work on Counter Galois Onion and congestion control.

by [wesleyac](/author/wesleyac)
| May 1, 2025

![](/arti_1_4_3_released/lead.png)

Arti is our ongoing project to create a next-generation Tor client in
Rust. Now we're announcing the latest release, Arti 1.4.3.

This release adds support for exporting metrics via [Prometheus](https://prometheus.io).
To use this feature, compile Arti with the `metrics` feature,
and add the `[metrics]` section to your configuration file,
as shown in our [example config](https://gitlab.torproject.org/tpo/core/arti/-/blob/494ad6c1a181d3132773f5168856a220625c2cfb/crates/arti/src/arti-example-config.toml#L99-115).
Currently, only a couple metrics are exported, but more will be added as time goes on.
If you are using Arti and there are metrics that would be useful for your usecase,
please do file an issue asking for them to be added!
Keep in mind that enabling metrics has the potential to leak information
to anyone who can access the metrics port.
If you use metrics in production, be sure to carefully check your firewall rules
to ensure that the metrics information is not more widely accessible than you need it to be.

We're also publishing the new [`arti-ureq`](https://crates.io/crates/arti-ureq) Rust crate,
which allows making HTTP requests over Tor using Arti with the Rust [`ureq`](https://crates.io/crates/ureq) library.
Several [example programs](https://gitlab.torproject.org/tpo/core/arti/-/tree/main/examples/ureq-examples?ref_type=heads) are available in the Arti repo.

This release also has some of the cryptographic groundwork for supporting [Counter Galois Onion](https://eprint.iacr.org/2025/583),
a new encryption scheme designed to protect against tagging attacks,
thus strengthening Tor's end-to-end integrity protection.

This release also has some under-the-hood steps towards implementing [congestion control](https://blog.torproject.org/congestion-contrl-047/),
a protocol which intelligently adjusts the rate at which data is sent
to ensure that the Tor network runs as fast and smoothly as possible.

For full details on what we've done, and for information about
many smaller and less visible changes as well,
please see the [CHANGELOG](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/CHANGELOG.md#arti-143--1-may-2025).

For more information on using Arti, see our top-level [README](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/README.md), and the
documentation for the [`arti` binary](https://gitlab.torproject.org/tpo/core/arti/-/tree/main/crates/arti).

Thanks to everybody who's contributed to this release, including
CocytusDEDI, hashcatHitman, hjrgrn, nield, playbahn, syphyr, Vijaya Bhaskar, and Yaksh Bariya.
Also, our deep thanks to
the [Bureau of Democracy, Human Rights and Labor](https://www.state.gov/bureaus-offices/under-secretary-for-civilian-security-democracy-and-human-rights/bureau-of-democracy-human-rights-and-labor/)
and our [other sponsors](https://www.torproject.org/about/sponsors/)
for funding the development of Arti!

* [announcements](/category/announcements)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/arti_1_4_3_released/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/arti_1_4_3_released/&text=Arti%201.4.3%20is%20released%20and%20ready%20for%20download.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/arti_1_4_3_released/&text=Arti%201.4.3%20is%20released%20and%20ready%20for%20download.)
[Bluesky](https://bsky.app/intent/compose?text=Arti%201.4.3%20is%20released%20and%20ready%20for%20download.%0Ahttps%3A//blog.torproject.org/arti_1_4_3_released/)

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

Tor Browser 14.5.7 is now available from the Tor Browser download page and also from our distribution directory.

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