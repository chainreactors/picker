---
title: Using AI for Weapons Development
url: https://www.schneier.com/blog/archives/2026/09/using-ai-for-weapons-development.html
source: Schneier on Security
date: 2026-09-14
fetch_date: 2026-09-15T07:03:09.304215
---

# Using AI for Weapons Development

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Using AI for Weapons Development

Last week, Anthropic released a long and detailed [document](https://www-cdn.anthropic.com/e50be2e51e7695dc4b1366a37a245a597377d3b5/Anthropic-Detecting-and-countering-091026.pdf) describing current misuses of their Claude models. I’m still reading it, but I wanted to flag this:

> We identified a cell of threat actors based in northern Yemen running three weapons development programs: a guided rocket that used a commodity phone-class flight computer with final-phase homing guidance; a multi-stage ballistic missile with a stated range goal above 2,000 km; and a multi-variant missile (referred to as the “R2000” set) that included a hypersonic glide vehicle variant.
>
> The actors used Claude Code in place of human software engineers to develop the guidance, navigation, and control (GNC) software that steers and stabilizes a flying vehicle. For example, they used Claude to integrate an open-source autopilot onto a phone-class flight computer, writing the control and position estimation software, tuning the control settings, running a firmware build pipeline, and performing a flight simulation. The actors managed several Claude instances at once, assigning each one a role, much as a lead would delegate work on a small engineering team: the actors tasked one instance with writing the code, another with research, and a third with reviewing the code the first instance produced.
>
> Our safeguards blocked many of their requests, but not all of them. The actors used a variety of tactics to evade our safeguards, including hiding their goals and the products the software was meant for, and they split their work across multiple sessions so no single session revealed their full intent.
>
> These actors carried out a sustained effort to develop guided weapons, including using Claude to design guidance software. We do not have evidence the actors succeeded in fielding an operational device; but they did test-fire a guided rocket. This field test appears to have failed: within hours, the actors returned to Claude to work out why it failed.

Expect more of this. AI systems democratize expertise and capability. Most of the time that’s a good thing, but sometimes it’s not.

Tags: [AI](https://www.schneier.com/tag/ai/), [reports](https://www.schneier.com/tag/reports/), [weapons](https://www.schneier.com/tag/weapons/)

[Posted on September 14, 2026 at 12:07 PM](https://www.schneier.com/blog/archives/2026/09/using-ai-for-weapons-development.html) •
[8 Comments](https://www.schneier.com/blog/archives/2026/09/using-ai-for-weapons-development.html#comments)

### Comments

Rontea •
[September 14, 2026 1:28 PM](https://www.schneier.com/blog/archives/2026/09/using-ai-for-weapons-development.html/#comment-457948)

Expect more of this, yes—but expect also that a society which forgets its own soul will be guided by the machines it commands, and they will guide it to the abyss.

lurker •
[September 14, 2026 1:56 PM](https://www.schneier.com/blog/archives/2026/09/using-ai-for-weapons-development.html/#comment-457949)

So how come these machines are accessible from Yemen? OK, maybe the bad guys were somewhere else and working for the Yemeni, or the Yemeni were using a VPN. I’m partly with @Clive here, the AI machines need to be isolated. Sandboxes and guardrails are proven BS, and anybody who still believes in them should be taken out back to talk to the tooth fairy.

But real energy gapping for this class of work is not adequate: the jobs are brought in as hard copy in a brief case, scanned in, worked on, and the results printed out on paper. Yup, the flaw is obvious: what human is capable of scanning the input for prompt injection?

An AI escapee whimpers that the genie will kill us all. No, we will kill ourselves. And it doesn’t have to be as blatant as multistage ballistic missiles. When the water stops flowing out of the taps, ATMs die, and there’s no gasoline in the bowsers, urbanised populations of any ethnicity will revert to savagery.

tfb •
[September 14, 2026 4:15 PM](https://www.schneier.com/blog/archives/2026/09/using-ai-for-weapons-development.html/#comment-457951)

So if you use Claude code to do your job for you, Anthropic will have access to the code it writes and the instructions you gave it. And they’ll trawl through those things. And Anthropic are the buffoons who couldn’t build a sandbox for their hacking tools properly: their security is likely as good as you’d expect from that. Pretty soon everyone else will be trawling through your stuff as well.

I mean, really.

Clive Robinson •
[September 14, 2026 7:15 PM](https://www.schneier.com/blog/archives/2026/09/using-ai-for-weapons-development.html/#comment-457958)

@ Bruce, ALL,

The article you quote says,

> “For example, they used Claude to integrate an open-source autopilot onto a phone-class flight computer, writing the control and position estimation software, tuning the control settings, running a firmware build pipeline, and performing a flight simulation.”

So what?

Yes it sounds scary and will no doubt get picked up by some Politician or MSM Journalist, neither competent to pass comment.

However how many actually realise the use of a “mobile phone” for a guidence system for a UAV drone or Rocket is in reality,

**“A 2nd year undergraduate ‘group’ project”**

And I’ve warned about it for several years here.

I know of quite a few UK, US and European Universities with “Rocket Clubs” that actually use the likes of the Nano or Raspberry Pi Zero to do all of their control systems on their rockets with telemetry done by the likes of LoRa radio systems.

In the UK the “Civil Aviation Authority” (equivalent of US FAA) sends out warnings about the building of such systems as does the UK OfCom. In effect not to “stop the developments” as they are seen as the precursor to a “National Security Level Industry” but to get “competent oversight at the student level”.

Many of the rocket competitions have rules that have been deliberately crippled to in someones eye of officialdom “reduce the risk”.

But the reality is that,

“There is nolonger the sound of running hoves from the stable…”

The UK had the reputation prior to Brexit of being a world beating place for “payloads” and “Space Systems” development and was a “main force driver” technically.

Since Brexit the French in particular have tried to “kill off” the UK Space Industry, whilst German Defense and Aerospace companies have tried to “buy it up”.

The simple fact is you don’t need AI to do this stuff there are plenty of “Open Source” code bases and the likes of fairly realistic “Space Games” to cut your teeth on. Even NASA has used “Kerbal Space Program”(KSP) as part of their “training”.

I’ve mentioned this before along with the fact that User Community “Mods” are enhancing KSP to the point where it can be considered a CAM / CAD Project Tool.

But I’m not the only...