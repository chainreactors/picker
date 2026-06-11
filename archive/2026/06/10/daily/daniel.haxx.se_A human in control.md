---
title: A human in control
url: https://daniel.haxx.se/blog/2026/06/10/a-human-in-control/
source: daniel.haxx.se
date: 2026-06-10
fetch_date: 2026-06-11T06:34:32.610106
---

# A human in control

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2019/12/sleeping-person.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# A human in control

[June 10, 2026](https://daniel.haxx.se/blog/2026/06/10/a-human-in-control/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [1 Comment](https://daniel.haxx.se/blog/2026/06/10/a-human-in-control/#comments)

There seems to be a fair amount of people in either extremes in the current AI landscape. At one side we see the “vibe coders” who use agents and allow them to merge code without any person even looking at the source, while on the other side of the field there are people who are against everything and anything even remotely associated with AI.

My personal stance is somewhere in between, as I suppose shouldn’t be too surprising to readers of this blog.

## A work of love and pride

The core team behind curl, and that is more people than just me, consists of individuals to whom code quality and source code excellence is important. We do software development because it is a craft we love and we are proud of what we have accomplished this far. We do not hand over our responsibilities to any machines. *We stand for every bit of code we merge – as humans.*

## AIs do mistakes

Blindly accepting code written by AI means that you merge a certain amount of errors, but this is certainly true for human written code as well, so this is not in itself special. Some data suggests that AI generated code might even contain more mistakes than the human versions.

We invented test cases and code review a long time ago as a means to help us combat and reduce mistakes to get merged. The particular way code was written does not take away the benefits from code review and getting additional checks and eyes on pending changes. A good code review helps spotting mistakes, omissions or slip-ups. It also helps reinforce the architecture and established design choices. This is true however the code was created.

This far, code reviews done by automatic AI bots and the likes have not yet managed to replace the humans. They are simply not good enough.

Human reviews are much better. They catch other things and they help make sure proposed changes stay on track.

Not to mention how I want to know how curl works, even if I don’t keep 100% intimate knowledge of every single angle and corner, I know most of it. I think it helps me make better decisions, debug better, help users better and keep the architecture sound.

Getting the initial code written is not the big deal. For curl, maintaining and polishing the landed code *through decades* is the real task.

*Everything we merge in curl is determined fine and fitting by humans.*

## Humans do mistakes

In all living software projects we get bugs reported and we fix them. We do new releases and continue to iterate. We have done this since software was invented and we still do, as humans are quite fallible and easily make mistakes.

We try to reduce the error density and frequency by adding tests and by adding more human eyes on the code before we green-light it. It helps, but is not perfect.

To help us do better code we invent, introduce and enforce a wide variety of different tools. With tools that look at code and identify problems in the early stages, they help avoid landing bad code in the first place. They make us do better code. They reduce the bug frequency.

Some of the best tools for detecting coding mistakes today use AI. These tools might work on existing source code in a git repository or they might look at proposed changes in pull-requests.

Above I mentioned that human code reviews are better; but the opposite is also true. In a somewhat complicated change request, it is now common that after the humans can’t spot any more problems, the AI PR review bots can still find an issue or two to remark on. Sure, sometimes they are wrong and then the comment is easily dismissed, but more often than not the findings they point out are actually something worth addressing before merge.

*curl is developed and driven by humans, assisted by tools.*

## Communication is for humans

Open Source is about sharing code and is a development model where we do things in the open. The *communication* part of this model is key. Share your ideas, your visions, your problems or maybe just your ideas for what to do this afternoon.

Express what you want or what the problem is, and the team can respond and we can work together on fixing and improving whatever needs to be done.

Effective communication, a condition for good Open Source, implies *human-to-human* interaction. Inserting a large AI generated tone-deaf large wall-of-text into such a flow *can* still work, but only in the same way humans can learn to work with difficult individuals as well. It is not ideal and it is not a smooth way of working. It introduces sand in the machine. Don’t do that. It is rude.

*Effective Open Source work means we communicate as humans, even if parts of the work and the code is made with the help of AI.*

## The combination

Humans and machines excel at different things. We can complement each other in software development.

Everyone is free to act to their own will, but in the curl project we don’t hand over responsibility to machines. We stand for our product. We make it as good as we possibly can; using all the tools that are available to us. I claim that in order to do this, humans need to remain in control.

[AI](https://daniel.haxx.se/blog/tag/ai/)[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[Development](https://daniel.haxx.se/blog/tag/development/)[Security](https://daniel.haxx.se/blog/tag/security/)

# Post navigation

[Previous Postcurl up 2026 summary](https://daniel.haxx.se/blog/2026/05/28/curl-up-2026-summary/)

## One thought on “A human in control”

1. ![](https://secure.gravatar.com/avatar/1c88dbe9b80f2843c278e2cd1aac9af80757089070a5556462515218aa602eaa?s=34&d=monsterid&r=g) **Valentin** says:

   [June 10, 2026 at 13:20](https://daniel.haxx.se/blog/2026/06/10/a-human-in-control/#comment-27498)

   We know your articles are written by you and not AI proof read, because you have some typos, like here

   “We stand for ever bit of code we merge – as humans.”
   Should be “every” ofc.

   Great article!

   [Reply](https://daniel.haxx.se/blog/2026/06/10/a-human-in-control/?replytocom=27498#respond)

### Leave a Reply [Cancel reply](/blog/2026/06/10/a-human-in-control/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
threeninesevenfive2

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [A human in control](https://daniel.haxx.se/blog/2026/06/10/a-human-in-control/)
  June 10, 2026
* [curl up 2026 summary](https://daniel.haxx.se/blog/2026/05/28/curl-up-2026-summary/)
  May 28, 2026
* [The pressure](https://daniel.haxx.se/blog/2026/05/26/the-pressure/)
  May 26, 2026
* [named globs with curl](https://daniel.haxx.se/blog/2026/05/16/named-globs-with-curl/)
  May 16, 2026
* [Mythos finds a curl vulnerability](https://daniel.haxx.se/blog/2026/05/11/mythos-finds-a-curl-vulnerability/)
  May 11, 2026
* [Approaching zero bugs?](https://daniel.haxx.se/blog/2026/04/30/approaching-zero-bugs/)
  April 30, 2026

# Recent Comments

* Valentin on [A human in control](https://daniel.haxx.se/blog/2026/06/10/a-human-in-control/comment-page-1/#comment-27498)
* [Dick Brooks](...