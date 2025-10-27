---
title: Adding hidden Login Items on macOS Ventura
url: https://derflounder.wordpress.com/2022/10/27/adding-hidden-login-items-on-macos-ventura/
source: Der Flounder
date: 2022-10-28
fetch_date: 2025-10-03T21:05:05.761488
---

# Adding hidden Login Items on macOS Ventura

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Adding hidden Login Items on macOS Ventura

## Adding hidden Login Items on macOS Ventura

October 27, 2022
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

One of the changes made between macOS Monterey’s System Preferences and macOS Ventura’s System Settings is that the [Hide checkbox in System Preferences’ Login Items](https://support.apple.com/guide/mac-help/open-items-automatically-when-you-log-in-mh15189/12.0/mac/12.0) has disappeared from [System Settings’ Login Items](https://support.apple.com/guide/mac-help/open-items-automatically-when-you-log-in-mh15189/13.0/mac/13.0).

**Login Items in System Preferences**

![Screen Shot 2022 10 27 at 2 25 28 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/10/screen-shot-2022-10-27-at-2.25.28-pm.png?w=600&h=449 "Screen Shot 2022-10-27 at 2.25.28 PM.png")

**Login Items in System Settings**

![Screenshot 2022 10 27 at 2 40 18 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/10/screenshot-2022-10-27-at-2.40.18-pm.png?w=599&h=524 "Screenshot 2022-10-27 at 2.40.18 PM.png")

Fortunately for those who want to continue being able to launch applications on login and automatically hide them, it’s still possible to do so on macOS Ventura from the command line [using osascript](https://www.oreilly.com/library/view/applescript-in-a/1565928415/re156.html).

To do this, run a command similar to the one shown below using the logged-in user’s privileges:

```
/usr/bin/osascript -e 'tell application "System Events" to make login item at end with properties {path:"/path/to/itemname", hidden:true}'
```

For example, if you want Safari to launch at login with its windows automatically hidden, run the command below using the logged-in user’s privileges:

```
/usr/bin/osascript -e 'tell application "System Events" to make login item at end with properties {path:"/Applications/Safari.app", hidden:true}'
```

Safari will appear in the **Login Items** list without any sign that it’s launching as hidden, but the application behavior on login will be just like it would be on earlier versions of macOS where the **Hide** checkbox was checked.

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2022/10/27/adding-hidden-login-items-on-macos-ventura/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2022/10/27/adding-hidden-login-items-on-macos-ventura/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2022/10/27/adding-hidden-login-items-on-macos-ventura/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2022/10/27/adding-hidden-login-items-on-macos-ventura/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2022/10/27/adding-hidden-login-items-on-macos-ventura/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2022/10/27/adding-hidden-login-items-on-macos-ventura/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2022/10/27/adding-hidden-login-items-on-macos-ventura/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2022/10/27/adding-hidden-login-items-on-macos-ventura/?share=pocket)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/)

Comments (6)
[Leave a comment](#respond)

1. ![Rocío Segoviano Aguilar's avatar](https://0.gravatar.com/avatar/fe95c444097e7d543fb72f3952b8938b4289995a90f5914da3cdd7d59e64210d?s=32&d=identicon&r=G)

   Rocío Segoviano Aguilar

   November 11, 2022 at 2:18 am

   [Reply](https://derflounder.wordpress.com/2022/10/27/adding-hidden-login-items-on-macos-ventura/?replytocom=68706#respond)

   What about if my cellphone is hacked with “Pegasus”!!!
2. ![Frédéric Harper's avatar](https://0.gravatar.com/avatar/38d9a54b27b1bcb9bc2faf101a973bdb3979decaa7f7d3b74fafad9b7672d75c?s=32&d=identicon&r=G)

   [Frédéric Harper](https://fred.dev)

   November 16, 2022 at 11:04 pm

   [Reply](https://derflounder.wordpress.com/2022/10/27/adding-hidden-login-items-on-macos-ventura/?replytocom=68772#respond)

   It’s missing two things: trailing single quote at the end of the command, and Ventura 13.0.1, you need to append the name of the login item if you don’t want a “login item UNKNOWN” error.

   * ![Tiago's avatar](https://2.gravatar.com/avatar/b18ffead5f99fa93f249cbdf3953a30fa805227205d2cb7b345e3fed27f98f67?s=32&d=identicon&r=G)

     [Tiago](http://gravatar.com/horrystorm)

     December 2, 2022 at 12:51 pm

     [Reply](https://derflounder.wordpress.com/2022/10/27/adding-hidden-login-items-on-macos-ventura/?replytocom=69000#respond)

     How to append the name of the login item?

     + ![Alec's avatar](https://0.gravatar.com/avatar/6c10ba4fb5cf6ed0d3b9a962f518c95ed830f821f6044419f5624eacc701f56b?s=32&d=identicon&r=G)

       Alec

       January 5, 2023 at 10:15 pm

       As a final property in the dictionary:

       ❯ /usr/bin/osascript -e ‘tell application “System Events” to make login item at end with properties {path:”/Applications/Safari.ap”, hidden:true, name:”Safari”}’
3. ![TommyWillB's avatar](https://2.gravatar.com/avatar/8789c3095760f803970e10495070ba7b335f45c58b9e0cffac021eacfa5dad0c?s=32&d=identicon&r=G)

   [TommyWillB](http://www.tommywillb.com)

   January 28, 2023 at 4:00 pm

   [Reply](https://derflounder.wordpress.com/2022/10/27/adding-hidden-login-items-on-macos-ventura/?replytocom=69655#respond)

   I did this with Activity Monitor. It did not launch it “hidden”… It merely minimized it.
4. ![TommyWillB's avatar](https://2.gravatar.com/avatar/8789c3095760f803970e10495070ba7b335f45c58b9e0cffac021eacfa5dad0c?s=32&d=identicon&r=G)

   [TommyWillB](http://www.tommywillb.com)

   January 28, 2023 at 4:03 pm

   [Reply](https://derflounder.wordpress.com/2022/10/27/adding-hidden-login-items-on-macos-ventura/?replytocom=69656#respond)

   Your example commands are missing the final end single-quote ‘

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2022/10/27/adding-hidden-login-items-on-macos-ventura/#respond)

Δ

[Downloading macOS Monterey from the App Store](https://derflounder.wordpress.com/2022/11/11/downloading-macos-monterey-from-the-app-store/)
[Opening macOS Ventura’s System Settings to desired locations via the command line](https://derflounder.wordpress.com/2022/10/25/opening-macos-venturas-system-settings-to-desired-locations-via-the-command-line/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.wordpress.com/feed/ "Subscribe with Google")
* [Youdao](http://reader.youdao.com/#url=https://derflounder.wordpress.com/feed/ "Subscribe with Youdao")
* [Xian Guo](http://www.xianguo.com/subscribe.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Xian Guo")
* [Zhua Xia](http://www.zhuaxia.com/add_channel.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Zhua Xia")
* [My Yahoo!](http://add.my.yahoo.com/rss?url=https://...