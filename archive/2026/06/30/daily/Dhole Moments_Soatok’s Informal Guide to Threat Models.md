---
title: Soatok’s Informal Guide to Threat Models
url: https://soatok.blog/2026/06/30/soatoks-informal-guide-to-threat-models/
source: Dhole Moments
date: 2026-06-30
fetch_date: 2026-07-01T06:23:40.682333
---

# Soatok’s Informal Guide to Threat Models

[Skip to the content](#site-content)

Search

[Dhole Moments](https://soatok.blog/)

Software, Security, Cryptography, and Furries

Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Search

Search for:

Close search

Close Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Categories

[Software Security](https://soatok.blog/category/technology/software-security/)

# Soatok’s Informal Guide to Threat Models

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [June 30, 2026](https://soatok.blog/2026/06/30/soatoks-informal-guide-to-threat-models/)

![Soatok's Informal Guide to Threat Models](https://i0.wp.com/soatok.blog/wp-content/uploads/2026/06/BlogHeader-2026-ThreatModel-Guide.png?fit=1200%2C675&ssl=1)

After a long day of exhausting conversations about [Hybrid Post-Quantum Cryptography](https://soatok.blog/2026/04/13/hybrid-constructions-the-post-quantum-safety-blanket/), random jackasses trying to play gotcha with endpoint attacks against end-to-end encrypted messaging apps, and message board discussions in the wake of dumb politicians pushing more “age verification” bullshit on us all, it’s become abundantly clear to me that the phrase “threat model” is a foreign concept to most people.

Except, y’know, as a buzzword.

![Comic. Panel 1: Person in a DEFCON shirt says "threat model". Panel 2: Soatok (blue dhole) has his eyes glow red, like an activated sleeper agent. Panel 3: The blue dhole is in the air ominously behind the "threat model" utterer with a bat labeled "STFU".](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/08/embyr-defcon29.png?resize=768%2C355&ssl=1)

Art by [Embyr](https://sfw.furaffinity.net/user/embyr7).

For context, this was commissioned during the era of anti-vaccine losers claiming to “do their own research” briefly co-opting the word “threat model” as a buzz word.

I just still find it kind of funny even without this context.

> To be up front: If you’re here looking for an academic resource with over 100 citations on how to write a formal threat model document for your new startup which involves multiple blockchains, this probably isn’t the gay furry blog for you. Maybe start with [STRIDE](https://en.wikipedia.org/wiki/STRIDE_model) and [system theory](https://www.ul.com/sis/blog/introduction-to-stamp-stpa-and-cast).
>
> But if you’re looking to build an intuition for what questions a good threat model should answer, and you’re starting from zero, you’re probably in the right place.

So let’s talk about threat modeling.

## Threat Modeling For Neophytes

![Purple protogen (Neophyte) smiling.](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/07/neophyte-happy.png?resize=350%2C512&ssl=1)

Their name is Neophyte, if you didn’t get the joke.

Art: [Harubaki](https://harubaki.carrd.co/)

At a high level, don’t overthink this too much.

While a threat model is a formal cybersecurity process that some infosec folks actually specialize in, you can run informal threat models in the design and architecture phases of developing a new product or service and no one can stop you. You might just end up with a better result.

A threat model should, at minimum, answer these basic questions:

1. **What are we even protecting to begin with?**
   * If you can’t answer this, you have a lot of ground work to do.
2. **Who/what wants to harm what we’re protecting?**
   * Hackers, activists, cyber-stalkers, social media harassment networks
   * Natural disasters / bad karma
   * Underpaid and overworked employees who get fed up
   * Idiotic legislatures paid by large corporate lobbyists to pass stupid laws that hurt everyone
   * Nation State Adversaries!!!!1oneon
3. **How might (2) attack (1)?**
   * Attack scenarios go here
   * Murphy’s Law goes here
4. **What will we do to prevent (3) from happening?**
   * Murphy’s Law also goes here!

And, like, okay. If you can check those off, you can call your document a threat model in some sense.

However, this is often useless in practice because some crucial details are omitted.

5. **How are the assets (1) related / connected?**
   * [Think in graphs, not lists](https://github.com/JohnLaTwC/Shared/blob/master/Defenders%20think%20in%20lists.%20Attackers%20think%20in%20graphs.%20As%20long%20as%20this%20is%20true%2C%20attackers%20win.md).
   * Not all targets are equal value.
6. **What assumptions are we making, especially with (4) and (5)?**
   * I’ll say more about this below.
7. **What threats are we deliberately *not* addressing?**
   * You literally cannot address every possible attack that any person will ever imagine in the unforeseeable future, so don’t pretend to.

Too many people take assumptions (6) for granted, ironically, but it’s **incredibly important** to be as clear about what your assumptions are.

If one of your assumptions is wrong, then your model is incomplete (at best), or your list of accepted risks (7) needs to be reconsidered.

For example: The [Invisible Salamanders attack](https://soatok.blog/2024/09/10/invisible-salamanders-are-not-what-you-think/) breaks abuse reporting in some end-to-end encrypted messaging designs, but only if you introduce abuse reporting.

The attack is possible because one of the assumptions that went into the AEAD schemes in question (AES-GCM, ChaCha20-Poly1305) is that there is only one valid key for a given message. The second you introduce multiple valid keys for a given message (or [confused deputies](https://scottarc.blog/2022/10/17/lucid-multi-key-deputies-require-commitment/) for that matter), you’ve gone outside the security guarantees of your algorithm–which, as an attacker, makes for [a fun trick](https://github.com/soatok/gcm-exploit).

Being clear about your assumptions allows you to identify your own unknown unknowns. You don’t have to be perfect.

In fact: Threat models are supposed to be living documents, not point-in-time snapshots. Update them whenever you deem appropriate.

![High Paw (high five) sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/09/soatoktelegrams2020-08.png?resize=512%2C512&ssl=1)

Art: [CMYKat](https://cmykatgraphics.carrd.co/)

### How to Get Started

If you’re looking to do threat modeling professionally, you probably want to read the [Threat Modeling Manifesto](https://www.threatmodelingmanifesto.org/). Here’s how I approach it.

First, write down the 7 items above in a format that you can vaguely copy and paste rapidly. You’re going to need it.

Next, map out (on a large piece of graph paper, preferably–or the digital equivalent) the components of the system you’re designing or analyzing. If any widget directly talks to, depends on, or interacts with another widget, you need that relationship drawn in whatever convention is most useful to you.

Once this is setup, you want to draw a box around the entire graph, and then pretend you’re playing Fortnite: Every so often, the box gets smaller and focused more on each individual component. Each iteration, note all the inputs and outputs to each component, and try to answer as many of the 7 items as you can.

Repeat until you’ve drilled down as far as your abstraction allows you, then brainstorm what assumptions you have about the layers you *aren’t* drilling deeper into.

![Clipboard Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/04/soatok-telegrams-wave-3-commission-11.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

What you’re doing is starting at the highest level and working your way down into more specific pieces.

Your database probably doesn’t depend on the security of X25519 the same way that your load balancer does. But your database also probably shouldn’t have an RSS feed built into it either. Take note of inappropriate relationships and aim to sever them if you c...