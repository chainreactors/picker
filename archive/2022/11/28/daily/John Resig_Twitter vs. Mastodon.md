---
title: Twitter vs. Mastodon
url: https://johnresig.com/blog/twitter-mastodon/?utm_source=rss&utm_medium=rss&utm_campaign=twitter-mastodon
source: John Resig
date: 2022-11-28
fetch_date: 2025-10-03T23:54:41.784004
---

# Twitter vs. Mastodon

* [Home](https://johnresig.com/)
* [Blog](https://johnresig.com/category/blog/)
* [Projects](https://johnresig.com/projects/)
* [Speaking](https://johnresig.com/speaking/)
* [Research](https://johnresig.com/research/)
* [About](https://johnresig.com/about/)

[[![John Resig](https://johnresig.com/wp-content/uploads/2022/11/cropped-khan-john-resig-photo-square.jpg)](https://johnresig.com/)](/about/)

John Resig

* [Subscribe](https://johnresig.com/subscribe/)
* [Contact](https://johnresig.com/about/)

## Twitter vs. Mastodon

Some context on [Mastodon](https://joinmastodon.org/), after a couple weeks of exploring it – I’m sure I’m missing a lot, but this is my understanding of the tech, so far. I’ve been an avid user of Twitter so most of my knowledge comes by comparing Mastodon to Twitter.

You can follow me on Mastodon here: [https://mastodon.social/@jeresig](https://mastodon.social/%40jeresig)

# **Your main “timeline”**

This is the main place where you’re going to be reading things, but there are some major differences between what is shown on Twitter and on Mastodon.

**Twitter:**

* Individuals that you’ve subscribed to
* Posts that your friends have retweeted
* Posts that your friends are quote-tweeting
* Sometimes posts that your friends have liked
* Replies that your friends have made to their own posts
* Replies that your friends have made to other posts (if that person is also a friend)
* Ads

**Mastodon:**

* Individuals that you’ve subscribed to
* Posts that your friends have “retweeted” (boosted)
* Replies that your friends have made to their own posts (unless they’ve turned it off)
* Replies that your friends have made to other posts (unless they’ve turned it off)

**What’s missing on Mastodon:**

* Algorithmically-generated content from Twitter (such as posts your friends have liked)
* Quote-tweets (mostly – some clients apparently have ways of hacking around this by auto-expanding links to posts, but it’s not consistent)
* Ads

**Reading Your Timeline**:

* Mastodon provides a lot more control over what you see in your timeline. You can turn off boosts, or replies, for example (and also on a per-user basis, like on Twitter).
* Both services have the ability to create Lists and read posts by users in that List.

# **What’s the deal with servers?**

* Servers are different unique instances of Mastodon, different from Twitter where there is only a single server.
* You can create an account on any Mastodon server, even accounts on many servers.
* You can transfer your account between servers, if you’d like.
* Servers range in size and focus – some of them are very-niche (e.g. front-end.social exclusively for about ~250 frontend web devs) to very broad (e.g. mastodon.social, run by the Mastodon project and open to anyone with millions of users)
* Like Twitter, each server is impacted by the whims of its owner. The owner controls moderation of content, which users are allowed to join, and can “read DMs” – you need to trust your admin.
* If you subscribe to a user on another Mastodon server (B) your server (A) will reach out and tell the other server (B) that you want to receive updates. Then that other server (B) will notify your server (A) every time a new post comes in (while you, or another user on your server (A), is subscribed).
* Servers can control which other servers it’ll ingest posts from. This means that if there is a server with bad actors then your admin can disconnect from it entirely (removing all posts, the ability to subscribe, and hiding boosts). This does create a world where some big servers, like mastodon.social, are likely too big to ever disconnect from (this will likely create issues similar to the email world where besides a few big players folks running their own email servers is pretty rare).
* Also, Mastodon is using a protocol called ActivityPub to make all of this happen – and Mastodon isn’t the only thing using this protocol! Supposedly Tumblr will be adopting it in the future. [Anthony Sorace](https://pdx.social/%40a) mentioned [Pleroma](https://pleroma.social/) also doing microblog stuff, [BookWyrm](https://bookwyrm.social/) doing reading tracking/reviews, [Pixelfed](https://pixelfed.org/) doing image sharing, etc.

**Mastodon’s Local and Federated Timeline**

* Mastodon has a Local Timeline which is like a “List” of all users who are on your local server – you can see all posts by them. This is potentially very useful on a small server but is entirely unusable on servers of any decent size.
* Mastodon also has a Federated Timeline. This is like the Local Timeline but also includes posts from users on other servers that have been subscribed to by someone on your server (this is generally even less useful than the local timeline, especially on a busy server).

# **Other Differences to Note**

* Posts are longer on Mastodon, there is a character limit of 500
* Mastodon allows you to edit posts (supposedly Twitter Blue supports this, but I never signed up for it)! It keeps track of the history of changes as well.
* Mastodon encourages the use of Content Warnings. There is a lot of debate about how these should be used (and that enforcement likely differs based upon server norms). Since this is a native feature you can control how these posts are shown and in what ways (I auto-expand all content warned posts by default, for example).
* You have built-in control of post visibility (visible to all, visible to subscribers but can’t be searched for, followers only, mentioned only)
* There is no way to search for a post, or by post text. You can only search by hashtag – this makes it VERY hard to do any sort of drive-by pile-on, like what happens on Twitter.
* Likewise, there aren’t really trending topics, save for potentially a trending hashtag
* Quote tweeting isn’t a thing on Mastodon (at least not easily) which means that the practice of “dunking” on others via quote tweets is less likely to happen
* The official Mastodon software turns on accessibility features from the get-go, encouraging people to add alt text to their images (this exists on Twitter by it’s opt-in)
* DMs are different from on Twitter – if you tag a user in your DMs you may end up pulling them in to that discussion!
* Mastodon is Open Source and not controlled by a trans-hating fascist!

**Posted:** November 27th, 2022

---

**[Subscribe for email updates](/subscribe/)**

#### 1 Comment [(Show Comments)](#postcomment "Jump to the comments form")

1. ### **Dean Caton** (November 28, 2022 at [9:54 am](#comment-394988 "Permanent link to this comment"))

   Mastodon seems too complex for the average user. Have you heard of post.news? They seem to be the leading Twitter replacement contender.

   P.S. Glad to see you back on your blog again!

---

**Comments are closed.**
Comments are automatically turned off two weeks after the original post. If you have a question
concerning the content of this post, please feel free to [contact me](/about/).

---

[![Secrets of the JavaScript Ninja](/files/jsninja.74.jpg)](https://amzn.to/2oiS4em)

### [Secrets of the JS Ninja](https://amzn.to/2oiS4em)

Secret techniques of top JavaScript programmers. Published by Manning.

### [Subscribe for email updates](/subscribe/)

[![John Resig Twitter Updates](/images/twitter-74.png)](https://twitter.com/jeresig)

### [@jeresig](https://twitter.com/jeresig) / [Mastodon](https://mastodon.social/%40jeresig)

Infrequent, short, updates and links.