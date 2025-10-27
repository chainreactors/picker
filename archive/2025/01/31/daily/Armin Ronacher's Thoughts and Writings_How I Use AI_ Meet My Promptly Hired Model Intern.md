---
title: How I Use AI: Meet My Promptly Hired Model Intern
url: http://lucumr.pocoo.org/2025/1/30/how-i-ai
source: Armin Ronacher's Thoughts and Writings
date: 2025-01-31
fetch_date: 2025-10-06T20:07:27.879482
---

# How I Use AI: Meet My Promptly Hired Model Intern

[Armin Ronacher](/about/)'s Thoughts and Writings

* [blog](/)* [archive](/archive/)* [projects](/projects/)* [travel](/travel/)* [talks](/talks/)* [about](/about/)

# How I Use AI: Meet My Promptly Hired Model Intern

written on January 30, 2025

After Musk’s acquisition of Twitter, many people I respect and follow
moved to Bluesky. I [created an account there](https://bsky.app/profile/mitsuhiko.at) and made an honest attempt of
making it my primary platform. Sadly, I found Bluesky to be surprisingly
hostile towards AI content. There is an almost religious resistance to AI
on there, at least in whatever corner of the platform I ended up in.

Despite these challenges, some individuals on both Twitter and Bluesky
have shown genuine curiosity about my AI usage. In this post, I want to
share how I use Large Language Models and why I find them so helpful.

Before moving on, I want to include an an important disclaimer: I am by no
means an expert in AI; I’m mostly an enthusiastic user. Absolutely
nothing here is novel! What I do here is pretty boring which to some
degree is the point. I won’t be covering underlying technology or my
programmatic experience. This is strictly about how I use AI as a “techy
consumer”.

In addition, as you read through this article you will probably figure out
rather quickly that the way I use AI — despite being used in part for
content creation — does not really impact intellectual property much.
That said, I’m curious and open to discussions about how we should be
dealing with this problem. Particularly on Bluesky a lot of the
negativity towards AI is related to watering down of copyrights and human
creation. I don’t know the answers to these things, but I think we need
to have a productive dialog here rather than wishing for the technology to
go away.

## Why AI?

In short: AI makes me significantly more productive. I recently read
[Aaron Francis](https://x.com/aarondfrancis/)‘s Tweet about how he gets
a week’s worth of productivity out of a day now thanks to AI. I’m not
anywhere close to that, but I use AI a lot now. It has become
indispensable for me for both content writing as well as programming.

Moreover, a common misconception is that AI is still at the level it was
when ChatGPT first launched. Many people tried it early, saw its
limitations, and never returned. However, AI is evolving rapidly. If you
haven’t kept up, you risk drawing inaccurate conclusions based on outdated
impressions. In some sense I believe people who never tried to use AI
yet, are in a better position to judge than the folks who used it two
years ago and never returned.

## My AI Toolkit

I work with a variety of AI tools, mostly because of professional
curiosity and to a smaller degree because each tool excels at something
slightly different. Here are the ones I use most often:

* [Open WebUI](https://openwebui.com/). In short this is a Python web
  app that offers a chat interface similar to ChatGPT.
  Unlike ChatGPT, however, it lets you talk to different models. First and
  foremost, I use this to talk to local models hosted by Ollama, but
  secondarily I also use it to interface with other remote services like
  OpenAI, Anthropic and DeepSeek.
* [Simon’s llm](https://github.com/simonw/llm). This is a command line
  tool with plenty of plugins that lets you prompt different models. Think
  of it as a command-line version of Open WebUI. It’s particularly useful
  for quick scripting and basic automation.
* [Ollama](https://ollama.com/). This allows me to run models locally
  on my MacBook Pro M1 Max. With the 64GB of RAM it has, it’s a pretty
  potent machine for basic inference despite it being three years old.
  I’ll explain later why I use local models.
* [Cursor](https://www.cursor.com/). It is a fork of Visual Studio
  Code with AI-based auto completion and code generation built-in. It’s
  my go-to for programming with AI assistance at the moment.
* [ChatGPT](https://chatgpt.com/). Like probably most AI users, I use
  ChatGPT, particularly on my phone. I pay for the Plus subscription
  because I use it enough to get a lot of value out of it. One
  significant use of this for me is in fact the voice mode (more on that
  later).

It’s probably worth mentioning that you can get most of the benefits of this from just paying for a single AI
tool. I think as one expands their use, as especially as one gets better at writing prompts,
the desire naturally grows to use more tooling. As for which models
(and services) to use day to day I don’t have a particular strong strategy
and preferences change quickly. For instance after DeepSeek’s R1 release,
I started exploring it quite a bit for programming — and it’s doing a
phenomenal job at it —  and as of writing that’s just a few days old.

If you want to run models locally, Apple Silicon machines currently offer
some of the best “bang for your buck” in terms of performance, power
usage, and money. With [tailscale](https://tailscale.com/), I can even
access my MacBook’s Open WebUI interface from my phone, as long as it is
powered on.

Guide for installing llm and Open WebUIThis is a bit of a plug for [uv](https://docs.astral.sh/uv/) quite
honestly. If you have it, it’s crazy quick to get Open WebUI and `llm`
running locally:

```
uv tool install -p python3.11 open-webui
uv tool install --with llm-ollama --with llm-claude-3 --with llm-deepseek llm
```

Afterwards you can launch `open-webui` and use the llm tool:

```
open-webui serve
llm keys set deepseek
llm -m deepseek-coder '# write timsort in python'
```

* By default, Open WebUI only connects to OpenAI or Ollama. If you want to
  add the hosted Anthropic or DeepSeek models, you need to create a custom
  function in the “Functions” section of Open WebUI’s admin panel.
* Import the functions and configure your API keys, and you’re ready to go.

Functions you can import to the WebUI:

* [Anthropic](https://openwebui.com/f/justinrahb/anthropic)
* [DeepSeek](https://openwebui.com/f/xgawatt/DeepseekAPI)
## AI Affordances

One frequent concern I hear is “you cannot trust LLMs” as they tend to
hallucinate. I get this in particular when I explain that I frequently
use this as a replacement for Google! However, I approach the risk of
hallucination the same way I would when seeking advice from another human:
people can and are routinely wrong, and you learn to cross-check
selectively.

I treat AI as I would a collaborator or a pretty good intern but I remain
responsible for the final outcome. In this case the intern also happens
to get better month by month as models improve. And a bit like a human,
that digital intern has morals and wants to be argued with. Except, of
course, that some of those AI interns [don’t want to talk about China](https://www.reddit.com/r/LocalLLaMA/comments/187oidh/deepseek_coder_7b_33b_thinks_its_trained_by_openai/),
while others get a stroke [if you talk about certain people](https://www.reddit.com/r/ChatGPT/comments/1h3rz4l/david_mayer_is_not_the_only_one_jonathan_zittrain/).
But regardless of how good they get, in the end, it’s my fault and my
fault alone if I do the wrong thing. I won’t blame the AI and I need to
spot check.

However, the logical conclusion of this is not that it’s wrong all the time
and you need to check everything, or that you cannot trust it at all.
It’s similar to how you engage in a technical discussion with others about
a problem. I have seen more than one situation where the conventional
wisdom in the room is just wrong for a few minutes, until someone points
out that we had it wrong.

Another major advantage is that AI tools are relatively open. You can run
models locally and integrate them with scripts. Even the famous OpenAI
which is not at all open is much more open than a Google search is. For
instance, you can create a simple script for grammar-checking right from
your command line.

In other words, you *can* integrate it locally and nobody stops you. By
contrast, many, many years ago I had a to...