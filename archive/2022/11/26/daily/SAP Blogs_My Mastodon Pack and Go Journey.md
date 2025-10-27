---
title: My Mastodon Pack and Go Journey
url: https://blogs.sap.com/2022/11/25/my-mastodon-pack-and-go-journey/
source: SAP Blogs
date: 2022-11-26
fetch_date: 2025-10-03T23:48:48.923637
---

# My Mastodon Pack and Go Journey

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Welcome Corner](/t5/welcome-corner/gh-p/welcome-corner)
* [Blog Posts](/t5/welcome-corner-blog-posts/bg-p/welcome-cornerblog-board)
* My Mastodon Pack and Go Journey

Welcome Corner Blog Posts

Go a little bit deeper into the Welcome Corner with blog posts. Learn how to get started in SAP Community and get tips on maximizing your participation.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/welcome-cornerblog-board/article-id/36193&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [My Mastodon Pack and Go Journey](/t5/welcome-corner-blog-posts/my-mastodon-pack-and-go-journey/ba-p/13558157)

![JimSpath](https://avatars.profile.sap.com/1/9/id19e0902ffb151e54856445a6cc9bb1df4e8202ab913d64c6e2e2d8625cd7bf0a_small.jpeg "JimSpath")

![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion")
[JimSpath](https://community.sap.com/t5/user/viewprofilepage/user-id/184)

SAP Champion

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=welcome-cornerblog-board&message.id=36193)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/welcome-cornerblog-board/article-id/36193)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558157)

‎2022 Nov 25
5:54 PM

[5
Kudos](/t5/kudos/messagepage/board-id/welcome-cornerblog-board/message-id/36193/tab/all-users "Click here to see who gave kudos to this post.")

851

* SAP Managed Tags
* [SAP Community](https://community.sap.com/t5/c-khhcw49343/SAP%2520Community/pd-p/486157991894093153608181816584982)

* [SAP Community

  Topic](/t5/c-khhcw49343/SAP%2BCommunity/pd-p/486157991894093153608181816584982)

View products (1)

Along with many others, I packed up my social media presence on the twitter sites, and unpacked in the Fediverse of Mastodon instances. The time to move was obvious for me but the path was not. Leaving behind may contacts and previous communications is like losing the text message history on your mobile device (the infamous "new phone who this?").

I looked at a few ways to save/export contact lists and on a dive through a couple thousand I found the veritable beginning of that social media channel with seven luminaries of the SAP community space(s). Unsurprising as I started connecting there because of what [James Governor](https://redmonk.com/team/james-governor/) shared to the TechEd communities.

![](/legacyfs/online/storage/blog_attachments/2022/11/tw-follows.png)

My first follows

### Data Export Attempts

Turned out just browsing was enough to find my first hundred or so people to get started on Mastodon. I ran online scripts that found a dozen or 2 but thought I'd go another way. Online help suggested to make an official export data request through the Twitter web site. Basic steps:

1. Request zip

2. Verify request

3. Wait

4. Download from supplied link

```
-rw-r--r--+ 1 Jim None 662754007 Nov 18 11:38 twitter-2022-11-18-##.zip
```

![](/legacyfs/online/storage/blog_attachments/2022/11/follows.jpg)

Follows/Followers/Mutuals

The image above of craig.cmehil et al shows their current "screen names" which, being variable, aren't a key identifier; the "user id" is. Converting the latter to the former works on a recent browser, though availability of any API in the future might be a problem. I found a short script that appeared to work without needing an access key, but the libraries seem to already be outdated.

Of the 7 people, 4 mention Mastodon in their visible Twitter bios when I captured the image.

Besides user searches, prior "tweet" posts might be found with this pattern:

```
https://twitter.com/{userName}/status/{tweetId}
```

My first seems to have been a mundane search for a cup of coffee:

<https://twitter.com/jspath55/status/454267732>

[ twitter.com/jspath55/status/454267732 ]

Examples of API URLs:

<https://twitter.com/intent/user?user_id=>

<https://twitter.com/intent/user?screen_name=>

Inside the downloaded archive are follows and follower data streams:

```
 283934 Stored 283934 0% 11-18-22 16:25 00000000 data/follower.js

 394725 Stored 394725 0% 11-18-22 16:25 00000000 data/following.js
```

My mutual count is around 800 from a total of 4000 follower+following.

Here is an example of an account I followed (local author of "The Widows of Malabar Hill") with the saved identifier and the associated account:

<https://twitter.com/intent/user?user_id=94355210>

<https://twitter.com/intent/user?screen_name=sujatamassey>

### On the Mastodon side

Just as the migration began in earnest, as evidenced by tracking various accounts and trending topics, those running the hosts were presented with a version upgrade. I initially saw a message about a release candidate, which is not what you'd want to pick as the stable platform for a predicted large growth (if allowed) of new users and traffic.

Hard times for some if not all system administrators as they tried to keep up with the changes.

![](/legacyfs/online/storage/blog_attachments/2022/11/mastodon-v4-cropped.png)

Mastodon 4 startup queueing

When V4.x began to be rolled out on the instance I am connected to, a few burps, lost or changed addresses, and somewhat of a user interface evolution (more on media in another post). I'm getting responses from more and more people.

#### SysOp Challenges

```
I'm burning the candle on both ends here.

Look at this toot timestamp.

Please save space for some patience.
```

Link: [https://chaos.social/@chad@mstdn.ca/109398058883988287](https://chaos.social/%40chad%40mstdn.ca/109398058883988287) or maybe something else; I admit I am still learning (and some links changed from 3 to 4).

I see new Mastodon instances being set up and already growing, which is testimony to the open source community roots and networks. The resiliency and stability are good indicators in my view.

### Social timeline

Seems I'm ready for the technical challenge of an environment swap to clear the decks, though losing multiple friend voices at one time can be a daunting human experience. I can grieve the loss as we've done in real world health challenges along with online mental health coping.

For the near term, I'll search on hash tags which Mastodon supplies on a web column view.

![](/legacyfs/online/storage/blog_attachments/2022/11/hashtags.png)

Hash tags on Mastodon

### Previous Steps:

* [is-it-time-to-join-the-elephant-parade-or-what-is-this-mastodon-doing-in-my-web/](https://blogs.sap.com/2022/11/07/is-it-time-to-join-the-elephant-parade-or-what-is-this-mastodon-doing-in-my-web/)

* [second-thoughts-on-the-great-mastodon-migration/](https://blogs.sap.com/2022/11/12/second-thoughts-on-the-great-mastodon-migration/)

* [mastodon](/t5/tag/mastodon/tg-p/board-id/welcome-cornerblog-board)
* [social media](/t5/tag/social%20media/tg-p/board-id/welcome-cornerblog-board)
* [twitter](/t5/tag/twitter/tg-p/board-id/welcome-cornerblog-board)

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fwelcome-corner-blog-posts%2Fmy-mastodon-pack-and-go-journey%2Fba-p%2F13558157%23comment-on-this)

Copy Link...