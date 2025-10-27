---
title: Your MCP Doesn’t Need 30 Tools: It Needs Code
url: https://lucumr.pocoo.org/2025/8/18/code-mcps/
source: Armin Ronacher's Thoughts and Writings
date: 2025-08-19
fetch_date: 2025-10-07T00:15:08.756002
---

# Your MCP Doesn’t Need 30 Tools: It Needs Code

[Armin Ronacher](/about/)'s Thoughts and Writings

* [blog](/)* [archive](/archive/)* [projects](/projects/)* [travel](/travel/)* [talks](/talks/)* [about](/about/)

# Your MCP Doesn’t Need 30 Tools: It Needs Code

written on August 18, 2025

I wrote a while back about why [code performs better](/2025/7/3/tools/)
than MCP ([Model Context
Protocol](https://en.wikipedia.org/wiki/Model_Context_Protocol)) for some
tasks. In particular, I pointed out that if you have command line tools
available, agentic coding tools seem very happy to use those. In the meantime,
I learned a few more things that put some nuance to this. There are a handful
of challenges with CLI-based tools that are rather hard to resolve and require
further examination.

In this blog post, I want to present the (not so novel) idea that an
interesting approach is using MCP servers exposing a single tool, that accepts
programming code as tool inputs.

## CLI Challenges

The first and most obvious challenge with CLI tools is that they are sometimes
platform-dependent, version-dependent, and at times undocumented. This has
meant that I routinely encounter failures when using tools on first use.

A good example of this is when the tool usage requires non-ASCII string inputs.
For instance, Sonnet and Opus are both sometimes unsure how to feed newlines or
control characters via shell arguments. This is unfortunate but ironically
not entirely unique to shell tools either. For instance, when you program with
C and compile it, trailing newlines are needed. At times, agentic coding tools
really struggle with appending an empty line to the end of a file, and you can
find some quite impressive tool loops to work around this issue.

This becomes particularly frustrating when your tool is absolutely not in the
training set and uses unknown syntax. In that case, getting agents to use it
can become quite a frustrating experience.

Another issue is that in some agents (Claude Code in particular), there is an
extra pass taking place for shell invocations: the security preflight. Before
executing a tool, Claude also runs it through the fast Haiku model to determine
if the tool will do something dangerous and avoid the invocation. This further
slows down tool use when multiple turns are needed.

In general, doing multiple turns is very hard with CLI tools because you need
to teach the agent how to manage sessions. A good example of this is when you
ask it to use [tmux for remote-controlling an LLDB
session](https://www.youtube.com/watch?v=tg61cevJthc). It’s absolutely capable
of doing it, but it can lose track of the state of its tmux session. During
some tests, I ended up with it renaming the session halfway through,
forgetting that it had a session (and thus not killing it).

This is particularly frustrating because the failure case can be that it
starts from scratch or moves on to other tools just because it got a small
detail wrong.

## Composability

Unfortunately, when moving to MCP, you immediately lose the ability to compose
without inference (at least today). One of the reasons lldb can be
remote-controlled with tmux at all is that the agent manages to compose quite
well. How does it do that? It uses basic tmux commands such as `tmux send-keys` to send inputs or `tmux capture-pane` to get the output, which don’t
require a lot of extra tooling. It then chains commands like `sleep` and `tmux capture-pane` to ensure it doesn’t read output too early. Likewise, when it
starts to fail with encoding more complex characters, it sometimes changes its
approach and might even use `base64 -d`.

The command line really isn’t just one tool — it’s a series of tools that
can be composed through a programming language: bash. The most interesting
uses are when you ask it to write tools that it can reuse later. It will start
composing large scripts out of these one-liners. All of that is hard with MCP
today.

## Better Approach To MCP?

It’s very clear that there are limits to what these shell tools can do. At
some point, you start to fight those tools. They are in many ways only as good
as their user interface, and some of these user interfaces are just
inherently tricky. For instance, when evaluated, [tmux performs better than
GNU screen](https://mariozechner.at/posts/2025-08-15-mcp-vs-cli/), largely
because the command-line interface of tmux is better and less error-prone. But
either way, it requires the agent to maintain a stateful session, and it’s not
particularly good at this today.

What is stateful out of the box, however, is MCP. One surprisingly useful way
of running an MCP server is to make it an MCP server with a single tool (the
ubertool) which is just a Python interpreter that runs [`eval()` with retained
state](https://github.com/mitsuhiko/pexpect-mcp/blob/main/src/pexpect_mcp/server.py).
It maintains state in the background and exposes tools that the agent already
knows how to use.

I did this experiment in a few ways now, the one that is public is
[`pexpect-mcp`](https://github.com/mitsuhiko/pexpect-mcp/). It’s an MCP that
exposes a single tool called `pexpect_tool`. It is, however, in many ways a
misnomer. It’s not really a `pexpect` tool — it’s a Python interpreter running
out of a virtualenv that has `pexpect` installed.

What is `pexpect`? It is the Python port of the ancient `expect` command-line
tool which allows one to interact with command-line programs through scripts.
The documentation describes `expect` as a “program that ‘talks’ to other
interactive programs according to a script.”

What is special about `pexpect` is that it’s old, has a stable API, and has been
used all over the place. You could wrap `expect` or `pexpect` with lots of
different MCP tools like `pexpect_expect`, `pexpect_sendline`, `pexpect_spawn`,
and more. That’s because the `pexpect.Spawn` class exposes 36 different API
functions! That’s a lot. But many of these cannot be used in isolation well
anyway. Take this motivating example from the docs:

```
child = pexpect.spawn('scp foo user@example.com:.')
child.expect('Password:')
child.sendline(mypassword)
```

Even the most basic use here involves three chained tool calls. And that doesn’t
include error handling, which one might also want to encode.

So instead, a much more interesting way to have this entire thing run is to just
have the command language to the MCP be Python. The MCP server turns into a
stateful Python interpreter, and the tool just lets it send Python code
that is evaluated with the same state as before. There is some extra support
in the MCP server to make the experience more reliable (like timeout support),
but for the most part, the interface is to just send Python code. In fact, the
exact script from above is what an MCP client is expected to send.

The tool description just says this:

```
Execute Python code in a pexpect session. Can spawn processes and interact with
them.

Args:
  `code`: Python code to execute. Use 'child' variable to interact with the
  spawned process. The pexpect library is already imported. Use
  `pexpect.spawn(...)` to spawn something. timeout: Optional timeout in seconds.
  If not provided, uses global `TIMEOUT` (default 30s).

Example:
  child = pexpect.spawn('lldb ./mytool')
  child.expect("(lldb)")

Returns:
  The result of the code execution or an error message.
```

This works because the interface to the MCP is now not just individual tools it
has never seen — it’s a programming language that it understands very well,
with additional access to an SDK (`pexpect`) that it has also seen and learned
all the patterns from. We’re relegating the MCP to do the thing that it does
really well: session management and guiding the tool through a built-in prompt.

More importantly, the code that it writes is very similar to what it might
put into a reusable script. There is so little plumbing in the actual MCP
that you can tell the agent after the session to write a reusable pexpect
script from what it learned in the session. Th...