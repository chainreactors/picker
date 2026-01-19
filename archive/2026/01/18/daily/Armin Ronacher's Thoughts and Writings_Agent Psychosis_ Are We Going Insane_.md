---
title: Agent Psychosis: Are We Going Insane?
url: https://lucumr.pocoo.org/2026/1/18/agent-psychosis/
source: Armin Ronacher's Thoughts and Writings
date: 2026-01-18
fetch_date: 2026-01-19T03:34:42.186446
---

# Agent Psychosis: Are We Going Insane?

[Armin Ronacher](/about/)'s Thoughts and Writings

* [blog](/)* [archive](/archive/)* [projects](/projects/)* [travel](/travel/)* [talks](/talks/)* [about](/about/)

# Agent Psychosis: Are We Going Insane?

written on January 18, 2026

> You can use Polecats without the Refinery and even without the Witness or
> Deacon. Just tell the Mayor to shut down the rig and sling work to the
> polecats with the message that they are to merge to main directly. Or the
> polecats can submit MRs and then the Mayor can merge them manually. It’s
> really up to you. The Refineries are useful if you have done a LOT of up-front
> specification work, and you have huge piles of Beads to churn through with
> long convoys.
>
> — [Gas Town Emergency User Manual](https://steve-yegge.medium.com/gas-town-emergency-user-manual-cf0e4556d74b), Steve Yegge

Many of us got hit by the agent coding addiction. It feels good, we barely
sleep, we build amazing things. Every once in a while that interaction involves
other humans, and all of a sudden we get a reality check that maybe we overdid
it. The most obvious example of this is the massive degradation of quality of
issue reports and pull requests. As a maintainer many PRs now look like an
insult to one’s time, but when one pushes back, the other person does not see
what they did wrong. They thought they helped and contributed and get agitated
when you close it down.

But it’s way worse than that. I see people develop parasocial relationships
with their AIs, get heavily addicted to it, and create communities where people
reinforce highly unhealthy behavior. How did we get here and what does it do to
us?

I will preface this post by saying that I don’t want to call anyone out in
particular, and I think I sometimes feel tendencies that I see as negative, in
myself as well. I too, have [thrown some vibeslop
up](https://github.com/badlogic/pi-mono/pulls?q=slop+is%3Apr+author%3Amitsuhiko+)
to other people’s repositories.

## Our Little Dæmons

In His Dark Materials, every human has a dæmon, a companion that is an
externally visible manifestation of their soul. It lives alongside as an
animal, but it talks, thinks and acts independently. I’m starting to relate our
relationship with agents that have memory to those little creatures. We become
dependent on them, and separation from them is painful and takes away from our
new-found identity. We’re relying on these little companions to validate us and
to collaborate with. But it’s not a genuine collaboration like between humans,
it’s one that is completely driven by us, and the AI is just there for the ride.
We can trick it to reinforce our ideas and impulses. And we act through this
AI. Some people who have not programmed before, now wield tremendous powers,
but all those powers are gone when their subscription hits a rate limit and
their little dæmon goes to sleep.

Then, when we throw up a PR or issue to someone else, that contribution is the
result of this pseudo-collaboration with the machine. When I see an AI pull
request come in, or on another repository, I cannot tell how someone created it,
but I can usually after a while tell when it was prompted in a way that is
fundamentally different from how I do it. Yet it takes me minutes to figure
this out. I have seen some coding sessions from others and it’s often done with
clarity, but using slang that someone has come up with and most of all: by
completely forcing the AI down a path without any real critical thinking.
Particularly when you’re not familiar with how the systems are supposed to work,
giving in to what the machine says and then thinking one understands what is
going on creates some really bizarre outcomes at times.

But people create these weird relationships with their AI agent and once you see
how some prompt their machines, you realize that it dramatically alters what
comes out of it. To get good results you need to provide context, you need to
make the tradeoffs, you need to use your knowledge. It’s not just a question of
using the context badly, it’s also the way in which people interact with the
machine. Sometimes it’s unclear instructions, sometimes it’s weird role-playing
and slang, sometimes it’s just swearing and forcing the machine, sometimes it’s
a weird ritualistic behavior. Some people just really ram the agent straight
towards the most narrow of all paths towards a badly defined goal with little
concern about the health of the codebase.

## Addicted to Prompts

These dæmon relationships change not just how we work, but what we produce. You
can completely give in and let the little dæmon run circles around you. You can
reinforce it to run towards ill defined (or even self defined) goals without any
supervision.

It’s one thing when newcomers fall into this dopamine loop and produce
something. When [Peter](https://steipete.me/) first got me hooked on Claude, I
did not sleep. I spent two months excessively prompting the thing and wasting
tokens. I ended up building and building and creating a ton of tools I did not
end up using much. “You can just do things” was what was on my mind all the
time but it took quite a bit longer to realize that just because you can, you
might not want to. It became so easy to build something and in comparison it
became much harder to actually use it or polish it. Quite a few of the tools I
built I felt really great about, just to realize that I did not actually use
them or they did not end up working as I thought they would.

The thing is that the dopamine hit from working with these agents is so very
real. I’ve been there! You feel productive, you feel like everything is
amazing, and if you hang out just with people that are into that stuff too,
without any checks, you go deeper and deeper into the belief that this all makes
perfect sense. You can build entire projects without any real reality check.
But it’s decoupled from any external validation. For as long as nobody looks
under the hood, you’re good. But when an outsider first pokes at it, it looks
pretty crazy. And damn some things look amazing. I too was blown away (and
fully expected at the same time) when Cursor’s AI written [Web
Browser](https://github.com/wilsonzlin/fastrender) landed. It’s super
impressive that agents were able to bootstrap a browser in a week! But holy
crap! I hope nobody ever uses that thing or would try to build an actual browser
out of it, at least with this generation of agents, it’s still pure slop with
little oversight. It’s an impressive research and tech demo, not an approach to
building software people should use. At least not yet.

There is also another side to this slop loop addiction: token consumption.

Consider how many tokens these loops actually consume. A well-prepared session
with good tooling and context can be remarkably token-efficient. For instance,
the entire [port of MiniJinja to Go](/2026/1/14/minijinja-go-port/) took only
2.2 million tokens. But the hands-off approaches—spinning up agents and
letting them run wild—burn through tokens at staggering rates. Patterns like
[Ralph](https://ghuntley.com/ralph/) are particularly wasteful: you restart the
loop from scratch each time, which means you lose the ability to use cached
tokens or reuse context.

We should also remember that current token pricing is almost certainly
subsidized. These patterns may not be economically viable for long. And those
discounted coding plans we’re all on? They might not last either.

## Slop Loop Cults

And then there are things like [Beads](https://github.com/steveyegge/beads) and
[Gas Town](https://github.com/steveyegge/gastown), Steve Yegge’s agentic coding
tools, which are the complete celebration of slop loops. Beads, which is
basically some sort of issue tracker for agents, is 240,000 lines of code that …
manages markdown files in GitHub repositories. And the code quality is abysmal.

There appears to be some competition in place to run as many of these agents in
parallel with almost no quality con...