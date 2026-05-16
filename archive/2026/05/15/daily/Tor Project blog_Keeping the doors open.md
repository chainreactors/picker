---
title: Keeping the doors open
url: https://blog.torproject.org/keeping-the-doors-open-unredacted/
source: Tor Project blog
date: 2026-05-15
fetch_date: 2026-05-16T05:15:41.082419
---

# Keeping the doors open

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Keeping the doors open

by [Unredacted.org](/author/unredacted.org)
| May 15, 2026

![](/keeping-the-doors-open-unredacted/lead.png)

*This guest post is part of a spotlight series on the organizations defending the free internet.*

A user in China once said this about our work:

> *"You have helped many many people to overcome the great firewall.
> Without your help, I would be in the totally darkness trap and being brain-washed."*

**We don't hear from the people who use our services very often. Most of them can't or don't feel that they can safely send a message. When one comes through, it's a reminder of what's actually at stake.**

We're [Unredacted](https://unredacted.org/), a US-based 501(c)(3) non-profit. We build and operate Internet infrastructure that helps people reach the open Internet and protect their right to privacy. We do this by operating a network of over 300 servers around the world. We're a way through when the front door is locked, and a place to communicate when the public square isn't safe. Most of the work is invisible: datacenter work, hardware, automation, open source software, bandwidth, abuse queues, monitoring alerts, and the late nights spent keeping all of it online.

What we do falls into three areas. Censorship Evasion is where Unredacted Door lives, our umbrella for the services designed to route around blocking. Secure Infrastructure is where we run things like [XMPP.is](https://xmpp.is/) and our [Matrix homeserver](https://unredacted.org/services/si/matrix/), and other free services built with security and privacy in mind. Unredacted Education is the writing and documentation side: guides and explainers for the people who want to understand the work and replicate it. Alongside those, [Unredacted Labs](https://unredacted.org/blog/2025/05/unredacted-labs/) is where we experiment with infrastructure ideas that aren't quite production-ready. GreenWare is one of those, our effort to run real network capacity on hardware that doesn't burn a lot of power.

## Unredacted Door

The name is literal. When the entrance to the open Internet gets walled off, people need another way in.

Unredacted Door brings together several of our circumvention services: FreeSocks, messaging proxies for Signal and Telegram, Tor bridges, and Snowflake proxies. In a recent 30-day window, these services carried nearly 300 TiB of traffic for tens of thousands of people routing around censorship in their countries. That's roughly the equivalent of bandwidth to stream tens of thousands of hours of 4K video. Demand isn't slowing, and we need to continue building more. Every new filter, every new law, every "for your safety" rollout sends more people looking for a route the censors haven't found yet.

The largest piece of Unredacted Door is [FreeSocks](https://freesocks.org/): free proxies for people in places where censorship is severe. If you've never run into one, a proxy is a relay point. Your app doesn't talk directly to the blocked service. It talks to a server that carries the connection past whatever filters are sitting between you and the wider Internet. FreeSocks is built to make that relay quietly unremarkable, which is exactly the trait a standard VPN tends to lack. A VPN advertises itself. There's a known endpoint, a known handshake, an obvious shape on the wire. Censors are very good at blocking things they can recognize.

No single tool covers every situation. Tor Browser gives you strong privacy and anonymity for browsing. Snowflake helps people reach Tor when access to the network itself is blocked. FreeSocks proxies push specific traffic through a route that's harder to spot. People living under censorship usually need a few of these on hand, because no single door stays open forever.

That's why we're putting serious work into the next version of FreeSocks (v2). It uses Xray - a powerful and versatile traffic-routing engine, which can make proxy traffic look more like ordinary web traffic bundled with our open source [control plane](https://github.com/unredacted/freesocks-control-plane) that allows us to rotate endpoints automatically when censors find and block a server. The less a user has to fiddle with their setup while they're already under pressure, the better.

## GreenWare: sustainable infrastructure, literally

Tor relays, bridges, proxies, and more. They run on hardware in datacenters, and that hardware has a real footprint: financial, operational, and environmental. If we want privacy infrastructure to last, we have to ask what's actually sustainable to operate.

[GreenWare](https://unredacted.org/blog/2025/05/unredacted-labs/#greenware) is our attempt to shrink that footprint without shrinking what we can carry on it. The premise is straightforward: most Tor relay traffic doesn't need a server that draws power like a space heater. A relay needs a steady network, predictable CPU, and enough memory to hold its state. That's a workload a single-board computer can handle, if the chassis around it is built to take it seriously.

We started with Raspberry Pi 5 boards powered over PoE, fed entirely through their network cables. The idea worked. A typical server in a datacenter draws as much power as a small space heater. A Pi draws less than a lightbulb. But the first generation had ceilings. Density wasn't where we wanted it, and a few of the supporting components weren't built for the hours we were putting on them.

So we run two deployments in parallel now. The first is a 1U chassis with 20 ComputeBlade modules stacked into it. We deployed all 20 in our datacenter and moved a chunk of our Tor exit relays onto them. That chassis pulls a little over 100W under load, roughly what an old incandescent bulb burns. The second is a custom Raspberry Pi chassis we designed after the ComputeBlade work taught us what we actually wanted in the field. Both are live, and as of writing all 123 of our Tor exit relays run on this combined infrastructure, drawing roughly 400W in total. As time goes on, we'll have more to say about the chassis design and the project as it matures.

The Tor network runs on people and organizations willing to operate infrastructure for it. Exits are the hardest part of that job. They need bandwidth, maintenance, abuse handling, legal nerve, and money. If we can drop the cost and the power required to run real exit capacity, more people can take on a piece of the work and diversify and grow the network.

Our longer-term ambition is to keep pushing on efficient hardware, carbon tracking, and eventually renewable-powered micro points of presence. We'd be more than glad to partner with organizations and companies that want to see this grow.

The open Internet is kept open by many people and organizations investing energy, time, and effort: The [researchers measuring censorship](https://blog.torproject.org/Defending-the-right-to-know/), the [relay operators providing bandwidth](https://blog.torproject.org/exploring-stateless-relays/), and the communities that refuse to leave one another behind. At Unredacted, our part is building and maintaining the routes people may need when the obvious ones disappear.

* [community](/category/community)
* [partners](/category/partners)
* [human rights](/category/human-rights)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/keeping-the-doors-open-unredacted/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/keeping-the-doors-open-unredacted/&text=Anti-censorship%20tools%20are%20only%20as%20powerful%20as%20their%20ability%20to%20keep%20running.%20When%20the%20door%20to%20the%20open%20internet%20gets%20slammed%20s...