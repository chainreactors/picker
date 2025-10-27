---
title: AI-generated Linux kernel schedulers in Rust
url: http://arighi.blogspot.com/2024/09/ai-generated-linux-kernel-schedulers-in.html
source: arighi's blog
date: 2024-09-09
fetch_date: 2025-10-06T18:22:24.112771
---

# AI-generated Linux kernel schedulers in Rust

# [arighi's blog](http://arighi.blogspot.com/)

## Sunday, September 8, 2024

### AI-generated Linux kernel schedulers in Rust

## Overview

Many kernel hackers and OS enthusiasts have long dreamed of designing
and running a custom Linux scheduler. However, this has traditionally
been highly inaccessible, achievable only by a handful of core kernel
developers with years of deep expertise.

What if we could leverage Rust, generative Artificial Intelligence
(AI) and Large Language Models (LLMs) to create an AI that can translate
high-level scheduling concepts directly into functional kernel code?

## State of the art

Using an AI to write functional Linux kernel code can be a bit
tricky. There are experiments to use LLMs to review kernel patches, see
for example [Testing
AI-enhanced reviews for Linux patches](https://lwn.net/Articles/987319/). However, in terms of generating
fully functional code, examples have been limited to producing and fixing
simple “hello world” kernel modules or similar.

We are still far from being able to automatically generate a fully
functional Linux scheduler, primarily due to the vast amount of
knowledge and concepts required, which are scattered throughout the
kernel’s source code, an already highly complex system to
comprehend.

## Rust + sched\_ext

Recently I’ve been working at improving the usability of [scx\_rustland\_core](https://github.com/sched-ext/scx/tree/main/rust/scx_rustland_core):
a Rust framework based on [sched\_ext](https://github.com/sched-ext/scx) that enables the
implementation of custom Linux kernel schedulers in Rust, which run as
regular user-space processes, and use BPF to channel scheduling events
and actions between the kernel and user space.

This framework offers high-level Rust abstractions for the underlying
BPF and `sched_ext` subsystems, enabling developers to
concentrate on scheduling concepts, without worrying about the low-level
kernel implementation details.

This can make scheduling development much more accessible, as you can
simply create a regular Rust project (like any other user-space Rust
application) and implement the scheduling policy using the high-level
Rust APIs.

## Add ChatGPT to the equation

To validate the usability of this framework I decided to use ChatGPT
and see if the AI was able to produce working schedulers and/or improve
them using the high-level Rust API.

For this experiment, I have used the ChatGPT-4o LLM, giving as input
a simple FIFO scheduler implemented on top of
`scx_rustland_core` with well-documented code, in particular
with a very detailed description of how to use the scheduling framework
API. Then the prompt includes a request to modify the code based on the
requirements specified by command line (that are simply appended to the
prompt).

The new source code is then generated, written to a file (replacing
the original implementation), recompiled and executed.

All the source code of this experiment is available here: [scx\_rust\_scheduler](https://github.com/arighi/scx_rust_scheduler).

## Demo

This demo video shows a simple implementation of this idea.

A Python script sends the initial FIFO scheduler code along with
additional requirements to the AI, requesting it to generate a new
scheduler that meets the specified criteria.

The AI then produces the updated code, which overwrites the original
FIFO scheduler. This new code is compiled and executed, enabling the
process to be repeated for multiple iterations by specifying further
high-level requirements.

## Result

As shown in the video above, the experiment shows that the AI enhanced
the initial FIFO scheduler based on high-level guidance from the user.
This improvement reduced the total execution time for a specific multi-threaded
message-passing workload from ~5.3 seconds with the initial FIFO scheduler to
~4.9 seconds with the final optimized scheduling policy.

Benchmark:

```
$ sudo perf bench -f simple sched messaging -t -g 24 -l 2000
```

However, keep in mind that this was just a basic example and
represents a single, specific workload. Moreover, if the scheduling policy’s
requirements become too complex or intricate, the AI will likely to
introduce syntax errors or logical mistakes in the generated code.

This could be improved by better documenting the initial code in a
way that’s more comprehensible, but still, the improvements seen over the
multiple iterations in the demo were largely driven by the human guidance
more than the AI, that was acting more like a translator.

Nevertheless, it is quite impressive that instructions could be given
at such a high level of abstraction, similar to explaining concepts to a
class of students, and real, functional code capable of replacing the
current Linux kernel scheduler was produced and executed in real-time,
all within just a bunch of seconds.

## Conclusion

The goal of this experiment was to demonstrate the ease of use of
`scx_rustland_core` and showcase the potential that the
`sched_ext` technology can offer.

While LLMs aren’t poised to replace human kernel developers anytime
soon (at least not yet), they could still serve as valuable tools to
lower the entry barrier for kernel development, especially for those
passionate about it.

Though this was just a funny experiment, it could provide a great
academic playground for students to test and explore simple scheduling
concepts with ease.

Posted by

[arighi](https://www.blogger.com/profile/15223521151492879497 "author profile")

at
[10:53 AM](http://arighi.blogspot.com/2024/09/ai-generated-linux-kernel-schedulers-in.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=4397409626710913610&postID=197443640048878165&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=4397409626710913610&postID=197443640048878165&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=4397409626710913610&postID=197443640048878165&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=4397409626710913610&postID=197443640048878165&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=4397409626710913610&postID=197443640048878165&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=4397409626710913610&postID=197443640048878165&target=pinterest "Share to Pinterest")

#### No comments:

[Post a Comment](https://www.blogger.com/comment/fullpage/post/4397409626710913610/197443640048878165)

[Newer Post](http://arighi.blogspot.com/2025/01/accelerating-micro-vm-boot-time-with.html "Newer Post")

[Older Post](http://arighi.blogspot.com/2024/08/re-implementing-my-linux-rust-scheduler.html "Older Post")
[Home](http://arighi.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](http://arighi.blogspot.com/feeds/197443640048878165/comments/default)

## Blog Archive

* [May](http://arighi.blogspot.com/2025/05/) (1)
* [February](http://arighi.blogspot.com/2025/02/) (1)
* [January](http://arighi.blogspot.com/2025/01/) (1)
* [September](http://arighi.blogspot.com/2024/09/) (1)
* [August](http://arighi.blogspot.com/2024/08/) (1)
* [May](http://arighi.blogspot.com/2024/05/) (1)
* [April](http://arighi.blogspot.com/2024/04/) (1)
* [March](http://arighi.blogspot.com/2024/03/) (1)
* [February](http://arighi.blogspot.com/2024/02/) (1)
* [July](http://arighi.blogspot.com/2023/07/) (1)
* [August](http://arighi.blogspot.com/2019/08/) (1)
* [December](http://arighi.blogspot.com/2018/12/) (1)
* [August](http://arighi.blogspot.com/2013/08/) (1)
* [May](http://arighi.blogspot.com/2013/05/) (1)
* [August](http://arighi.blogspot.com/2011/08/) (2)
* [January](http://arighi.blogspot.com/2011/01/) (2)
* [September](http://arighi.blogspot.com/2009/09/) (1)
* [June](http://arighi.blogspot.com/2009/06/) (2)
* [May](http://arighi.blogspot.com/2009/05/) (2)
* [April](http://arighi.blogspot.com/2009/04/) (...