---
title: Announcing Vanguards Support in Arti
url: https://blog.torproject.org/announcing-vanguards-for-arti/
source: Tor Project blog
date: 2024-07-17
fetch_date: 2025-10-06T17:43:26.202943
---

# Announcing Vanguards Support in Arti

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Announcing Vanguards Support in Arti

by [gabi](/author/gabi)
| July 16, 2024

![](/announcing-vanguards-for-arti/lead.png)

As of version 1.2.2, Arti supports [Vanguards](https://spec.torproject.org/vanguards-spec/index.html?highlight=vanguards#tor-vanguards-specification), a defense against guard
discovery attacks targeting onion services and onion service clients. [First introduced in 2018 as an add-on to v3 onion services](https://blog.torproject.org/announcing-vanguards-add-onion-services/), Vanguards serve to mitigate the risk of de-anonymization attacks.

## Why

A guard discovery attack reveals the [guard relays](https://support.torproject.org/about/entry-guards/) of a onion service or
client to the attacker. While this does not, in and of itself, deanonymize the
victim, it does make it easier to launch traffic analysis attacks, which *can*
ultimately lead to deanonymization. See ['From "Onion Not Found" to Guard
Discovery'](https://www.researchgate.net/publication/356421302_From_Onion_Not_Found_to_Guard_Discovery/fulltext/619be24907be5f31b7ac194a/From-Onion-Not-Found-to-Guard-Discovery.pdf?origin=publication_detail) and section VI of ['Trawling for Tor Hidden Services: Detection,
Measurement, Deanonymization'](https://www.ieee-security.org/TC/SP2013/papers/4977a080.pdf) for more on guard discovery attacks.

To defend against this type of attack, Arti now uses additional layers of
guards, called *vanguards*, when building onion service circuits.

Before Vanguards, Arti would build these circuits by randomly selecting the
second and third hops from the set of all relays. Now, the second and third hops
are selected from restricted subsets of relays, called the L2 and L3 vanguard
sets, respectively. By pinning the second and third hops for a period of time,
we make guard discovery attacks [significantly more costly](https://spec.torproject.org/vanguards-spec/vanguards-stats.html) to perform
successfully.

Arti's Vanguards implementation is based on the research behind Tor's [Vanguards
add-on](https://blog.torproject.org/announcing-vanguards-add-onion-services/), and offers similar protections to its [Vanguards component](https://github.com/mikeperry-tor/vanguards/blob/master/README_TECHNICAL.md#the-vanguards-subsystem). The other
experimental defenses from the add-on are not yet implemented in Arti (but they
are on our roadmap!)

## Who is this for?

If you are using Arti to connect to onion services, or if you are running an
Arti onion service, this change affects you. In particular, if you are running
a long-running onion service and would like to harden it against guard
discovery attacks, we recommend you read on. If you are not interested in the
nitty-gritty of the new subsystem, you can skip over to the `Usage` section
below.

## Lite or Full vanguards?

Arti's Vanguards subsystem supports two mutually exclusive modes of operation:

* Lite, for clients and short-lived onion services
* Full, for onion services with high uptimes (longer than one month)

Full vanguards provide better security than lite vanguards, but come with a
performance cost: circuits using full vanguards have an additional hop, and will
therefore have higher latency than those built using lite vanguards.

### Lite vanguards

With lite vanguards, the second hop of every onion service circuit is selected
from the L2 vanguard set. The third hop is selected as before, by randomly
choosing a relay that can serve as a middle relay:

```
     Client hsdir:  C - G - L2 - M - HSDir
     Client intro:  C - G - L2 - M - Intro
     Client rend:   C - G - L2 - Rend
     Service hsdir: S - G - L2 - M - HSDir
     Service intro: S - G - L2 - M - Intro
     Service rend:  S - G - L2 - M - Rend
```

where `L2` is a second-layer vanguard, and `M` is a randomly selected middle
relay.

The L2 vanguard set is ephemeral (it is not preserved across process restarts).

### Full vanguards

In addition to using L2 vanguards, circuits with Full vanguards also use an L3
vanguard as the third hop. Moreover, onion service circuits where the target
might be controlled by an adversary are extended by an additional middle relay,
sampled from the set of all relays:

```
     Client hsdir:  C - G - L2 - L3 - M - HsDir
     Client intro:  C - G - L2 - L3 - M - Intro
     Client rend:   C - G - L2 - L3 - Rend
     Service hsdir: S - G - L2 - L3 - HsDir
     Service intro: S - G - L2 - L3 - Intro
     Service rend:  S - G - L2 - L3 - M - Rend
```

where L2 and L3 are second- and third-layer vanguards, respectively,
and `M` is a randomly selected middle relay.

The L2 and L3 vanguard sets are written to disk, and thus are preserved across
restarts.

### Vanguard lifetimes

The L2 and L3 vanguard sets are built by randomly selecting a fixed number of
relays that have the `Fast`, `Stable`, and `Valid` flags. We select 4 relays for
the L2 set, and 8 for the L3 one.

Each vanguard is assigned a random lifetime from the `max(X, X)` distribution,
where `X` is a uniform random value between the minimum and maximum vanguard
lifetimes specified in the consensus (we use the `max(X, X)` distribution to
introduce a bias towards longer lifetimes). Vanguards are rotated when their
lifetime expires.

The lifetime of an L2 vanguard is between 1 and 12 days, whereas L3 vanguards
have a much shorter lifetime (between 1 and 48 hours). This short lifetime aims
to deter adversaries from attempting to compromise the L3 vanguards: by the time
the attack succeeds, there is a high chance the vanguards will have already been
rotated. In other words, the lifetime was chosen so that the only feasible way
to control the third hop in the victim's circuit is through a Sybil attack. In
contrast, a successful Sybil attack against the second layer would take a very
long time. For more about our threat model, see the [vanguards specification](https://spec.torproject.org/vanguards-spec/full-vanguards.html#threat-model-assumptions-and-goals).

## Relaxed path building restrictions

When vanguards are enabled, we relax some of the path building restrictions that
would otherwise be enforced. For instance, same-family and same-subnet
restrictions do not apply, and the last hop of a circuit is allowed to be the
same as the first.

The relaxed restrictions prevent attackers from, for example, finding out the
guard of a onion service by successively using each relay with the `Guard` flag
as a rendezvous point, and checking which of them the service consistently fails
to connect to.

## Usage

Vanguards are enabled by default in Arti since version 1.2.2. However, a number
of security issues affecting vanguards were discovered in Arti 1.2.2, 1.2.3, and
1.2.4, so we strongly recommend running a version no older than 1.2.5.

By default, Arti uses lite vanguards for all onion service circuits. We
recommend most users stick with the provided defaults. However, if you are
running a **long-lived onion service** (with an uptime exceeding one month), we
recommend using full vanguards instead.

You can enable full vanguards by setting `vanguards.mode` in your [TOML config](https://gitlab.torproject.org/tpo/core/arti/-/blob/9dd06a9c981ee4935c33bca582073c7e96e2d599/crates/arti/src/arti-example-config.toml#L448-462):

```
[vanguards]
mode = "full"
```

or via the command-line, using

```
arti proxy -o=vanguards.mode=full
```

While we do not recommend disabling vanguards, you can do so by setting
`vanguards.mode` to `disabled`.

## Choice of parameters

The vanguard set sizes and the vanguard lifetime bounds are read from the
[consensus](https://spec.torproject.org/param-spec.html#vanguards). Like other consensus parameters, the vanguard parameters can be
overriden in Arti using the [`o...