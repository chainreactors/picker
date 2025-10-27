---
title: Disabling Apple Mail website link previews compose option on macOS Sequoia
url: https://derflounder.wordpress.com/2025/01/05/disabling-apple-mail-website-link-previews-compose-option-on-macos-sequoia/
source: Der Flounder
date: 2025-01-06
fetch_date: 2025-10-06T20:07:32.306114
---

# Disabling Apple Mail website link previews compose option on macOS Sequoia

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/) > Disabling Apple Mail website link previews compose option on macOS Sequoia

## Disabling Apple Mail website link previews compose option on macOS Sequoia

January 5, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

Beginning with macOS Ventura, Apple’s Mail app adds a rich link preview when you’re composing an email and [paste a web address into the email window](https://www.macrumors.com/how-to/disable-apple-mail-url-link-previews/). For example, here’s how it looks when I paste the following URL into a new email:

<https://wwww.apple.com>

![](https://derflounder.wordpress.com/wp-content/uploads/2025/01/screenshot-2025-01-05-at-3.39.png?w=600&h=372 "Screenshot 2025-01-05 at 3.39.png")

For those who find this behavior undesirable and wish to turn it off, it can be disabled using the following process:

1. Launch Mail

2. Under the **Mail** menu, select **Settings**.

3. In the **Settings** window, select the **Composing** option.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/01/screenshot-2025-01-05-at-4.30.png?w=599&h=444 "Screenshot 2025-01-05 at 4.30.png")

4. Uncheck the **Add link previews** option.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/01/screenshot-2025-01-05-at-4.31.png?w=600&h=508 "Screenshot 2025-01-05 at 4.31.png")

With this option disabled, here’s how it looks when I paste the following URL into a new email:

<https://wwww.apple.com>

![](https://derflounder.wordpress.com/wp-content/uploads/2025/01/screenshot-2025-01-05-at-3.51.png?w=600&h=372 "Screenshot 2025-01-05 at 3.51.png")

I have not found a way to disable the **Add link previews** option in Apple’s Mail app on macOS Sequoia using a [defaults](https://ss64.com/mac/defaults.html) command, but it is possible to disable the **Add link previews** option using a configuration profile. For more details, please see below the jump.

The relevant preference domain and key values are below:

* Preference domain: **com.apple.mail**
* Key: **AddLinkPreviews**
* Value: Boolean

Setting a boolean value of **false** will disable the **Add link previews** option in Apple’s Mail app on macOS Sequoia. I’ve built a configuration profile with the boolean value of **false** set, where the profile is available on GitHub via the link below:

<https://github.com/rtrouton/profiles/tree/main/AppleMailDisableLinkPreviews>

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2025/01/05/disabling-apple-mail-website-link-previews-compose-option-on-macos-sequoia/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2025/01/05/disabling-apple-mail-website-link-previews-compose-option-on-macos-sequoia/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2025/01/05/disabling-apple-mail-website-link-previews-compose-option-on-macos-sequoia/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2025/01/05/disabling-apple-mail-website-link-previews-compose-option-on-macos-sequoia/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2025/01/05/disabling-apple-mail-website-link-previews-compose-option-on-macos-sequoia/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2025/01/05/disabling-apple-mail-website-link-previews-compose-option-on-macos-sequoia/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2025/01/05/disabling-apple-mail-website-link-previews-compose-option-on-macos-sequoia/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2025/01/05/disabling-apple-mail-website-link-previews-compose-option-on-macos-sequoia/?share=pocket)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/)

Comments (3)
[Leave a comment](#respond)

1. ![Josh's avatar](https://2.gravatar.com/avatar/89e4973c7dc8ee1f6465b7637ecbf51d7b51548276c760dfd1a95a860cb7b822?s=32&d=identicon&r=G)

   Josh

   January 6, 2025 at 8:43 pm

   [Reply](https://derflounder.wordpress.com/2025/01/05/disabling-apple-mail-website-link-previews-compose-option-on-macos-sequoia/?replytocom=72645#respond)

   Does it need to be in a <Forced> array to work? Could it be a <Set-once> to allow users who might like that functionality to knowingly opt-in to it?
2. ![Josh's avatar](https://2.gravatar.com/avatar/89e4973c7dc8ee1f6465b7637ecbf51d7b51548276c760dfd1a95a860cb7b822?s=32&d=identicon&r=G)

   Josh

   January 6, 2025 at 8:44 pm

   [Reply](https://derflounder.wordpress.com/2025/01/05/disabling-apple-mail-website-link-previews-compose-option-on-macos-sequoia/?replytocom=72646#respond)

   Does it need to be in a <Forced> array to work? Could it be in a <Set-Once> to allow users to knowingly opt-in to that behavior, if they want it?
3. ![paulrauschelbach's avatar](https://1.gravatar.com/avatar/a34a94f7f451f33347acb00a5f57a62d6d01d1d0420302bbc0167a1cf8a1c6a5?s=32&d=identicon&r=G)

   paulrauschelbach

   January 10, 2025 at 4:48 pm

   [Reply](https://derflounder.wordpress.com/2025/01/05/disabling-apple-mail-website-link-previews-compose-option-on-macos-sequoia/?replytocom=72649#respond)

   This command works to set it the value macOS Sequoia:

   defaults write com.apple.mail AddLinkPreviews false

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2025/01/05/disabling-apple-mail-website-link-previews-compose-option-on-macos-sequoia/#respond)

Δ

[Generating randomized long usernames for Jamf Pro standard user accounts](https://derflounder.wordpress.com/2025/01/12/generating-randomized-long-usernames-for-jamf-pro-standard-users/)
[Suppressing the Welcome to Mac screen with a configuration profile on macOS Sequoia](https://derflounder.wordpress.com/2025/01/04/suppressing-the-welcome-to-mac-screen-with-a-configuration-profile-on-macos-sequoia/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.wordpress.com/feed/ "Subscribe with Google")
* [Youdao](http://reader.youdao.com/#url=https://derflounder.wordpress.com/feed/ "Subscribe with Youdao")
* [Xian Guo](http://www.xianguo.com/subscribe.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Xian Guo")
* [Zhua Xia](http://www.zhuaxia.com/add_channel.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Zhua Xia")
* [My Yahoo!](http://add.my.yahoo.com/rss?url=https://derflounder.wordpress.com/feed/ "Subscribe with My Yahoo!")
* [newsgator](http://www.newsgator.com/ngs/subscriber/subfext.aspx?url=https://derflounder.wordpress.com/feed/ "Subscribe with newsgator")
* [Bloglines](http://www.bloglines.com/sub/https%3A//derflounder.wordpress.com/feed/ "Subscribe with Bloglines")
* [iNezha](http://inezha.com/add?url=https://derflounder.wordpress.com/feed/ "Subscribe with ...