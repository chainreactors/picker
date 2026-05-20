---
title: HIPAA Updates and Threat Models
url: https://shostack.org/blog/hipaa-nprm-threat-modeling/
source: Shostack & Friends Blog
date: 2026-05-19
fetch_date: 2026-05-20T06:03:38.327735
---

# HIPAA Updates and Threat Models

[Skip to main content](#main-content)

[![Shostack and Associates logo, click for Homepage](/img/Shostack-logo-white.png)](/)

* [About](/about)
  + [Shostack + Associates](/about)
  + [Adam Shostack](/about/adam)
  + [Our Partners](/partners)
* [Services](/training)
  + [Training](/training)
  + [Accelerator](/secure-design-accelerator)
  + [Expert Witness](/expert-witness)
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
2. [Blog](/blog/)
3. HIPAA Updates and Threat Models

Shostack + Friends Blog

# HIPAA Updates and Threat Models

HIPAA reform seems to lead to published threat models, and that’s going to be a hard change.
![Devils, in the details](/images/blog/img/2026/hipaa-devils-in-the-details-1000w.png)

The Department of Health and Human Services is working on an
upgrade to HIPAA security rules. The update will be complicated
and contentious; there’s strong arguments for immediate
strengthening of the rules, and there’s a strong argument that
most hospitals can’t afford the modernization work. I’m glad that
other people need to figure it out.

However, I did want to call out one element, which Ty Greenhalgh
spotlights in his [HIPAA Overhaul: Preparing for the
HIPAA Security Rule NPRM Finalization](https://www.linkedin.com/pulse/hipaa-overhaul-preparing-security-rule-nprm-ty-greenhalgh-ekaoe/?trackingId=%2Fw7J%2FN%2BR0n%2BSfMkDVaFXng%3D%3D) on Linkedin:
> “This requires organizations to map not just the primary software, but
> the underlying APIs, cloud storage buckets, and third-party code
> libraries that support it. The hearing participants noted that this
> level of transparency is often unavailable to the healthcare provider,
> as vendors frequently treat these sub-system architectures as
> proprietary information. There is a strong push from the industry to
> require Business Associates and software vendors to provide a Software
> Bill of Materials (SBOM) to help hospitals meet this mapping
> requirement.”

## Future state

They’re going to need to
start publishing — or at least sharing
threat models.

Having already addressed that the future state won’t be the current
state, we can disregard that “this level of transparency is often
unavailable...” and note: this seems a lot like HHS will be
requiring vendors to provide threat models. In contrast to the
industry push, SBOMs may be necessary, but they’re not sufficient
to understand architecture. SBOMs don’t tell you anything about the *arrangement*
or architecture of a system.

For that, they’re going to need to start publishing, or at least
sharing threat models. Last year, Loren Kohnfelder and I published
a paper on exactly this topic: [Publish Your Threat Model!](https://arxiv.org/abs/2511.08295)
(A [blog-length discussion is
here](/blog/publish-your-threat-model/).)

My take is that requiring threat models will be a long term good,
and the transition will be a challenge.

## The challenge: Medical software makers

Many medical software makers can’t publish or even share a threat model, because they don’t have them.

The first problem is that many medical software makers are where
device makers were in 2014, and for many of them their threat
models really will be “roadmaps for attackers.” And so in the
short to medium term, the medical software maker threat models will likely be shared
under NDA, rather than published. That’s
a scandal, and it doesn’t need to be that way. For example, recently, Andrew Nesbitt, in his post [Not a Security Issue](https://nesbitt.io/2026/05/12/not-a-security-issue.html),
discovered that roughly 500 open source projects already publish
their threat models. If open source projects can do it, so can the
major makers of medical software.

In many cases, many medical software makers can’t publish or even
share a threat model, because they don’t have them. Creating
threat models for
existing software will be both daunting and depressing.

The daunting part is a combination of the many shops where
no one understands how it works anymore, and that’s magnified by a
perception that the threat model needs to go deep. Going
super-deep isn’t usually a requirement because older software
tends to lack boundaries, and so highly abstract models may be as
valuable as more detailed ones.

The depressing part is that the software lacks boundaries, runs
with high privilege, and everyone knows those need to change. A
threat model can be a great way to start that change, by creating
a map of the current state. (The effort to specify the current model
often naturally leads to
a discussion about the future state).

## The challenge: Hospitals

The next step is to discuss how hospitals can effectively
start to assess threat models from their vendors current and
future vendors. Vendor selection will start to change. A very rough
rubric is simply, does the vendor have a public threat model? Vendors who are willing to publish their threat models
have more confidence that they’ve done a good job than the ones who have
not.

Evaluation can go deeper by looking at the level of detail: A basic
threat model here includes a diagram of 5-20 boxes and a list of
threats. Does the threat model explain
where the endpoints are, where the cloud storage buckets are and
how each is protected? Does it map to the SBOM?

After level of detail, the next question could be how many boundaries are
in the model: Are there several?
If the software operates as a full-trust monolith, that raises the
likelihood of future problems having a large blast radius, and
shows that any words the vendor said about zero trust
were... aspirational(?)

These are obviously broad brush strokes for assessment, and we’re going to have to
start figuring it out.

Image by midjourney: “a photograph of stacks of regulations on a desk. There are a few small red cartoonish devils, the size of a quarter or a bit bigger. Some are milling around, scribbling on the paper. Some are peeking out from within the stacks The photo is light and bright”

Originally published by Adam on 19 May 2026

Categories:
  [regulation](/blog/category/regulation)
  [security](/blog/category/security)
  [threat modeling](/blog/category/threat-modeling)

## Our Favorite Content

[General threat modeling posts](/blog/category/threat-modeling)

[The Security Principles of Saltzer and Schroeder, illustrated with Star Wars](/blog/the-security-principles-of-saltzer-and-schroeder)

[Other Star Wars blog posts](/blog/category/star-wars)

[Modeling attackers and their motives](/blog/modeling-attackers-and-their-motives)

[Doing science with near misses](/blog/doing-science-with-near-misses)

[Posts about Adam’s “Threats” book](/blog/category/threats-book)

[Posts about Adam’s “Threat Modeling” book](/blog/category/threat-modeling-book)

[Posts about “The New School of Information Security” book](/blog/category/the-new-school)

[About this blog](/blog/about)

## Subscribe (RSS/Mail)

RSS/ATOM: The RSS [feed is here](https://shostack.org/feed.xml). We recommend RSS as the best way to follow this blog, and think generally RSS is the best way to take control of the information you take in. You can [read our thinking here](https://shostack.org/blog/take-control-of-what-you-read).

Email: If you’d like a lower volume set of updates on what Adam is doing, [Adam’s New Thing](/contact) gets only a few messages a year, guaranteed. We include a subset of posts in each.

## Recent posts

[![Devils, in the details](/images/blog/img/2026/hipaa-devils-in-the-details-175w.png)](/blog/hipaa-nprm-threat-modeling/)

### [HIPAA Updates and Threat Models](/blog/hipaa-nprm-threat-modeling/)

19 May 2026

HIPAA reform se...