---
title: Finding the version number of the Xcode command line tools using the softwareupdate command
url: https://derflounder.wordpress.com/2023/01/18/finding-the-version-number-of-the-xcode-command-line-tools-using-the-softwareupdate-command/
source: Der Flounder
date: 2023-01-19
fetch_date: 2025-10-04T04:16:05.842814
---

# Finding the version number of the Xcode command line tools using the softwareupdate command

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Xcode](https://derflounder.wordpress.com/category/xcode/), [Xcode Command Line Tools](https://derflounder.wordpress.com/category/xcode-command-line-tools/) > Finding the version number of the Xcode command line tools using the softwareupdate command

## Finding the version number of the Xcode command line tools using the softwareupdate command

January 18, 2023
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As part of making sure your development environment is up to date, it’s often helpful to know what version of Xcode or the Xcode Command Line Tools that you’re using. For [Xcode](https://developer.apple.com/xcode), this is relatively straightforward as you can check **Xcode.app**‘s version number or you can use the command shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | xcodebuild -version |

[view raw](https://gist.github.com/rtrouton/16c5b208d6d5bfd65d8d1c35c8982893/raw/1d759210d8ae6e72d4428db1afb355fd41e92ba2/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/16c5b208d6d5bfd65d8d1c35c8982893#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

On a Mac running Xcode, running that command should provide output similar to what’s shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % xcodebuild -version |
|  | Xcode 14.2 |
|  | Build version 14C18 |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/641f9ff840a0ed0c10bb08721942c3ea/raw/b22f23da3fa0d9670eb965d1b836a64cd7c45ed0/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/641f9ff840a0ed0c10bb08721942c3ea#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

However, for the [Xcode Command Line Tools](https://www.makeuseof.com/install-xcode-command-line-tools/), this process isn’t as straightforward. There isn’t a specific app to check for version information and running the command above results in the following output:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % xcodebuild -version |
|  | xcode-select: error: tool 'xcodebuild' requires Xcode, but active developer directory '/Library/Developer/CommandLineTools' is a command line tools instance |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/e0c3b043d44685ff413a28ba5ead5b5d/raw/0f5ecb1a26b1ef714d4a0dbf3d2ea577dcb4b81c/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/e0c3b043d44685ff413a28ba5ead5b5d#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

So how can you determine the latest installed version of the Xcode Command Line Tools? One way is to use the **softwareupdate** command’s **history** function, which should show all of the versions of the Xcode Command Line Tools which have been installed. You can use the following command to display all the installations of the Xcode Command Line Tools:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | softwareupdate –history | grep "Command Line Tools for Xcode" |

[view raw](https://gist.github.com/rtrouton/0a559054491820f8f59cad8de4f04718/raw/e7d2031b81f0854a94d9d7cf67128073cf5b7fd6/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/0a559054491820f8f59cad8de4f04718#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

For example, since both Xcode Command Line Tools 12 and Xcode Command Line Tools 13 are available for macOS Big Sur 11.7.x, you may see output similar to what’s shown below on a Mac running Big Sur:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % softwareupdate –history | grep "Command Line Tools for Xcode" |
|  | Command Line Tools for Xcode 12.5 09/21/2022, 15:04:54 |
|  | Command Line Tools for Xcode 13.2 01/17/2023, 11:18:19 |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/856d03619ec311048deba84f459eeb7a/raw/06e44be33505afa88e4e76fc52c12474400cd0ff/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/856d03619ec311048deba84f459eeb7a#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

Since the latest installed version of the Xcode Command Line Tools should be listed at the bottom of the output from the **softwareupdate** command’s **history** function, you should be able to use the following command to get the version number of the latest installed version of the Xcode Command Line Tools:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | softwareupdate –history | awk '/Command Line Tools for Xcode/ {print $6}' | tail -1 |

[view raw](https://gist.github.com/rtrouton/ea2eb66eaaa0f537169fd860a2d7bf08/raw/0a72626c6026b0ff0c5e6bc1da224dc6a373b276/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/ea2eb66eaaa0f537169fd860a2d7bf08#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

As of the date of this post, the latest version of the Xcode Command Line Tools on macOS Ventura 13.1 is version 14.2, so you should see output similar to what’s shown below on a fully updated macOS 13.1 Mac running the latest version of the Xcode command line tools:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | user...