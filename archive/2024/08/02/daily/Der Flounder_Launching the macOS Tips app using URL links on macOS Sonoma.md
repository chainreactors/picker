---
title: Launching the macOS Tips app using URL links on macOS Sonoma
url: https://derflounder.wordpress.com/2024/08/01/launching-the-macos-tips-app-using-url-links-on-macos-sonoma/
source: Der Flounder
date: 2024-08-02
fetch_date: 2025-10-06T18:01:08.384216
---

# Launching the macOS Tips app using URL links on macOS Sonoma

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Launching the macOS Tips app using URL links on macOS Sonoma

## Launching the macOS Tips app using URL links on macOS Sonoma

August 1, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

One of the apps which Apple includes in macOS is the **Tips** app, which is located in the following location:

**/System/Library/CoreServices/Tips.app**

![](https://derflounder.wordpress.com/wp-content/uploads/2024/08/screenshot-2024-08-01-at-1.30.15e280afpm.png?w=595 "Screenshot 2024-08-01 at 1.30.15 PM.png")

This app provides information that Apple considers useful to folks using Macs. One of the lesser known things about it is that it has a [custom URL scheme](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app), which allows the **Tips** app to be opened by calling a particular URL. In the **Tips** app’s case, the URL scheme is the following:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | x-apple-tips:// |

[view raw](https://gist.github.com/rtrouton/839b585ca93506b5a01fdacf97419193/raw/b5e1a3eb9dea3705ed21414e93641db8c53677d9/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/839b585ca93506b5a01fdacf97419193#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

If you want to open the **Tips** app via a browser link, you can use the following URL without specifying anything else:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | x-apple-tips:// |

[view raw](https://gist.github.com/rtrouton/839b585ca93506b5a01fdacf97419193/raw/b5e1a3eb9dea3705ed21414e93641db8c53677d9/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/839b585ca93506b5a01fdacf97419193#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

![](https://derflounder.wordpress.com/wp-content/uploads/2024/08/screenshot-2024-08-01-at-1.08.png?w=595 "Screenshot 2024-08-01 at 1.08.png")

However I’ve also found it to be possible to open the **Tips** app to particular sections. For example, the following URL will open the **Tips** app and display the **What’s New** information:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | x-apple-tips://open?collection=WhatsNewInMacOS |

[view raw](https://gist.github.com/rtrouton/13097d6138369ef8a5ae6d3bff94a95f/raw/8861d14f6e0ff825a0679967b981362befa55b3d/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/13097d6138369ef8a5ae6d3bff94a95f#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

![](https://derflounder.wordpress.com/wp-content/uploads/2024/08/screenshot-2024-08-01-at-1.08-1.png?w=595 "Screenshot 2024-08-01 at 1.08.png")

The following URL will open the Tips app and display the **Welcome to Mac** information:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | x-apple-tips://open?collection=WelcomeToMac |

[view raw](https://gist.github.com/rtrouton/dfaad72d9aaaf5962b8452b716c75683/raw/6ec3855a15dae5677fc8f37b1859f688dfcf6503/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/dfaad72d9aaaf5962b8452b716c75683#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

![](https://derflounder.wordpress.com/wp-content/uploads/2024/08/screenshot-2024-08-01-at-12.57.png?w=595 "Screenshot 2024-08-01 at 12.57.png")

Because these are URLs, you can also use the [open command](https://scriptingosx.com/2017/02/the-macos-open-command/) on macOS to call the URL and have the **Tips** app open to the desired area. For example, if you have a script where as part of it you want to have the **Tips** app open and show the **What’s New** information, you can use the following command in the script:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | open "x-apple-tips://open?collection=WhatsNewInMacOS" |

[view raw](https://gist.github.com/rtrouton/c7bdd26b0b75f5082563647025641e8c/raw/f307d63dbe497978d5dd38184e7f70cb4f595062/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/c7bdd26b0b75f5082563647025641e8c#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

One thing I haven’t learned as of yet is where the **Tips** app is pulling its information for the **collection** part in the URL. If anyone has more information about this, please share it in the comments.

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2024/08/01/launching-the-macos-tips-app-using-url-links-on-macos-sonoma/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2024/08/01/launching-the-macos-tips-app-using-url-links-on-macos-sonoma/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2024/08/01/launching-the-macos-tips-app-using-url-links-on-macos-sonoma/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2024/08/01/launching-the-macos-tips-app-using-url-links-on-macos-sonoma/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2024/08/01/launching-the-macos-tips-app-using-url-links-on-macos-sonoma/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2024/08/01/launching-the-macos-tips-app-using-url-links-on-macos-sonoma/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2024/08/01/launching-the-macos-tips-app-using-url-links-on-macos-sonoma/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2024/08/01/launching-the-macos-tips-app-using-url-links-on-macos-sonoma/?share=pocket)

Like Loading...

### *Related*

Categories: [Mac admin...