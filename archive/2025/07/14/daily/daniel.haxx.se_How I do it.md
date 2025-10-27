---
title: How I do it
url: https://daniel.haxx.se/blog/2025/07/13/how-i-do-it/
source: daniel.haxx.se
date: 2025-07-14
fetch_date: 2025-10-06T23:23:13.954555
---

# How I do it

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2019/10/daniel-DN-2-jonas-lindkvist.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# How I do it

[July 13, 2025](https://daniel.haxx.se/blog/2025/07/13/how-i-do-it/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [1 Comment](https://daniel.haxx.se/blog/2025/07/13/how-i-do-it/#comments)

A while ago I received an email with this question.

> I’ve been subscribed to your [weekly newsletter](https://lists.haxx.se/listinfo/daniel) for a while now, receiving your weekly updates every Friday. I’m writing because I admire your consistency, focus, and perseverance. I can’t help but wonder, with admiration, how you manage to do it.

Since this is a topic I receive questions about semi-regularly, I decided I would attempt to answer it. I have probably touched the subject in previous blog posts as well.

## Work

Let me start out by defining what I consider my primary work to be. Or perhaps I should call it my *mission* because it goes way beyond just “work”. curl is irrevocably a huge part of me and my life.

* I drive the curl project. Guide, develop, review, comment, admin, debug, merge, commit, support, assess security reports, lead, release, talk about it, inspire etc.
* It does not necessarily mean that I do the most number of commits to curl every month. We have a set of very skilled and devoted committers that can do a lot without me.
* I keep up with relevant Internet protocol developments and make sure to give feedback on what I think is good and bad, in particular from a small player’s/library’s view that is sometimes a bit different than the tech giants’ takes. This means participating actively in some IETF groups and keeping myself informed about what is happening in a number of other HTTP, web and browser oriented communities.
* I keep up with related technologies and Open Source projects to understand how to navigate. Feedback issues, comments and pull requests to neighbor projects that we use – to strengthen them (and then by association the combination curl + them) and to increase the chances that they will help us out in similar fashion.
* I use my position as lead developer of curl to blog and speak up about things I think need to be said, explained or giggled at. Be it stupid emails, bad uses of AI or inefficient security organizations. Ideally this occasionally helps other people and projects as well.

As a successful Open Source project I acknowledge and am aware that we (I mean curl) might get more attention than some others, and that we are used as or considered a “model” sometimes, making it even more important to do things right. From my language use in public to source code decisions. I try to live up to these expectations.

A part of my job is to make companies become paying customers so that I can afford working on curl – and once they have become customers I need to every now and then attend to support tickets from them. I can work full-time on curl thanks to my commercial customers.

## Why

I have a strong sense of loyalty and commitment. When I join a project or a cause, I typically stick around and do my share of the job until it is finished.

I enjoy programming and software development – and I have done so ever since I first learned about programming as a teen in the mid 1980s. It is fun to create something that is useful and that can be used by others, but I also like solving the puzzles and challenges that come up in the process.

When the software project you work on never finishes, and is used by a crazy amount of users it gives you a sense of responsibility and *pride*. An even bigger incentive to make sure it actually works as intended. A desire to please the users. All the users.

Even after having reached many *billions* of installations there are still challenges to push the project further and harder on every possible front. Make it the best documented one. Make it an exemplary Open Source project. Make it newcomer friendly. Add more tests. Make sure not a single project in the world can claim they ship better security advisories. Work really hard on making it the most secure network library there is. While at the same being welcoming and friendly to new contributors.

**If there is *any* area that curl is not best-in-class, we should put in more work and improve curl in that area**. While at the same time keep up and polish it in all other aspects.

This is what drives me. This is what I want.

## How

Getting top scores in every possible (imaginary and real) scorecard is accomplished through good old engineering. Do the job. Test. Iterate. Fail. Fix. Add tests. Do it again. Over and over.

A normal work day I sit down at my desk at about 8 in the morning and start. I iterate over issues, pull-requests and the everyday curl maintenance. I post silly messages on Mastodon and I chat with friends on IRC.

I try to end my regular work days at around 18:00, but I may go longer or shorter some days depending on what I feel like or if it’s “floorball day”. (I leave early on Wednesdays to go play with friends.)

As I live in Sweden and have many North-American colleagues and customers, I have occasional evening meetings to deal with the nine hour time difference to their west coast.

At some time between 22:00 and 23:00 I sit down in front of my computer again for the evening shift. I continue working on issues, fix bugs and review pull-requests. At 1am I sleep.

It makes me do maybe 50-55 hours of work per normal week. I call it all work hours plus plenty of spare time. Because this is the passion of my life. It is my job *and* my hobby. Because I want to. I love it. It is not a setup and number of hours I ask nor expect anyone else to do.

I have worked like this since early 2019 when I started doing curl full-time.

## Independent

One explanation how this all works is that curl is *independent*. Truly independent in most senses of the word.

No companies control or own curl in any way. Yet every company is welcome to participate.

curl is not part of any foundation or umbrella organization. We range free.

curl is extremely liberally licensed.

## On motivation

One of the hardest questions to answer is how I can keep up the motivation and still consider this *fun* and exciting after all this time.

First let’s not pretend that it *always* feels fun and thrilling. Sometimes it actually feels a bit boring and *done.* There is no shame in that and it is not strange or odd. Such periods come and go. When they come, I might do less curl for a while. Or maybe find a corner of the project that is not important but could be fun to poke at. I have learned that these periods come and go.

What motivates me is that *everyone* runs and uses curl and libcurl. Positive feedback is fuel that can keep me running for a long time. Making curl a leading tool that shoulders and carries a lot of digital infrastructure makes me feel a purpose. When there is a bug reported, I can feel almost hurt and sometimes ashamed and I *need* to get it fixed. curl is supposed to be *one of the best* in all categories and if it ever is not, I will work hard on making it so.

The social setup around Open Source and a success such as curl also makes it fun. I work full-time from home without geographical proximity to any other curl regulars. But I don’t need that. We can joke around in chat, we help each other in issues and pull-requests and we can do bad puns in video meetings. Contrary to “normal” job colleagues, these people are here because they want, believe and strive for som...