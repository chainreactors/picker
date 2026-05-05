---
title: Content for Content’s Sake
url: https://lucumr.pocoo.org/2026/5/4/content-for-contents-sake/
source: Armin Ronacher's Thoughts and Writings
date: 2026-05-04
fetch_date: 2026-05-05T05:03:15.892562
---

# Content for Content’s Sake

[Armin Ronacher](/about/)'s Thoughts and Writings

* [blog](/)* [archive](/archive/)* [projects](/projects/)* [travel](/travel/)* [talks](/talks/)* [about](/about/)

# Content for Content’s Sake

written on May 04, 2026

Language is constantly evolving, particularly in some communities. Not
everybody is ready for it at all times. I, for instance, cannot stand that my
community is now constantly “cooking” or “cooked”, that people in it are “locked
in” or “cracked.” I don’t like it, because the use of the words primarily
signals membership of a group rather than one’s individuality.

But some of the changes to that language might now be coming from … machines?
Or maybe not. I don’t know. I, like many others, noticed that some words keep
showing up more than before, and the obvious assumption is that LLMs are at
fault. What I did was take 90 days’ worth of my local coding sessions and look
for medium-frequency words where their use is inflated compared to what
[wordfreq](https://github.com/tecnickcom/wordfreq) would assume their frequency
should be. Then I looked for the more common of these words and did a Google
Trends search (filtered to the US). Note that some words like “capability” are
more likely going to show up in coding sessions just because of the nature of
the problem, so the actual increase is much more pronounced than you would
expect.

You can click through it; this is what the change over time looks like. Note
that these are all words from agent output in my coding sessions that are
inflated compared to historical norms:

Loading word trend chart…

The interactive word trend chart requires JavaScript.

Something is going on for sure. Google Trends, in theory, reflects words that
people search for. In theory, maybe agents are doing some of the Googling, but
it might just be humans Googling for stuff that is LLM-generated; I don’t know.
This data set might be a complete fabrication, but for all the words I checked
and selected, I also saw an increase on Google Trends.

So how did I select the words to check in the first place? First, I looked for
the highest-frequency words. They were, as you would expect, things like “add”,
“commit”, “patch”, etc. Then I had an LLM generate a word list of words that
it thought were engineering-related, and I excluded them entirely from the list.
Then I also removed the most common words to begin with. In the end, I ended up
with the list above, plus some other ones that are internal project names. For
instance, [habitat](https://earendil-works.github.io/absurd/tools/habitat/) and
[absurd](https://earendil-works.github.io/absurd/), as well as some other internal
code names, were heavily over-represented, and I had to remove those. As you
can see, not entirely scientific. But of the resulting list of words with a
high divergence compared to wordfreq, they *all* also showed spikes on Google
Trends.

There might also be explanations other than LLM generation for what is going on,
but I at least found it interesting that my coding session spikes also show up
as spikes on Google Trends.

## The Rise of LLM Slop

The choice of words is one thing; the way in which LLMs form sentences is
another. It’s not hard to spot LLM-generated text, but I’m increasingly
worried that I’m starting to write like an LLM because I just read so much more
LLM text. The first time I became aware of this was that I used the word
“substrate” in a talk I gave earlier this year. I am not sure where I picked it
up, but I really liked it for what I wanted to express and I did not want to use
the word “foundation”. Since then, however, I am reading this word everywhere.
This, in itself, might be a case of the [Baader–Meinhof
phenomenon](https://en.wikipedia.org/wiki/Frequency_illusion), but you can also
see from the selection above that my coding agent loves substrate more than it
should, and that Google Trends shows an increase.

We have all been exposed to LLM-generated text now, but I feel like this is
getting worse recently. A lot of the tweet replies I get and some of the Hacker
News comments I see read like they are LLM-generated, and that includes people
I know are real humans. It’s really messing with my brain because, on the one
hand, I really want to tell people off for talking and writing like LLMs; on the
other hand, maybe we all are increasingly actually writing and speaking like
LLMs?

I was listening to a talk recording recently (which I intentionally will not
link) where the speaker used the same sentence structure that is
over-represented in LLM-generated text. Yes, the speaker might have used an LLM
to help him generate the talk, but at the same time, the talk sounded natural.
So either it was super well-rehearsed, or it was natural.

## Engage and Farm

At least on Twitter, LinkedIn, and elsewhere, there is a huge desire among
people to write content and be read. Shutting up is no longer an option and,
as a result, people try to get reach and build their profile by engaging with
anything that is popular or trending. In the same way that everybody has
gazillions of Open Source projects all of a sudden, everybody has takes on
everything.

My inbox is a disaster of companies sending me AI-generated nonsense and I now
routinely see AI-generated blog posts (or at least ones that look like they are
AI-generated) being discussed in earnest on Hacker News and elsewhere.

Genuine human discourse had already been an issue because of social media
algorithms before, but now it has become incredibly toxic. As more and more
people discover that they can use LLMs to optimize their following, they are
entering an arms race with the algorithms and real genuine human signal is
losing out quickly. There are entire companies now that just exist to [automate
sending LLM-generated shit](https://polsia.com/) and people evidently pay money
for it.

## Speed Should Kill

If we take into account the idea that the highest-quality content should win
out, then the speed element would not matter. If a human-generated comment
comes in 15 minutes after a clanker-generated one, but outperforms it by being
better, then this whole LLM nonsense would show up less. But I think that
LLM-generated noise actually performs really well. We see this plenty with Open
Source now. Someone builds an interesting project, puts it on GitHub and within
hours, there are “remixes” and “reimplementations” of that codebase. Not only
that, many of those forks come with sloppy marketing websites, paid-for domains,
and a whole story on socials about why this is the path to take.

I have complained before that Open Source is quickly deteriorating because
people now see the opportunity to build products on top of useful Open Source
projects, but the underlying mechanics are the same as why we see so much LLM
slop. Someone has a formed opinion (hopefully) at lunch, and then has a
clanker-made post 3 minutes later. It just does not take that much time to
build it. For the tweets, I think it’s worse because I suspect that some people
have scripts running to mostly automate the engagement.

And surely, we should hate all of this. These low-effort posts, tweets, and Open
Source projects should not make it anywhere. But they do! Whatever they play
into, whether in the algorithms or with human engagement, they are not punished
enough for how little effort goes into them.

## Friction and Rate Limiting

That increases in speed and ease of access can turn into problems is a
long-understood issue. ID cards are a very unpopular thing in the UK because
the British are suspicious of misuse of a central database after what happened in
Nazi Germany. Likewise the US has the Firearm Owners Protection Act from 1986,
which also bans the US from creating a central database of gun owners. The
gun-tracing methodologies that result from not having such a database [look like
something out of a Wes Anderson movie](https://www.youtube.com/watch?v=rMQ2b6ZwwCU).
We have known for a long time that certain t...