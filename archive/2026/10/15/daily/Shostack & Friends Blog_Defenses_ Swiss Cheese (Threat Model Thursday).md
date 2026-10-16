---
title: Defenses: Swiss Cheese (Threat Model Thursday)
url: https://shostack.org/blog/cybersecurity-defenses-a-swiss-cheese-model/
source: Shostack & Friends Blog
date: 2026-10-15
fetch_date: 2026-10-16T06:36:39.979579
---

# Defenses: Swiss Cheese (Threat Model Thursday)

[Skip to main content](#main-content)

[![Shostack and Associates logo, click for Homepage](/img/Shostack-logo-white.png)](/)

* [About](/about)
  + [Shostack + Associates](/about)
  + [Adam Shostack](/about/adam)
  + [Our Partners](/partners)
* [Services](/training)
  + [Training](/training)
  + [Accelerator](/secure-design-accelerator)
  + [Speaking Requests](/speaking)
  + [Consulting](/consulting)
* [Resources](/resources)
  + [Overview](/resources)
  + [Threat Modeling](/resources/threat-modeling)
  + [Books](/books)
  + [Games](/tm-games)
  + [Cyber Public Health](/resources/cyber-public-health)
  + [Lessons Learned](/resources/lessons)
  + [Videos](/resources/videos)
  + [Whitepapers](/resources/whitepapers)
* [Blog](/blog)
* [Contact](/contact)

1. [Shostack + Associates](/)
2. [Blog](/blog)
3. Defenses: Swiss Cheese (Threat Model Thursday)

Shostack + Friends Blog

# Defenses: Swiss Cheese (Threat Model Thursday)

Adam Shostack, Shostack + Associates

A “Swiss cheese model” of defenses helps engineers organize defenses and think broadly.
![A Swiss cheese model of cybersecurity](/images/blog/img/2026/swiss-cheese-cybersecurity-1664w.png)

In this [Threat Model Thursday](https://shostack.org/blog/category/threat-model-thursday) post about the [new edition of Threat
Modeling](https://amzn.to/4urxcBJ), I want to talk about the Defenses part of the book, and
a key metaphor (“the Swiss Cheese Model”) that organizes it.

## Modeling defenses

How to answer the question of “what are we going to do about it” is
the most heavily re-organized part of the book. We can take broad
strategies from risk management: eliminate, mitigate, transfer or
accept. We can take strategic goals from NIST CSF and protect,
detect or respond. (The goal of identify overlaps with the
question of ‘what are we working on,’ and most recovery work is
covered in business continuity/disaster recovery planning. Ideally
that’s informed by threat models that show the systems in use, but
that doesn’t strongly influence threat modeling programs.) The
first edition text focused heavily on feature-like techniques
available to developers. That didn’t meet my goals for the second
edition.

At the strategic end of security engineering, threat modeling
should consider a broad set of defensive possibilities, and that
meant enumerating and explaining those. This led to the discovery
that most of how we’ve talked about defenses has been narrow,
tactical, and implicit. It’s implicit because where we are in a
project *and* in an ecosystem controls what defenses we
pick. It even controls our language, in the use of the term
“controls” as a near-synonym for defenses. And “controls” means a
few different things: it means the products we bolt on. It means
the operational procedures we apply, and sometimes even the
governance structures that overlay both. And if you’re, say, an
Amazon customer, deploying other people’s products (say, SAP and
Hubspot) on someone else’s cloud, those realities dominate your
defensive choices.

What’s more, the way people talk about defenses doesn’t usually
engage with those realities. (“A fish has no word for water.”) We
all accept the narrow and tactical way our products can be
customized, and while LLMs are changing that a little, most
organizations no longer customize even their open source packages,
wary of the maintenance costs.

All of this is modeling work. What do we include? What do we
abstract? How does a model help us or hinder us? I’ve been exploring how we talk about these, most publicly
with talks like [Layered Defenses: A New Hope](https://shostack.org/blog/layered-defenses-bsides-seattle-2026/) at BSides
Seattle, or a “mastermind” session at [ThreatModCon
Vienna](https://www.threatmodcon.com/agenda/layering-defenses-a-new-hope), because there’s no perfect answer.

## Swiss Cheese Models in Cybersecurity

James Reason’s Swiss Cheese model presents safety as a stack of
slices of Swiss cheese. Each bit of cheese has some holes, and
each hole lets problems proceed to the next layer. If the holes
align, a hazard event becomes an incident. These models have been
applied to cybersecurity. For example, EMIsoft presented a [nice
one](https://www.emsisoft.com/en/blog/38186/how-we-use-the-swiss-cheese-model-to-prevent-malware-infections/) in 2024 and there are others. The book’s approach is broader
than the others I’ve seen, and organizes defenses into:

* Defensive design
* Defensive coding
* Security features
* Products
* Operations

The cheese is drawn carefully (well, except the missing
holes in this draft figure!) The design and features have large gaps, and
defensive coding lets many bugs through. Products and operations are stacks of
cheese, representing the many layers within each. The model is shown without
arrows to focus your attention on the presentation of the defensive layers.

The technically strongest defenses tend to be at the start of the
list: defensive design and coding. As you get to security
features, you're often making tradeoffs. And when you get to
products and operations, you're often deferring security to
others, who may do it better or worse than you. That’s often
unavoidable: you can’t tell a customer to switch from Okta to
Ping, or vice versa. They get to select their defensive products,
and what’s more, unless you compete with those, those
undifferentiated features will get less attention and care from
you. So it’s a reasonable choice to defer to products, and
similarly, there are defenses (such as applying patches or reading
logs)
that are inevitably operational.

This model is intended to encourage threat modeling practitioners to
consider a broad set of possibilities. Circumstances can obviously
preclude many of those choices, and there’s a section on threat modeling
unalterable components.

So as you can see, Chapter 9, Technical Defenses, is scoped and
imagined very differently from the previous edition, and it leads
off a re-conceptualized Part IV: What Are We Going to Do About It?
The Part continues with Chapter 10, Defense Project Management,
Chapter 11, Risk Manage What Remains, and closes with Chapter 12,
Did We Do a Good Job?

This new organization is much clearer, and starts where I believe
engineers ought to start, which is technical defenses, and those
defenses need to be project managed. That’s the core of the work,
and only as that work isn’t feasible do we consider risk
management.

This aligns with [new CRA guidance](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation) from the European Union: “Manufacturers also need to implement appropriate
measures to address those risks,” and “the requirement that the product with digital elements placed on the market
ensures an appropriate level of cybersecurity based on the risks.”
(Paras 156/157) Those require design isolation, defensive coding, and
security features.

That perspective may be new to many
organizations, but threat modeling is the way to find more
options, and find them sooner. There’s no single right answer for
all security problems, and this new part makes the choices —
design, code, feature, product, operation — much more
explicit, and also considers tradeoffs... but this post is long so
we’ll talk about those next week.

Image: Wiley. This post drew my attention to
the fact that the final slices of cheese had no holes, an
excellent design decision, albeit one which breaks the metaphor,
and should be fixed by the time the book is printed.

Originally published by Adam on 15 Oct 2026

Categories:
  [books](/blog/category/books)
  [security](/blog/category/security)
  [threat modeling](/blog/category/threat-modeling)
  [threat model thursday](/blog/category/threat-model-thursday)

## Our Favorite Content

[General threat modeling posts](/blog/category/threat-modeling)

[The Security Principles of Saltzer and Schroeder, illustrated with Star Wars](/blog/the-security-principles-of...