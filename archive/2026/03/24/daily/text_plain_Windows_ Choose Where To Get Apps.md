---
title: Windows: Choose Where To Get Apps
url: https://textslashplain.com/2026/03/24/windows-choose-where-to-get-apps/
source: text/plain
date: 2026-03-24
fetch_date: 2026-03-25T04:16:12.372781
---

# Windows: Choose Where To Get Apps

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Windows: Choose Where To Get Apps

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2026-03-242026-03-24](https://textslashplain.com/2026/03/24/windows-choose-where-to-get-apps/)Posted in[security](https://textslashplain.com/category/security/)Tags:[MoTW](https://textslashplain.com/tag/motw/), [security](https://textslashplain.com/tag/security/), [SmartScreen](https://textslashplain.com/tag/smartscreen/), [Windows](https://textslashplain.com/tag/windows/)

Modern versions of Windows offer a setting named “Choose where to get apps” which can reduce attack surface by limiting the locations from which applications can be installed. *Internally, we’ve called this feature “Smart Install”*.

By default, this option is set to “**Anywhere**“, which means that Windows will allow an executable [downloaded from the Internet](https://textslashplain.com/2016/04/04/downloads-and-the-mark-of-the-web/) to run.

[![](https://textslashplain.com/wp-content/uploads/2026/03/image.png?w=695)](https://textslashplain.com/wp-content/uploads/2026/03/image.png)

Beyond the default, there are three other options.

[![](https://textslashplain.com/wp-content/uploads/2026/03/image-1.png?w=602)](https://textslashplain.com/wp-content/uploads/2026/03/image-1.png)

### Option: Let me know or Warn

The verbosely-named options:

* Anywhere, but let me know if there’s a comparable app in the Microsoft Store
* Anywhere, but warn me before installing an app that’s not from the Microsoft Store

…mean the SmartScreen Application Reputation call is sent specifying either `appControl/level=preferStore` (Warn) or `appControl/level=recommendations` (LMK) values:

[![](https://textslashplain.com/wp-content/uploads/2026/03/image-8.png?w=656)](https://textslashplain.com/wp-content/uploads/2026/03/image-8.png)

[![](https://textslashplain.com/wp-content/uploads/2026/03/image-11.png?w=606)](https://textslashplain.com/wp-content/uploads/2026/03/image-11.png)

After the AppRep call, a followup query is sent to a webservice (at `sfdataservice.microsoft.com/smartinstall`) to determine whether there’s a Store app available that might satisfy the user’s needs.

[![](https://textslashplain.com/wp-content/uploads/2026/03/image-9-1.png?w=1024)](https://textslashplain.com/wp-content/uploads/2026/03/image-9-1.png)

If the **Warn** option is selected, the user is shown a prompt regardless of whether a Store-hosted equivalent of the app is available:

[![](https://textslashplain.com/wp-content/uploads/2026/03/image-9-2.png?w=676)](https://textslashplain.com/wp-content/uploads/2026/03/image-9-2.png)

If the **Let me know** option is selected, a notice is shown *only* if a Store app is available. *Note: I don’t know how well this option works. The Microsoft Store is lacks the majority of apps. The only app I know that’s available via the Store and a traditional EXE download ([Paint.NET](https://www.getpaint.net/download.html#download)) does not result in Windows showing the Store suggestion.*

### Option: The Microsoft Store only

The simplest option is the “The Microsoft Store only” option. It means that after attempting to launch a downloaded app from Explorer, following the web service calls, Windows will show the following prompt:

[![](https://textslashplain.com/wp-content/uploads/2026/03/image-2.png?w=654)](https://textslashplain.com/wp-content/uploads/2026/03/image-2.png)

Attempting to run such a file by calling `ShellExecute` with [`SEE_MASK_FLAG_NO_UI`](https://learn.microsoft.com/en-us/windows/win32/api/shellapi/ns-shellapi-shellexecuteinfoa) results in a silent failure (no prompt); the function will return an error code of `ACCESS_DENIED`.

##### Surprise #1 – Plumbed into extra surfaces!

One *truly wild* aspect of this is that it means it behaves differently than most features powered by the [Mark of the Web](https://textslashplain.com/2016/04/04/downloads-and-the-mark-of-the-web/#:~:text=Launcher%20must%20participate).

When any option other than **Anywhere** is enabled, the [SmartScreen Application Reputation](https://textslashplain.com/2023/08/23/smartscreen-application-reputation-in-pictures/) service *can*1 be consulted **even when running a binary from the Command Prompt**:

[![](https://textslashplain.com/wp-content/uploads/2026/03/image-9.png?w=660)](https://textslashplain.com/wp-content/uploads/2026/03/image-9.png)

[![](https://textslashplain.com/wp-content/uploads/2026/03/image-10.png?w=685)](https://textslashplain.com/wp-content/uploads/2026/03/image-10.png)

…and if the execution is disallowed by the setting, execution can be blocked:

[![](https://textslashplain.com/wp-content/uploads/2026/03/image-4.png?w=346)](https://textslashplain.com/wp-content/uploads/2026/03/image-4.png)

When run from PowerShell, no UI is shown but the execution is blocked:

[![](https://textslashplain.com/wp-content/uploads/2026/03/image-5.png?w=814)](https://textslashplain.com/wp-content/uploads/2026/03/image-5.png)

##### Surprise #2 – Blocking Dangerous File types!

Another interesting surprise is the behavior in Windows when the filetype is a [“Dangerous” one](https://textslashplain.com/2023/04/05/file-types/#:~:text=inherently%20dangerous) but not an “App.” Those dangerous file types may be specified in the registry by an application’s developer, or manually using the `HighRiskFileTypes` registry key:

[![](https://textslashplain.com/wp-content/uploads/2026/03/image-12.png?w=661)](https://textslashplain.com/wp-content/uploads/2026/03/image-12.png)

Normally, attempting to use Explorer to open a downloaded file of a dangerous extension would result in a legacy Attachment Execution Services prompt like this:

[![](https://textslashplain.com/wp-content/uploads/2026/03/image-9-3.png?w=467)](https://textslashplain.com/wp-content/uploads/2026/03/image-9-3.png)

However, if Windows is configured to **Get Apps from** **Store Only**, the opening of an Internet Zone MotW-bearing file is **blocked silently**, providing a kludgy version of one of the most exciting aspects of [the Smart App Control feature](https://textslashplain.com/2016/04/04/downloads-and-the-mark-of-the-web/#:~:text=The%20current-,list%20of%20SAC%2Dblocked,-%2Dif%2DMotW%20extensions).

## Troubleshooting Smart Install UI

In some cases, users complain that this feature isn’t working as described above.

This can happen if the `Microsoft.StorePurchaseApp` is not installed, because that package contains the warning prompts.

Normally, running `Get-AppxPackage *purchase*` from PowerShell should show this:

[![](https://textslashplain.com/wp-content/uploads/2026/03/image-7.png?w=800)](https://textslashplain.com/wp-content/uploads/2026/03/image-7.png)

…but when the package isn’t installed, the command will return no packages.

[![](https://textslashplain.com/wp-content/uploads/2026/03/image-9-5.png?w=836)](https://textslashplain.com/wp-content/uploads/2026/03/image-9-5.png)

When the UI application is not installed, Windows falls back to showing the legacy (XP-era) Attachment Execution Services security prompts.

-Eric

PS: On subtle behavior is that the Microsoft offers “Portable Store Installer” executables to allow apps to “download” from websites (e.g. this [one for ClipChamp](https://apps.microsoft.com/detail/9p1j8s7ccwwt?hl=en-GB&gl=US)). Such PSI installers have an `Original filename` of `StoreInstaller.exe` and they are signed with a specific Microsoft certificate chain. The “Choose Where to Get Apps” feature recognizes these installers and allow-lists them as if they came from the store (because, *logically*, they do).

[![](https://textslashplain.com/wp-content/uploads/2026/03/image-9-6.png?w=398)](https://textslashplain.com/wp-content/uploads/2026/03/image-9-6.png)

[![](https://textslashplain.com/wp-content/uploads/2026/03/image-9-7.png?w=403)](https://textslashplain.com/wp-content/uplo...