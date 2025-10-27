---
title: The Reciprocal Value of Access to Maintainers
url: https://words.filippo.io/dispatches/reciprocal/
source: Filippo Valsorda
date: 2022-10-27
fetch_date: 2025-10-03T20:58:35.433558
---

# The Reciprocal Value of Access to Maintainers

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

26 Oct 2022

# The Reciprocal Value of Access to Maintainers

Last May I left Google to build a more sustainable model for Open Source maintenance. After a summer break, I resumed [my maintenance work on the Go project](https://words.filippo.io/dispatches/go1-20/) in September, and I started offering my services to companies that rely on Go.

My vision is that of Open Source maintenance as a real [profession](https://words.filippo.io/professional-maintainers/), where maintainers offer ongoing contracts to the companies that critically rely on their projects. Maintainers get paid like the senior engineers they are, and companies get reassurances on the reliability of their dependencies, mitigating business risk.

When pitching my services to companies, I am selling three things: ongoing maintenance, access to the maintainer, and marketing. An easily overlooked component of the access part is **the reciprocal value of companies having a direct line to the maintainers** of the projects they rely on.

If you’re a company that relies on a critical piece of Open Source software, the project’s roadmap matters to you. For example:

* you might be interested in adopting a new package that’s being added in the next release and want to make sure it fits your use case
* you might rely on a legacy option that’s being deprecated or made simpler and slower to reduce complexity and need that rescheduled
* you might consistently find your developers make mistakes when using an API and could benefit from a safer interface
* you might be affected by a set of bugs in a specific component that you need addressed with better testing or a refactor
* you might use a protocol implementation that’s evolving and that the project has to keep up with

I’m not talking about extra features or individual bugfixes. Those, you can usually contribute as a PR (although that *increases the maintenance burden*[1](#fn:burden) and still requires maintainer time for the design, decision, and code review processes). All the examples I listed above are things you primarily need the maintainer to prioritize in their own roadmap.

How do you encourage them to do that and support them in doing it? There is no good, reliable answer in the current models of Open Source.

Sure, there’s many ways to reach a maintainer. The public issue tracker, their emails… even Twitter DMs (please don’t). I don’t always respond, but I truly read everything that comes my way. The problem is that an endless stream of unqualified requests is not very useful for decision-making.

Everyone wants something from your project, everyone has a feature request or an idea for how to design a thing or a theory for what’s the root cause of a bug or a preference for what to prioritize next. When you’re [working in public](https://alexdanco.com/2020/10/08/making-is-show-business-now/) you need to change how you think about external inputs: they are kind offers, that you’re free to take or leave.

Even more importantly, they are *unqualified*: as a maintainer you don’t know if they reflect a real-world need that’s impacting production workloads, or just someone who did not do their research properly or who would be better served by a different project with different goals. It can actually be pretty hard to get reliable, actionable information about the needs of the users of your project.

There are a few things that work. First, personal experience as a user of your own library, which is invaluable but also unavoidably very limited in scope. Second, personal relationships and high-bandwidth interactions. For example, if I meet an engineer at a conference who tells me they are struggling with the performance of a component I get to grill them on what workload they’re running, what they tried to address it, what alternatives they considered, what tradeoffs they can make. I can’t afford to do that for every open issue! Those interactions also grow into personal relationships, where I can trust that they did their research before raising something directly with me.

Those interactions and personal relationships can be very valuable for a company, but they are not a reliable risk mitigation if they depend on the timing of a conference or on the continued employment of a person who has the maintainer’s ear.

That’s what a contractual relationship with a maintainer does: it institutionalizes the high-trust, high-attention relationship and makes it reliable.

From the other side, having a direct line to the major users of my code is valuable to me as a maintainer: I get to reach out, ask questions, and learn about how they use it. Is this component as important as I think? Does anybody use this feature? Is deprecating that feasible? What are the pain points of this thing I am planning to refactor? Would this new solution address real-world use cases?

To be clear, what this doesn’t do is provide a guarantee that a certain issue will be resolved or a change merged. It also doesn’t cut out other, non-paying users. It’s not pay to play. That wouldn’t be in anyone’s interest, because an Open Source project that prioritizes one stakeholder over the ecosystem will either bloat or become irrelevant, losing most of its value.

This reciprocal value is, I believe, very specific of a funding model that involves [high-touch](https://en.wikipedia.org/wiki/High-touch) direct relationships with multiple companies. If an intermediary gets involved, the communication channel is severed. If there is only one funder, the broad surveying capability is lost.

This is why I am pursuing professional maintainership as a high-touch contractor. If this is interesting to you and your company relies on Go and its cryptography libraries, drop me a line.

## The picture

Pop quiz: what’s this lion’s name?

![A large stone lion, bigger than life, on a pedestal pictured from the right. In the background, a tree, a building with white columns, and a skyscraper.](https://assets.buttondown.email/images/0279c084-6ea3-421c-ae14-bcfaa91fcdbd.jpeg)

---

1. This might be an unpopular opinion: sending PRs is not contributing back to the project. It might be contributing back to the ecosystem, but it imposes a cost on the project both immediately (for code review) and on an ongoing basis (for maintenance). [↩](#fnref:burden "Jump back to footnote 1 in the text")

[Subscribe](https://filippo.io/newsletter) 📮 | [Feed](https://words.filippo.io/rss/) 📡 | [Bluesky](https://bsky.app/profile/filippo.abyssdomain.expert) 🦋 | [Mastodon](https://abyssdomain.expert/%40filippo) 🐘