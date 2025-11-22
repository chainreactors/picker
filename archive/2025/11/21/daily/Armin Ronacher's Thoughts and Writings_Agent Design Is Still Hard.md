---
title: Agent Design Is Still Hard
url: https://lucumr.pocoo.org/2025/11/21/agents-are-hard/
source: Armin Ronacher's Thoughts and Writings
date: 2025-11-21
fetch_date: 2025-11-22T03:06:00.772124
---

# Agent Design Is Still Hard

[Armin Ronacher](/about/)'s Thoughts and Writings

* [blog](/)* [archive](/archive/)* [projects](/projects/)* [travel](/travel/)* [talks](/talks/)* [about](/about/)

# Agent Design Is Still Hard

written on November 21, 2025

I felt like it might be a good time to write about some new things I’ve
learned. Most of this is going to be about building agents, with a little bit
about using agentic coding tools.

TL;DR: Building agents is still messy. SDK abstractions break once you hit
real tool use. Caching works better when you manage it yourself, but differs
between models. Reinforcement ends up doing more heavy lifting than expected,
and failures need strict isolation to avoid derailing the loop. Shared state
via a file-system-like layer is an important building block. Output tooling is
surprisingly tricky, and model choice still depends on the task.

## Which Agent SDK To Target?

When you build your own agent, you have the choice of targeting an underlying
SDK like the OpenAI SDK or the Anthropic SDK, or you can go with a higher level
abstraction such as the Vercel AI SDK or Pydantic. The choice we made a while
back was to adopt the Vercel AI SDK but only the provider abstractions, and to
basically [drive the agent loop
ourselves](https://ai-sdk.dev/cookbook/node/manual-agent-loop). At this point
[we](https://earendil.com/) would not make that choice again. There is
absolutely nothing wrong with the Vercel AI SDK, but when you are trying to
build an agent, two things happen that we originally didn’t anticipate:

The first is that the differences between models are significant enough that
you will need to build your own agent abstraction. We have not found any of
the solutions from these SDKs that build the right abstraction for an agent. I
think this is partly because, despite the basic agent design being just a loop,
there are subtle differences based on the tools you provide. These differences
affect how easy or hard it is to find the right abstraction (cache control,
different requirements for reinforcement, tool prompts, provider-side tools,
etc.). Because the right abstraction is not yet clear, using the original SDKs
from the dedicated platforms keeps you fully in control. With some of these
higher-level SDKs you have to build on top of their existing abstractions,
which might not be the ones you actually want in the end.

We also found it incredibly challenging to work with the Vercel SDK when it
comes to dealing with provider-side tools. The attempted unification of
messaging formats doesn’t quite work. For instance, the web search tool from
Anthropic routinely destroys the message history with the Vercel SDK, and we
haven’t yet fully figured out the cause. Also, in Anthropic’s case, cache
management is much easier when targeting their SDK directly instead of the
Vercel one. The error messages when you get things wrong are much clearer.

This might change, but right now we would probably not use an abstraction when
building an agent, at least until things have settled down a bit. The benefits
do not yet outweigh the costs for us.

Someone else might have figured it out. If you’re reading this and think I’m
wrong, please drop me a mail. I want to learn.

## Caching Lessons

The different platforms have very different approaches to caching. A lot has
been said about this already, but Anthropic makes you pay for caching. It
makes you manage cache points explicitly, and this really changes the way you
interact with it from an agent engineering level. I initially found the manual
management pretty dumb. Why doesn’t the platform do this for me? But I’ve
fully come around and now vastly prefer explicit cache management. It makes
costs and cache utilization much more predictable.

Explicit caching allows you to do certain things that are much harder
otherwise. For instance, you can split off a conversation and have it run in
two different directions simultaneously. You also have the opportunity to do
context editing. The optimal strategy here is unclear, but you clearly have a
lot more control, and I really like having that control. It also makes it much
easier to understand the cost of the underlying agent. You can assume much
more about how well your cache will be utilized, whereas with other platforms
we found it to be hit and miss.

The way we do caching in the agent with Anthropic is pretty straightforward.
One cache point is after the system prompt. Two cache points are placed at the
beginning of the conversation, where the last one moves up with the tail of the
conversation. And then there is some optimization along the way that you can
do.

Because the system prompt and the tool selection now have to be mostly static,
we feed a dynamic message later to provide information such as the current
time. Otherwise, this would trash the cache. We also leverage reinforcement
during the loop much more.

## Reinforcement In The Agent Loop

Every time the agent runs a tool you have the opportunity to not just return
data that the tool produces, but also to feed more information back into the
loop. For instance, you can remind the agent about the overall objective and
the status of individual tasks. You can also provide hints about how the tool
call might succeed when a tool fails. Another use of reinforcement is to
inform the system about state changes that happened in the background. If you
have an agent that uses parallel processing, you can inject information after
every tool call when that state changed and when it is relevant for completing
the task.

Sometimes it’s enough for the agent to self-reinforce. In Claude Code, for
instance, the todo write tool is a self-reinforcement tool. All it does is
take from the agent a list of tasks that it thinks it should do and echo out
what came in. It’s basically just an echo tool; it really doesn’t do anything
else. But that is enough to drive the agent forward better than if the only
task and subtask were given at the beginning of the context and too much has
happened in the meantime.

We also use reinforcements to inform the system if the environment changed
during execution in a way that’s problematic for the agent. For instance, if
our agent fails and retries from a certain step forward but the recovery
operates off broken data, we inject a message informing it that it might want
to back off a couple of steps and redo an earlier step.

## Isolate Failures

If you expect a lot of failures during code execution, there is an opportunity
to hide those failures from the context. This can happen in two ways. One is
to run tasks that might require iteration individually. You would run them in
a subagent until they succeed and only report back the success, plus maybe a
brief summary of approaches that did not work. It is helpful for an agent to
learn about what did not work in a subtask because it can then feed that
information into the next task to hopefully steer away from those failures.

The second option doesn’t exist in all agents or foundation models, but with
Anthropic you can do context editing. So far we haven’t had a lot of success
with context editing, but we believe it’s an interesting thing we would love to
explore more. We would also love to learn if people have success with it.
What is interesting about context editing is that you should be able to
preserve tokens for further down the iteration loop. You can take out of the
context certain failures that didn’t drive towards successful completion of the
loop, but only negatively affected certain attempts during execution. But as
with the point I made earlier: it is also useful for the agent to understand
what didn’t work, but maybe it doesn’t require the full state and full output
of all the failures.

Unfortunately, context editing will automatically invalidate caches. There is
really no way around it. So it can be unclear when the trade-off of doing that
compensates for the extra cost of trashing the cache.

## Sub Agents / Sub Inference

As I...