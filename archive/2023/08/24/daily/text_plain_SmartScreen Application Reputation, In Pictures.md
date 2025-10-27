---
title: SmartScreen Application Reputation, In Pictures
url: https://textslashplain.com/2023/08/23/smartscreen-application-reputation-in-pictures/
source: text/plain
date: 2023-08-24
fetch_date: 2025-10-04T12:01:32.014678
---

# SmartScreen Application Reputation, In Pictures

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# SmartScreen Application Reputation, with Pictures

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2023-08-232025-09-03](https://textslashplain.com/2023/08/23/smartscreen-application-reputation-in-pictures/)Posted in[security](https://textslashplain.com/category/security/), [tech](https://textslashplain.com/category/tech/), [web](https://textslashplain.com/category/tech/web/)Tags:[Authenticode](https://textslashplain.com/tag/authenticode/), [browsers](https://textslashplain.com/tag/browsers/), [certificate](https://textslashplain.com/tag/certificate/), [Edge](https://textslashplain.com/tag/edge/), [MoTW](https://textslashplain.com/tag/motw/), [security](https://textslashplain.com/tag/security/), [SmartAppControl](https://textslashplain.com/tag/smartappcontrol/), [SmartScreen](https://textslashplain.com/tag/smartscreen/)

*Last Update: Sept 3, 2025*

I’ve previously explained how Chromium-based browsers [assign a “danger level”](https://textslashplain.com/2021/05/19/download-blocking-by-file-type/) based on the [type of the file](https://textslashplain.com/2023/04/05/file-types/), as determined from its extension. Depending on the Danger Level, the browser may warn the user before a file download begins in order to confirm that the user really wanted a potentially-dangerous file.

Deep in that article, I noted that Edge and Chrome can *override* the danger level for specific files based on the result of reputation checks against their respective security services (SmartScreen for Edge, SafeBrowsing for Chrome).

*Stated another way, reputation services don’t just block download of known-unsafe files, they also smooth the download flow for known-safe files.*

SmartScreen Application Reputation (AppRep) is a cloud service that maintains reputation information on billions of files in use around the world, and uses that reputation information to help keep users’ devices and personal information safe. It enhances the legacy [Windows Attachment Manager](https://support.microsoft.com/en-us/topic/information-about-the-attachment-manager-in-microsoft-windows-c48a4dcd-8de5-2af5-ee9b-cd795ae42738) security feature that shows warnings for dangerous files opened from the Internet.

To see what SmartScreen AppRep looks like, consider the case of downloading a trustworthy `.EXE` installer file (the Edge Canary setup program) in Edge with SmartScreen disabled and enabled.

#### Scenario: “Good” File

With **SmartScreen disabled**, we see a warning from the browser that the file *could harm your device*, because the `.exe` file type which has a danger level of `ALLOW_ON_USER_GESTURE` and I haven’t visited this download site before today1 in this browser profile:

[![](https://textslashplain.com/wp-content/uploads/2023/08/image-24.png?w=720)](https://textslashplain.com/wp-content/uploads/2023/08/image-24.png)

Danger Level: ALLOW\_ON\_USER\_GESTURE, not overridden

In contrast, if we **enable SmartScreen** and try again, this time, the new download `MicrosoftEdgeSetupCanary (5).exe` is **not interrupted** by a warning:

[![](https://textslashplain.com/wp-content/uploads/2023/08/image-25.png?w=721)](https://textslashplain.com/wp-content/uploads/2023/08/image-25.png)

Default Danger Level overridden to “Allow” by SmartScreen AppRep

The new download’s default danger level was overridden by the result of SmartScreen’s reputation check on the downloaded file’s signature and hash. The result indicated that this is a known-safe signer or file:

[![](https://textslashplain.com/wp-content/uploads/2023/08/image-26.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/08/image-26.png)

#### Scenario: “Bad” File

Now, consider the case the file is known to Microsoft to be malware. If SmartScreen isn’t enabled, there’s know way for Edge to know the file is bad, so users see the same security prompt as they saw for a “Good” file:

[![](https://textslashplain.com/wp-content/uploads/2024/02/image-21.png?w=724)](https://textslashplain.com/wp-content/uploads/2024/02/image-21.png)

On the other hand, if SmartScreen is enabled, AppRep reports the file is bad and the user gets a block notice in Edge.

[![](https://textslashplain.com/wp-content/uploads/2024/02/image-18.png?w=723)](https://textslashplain.com/wp-content/uploads/2024/02/image-18.png)

A user may choose to override the block by choosing **Keep** from the context menu:

[![](https://textslashplain.com/wp-content/uploads/2024/02/image-19.png?w=699)](https://textslashplain.com/wp-content/uploads/2024/02/image-19.png)

If the user chooses to Keep the file, an explanatory confirmation dialog is presented:

[![](https://textslashplain.com/wp-content/uploads/2024/02/image-20.png?w=726)](https://textslashplain.com/wp-content/uploads/2024/02/image-20.png)

#### Scenario: “Unknown”/”Uncommon” File

In some cases, SmartScreen doesn’t have enough information to know if a file is good or bad.

If SmartScreen is disabled in Edge, the user sees the same old dialog as they saw for “Good” and “Bad” files:

[![](https://textslashplain.com/wp-content/uploads/2024/02/image-22.png?w=724)](https://textslashplain.com/wp-content/uploads/2024/02/image-22.png)

However, if SmartScreen is enabled, the user sees a notice warning them that the file is uncommon

[![](https://textslashplain.com/wp-content/uploads/2024/02/image-23.png?w=725)](https://textslashplain.com/wp-content/uploads/2024/02/image-23.png)

The user may elect to keep the file:

[![](https://textslashplain.com/wp-content/uploads/2024/02/image-24.png?w=721)](https://textslashplain.com/wp-content/uploads/2024/02/image-24.png)

If the user chooses to Keep the file, an explanatory confirmation dialog is shown:

[![](https://textslashplain.com/wp-content/uploads/2024/02/image-25.png?w=698)](https://textslashplain.com/wp-content/uploads/2024/02/image-25.png)

---

### Windows Shell Integration

Beyond the integration into Edge, SmartScreen Application Reputation is also built into the Windows Shell. Even when you download an executable file using a non-Edge browser like Firefox or Chrome, the file is tagged with a [Mark-of-the-Web (MotW)](https://textslashplain.com/2016/04/04/downloads-and-the-mark-of-the-web/).

When a MotW-adorned file is executed via the `ShellExecute()` API, such as when the user double-clicks in Explorer or the browser’s download manager, the SmartScreen AppRep service evaluates the file if its [extension](https://textslashplain.com/2023/04/05/file-types/) is in the list of AppRep-supported file types (`.appref-ms .bat .cmd .com .cpl .dll .drv .exe .gadget .hta .js .jse .lnk .msi .msu .ocx .pif .ps1 .scr .sys .vb .vbe .vbs .vxd .website .wsf .docm)`.

If the file has a known “Good” reputation, no security prompt is shown. However, if it is malicious or unknown, a prompt will warn or block the file:

[![](https://textslashplain.com/wp-content/uploads/2024/02/image-9.png?w=1024)](https://textslashplain.com/wp-content/uploads/2024/02/image-9.png)

Prompt when AppRep service reported Unknown

[![](https://textslashplain.com/wp-content/uploads/2024/02/image-10.png?w=1024)](https://textslashplain.com/wp-content/uploads/2024/02/image-10.png)

Prompt when AppRep service reported Malware

In various cases, the legacy [Windows Attachment Execution Services](https://support.microsoft.com/en-us/topic/information-about-the-attachment-manager-in-microsoft-windows-c48a4dcd-8de5-2af5-ee9b-cd795ae42738) (AES) security prompt is shown instead:

[![](https://textslashplain.com/wp-content/uploads/2024/02/image-11.png?w=873)](https://textslashplain.com/wp-content/uploads/2024/02/image-11.png)

… if any of the following are true:

* If SmartScreen is disabled via the Windows Security toggle > Reputation-based Protection > `Check apps and files`
* If the file’s extension is [deemed `High Risk`](https://support.microsoft.com/en-us/...