---
title: decomplexifying curl
url: https://daniel.haxx.se/blog/2024/10/27/decomplexifying-curl/
source: daniel.haxx.se
date: 2024-10-28
fetch_date: 2025-10-06T18:49:12.180181
---

# decomplexifying curl

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2024/10/daniel-mountain.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# decomplexifying curl

[October 27, 2024](https://daniel.haxx.se/blog/2024/10/27/decomplexifying-curl/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

(I wrote about this topic in [my weekly email](https://lists.haxx.se/listinfo/daniel) this week. This is the blog version, somewhat extended.)

## Easy to read

Two contributing factors that make code hard to read are *function length* and *function complexity*. To keep source code easy to read, understand and debug we should strive towards keeping functions short and simple. Nothing ground-breaking in that conclusion.

I know, it sounds really simple and straight forward but in a living project that goes on for decades, code develops, moves and grows over time. What started out small and simple risk gradually turning into something else.

This of course because there are so many more factors involved that need to be given focus as well. Like security, bugfixes, performance, food on the table and getting more people involved.

## Graphs graphs graphs

Last week I added two more graphs to [the curl dashboard](https://curl.se/dashboard.html) showing function complexity and function length growth in curl code over the decades: one plot for the worst function and one plot for the 99th percentile in each graph. For both graphs, the 99th percentile plots shrink gradually over time but the worst offenders grow. This means that there are a few functions that with attention could improve readability and code maintainability but that in general things are under control.

One of the main points for me with graphing the project from as many angles as possible is to unveil things like this. Areas that might need attention, and then keep a check on these areas going forward. Details like these are otherwise rather subtle and not easily detected when manually browsing around.

It has been said that whatever measurement you use to track engineering progress, that will then become the goal for what engineers work towards. I hope to combat this by measuring (and graphing) as many angles as possible of the curl project. To help push us in the right direction in as many different areas as possible.

## Improve

I took it upon myself to improve the situation: to reduce the size of the largest function in the code base and to simplify the most complex one. Incidentally they were different functions: the largest function was the big switch handling [curl\_easy\_setopt](https://curl.se/libcurl/c/curl_easy_setopt.html) options, and the most complex one was the main curl tool function setting up a single transfer.

These two functions had simply just slowly and consistently been growing over time, in size and complexity. No one’s “fault” really and not with any specific plan or intention. The graph helped me decide to act and the *pmccabe* tool helped me identify them. We can of course argue about the specific method or number that pmccabe presents for complexity, but I think it at least is pretty good at actually identifying the correct functions and the exact particular score it sets is not terribly important.

Both pull-requests became > 2000 modified lines monsters, but they also had immediate and distinct effects on the graphs; which ideally should mean that the code readability is now a little better than before, making the functions easier to improve and work with going forward

## Complexity

The single worst function in production code had gotten quite complex. I spent a work day on the case and look at the drop on the right edge of the graph below, made after my fix landed. Most of the job was to properly split the function into several smaller ones that made sense.

The single worst offender at this particular time was the function in the curl tool that sets up a single transfer job.

![](https://daniel.haxx.se/blog/wp-content/uploads/2024/10/Screenshot-2024-10-25-at-10-23-03-curl-Project-status-dashboard.png)

There are still some pretty complex ones remaining. Room for further improvements no doubt.

## Function length

The worst offenders in terms of function size in curl have been of two kinds: state machines with many states and functions handling big switches for options.

In this particular case, this was the big function handling curl\_easy\_setopt(), and as we have over three hundred options having them all handled in a single function made it very big. The new setup splits that handling up into multiple smaller functions, one for each kind of input.

![](https://daniel.haxx.se/blog/wp-content/uploads/2024/10/Screenshot-2024-10-25-at-10-26-02-curl-Project-status-dashboard.png)

The largest one is now at over 1,500 lines. Still on the too large side of things but way better than before.

## Going forward

Yes, I am a *graphaholic* and I seem to keep finding new ways to illustrate project status and development using plots on timelines. I am also most likely the biggest consumer of these graphs as I monitor them daily to make sure I have full control of how we are in the project, in every imaginable aspect.

I intend to try to continue simplifying a few more of the functions in the pmccabe toplist.

Let’s see what the graph shows in another three years.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[Development](https://daniel.haxx.se/blog/tag/development/)[statistics](https://daniel.haxx.se/blog/tag/statistics/)

# Post navigation

[Previous PostUndefinedBehaviorSanitizer’s unexpected behavior](https://daniel.haxx.se/blog/2024/10/17/undefinedbehaviorsanitizers-unexpected-behavior/)[Next PostEighteen years of ABI stability](https://daniel.haxx.se/blog/2024/10/30/eighteen-years-of-abi-stability/)

# Recent Posts

* [How I maintain release notes for curl](https://daniel.haxx.se/blog/2025/10/01/how-i-maintain-release-notes-for-curl/)
  October 1, 2025
* [CRA compliant curl](https://daniel.haxx.se/blog/2025/09/22/cra-compliant-curl/)
  September 22, 2025
* [Bye bye Kerberos FTP](https://daniel.haxx.se/blog/2025/09/19/bye-bye-kerberos-ftp/)
  September 19, 2025
* [From suspicion to published curl CVE](https://daniel.haxx.se/blog/2025/09/18/from-suspicion-to-published-curl-cve/)
  September 18, 2025
* [Developer of the year](https://daniel.haxx.se/blog/2025/09/13/developer-of-the-year/)
  September 13, 2025
* [curl 8.16.0](https://daniel.haxx.se/blog/2025/09/10/curl-8-16-0/)
  September 10, 2025

# Recent Comments

* F.Nagy on [Developer of the year](https://daniel.haxx.se/blog/2025/09/13/developer-of-the-year/comment-page-1/#comment-27323)
* Fredrik on [Developer of the year](https://daniel.haxx.se/blog/2025/09/13/developer-of-the-year/comment-page-1/#comment-27322)
* [Fazal Majid](https://majid.info/) on [preparing for the worst](https://daniel.haxx.se/blog/2025/09/09/preparing-for-the-worst/comment-page-1/#comment-27321)
* Nikhil on [About](https://daniel.haxx.se/blog/about/comment-page-1/#comment-27320)
* A. Ros on [car brands running curl](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/comment-page-1/#comment-27318)
* [Daniel Stenberg](https://daniel.haxx.se/) on [car brands running curl](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/comment-page-1/#comment-27317)
* Yoann Ricordel on [HTTP is not simple](https://daniel.haxx.se/blog/2025/08/08/http-is-not-simple/comment-page-1/#comment-27316)
* Ond?ej Surý on [Hello Sprout](https://daniel.haxx.se/blog/2025/07/28/hello-sprout/comment-page-1/#comment-27315)
* H. S...