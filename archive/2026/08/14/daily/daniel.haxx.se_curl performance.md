---
title: curl performance
url: https://daniel.haxx.se/blog/2026/08/14/curl-performance-2/
source: daniel.haxx.se
date: 2026-08-14
fetch_date: 2026-08-15T02:48:25.835325
---

# curl performance

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/07/speedometer.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl performance

[August 14, 2026](https://daniel.haxx.se/blog/2026/08/14/curl-performance-2/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [4 Comments](https://daniel.haxx.se/blog/2026/08/14/curl-performance-2/#comments)

*tldr: the live version is here: <https://curl.se/perf/>*

How fast is “fast” and is it good enough? Does it run as fast now as it did before or was there a regression? What exactly needs to be fast? How fast is it?

These are questions that many projects and products face, and in curl we are no different. Yet, performance testing and comparisons are *hard* and full of landmines and time-wasting efforts. For many years we have occasionally brought up the idea of a performance test suite for curl only to shut it down again because the challenges seemed hard and no one was volunteering to do this.

This week it changed.

## Let’s do this

I started out trying to find existing projects that host performance results for Open Source projects so that we could just feed our results something else and get great visualizations and data management. I did not find any such.

I then took a look at what existing tools there are for this purpose, and most pointers seemed to suggest that Grafana is a popular and maybe even a good solution to build something like this with. But man, that is a complicated machine and it felt more than a little overwhelming just figure out where or how to start with it. I decided to postpone that take as well.

## Let *me* do this

I decided that instead of trying to do this the best and optimal way – I shouldn’t let perfect be the enemy of good – I would start out by doing the things I know how to do and take it as far as I can one step at a time. *Something should be better than nothing*.

Performance testing needs decently stable system conditions so that repeated runs produce reasonably similar results, when all involved factors remain identical. This is basically impossibly to accomplish using most cloud infrastructure since those are almost always shared with countless other users. At least on the cheap and free tiers we use.

We probably need our own dedicated hardware for this, but instead of trying to figure out where to get that and arrange for that, I would start by running performance tests on my own local development machine. I am a single user on this and it has many cores and runs decently fast. It should be good enough to get this going on.

I created a first shell script that updates the curl source code from git, it configures and builds it. Then it runs a bunch of tests, outputs a bunch of data and logs all the output in a single log file. I started out with a few simple tests. How fast does curl download a 100 GB file from localhost, how many allocations and how big allocations does it need for a single HTTP download?

My second script parses all the test log files from the previous builds and generates summaries and graphs for them. To make it possible for humans to see how the performance changes between builds and ideally to automatically detect when something changes more than what should be tolerated.

As I am a graph addict already [since before](https://curl.se/dashboard.html), and that journey has taught me a little [gnuplot](http://www.gnuplot.info/), I decided that even while there probably are much better tools and fancy JavaScript things that *could* be used, I don’t know them and learning them now is an endeavor I rather avoid. So I stick to what I know and can get results with quickly.

A third script is invoked from a crontab every twenty minutes, sets up some variables and invokes the runner script.

Once the basics started to work, I showed my curl friends the early versions and I soon created a [new git repository for the code](https://github.com/curl/perf).

## It’s live baby

After a little more poking, I soon made my locally produced performance test summary get packaged and automatically transferred [to the curl website](https://curl.se/perf/) after each build, and voila, the first public curl performance tests were live and public.

Getting this data available immediate triggered curl developers. It only took hours until we had the first proposed changes to improve some numbers, and soon we had a few merges to that affect. Visibility really helps!

The performance numbers we get are still varying to a certain degree, partially of course because I still use my machine for my daily development things, but also because most of them do real (localhost) networking and that is by its nature a little… *varying*.

The system builds and runs a new round every twenty minutes and it does that using the latest commits from git. This setup makes it sometimes run many rounds on the same commit and it might also mean that it sometimes updates and get several new commits at once, so it might skip a round for some commits. I might reconsider this design later, but since it is still a twenty minute time window, the number of commits is still limited.

When the script makes multiple build rounds on the same commit, it accumulates the numbers and for the graph it stores the maximum, the median and the minimum value. It helps show the variation per commit and allows us to cram more into the graphs. It is still early days, but there will be a maximum limit to how many commits that can be displayed in a single graph and still be helpful.

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/08/Screenshot-2026-08-14-at-13-12-01-.png)

HTTP/2 parallel download speed through 261 builds spread over 31 build rounds

## Distribution

To help visualize the distribution and data spread per test, I created a separate illustration that shows the minimum, maximum, P25, P75, medium and mean values in a *Box-and-Whisker Plot*.

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/08/Screenshot-2026-08-14-at-13-09-58-.png)

A Box-and-Whisker Plot showing the HTTP/2 parallel download speed data distribution.

## Changing conditions

An obvious downside with me just storing build logs in files, is that it will not scale up to the millions. I did however decide that I’m not designing this system for that. At least not now.

Performance tests are highly specific and dependent on the exact machine it runs on, the exact third party libraries and their versions that are used, the other components involved in the tests, such as the servers, and more.

I expect that we will change conditions for the tests every once in a while that makes it hard to compare the current numbers with past numbers. Therefore I think the performance test numbers and values are primarily useful in the short term. To help us spot if we land something that subtly and *unintentionally* degrades something.

## Stakes

To detect extremely slow and long-term changes in performance and even making sure we can better survive wiping all the existing build logs etc, I introduced a concept I call *stakes*. As in a stake pole. A marker. An arbitrary threshold set manually for each specific test. This value can be used to measure performance test results against, now and later. As conditions change and maybe something makes the results go up or down and we are fine with those changes because they are motivated and expected, then we just change the stakes.

If it works out, I might try to have the system automatically detect and maybe highlight tests that deviate too much from its set stake (at least if do...