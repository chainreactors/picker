---
title: Fiddler – My Mistakes
url: https://textslashplain.com/2024/11/24/fiddler-my-mistakes/
source: text/plain
date: 2024-11-26
fetch_date: 2025-10-06T19:19:52.629775
---

# Fiddler – My Mistakes

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Fiddler – My Mistakes

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2024-11-242025-09-24](https://textslashplain.com/2024/11/24/fiddler-my-mistakes/)Posted in[bluebadge](https://textslashplain.com/category/bluebadge/), [books](https://textslashplain.com/category/books/), [life](https://textslashplain.com/category/life/), [storytelling](https://textslashplain.com/category/storytelling/), [tech](https://textslashplain.com/category/tech/)Tags:[career](https://textslashplain.com/tag/career/), [Fiddler](https://textslashplain.com/tag/fiddler/), [performance](https://textslashplain.com/tag/performance/)

On a flight back from Redmond last week, I finally read Linus Torvalds’ 2002 memoir “[Just For Fun](https://amzn.to/497bFVT).” I really enjoyed its picture of Linux (and Torvalds) early in its success, with different chapters varyingly swooning that Linux had 12 or 25 million users. But more than that, I enjoyed some of the “behind the scenes” of a world-famous project that started out small before growing out-of-control.

Twenty years ago, I released the first builds of Fiddler, an app I’d begun as a side project while working on the clipart feature team in Microsoft Office. Originally, the idea was to build a debugger for the client/server communications between the Office client applications and the clipart download website. To put it mildly, the project was much more successful than I would’ve ever hoped (or *believed*) back then. More than anything else, Fiddler was a learning experience for me — when I started, I knew neither HTTP nor C#, so setting out to build a Web Debugger in .NET was quite an ambitious undertaking.

By the time I’d finished officially working on the project, Fiddler and its related projects amounted to perhaps 40000 of lines of code. But that’s misleading– over the years, I probably wrote at least five times as many, constantly rewriting and refactoring as I learned more (and as the .NET Framework grew more powerful over the twelve years Fiddler was under my control). I learned a huge amount while building Fiddler, mostly by making mistakes and then learning from them.

In today’s post, I’d like to summarize some of the mistakes I made in writing Fiddler (big and small) — the sorts of things I’d tell my earlier self if I ever manage to build that [time machine](https://textslashplain.com/2021/10/01/practical-time-machines/). I’ll also talk about some things that went unexpectedly well, and decisions where even now, I couldn’t say whether a different choice would’ve led to a better outcome. Some of these are technical (only of interest to geeks), and some may be interesting for other audiences.

While personal experience tends to be the [most *vivid* teacher](https://bsky.app/profile/ericlawrence.com/post/3ld4zi3w4ss2h), learning from the mistakes of others tends to be more *efficient*.

### The Mistakes

I made a huge number of mistakes while building Fiddler, but I was fast to correct the majority when I became aware of them. The mistakes that were the hardest (or effectively impossible) to fix still linger today.

##### **Collaboration**

The *core* mistake I made with Fiddler was spending the first years *thinking* about it endlessly, without doing much *talking* about it. Had I spent more time talking to more experienced developers, I could have avoided most of the big technical mistakes I made. *Similarly, had I talked to my few friends in the startup/business community, I would’ve been much more prepared for Fiddler’s eventual sale.*

Still, I know I’m being a bit hard on myself here– twenty years ago, it wasn’t clear that Fiddler was really going to amount to more than “Just another side project”– one of a dozen or so I had cooking at any given time.

##### Threading

When Fiddler was first built, I knew that it needed to do a lot of work in parallel, so I quickly settled upon a model that used a thread per request. When Fiddler received a new connection from a client, it would spawn a new thread and that thread would read the request headers and body, perform any necessary modifications, lookup the target site’s address in DNS, connect to that address, secure the connection with HTTPS, resend the client’s request, read the response headers and body from the server, perform any necessary modifications, and return that response to the client. The thread would then either wait for another request on the client’s connection, or self-destruct if the connection was closed. As you can see, that’s a huge stream of work, and we want it to happen as fast as possible, so I naively assumed that the simplicity of the thread-per-connection would provide the best performance.

What I didn’t realize for a few years, however, is that virtually all of those operations involve a huge amount of “waiting around” — waiting for the network stack to send the full request from the client, waiting to resolve the hostname in DNS, waiting for the connection to the server, waiting for the server to return content, waiting for the client to read the response from Fiddler, and so much more. Taken as a whole, it’s a *huge* amount of waiting. I didn’t realize this for *years*, however, and didn’t look closely at the various much more complicated asynchronous programming paradigms added to the .NET Framework over the years. “*Why would I want all of that complexity?”* I wondered.

Eventually, I learned. I noticed that projects like the .NET Kestrel web server are built entirely around cutting-edge asynchronous programming concepts. While Fiddler would slow to a crawl with a few dozen simultaneous connections, Kestrel started at tens of thousands per second and only got faster from there. When I starting looking closer at Fiddler’s thread performance, I found a huge regression I’d introduced without noticing for *years*: Early in Fiddler’s development, I’d switched from creating an entirely new thread to using the .NET thread pool. In the abstract, this is better, but I never noticed that when the thread pool was out of threads, the Framework’s code deliberately would wait 500 milliseconds before adding a new thread. This meant that after Fiddler had around 30 connections active, every subsequent new connection was *deliberately* delayed. *Ouch*!

Unfortunately, Fiddler’s extensibility model was such that it wouldn’t’ve been possible to completely rewrite it to use .NET’s asynchronous patterns, although from 2014 to 2016, I gradually coaxed the implementation toward those patterns where possible. In the course of doing so, I learned a huge amount about the magic of async/await and how it works under the covers.

##### Simple Fields

I started building Fiddler (before I knew almost any C# at all) by defining the basic objects: HTTP headers, a Request object, a Response object, a Proxy object, a Connection object, and so forth. In many cases, I exposed data as public fields on each object rather than wrapping fields in C# Properties, reasoning that for most things, Properties represented unnecessary indirection and overhead, and remember, *I wanted Fiddler to be fast*.

It was quite a few years before I realized the error of my ways– while Properties do, in fact, introduce overhead, it’s *the cheap kind* of overhead. Many of the optimizations (performance and developer experience) I’d’ve liked to have made to Fiddler in later years were precluded by the need to preserve compatibility– converting fields to properties is a breaking change.

By far, the biggest mistake was exposing the HTTP `body` data as a simple `byte[]` field on the request and response objects. While plain byte arrays are *conceptually* easiest to understand, easy for me to implement, and convenient for extension and script authors, it was a disastrous choice. Many HTTP bodies are tiny, but a large percentage are over the 85kb thr...