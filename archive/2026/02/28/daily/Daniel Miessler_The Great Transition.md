---
title: The Great Transition
url: https://danielmiessler.com/blog/the-great-transition?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2026-02-28
fetch_date: 2026-03-01T04:28:19.918047
---

# The Great Transition

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[about](/about/)[members](/members/)[UL Site](https://unsupervised-learning.com)[DAEMON](https://daemon.danielmiessler.com)

# The Great Transition

A mental model for thinking about all the big changes that are happening as a single transition

February 28, 2026

[#ai](/archives/?tag=ai) [#future](/archives/?tag=future) [#society](/archives/?tag=society) [#technology](/archives/?tag=technology) [#business](/archives/?tag=business)

[![The Great Transition—multiple streams converging](/images/the-great-transition.webp)](/images/the-great-transition.webp)

I'm going to try to encapsulate a whole bunch of stuff that's going on right now and wrap it into a single container. It's actually very difficult to do because there's so much change, and things are getting crazier every single week, every single day almost.

I've noticed a whole bunch of transitions happening at the same time, and I'm calling it the great transition. It's really many smaller transitions, but they have a theme and a direction. And I think I know roughly where they're going.

What I want to give you is something where if you think about all of these ideas and just let them stew, the news that comes out over the next weeks, months, even years will just make more sense. You can put it into this container, this mental model of thinking about things.

## Knowledge goes from private to public [​](#knowledge-goes-from-private-to-public)

There are a few different things making this happen. One is just LLMs in general, AI in general. The concept is that it consumes all the stuff from the internet—all the books, all the blogs, forum conversations—all this training that's been done on these models. All of that condenses into a model that's kind of representative of all this knowledge. Everybody kind of knows that already.

What's not so much understood is what this is actually doing to knowledge work.

In the past, going back 10, 20, 30, 50 years, if you were an expert in something, you had knowledge that no one else had. If you were a specialist consultant at McKinsey or you were a heart doctor or whatever, you had special knowledge. And you hadn't captured even a 10th of it. Let's say you've written two books—you still haven't captured a 10th of your knowledge. You just know things that other people don't. If you're a security professional who's been doing this for 20 years, you just understand things. If you're a CISO that's done this multiple times, you just understand things and get things that nobody else has. And importantly, it's not in a book somewhere. Even if you've written books, your knowledge is still not fully in the books.

That has always protected smart people—the ones with both the smarts and the experience. That combination has made them very special.

What is happening now is completely changing that.

🧠 [Skills](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/skills)—folders of markdown files—are how specialized knowledge gets captured and made portable.

Especially with skills—this whole concept that [Anthropic](https://www.anthropic.com) came up with. We're talking about a folder full of markdown files that can encapsulate a decent amount of your knowledge. You still have the capture problem where they don't know exactly what to say, how to capture it, but here's the situation: many, many smart people are producing skills and many, many other smart people are going to collect specialized knowledge from all over the internet, anywhere it's been written down, and bring that into a skill. Plus all these specialist people—they're writing books, doing presentations, writing blogs, doing interviews, doing podcasts.

In the past we'd never had a system that could basically say, go get all of that. Go get everything Dr. Huberman has ever said about health or morning routines, bring it all together and turn that into a skill. This is one prompt. Find everything Huberman has said about morning routines from every podcast, every blog, every article, every interview and put that into a skill. That new thing combined with the models just getting better—it feeds on itself. The model then can consume all those skills.

The gap between specialized privatized knowledge—inside of someone's mind, some specialist doctor, some specialist psychiatrist who's been doing this work for 40 or 50 years—the delta between what they know and no one else knows is getting smaller. That is massively impactful for humanity in general.

Then there's another layer on this. All of that is being consumed by these labs who are spending billions of dollars bringing that knowledge into the models. But what we just saw from Anthropic—and this is happening all over the place—a bunch of Chinese labs are doing it in mass, very organized. China is known for doing this. They are famous for stealing ideas and stealing content.

They're also massively going all in on open source models. I believe they have a very clear strategy: you don't have to compete to be a pinnacle lab. They don't have an Anthropic. They don't have a Google DeepMind. They don't have an OpenAI. But they do have [DeepSeek](https://www.deepseek.com), and DeepSeek has been called out for doing this for a very long time. They are capturing the knowledge of all the billions of dollars of work and bringing it into open source.

What they are doing as a Chinese strategy for AI is releasing it, diffusing it, absorbing it into the pool. You've heard the metaphor peeing in the pool. Our specialized knowledge—what specialized humans could do that no one else could do—that is the pee that's going into the pool. You can't pull it out. It's just going to be in there.

And the techniques that make those premier labs better—those are also being diffused. Somehow when the major labs have a major advantage and jump ahead, the Chinese models seem to get it a few months later. The specialized knowledge is being diffused into public domain. That's just a transition that's happening.

## Products go from standalone software to APIs [​](#products-go-from-standalone-software-to-apis)

I talked about this in [my book from 2016](/blog/the-real-internet-of-things)—basically said that **[businesses become APIs](/blog/mobile-ai-digital-assistants-business-apis)**. And we're finally now starting to see this.

📚 From [*The Real Internet of Things*](/blog/the-real-internet-of-things), published in 2016.

All these people releasing tools, models, functionality—a company that does remove background, Excalidraw just came out with a new piece of functionality where you could just describe what you want to make and it will build all the different objects for you in your favorite fonts and your favorite aesthetic. It'll just build you diagrams.

My first question when I saw this was hold on. I went and looked at the documentation and it basically said you just go into the interface and type into Excalidraw what you want. And I'm like, what are you talking about? Do you honestly think in early 2026, I'm going to open up Excalidraw and type in a prompt? Are you kidding me?

So I posted: this looks amazing. Looks fantastic. There's no way I'm going to use it. Can you make this available as an [MCP](https://modelcontextprotocol.io)? Can you make this available as an API? I'm not going to do any of this ever. **If I have to open an app, I've already lost.** My AI should be doing all of this for me.

When I posted that on Twitter, a whole bunch of people showed up and they're like, yeah, a hundred percent. I need an MCP for this. Otherwise it's not useful.

That is the way everything is going. If you notice, most of the releases coming out for products now, they're like, here's the MCP for it. Here's how your agents can do this automatically. This is just becoming the new way to release software. And this ...