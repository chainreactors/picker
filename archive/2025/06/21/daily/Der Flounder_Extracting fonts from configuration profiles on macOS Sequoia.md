---
title: Extracting fonts from configuration profiles on macOS Sequoia
url: https://derflounder.wordpress.com/2025/06/20/extracting-fonts-from-configuration-profiles-on-macos-sequoia/
source: Der Flounder
date: 2025-06-21
fetch_date: 2025-10-06T22:52:54.964854
---

# Extracting fonts from configuration profiles on macOS Sequoia

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/) > Extracting fonts from configuration profiles on macOS Sequoia

## Extracting fonts from configuration profiles on macOS Sequoia

June 20, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

One way to deliver custom fonts on macOS is to [deploy them via a configuration profile](https://support.apple.com/en-sg/guide/deployment/depeba084b8/1/web/1.0). In this case, you’re deploying a profile which includes a copy of the font file or files. For example, here’s how the [open source Caprasimo font](https://fonts.google.com/specimen/Caprasimo) looks when deployed via a profile.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-20-at-5.02.37pm.png?w=599&h=524 "Screenshot 2025-06-20 at 5.02.37 PM.png")

You can access information about the font in question using the **Font Book** app on macOS Sequoia.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-20-at-5.03.54pm.png?w=599&h=385 "Screenshot 2025-06-20 at 5.03.54 PM.png")

In **Font Book.app**, you should see the profile-deployed font appearing in the **My Fonts** section. You can also access information about the font from here.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-20-at-5.03.03pm.png?w=600&h=390 "Screenshot 2025-06-20 at 5.03.03 PM.png")

But how do you extract the font file from the profile? You can also do this using the **Font Book** app. For more details, see below the jump.

You can use the following procedure to export a font which was installed using a configuration profile:

1. Open **Font Book.app**.

2. Find the font in question and select it.

3. Under the **File** menu, choose the **Export…** option.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-20-at-5.05.png?w=583&h=600 "Screenshot 2025-06-20 at 5.05.png")

4. Select where you want to save the exported font file to.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-20-at-5.07.07pm.png?w=600&h=336 "Screenshot 2025-06-20 at 5.07.07 PM.png")

5. Verify that the font file has been exported to the desired location.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-20-at-5.07.46pm.png?w=599&h=365 "Screenshot 2025-06-20 at 5.07.46 PM.png")

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2025/06/20/extracting-fonts-from-configuration-profiles-on-macos-sequoia/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2025/06/20/extracting-fonts-from-configuration-profiles-on-macos-sequoia/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2025/06/20/extracting-fonts-from-configuration-profiles-on-macos-sequoia/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2025/06/20/extracting-fonts-from-configuration-profiles-on-macos-sequoia/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2025/06/20/extracting-fonts-from-configuration-profiles-on-macos-sequoia/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2025/06/20/extracting-fonts-from-configuration-profiles-on-macos-sequoia/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2025/06/20/extracting-fonts-from-configuration-profiles-on-macos-sequoia/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2025/06/20/extracting-fonts-from-configuration-profiles-on-macos-sequoia/?share=pocket)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/)

Comments (3)
[Leave a comment](#respond)

1. ![TheAppleUser's avatar](https://1.gravatar.com/avatar/700464cb5ab99986d55c4a635276f44f5c4a8085d054dff760c2e34e05c084f6?s=32&d=identicon&r=G)

   TheAppleUser

   June 20, 2025 at 9:34 pm

   [Reply](https://derflounder.wordpress.com/2025/06/20/extracting-fonts-from-configuration-profiles-on-macos-sequoia/?replytocom=72754#respond)

   Interesting – good info, but I don’t see that font on two Sequoia Macs…perhaps Tahoe?

   Thank you for the great tips!

   * ![rtrouton's avatar](https://0.gravatar.com/avatar/fb809ae714f8d9d5be5d4c0d7086f9bb3781e9ccdd25cf8b3aa24b140a641e0e?s=32&d=identicon&r=G)

     [rtrouton](http://www.taomechworks.net)

     June 20, 2025 at 9:37 pm

     [Reply](https://derflounder.wordpress.com/2025/06/20/extracting-fonts-from-configuration-profiles-on-macos-sequoia/?replytocom=72755#respond)

     The example font I used is not included with macOS. It’s an open source font which Google has made available.

     + ![TheAppleUser's avatar](https://1.gravatar.com/avatar/700464cb5ab99986d55c4a635276f44f5c4a8085d054dff760c2e34e05c084f6?s=32&d=identicon&r=G)

       TheAppleUser

       June 20, 2025 at 9:40 pm

       Awesome, thank you!

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2025/06/20/extracting-fonts-from-configuration-profiles-on-macos-sequoia/#respond)

Δ

[Deploying software update management using Blueprints in Jamf Pro](https://derflounder.wordpress.com/2025/06/24/deploying-software-update-management-using-blueprints-in-jamf-pro/)
[Setting reduced transparency on macOS Sequoia](https://derflounder.wordpress.com/2025/06/18/setting-reduced-transparency-on-macos-sequoia/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.wordpress.com/feed/ "Subscribe with Google")
* [Youdao](http://reader.youdao.com/#url=https://derflounder.wordpress.com/feed/ "Subscribe with Youdao")
* [Xian Guo](http://www.xianguo.com/subscribe.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Xian Guo")
* [Zhua Xia](http://www.zhuaxia.com/add_channel.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Zhua Xia")
* [My Yahoo!](http://add.my.yahoo.com/rss?url=https://derflounder.wordpress.com/feed/ "Subscribe with My Yahoo!")
* [newsgator](http://www.newsgator.com/ngs/subscriber/subfext.aspx?url=https://derflounder.wordpress.com/feed/ "Subscribe with newsgator")
* [Bloglines](http://www.bloglines.com/sub/https%3A//derflounder.wordpress.com/feed/ "Subscribe with Bloglines")
* [iNezha](http://inezha.com/add?url=https://derflounder.wordpress.com/feed/ "Subscribe with iNezha")

June 2025

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | | | 1 |
| [2](https://derflounder.wordpress.com/2025/06/02/) | 3 | 4 | 5 | 6 | 7 | 8 |
| 9 | [10](https://derflounder.wordpress.com/2025/06/10/) | [11](https://derflounder.wordpress.com/2025/06/11/) | 12 | 13 | 14 | 15 |
| 16 | 17 | [18](https://derflounder.wordpress.com/2025/06/18/) | 19 | [20](https://derflounder.wordpress.com/2025/06/20/) | 21 | 22 |
| 23 | [24](https://derflounder.wordpress.com/2025/06/24/...