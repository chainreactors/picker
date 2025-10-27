---
title: Scaling Mastodon is Impossible
url: http://lucumr.pocoo.org/2022/11/14/scaling-mastodon
source: Armin Ronacher's Thoughts and Writings
date: 2022-11-15
fetch_date: 2025-10-03T22:42:28.678310
---

# Scaling Mastodon is Impossible

[Armin Ronacher](/about/)'s Thoughts and Writings

* [blog](/)* [archive](/archive/)* [projects](/projects/)* [travel](/travel/)* [talks](/talks/)* [about](/about/)

# Scaling Mastodon is Impossible

written on November 14, 2022

In light of [recent events at Twitter](https://en.wikipedia.org/wiki/Acquisition_of_Twitter_by_Elon_Musk) a
lot of the people that I follow (or used to follow) on that platform have
started evaluating (or moved) to [Mastodon](https://en.wikipedia.org/wiki/Mastodon_%28software%29). And [I also
have a Mastodon account now](https://hachyderm.io/%40mitsuhiko). But
after a few days with this thing I have a lot of thoughts on this that are
too long for a Tweet or Toot. Since some of my followers asked though I
decided do a longform version of this and explain my dissatifaction with
Mastodon a bit better.

The short version of this is that I believe that Mastodon — more
specifically federation and decentralization won’t work out.

## My Claim: Decentralization is a Questionable Goal

In the last few years a lot of centralized services did not develop like
people wanted which I believe resulted in the pendulum prominently swinging
towards decentralization.

Decentralization promotes an utopian view of the world that I believe fails
to address actual real problems in practice. Yet on that decentralization
wave a lot of projects are riding from crypto-currencies [1](#fn-1), defi or things
such as Mastodon. All of these things have one thing in common: distrust.
Some movements come from the distrust of governments or taxation, others
come from the distrust of central services.

In my mind the discussion about centralization and decentralization
completely misses the point of the intended outcomes. Centralization or
decentralization should really be an implementation detail of the solution
to an actual problem. For that particular problem the solution might be
one of those two things, or something in the middle. But out of principle
it should be neither of those two things.

I rather understand what exactly the goals are that should be solved, and
out of that the right approach on a technical level can be found.

## What are we trying to solve?

Let’s ignore Twitter for a second and let’s talk about software
engineering. Specifically dependency management. I think dependency
management is an interesting proxy for the problem here and there are some
lessons to be learned from it. As a frequent reader of this blog you
might remember me writing quite a lot about [scaling](/2022/1/10/dependency-risk-and-funding/) [code](/2019/7/29/dependency-scaling/) [dependencies](/2016/3/24/open-source-trust-scaling/). When I started writing Python
developers used much fewer dependencies than today. When you did use
dependencies, it was your own problem to figure out how to get it as
automated depencency downloading originally was not a thing yet. The
Python tools over time gained the ability to declare dependencies and
they were able to pick them up from PyPI (or the cheese-shop as it was
frequently called) but we did not yet have centralized package hosting.

We used to self host our dependencies. Even if we did not necessarily
want to pay for the hosting cost, we had to host them. Many picked
third party websites such as SourceForge, Berlios or others to avoid
paying the cost of traffic. This decentralization however came with a lot
of challenges and today decentralized package hosting is no longer
supported by the Python ecosystem. This did not happen, because PyPI
turned evil and really wanted to kill decentralized package hosting,
but because it turns out that decentralized hosting came with a lot of
challenges.

For one as time went on, a lot of these packages went away because the
hosts they were hosted on shut down. So the first cracks that showed up
just was an effect of things ageing. People walk away of projects, in
some cases die and with that, their server bills go unpaid and domains
eventually lapse. Some companies also go out of business. SourceForge
did not really ever die, but they had financial challenges and made their
hosting page ever more hostile for the installers to give access to the
uploaded tarballs.

The second thing that became apparent over time was also that
decentralized services came with a lot of security risks. Every one of
those hosts allowed the re-publishing of already existing packages.
Domains that lapsed could be re-registered by other people and new
packages could be placed there.

NPM and PyPI today can help secure the ecosystem by setting minimum
standards or by resurrecting accidentally published packages or to yank
hacked versions. These are all clear benefits that we all get something
from as community.

Now a lot of these issues can be solved in a decentralized design, but
really there was a good reason why it went away, even in the entire
absence of a bad player!

Obviously there are nuances here and it’s clear that central services come
with risks, but so do decentralized services and they don’t have clear
upsides. On decentralized systems in particular I encourage you to read
[Moxie’s take on web3](https://moxie.org/2022/01/07/web3-first-impressions.html) which
outlines the challenges of this much better than I ever could. In
particular it makes two very important points, namely that people don’t
like self hosting (at scale) and that it’s easier to move platforms than
(decentralized) protocols. The latter in particular is also something
that the Python ecosystem learned. PyPI today offers more secure
checksums than when Python originally started out. It also has more
stringient rules around package names and unpublishing. These are all
protocol decisions that i was able to push out because the python
packaging infrastructure in Python is rather tighly controlled.

You might now get the impression that I’m really into centralization. I’m
not really, but I think my position here is complicated. Going back to
the topic of decentralized dependency hosting you might remember that I
was recently [quite critical of PyPI](/2022/7/9/congratulations/). I’m
very well aware that a centralized service comes with risks and that you
need to follow whatever rules that service sets.

Decentralization is appealing, particularly when things are very
centralized and we’re exposed to it’s faults much more.

In my mind in recent years decentralization mostly gained a lot of popular
support because of the erosion of society. There is a backlash by some
against western governments which are seen as behaving irresponsibly with
regulatory over-reach, increasing levels of corruption, decreasing quality
of public services and frustration about taxation. And there is some
merit to these ideas. There is also a proxy war going on about freedom of
speech and expression and the desire to create safe spaces. I welcome you
to watch Jonathan Haidt’s talk about [the moral roots of liberals and
conservatives](https://www.youtube.com/watch?v=8SOQduoLgRw) for a bit
of context on that.

So really before we talk about centralization and decentralization, I
think we actually need to understand what we want to accomplish. And
really I think this is where we likely already disagree tremendously.
Mastodon encourages not just decentralization, but federation. You can
pick your own mastodon server but you can also communicate with people on
other instances. I will make the point that **this is the root of the
issue here**.

## We can’t agree

So let’s talk more about Mastodon here. I have been using this for a few
weeks now in different ways and it’s pretty clear that this thing is
incredibly brittle. The ActivityPub is a pretty messy protocol, and
it also appears to not have been written with scalability in mind much.
The thing does not scale to the number of users it currently has and there
is probably no trivial way to fix it up.

But before we even hit the issue of the technology, we hit the issue of
there being absolutely no agreement of what ...