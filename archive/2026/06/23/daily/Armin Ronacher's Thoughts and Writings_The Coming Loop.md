---
title: The Coming Loop
url: https://lucumr.pocoo.org/2026/6/23/the-coming-loop/
source: Armin Ronacher's Thoughts and Writings
date: 2026-06-23
fetch_date: 2026-06-24T05:59:28.355278
---

# The Coming Loop

[Armin Ronacher](/about/)'s Thoughts and Writings

* [blog](/)* [archive](/archive/)* [projects](/projects/)* [travel](/travel/)* [talks](/talks/)* [about](/about/)

# The Coming Loop

written on June 23, 2026

> I don’t prompt Claude anymore. I have loops running that prompt Claude and
> figuring out what to do. My job is to write loops.
>
> — Boris Cherny

Over the last months I have watched more and more people build something on top
of coding agents that feels meaningfully different from just using a coding
agent. Some of this happens on top of [Pi](https://pi.dev/) which is cool to
see for sure! The pattern is the same everywhere though: work is put into a
queue of sorts, a machine picks it up, attempts it, stops, and then some harness
decides whether that was actually the end.

If not, the harness continues the same session, injects another message, starts
a fresh session with modified context, or sends the task to another machine. The
task stays alive beyond the point where the model by itself would normally have
said: “I am done.”

I think about that type of loop more than I want to admit.

There is already an agent loop inside every coding agent. The model calls a
tool, incorporates the result, calls another tool, reads a file, edits a file,
runs tests, and eventually produces some answer. That loop is one we have been
quite familiar with for a long time. The other loop is the harness level loop:
the loop outside the agent loop. That loop is also [not
new](https://ghuntley.com/ralph/). We have been doing versions of this since
early Claude Code days, but that loop is becoming ever more present in agentic
engineering and in recent weeks it has started to dominate the Twitter
discourse.

## I Am Not Good At This Yet

My current status is that I have not had much success with this way of working
for code I deeply care about which turns out to be quite a lot of code.

Part of that is taste and part of it is control. I attempt to set a high bar
for what I want code to look like, and I want to understand the code I ship.
Under pressure, or in a discussion with another human, I want to be able to
explain what the system does without first having to ask a clanker to explain it
to me. Now there is obviously a question if this desire to understand the code
is one that I will still have a few years from now. For now I have not moved
past the point of comprehension being important to me.

Given this desire, there is something I lack with my experience of code written
without me paying attention, particularly from loops. Present-day models tend
to produce code that is too defensive, too complex, too local in its reasoning.
They avoid strong invariants. They add fallbacks instead of making bad states
impossible. They duplicate code, invent bad abstractions, and paper over
unclear design with more machinery. Worse though: I so far see very little
progress of this improving. If anything, on that front it feels to me that
we might even be making steps in the wrong direction. At least for my taste,
present-day hands-off harnesses like Claude Code with ultracode produce worse
code than what we were producing last autumn. That’s because Claude Code, with
Fable for instance will be working uninterrupted on a problem for thirty minutes
or more, when previously the process would have been much more human in the
loop.

Furthermore it’s well understood that models tend to observe some local failure
and add a local defense. [Karpathy
mentioned](https://x.com/karpathy/status/1976082963382272334) how they are
“mortally terrified of exceptions”. In systems with important invariants,
especially persisted data formats or core infrastructure, the right fix is not
“handle every malformed case.” The right fix is to make the malformed case
unrepresentable or impossible to write in the first place. Yet even with a lot
of manual steering, that type of code does not come out of LLMs naturally, and
even if the code comes out naturally like that, they will still attempt to
handle now impossible errors.

When you take that behavior and you put it behind loops, you tend to amplify it.
If each iteration adds another small defense, the system slowly becomes less
understandable while appearing more robust. The more hands-off you are, the
more that happens. It also teaches really bad practices when tools like this
are given to juniors without clear guidance. Because if you ask them, why they
are doing all that, they will convincingly argue their case.

## Where Loops Work

At the same time, it would be dishonest to pretend the loop pattern does not
work because it already works astonishingly well in some domains.

Porting code one of them. There are already impressive examples of large
automatic porting efforts, including the reported work around moving parts of
[Bun from Zig to
Rust](https://ziggit.dev/t/bun-is-being-ported-from-zig-to-rust/15330). I have
used it with success myself [to port MiniJinja to
Go](/2026/1/14/minijinja-go-port/). Performance explorations are another case
where this works beautifully. A machine can try experiments, benchmark them,
discard failures, and keep searching. Security scanning fits naturally too and
so does almost any type of research: asking a system to explore a complex
problem space and report back without necessarily committing lasting code. One
thing that many of these have in common is that they either do not generate new
code, but transform code that already exists, or they produce code that
intentionally does not have a long shelf life. They either produce proof of
concepts or ideas, surface findings or are more akin to mechnical
transformation.

I believe that loops that produce artifacts without necessity of longevity or
that create some form of clearly verifiable mechnical translation matters more
than the general ability of a harness to mechanically measure a goal. Many
successful applications of loops use another LLM as a judge or as an
orchestrator. The mechnical translation case can be verified with a binary test
case, but it can also be judged by an LLM instead!

Claude Code, for instance, is increasingly good at creating entire experimental
workflows that it will then execute. Sure, the code it produces is slop, but
that’s more the fault of the model than the harness not being a good judge on if
a step in the workflow resulted in a net improvement or completion.

The harness just needs some signal that lets it continue. It does not have to
be objective or binary, it just has to be useful enough to drive another
iteration.

I absolutely love loops already that take the boring parts out of my day to
experiment and measure and to give me ideas.

## Software As Organism

On the other hand using that same looping methodology to write lasting code does
not yet sit well with me. The metaphor I like to reach for is one of moving
from software as a deterministic machine to software as an organism.

I became a software engineer in an enviornment that encouraged me to understand
the machine. There was always a layer you could peel off to deepen your
understanding. Machines that did not exhibit deterministic observable behavior
were maybe accepted, but generally seen as not exactly optimal. Software
architecture-wise, I saw it as desireable to push further towards more
determinism rather than less. Likewise the ability to understand the code has
been an undeniable goal. In practice not always possible we still took pride in
writing code so that it became possible even for new engineers to navigate
complex code bases through clever architecture. On well designed systems there were
always engineers that knew where the invariantes lived, which parts were
load-bearing and which changes were safe. Ideally all of that was also well
documented. Where that understanding was lacking, it was generally regarded as
something to improve upon.

Obviously that ideal has always been strained. Many software systems,
especially very successful ones had periods w...