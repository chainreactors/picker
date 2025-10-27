---
title: Agentic Coding Recommendations
url: http://lucumr.pocoo.org/2025/6/12/agentic-coding
source: Armin Ronacher's Thoughts and Writings
date: 2025-06-13
fetch_date: 2025-10-06T22:50:52.870722
---

# Agentic Coding Recommendations

[Armin Ronacher](/about/)'s Thoughts and Writings

* [blog](/)* [archive](/archive/)* [projects](/projects/)* [travel](/travel/)* [talks](/talks/)* [about](/about/)

# Agentic Coding Recommendations

written on June 12, 2025

There is currently an explosion of people sharing their experiences with
agentic coding. After my last [two](/2025/6/4/changes/) [posts](/2025/6/10/genai-criticism/) on the topic, I received quite a few
questions about my own practices. So, here goes nothing.

## Preface

For all intents and purposes, here’s what I do: I predominently use
[Claude Code](https://www.anthropic.com/claude-code) with the cheaper
Max subscription for $100 a month [1](#fn-1). That works well for several
reasons:

* I exclusively use the cheaper Sonnet model. It’s perfectly adequate for
  my needs, and in fact, I prefer its outputs over the more expensive Opus
  model.
* I optimize my tool usage to be token efficient. I avoid screenshots and
  browser interactions wherever possible. More on that later.

My general workflow involves assigning a job to an agent (which
effectively has full permissions) and then waiting for it to complete the
task. I rarely interrupt it, unless it’s a small task. Consequently, the
role of the IDE — and the role of AI in the IDE — is greatly diminished;
I mostly use it for final edits. This approach has even revived my usage
of Vim, which lacks AI integration.

One caveat: I expect this blog post to age very poorly. The pace of
innovation here is insane; what was true a month ago barely holds true
today. That’s why I’m sticking to concepts I believe have staying power.

If you want to a small session of me working on an Open Source library
with it, I have [a recording you can watch](https://www.youtube.com/watch?v=sQYXZCUvpIc).

## The Basics

I disable all permission checks. Which basically means I run `claude --dangerously-skip-permissions`. More specifically I have an alias
called `claude-yolo` set up. Now you can call that irresponsible and
there are definitely risks with it, but you can manage those risks with
moving your dev env into docker. I will however say that if you can watch
it do its thing a bit, it even works surprisingly well without
dockerizing. YMMV.

MCP. This is a term you cannot avoid. It basically is a standardized
protocol to give agents access to more tools. Honestly: at this point I
barely use it, but I do use it. The reason I barely use it is because
Claude Code is very capable of just running regular tools. So MCP for me
is really only needed if I need to give Claude access to something that
finds too hard to use otherwise. A good example for this is the
[playwright-mcp](https://github.com/microsoft/playwright-mcp) for
browser automation. I use it because I haven’t found anything better yet.
But for instance when I want my agent to poke around in my database, I
just uses whatever it finds to be available. In my case it loves to use
`psql` and that’s more than good enough.

In general I really only start using MCP if the alternative is too
unreliable. That’s because MCP servers themselves are sometimes not super
reliable and they are an extra thing that can go wrong. Trying to keep
things very simple. My custom tools are normal scripts that it just runs.

## Choice Of Language

I’ve evaluated agent performance across different languages my workload,
and if you can choose your language, I strongly recommend Go for new
backend projects. Several factors strongly favor Go:

* **Context system:** Go provides a capable copy-on-write data bag that
  explicitly flows through the code execution path, similar to contextvars
  in Python or .NET’s execution context. Its explicit nature greatly
  simplifies things for AI agents. If the agent needs to pass stuff to
  any call site, it knows how to do it.
* **Test caching:** Surprisingly crucial for efficient agentic loops. In
  Rust, agents sometimes fail because they misunderstand `cargo test`‘s
  invocation syntax. In Go, tests run straightforwardly and
  incrementally, significantly enhancing the agentic workflow. It does
  not need to figure out which tests to run, go does.
* **Go is sloppy:** Rob Pike famously described Go as suitable for
  developers who aren’t equipped to handle a complex language. Substitute
  “developers” with “agents,” and it perfectly captures why Go’s
  simplicity benefits agentic coding.
* **Structural interfaces:** interfaces in Go are structural. If a type
  has the methods an interface expects, then it conforms. This is
  incredibly easy for LLMs to “understand”. There is very little surprise
  for the agent.
* **Go has low eco-system churn:** Go’s entire ecosystem embraces
  backwards compatiblity and explicit version moves. This greatly reduces
  the likelihood of AI generating outdated code — starkly contrasting
  JavaScript’s fast-moving ecosystem for instance.

For comparison, Python — my initial choice — often poses significant
challenges. Agents struggle with Python’s magic (eg: Pytest’s fixture
injection) or complex runtime challenges (eg: wrong event loop when
working with async), frequently producing incorrect code that even the
agentic loop has challenges resolving. Python also has practical
performance problems. I don’t mean that it writes slow code, i mean that
the agent loop is really slow. That’s because the agent loves to spawn
processes and test scripts, and it can take quite a while for the
interpreter to boot up and initialize the entire application.

On the frontend I settled on tailwind, react with tanstack’s query and
router as well as vite. I’m not amazingly happy with it, but I found it
better than the alternatives. Tailwind and vite are great, no complaints
there. Tanstack’s file based router does not make me super happy. In
parts because it likes to have dollar signs in the file names and those
really like to confuse the agent. For instance it’s quite common that it
tries to edit `$param.tsx` but it edits the file `.tsx` instead because it
to confused by shell interpolation. It’s a minor thing, but a very
annoying thing.

## Tools, Tools, Tools

Regardless of language, effective tooling is paramount. Key rules:

* **Anything can be a tool**. A shell script can be a tool, an MCP server
  can be a tool, a log file can be a tool. If the agent can interact or
  observe it, it counts.
* Tools need to be **fast**. The quicker they respond (and the less
  useless output they produce) the better. Crashes are tolerable; hangs
  are problematic.
* Tools need to be **user friendly**! Tools must clearly inform agents of
  misuse or errors to ensure forward progress.
* Tools need to be **protected against an LLM chaos monkey** using them
  completely wrong. There is no such things as user error or undefined
  behavior!
* Tools need to provide the right **debuggability and observability**.

Example: I place critical tools into a `Makefile`. A `make dev` command
starts my services via a process manager. I made two key changes to what I
normally do:

1. I had to protect the process manager against being spawend a second
   time when it’s already running. I use a [fork of shoreman](https://gist.github.com/mitsuhiko/8ca80fda0bf48045d54bcd34d76ad887)
   which writes a pidfile. When spanwed a second time it errors and logs
   “services already running”. Why does that matter? Because the agent
   sometimes does not know if the server is already running and otherwise
   happily spawns it a second time resulting in two version of the
   service bound to the same port.
2. I am not only printing the output to my terminal, I’m also always
   logging it to a file. This allows the agent to read the log file to
   diagnose what’s happening.

Here an example agentic interaction that demonstrates this rather well:

```
⏺ Great! The formatting looks good. Now let me run the development server to test the
   dynamic onboarding:

⏺ Bash(make dev)
  ⎿  Error: error: services are already running
     make: *** [dev] Error 1

⏺ The develop...