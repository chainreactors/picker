---
title: Checking APNS communication on macOS Tahoe
url: https://derflounder.wordpress.com/2026/08/29/checking-apns-communication-on-macos-tahoe/
source: Der Flounder
date: 2026-08-29
fetch_date: 2026-08-30T07:41:53.315763
---

# Checking APNS communication on macOS Tahoe

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Apple Push Notification Service](https://derflounder.wordpress.com/category/apple-push-notification-service/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Mobile Device Management](https://derflounder.wordpress.com/category/mobile-device-management/) > Checking APNS communication on macOS Tahoe

## Checking APNS communication on macOS Tahoe

August 29, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

I recently needed to determine whether communication between an MDM server and a managed Mac was working, entirely from the Mac’s side. I’ll skip to the end of the story for this particular quest for truth and knowledge:

I couldn’t. If someone else knows of a way, please let me know in the comments.

What I did figure out was that you could check to see if the Mac in question is communicating properly with APNS. That is possible and you can use the information logged to the unified system log to do so. For more details, please see below the jump.

First, let’s talk about how macOS gets MDM commands from an MDM server. It receives them through a push-notification mechanism rather than by polling the MDM server directly. The sequence looks like this:

1. The MDM server asks Apple’s [Push Notification Service](https://theapplewiki.com/wiki/Apple_Push_Notification_Service) (APNS) to send the target Mac a silent, background notification of push type **mdm** – a type reserved specifically for telling managed devices to contact their MDM server.

2. [apsd](https://www.manpagez.com/man/8/apsd/) (the Apple Push Notification Service daemon for macOS) receives that push notification over its persistent connection to Apple’s APNS infrastructure, then routes it to whichever process is registered for that push’s topic. For MDM, this is [mdmclient](https://www.manpagez.com/man/1/mdmclient/) (the MDM client for macOS), which is registered to receive push notifications which use one of the two following push notification topics:

* **com.apple.aps.mdmclient.agent.push.production**: This topic is for the MDM user channel
* **com.apple.aps.mdmclient.daemon.push.production**: This topic is for the MDM device channel.

3. The **mdmclient** process, having received the notification, contacts the MDM server directly over HTTPS to retrieve and process the relevant MDM command from the MDM server.

**Note:** *The push notification itself does not carry any commands. The notification is only a signal telling the Mac that something is waiting to be fetched from the MDM server.*

If step 1 or 2 fails, the Mac never learns an MDM command is waiting for it on the MDM server, even if the MDM server itself and the Mac’s MDM enrollment are otherwise working correctly. Because receiving an MDM command is a two-party event, this is why my original quest hit a dead end. A check run entirely from the device’s end cannot fully prove end-to-end command delivery works. The only way to prove it is for the MDM server to send an MDM command and the Mac then receive the command.

However, what can be verified entirely from the device’s end is whether the prerequisites for receiving an MDM command are in place:

1. The Mac has a connection to APNS which is working correctly.
2. Verifiable evidence that MDM push traffic specifically has been getting through to the Mac.

So while I can’t check if communication between an MDM server and a managed Mac is working, I can check that communication between the APNS service and a Mac is working. If APNS communication is not working, then I know for certain that communication between an MDM server and a managed Mac is also not working. Not exactly the result I wanted, but an acceptable substitute for most use cases.

How can I check whether APNS communication is working or not? As mentioned earlier, by using the Mac’s [unified logging system](https://education.apple.com/story/250014802). In this case, you can use the [log command line tool](https://www.manpagez.com/man/1/log/) with a [predicate](https://eclecticlight.co/2016/10/17/log-a-primer-on-predicates/) that looks for the logging produced by the Apple Push Notification service daemon’s **apsd** process or the macOS MDM agent’s **mdmclient** process. For example, if I wanted to check the logging for the past 24 hours, I would use the following command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/log show –predicate 'process == "apsd" OR process == "mdmclient"' –style compact –info –debug –last 24h |

[view raw](https://gist.github.com/rtrouton/7bed96a128ec228e05e8c1c7210c9461/raw/27bd1d97d424930b68054f061266c2815c880a44/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/7bed96a128ec228e05e8c1c7210c9461#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | –predicate 'process == "apsd" OR process == "mdmclient"' : Filters the unified log to only entries logged by the apsd (the Apple Push Notification service daemon) or mdmclient (the macOS MDM agent) processes. |
|  | –style compact : Keeps each log entry on one line, making it easier to search using command line tools like grep |
|  | –info –debug : Raises output verbosity so informational and debug-level messages (hidden by default) are included. |
|  | –last 24h : Limits the logging search to the previous 24 hours. |

[view raw](https://gist.github.com/rtrouton/48de60868e04d769e2fda45556fc8407/raw/df20bb61a71925f07816e8394aaf263f0c34bd3e/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/48de60868e04d769e2fda45556fc8407#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

Log patterns to watch for:

1. **Connected to courier** entries:

These log entries are written when the **apsd** process successfully establishes its persistent connection to one of Apple’s APNS courier servers.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | 2026-08-29 11:36:39.340 Df apsd[392:1224] [com.apple.apsd:courier] <APSCourierConnectionManager: 0x1036e3710; production>: Connected to courier 18-courier.push.apple.com (17.57.144.12) connection: <APSCourierConnection: 0x9451043c0> usingPackedFormat YES secureHandshakeEnabled YES onInterface: NonCellular |

[view raw](https://gist.github.com/rtrouton/39e5671595b6177948550fa77821c960/raw/c0dc897666e78745cd8512dd47ecf9bdd5730158/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/39e5671595b6177948550fa77821c960#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

These log entries appearing means that the Mac has a ...