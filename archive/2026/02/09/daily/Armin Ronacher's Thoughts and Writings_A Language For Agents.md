---
title: A Language For Agents
url: https://lucumr.pocoo.org/2026/2/9/a-language-for-agents/
source: Armin Ronacher's Thoughts and Writings
date: 2026-02-09
fetch_date: 2026-02-10T04:25:11.680877
---

# A Language For Agents

[Armin Ronacher](/about/)'s Thoughts and Writings

* [blog](/)* [archive](/archive/)* [projects](/projects/)* [travel](/travel/)* [talks](/talks/)* [about](/about/)

# A Language For Agents

written on February 09, 2026

Last year I first started thinking about what the future of programming
languages might look like now that agentic engineering is a growing thing.
Initially I felt that the enormous corpus of pre-existing code would cement
existing languages in place but now I’m starting to think the opposite is true.
Here I want to outline my thinking on why we are going to see more new
programming languages and why there is quite a bit of space for interesting
innovation. And just in case someone wants to start building one, here are some
of my thoughts on what we should aim for!

## Why New Languages Work

Does an agent perform dramatically better on a language that it has in its
weights? Obviously yes. But there are less obvious factors that affect how
good an agent is at programming in a language: how good the tooling around it is
and how much churn there is.

Zig seems underrepresented in the weights (at least in the models I’ve used)
and also changing quickly. That combination is not optimal, but it’s still
passable: you can program even in the upcoming Zig version if you point the
agent at the right documentation. But it’s not great.

On the other hand, some languages are well represented in the weights but agents
still don’t succeed as much because of tooling choices. Swift is a good
example: in my experience the tooling around building a Mac or iOS application
can be so painful that agents struggle to navigate it. Also not great.

So, just because it exists doesn’t mean the agent succeeds and just because it’s
new also doesn’t mean that the agent is going to struggle. I’m convinced that
you can build yourself up to a new language if you don’t want to depart
everywhere all at once.

The biggest reason new languages might work is that the cost of coding is going
down dramatically. The result is the breadth of an ecosystem matters less. I’m
now routinely reaching for JavaScript in places where I would have used Python.
Not because I love it or the ecosystem is better, but because the agent does
much better with TypeScript.

The way to think about this: if important functionality is missing in my
language of choice, I just point the agent at a library from a different
language and have it build a port. As a concrete example, I recently built an
Ethernet driver in JavaScript to implement the host controller for our sandbox.
Implementations exist in Rust, C, and Go, but I wanted something pluggable and
customizable in JavaScript. It was easier to have the agent reimplement it than
to make the build system and distribution work against a native binding.

New languages will work if their value proposition is strong enough and they
evolve with knowledge of how LLMs train. People will adopt them despite being
underrepresented in the weights. And if they are designed to work well with
agents, then they might be designed around familiar syntax that is already known
to work well.

## Why A New Language?

So why would we want a new language at all? The reason this is interesting to
think about is that many of today’s languages were designed with the assumption
that punching keys is laborious, so we traded certain things for brevity. As an
example, many languages — particular modern ones — lean heavily on type
inference so that you don’t have to write out types. The downside is that you
now need an LSP or the resulting compiler error messages to figure out what the
type of an expression is. Agents struggle with this too, and it’s also
frustrating in pull request review where complex operations can make it very
hard to figure out what the types actually are. Fully dynamic languages are
even worse in that regard.

The cost of writing code is going down, but because we are also producing more
of it, understanding what the code does is becoming more important. We might
actually want more code to be written if it means there is less ambiguity when
we perform a review.

I also want to point out that we are heading towards a world where some code is
never seen by a human and is only consumed by machines. Even in that case, we
still want to give an indication to a user, who is potentially a non-programmer,
about what is going on. We want to be able to explain to a user what the code
will do without going into the details of how.

So the case for a new language comes down to: given the fundamental changes in
who is programming and what the cost of code is, we should at least consider
one.

## What Agents Want

It’s tricky to say what an agent wants because agents will lie to you and they
are influenced by all the code they’ve seen. But one way to estimate how they
are doing is to look at how many changes they have to perform on files and how
many iterations they need for common tasks.

There are some things I’ve found that I think will be true for a while.

### Context Without LSP

The language server protocol lets an IDE infer information about what’s under
the cursor or what should be autocompleted based on semantic knowledge of the
codebase. It’s a great system, but it comes at one specific cost that is tricky
for agents: the LSP has to be running.

There are situations when an agent just won’t run the LSP — not because of
technical limitations, but because it’s also lazy and will skip that step if it
doesn’t have to. If you give it an example from documentation, there is no easy
way to run the LSP because it’s a snippet that might not even be complete. If
you point it at a GitHub repository and it pulls down individual files, it will
just look at the code. It won’t set up an LSP for type information.

A language that doesn’t split into two separate experiences (with-LSP and
without-LSP) will be beneficial to agents because it gives them one unified way
of working across many more situations.

### Braces, Brackets, and Parentheses

It pains me as a Python developer to say this, but whitespace-based indentation
is a problem. The underlying token efficiency of getting whitespace right is
tricky, and a language with significant whitespace is harder for an LLM to work
with. This is particularly noticeable if you try to make an LLM do surgical
changes without an assisted tool. Quite often they will intentionally disregard
whitespace, add markers to enable or disable code and then rely on a code
formatter to clean up indentation later.

On the other hand, braces that are not separated by whitespace can cause issues
too. Depending on the tokenizer, runs of closing parentheses can end up split
into tokens in surprising ways (a bit like the “strawberry” counting problem),
and it’s easy for an LLM to get Lisp or Scheme wrong because it loses track of
how many closing parentheses it has already emitted or is looking at. Fixable
with future LLMs? Sure, but also something that was hard for humans to get
right too without tooling.

### Flow Context But Explicit

Readers of this blog might know that I’m a huge believer in async locals and
flow execution context — basically the ability to carry data through every
invocation that might only be needed many layers down the call chain. Working
at an observability company has really driven home the importance of this for
me.

The challenge is that anything that flows implicitly might not be configured.
Take for instance the current time. You might want to implicitly pass a timer
to all functions. But what if a timer is not configured and all of a sudden a
new dependency appears? Passing all of it explicitly is tedious for both humans
and agents and bad shortcuts will be made.

One thing I’ve experimented with is having effect markers on functions that are
added through a code formatting step. A function can declare that it needs the
current time or the database, but if it doesn’t mark this explicitly, it’s
essentially a linting w...