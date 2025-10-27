---
title: Geomys, a blueprint for a sustainable open source maintenance firm
url: https://words.filippo.io/dispatches/geomys/
source: Filippo Valsorda
date: 2024-07-09
fetch_date: 2025-10-06T17:39:34.207232
---

# Geomys, a blueprint for a sustainable open source maintenance firm

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

8 Jul 2024

# Geomys, a blueprint for a sustainable open source maintenance firm

In 2022, I left Google in search of a sustainable approach to open source maintenance. A year later, I was a [full-time independent professional open source maintainer](https://words.filippo.io/full-time-maintainer/). Today I’m announcing the natural progression of that experiment: Geomys,[1](#fn:name) a small firm of professional maintainers with a portfolio of critical Go projects.

I’m joined by **[Nicola Murino](https://github.com/drakkan)**, who’s been maintaining [golang.org/x/crypto/ssh](https://pkg.go.dev/golang.org/x/crypto/ssh) for us since last summer[2](#fn:ssh), and by **[Dominik Honnef](https://honnef.co/)**, the maintainer of [Staticcheck](https://staticcheck.dev/) and [Gotraceui](https://gotraceui.dev/). They are now Geomys’ first ✨ *Associate Maintainers*. ✨ The team is completed by **Matilde Dal Zilio**, our Administrative Director who’s been helping make this journey possible from the beginning.

![The Geomys logo, an ink outline of a quaint Italian town on the side of a mountain, and below it a narrow paragraph styled like a dictionary entry for Geomys, with two definitions: 1 (Sci.) a genus of mammals often collectively referred to as the eastern pocket gophers; and 2 an organization of open source maintainers.](https://assets.buttondown.email/images/d4cdc4b2-a571-4692-95f7-100d65bd8946.png)

Geomys launches with a robust portfolio of popular, foundational open-source Go projects:

* the `crypto/...` and `golang.org/x/crypto/…` packages in the Go standard library, co-maintained by me and the Google Go team
* the `filippo.io/…` crypto packages, including [filippo.io/edwards25519](https://filippo.io/edwards25519)
* [x/crypto/ssh](https://pkg.go.dev/golang.org/x/crypto/ssh), the Go SSH implementation that runs many CI and deployment systems, maintained by Nicola
* [Staticcheck](https://staticcheck.dev/), the high-signal low-noise static analyzer enabled by default in [vscode-go](https://github.com/golang/vscode-go/wiki/tools#staticcheck), maintained by Dominik
* [Gotraceui](https://gotraceui.dev/), a tool for visualizing and analyzing Go execution traces, maintained by Dominik
* [bluemonday](https://github.com/microcosm-cc/bluemonday), the popular HTML sanitizer[3](#fn:bluemonday)
* [age](https://age-encryption.org/), the file encryption tool, library, and format
* [mkcert](https://mkcert.dev/), a tool to generate local development certificates

Every company that was previously a client of mine is now a Geomys client, paying the same monthly retainer for the professional maintenance of their critical dependencies, and for direct access to the expertise of maintainers. What’s changed is that they are now supporting more projects, and have access to more maintainers.

![The logos of Geomys’ first clients: Latacora, Interchain, Smallstep, Ava Labs, Teleport, SandboxAQ, Tailscale, and Charm](https://assets.buttondown.email/images/7cbe0b6d-ad07-41f5-887f-d93d8793975f.png)

## How we got here

I started with a rather non-consensus hypothesis: companies *want* to pay for their critical open source dependencies, but most projects are not selling them a legible way to do so. The last year has shown I was definitely onto something: I have signed four more major clients, and lost only one.[4](#fn:lost)

The model and pitch also came into clearer focus. Truly, it’s simple: if you’re betting your business on a critical open source technology, you

1. want it to be sustainably and predictably maintained; and
2. need occasional access to expertise that would be blisteringly expensive to acquire and retain.[5](#fn:buildbuy)

Getting maintainers on retainer solves both problems for a fraction of the cost of a fully-loaded full-time engineer. From the maintainers’ point of view, it’s steady income to keep doing what they do best, and to join one more Slack Connect channel to answer high-leverage questions. It’s a great deal for both sides.

There were more lessons learned, which can be summarized as “yup, these are enterprise sales, checks out”, and “advisor is a better word than consultant but still not perfect”, and “we sorely need to build standard contract language”. I will write these up soon, but if you’re impatient you can watch [my recent FOSDEM talk](https://fosdem.org/2024/schedule/event/fosdem-2024-2000-maintaining-go-as-a-day-job-a-year-later/).

Still, even if the path may look straightforward in hindsight, it’s a new model and materializing it has been a challenge. I am incredibly grateful to my clients for believing in it and for making it work with me.

## What next

Now, where do we go from here? How do I help this grow?

One way is by making it easier to do what I did, so that others can replicate it. Part of the point of doing it myself was clearing a path and making the life of future professional maintainers easier. That’s still part of the plan, but for “open source maintainer” to graduate to a mature profession, it needs to also be accessible to folks who can’t or don’t want to take on that risk, uncertainty, and extra workload.

From the onset, I envisioned small firms of professional maintainers with thematic portfolios, accommodating diverse maintainers and project sizes, just like the specialized firms of other professionals. I am now ready to try and build one.

I can tell you when I made up my mind, actually. It was with this message from a client:

> I noticed that there are two critical Go projects that we (and many others) rely on are not very actively maintained. […] Do you have any interest to become owners/co-maintainers of these projects? We’d be interested in sponsoring the maintenance, security audit, and hardening of those projects.

They trust us to maintain open source projects as a reliable team of professionals, and they understand the importance of keeping their critical dependencies healthy, so they want us to get involved in more. That’s what we’ll do.[6](#fn:proj)

## Geomys

Alright, so how does Geomys work?

Clients still pay a fixed monthly retainer to ensure the professional maintenance of the whole portfolio, and to get access to the expertise of all of Geomys’ maintainers. It’s a package deal because in my experience it’s nearly impossible to rigorously apportion value to specific projects, and it would slow down the sales process. Also, it risks penalizing smaller projects, and I want every project in the Geomys portfolio to be sustainably funded. Instead, clients just have to decide if the portfolio as a whole is worth the sticker price.

Associate Maintainers get a stable, guaranteed income—significantly higher than what GitHub Sponsors generates—and a cut of future retainer revenue growth. There’s no formula, we negotiate and figure out numbers that make the Associate happy and that are sustainable for Geomys, based on the project and on how much time the maintainer wants to dedicate to them. I expect the percentage value of the revenue share to go down over the years, rewarding those who take the most risk by joining early.

The expectations of Associates are primarily to keep doing what they’re doing: they are already experienced maintainers who know how to keep their projects healthy, now with the freedom and peace of mind of sustainably dedicating proper part-time or full-time attention to them. We want them to work on their schedule, and in their own way. I don’t wish to micromanage anyone, nor would I be particularly good at it. I like to think of Geomys as enabling maintainers to do what they already do well.

We only ask that they join the Geomys Slack Connect channels of interested clients, and ideally that they work with our technical writer to publish the occasional article about what they’re up to. Geomys is not meant to overshadow the Associates’ profiles. Quite the opposite: ...