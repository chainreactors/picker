---
title: Basic Infrastructure
url: https://www.tbray.org/ongoing/When/202x/2024/08/13/Basic-Infrastructure
source: ongoing by Tim Bray
date: 2024-08-14
fetch_date: 2025-10-06T18:02:25.278589
---

# Basic Infrastructure

# Basic Infrastructure

Search

Recently, I was looking at the infrastructure bills for our
[CoSocial](https://cosocial.ca) co-op member-owned Mastodon instance, mostly Digital Ocean and a bit of AWS. They seemed
too high for what we’re getting. Which makes me think about the kind of infrastructure that a decentralized social network
needs, and how to get it.

I worked at AWS for 5½ years and part of my job was explaining why public-cloud infrastructure is a good idea. I had no
trouble doing that because, for the people who are using it, it *was* (and is) a good idea. The public cloud offers a quality of
service, measured by performance, security, and durability, that most customers couldn’t build by themselves.
One way to put it is this: If you experience problems in those areas, they are much more likely to be problems in your software
than in the cloud infrastructure.

Of course, providing this level of service costs billions in capex and salaries for thousands of expensive senior
engineers. So you can expect your monthly cloud-services bill to be substantial.

But what if… ·
What if you don’t need that quality of service? What if an hour of downtime now and then was an irritant but not an
existential problem? What if you were OK with occasionally needing to restore data from backup? What if everything on your
server was public data and not interesting to bad actors?

Put another way, what if you were running a small-to-medium Fediverse instance?

If it goes offline occasionally, nobody’s life is damaged much. And, while I grant that this is not well-understood, at this
point in time everything on Fedi should be considered public, and I don’t think that’ll change even when we get end-to-end
encryption because that data of course isn’t plain text. Here is what you care about:

1. Members’ posts don’t get permanently lost.
2. You don’t want bad people hijacking your members’ accounts and posting damaging stuff.
3. You don’t want to provision and monitor a relational database.

“Basic”? ·
So, what I want for decentralized social media is computers and storage “in the cloud”, as in I don’t want to have to visit them
physically. But I don’t need them to be very fast or to be any more reliable than modern server and disk hardware generally are. I do
need some sort of effective backup/restore facility, and I want good solid modern authentication.

And, of course, I want this to be a whole lot cheaper than the “enterprise”-facing public cloud. Because I’m not an
enterprise.

(I think I still need a CDN. But that’s OK because they’re commoditized and competitive these days.)

I know this is achievable. What I don’t know is who might want to offer this kind of infrastructure. I think some of it is
already out there, but you have to be pretty savvy about knowing who the vendors are and their product ranges and strengths and
weaknesses.

Maybe we don’t need any new products, just a new product category, so people like me know which products to look at.

How about “Basic Infrastructure”?

---

**Updated: 2024/08/13**

---

## Contributions

Comment feed for ongoing:[![Comments feed](/ongoing/Feed.png)](/ongoing/comments.atom)

From: [Andrew Reilly](http://) (Aug 13 2024, at 20:46)

What does the average and peak data rates look like for your fediverse instance?

From a 10000-foot perspective, it seems not a whole lot different from pre-internet BBS systems or nntp-era usenet servers, and they managed fine on 16- or 32-bit computers (singular) in a basement with a couple of 1200baud modems. Modern domestic internet in many major capitals is gigabit and uncapped these days, and cheap hardware is so many orders of magnitude bigger and faster than the BBS systems that it's almost silly to compare them, and yet they're doing about the same thing.

WhatsApp made it to its first half-billion subscribers with a single-image FreeBSD box connected to the backbone with a couple of off-the-shelf network cards.

All I'm suggesting is that a single decent modern server in a colo ought to get the job done, especially if you're prepared to spring for CDN fronting.

*[[link](#c1723607193.469357)]*

From: [Chris Swan](https://blog.thestateofme.com/) (Aug 13 2024, at 22:14)

Welcome to the infrastructure (as a service) ghetto. Let <https://lowendbox.com> be your guide for what's on offer...

The main difference you'll notice is bandwidth pricing. Stuff that would cost hundreds a month in egress on EC2 or S3 can be done for a handful of dollars.

FWIW AWS Lightsail bundles a bunch of EC2 stuff to give VPS like pricing, but the potential overage charges have always scared me off. Also individual hyperscaler instances are generally less reliable than skid row VPS (though the failure modes are very different).

*[[link](#c1723612477.150462)]*

From: [Wes Felter](https://x.com/wmf) (Aug 13 2024, at 22:16)

Digital Ocean is already a tier below AWS/GCP/Azure and Hetzner/OVH seem to be another tier below DO. (I find it curious that European hosting is cheaper than US; I thought everything was more expensive there.)

Besides the cost of infrastructure, cloud-native high availability practices like Paxos/Raft voting and database replication are great at high scale but really expensive at low scale. Unfortunately there's little discussion of what we might call "medium availability" practices (which would probably still be more reliable than 1990s HA).

In my opinion the real reason your bill is so high is that Mastodon is grossly inefficient. It probably uses 100x more resources than necessary but I guess rearchitecting it is a coordination problem; it would cost a lot upfront but save a lot over time.

*[[link](#c1723612573.698355)]*

From: [Dan](https://www.sidhe.org/blog/) (Aug 14 2024, at 12:51)

The economics and support dynamics of something like this are weird and I suspect don't lend themselves to being sold. If you sell the reliable-ish services, the people who \*said\* they were OK with flaky will inevitably turn out not to be actually OK with it and complain loudly. At which point you have a support burden (which increases the price) and then the services get made more reliable (which increases the price).

I half want a way to pop a box in my study and a few other people's studies/closets/basements, set up across-the-internet mirroring, and only open the thing up via an actually-high-availability CDN. (Which I am now wondering if that could be done via Tailscale and some cleverness, though even then it still leaves the "that box is actually in my living room" problem)

*[[link](#c1723665078.147999)]*

From: [Rob Sayre](http://) (Aug 17 2024, at 13:41)

Use Hetzner and put Cloudflare in front. Should be free or close.

*[[link](#c1723927299.438217)]*

[ongoing](https://www.tbray.org/ongoing/)

[What this is](/ongoing/WhatItIs) ·
[![Subscribe to ongoing](/ongoing/Feed.png "Subscribe to ongoing")](/ongoing/ongoing.atom)
[Truth](/ongoing/Truth) ·
[Biz](/ongoing/Biz) ·
[Tech](/ongoing/Tech)

[author](/ongoing/misc/Tim) ·
[Dad](http://www.textuality.com/BillBray/)
[colophon](/ongoing/misc/Colophon) ·
[rights](/ongoing/misc/Copyright)

[![picture of the day](/ongoing/potd.png)](/ongoing/goto-potd/)

[August](/ongoing/When/202x/2024/08/) [13](/ongoing/When/202x/2024/08/13/), [2024](/ongoing/When/202x/2024/)
 · [Technology](/ongoing/What/Technology) (90 fragments)

 · · [Cloud](/ongoing/What/Technology/Cloud) (26 more)

By [Tim Bray](/ongoing/misc/Tim).

The opinions expressed here
are my own, and no other party
necessarily agrees with them.

A full disclosure of my
professional interests is
on the [author](/ongoing/misc/Tim) page.

I’m on [Mastodon](https://cosocial.ca/%40timbray)!