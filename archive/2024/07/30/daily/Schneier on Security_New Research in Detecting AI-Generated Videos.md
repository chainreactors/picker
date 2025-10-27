---
title: New Research in Detecting AI-Generated Videos
url: https://www.schneier.com/blog/archives/2024/07/new-research-in-detecting-ai-generated-videos.html
source: Schneier on Security
date: 2024-07-30
fetch_date: 2025-10-06T17:47:16.083962
---

# New Research in Detecting AI-Generated Videos

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## New Research in Detecting AI-Generated Videos

The [latest](https://www.livescience.com/technology/artificial-intelligence/new-ai-algorithm-flags-deepfakes-with-98-accuracy-better-than-any-other-tool-out-there-right-now) in what will be a continuing arms race between creating and detecting videos:

> The new tool the research project is unleashing on deepfakes, called “MISLnet”, evolved from years of data derived from detecting fake images and video with tools that spot changes made to digital video or images. These may include the addition or movement of pixels between frames, manipulation of the speed of the clip, or the removal of frames.
>
> Such tools work because a digital camera’s algorithmic processing creates relationships between pixel color values. Those relationships between values are very different in user-generated or images edited with apps like Photoshop.
>
> But because AI-generated videos aren’t produced by a camera capturing a real scene or image, they don’t contain those telltale disparities between pixel values.
>
> The Drexel team’s tools, including MISLnet, learn using a method called a constrained neural network, which can differentiate between normal and unusual values at the sub-pixel level of images or video clips, rather than searching for the common indicators of image manipulation like those mentioned above.

Research [paper](https://arxiv.org/pdf/2404.15955).

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [AI](https://www.schneier.com/tag/ai/), [deepfake](https://www.schneier.com/tag/deepfake/), [videos](https://www.schneier.com/tag/videos/)

[Posted on July 29, 2024 at 7:02 AM](https://www.schneier.com/blog/archives/2024/07/new-research-in-detecting-ai-generated-videos.html) •
[10 Comments](https://www.schneier.com/blog/archives/2024/07/new-research-in-detecting-ai-generated-videos.html#comments)

### Comments

Clive Robinson •
[July 29, 2024 9:00 AM](https://www.schneier.com/blog/archives/2024/07/new-research-in-detecting-ai-generated-videos.html/#comment-439678)

@ Bruce, ALL,

Re : Demise of an arms race.

> “The latest in what will be a continuing arms race”

History shows us that even in a war arms races come to an end.

With the winner generally being the side with,

1, Greatest technological capacity.

Because of two reasons,

The first is an arms race gets expensive to some power law for each increment in capability.

The second is some technology obsoletes the technology the arms race is based on, and effectively a new arms race begins.

Perhaps not as well known as it should be but LLM AI systems in their current form have got beyond the size where the laws of physics and basic geometry allow simple scaling up, because whilst much can be done in parallel not every thing can and it takes quite a while for a signal to get from one corner of a cube to the furthest corner.

A grain of sand is considered about 1pS or picosecond in size and a one foot length 1nS or nano-second. As these are the times it takes light in freespace to travel these distances.

But there is also a density issue. Such electronics draws a European sized countries worth of electricity and in terms of power in to power out current LLMs are about as inefficient as it gets. Which means that most of that input power becomes heat. Air is not a particularly good conductor of heat and even though water is better it has a lot of disadvantages. Copper silver, gold and diamond do a much better job as conductors of heat but there are other limits on their use.

So even with optimal step down techniques to move the heat away, only about 1/10,000th of any given volume can be considered as being computing volume often less a lot less.

I could give other reasons for why current LLM AI systems are hitting the cost and resource brick walls of physics but that’s not really that interesting. We know it’s going to happen and realistically when even with significant algorithmic improvements.

What is interesting is the second way Arms Races end, that is how the current LLM systems Arms Race will be replaced with a new AI arms race. For the cycle to start all again.

Oh and at some point when things move to Carbon and potentially Iron based systems as Silicon and Aluminium reach their limits.

Clive Robinson •
[July 29, 2024 9:32 AM](https://www.schneier.com/blog/archives/2024/07/new-research-in-detecting-ai-generated-videos.html/#comment-439679)

@ Bruce, ALL,

Re : Is it plagiarism or coincidence?

I suspect some of you remember that a little while ago I pointed out a certain “naughty wordlist” member was a term of art in a knowledge domain.

And that it was a more correct if not appropriate word to use than “Hallucinate” for LLM AI systems churning out nonsense…

Well it looks like others are picking up on this and on 25th July just last week put up,

<https://www.livescience.com/technology/artificial-intelligence/ai-isnt-hallucinating-its-bullshitting>

It’s basically what I’d said “fleshed out” because they had a little more space to fill 😉

Anyway there is an “original paper / publication” at,

<https://link.springer.com/article/10.1007/s10676-024-09775-5>

That I amplified a little.

For various reasons I suggest the use of “the correct term of art”. As it might help the general public get their head around things. After all most humans BS a lot as a form of humour or for comical effect and it’s seen as “a human thing to do”. Whereas few humans hallucinate without their being some aberrant cause. Thus it’s seen as something dark and dangerous for which people get locked away for.

Winter •
[July 29, 2024 10:05 AM](https://www.schneier.com/blog/archives/2024/07/new-research-in-detecting-ai-generated-videos.html/#comment-439680)

> The latest in what will be a continuing arms race between creating and detecting videos:

Like every arms race, the limits on this arms race will be set by resource limitations. Especially, the difficulty of collecting training data and the cost of training ever larger models on ever larger training sets will become a problem.

Obviously, people will have to “work smarter, not harder” 😉

Gert-Jan •
[July 30, 2024 6:32 AM](https://www.schneier.com/blog/archives/2024/07/new-research-in-detecting-ai-generated-videos.html/#comment-439691)

In the long run, I think it’s impossible for detection software to determine that something is AI generated.

But that’s a bit besides the point. First of all, such detection system can only guarantee (or least indicate with high degree of certainty) that the work has been manipulated. It can’t guarantee that something was created without any such manipulation (false negatives).

Research has shown that fact checking social media posts is a process that does not work very well to prevent the spread is misinformation and disinformation.

Something similar applies here. There will always be a delay between some...