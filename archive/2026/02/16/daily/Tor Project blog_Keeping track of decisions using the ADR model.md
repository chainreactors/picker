---
title: Keeping track of decisions using the ADR model
url: https://blog.torproject.org/tpa-adr/
source: Tor Project blog
date: 2026-02-16
fetch_date: 2026-02-17T04:21:53.849002
---

# Keeping track of decisions using the ADR model

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Keeping track of decisions using the ADR model

by [anarcat](/author/anarcat)
| February 16, 2026

![](/static/images/lead.png)

In the Tor Project system Administrator's team (colloquially known as
TPA), we've recently changed how we take decisions, which means you'll
get clearer communications from us about upcoming changes or
*targeted* questions about a proposal.

Note that this change only affects the TPA team. At Tor, each team has
its own way of coordinating and making decisions, and so far this
process is only used inside TPA. We encourage other teams inside and
outside Tor to evaluate this process to see if it can improve your
processes and documentation.

# The new process

We had traditionally been using a "RFC" ("Request For Comments")
process and have recently switched to "ADR" ("Architecture Decision
Record").

The ADR process is, for us, pretty simple. It consists of three
things:

1. a simpler template
2. a simpler process
3. communication guidelines separate from the decision record

## The template

As team lead, the first thing I did was to propose a new template (in
[ADR-100](https://gitlab.torproject.org/tpo/tpa/team/-/wikis/policy/0100-adr-template)), a variation of the [Nygard template](https://github.com/joelparkerhenderson/architecture-decision-record/blob/main/locales/en/templates/decision-record-template-by-michael-nygard/index.md). The [TPA
variation of the template](https://gitlab.torproject.org/tpo/tpa/team/-/wikis/policy/template) is similarly simple, as it has only 5
headings, and is worth quoting in full:

* **Context**: What is the issue that we're seeing that is motivating
  this decision or change?
* **Decision**: What is the change that we're proposing and/or doing?
* **Consequences**: What becomes easier or more difficult to do
  because of this change?
* **More Information** (optional): What else should we know? For
  larger projects, consider including a timeline and cost estimate,
  along with the impact on affected users (perhaps including existing
  Personas). Generally, this includes a short evaluation of
  alternatives considered.
* **Metadata**: status, decision date, decision makers, consulted,
  informed users, and link to a discussion forum

The [previous RFC template](https://gitlab.torproject.org/tpo/tpa/wiki-replica/-/blob/d52de1828d3ee406996345704d12663dd30f5513/policy/template.md) had **17** (seventeen!) headings, which
encouraged much longer documents. Now, the decision record will be
easier to read and digest at one glance.

An immediate effect of this is that I've started using GitLab issues
more for comparisons and brainstorming. Instead of dumping in a
document all sorts of details like pricing or in-depth alternatives
comparison, we record those in the discussion issue, keeping the
document shorter.

## The process

The whole process is simple enough that it's worth quoting in full as
well:

> Major decisions are introduced to stakeholders in a meeting, smaller
> ones by email. A delay allows people to submit final comments before
> adoption.

Now, of course, the devil is in the details (and [ADR-101](https://gitlab.torproject.org/tpo/tpa/team/-/wikis/policy/0101-adr-process)), but the
point is to keep things simple.

A crucial aspect of the proposal, which Jacob Kaplan-Moss calls the
[one weird trick](https://jacobian.org/2023/dec/5/how-to-decide/), is to "decide who decides". Our previous process
was vague about who makes the decision and the new template (and
process) clarifies decision makers, for each decision.

Inversely, some decisions degenerate into endless discussions around
trivial issues because *too many* stakeholders are consulted, a
problem known as the [Law of triviality](https://en.wikipedia.org/wiki/Bike_shedding), also known as the "Bike
Shed syndrome".

The new process better identifies stakeholders:

* "informed" users (previously "affected users")
* "consulted" (previously undefined!)
* "decision maker" (instead of the vague "approval")

Picking those stakeholders is still tricky, but our definitions are
more explicit and aligned to the classic [RACI matrix](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix) (Responsible,
Accountable, Consulted, Informed).

## Communication guidelines

Finally, a crucial part of the process ([ADR-102](https://gitlab.torproject.org/tpo/tpa/team/-/wikis/policy/0102-adr-communications)) is to decouple
the act of making and recording decisions from *communicating* about
the decision. Those are two *radically* different problems to
solve. We have found that a single document can't serve both purposes.

Because ADRs can affect a wide range of things, we don't have a
specific template for communications. We suggest the [Five Ws](https://en.wikipedia.org/wiki/Five_Ws)
method (Who? What? When? Where? Why?) and, again, to keep things simple.

# How we got there

The [ADR process](https://adr.github.io/) is not something I invented. I first stumbled upon
it in the [Thunderbird Android project](https://github.com/thunderbird/thunderbird-android/blob/be2af5c6a0bce08385fc3f654c1185ccf9db3859/docs/architecture/adr/README.md). Then, in parallel, I was in
the [process of reviewing the RFC process](https://gitlab.torproject.org/tpo/tpa/team/-/issues/41428), following Jacob
Kaplan-Moss's [criticism of the RFC process](https://jacobian.org/2023/dec/1/against-rfcs/). Essentially, he argues
that:

1. the RFC process "doesn't include any sort of decision-making framework"
2. "RFC processes tend to lead to endless discussion"
3. the process "rewards people who can write to exhaustion"
4. "these processes are insensitive to expertise", "power dynamics and
   power structures"

And, indeed, I have been guilty of a lot of those issues. A verbose
writer, I have written [extremely long proposals](https://gitlab.torproject.org/tpo/tpa/team/-/wikis/policy/tpa-rfc-33-monitoring) that I suspect no
one has ever fully read. Some proposals were adopted by exhaustion, or
ignored because not looping in the right stakeholders.

Our [discussion issue](https://gitlab.torproject.org/tpo/tpa/team/-/issues/41428) on the topic has more details on the issues I
found with our RFC process. But to give credit to the old process, it
did serve us well while it was there: it's better than nothing, and it
allowed us to document a staggering number of changes and decisions
([95 RFCs](https://gitlab.torproject.org/tpo/tpa/team/-/wikis/policy)!) made over the course of 6 years of work.

# What's next?

We're still experimenting with the communication around decisions, as
this text might suggest. Because it's a separate step, we also have a
tendency to forget or postpone it, like this post, which comes a
couple of months late.

Previously, we'd just ship a copy of the RFC to everyone, which was
easy and quick, but incomprehensible to most. Now we need to write a
separate communication, which is more work but, hopefully, worth the
as the result is more digestible.

We can't wait to hear what you think of the new process and how it
works for you, here or in the [discussion issue](https://gitlab.torproject.org/tpo/tpa/team/-/issues/41428)! We're particularly
interested in people that are already using a similar process, or that
will adopt one after reading this.

* [- announcements](/category/announcements)
* [- sysadmin](/category/sysadmin)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/tpa-adr/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/tpa-adr/&text=The%20TPA%20%28Tor%20Project%20system%20Administrators%29%20team%20has%20changed%20its%20decision%20making%20process%20from%20RFC%20%28%22Request%20for%20Co...