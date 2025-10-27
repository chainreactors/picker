---
title: Hacking the “Bike Angels” System for Moving Bikeshares
url: https://www.schneier.com/blog/archives/2024/09/hacking-the-bike-angels-system-for-moving-bikeshares.html
source: Schneier on Security
date: 2024-09-24
fetch_date: 2025-10-06T18:30:49.124077
---

# Hacking the “Bike Angels” System for Moving Bikeshares

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

## Hacking the “Bike Angels” System for Moving Bikeshares

I always like a good hack. And [this story](https://www.nytimes.com/2024/09/19/nyregion/citi-bike-scam-nyc.html?smid=nytcore-android-share) delivers. Basically, the New York City bikeshare program has a system to reward people who move bicycles from full stations to empty ones. By deliberately moving bikes to create artificial problems, and exploiting exactly how the system calculates rewards, some people are making a lot of money.

> At 10 a.m. on a Tuesday last month, seven Bike Angels descended on the docking station at Broadway and 53rd Street, across from the Ed Sullivan Theater. Each rider used his own special blue key -­- a reward from Citi Bike—­ to unlock a bike. He rode it one block east, to Seventh Avenue. He docked, ran back to Broadway, unlocked another bike and made the trip again.
>
> By 10:14, the crew had created an algorithmically perfect situation: One station 100 percent full, a short block from another station 100 percent empty. The timing was crucial, because every 15 minutes, Lyft’s algorithm resets, assigning new point values to every bike move.
>
> The clock struck 10:15. The algorithm, mistaking this manufactured setup for a true emergency, offered the maximum incentive: $4.80 for every bike returned to the Ed Sullivan Theater. The men switched direction, running east and pedaling west.

Nicely done, people.

Now it’s Lyft’s turn to modify its system to prevent this hack. Thinking aloud, it could try to detect this sort of behavior in the Bike Angels data—and then ban people who are deliberately trying to game the system. The detection doesn’t have to be perfect, just good enough to catch bad actors most of the time. The detection needs to be tuned to minimize false positives, but that feels straightforward.

Tags: [hacking](https://www.schneier.com/tag/hacking/), [noncomputer hacks](https://www.schneier.com/tag/noncomputer-hacks/), [scams](https://www.schneier.com/tag/scams/)

[Posted on September 23, 2024 at 11:46 AM](https://www.schneier.com/blog/archives/2024/09/hacking-the-bike-angels-system-for-moving-bikeshares.html) •
[11 Comments](https://www.schneier.com/blog/archives/2024/09/hacking-the-bike-angels-system-for-moving-bikeshares.html#comments)

### Comments

yet another bruce •
[September 23, 2024 5:19 PM](https://www.schneier.com/blog/archives/2024/09/hacking-the-bike-angels-system-for-moving-bikeshares.html/#comment-440709)

I wonder if it would be possible to construct a naturally robust system by always considering the state of the originating station and the state of the terminating station in the cost of any. This means that trips originating from a nearly empty station would be more expensive as would trips terminating in a nearly full station. I imagine you would want a smooth function to avoid exploits based on quantization or thresholds and you would want to adjust price frequently. Fifteen minutes between updates seems very slow.

You could still pay angels to move bikes since trips originating in very full stations or ending in mostly empty stations could be assigned a negative cost.

Erdem Memisyazici •
[September 24, 2024 12:31 AM](https://www.schneier.com/blog/archives/2024/09/hacking-the-bike-angels-system-for-moving-bikeshares.html/#comment-440716)

If you allow it, it could be exploited. There are entire communities who can round up at least 100 people in one hour who would gladly ride a bike for $5 across one block. Gone are the days of genuine crowds when we now have these group think enabling devices all in the hands of the general public leading to cheap astroturfing and the like as common occurrences.

It used to be solely done by state level actors to gather fake crowds and stage the appearance of uprisings yet now every Joe has an app for it. Not to mention medical networks on the rise that monitor the mental health of an entire area (a bit harsh for the privacy conscious). Private groups that do the same for law enforcement, neighborhood watch groups, or just students in a frat who can also gather a crowd to call the first group of 100 bike riders “silly sods” the whole way across the block but they get paid better.

It’s ridiculous what a fast communications network and a bad economy can lead to.

Bike rider •
[September 24, 2024 3:12 AM](https://www.schneier.com/blog/archives/2024/09/hacking-the-bike-angels-system-for-moving-bikeshares.html/#comment-440717)

Clearly the reward could be less for an empty station when there are full stations very close by. Regular bike users can easily walk a block to the full station, so the empty one isn’t as much of an emergency as it would be if it was a more isolated one. The exploit depends on the short distance.

Winter •
[September 24, 2024 3:41 AM](https://www.schneier.com/blog/archives/2024/09/hacking-the-bike-angels-system-for-moving-bikeshares.html/#comment-440718)

Sounds like yet another example of the Cobra Effect [1]:

> The term cobra effect was coined by economist Horst Siebert based on an anecdotal occurrence in India during British rule. The British government, concerned about the number of venomous cobras in Delhi, offered a bounty for every dead cobra. Initially, this was a successful strategy; large numbers of snakes were killed for the reward. Eventually, however, people began to breed cobras for the income. When the government became aware of this, the reward program was scrapped. When cobra breeders set their snakes free, the wild cobra population further increased. This story is often cited as an example of Goodhart’s law or Campbell’s law.

It has often been shown that monetary rewards for volunteering activities people do as good citizens (ie, intrinsic motivations) reduces their motivation for doing the volunteering. [2] So, a reward scheme for “Bike Angels” will not attract more “Angels”, but more grifters, as is shown.

[1] ‘https://en.wikipedia.org/wiki/Perverse\_incentive#cite\_note-schwarz22-4

[2] ‘https://www.researchgate.net/publication/2392860\_Does\_Pay\_Motivate\_Volunteers

> But we obtain the puzzling result that, when rewarded, volunteers work less. These findings are in line with a large literature in social psychology emphasizing that external rewards can undermine the intrinsic motivation for an activity.

arf'n'arf •
[September 24, 2024 5:34 AM](https://www.schneier.com/blog/archives/2024/09/hacking-the-bike-angels-system-for-moving-bikeshares.html/#comment-440719)

Obviously, the Bike Angels shouldn’t be able to use their blue key to drop bikes at a station that doesn’t need them.

The problem is that the blue key is used to permit bike removal not bike drop off. If that problem was fixed then everything would work nicely.

branden •
[September 24, 2024 10:55 AM](https://www.schneier.com/blog/archives/2024/09/hacking-the-bike-angels-system-for-moving-bikeshares.html/#comment-440730)

> Now it...