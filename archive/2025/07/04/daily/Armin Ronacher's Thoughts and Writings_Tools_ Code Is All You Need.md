---
title: Tools: Code Is All You Need
url: https://lucumr.pocoo.org/2025/7/3/tools/
source: Armin Ronacher's Thoughts and Writings
date: 2025-07-04
fetch_date: 2025-10-06T23:39:30.845502
---

# Tools: Code Is All You Need

[Armin Ronacher](/about/)'s Thoughts and Writings

* [blog](/)* [archive](/archive/)* [projects](/projects/)* [travel](/travel/)* [talks](/talks/)* [about](/about/)

# Tools: Code Is All You Need

written on July 03, 2025

If you’ve been following me on Twitter, you know I’m not a big fan of MCP
([Model Context Protocol](https://en.wikipedia.org/wiki/Model_Context_Protocol))
right now. It’s not that I dislike the idea; I just haven’t found it to work as
advertised. In my view, MCP suffers from two major flaws:

1. **It isn’t truly composable.** Most composition happens through inference.
2. **It demands too much context.** You must supply significant upfront input, and
   every tool invocation consumes even more context than simply writing and
   running code.

A quick experiment makes this clear: try completing a GitHub task with the
GitHub MCP, then repeat it with the `gh` CLI tool. You’ll almost certainly
find the latter uses context far more efficiently and you get to your intended
results quicker.

## But MCP is the Future!

I want to address some of the feedback I’ve received on my stance on this. I
evaluated MCP extensively in the context of agentic coding, where its
limitations were easiest to observe. One piece of feedback is that MCP might
not make a ton of sense for general code generation, because models are already
very good at that but they make a lot of sense for end-user applications, like,
say, automating a domain-specific task in a financial company. Another one is
that I need to look at the world of the future, where models will be able to
reach many more tools and handle much more complex tasks.

My current take is that my data indicates that current MCP will always be harder
to use than writing code, primarily due to the reliance on inference. If you
look at the approaches today for pushing towards higher tool counts, the
proposals all include a layer of filtering. You pass all your tools to an LLM
and ask it to filter it down based on the task at hand. So far, there hasn’t
been much better approaches proposed.

The main reason I believe this will most likely also hold true — that you
shouldn’t be using MCP in its current form even for non-programming,
domain-specific tasks — is that even in those cases code generation just is the
better choice because of the ability to compose.

## Replace Yourself With A Shellscript

The way to think about this problem is that when you don’t have an AI, and
you’re solving a problem as a software engineer, your tool of choice is code.
Perhaps as a non-software engineer, code is out of reach. Many many tasks
people do by hand are actually automatable through software. The challenge is
finding someone to write that software. If you’re working in a niche
environment and you’re not a programmer yourself, you might not pick up a
programming book to learn how to code, and you might not find a developer
willing to provide you with a custom piece of software to solve your specific
problem. And yes, maybe your task requires some inference, but many do need
them all the time.

There is a reason we say “to replace oneself with a shell script”, it’s because
that has been happening for a long time. With LLMs and programming, the idea is
that rather than replacing yourself with a shell script, you’re replacing
yourself with an LLM. But you run into three problems: cost, speed, and general
reliability. All these problems are what we need to deal with *before we can
even think of tool usage* or MCP. We need to figure out how to ensure that our
automated task actually works correctly at scale.

## Automation at Scale

The key to automation is really to automate things that will happen over and
over. You’re not going to automate a one-shot change that will never recur.
You’re going to start automating the things where the machine can truly give you
a productivity boost because you’re going to do it once or twice, figure out how
to make it work, and then have the machine repeat it a thousand times. For that
repetition, there’s a very strong argument to be made for always using code.
That’s because if we instruct the machine to use inference to do it, it might
work, particularly for small tasks, but it requires validation which can take
almost the same time as doing it in the first place. Getting an LLM to
calculate for you sort of works, but it’s much better for the LLM to write the
Python code to do the calculation. Why? First, you can review the formula, not
the calculated result. We can write it ourselves or we can use the LLM as a
judge to figure out if the *approach* is correct. Don’t really have to validate
that Python calculates correct, you can rely on that. So, by opting for code
generation for task solving, we get a little closer to being able to verify and
validate the process ourselves, rather than hoping the LLM inferred correctly.

This obviously goes way beyond calculation. Take, for instance, this blog. I
converted this entire blog from reStructuredText to Markdown recently. I put
this conversion off for a really long time, partly because I was a little too
lazy. But also, when I was lazy enough to consider deploying an LLM for it, I
just didn’t trust it to do the conversion itself without regressing somewhere.
I was worried that if it ran out of context, it might start hallucinating text
or change wording slightly. It’s just that I worried about subtle regressions
too much.

I still used an LLM for it, but I asked it to do that transformation in a
different way: through code.

## LLM to Code to LLM

1. I asked the LLM to perform the core transformation from reStructuredText to
   Markdown but I also asked it to do this in a way that uses the underlying AST
   (Abstract Syntax Tree). So, I instructed it to parse the reStructuredText
   into an actual reStructuredText AST, then convert that to a Markdown AST, and
   finally render it to HTML, just like it did before. This gave me an intermediate
   transformation step and a comparable end result.
2. Then, I asked it to write a script that compares the old HTML with the new HTML,
   performs the diffing after some basic cleanup it deemed necessary for
   comparison. I asked it to consider what kind of conversion errors were
   actually acceptable. So, it read through its own scripts to see where it might
   not match the original output due to known technical limitations (e.g.,
   footnotes render differently between the Markdown library I’m using and the
   reStructuredText library, so even if the syntax matches correctly, the HTML
   would look different). I asked it to compensate for this in that script.
3. After that was done, I asked it to create a third script, which I could run
   over the output of hundreds of files to analyze the differece to go back into
   the agentic loop for another iteration tep.

Then I kicked this off in a loop. I did not provide all the posts, I started
with 10 until differences were low and then had it do it for all. It did this
for maybe 30 minutes or so until I came back to it and found it in a pretty
acceptable state.

What’s key about this transformation is not so much that the LLM was capable of
pulling it off, but that I actually trusted this process at the end because I
could review the approach. Not only that, I also tried to ask another LLM what
it thinks of the code that another LLM wrote, and the changes. It gave me much
higher confidence that what was going on would not lose data. It felt right to
me. It felt like a mechanical process that was fundamentally correct, and I was
able to observe it and do spot checks. At worst, the regressions were minor
Markdown syntax errors, but the text itself wouldn’t have been corrupted.

Another key here is also that because the inference is rather constant, the cost
of inference in this process scales with the number of iteration steps and the
sample size, but it doesn’t depend on how many documents I’m wanting to convert
overall. Eventually, I just had it run over...