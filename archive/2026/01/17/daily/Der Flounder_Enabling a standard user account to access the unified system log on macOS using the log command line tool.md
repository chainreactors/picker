---
title: Enabling a standard user account to access the unified system log on macOS using the log command line tool
url: https://derflounder.wordpress.com/2026/01/17/enabling-a-standard-user-account-to-access-the-unified-system-log-on-macos-using-the-log-command-line-tool/
source: Der Flounder
date: 2026-01-17
fetch_date: 2026-01-18T03:38:08.585188
---

# Enabling a standard user account to access the unified system log on macOS using the log command line tool

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Logging](https://derflounder.wordpress.com/category/logging/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Enabling a standard user account to access the unified system log on macOS using the log command line tool

## Enabling a standard user account to access the unified system log on macOS using the log command line tool

January 17, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As part of my work, I occasionally need to pull information from the [unified system log](https://developer.apple.com/documentation/os/logging), either directly on a Mac or [from a sysdiagnose file](https://derflounder.wordpress.com/2025/04/30/using-sysdiagnose-logarchive-files-to-provide-access-to-system-logging/), using the [log command line tool](https://ss64.com/mac/log.html). However, I also prefer to run as a standard user account most of the time and use privilege elevation tools like [SAP’s Privileges](https://github.com/SAP/macOS-enterprise-privileges) or the [privilege elevation functionality built into Jamf’s Self Service+ tool](https://learn.jamf.com/en-US/bundle/jamf-connect-documentation-current/page/Privilege_Elevation_Local_Accounts.html) to get admin privileges when needed.

The combination of the two sometimes means I get halted while working because the **log** command line tool needs an account with admin privileges to run when it is getting log information from the unified system log on the Mac I’m using. Using the **log** command line tool doesn’t require root privileges or require admin authorization, but it needs to be run by a user with admin rights.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-17-at-5.47.53pm.png?w=595 "Screenshot 2026-01-17 at 5.47.53 PM.png")

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-17-at-5.47.57pm.png?w=595 "Screenshot 2026-01-17 at 5.47.57 PM.png")

**Note:** This requirement for admin privileges does not appear to be coming from the **log** command line tool itself, but instead is coming from the unified system log. The reason I’m saying this is that accessing logs using the **log** tool [from a sysdiagnose file](https://derflounder.wordpress.com/2025/04/30/using-sysdiagnose-logarchive-files-to-provide-access-to-system-logging/) does not require admin privileges. If any readers have more information about this topic, please let me know in the comments.

This has been an occasional annoyance because I get pulled briefly out of my focus while working in order to elevate my account’s privileges and then go back to my work. However, I was able to develop a solution for this issue using the [sudo command line tool](https://ss64.com/mac/sudo.html). For more details, please see below the jump.

This method uses the ability on macOS for the **sudo** command line tool to use properly formatted configurations for the **sudo** tool, where those configuration files are stored as plaintext files in the **/private/etc/sudoers.d** directory. The following process will create a **sudo** configuration which is stored in a plaintext file named **logstandarduser** which will be stored in the **/private/etc/sudoers.d** directory.

The configuration should be a plaintext file and formatted as followed:

A. Enter the following:

**%staff**

B. Hit the Tab key to create a tabbed space
C. Enter the rest of the line:

**ALL = (ALL) /usr/bin/log**

The complete configuration file should look like this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | %staff ALL = (ALL) /usr/bin/log |

[view raw](https://gist.github.com/rtrouton/8a8b5bfe0c148d62313c0c13c7cca79f/raw/09d941cade554948064175738499712589121e34/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/8a8b5bfe0c148d62313c0c13c7cca79f#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

What this does is create a **sudo** configuration which allows all members of the **staff** group on the Mac, which is a group that has all local users on the Mac as members, to run the **log** command line tool with root privileges. This removes the need for the account to have admin rights and enables accounts with only standard rights to use the **log** command line tool to get information from the unified system log on that Mac.

This sudo configuration can be deployed to Macs by either copying the **logstandarduser** file into the **/private/etc/sudoers.d** directory (a task which requires root privileges) or by [using DDM](https://derflounder.wordpress.com/2025/05/27/deploying-sudo-configurations-using-blueprints-in-jamf-pro/) to deploy the **logstandarduser** file as a configuration file for the **sudo** tool.

Once the **sudo** configuration is deployed, it should be possible for any local account on the Mac to query the unified system log via using the **sudo** command line tool to run the **log** command line tool.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-17-at-6.21.26pm.png?w=595 "Screenshot 2026-01-17 at 6.21.26 PM.png")

### Share this:

* [Print (Opens in new window)
  Print](https://derflounder.wordpress.com/2026/01/17/enabling-a-standard-user-account-to-access-the-unified-system-log-on-macos-using-the-log-command-line-tool/#print?share=print)
* Email a link to a friend (Opens in new window)
  Email
* More

* [Share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2026/01/17/enabling-a-standard-user-account-to-access-the-unified-system-log-on-macos-using-the-log-command-line-tool/?share=facebook)
* [Share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2026/01/17/enabling-a-standard-user-account-to-access-the-unified-system-log-on-macos-using-the-log-command-line-tool/?share=linkedin)
* [Share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2026/01/17/enabling-a-standard-user-account-to-access-the-unified-system-log-on-macos-using-the-log-command-line-tool/?share=reddit)
* [Share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2026/01/17/enabling-a-standard-user-account-to-access-the-unified-system-log-on-macos-using-the-log-command-line-tool/?share=twitter)
* [Share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2026/01/17/enabling-a-standard-user-account-to-access-the-unified-system-log-on-macos-using-the-log-command-line-tool/?share=pinterest)
* [Share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2026/01/17/enabling-a-standard-user-account-to-access-the-unified-system-log-on-macos-using-the-log-command-line-tool/?share=tumblr)
* [Share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2026/01/17/enabling-a-standard-user-account-to-access-the-unified-system-log-on-macos-using-the-log-command-line-tool/?share=pocket)

Like Loading...

### *Related*

Categories: [Logging](https://derflounder.wordpress.com/category/logging/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/)

Comments (0)
[Leave a comment](#respond)

1....