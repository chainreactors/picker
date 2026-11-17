---
title: Actual curl rewrites in rust
url: https://daniel.haxx.se/blog/2026/11/17/actual-curl-rewrites-in-rust/
source: daniel.haxx.se
date: 2026-11-16
fetch_date: 2026-11-17T09:56:16.455253
---

# Actual curl rewrites in rust

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2023/09/old-machine.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# Actual curl rewrites in rust

[November 17, 2026](https://daniel.haxx.se/blog/2026/11/17/actual-curl-rewrites-in-rust/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [1 Comment](https://daniel.haxx.se/blog/2026/11/17/actual-curl-rewrites-in-rust/#comments)

For a long time we have received repeated requests for, or questions about, a curl rewrite in rust. Often as a joke, but also seriously.

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/11/orly-rewriting-curl-in-rust.png)

A joke from years ago

In this modern world of AIs, we have only been waiting for someone to prove it possible and now it seems we don’t have to wait anymore.

This fall seems to be the time of the curl-in-rust takes as we first saw [urlx](https://github.com/jonwiggins/urlx) appear a few months ago, claimed to be *a memory-safe, from-scratch reimplementation of curl and libcurl* and now in November [curl, rewritten in Rust](https://github.com/kov/curl) – *a rewrite of curl and libcurl in Rust*. This second one confusingly enough not even using a different name.

This latter one [claims to have spent 8,600 USD](https://claude.ai/artifact/K4BoWt35HQz1xWZBR3bMRD) to make it happen.

## Writing code once was never the issue

Writing code *once* was never the big deal with software and it still isn’t. Sure, it’s fascinating that you can make a set of agents accomplish this in only a few weeks but let’s face it: it could do this because all the AIs of the world have trained on curl code for years. curl is extremely well documented, there are hundreds of existing open source application using its API and there are thousands of test cases to verify the implementation.

The C code sits there and all the AI needs to do is convert it to rust, then polish until the tests work.

![](https://daniel.haxx.se/blog/wp-content/uploads/2021/04/I-could-write-curl-in-a-3-day-weekend.png)

A know-it-all person’s comment from years ago

## curl is the result of time

curl has come to be what it is thanks to many decisions, lots of time, many users, oceans of feedback and many iterations. Sure, recreating what curl is at any specific single moment in time is certainly doable. Doable, because we have made a perfect specification for that project.

## Behind already

During the time these agents converted 185,000 lines of C code into 340,000 lines of Rust code (I counted), we merged over 300 commits in the actual curl project. We actually improved curl during these a little more than three weeks. A little over 200 bugfixes actually. 200 bugfixes that none of those rust rewrites have. We also fixed a few vulnerabilities. In another month we have done another 200 and maybe fixed a few more vulnerabilities. Will these clones keep up?

The constant tweaking, fixing, improving and extending is what makes a software project live, what makes it attractive to users and what makes it able to compete with alternatives.

That fixing, and occasional new feature, is a direct result of a working community of users, contributors and maintainers. That goes way beyond the source code or which language that is used.

A primary reason it is hard to make a competing curl alternative is because of the development speed, the development team and the community around curl. It is not because of the chosen language it is implemented in. Only curl can boast decades of ABI and API stability and prove that we know this and can do it well – over time. An alternative that pops up today might be able to do it as well, and *in a few decades we will know if they could*.

## C

I know I’m repeating myself but: out of the 81 vulnerabilities we have confirmed in curl so far during 2026, 14 were the result of mistakes that most likely would have been avoided had we used a memory-safe language such as rust. That’s 17.3%.

A Rust implementation of curl would thus still have had 67 of those vulnerabilities.

## No rewrites

I don’t believe in rewrites into any language. I believe in constant and never-ending polishing, iterating and refactoring.

## Those rewrites

I should add that I have not been in contact with any of the people behind these rewrites, and if there are two I bet there are more that I just haven’t seen yet. I only know of them because people have pasted me links to their repositories.

I don’t know what they will do with those projects going forward. Are they anything more than proof of concepts? I presume we will find out.

They can of course follow along our commits and convert them to rust on the fly if they want – we only do about 11 commits per day on average. Or maybe they ignore the bugreports or maybe they take their projects in other directions?

I wish them good luck whatever they decide!

## How do I feel about them?

Several people asked me this.

*Imitation is the sincerest form of flattery that mediocrity can pay to greatness*. / Someone

I’m amused. A little puzzled. Fascinated. They spent their money and effort on *that?*

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)

# Post navigation

[Previous Post30 years of Internet transfers with curl](https://daniel.haxx.se/blog/2026/11/11/30-years-of-internet-transfers-with-curl/)

## One thought on “Actual curl rewrites in rust”

1. ![](https://secure.gravatar.com/avatar/67dfb6f601466f7a3c644417d92bc76ccfedb6dc920710316cbe16684f074d82?s=34&d=monsterid&r=g) **Owen** says:

   [November 17, 2026 at 07:44](https://daniel.haxx.se/blog/2026/11/17/actual-curl-rewrites-in-rust/#comment-27581)

   I find it quite interesting. I couldn’t possibly be part of the “just rewrite it in Rust” crowd, but I also do see the benefits in many cases.

   It feels like, while ideally it’d be good to have that effort put into curl itself and see things improved and fixed, the fact that it’s a problem space people are paying attention to at all is a Good Thing™?. I hope something useful comes of them, just so we’ve got something interesting and novel to look at, at least. Maybe it leads to better understanding of the big wonderful world of internet transfers.

   I appreciate the hubris – you’ve gotta start with blind, cocky optimism sometimes. 😛

   [Reply](https://daniel.haxx.se/blog/2026/11/17/actual-curl-rewrites-in-rust/?replytocom=27581#respond)

### Leave a Reply [Cancel reply](/blog/2026/11/17/actual-curl-rewrites-in-rust/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
5five192

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [Actual curl rewrites in rust](https://daniel.haxx.se/blog/2026/11/17/actual-curl-rewrites-in-rust/)
  November 17, 2026
* [30 years of Internet transfers with curl](https://daniel.haxx.se/blog/2026/11/11/30-years-of-internet-transfers-with-curl/)
  November 11, 2026
* [Scrutinize our assessments](https://daniel.haxx.se/blog/2026/11/03/scrutinize-our-assessments/)
  November 3, 2026
* [“ignore the slop”](https://daniel.haxx.se/blog/2026/10/22/ignore-the-slop/)
  October 22, 2026
* [Do minor curl vulnerabilities in the open](https://daniel.haxx.se/blog/2026/10/20/do-minor-curl-vulnerabilities-in-the-open/)
  October 20, 2026
* [OSI approved the curl license](https://daniel.haxx.se/blog/2026/10/15/osi-approved-the-curl-license/)
  October 15, 2026

# Recent Comments

* Owen on [Actual...