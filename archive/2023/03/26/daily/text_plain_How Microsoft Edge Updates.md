---
title: How Microsoft Edge Updates
url: https://textslashplain.com/2023/03/25/how-microsoft-edge-updates/
source: text/plain
date: 2023-03-26
fetch_date: 2025-10-04T10:43:46.335486
---

# How Microsoft Edge Updates

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# How Microsoft Edge Updates

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2023-03-252025-04-08](https://textslashplain.com/2023/03/25/how-microsoft-edge-updates/)Posted in[browsers](https://textslashplain.com/category/browsers/), [dev](https://textslashplain.com/category/dev/), [web](https://textslashplain.com/category/tech/web/)

By default, Edge will update in the background automatically while you’re not using it. Open Microsoft Edge and you’ll be using the latest version.

However, if Edge is already running and an update becomes available, an **update notifier** icon will show in the Edge toolbar. When you see the update notifier (a green or red arrow on the … button):

[![](https://textslashplain.com/wp-content/uploads/2023/03/image-49.png?w=632)](https://textslashplain.com/wp-content/uploads/2023/03/image-49.png)

… this means an update is ready for use and you simply need to restart the browser to have it applied.

While you’re in this state, if you open Edge’s application folder, you’ll see the new version sitting side-by-side with the currently-running version:

[![](https://textslashplain.com/wp-content/uploads/2023/03/image-50.png?w=986)](https://textslashplain.com/wp-content/uploads/2023/03/image-50.png)

When you choose to restart:

[![](https://textslashplain.com/wp-content/uploads/2023/03/image-51.png?w=895)](https://textslashplain.com/wp-content/uploads/2023/03/image-51.png)

…either via the prompt or manually, Edge will [rename and restart](https://source.chromium.org/chromium/chromium/src/%2B/main%3Achrome/browser/first_run/upgrade_util_win.cc;l=157) with the new binaries and remove the old ones:

[![](https://textslashplain.com/wp-content/uploads/2023/03/image-52.png?w=854)](https://textslashplain.com/wp-content/uploads/2023/03/image-52.png)

In addition to cleaning up the old binaries, the newly-started Edge instance verifies if any data migration needs to take place (e.g. if the user profile database structure has been changed) and performs that migration.

The new instance restarts using Chromium’s [session restoration](https://textslashplain.com/2019/06/24/surprise-undead-session-cookies/) feature, so all of your tabs, windows, cookies, etc, are right where you left them before the update (akin to typing `edge://restart` in the omnibox).

This design means that the new version is ready to go immediately, without the need to wait for any downloads or other steps that could take a while or go wrong along the way. This is important, because **users who don’t restart the browser will continue running the outdated version** (even for new tabs or windows) until they restart, and this could expose them to security vulnerabilities. **Security Tip: If your see the update notification, you should restart as soon as possible!**

[Three](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-policies#relaunchwindow) [Group](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-policies#relaunchnotification) [Policies](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-policies#relaunchnotificationperiod) give administrators control of the relaunch process, including the ability to force a restart.

### Threat Management / Software Inventory

Unfortunately, this design can cause some confusion for Enterprise Software Inventory / Threat Management products, because they will typically check the version of the current `msedge.exe` file on disk. That version may be outdated pending the relaunch of the browser, which will perform the replacement process.

For example, if the `msedge.exe` is on version `119.0.2112.0`, but version `119.0.2213.0` is currently staged as `new_msedge.exe`, your Software Inventory tool might complain that the user has an outdated version of Edge until the user launches the browser.

### Manually vs. Automatic Update Check

Users can trigger a check for updates by clicking **…** > **Help & Feedback** > **About Microsoft Edge** or navigating to `edge://settings/help`.

If that doesn’t work (e.g. because Edge crashes before navigating anywhere) fear not — **Edge’s Update Service** will install a new release within a few hours of it becoming available. If you’d like to speed it along, you can ask the Updater to update Edge Canary thusly:

`"C:\Program Files (x86)\Microsoft\EdgeUpdate\MicrosoftEdgeUpdate.exe" "/silent /install appguid={65C35B14-6C1D-4122-AC46-7148CC9D6497}&appname=Microsoft%20Edge%20Canary&needsadmin=False"`

If you instead wanted to update Stable, the command line would be

`C:\Program Files (x86)\Microsoft\EdgeUpdate\MicrosoftEdgeUpdate.exe" -argumentlist "/silent /install appguid={56EB18F8-B008-4CBD-B6D2-8C97FE7E9062}&appname=Microsoft%20Edge&needsadmin=True"`

## Beware Fake Updates from websites

If a website claims that you need to install a browser update to continue, **don’t do it**, [it’s a scam](https://twitter.com/ericlaw/status/1729914165328785711)! Websites sometimes are compromised by malicious ads pretending to be a browser update, in the hopes that you’ll download and run their malicious software. Edge (and Chrome) never distribute updates in this way.

[![](https://textslashplain.com/wp-content/uploads/2023/12/image-6.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/12/image-6.png)

Screenshot of a SCAM site that attempts to trick the user into installing malware

-Eric

#### Technical Appendix

Chromium’s code for renaming the `new_browser.exe` binary can be seen [here](https://source.chromium.org/chromium/chromium/src/%2B/main%3Achrome/browser/first_run/upgrade_util_win.cc;l=157). When Chrome is installed at the machine-wide level, Chromium’s `setup.exe` is passed the `--rename-chrome-exe` command line switch, and its [code](https://source.chromium.org/chromium/chromium/src/%2B/main%3Achrome/installer/setup/setup_main.cc;l=535;drc=8101d6d81854e4f437e0f03f77694a01aaa8df7a) performs the actual rename.

[![](https://textslashplain.com/wp-content/uploads/2023/03/image-53.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/03/image-53.png)

Edge’s background updater uses a variety of approaches to ensure that it’s available to install a new version upon release:

[![](https://textslashplain.com/wp-content/uploads/2023/12/image-10.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/12/image-10.png)
[![](https://textslashplain.com/wp-content/uploads/2023/12/image-11.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/12/image-11.png)

### Share this:

* [Click to share on X (Opens in new window)
  X](https://textslashplain.com/2023/03/25/how-microsoft-edge-updates/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://textslashplain.com/2023/03/25/how-microsoft-edge-updates/?share=facebook)

Like Loading...

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2023-03-252025-04-08](https://textslashplain.com/2023/03/25/how-microsoft-edge-updates/)Posted in[browsers](https://textslashplain.com/category/browsers/), [dev](https://textslashplain.com/category/dev/), [web](https://textslashplain.com/category/tech/web/)

## Published by ericlaw

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity. [View more posts](https://textslashplain.com/author/ericlaw1979/)

## Post navigation

[Previous Post Previous post:](https://textslashplain.com/2023/03/22/attack-techniques-spoofing-via-userinfo/)

[Next Post Next post:](https://textslashplain.com/2023/04/05/file-types/)

## 4 thoughts on “How Microsoft Edge Updates”

1. ![larrylaca's avatar](https://2.gravatar.com/avatar/e7bb4cb7b73bbc1a4b781fe8df6a25664ec73b705cf5364fc3681416754694b0?s=32&d=identicon&r=G)...