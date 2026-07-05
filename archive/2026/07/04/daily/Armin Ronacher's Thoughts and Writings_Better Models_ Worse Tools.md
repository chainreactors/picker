---
title: Better Models: Worse Tools
url: https://lucumr.pocoo.org/2026/7/4/better-models-worse-tools/
source: Armin Ronacher's Thoughts and Writings
date: 2026-07-04
fetch_date: 2026-07-05T05:55:41.620139
---

# Better Models: Worse Tools

[Armin Ronacher](/about/)'s Thoughts and Writings

* [blog](/)* [archive](/archive/)* [projects](/projects/)* [travel](/travel/)* [talks](/talks/)* [about](/about/)

# Better Models: Worse Tools

written on July 04, 2026

A very strange [Pi issue](https://github.com/earendil-works/pi/issues/6278)
sent me down a rabbit hole over the last two days. The short version is that
newer Claude models sometimes call Pi’s edit tool with extra, invented fields in
the nested `edits[]` array. And not Haiku or some small model: Opus 4.8. The
edit itself is usually correct but the arguments do not match the schema as
the model invents made-up keys and Pi thus rejects the tool call and asks to
try again.

That alone is not too surprising as models emit malformed tool calls sometimes.
Particularly small ones. What surprised me is that this is getting worse with
newer Anthropic models as both Opus 4.8 and Sonnet 5 show it but none of the
older models. In other words, the SOTA models of the family are worse at this
specific tool schema than their older siblings.

In case you are curious about Fable: I intentionally did not test it because I
was not sure if the classifiers they are running might downgrade me to Opus
silently.

## Tool Calls Are Text

If you have not spent too much time looking at LLM tool calling internals, the
important thing to understand is that tool calls are not magic and use some
rather crude in-band signalling. The model receives a transcript, a system
prompt and a list of available tools. The server munches that into a large
prompt with special marker tokens. Because the model was trained and
reinforced on examples of that format, at some point during generation it emits
something that the API or client interprets as “call this tool with these
arguments”.

For a file edit tool, the intended invocation payload might say something like
this:

```
{
  "path": "some/file.py",
  "edits": [
    {
      "oldText": "text to replace",
      "newText": "replacement text"
    }
  ]
}
```

A harness then validates the arguments, performs the edit, and feeds the result
back into the model. If validation fails, the model sees an error and usually
tries again.

How exactly that formatting happens is not known for the Anthropic models, but
some people have gotten out “ANTML” markers and they at times do leak also into
public communications. To the best of my knowledge, the call above would come
out serialized like this from the model:

```
<antml:function_calls>
  <antml:invoke name="edit">
    <antml:parameter name="path">some/file.py</antml:parameter>
    <antml:parameter name="edits">
[
  {
    "oldText": "text to replace",
    "newText": "replacement text"
  }
]
    </antml:parameter>
  </antml:invoke>
</antml:function_calls>
```

An important thing to note here is that this thing, while looking like XML, is
not really XML. It’s just a thing they found convenient to tokenize and train
on. The other thing to note is that a basic top-level string parameter appears
in-line whereas an array of objects is implemented via JSON serialization.
While I’m not *entirely sure* that this is how it works, there are some
indications that this is not too far off. This will become relevant later.

There are two very different ways to make the model produce a structure like
this:

1. You can *ask* the model to produce valid JSON matching a schema and then
   validate it afterwards.
2. You can constrain the sampler so that invalid JSON, or even invalid schema
   shapes, cannot be sampled in the first place.

The second approach is what people usually refer to as grammar-aware or
constrained decoding. The sampler masks out tokens that would violate the
grammar. If the model is currently inside a JSON object and the schema says
only `oldText` and `newText` are allowed, the sampler can prevent it from
emitting `"in_file"` or `"type"`. Grammar-aware decoding can be used both to
constrain something to be syntactically valid JSON and also to enforce specific
enum values or keys.

Without any form of constraints the model is merely following a learned
convention.

## The Failure

Pi’s edit tool supports multiple exact string replacements in one call. That is
why the arguments contain an `edits` array. In the failing cases the model
produces entries like this:

```
{
  "oldText": "...",
  "newText": "...",
  "requireUnique": true
}
```

or this:

```
{
  "oldText": "...",
  "newText": "...",
  "oldText2": "",
  "newText2": ""
}
```

Across repeated trials I saw a whole zoo of invented trailing keys: `type`,
`id`, `kind`, `unique`, `requireUnique`, `matchCase`, `in_file`,
`forceMatchCount`, `children`, `notes`, `cost`, `oldText2`, `newText2`,
`oldText_2`, `newText_2`, and even an `event.0.additionalProperties` key inside
the edit object itself.

The most annoying part is that the actual `oldText` and `newText` payloads were
byte-correct in the invalid calls I inspected. The model had in fact produced
the right invocation but then added nonsense at the end of the object.

The failure is also heavily context-dependent. A fresh single-turn prompt like
“edit this file” did not reproduce it at all for me. An agentic history where the
model had read files, diagnosed a problem and then composed a multi-line edit
could reproduce it. And more annoyingly, not all transcripts will show that behavior.
In fact, I needed [Petr Baudis](https://github.com/pasky)‘s transcripts to
reproduce this for me at all! In that user’s session continuing the session
caused Opus 4.8 to fail around 20% of the time. Stripping thinking blocks from
history reduced the failure rate by half. Turning on strict tool invocation
eliminated it in my runs.

## Why It’s Getting Worse

My strongest hypothesis is that this is not random deterioration but a training
artifact.

When older Anthropic models were trained, they were trained on some tools (some of
which were documented). But that training did not yet have a user-shipped
harness like Claude Code as the obvious target. Modern Anthropic models are
most likely different because their post-training includes Claude Code or a
harness that looks very similar. The model learns what a successful tool call
looks like in that environment. It also learns what mistakes are tolerated by that environment.

Claude Code’s own tools are comparatively flat. The ordinary edit tool is not
Pi’s nested `edits[]` shape; it is closer to `file_path`, `old_string`,
`new_string`, and an optional flag (`replace_all`). Looking at Claude Code’s
client is very instructive: it contains retry paths for malformed tool use,
parameter aliases, type coercions, Unicode repairs and filtering of unknown
keys. In other words, Anthropic’s own client appears to expect and accept a
fair amount of slop and repairs it, mostly silently.

If reinforcement learning happens in a harness like that, or a simulation of
one, then slightly malformed tool calls can still complete the task and receive
reward. The harness fully absorbs the error and there is little gradient
against inventing an alias, adding a stray field or using a nearby parameter
name.

Worse, the model may become very strongly adapted to the canonical Claude Code
edit tool shape. A different harness can present a tool with the same semantic
intent but a different schema. Such a tool can increasingly be
off-distribution. The better-trained model might actually fight you harder
because its prior is stronger.

This is not too surprising, but it is a change from how this was a few months ago.
When Opus 4.5 launched, it adapted to other edit tools exceptionally well. In
fact, I was pretty convinced that we’re on a good path where the models are
more likely to adapt to any sort of tool shape that comes around for as long
as the instructions are good.

Now I’m somewhat worried about the track we’re on here. Alternative tool
schemas might not just be unfamiliar. They might be implicitly punished by
post-training that optimizes for one particular, forgiving tool ec...