---
title: If This Isn't Intelligence, I Don't Know What Is
url: https://danielmiessler.com/blog/this-is-intelligence
source: Daniel Miessler
date: 2025-07-07
fetch_date: 2025-10-06T23:27:41.392889
---

# If This Isn't Intelligence, I Don't Know What Is

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[speaking](/speaking/)[about](/about/)

# This is Intelligence

Showing AI doing thousands of dollars of consulting work that could not previously be automated

July 6, 2025

[#ai](/archives/?tag=ai) [#philosophy](/archives/?tag=philosophy) [#technology](/archives/?tag=technology) [#recommended](/archives/?tag=recommended) [#top](/archives/?tag=top)

![Claude Report](/images/claude-report.png)pnpm install -g ccusage

I have a friend named [Marcus Hutchins](https://marcushutchins.com) who doesn't believe modern AI is intelligent. He thinks it's basically autocomplete. We actually had [a full debate about it here](https://youtu.be/I9-iD_rLRjA) that you should check out. It was a very civil and brilliant conversation, and we both learned a lot about each other's positions.

But I wanted to post a follow-up to that debate because I have some evidence—and a challenge—to share.

Over the last few days, I've been doing a ton of projects, and one of them has been cleaning up my site and adding some functionality.

## 1. Tagging my entire site [​](#_1-tagging-my-entire-site)

![Archives Display](/images/archives-display.png)This required a "human" to actually read and understand all the content.

1. Go read all 3061 blog posts
2. Retag them with one or more of my 20 content tags using AI to understand the content apply them appropriately
3. Rewrite all the tags
4. Push the changes

## 2. Bring my images home [​](#_2-bring-my-images-home)

Over the years I've had images hosted in many other CMSs, and most recently the whole site was on Beehiiv. I wanted to bring all the images home to my own local image store, so I had AI do the following:

1. Go find all instances of images that pointed to subdomains and third party content
2. Download that image
3. Rename it
4. Put it in my new local image store
5. Change the links multiple places in the post to point to the new location
6. Push the changes yy And keep in mind that was just a simple command I gave it, and it figured that all out, built a plan, and carried it out.

## 3. Converting super nasty HTML bundles to Markdown [​](#_3-converting-super-nasty-html-bundles-to-markdown)

![Nasty HTML](/images/nasty-html.png)

When I moved my site from Beehiiv, I had a lot of content that was wrapped in super nasty HTML bundles. This was because Beehiiv is a newsletter platform, and it doesn't really care about Markdown or clean HTML. It just wants to send out emails.

So it wasn't just images that were super broken, it was also the core content as well. When I brought my content back over from Beehive, it was all wrapped in this super nasty embedded HTML bundle.

Getting someone to do this consistently across 3,000 posts would also have been impossible.

And the whole point of going to my new static site was to have everything be pristine Markdown, with none of the content modified during the conversion.

So now I have an AI function where I basically just say, "Clean up this post", and I hand it any URL, and it goes and:

1. Completely rewrites all the HTML to clean Markdown
2. Fixes all the images
3. Applies all my custom formatting, which is like 15 different unique theme things
4. Makes sure nothing is broken through testing
5. Pushes the changes

It's completely insane.

## The takeaway [​](#the-takeaway)

Here's an example of the system working on one of the tasks.![AI Or](/images/ai-work.png)

Anyone who has done any technical work around maintaining a website, or complex HTML, will instantly recognize how tedious this work is.

And most importantly—several things here *you can't just script*.

This was mostly Claude Code, by the way. For anyone curious.

* No technology prior to modern AI would read posts for you and tag them based on their meaning
* Same with cleaning posts full of garbage HTML and rewriting it as clean Markdown

Think about all the work on Upwork and Fiverr.

Even for the tasks that someone *could* code, it'd still be shit work to do, and it'd take forever to troubleshoot. Claude wrote dozens of these over the course of the work, with many being a couple hundred lines of code, and it did it all in a few seconds.

Including testing afterwards. And providing monitoring and status updates all along so I could watch its progress.

These all would have required a human to do the work, and it would have taken weeks or months to do it all manually. Or you pay someone to do it—probably poorly—and it would cost thousands of dollars.

**TL;DR: This was hundreds of hours and thousands of dollars worth of work that I just had AI do in a few days.**

## Summary (my argument) [​](#summary-my-argument)

I don't see how it's possible to argue this isn't intelligence.

Again, this is not possible to do without either manual *human* work, or AI. In fact, that's my actual definition of AI.

I do agree with him that this is a special and still-only-human type of intelligence.

Marcus disagrees. As we cover in the debate, he defines it more as a *completely* new thing—like Einstein's `e=mc^2`, or the invention of the wheel.

I have multiple problems with this:

1. It devalues 99.99% of all cognitive work being done by people
2. It implies it's ok for anyone *not* doing that kind of work to get replaced

Essentially, this definition is so restrictive as to be useless.

It doesn't apply to the difficult cognitive work that *hundreds of millions of people* are being paid lots of money to do. Work that they might no longer be paid for because of the technology shown above.

Whatever we want to call that.

Do we really need a new name?

*Cognitive Work Replacement Technology*?

I don't see the need for it. The existing name already works.

#### Notes

1. I'll do a separate post addressing Marcus' definition of intelligence itself, which I think is the heart of the disagreement. Basically he thinks it's the ability to fill in the gaps when there's information missing, and I think it's demonstrably clear that AI can already do that. And that it could in 2022.

Share

[Post](https://ul.live/share/x?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fthis-is-intelligence&title=This%20is%20Intelligence "Share on X")  [LinkedIn](https://ul.live/share/linkedin?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fthis-is-intelligence&title=This%20is%20Intelligence "Share on LinkedIn") [HN Hacker News](https://ul.live/share/hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fthis-is-intelligence&title=This%20is%20Intelligence "Share on Hacker News")  [Reddit](https://ul.live/share/reddit?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fthis-is-intelligence&title=This%20is%20Intelligence "Share on Reddit")  [Facebook](https://ul.live/share/facebook?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fthis-is-intelligence&title=This%20is%20Intelligence "Share on Facebook")  [Forward](https://ul.live/share/email?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fthis-is-intelligence&title=This%20is%20Intelligence "Share via Email")

Follow

[Get The Newsletter](https://ul.live/nlpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fthis-is-intelligence&title=This%20is%20Intelligence)  [Follow On X](https://ul.live/xpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fthis-is-intelligence&title=This%20is%20Intelligence)  [Subscribe On YouTube](https://ul.live/ytpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fthis-is-intelligence&title=This%20is%20Intelligence)  [Follow On LinkedIn](https://ul.live/lipostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fthis-is-intelligence&title=This%20is%20Intelligence)

Search

This post was tagged with:

aiphilosophytechnologyrecommendedtop

[HOME](/)·[BLOG](/blog)·[ARCHIVES](/archives)·[ABOUT](/about)

© 1999 — 2025 Daniel Miessler. All rights reserved.