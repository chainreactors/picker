---
title: Arti 1.1.6 is released: Now you can connect* to Onion Services!
url: https://blog.torproject.org/arti_116_released/
source: Tor Project blog
date: 2023-07-01
fetch_date: 2025-10-04T11:57:20.454110
---

# Arti 1.1.6 is released: Now you can connect* to Onion Services!

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Arti 1.1.6 is released: Now you can connect\* to Onion Services!

by [nickm](/author/nickm)
| June 30, 2023

![](/arti_116_released/lead.png)

Arti is our ongoing project to create a next-generation Tor client in
Rust. Now we're announcing the latest release, Arti 1.1.6.

After months of hard work,
Arti finally has working
client-side onion service support!
That is, programs can\* now use Arti
to connect to onion services on the Tor network.

\*: Note that this feature is *not yet as secure* as the
equivalent feature in the C tor implementation,
and as such you probably shouldn't use it
for security-sensitive purposes.
(Our implementation is missing the â[vanguards-lite](https://gitlab.torproject.org/tpo/core/torspec/-/blob/main/proposals/333-vanguards-lite.md)â feature
that C tor uses to prevent [guard discovery](https://blog.torproject.org/announcing-vanguards-add-onion-services/) attacks.)
For this reason, the feature is (for now) disabled by default.
To turn it on, you can enable it on the command line
(`arti -o address_filter.allow_onion_addrs=true proxy`)
or edit your `arti.toml` configuration file
(set `allow_onion_addrs = true` in the section `[address_filter]`).

(*Edited 2023-07-07 to add*: Also, when you build Arti,
you need to provide a non-default Cargo feature.
Add `--features=arti/onion-service-client` when building.
This restriction will be removed in the next release.)

This release also introduces our key manager functionality.
Unlike the C `tor` implementation,
where the ability to manage keys on disk
grew organically (and unevenly) over time,
with Arti weâre trying to provide
a uniform and consistent API and CLI
for managing secret keys.
For now, this functionality is in a preliminary state,
and the usability is somewhat lacking.
If you want, you can use it to experiment with
[onion service client authorization](https://gitlab.torproject.org/gabi-250/arti-client-auth),
but you might have a better time
if you wait until the next release.

With this release, there have been
many smaller and less visible changes as well;
for those, please see the [CHANGELOG](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/CHANGELOG.md#arti-116-30-june-2023).

For more information on using Arti, see our top-level [README](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/README.md), and the
documentation for the [`arti` binary](https://gitlab.torproject.org/tpo/core/arti/-/tree/main/crates/arti).

Thanks to everybody who's contributed to this release, including
Alexander FÃ¦rÃ¸y, Andy, Jim Newsome, nate\_d1azzz, pinkforest,
Saksham Mittal, and Trinity Pointard.

Finally, our deep thanks to [Zcash Community Grants](https://zcashcommunitygrants.org/) for funding the
development of Arti!

* [announcements](/category/announcements)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/arti_116_released/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/arti_116_released/&text=Arti%201.1.6%20is%20released%20and%20ready%20for%20download.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/arti_116_released/&text=Arti%201.1.6%20is%20released%20and%20ready%20for%20download.)
[Bluesky](https://bsky.app/intent/compose?text=Arti%201.1.6%20is%20released%20and%20ready%20for%20download.%0Ahttps%3A//blog.torproject.org/arti_116_released/)

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