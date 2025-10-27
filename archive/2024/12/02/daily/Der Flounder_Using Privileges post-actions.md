---
title: Using Privileges post-actions
url: https://derflounder.wordpress.com/2024/12/01/using-privileges-post-actions/
source: Der Flounder
date: 2024-12-02
fetch_date: 2025-10-06T19:34:05.087913
---

# Using Privileges post-actions

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Privileges.app](https://derflounder.wordpress.com/category/privileges-app/), [Scripting](https://derflounder.wordpress.com/category/scripting/) > Using Privileges post-actions

## Using Privileges post-actions

December 1, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

One of the options available in Privileges 2.x is the capability of [running an action once admin rights have been granted or removed](https://github.com/SAP/macOS-enterprise-privileges/wiki/Using-Privileges#run-an-action-after-privilege-change).

![](https://derflounder.wordpress.com/wp-content/uploads/2024/12/runappwhenprivilegechange.gif?w=595 "RunAppWhenPrivilegeChange.gif")

This action can be launching an app or running a script and is set by the **Run after privilege change** setting.

![](https://derflounder.wordpress.com/wp-content/uploads/2024/12/screenshot-2024-11-30-at-12.01.07e280afpm.png?w=491&h=600 "Screenshot 2024-11-30 at 12.01.07 PM.png")

This action can be further customized by choosing to only run the action once admin rights have been granted. This can be set by the **Run only if administrator privileges have been granted** setting.

![](https://derflounder.wordpress.com/wp-content/uploads/2024/12/screenshot-2024-11-30-at-12.01.25e280afpm.png?w=491&h=600 "Screenshot 2024-11-30 at 12.01.25 PM.png")

Something to be aware of is that when using an action is that the script or application in question will be run within the context of the logged-in user. This means it will have the same level of access rights that the logged-in user currently has (standard versus admin.) This may be important if running the script or launching the application includes functionality which works for a user with admin rights but not for a user with standard rights. An example of this is running the following command using the [log command line tool](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/log.3.html):

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | log show –style syslog –predicate 'process BEGINSWITH "Privileges"' –last 1m |

[view raw](https://gist.github.com/rtrouton/df9996db1fc210e1f4378b110ac6a65c/raw/28be5c1106374401c931d700ba7e8aac3775f6e4/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/df9996db1fc210e1f4378b110ac6a65c#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

If the logged-in user has admin rights, the **log** command shown above runs without issues and without requesting authentication.

![](https://derflounder.wordpress.com/wp-content/uploads/2024/12/screenshot-2024-11-30-at-12.12.11e280afpm.png?w=595 "Screenshot 2024-11-30 at 12.12.11 PM.png")

If the logged-in user has standard rights, you get an error that the **log** command operation is not permitted.

![](https://derflounder.wordpress.com/wp-content/uploads/2024/12/screenshot-2024-11-30-at-12.10.52e280afpm.png?w=595 "Screenshot 2024-11-30 at 12.10.52 PM.png")

Privileges 2.x includes management options for setting post-actions, so that their operation and configuration can be set using configuration profiles. For more details, please see below the jump.

The relevant preference domain and key values are listed below:

* Preference domain: **corp.sap.privileges**
* Key: **PostChangeExecutablePath**
* Value: String containing the absolute filesystem path to an application or script

* Preference domain: **corp.sap.privileges**
* Key: **PostChangeActionOnGrantOnly**
* Value: Boolean

Here’s how the settings would appear in the following example:

1. The App Store app is launched as a post action.
2. The action is run once admin rights have been granted or removed.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | <?xml version="1.0" encoding="UTF-8"?> |
|  | <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "[http://www.apple.com/DTDs/PropertyList-1.0.dtd"&gt](http://www.apple.com/DTDs/PropertyList-1.0.dtd%22%26gt); |
|  | <plist version="1.0"> |
|  | <dict> |
|  | <key>PostChangeActionOnGrantOnly</key> |
|  | <false/> |
|  | <key>PostChangeExecutablePath</key> |
|  | <string>/System/Applications/App Store.app</string> |
|  | </dict> |
|  | </plist> |

[view raw](https://gist.github.com/rtrouton/1271824d13a0736d416281db93057401/raw/2e6b7f4e224d349f61bd4ee1fd5b85f9f3b7a459/corp.sap.privileges.plist)
 [corp.sap.privileges.plist](https://gist.github.com/rtrouton/1271824d13a0736d416281db93057401#file-corp-sap-privileges-plist)
hosted with ❤ by [GitHub](https://github.com)

Here’s how the settings would appear in the following example:

1. A script named **privileges\_teams\_report.sh** located in the **/usr/local/bin** directory is launched as a post action.
2. The action is run only when admin rights have been granted.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | <?xml version="1.0" encoding="UTF-8"?> |
|  | <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "[http://www.apple.com/DTDs/PropertyList-1.0.dtd"&gt](http://www.apple.com/DTDs/PropertyList-1.0.dtd%22%26gt); |
|  | <plist version="1.0"> |
|  | <dict> |
|  | <key>PostChangeActionOnGrantOnly</key> |
|  | <true/> |
|  | <key>PostChangeExecutablePath</key> |
|  | <string>/usr/local/bin/privileges\_teams\_report.sh</string> |
|  | </dict> |
|  | </plist> |

[view raw](https://gist.github.com/rtrouton/8d731bf073e331c1e5411cc272d8434b/raw/1a3c2023b30163d9d97733ae5cf1eed273ecb50b/corp.sap.privileges.plist)
 [corp.sap.privileges.plist](https://gist.github.com/rtrouton/8d731bf073e331c1e5411cc272d8434b#file-corp-sap-privileges-plist)
hosted with ❤ by [GitHub](https://github.com)

One use case for a post action script would be sending a report to a Slack or Teams channel via webhook. While [Privileges natively supports sending JSON output to a web hook](https://github.com/SAP/macOS-enterprise-privileges/wiki/Using-Privileges#run-an-action-after-privilege-change), both Slack and Teams need to have the JSON being sent to it formatted in specific ways, or else the receiving end won’t be able to work with it. They’re also different formats, so sending to Slack using JSON formatted for Teams doesn’t work and vice-versa.

I’ve written a couple of example scripts which can be used with Privileges as a post action, which are designed to be run as follows:

1. The reporting script is launched as a post action.
2. The action is run only when admin rights have been granted.

**Note:** The reason why the reporting script should be run only when admin r...