---
title: Our Constraints on Creativity
url: https://danielmiessler.com/blog/our-constraints-on-creativity?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2025-09-11
fetch_date: 2025-10-02T20:01:01.062189
---

# Our Constraints on Creativity

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[speaking](/speaking/)[about](/about/)

# Our Constraints on Creativity

A list of different ways we limit ourselves creatively

September 10, 2025

[#philosophy](/archives/?tag=philosophy) [#productivity](/archives/?tag=productivity) [#society](/archives/?tag=society)

[![Creative Limitations](/images/creative-limitations.png)](/images/creative-limitations.png)

The types of creative barriers that limit our potential

There are multiple constraints that limit how creative we can be as humans.

Let's talk about each of them and how we can counter them.

# Type 1: Not hearing your inner creativity [​](#type-1-not-hearing-your-inner-creativity)

[![Letters Young Poet Rainer Rilke](/images/letters-young-poet-book-small.jpg)](https://www.amazon.com/Letters-Young-Poet-Rainer-Rilke/dp/0393310396)

What I'll call Type 1 is the inability to access your true, internal self. I discovered this concept while reading ["Letters to a Young Poet"](https://www.amazon.com/Letters-Young-Poet-Rainer-Rilke/dp/0393310396)—a correspondence between a young poet and [Rilke](https://en.wikipedia.org/wiki/Rainer_Maria_Rilke) in the early 1900s. The young poet sought advice about his poetry. Rilke responded by urging him to reconnect with his inner curious child.

> To be solitary as you were when you were a child, when the grownups walked around involved with matters that seemed large and important because they looked so busy and because you didn't understand a thing about what they were doing. Rainer Maria Rilke

Rilke argued that we're most creative as young children—exploring without access to the adult world. Everything is possible. Everything becomes a game, exciting, imaginative. Rilke believed this represents our purest form of creativity.

[![Mathematica Secret World Intuition Curiosity](/images/mathematica-book-small.jpg)](https://www.amazon.com/Mathematica-Secret-World-Intuition-Curiosity/dp/0300270887)Mathematica by David Bessis

I encountered a similar idea again in ["Mathematica"](https://www.amazon.com/Mathematica-Secret-World-Intuition-Curiosity/dp/0300270887), which explains how our understanding of advanced mathematics is completely wrong.

This is one of my favorite books in many years.

It argues you can't learn higher-level math through memorization or mastering equations. It says Math is imagination-based! And that it requires visualizing how things work and how they connect. This visual understanding isn't secondary—*it's the entire foundation*.

I've always wanted to learn math, which is why I read this book. I am so happy that I did.

The author says this concept of the inner child, inner curiosity, or pure curiosity is absolutely essential. It's the voice we must rediscover within ourselves if we want to produce meaningful ideas. In Math, but I'd argue in other areas as well (see Rilke)

I can't express to you how much you have to read this book. It is just extraordinary.

# Type 2: External restrictions on your creativity [​](#type-2-external-restrictions-on-your-creativity)

Type 2 self-restriction is external, and looks a lot like peer pressure or audience capture. And whether you're a creator with an audience or not doesn't matter. What matters are the expectations placed on you.

And the real danger isn't the expectations you recognize—*it's the invisible ones.* Expectations from peers, family, friends, and work.

They don't just restrict what you're allowed to write or say. They restrict what you feel comfortable thinking. They limit how you approach problems or conceive solutions. You end up thinking only within the bounds of what's acceptable to those around you. You stop feeling creative. You stop having ideas. All because you've self-limited.

To do your best work, you need both types of freedom. You must separate yourself—go into isolation. A quiet office or library will suffice.

> What is necessary, after all, is only this: solitude, vast inner solitude. To walk inside yourself and meet no one for hours—that is what you must be able to attain. Rainer Maria Rilke

You should try to enter a state of pure, young-minded, unbridled curiosity. True authentic exploration and imagination. That's Type 1 freedom. Imagine it flowing from you, spilling out, uncontrolled. Type 2 freedom means escaping external factors that shape and limit what emerges from you.

Here's the complication, which utterly fascinates me: Excessive Type 2 limitations can actually destroy your Type 1 creativity.

It's as if Type 2 limitations recognize the dangerous ideas lurking within pure, childlike curiosity. They know that unrestricted creativity might produce thoughts that "those people" wouldn't approve of.

# Type 3: The anchoring restriction [​](#type-3-the-anchoring-restriction)

I just wrote [a new piece about the two primary limitations to creativity](/blog/two-creativity-barriers). You should check it out. But after finishing it I realized there was a third limitation, which is not even thinking about some options for creating a new solution, or solving a problem, because it was previously impossible.

# The analytics awakening [​](#the-analytics-awakening)

Let me give you my example from yesterday, while I was working on this newsletter. I was wishing I could get more from Fathom Analytics, which was my web analytics replacement for Google Analytics since it became total shit, and for Chartbeat since they became hundreds of dollars per month.

Chartbeat has always been my favorite analytics platform

Chartbeat has always been my favorite web analytics platform. It's gorgeous. It's dynamic. And most importantly—it counts pages that people are reading, not just the initial page load. In other words, it works how it's supposed to.

So yesterday I was looking at my Fathom interface and I'm like wait…could I just replace Chartbeat myself?

# The build [​](#the-build)

So I made this.

[![Analytics Dashboard](/images/analytics-dashboard.png)](/images/analytics-dashboard.png)

My custom analytics platform showing real-time visitor data

Oh, and I made a menu bar visual using Swift, which is way better than what I had with Fathom. That took less than minutes.

[![Menu Bar Analytics](/images/menubar-analytics.png)](/images/menubar-analytics.png)

The 🔥 142 bit

# The results [​](#the-results)

So let me be clear. I replaced Google Analytics and Chartbeat in a couple of hours (just visual tweaking after I had the main functionality in less than 20 minutes), and I have **WAY MORE** of my desired features than both of them combined. It's literally better for me in every way.

I now have:

* **Historical metrics** (which Chartbeat didn't have)
* **Realtime true metrics** (which Google Analytics didn't have)
* **A MacOS menubar item** (which neither of them had)
* **Infinite customization ability**

 The skill was in speccing it out given what I already knew about analytics.

I just replaced two SaaS apps that I've used for years. And I just kind of casually made it happen while I was reading stories and writing the newsletter.

It took a good amount of skill to Spec Code the thing via prompting (because I understand how the JS had to work, etc.), but Kai then took that and wrote the whole thing for me once he had that.

# Two realizations [​](#two-realizations)

So, two things:

1. **Holy crap this is nuts**
2. **We need to completely reframe what's possible now**

I have literally thought about wanting to replace Chartbeat *hundreds* of times prior to November of 2022. I just didn't have the time to do all those separate pieces, plus have the UI skills to make it look good. We're talking about:

* The analytics JavaScript itself
* The listener services
* The database
* The storage of the metrics
* The queries against the endpoints
* And then the GUI

18 minutes.

That's how long it took to go from:

> Hey, ...