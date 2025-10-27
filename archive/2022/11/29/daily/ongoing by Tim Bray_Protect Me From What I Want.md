---
title: Protect Me From What I Want
url: https://www.tbray.org/ongoing/When/202x/2022/11/28/On-Algorithms
source: ongoing by Tim Bray
date: 2022-11-29
fetch_date: 2025-10-03T23:58:05.315098
---

# Protect Me From What I Want

# Protect Me From What I Want

Search

*[This fragment is available in [an audio version](On-Algorithms.mp3).]*

Over on Mastodon, there are many people who enjoy not being in the grip of software like Facebook or Twitter that
single-mindedly tries to maximize “engagement”, which means the amount of time you stare at the screen so they can show you
ads. These algorithms don’t care *what* they’re showing you and if it turns out that showing you exclusively stories
vilifying or praising Donald Trump (depending) maximizes engagement, then that’s what you’ll see. So the chant over there is
“No algorithms on Mastodon!” This chant is wrong, and the discussion around it teaches us that we need clarity on what
algorithms are, what moral weight they can carry, and whether they can be avoided. (Spoiler: They can’t.)

This all started when I interjected
[here](https://mastodon.cloud/%40timbray/109419423801575664), and the longest and most twisted Mastodon thread I have
so far seen ensued. Let’s start with my initial remarks:

> I disagree. An algorithm is not intrinsically bad. As long as we understand that it represents the interests of
> whoever paid to have it constructed. I think an algorithm with human values that simply wanted to enrich experience is perfectly
> possible.
>
> I haven't seen one, probably because nobody has ever had a financial incentive to construct it.
>
> Mastodon would be a good place to try to make one.

In the following discussion I’m going to use Mastodon terminology: “Boost” is a synonym for “Retweet” and “Favorite” for
“Like”.

What an algorithm is and why there will always be one ·
Consider a Mastodon instance that is engaged in creating a feed for, well, you, because you’ve just opened that tab or app.
It gets the list of who you follow, probably finds some of those posts already in its memory, and reaches out to other Mastodon
instances for the rest. It ends up with a big jumbled unsorted list of what could go in your feed. “Good,” you say, “just sort them
in reverse chronological order and we’re done. Don’t talk to me about algorithms!”

Well, first of all, sorting
[is an algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm), and not a simple one at that.

But it’s not
that simple. Suppose one post from someone you don’t follow has been boosted by 5 people that you do, all at different
times. Does it appear just once in your feed (and using which boost timestamp?) or five times? Neither answer is obviously
right, but when you make that choice, you’re designing an algorithm.

Some of the posts are replies to each other, and to you. Do they appear right next to each other or in strict
chronological order, mixed up with other posts? If you’re going to thread them together, do you do that in chronological not
reverse-chronological order? Welcome to the world of algorithm design.

I guarantee the algorithm that generates “simple chronological order” isn’t simple at all. Among other things, it
handles lots of corner cases other than the ones I just mentioned, that nobody is smart enough to think of until they actually
start writing the code to present the posts to the people.

What “engagement” algorithms are like ·
Engagement maximization, a la Facebook or Twitter, is a special and very interesting case. It begins innocently; let’s
include a few posts in your feed from people you don’t follow if those people are super-popular, or are followed by nearly all
the people you do follow, or contain hashtags that you’ve been searching for a lot. Mostly harmless, right?

But then it gets deep. These things involve the application of large-scale Machine Learning (ML) technology. The big
operators have billions of data points; they know what appears in people’s posts, and they know how long the people were
“engaged”. So, by processing those billions of data points, they produce an “ML Model” which is then exercised to answer one
question: “What selection of posts should we feed this person to keep them engaged?”

Modern ML models aren’t simple at all, and also are generally not comprehensible by humans. The people who built the model
can’t answer questions like “Why is the model feeding a lot of posts by Ben Shapiro to people who seem only mildly
conservative?” But they can prove that doing what the model says maximizes “engagement”.

A lot of people are now reacting viscerally, saying “I never want that kind of algorithm in my life.” Well, that kind of
algorithm is being used every day to filter spam out of your email. And being used on Twitter to combat Nazis and incels, to the
extent that when oppressed groups migrate to Mastodon, they get a lot more abusive bigotry. (I think we can fix that.)

[![The BMW Art Car decorated by Jenny Holzer](jenny-holzer-art-car.png "The BMW Art Car decorated by Jenny Holzer")](-big/jenny-holzer-art-car.jpg.html)

The Jenny Holzer BMW Art Car. The biggest message, “Protect Me From What I Want”, is a little hard to
read.
Borrowed from
[BMW Art Cars 15](https://www.bmwartcarcollection.com/15-jenny-holzer-bmw-art-car/).

Protect me from what I want ·
And anyhow, those algorithms are just showing you what you want. Don’t try to deny it, if it wasn’t what you wanted you
wouldn’t be doomscrolling so much, would you? These ML models know what you want and that’s what they show you.

> (Jenny Holzer is wonderful. One time many years ago I was walking across Times Square in New York and on a huge
> otherwise-blank billboard were her words: “Protect me from what I want.” It felt like someone sticking a knife into my brain;
> that phrase explains so very much.)

In whose interest? ·
In my Mastodon-post outtake above, I said that an algorithm “represents the interests of whoever paid to have it
constructed”. That’s true and, in the context of a capitalist enterprise, a fairly complete answer. But in the world of
software, things can happen outside the control of capitalist enterprises.

Open-source, for example; the algorithms in Linux
that make computers useful, or in Postgres that reliably store and retrieve data, or in Nginx that efficiently respond to Web
traffic, were
mostly written by people who found the work interesting and had a problem they needed to solve for themselves.

With the advent of the Fediverse generally and Mastodon specifically, for the first time we have a large-scale opportunity to
experiment with algorithms that are written for people by people just because they’re cool, or because they produce feeds that
the programmer likes for herself, or that her Dad likes, or that she notices causes her kids to be less obsessive about screen
time.

So let’s stop saying “No algorithms!” because that’s just wrong, and figure out how to get *nice* algorithms built,
ones that primarily are there to serve humanity’s best interests.

One thing I think we can all agree on is this: We want algorithms that (unlike every commercial social-media algorithm)
don’t tell anyone else what we’re watching!

Write your own algorithm? ·
I’ll be honest: I want the algorithm both to give me, and protect me from, what I want. And I want some control over it. I
can think of a couple of ways this could happen:

1. Someone figures out a “feed algorithm construction kit” that has a bunch of knobs on it you can twist, with labels like
   “tennis” and “activism” and “Christianity” and “keto diet” and “baroque music” and “surprise” and “pretty” and “outrage” and
   so on, and you fool with the settings until you get a feed you like.

   I think this is plausible, but very difficult.
2. Mastodon introduces a feature where you can download and install algorithms, which can be posted by anyone. They are
   given the raw unsorted list of posts from people you follow and use that produce a coherent feed. You might have to pay for
   them. They could be free. They could involve elaborate ML, or not. They might sometimes pull in posts from people you don’t
   follow. They could be open-source, or not.

   I like this idea a lot, alth...