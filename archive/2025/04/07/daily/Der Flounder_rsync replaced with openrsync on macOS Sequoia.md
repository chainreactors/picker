---
title: rsync replaced with openrsync on macOS Sequoia
url: https://derflounder.wordpress.com/2025/04/06/rsync-replaced-with-openrsync-on-macos-sequoia/
source: Der Flounder
date: 2025-04-07
fetch_date: 2025-10-06T22:03:29.916084
---

# rsync replaced with openrsync on macOS Sequoia

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > rsync replaced with openrsync on macOS Sequoia

## rsync replaced with openrsync on macOS Sequoia

April 6, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

On many Unix-based operating systems, [rsync](https://en.wikipedia.org/wiki/Rsync) is a command line tool for transferring and synchronizing files on a computer, either between storage attached directly to the computer or between another computer located elsewhere on a network. The **rsync** command line tool has long been included on macOS, but Apple has provided the last version of **rsync** 2.x ([rsync 2.6.9, released in November 2006](https://download.samba.org/pub/rsync/NEWS#2.6.9)) and did not update **rsync** past that even though **rsync** 3.x was released. Why not? It has to do with the version of the [GNU General Public License](https://en.wikipedia.org/wiki/GNU_General_Public_License) (GPL) open source license that **rsync** 2.x and 3.x were released under, with [rsync 2.x being released under the GPLv2 license](https://rsync.samba.org/GPL2.html) and [rsync 3.x being released under the GPLv3 license](https://rsync.samba.org/GPL.html). Without going in-depth into the background legal issues, the reason for not providing **rsync** 3.x is that Apple decided that while it could comply with the terms of GPLv2 license with regards to **rsync** 2.x, it could not comply with the terms of GPLv3 license with regards to **rsync** 3.x.

What this has meant for macOS is that it has been shipping with a version of **rsync** which was last updated in 2006. While Apple has been updating the **rsync** 2.6.9 command line tool it shipped with macOS as needed in response to security issues and other problems, the fact remains that Apple’s version of **rsync** up until macOS Sequoia was almost twenty years old and did not include any of the new features introduced in **rsync** versions which came after version 2.6.9.

Now with macOS Sequoia, Apple has replaced **rsync** 2.6.9 with [openrsync](https://man.openbsd.org/openrsync), an implementation of **rsync** which is not using any version of the GPL open source license. Instead, **openrsync** is licensed under the [BSD family of licenses](https://en.wikipedia.org/wiki/BSD_licenses), specifically the [ISC license](https://en.wikipedia.org/wiki/ISC_license). The ISC license is a [permissive license](https://en.wikipedia.org/wiki/Permissive_software_license), which means it places minimal restrictions on on how the licensed software can be used, modified and distributed, which means Apple decided it is able to comply with the terms of the license for **openrsync** where it decided it could not comply with the terms of GPLv3 license with regards to **rsync** 3.x.

So I’ve spent a bunch of time talking about licenses. Why does this change matter? It matters in two ways:

1. Apple can ship updated versions of **openrsync** going forward without having to be concerned as to whether or not Apple can comply with the GPL open source license for **rsync**.
2. The **openrsync** command line tool is compatible with **rsync**, but as noted in the documentation [openrsync accepts only a subset of rsync’s command line arguments](https://github.com/kristapsdz/openrsync).

Item number 2 is important for Mac admins because it may mean that **rsync** functionality that worked on older versions of macOS may not be working now on macOS Sequoia because that functionality is not available as part of the **openrsync** command line tool included with macOS Sequoia. For more information about what functionality is supported in the **openrsync** command line tool on macOS Sequoia, please see the link below:

<https://manp.gs/mac/1/openrsync>

As of macOS 15.4, the **openrsync** tool is linked to **/usr/bin/rsync** so you can run the the **openrsync** command line tool like you have been the **rsync** command line tool. For version information about the **openrsync** command line tool, run the command shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/rsync –version |

[view raw](https://gist.github.com/rtrouton/aabc0329270ccde34dc40497980a49fd/raw/2a6836bf5d89be910a058857ea288505bedc5f13/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/aabc0329270ccde34dc40497980a49fd#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

You should see output similar to that shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % /usr/bin/rsync –version |
|  | openrsync: protocol version 29 |
|  | rsync version 2.6.9 compatible |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/c6493f74e9fb0210a3a3f33817357732/raw/459b1f7e5fbba2ac7749d529ee42de386217f5c0/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/c6493f74e9fb0210a3a3f33817357732#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2025/04/06/rsync-replaced-with-openrsync-on-macos-sequoia/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2025/04/06/rsync-replaced-with-openrsync-on-macos-sequoia/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2025/04/06/rsync-replaced-with-openrsync-on-macos-sequoia/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2025/04/06/rsync-replaced-with-openrsync-on-macos-sequoia/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2025/04/06/rsync-replaced-with-openrsync-on-macos-sequoia/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2025/04/06/rsync-replaced-with-openrsync-on-macos-sequoia/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2025/04/06/rsync-replaced-with-openrsync-on-macos-sequoia/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2025/04/06/rsync-replaced-with-openrsync-on-macos-sequoia/?share=pocket)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/)

Comments (16)
[Leave a comment](#respond)

1. ![mike's avatar](https://2.gravatar.com/avatar/ee89ff421e969e2461d90d1713ae5b0dc92e7446cf8c5643069c1d6cfd1a2a03?s=32&d=identicon&r=G)

   mike

   April 6, 2025 at 10:08 pm

   [Reply](https://derflounder.wordpress.com/2025/04/06/rsync-r...