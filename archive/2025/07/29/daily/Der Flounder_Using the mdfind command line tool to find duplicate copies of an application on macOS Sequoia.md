---
title: Using the mdfind command line tool to find duplicate copies of an application on macOS Sequoia
url: https://derflounder.wordpress.com/2025/07/28/using-the-mdfind-command-line-tool-to-find-duplicate-copies-of-an-application-on-macos-sequoia/
source: Der Flounder
date: 2025-07-29
fetch_date: 2025-10-06T23:50:54.877393
---

# Using the mdfind command line tool to find duplicate copies of an application on macOS Sequoia

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Scripting](https://derflounder.wordpress.com/category/scripting/) > Using the mdfind command line tool to find duplicate copies of an application on macOS Sequoia

## Using the mdfind command line tool to find duplicate copies of an application on macOS Sequoia

July 28, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

A common issue faced by Mac admins is that users can have multiple copies of an application on their system. This can be the result of users having standard user rights and running applications out of the home directories, or users reorganizing the **Applications** directory in a way that makes more sense to them for their needs. Meanwhile, when Mac admins need to report on whether the apps on the fleet are up to date, these additional or reorganized apps may not be patched but do show up in the software reporting as being out of date.

When you run into these situations, how to handle them? The first step is finding where the duplicates are and reporting on them. To do this, you can use the [mdfind](https://ss64.com/mac/mdfind.html) command line tool, using the [kMDItemCFBundleIdentifier metadata attribute](https://developer.apple.com/documentation/coreservices/kmditemcfbundleidentifier). This metadata attribute reports on the [bundle identifier](https://developer.apple.com/documentation/bundleresources/information-property-list/cfbundleidentifier) used by an application, so it should pick up all copies of an app which are using that unique identifier for that app. For more details, please see below the jump.

As an example case, I’m going to use the following scenario:

1. I need to locate all copies of the [BBEdit](https://www.barebones.com/products/bbedit/) app installed on a particular Mac
2. The user in question has three copies of BBEdit installed.

* In **/Applications**
* In a user-created **BBEdit** directory inside of **/Applications**.
* In a user-created **Applications** directory inside of their home folder.

BBEdit’s bundle identifier is **com.barebones.bbedit**, so I can use the following **mdfind** command to find all copies of **BBEdit.app**:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/mdfind "kMDItemCFBundleIdentifier == 'com.barebones.bbedit'" |

[view raw](https://gist.github.com/rtrouton/eacb2cca2c7ddfe5d8364c271ab76a61/raw/e0393edb020be4c9fb323d55623bda80553d5acc/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/eacb2cca2c7ddfe5d8364c271ab76a61#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

In the scenario described above, that should provide output similar to what’s shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % /usr/bin/mdfind "kMDItemCFBundleIdentifier == 'com.barebones.bbedit'" |
|  | /Applications/BBEdit/BBEdit.app |
|  | /Users/username/Applications/BBEdit.app |
|  | /Applications/BBEdit.app |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/fc3dc6c750fa1a354c6e5517135ca4a2/raw/8ed4c9889416a59cfa0d76a7db46448e03a0bec9/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/fc3dc6c750fa1a354c6e5517135ca4a2#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

However, you may not necessarily want to know about **/Applications/BBEdit.app** as that may be the only version you want installed. To exclude **/Applications/BBEdit.app** from your results, you can use the [grep](https://ss64.com/mac/grep.html) command line tool’s **-v** inverse match and **-E** regular expression options to exclude **/Applications/BBEdit.app** from the list of results:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % /usr/bin/mdfind "kMDItemCFBundleIdentifier == 'com.barebones.bbedit'" | grep -vE "^/Applications/BBEdit.app" |
|  | /Applications/BBEdit/BBEdit.app |
|  | /Users/username/Applications/BBEdit.app |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/22dc67afbbd9b3bea0ffe969cea761d2/raw/cefe70a33b53935daa24f11fc8acf09c0888f27b/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/22dc67afbbd9b3bea0ffe969cea761d2#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

If you needed to exclude additional directories (for example, you must exclude searching the user’s home folder for privacy reasons), you can add additional regular expressions to the **grep** command to exclude additional undesired results. Here’s an example where you’re excluding results from **/Users** and for **/Applications/BBEdit.app**:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % /usr/bin/mdfind "kMDItemCFBundleIdentifier == 'com.barebones.bbedit'" | grep -vE "^/Users|^/Applications/BBEdit.app" |
|  | /Applications/BBEdit/BBEdit.app |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/8c9a44b0f4fdd476fd489d7d856851d0/raw/17bcc32b9d35b4e617a2849735b1d455ee4ad7e7/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/8c9a44b0f4fdd476fd489d7d856851d0#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

For our scenario, here’s a script that should identify all installed copies of BBEdit on a Mac and display a list of all copies except for **/Applications/BBEdit.app**:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | #!/bin/bash |
|  |  |
|  | appname="BBEdit" |
|  | appidentifier="com.barebones.bbedit" |
|  | /usr/bin/mdfind "kMDItemCFBundleIdentifier == '$appidentifier'" | grep -vE "^/Applications/$appname.app" |

[view raw](https://gist.github.com/rtrouton/5d15886757f7aad7a5cad52fd2bda7c7/raw/5f7acbaf0c87ef64ba8e34a606830fd832fb0088/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/5d15886757f7aad7a5cad52fd2bda7c7#file-gistfile1-txt)
hosted with ❤ by [GitHub](https:/...