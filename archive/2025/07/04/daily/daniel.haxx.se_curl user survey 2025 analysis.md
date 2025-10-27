---
title: curl user survey 2025 analysis
url: https://daniel.haxx.se/blog/2025/07/03/curl-user-survey-2025-analysis/
source: daniel.haxx.se
date: 2025-07-04
fetch_date: 2025-10-06T23:51:55.214475
---

# curl user survey 2025 analysis

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2023/03/stickers-2023.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl user survey 2025 analysis

[July 3, 2025](https://daniel.haxx.se/blog/2025/07/03/curl-user-survey-2025-analysis/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [8 Comments](https://daniel.haxx.se/blog/2025/07/03/curl-user-survey-2025-analysis/#comments)

I’m pleased to announce that once again I have collected the results, generated the graphs and pondered over conclusions to make after the annual [curl user survey](https://daniel.haxx.se/blog/2025/05/19/the-curl-user-survey-2025-is-up/).

[Get the curl user survey 2025 analysis here](https://curl.se/docs/survey)

## Take-aways

I don’t think I spoil it too much if I say that there aren’t too many drastic news in this edition. I summed up ten key findings from it, but they are all more or less expected:

1. Linux is the primary curl platform
2. HTTPS and HTTP remain the most used protocols
3. Windows 11 is the most used Windows version people run curl on
4. 32 bit x86 is used by just 7% of the users running curl on Windows
5. all supported protocols are used by at least some users
6. OpenSSL remain the most used TLS backend
7. libssh2 is the most used SSH backend
8. 85% of respondents scored curl 5 out of 5 for “security handling”
9. Mastodon is a popular communication channel, and is wanted more
10. The median used curl version is just one version away from the latest

## On the process

Knowing that it is quite a bit of work, it took me a while just to get started this time – but when I finally did I decided to go about it a little different this year.

This time, the *twelfth* time I faced this task, I converted the job into a programming challenge. I took it upon me to generate all graphs with gnuplot and write the entire document using markdown (and write suitable glue code for everything necessary in between). This way, it should be easier to reuse large portions of the logic and framework for future years and it also helped me generate all the graphs in more consistent and streamlined way.

The final report could then eventually be rendered into single page HTML and PDF versions with pandoc; using 100% Open Source and completely avoiding the use of any word processor or similar. Pretty nice.

As a bonus, this document format makes it super flexible and easy should we need to correct any mistakes and generate updated follow-up versions etc in a very clean way. Just like any other release.

[Get the curl user survey 2025 analysis here](https://curl.se/docs/survey)

## A website section

It also struck me that we never actually created a single good place on the curl website for the survey. I thus created such a section on the site and made sure it features links to all the previous survey reports I have created over the years.

That new website section is what this blog post now points to for the 2025 analysis. Should thus also make it easier for any curious readers to find the old documents.

[Get the curl user survey 2025 analysis here](https://curl.se/docs/survey)

Enjoy!

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[survey](https://daniel.haxx.se/blog/tag/survey/)

# Post navigation

[Previous PostA family of forks](https://daniel.haxx.se/blog/2025/06/23/a-family-of-forks/)[Next Postkeeping tabs on curl’s memory use](https://daniel.haxx.se/blog/2025/07/08/keeping-tabs-on-curls-memory-use/)

## 8 thoughts on “curl user survey 2025 analysis”

1. ![](https://secure.gravatar.com/avatar/2febfa66539965bfc1ed9e5285062e85b2e2246ad3d375f074459f77ea06b6a6?s=34&d=monsterid&r=g) **[Andrei](http://https//andrybak.dev)** says:

   [July 3, 2025 at 16:19](https://daniel.haxx.se/blog/2025/07/03/curl-user-survey-2025-analysis/#comment-27205)

   > When the survey went up, curl 8.13.0 was the latest published release, even if there was an rc build of 8.14.0 out (which many people mentioned to me they actually used but could select in the survey).

   The sentence in parentheses seems to be missing a “not” in “could not”.

   1. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

      [July 3, 2025 at 17:54](https://daniel.haxx.se/blog/2025/07/03/curl-user-survey-2025-analysis/#comment-27206)

      @Andrei: indeed, thanks!

      1. ![](https://secure.gravatar.com/avatar/f02aa495722a230b26b4a221c56d1fef3a383bafd4f491140bbdac8ce961a481?s=34&d=monsterid&r=g) **George R. Goffe** says:

         [July 4, 2025 at 08:54](https://daniel.haxx.se/blog/2025/07/03/curl-user-survey-2025-analysis/#comment-27209)

         Howdy,

         I didn’t get any notice that there was a survey about curl, I would have loved to give you my own two cents.

         I have been a LONG time user of curl on multiple Unix platforms as well as windoze platforms. It’s great!

         I do a lot of website scrubbing and always have been blocked by overly aggressive authentication schemes. As you know, web servers can get a LOT of information about the originating system and can disallow web crawlers. I suspect that it has something to do with java-script but wouldn’t bet money on it.

         Best regards and THANKS for the cool code!

         George…

         1. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

            [July 4, 2025 at 09:07](https://daniel.haxx.se/blog/2025/07/03/curl-user-survey-2025-analysis/#comment-27210)

            @George: as mentioned in the report, we informed people about the survey over all the possible channels we could. We can’t do more!

            On servers blocking curl etc: these days the most effective ways to block anything that isn’t a “plain browser” involve TLS fingerprinting but adding JavaScript challenges to the mix is probably common as well.
2. ![](https://secure.gravatar.com/avatar/0b5735ddd44c3a275324819a00f207f68ab14740682cd570f4731262f18735f7?s=34&d=monsterid&r=g) **Richard Moore** says:

   [July 3, 2025 at 20:53](https://daniel.haxx.se/blog/2025/07/03/curl-user-survey-2025-analysis/#comment-27207)

   It would be nice to have the HTML version browsable online, not just as a zip download.

   1. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

      [July 3, 2025 at 20:55](https://daniel.haxx.se/blog/2025/07/03/curl-user-survey-2025-analysis/#comment-27208)

      @Richard: fair. Let me make that happen: Try <https://curl.se/docs/survey/2025/>

      1. ![](https://secure.gravatar.com/avatar/0b5735ddd44c3a275324819a00f207f68ab14740682cd570f4731262f18735f7?s=34&d=monsterid&r=g) **Richard Moore** says:

         [July 4, 2025 at 11:58](https://daniel.haxx.se/blog/2025/07/03/curl-user-survey-2025-analysis/#comment-27211)

         Thanks!
3. ![](https://secure.gravatar.com/avatar/7d1750b1d2422c002b3ce06460d331eadee34f87db44e9b90d350e3818145ea1?s=34&d=monsterid&r=g) **Tim Geiser** says:

   [July 16, 2025 at 18:54](https://daniel.haxx.se/blog/2025/07/03/curl-user-survey-2025-analysis/#comment-27264)

   The `Contribution` graph (“How have you contributed to the curl project?”) has an incorrect Y-axis label: it says “Share of Windows users who said they used which version,” but should say something like, “Share of users who sai...