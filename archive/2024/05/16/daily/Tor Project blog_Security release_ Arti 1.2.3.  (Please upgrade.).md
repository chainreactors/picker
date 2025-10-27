---
title: Security release: Arti 1.2.3.  (Please upgrade.)
url: https://blog.torproject.org/arti_1_2_3_released/
source: Tor Project blog
date: 2024-05-16
fetch_date: 2025-10-06T17:22:26.760513
---

# Security release: Arti 1.2.3.  (Please upgrade.)

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Security release: Arti 1.2.3. (Please upgrade.)

by [nickm](/author/nickm)
| May 15, 2024

![](/arti_1_2_3_released/lead.png)

We have released updates to Arti today,
to resolve a pair of security issues
related to circuit construction for onion services.

These vulnerabilities affect the crate `tor-circmgr 0.18.0`,
released along with Arti version 1.2.2.
They are fixed in `tor-circmgr 0.18.1`.
(Fixes will also appear in Arti version 1.2.4,
to be released on our regular schedule at the start of June.)

## Who is affected

If you use arti to connect to onion services,
or to run onion services,
and you are using Arti 1.2.2 or tor-circmgr 0.18.0,
you should upgrade.

(In Arti 1.2.1 and earlier, vanguards were still an experimental feature,
or absent, so those versions are classified as "not affected",
but downgrading to these versions will not improve your security.)

## Upgrade instructions

If you installed Arti via `cargo install`, use this command to update:

```
cargo install --locked --features=full arti
# or whatever --features you used before
```

If you obtained Arti as source code from git, fetch the tag `arti-v1.2.3`
and rebuild, with `cargo build --locked --release --features=full -p arti`.

## The issues

Both issues affect circuit construction when vanguards are enabled,
and affect the length.

First, when building anonymizing circuits to or from an onion service with
'lite' vanguards (the default) enabled,
the circuit manager code would build the circuits with one hop too few.
This makes users of this code more vulnerable to some kinds of traffic analysis
when they run or visit onion services.
This bug is tracked as issue [#1409](https://gitlab.torproject.org/tpo/core/arti/-/issues/1409), and as [TROVE](https://gitlab.torproject.org/tpo/core/team/-/wikis/NetworkTeam/TROVE)-2024-003.
Its severity is ["high"](https://gitlab.torproject.org/tpo/core/team/-/wikis/NetworkTeam/SecurityPolicy).

Second, when 'full' vanguards are enabled, some circuits are supposed to be
built with an extra hop to minimize the linkability of the guard nodes.
In some circumstances,
the circuit manager would build circuits with one hop too few,
making it easier for an adversary to discover the L2 and L3 guards
of the affected clients and services.
This issue is tracked as issue [#1400](https://gitlab.torproject.org/tpo/core/arti/-/issues/1400), and as [TROVE](https://gitlab.torproject.org/tpo/core/team/-/wikis/NetworkTeam/TROVE)-2024-004.
Its severity is ["medium"](https://gitlab.torproject.org/tpo/core/team/-/wikis/NetworkTeam/SecurityPolicy).

* [announcements](/category/announcements)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/arti_1_2_3_released/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/arti_1_2_3_released/&text=Arti%201.2.3%20is%20released%20and%20ready%20for%20download.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/arti_1_2_3_released/&text=Arti%201.2.3%20is%20released%20and%20ready%20for%20download.)
[Bluesky](https://bsky.app/intent/compose?text=Arti%201.2.3%20is%20released%20and%20ready%20for%20download.%0Ahttps%3A//blog.torproject.org/arti_1_2_3_released/)

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