---
title: Happy Families: new certificates for faster and easier relay management
url: https://blog.torproject.org/happy-families/
source: Tor Project blog
date: 2025-05-22
fetch_date: 2025-10-06T22:32:06.442376
---

# Happy Families: new certificates for faster and easier relay management

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Happy Families: new certificates for faster and easier relay management

by [nickm](/author/nickm)
| May 21, 2025

![](/static/images/lead.png)

Frequently relay operators (individuals or organization)
want to operate more than one relay.
In order to advertise this fact, they
declare that their relays belong to a "Relay Family" together.

Within the Tor protocol,
Relay Families help make sure that an honest relay operator
is never in a position to appear in the same circuit or observe two points of a circuit
to mount a traffic correlation attack.[1](#fn-relaxing)

Outside of its role in the Tor protocol,
Relay Families help Tor's [Network Health Team](https://gitlab.torproject.org/tpo/network-health/team) to keep an eye on
how many relays are operated by the same people,
and to diagnose issues with relay deployments.
Families give honest operators a transparent way to tell the world,
"I'm not running a [Sybil attack](https://www.freehaven.net/anonbib/cache/sybil.pdf);
I'm being transparent with my relays."

## So what's the problem?

When we added relay families
[back](https://gitlab.torproject.org/tpo/core/tor/-/commit/959199340a8b777f13a6b5ce921d9d8eab9510e0)
[in](https://gitlab.torproject.org/tpo/core/tor/-/commit/7fa5d224d4469de9ff69f41a245ada9b329a2840)
[2004](https://gitlab.torproject.org/tpo/core/tor/-/commit/ff38cc06e1f7466ed7c6a3524d9817e1c48a0de2),
we made the implementation simple:
Two relays are considered to belong to the same family
if and only if
each one lists the other one in its list of family members.
So if relay A lists relay B, and vice versa,
they are treated as belonging to a family.
But if only one lists the other as belonging to its family,
then they aren't in a family together.

(Given the role of families in routing decisions,
it would be Bad if an attacker's relay
could put itself in a "fake family"
containing all the relays that *aren't* administered by the attacker!)

But this means that in order to represent a relay family with N members,
each member needs to list N-1 other members,
requiring a total of O(N2) listed relays in order to represent the
whole family.
As the Tor network grows, so do family sizes.
Right now, something like 85% of the total space used for microdescriptors
in a full Tor directory is taken up by family declarations!
(Even after compression, it's still 32%.)

What's more, declaring families is annoying.
When a relay family adds a new member,
*every relay in the family* needs to be reconfigured
to list that member as part of its family.
Tools like [ansible-relayor](https://github.com/nusenu/ansible-relayor)
make this easier to do, but it's still harder than it needs to be.

## What's the solution? Family certificates!

Instead of listing one another to indicate that they belong to the same family, relays should use cryptography!

(Okay, \_more\_ cryptography.)

In place of a list of other relays in the same family,
each relay should carry a "family certificate" that proves
its membership in a family.
The family certificate is signed with a private key that identifies the
family:
only relays signed with the same key are considered to belong to the same
family.

Now, instead of O(N2) listed relays,
each family just needs to list one signed certificate. This will make microdescriptors smaller and decrease download sizes.

The full solution was specified first in [proposal 242](https://spec.torproject.org/proposals/242-better-families.html)
and later extended in [proposal 321](https://spec.torproject.org/proposals/321-happy-families.html).
This solution is now implemented in [Arti](https://arti.torproject.org/)
and in the 0.4.9.x (alpha) versions of the [C Tor implementation](https://gitlab.torproject.org/tpo/core/tor).

If you're running a relay family,
see [the community portal](https://community.torproject.org/relay/setup/post-install/family-ids/)
for information about how to deploy it with 0.4.9.x.

## So, when will we see the full benefits?

Old Tor clients don't understand family certificates.
That means that relays are going to have to keep advertising families
in the old way
until we can be sure that nearly all clients have upgraded.

In the coming months, after Tor 0.4.9.x is stable,
please expect us to be encouraging as many clients and relays to upgrade. The faster everyone moves, the sooner directory authorities can retire the old format. For now, you can help test the feature with the next alpha release.

## What else will shrink directories in 0.4.9.x?

To make microdescriptors even smaller,
and thereby lower download sizes,
Tor 0.4.9.x is going to
[stop listing obsolete RSA "TAP keys" in them](https://spec.torproject.org/proposals/350-remove-tap.html).
These keys account for yet more of the microdescriptor sizes,
but nothing uses them any more!

Once long family lists *and* TAP keys are gone,
we estimate that the aggregate size of compressed microdescriptors
will be something like 25% of their current size.
Since microdescriptors are currently around 70% of the directory information
needed to bootstrap a client
(the rest is a consensus document and a set of certificates),
the bandwidth to bootstrap a fresh connection to the network
will be something around 50% of what it is now.

## And what might grow directories again?

We're [working on designs](https://spec.torproject.org/proposals/355-revisiting-pq.html) to make Tor's cryptography stronger
against [quantum computation](https://en.wikipedia.org/wiki/Shor%27s_algorithm).
Although cryptographically relevant quantum computers (CRQCs)
are still a thing of the future[2](#fn-future),
we want to make sure that Tor's encryption algorithms will be strong enough
to resist them,
in order to defeat any adversary who records traffic today
in hopes of decrypting it later, once the future arrives.
(TLS is going through a [similar transition](https://openssl-library.org/post/2025-04-08-openssl-35-final-release/).)

Fortunately, we can make these cryptographic improvements
without any significant cost in directory bandwidth!

But eventually, when CRQCs are closer,
we'll also need to resist *active* attacks,
by attackers who can use a CRQC *online* to impersonate a relay.
To do this, we may need to distribute *more*
information in the directories again:
current [post-quantum key encapsulation schemes](https://en.wikipedia.org/wiki/Kyber)
use longer keys than the ones we use today.
So some of the space that we're freeing now may eventually
be needed for other work.

## Thanks

Thanks to everybody who's worked to make any version of this proposal
better, and/or reported bugs and issues with the code!

Also, thanks to all the individual donors who made this work possible.
This project wasn't funded by any restricted grant or contract;
only your donations made it possible.

[![Donate Button](/happy-families/button-large-black.png)](https://torproject.org/donate/donate-bp2-sc2025)

---

1. But surprisingly enough, some research suggests that this
   requirement may be *bad* for security if rigidly enforced!
   We're looking into this, and [developing alternative designs](https://spec.torproject.org/proposals/354-relaxed-restrictions.html).[↩](#fnref-relaxing)
2. How far in the future? Estimates vary! Still, it pays to be cautious.[↩](#fnref-future)

* [announcements](/category/announcements)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/happy-families/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/happy-families/&text=Relay%20Families%20are%20Tor%E2%80%99s%20way%20of%20grouping%20together%20relays%20run%20by%20the%20same%20operator%2C%20providing%20...