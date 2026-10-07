---
title: What is Codemode
url: https://lucumr.pocoo.org/2026/10/6/codemode/
source: Armin Ronacher's Thoughts and Writings
date: 2026-10-06
fetch_date: 2026-10-07T07:50:31.338521
---

# What is Codemode

[Armin Ronacher](/about/)'s Thoughts and Writings

* [blog](/)* [archive](/archive/)* [projects](/projects/)* [travel](/travel/)* [talks](/talks/)* [about](/about/)

# What is Codemode

written on October 06, 2026

More than a year ago I wrote a few posts here that recommended people not to
load custom tools into their context (or
[MCP](https://en.wikipedia.org/wiki/Model_Context_Protocol) servers) but to just
use more scripts. Most importantly I wrote that [Code Is All You
Need](/2025/7/3/tools/) and I wrote about that [MCP needs
code](/2025/8/18/code-mcps/). With Pi 1.0 we now added MCP support via Codemode
which in some ways is a long time coming, but then also maybe somewhat
surprising to some. So I want to share some updated thoughts on this blog on
what this all means.

## What Are Tools

When a harness like Pi provides tools for an LLM to call, it does so by
supplying some tool definitions which then translate into some token structure
on the server side. Whether a model is encouraged to call a tool is the result
of the reinforcement learning process. Something [I wrote about
before](/2026/7/4/better-models-worse-tools/) if you want to learn more.

One of the reasons we strongly lean towards CLI and bash is because it allows
easy composition of calls, and because the model also learns how the file system
works when it’s trained. So when it invokes a tool like `echo foo > /tmp/test.txt` the model also learns that after that tool call, there is now a
file called `test.txt` in `/tmp`.

However bash has one fundamental limitation which is that it can only compose
programs that run. And there are some things, which are not programs, but
native tools to the LLM and they sort of have to be.

The most obvious example here is `read` or `view_image`. If a multimodal model
needs to read an image, it cannot use `cat` for that because the harness needs
to inject the actual image payload into the protocol of the LLM.

Another quite vivid example are sub agents. In order to spawn and orchestrate
sub agents, it’s tricky to avoid tools that are provided by the harness. While
in theory the agent could provide a CLI tool that talks to the outer harness
via environment variables and Unix sockets, it’s a rather crude process. It
however has another issue, and that is where the code runs.

## Brains vs Hands

To better understand that, it’s important to think a bit more about where all the
bits and pieces run. There really usually are two different systems involved.
The first is the brain, the harness: it runs on one machine. It’s trusted. The
second is *often* the same machine, but it’s really where the tools are
executing: the hands. In Pi we now call this the execution environment, but you
can think of it as the target of all the operations.

Crucially what is important for us, is that there is a dividing line between the
harness brain and the target environment that runs bash and executes the tools.

And splitting this in half has some really important consequences. For a start
it means that they are running on different file systems and they have different
levels of trust. If you for instance use a sandboxing solution [like
Gondolin](https://earendil-works.github.io/gondolin/) your bash stuff will be
sandboxed just fine, but the harness itself will not be.

## Orchestrating The Harness

Which brings us to what Codemode really does: it’s a way for the LLM to express
and orchestrate complex operations on the harness side, but not the execution
environment side. Codemode runs in the harness, in its own sandbox. In case of
Pi it’s running in QuickJS within a WASM runtime with intentional limitations:
no network, no file system, no timers, limited RAM. The only way is to call
more tools. You could also imagine that Codemode could run Scheme or some other
language as well.

If you are not familiar with Codemode, it’s basically just a way to issue
tool calls from within some language, in our case JavaScript. That allows you
to compose those calls without necessarily going through the LLM’s context.
Credit for naming goes to our friends at Cloudflare [who coined
it](https://blog.cloudflare.com/code-mode/).

For instance if you issue a bash call as a regular tool call in the LLM, then
we only throw the trailing 2000 lines into the context and if the agent wants
more, it needs to look at the overflow file itself. If however the agent issues
that invocation via Codemode, then the Codemode side gets larger outputs
sent structurally.

Most importantly, because Codemode is JavaScript the agent can express
concurrent operations and basic workflows. A common way in which you see agents
now use this, is to first probe at 5-10 items from some tool response to see
what it looks like, and to then write a Codemode script that processes the next
n items.

Codemode also allows you to throw state into the transcript! That means that
one Codemode invocation can stash away data, that the next call in the session
can load again. And remember: this is on the harness host, not the sandbox.

In case of Pi, Codemode also allows you to issue calls that naturally do not
make any sense in Pi’s traditional interface. For instance if you want to
generate images with an image model or you want to classify some text with a
one shot classifier model, those Pi APIs are exposed via Codemode, but not via
regular tools where they would just waste context.

## What It Looks Like

So now that we talked a bunch about it, it’s probably worth being a bit more
explicit about it. Let’s walk ourselves through some invocations of Codemode
of recent Pi sessions of mine. Note that none of this code is human written.
It’s from real sessions of Pi, just re-indented for your viewing pleasure. The
agent starts using Codemode automatically either because it’s a task where the
model already naturally picks up that tool, or because a user asked it to.

Note that Codemode is by default only enabled in Pi when MCP is enabled, but you
can turn it on with `"defaultTools": ["+codemode"]` in the settings. Just ask
Pi to enable it for you.

### Generating Images

Let’s start simple with image generation. Image generation is a feature that Pi
supports in the AI SDK core, but it’s not a tool that the agent can use. In the
past the only way to use image models has been to write a bespoke extension or
to have the agent run node itself and use the internal image APIs. However
because we expose quite a few of the internal model APIs within Codemode, it
means that the agent can use it:

```
const [painter] = await models.getAvailableOfType("image");
const result = await models.generateImages(painter, {
  input: [{ type: "text", text: "A cute little puppy sitting on a grassy " +
    "lawn, soft natural light, photorealistic" }],
});
if (result.stopReason !== "stop") return result.errorMessage;

for (const block of result.output) {
  if (block.type === "image") image(block);
  else text(block.text);
}
```

Note that the call to `image()` sends the image back as image content to the
LLM. On the harness side it feeds it directly into both the agent, as well as
onto disk as a temporary artifact in case the agent wants to be able to pass
that image back to bash.

### Classifying Things

Similar things apply to classifier models such as [Jev](https://typesafe.ai/).
They also do not fit well into the workflows of an agent through the typical
tools. But rather than making a bespoke tool available, Codemode just allows
the agent to reach into the AI SDK and invoke those directly. Here you can see
how Jev is used to mass process GitHub issues for a quick sentiment analysis:

```
const jev = await models.getModelOfType("classifier", "typesafe", "jev-latest");
const r = await tools.bash({
  command: "gh issue list --state open --limit 100 " +
    "--json number,title,body,comments",
});
const issues = JSON.parse(r.output);

const results = await Promise.all(issues.map(async (issue) => {
  const res = await models.classify(jev, {
    state: {
  ...