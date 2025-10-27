---
title: LogUI build 65 introduces a Logarchive Tool
url: https://eclecticlight.co/2025/06/11/logui-build-65-introduces-a-logarchive-tool/
source: Instapaper: Unread
date: 2025-06-12
fetch_date: 2025-10-06T22:56:00.271019
---

# LogUI build 65 introduces a Logarchive Tool

[Skip to content](#content)

[![](https://eclecticlight.co/wp-content/uploads/2015/01/eclecticlightlogo-e1421784280911.png?w=103)](https://eclecticlight.co/)

# [The Eclectic Light Company](https://eclecticlight.co/)

Macs & painting – 🦉 No AI content

##### Main navigation

Menu

* [Downloads](https://eclecticlight.co/downloads/)
* [Freeware](https://eclecticlight.co/free-software-menu/)
* [M-series Macs](https://eclecticlight.co/m1-macs/)
* [Mac Problems](https://eclecticlight.co/mac-troubleshooting-summary/)
* [Mac articles](https://eclecticlight.co/mac-problem-solving/)
* [Macs](https://eclecticlight.co/category/macs/)
* [Art](https://eclecticlight.co/painting-topics/)

[hoakley](https://eclecticlight.co/author/hoakley/)
[June 11, 2025](https://eclecticlight.co/2025/06/11/logui-build-65-introduces-a-logarchive-tool/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/), [Updates](https://eclecticlight.co/category/updates/)

# LogUI build 65 introduces a Logarchive Tool

![](https://eclecticlight.co/wp-content/uploads/2025/03/loguiicon.jpg?w=1005)

Just before the start of WWDC, I released an update to my log browser LogUI adding support for accessing logarchives. I promised that there was more support for logarchives on its way. LogUI 1.0 build 65 dedicates a whole window to them, in its Logarchive Tool.

There are many situations where you can’t access the active log, and you can’t create a logarchive using the `log` command tool or a `sysdiagnose`. These include:

* When you only have access to the contents of the Mac or device’s storage, particularly in forensics, or following hardware failure.
* When you want access to the logs in a backup. Time Machine backups normally include full log files, for example.
* When you don’t have `ssh` or similar access to a remote Mac.
* When the log records may be incomplete or damaged.

Provided that you can copy two folders from the hidden /var/db folder on that Mac or device, LogUI can turn those into a browsable logarchive.

#### Create a logarchive from folders

On your Mac, create a folder somewhere convenient such as ~/Documents. As this method doesn’t use the `log` command, this can be on an external disk if you wish.

From the source Data volume copy the folders at /var/db/diagnostics and /var/db/uuidtext to your folder, so it looks like this.

[![](https://eclecticlight.co/wp-content/uploads/2025/06/logui117.jpg)](https://eclecticlight.co/wp-content/uploads/2025/06/logui117.jpg)

Open LogUI, and from its Window menu open its **Logarchive Tool**. This offers you four tools and two checkboxes. Click on the **Create Logarchive** tool and first select the folder you created, containing the log folders. Then give the new logarchive a suitable name and save it somewhere convenient.

[![](https://eclecticlight.co/wp-content/uploads/2025/06/logui111.png)](https://eclecticlight.co/wp-content/uploads/2025/06/logui111.png)

LogUI should then inform you in its window that creation has completed. As this is performed using undocumented code for an undocumented format, it may not always work correctly. If there are any problems, repeat the same with the **Debug** checkbox ticked, and it will give you a detailed commentary of what it does, which should help you understand what went wrong.

#### Getting info about a logarchive

The trickiest part of accessing logarchives is knowing what they contain, more specifically the time periods for which they have log records. LogUI’s Logarchive window provides two aids to provide you with that information, in its **Catalogue** and **Analyse** tools.

**Catalogue** simply lists all the tracev3 files in the logarchive, giving the datestamps each was created and last modified, together with the period between those, and the file size.

[![](https://eclecticlight.co/wp-content/uploads/2025/06/logui114.png)](https://eclecticlight.co/wp-content/uploads/2025/06/logui114.png)

Leave that open as you browse that logarchive, to guide your way through its entries.

**Analyse** goes further, in telling you about the entries in each of the *persist* tracev3 files in the logarchive. It tells you the most common processes that wrote the entries in each of those files, allowing you to hone in on which are of most interest. If you want to extract that information for analysis in a spreadsheet, tick the **CSV** checkbox and it will be shown ready to import into your favourite spreadsheet.

[![](https://eclecticlight.co/wp-content/uploads/2025/06/logui116.png)](https://eclecticlight.co/wp-content/uploads/2025/06/logui116.png)

Finally, to save the contents of the current window as a text file, click on the **Save Text** tool at the right.

I have now checked LogUI’s compatibility with the first developer beta of Tahoe, and found and fixed one obscure bug in the Logarchive Tool before this new build. LogUI should now be fully compatible with macOS 14.6 and later, including Tahoe. It’s available now from here: [logui165](https://eclecticlight.co/wp-content/uploads/2025/06/logui165.zip)
and from [its Product Page](https://eclecticlight.co/consolation-t2m2-and-log-utilities/).

Enjoy!

### Share this:

* [Click to share on X (Opens in new window)
  X](https://eclecticlight.co/2025/06/11/logui-build-65-introduces-a-logarchive-tool/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://eclecticlight.co/2025/06/11/logui-build-65-introduces-a-logarchive-tool/?share=facebook)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://eclecticlight.co/2025/06/11/logui-build-65-introduces-a-logarchive-tool/?share=reddit)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://eclecticlight.co/2025/06/11/logui-build-65-introduces-a-logarchive-tool/?share=pinterest)
* [Click to share on Threads (Opens in new window)
  Threads](https://eclecticlight.co/2025/06/11/logui-build-65-introduces-a-logarchive-tool/?share=threads)
* [Click to share on Mastodon (Opens in new window)
  Mastodon](https://eclecticlight.co/2025/06/11/logui-build-65-introduces-a-logarchive-tool/?share=mastodon)
* [Click to share on Bluesky (Opens in new window)
  Bluesky](https://eclecticlight.co/2025/06/11/logui-build-65-introduces-a-logarchive-tool/?share=bluesky)
* Click to email a link to a friend (Opens in new window)
  Email
* [Click to print (Opens in new window)
  Print](https://eclecticlight.co/2025/06/11/logui-build-65-introduces-a-logarchive-tool/#print?share=print)

Like Loading...

### *Related*

Posted in [Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/), [Updates](https://eclecticlight.co/category/updates/) and tagged [log](https://eclecticlight.co/tag/log/), [logarchive](https://eclecticlight.co/tag/logarchive/), [LogUI](https://eclecticlight.co/tag/logui/), [macOS 26](https://eclecticlight.co/tag/macos-26/), [Tahoe](https://eclecticlight.co/tag/tahoe/), [Ulbow](https://eclecticlight.co/tag/ulbow/). Bookmark the [permalink](https://eclecticlight.co/2025/06/11/logui-build-65-introduces-a-logarchive-tool/).

## 5Comments

[Add yours](#reply-title)

1. 1
   ![Marc's avatar](https://2.gravatar.com/avatar/875b81dc5f354e367c50f6e23560b7627634c23e4cc556ad037b59f1ab2038ae?s=96&d=identicon&r=G)

   Marc
   [on June 11, 2025 at 8:13 pm](https://eclecticlight.co/2025/06/11/logui-build-65-introduces-a-logarchive-tool/#comment-106361)

   [Reply](https://eclecticlight.co/2025/06/11/logui-build-65-introduces-a-logarchive-tool/?replytocom=106361#respond)

   Thank you for all your efforts to understand and develop tools to make the unified log accessible and useful. I have almost never needed to delve into the log but I find these articles very interesting. Also, if I do need to access the log, I know the tools to get me starting.

   [Like](https://eclecticlight.co/2025/06/11/logui-build-65-introduces-a-logarchive-tool/?like_comment=106361&_wpnonce=ce3665c24b)Li...