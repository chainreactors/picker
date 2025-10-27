---
title: Allowing Notification Center notifications to appear during screen recordings on macOS Sequoia
url: https://derflounder.wordpress.com/2025/02/24/allowing-notification-center-notifications-to-appear-during-screen-recordings-on-macos-sequoia/
source: Der Flounder
date: 2025-02-25
fetch_date: 2025-10-06T20:34:10.280257
---

# Allowing Notification Center notifications to appear during screen recordings on macOS Sequoia

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Allowing Notification Center notifications to appear during screen recordings on macOS Sequoia

## Allowing Notification Center notifications to appear during screen recordings on macOS Sequoia

February 24, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As part of making some screen recordings of app behavior recently, I noticed that the Notification Center notifications I was expecting to see weren’t appearing. As soon as I stopped making the screen recordings and replicated what I was doing, I saw the Notification Center notifications appear like they should.

After verifying that I hadn’t somehow enabled [Focus](https://support.apple.com/guide/mac-help/set-up-a-focus-to-stay-on-task-mchl613dc43f/mac) or done something else to stop Notification Center notifications from appearing, I did some research which [uncovered the solution](https://obsproject.com/forum/threads/display-capture-disables-macos-notifications.152270/post-568504). For more details, please see below the jump.

As part of the **Notifications** preferences in the **Settings** app, there is the following option:

**Allow notifications when mirroring or sharing the display**

![](https://derflounder.wordpress.com/wp-content/uploads/2025/02/screenshot-2025-02-24-at-10.20.012am.png?w=595 "Screenshot 2025-02-24 at 10.20.012AM.png")

This setting also apparently includes making screen recordings, because enabling it allowed Notification Center notifications to appear during screen recordings. To enable this setting, please use the following procedure:

1. Open Settings

2. Go to **Notifications**.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/02/screenshot-2025-02-24-at-10.20.01am.png?w=595 "Screenshot 2025-02-24 at 10.20.01 AM.png")

3. Enable the **Allow notifications when mirroring or sharing the display** setting.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/02/screenshot-2025-02-24-at-10.20.14am.png?w=595 "Screenshot 2025-02-24 at 10.20.14 AM.png")

You should now see notifications appearing while mirroring, sharing the display, or when making screen recordings.

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2025/02/24/allowing-notification-center-notifications-to-appear-during-screen-recordings-on-macos-sequoia/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2025/02/24/allowing-notification-center-notifications-to-appear-during-screen-recordings-on-macos-sequoia/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2025/02/24/allowing-notification-center-notifications-to-appear-during-screen-recordings-on-macos-sequoia/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2025/02/24/allowing-notification-center-notifications-to-appear-during-screen-recordings-on-macos-sequoia/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2025/02/24/allowing-notification-center-notifications-to-appear-during-screen-recordings-on-macos-sequoia/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2025/02/24/allowing-notification-center-notifications-to-appear-during-screen-recordings-on-macos-sequoia/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2025/02/24/allowing-notification-center-notifications-to-appear-during-screen-recordings-on-macos-sequoia/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2025/02/24/allowing-notification-center-notifications-to-appear-during-screen-recordings-on-macos-sequoia/?share=pocket)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/)

Comments (3)
[Leave a comment](#respond)

1. ![dhausman's avatar](https://1.gravatar.com/avatar/a51beb5b6c113a0c773c8834ebb9babeeac6aa3bec7c4ea720703b8b74a8ac57?s=32&d=identicon&r=G)

   dhausman

   March 7, 2025 at 4:49 pm

   [Reply](https://derflounder.wordpress.com/2025/02/24/allowing-notification-center-notifications-to-appear-during-screen-recordings-on-macos-sequoia/?replytocom=72674#respond)

   This is also a nice option if you use a displaylink dock. I had to enable this to get notifications while I am using the dock.
2. ![dhausman's avatar](https://1.gravatar.com/avatar/a51beb5b6c113a0c773c8834ebb9babeeac6aa3bec7c4ea720703b8b74a8ac57?s=32&d=identicon&r=G)

   dhausman

   March 7, 2025 at 4:50 pm

   [Reply](https://derflounder.wordpress.com/2025/02/24/allowing-notification-center-notifications-to-appear-during-screen-recordings-on-macos-sequoia/?replytocom=72675#respond)

   This is also a nice option if you use a displaylink dock. I had to enable this to get notifications while I am using the dock.
3. ![dhausman's avatar](https://1.gravatar.com/avatar/a51beb5b6c113a0c773c8834ebb9babeeac6aa3bec7c4ea720703b8b74a8ac57?s=32&d=identicon&r=G)

   dhausman

   March 7, 2025 at 4:51 pm

   [Reply](https://derflounder.wordpress.com/2025/02/24/allowing-notification-center-notifications-to-appear-during-screen-recordings-on-macos-sequoia/?replytocom=72676#respond)

   This is also nice to turn on if you use a displaylink dock. I figured this out when no notifications were working since the displaylink driver is “recording” your screen to show it on other monitors.

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2025/02/24/allowing-notification-center-notifications-to-appear-during-screen-recordings-on-macos-sequoia/#respond)

Δ

[Rotating the credentials for a Jamf Pro AWS cloud distribution point](https://derflounder.wordpress.com/2025/02/28/rotating-the-credentials-for-a-jamf-pro-aws-cloud-distribution-point/)
[Managing Apple Intelligence features on macOS Sequoia 15.3](https://derflounder.wordpress.com/2025/01/29/managing-apple-intelligence-features-on-macos-sequoia-15-3/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.wordpress.com/feed/ "Subscribe with Google")
* [Youdao](http://reader.youdao.com/#url=https://derflounder.wordpress.com/feed/ "Subscribe with Youdao")
* [Xian Guo](http://www.xianguo.com/subscribe.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Xian Guo")
* [Zhua Xia](http://www.zhuaxia.com/add_channel.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Zhua Xia")
* [My Yahoo!](http://add.my.yahoo.com/rss?url=https://derflounder.wordpress.com/feed/ "Subscribe with My Yahoo!")
* [newsgator](http://www.newsgator.com/ngs/subscriber/subfext.aspx?url=https://derflounder.wordpress.com/feed/ "Subscribe with newsgator")
* [Bloglines](http://www.bloglines.com/sub/https%3A//derflounder.wordpress.com/feed/ "Subscribe with Bloglines")
* [iNezha](http://inezha.com/add?url=https://derflounder.wordpress.com/feed/ "Subscribe with iNezha")

February 2025

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | | 1 | 2 |
| 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| 17 |...