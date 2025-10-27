---
title: Improving Native Message Host Reliability on Windows
url: https://textslashplain.com/2023/03/16/improving-native-message-host-reliability-on-windows/
source: text/plain
date: 2023-03-17
fetch_date: 2025-10-04T09:51:29.057604
---

# Improving Native Message Host Reliability on Windows

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Improving Native Message Host Reliability on Windows

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2023-03-162023-11-28](https://textslashplain.com/2023/03/16/improving-native-message-host-reliability-on-windows/)Posted in[browsers](https://textslashplain.com/category/browsers/), [dev](https://textslashplain.com/category/dev/), [web](https://textslashplain.com/category/tech/web/)Tags:[Chrome](https://textslashplain.com/tag/chrome/), [Chromium](https://textslashplain.com/tag/chromium/), [Edge](https://textslashplain.com/tag/edge/), [extensions](https://textslashplain.com/tag/extensions/), [NativeMessaging](https://textslashplain.com/tag/nativemessaging/)

*Last Update: Nov 28, 2023*

**Update**: This change was checked into Chromium 113 before being backed out. The plan is to [*eventually* turn it on-by-default](https://chromium-review.googlesource.com/c/chromium/src/%2B/4522048), so extension authors *really* should read this post and update their extensions if needed.

The feature was relanded inside Chrome Canary version **115.0.5789.0**. It’s off-by-default, behind a flag on the `chrome://flags#launch-windows-native-hosts-directly` page.

[![](https://textslashplain.com/wp-content/uploads/2023/05/image-13.png?w=720)](https://textslashplain.com/wp-content/uploads/2023/05/image-13.png)

In [Chrome 120.0.6090](https://chromiumdash.appspot.com/commits?commit=57c3662e332095c8e7d98255d86e29d3a86c530c&platform=Windows)+ and **Edge 120+**, [a Group Policy](https://chromium-review.googlesource.com/c/chromium/src/%2B/4918033) **`NativeHostsExecutablesLaunchDirectly`**  allows admins to turn this on for users in restricted environments (Cloud PCs that forbid `cmd.exe`, for example).

[![](https://textslashplain.com/wp-content/uploads/2023/10/image-33.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/10/image-33.png)

[![](https://textslashplain.com/wp-content/uploads/2023/11/image-21.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/11/image-21.png)

---

## Background

Previously, I’ve [written about Chromium’s Native Messaging](https://textslashplain.com/2020/09/04/web-to-app-communication-the-native-messaging-api/) functionality that allows a browser extension to talk to a process running outside of the browser’s sandbox, and I shared a [Native Messaging Debugger](https://textslashplain.com/2022/01/08/debug-native-messaging/) I wrote that allows you to monitor (and even tamper with) the communication channels between the browser extension and the Host App.

### Obscure Problems on Windows

Native Messaging is a powerful capability, and a common choice for building extensions that need to interact with the rest of the system. However, over the years, users have reported a trail of bugs related to how the feature is implemented on Windows. While these bugs are typically only seen in uncommon configurations, they could break Native Messaging entirely for some users.

Some examples include:

* [crbug/335558](https://bugs.chromium.org/p/chromium/issues/detail?id=335558) – Ampersand in Host’s path prevents launching (**Fixed in 118**)
* [crbug/387228](https://bugs.chromium.org/p/chromium/issues/detail?id=387228) – Broken if `%comspec%` not pointed at `cmd.exe`
* [crbug/387233](https://bugs.chromium.org/p/chromium/issues/detail?id=387233) – Broken when `cmd.exe` is disabled or set to `RUNASADMIN`

While the details of each of these issues differ, they all have the same root cause: On Windows, Chromium did not launch Native Message Hosts directly, instead launching `cmd.exe` (Windows’ console command prompt) and directing *it* to launch the target Host:

[![](https://textslashplain.com/wp-content/uploads/2023/03/image-20.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/03/image-20.png)

This approach provided two benefits: it enabled developers to implement Hosts using languages like Python, whose scripts are not *directly* executable in Windows, and it enabled support for Windows XP, where the APIs did not allow Chromium to easily set up the communication channel between the browser and the Native Host.

Unfortunately, the `cmd-in-the-middle` design meant that anything that prevented cmd.exe from running ([387233](https://bugs.chromium.org/p/chromium/issues/detail?id=387233), [387228](https://bugs.chromium.org/p/chromium/issues/detail?id=387228)) or that prevented *it* from starting the Host ([335558](https://bugs.chromium.org/p/chromium/issues/detail?id=335558)) would cause the flow to fail. While these configurations tend to be uncommon (which is why the problems have existed for ten years), they also tend to be very very hard to recognize/diagnose, and the impacted customers often have little recourse short of abandoning the extension platform.

### The Fix

So, over a few nights and weekends, I [landed](https://storage.googleapis.com/chromium-find-releases-static/b65.html#b65bc1b87d2e413d2638e94cf402adc385232228) [a changelist](https://chromium-review.googlesource.com/c/chromium/src/%2B/4307561/) in Chromium to improve this scenario for Chromium **`113.0.5656`** and later. This change means that Chrome, Edge (version `113.0.1769`+), and other Chromium-derived browsers will now *directly* invoke any Native Host that is a Windows Executable (`.exe`) rather than going through `cmd.exe` instead:

[![](https://textslashplain.com/wp-content/uploads/2023/03/image-19.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/03/image-19.png)

This change will reach the [Stable Channel](https://textslashplain.com/2022/08/04/understanding-browser-channels/) of Chrome and Edge (v113) in the last week of April 2023.

Native Hosts that are *not* implemented by executables (e.g. Python scripts or the like) will continue to use the old codepath.

I’ve got my fingers crossed that effectively no one even *notices* this change, with the exception of those unfortunate users who were encountering the old bugs who will now find that they can use previously-broken extensions.

However, this change also fixes two other bugs that were caused by the `cmd-in-the-middle` flow and those changes *could* cause problems if your Windows executable was not aware of the expected behavior for Native Hosts.

### (In)Visibility

When Chromium launches a native host, it sets a `start_hidden` flag to prevent any UI from popping up from the host. That flag prevents the proxy `cmd.exe`‘s UI window (`conhost.exe`) from appearing on the screen. This `start_hidden` flag means that console-based ([`subsystem:console`](https://learn.microsoft.com/en-us/cpp/build/reference/subsystem-specify-subsystem?view=msvc-170)) Windows applications remain invisible during native-messaging communications. However, the `start_hidden` flag *didn’t* flow through to non-console applications (e.g. `subsystem:Windows`), like my [Native Messaging Debugger application](https://textslashplain.com/2022/01/08/debug-native-messaging/), which is built atop C#’s WinForms and *meant* to be seen by the user.

***UPDATE:** In the new version of this change that is available in version 115+, the browser will now look at headers inside of the target EXE. If the executable targets `SUBSYSTEM:CONSOLE`, it will be hidden as described in this section. If it targets `SUBSYSTEM:WINDOWS` (indicating a GUI application), the `start_hidden` flag will be set to false.*

[![](https://textslashplain.com/wp-content/uploads/2023/05/image-14.png?w=782)](https://textslashplain.com/wp-content/uploads/2023/05/image-14.png)

*This compatibility accommodation will not resolve ALL problems, however. If you have a console app that occasionally shows a UI (e.g. a Windows certificate selection dialog box, for example) you will need to ensure that your app calls `ShowWindow()` explicitly.*

The new Direct Launch for Executables flow changes this– now Wind...