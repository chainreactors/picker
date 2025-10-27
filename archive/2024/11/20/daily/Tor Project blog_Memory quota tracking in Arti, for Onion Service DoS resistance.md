---
title: Memory quota tracking in Arti, for Onion Service DoS resistance
url: https://blog.torproject.org/arti_1_3_0_memquota/
source: Tor Project blog
date: 2024-11-20
fetch_date: 2025-10-06T19:23:50.478781
---

# Memory quota tracking in Arti, for Onion Service DoS resistance

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Memory quota tracking in Arti, for Onion Service DoS resistance

by [Diziet](/author/diziet)
| November 19, 2024

![](/static/images/lead.png)

Last week we [released Arti 1.3.0](https://blog.torproject.org/arti_1_3_0_released/),
the latest version of our rewrite of Tor in Rust.
One new feature in this release is memory quota tracking.

### Tracking and restricting memory for queued data

The memory quota tracking feature allows you to restrict the amount of memory used by an Arti process.
In particular, it allows you to limit the amount of memory
*that other people can cause your Arti to use*.

This is particularly important when Arti is being used
to provide an Onion Service (aka a Tor Hidden Service).
Running an Onion Service means letting users from all over the network
connect to your service
(depending, to an extent, on your configuration settings).
That means those users can cause your system to do work,
and, generally, to store data in transit to and from your Onion Service.
In 2014, Jansen et al discovered that this kind of data storage can
[even be used to help deanonymise your service](https://www.freehaven.net/anonbib/cache/sniper14.pdf).

We have now implemented the recommended countermeasure:
Arti can track how much data is stored in its various queues.
When the configured limit is reached,
Arti starts shutting down connections, and discarding data,
until the queued data is below the limit.
We kill the connections with the oldest oustanding data.
This minimises the impact on unrelated, innocent, traffic.

We'll also need this memory limit feature for Arti Relay,
which is currently being developed.

### Configuration

In Arti, the memory quota tracker is controlled
by the [`[system.memory]`](https://gitlab.torproject.org/tpo/core/arti/-/blob/36b074480a9bc4774648cb5e47ff06976f2992be/crates/arti/src/arti-example-config.toml#L457)
configuration subsection in `arti.toml`.
You can enable it by writing something like this:

```
[system]
memory.max = "1 GiB"
```

The feature is compiled in by default.
Setting the limit for the first time requires an Arti restart.
After that, adjusting (or removing) the limit can be done
at runtime.

There is also a `memory.low_water` setting:
When Arti needs to free memory because `max` is exceeded,
it keeps tearing down connections until the usage is below `low_water`.
This [hysteresis](https://en.wikipedia.org/wiki/Hysteresis) helps stop the system oscillating.
The defaualt value of `low_water` is 75% of `max`.

(Note that unlike C Tor's `MaxMemInQueues` setting,
the current default in Arti is *not* to enable a memory limit.
In Arti you must turn on the feature explicitly, by setting `max`.
We hope to get more experience of how it works for users in practice,
before we consider whether to enable a limit by default.)

### Logging

After you've enabled memory quota tracking, you should see Arti print a log message like this:

```
2024-10-31T16:55:55Z  INFO tor_memquota::mtracker: memory quota tracking initialised max=1.00 GiB low_water=768 MiB
```

You can tell if memory reclaim has been triggered:

```
2024-10-31T17:22:19Z  INFO tor_memquota::mtracker::reclaim: memory tracking: 1.86 GiB > 1.00 GiB, reclamation started (target 768 MiB)
...
2024-10-31T17:22:20Z  INFO tor_memquota::mtracker::reclaim: memory tracking reclamation reached: 44.3 KiB (target 768 MiB): complete
```

### Caution: very new code!

This is a very new feature.
There is a lot of complexity behind the scenes,
and by its nature it is difficult to do a full-scale integration test.
It is quite possible that there are bugs!
We'd like to hear your feedback, when you enable this feature.

You can report issues you discover
[in our gitlab](https://gitlab.torproject.org/tpo/core/arti)
(also available via an
[anonymous ticket reporting system](https://anonticket.torproject.org/)).
You can also contact us informally by email, or on irc:
we're in `#tor-dev` on [OFTC](https://www.oftc.net/).

### Thanks to our sponsors

Thanks to
[Zcash Community Grants](https://zcashcommunitygrants.org/)
for their funding,
which enabled the development of this feature,
and of course to our [other sponsors](https://www.torproject.org/about/sponsors/)
for funding the development of Arti.

* [onion-services relays](/category/onion-services-relays)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/arti_1_3_0_memquota/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/arti_1_3_0_memquota/&text=Memory%20quota%20tracking%20%28Onion%20service%20DoS%20resistance%29%20in%20Arti)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/arti_1_3_0_memquota/&text=Memory%20quota%20tracking%20%28Onion%20service%20DoS%20resistance%29%20in%20Arti)
[Bluesky](https://bsky.app/intent/compose?text=Memory%20quota%20tracking%20%28Onion%20service%20DoS%20resistance%29%20in%20Arti%0Ahttps%3A//blog.torproject.org/arti_1_3_0_memquota/)

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