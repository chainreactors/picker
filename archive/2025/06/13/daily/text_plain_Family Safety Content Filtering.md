---
title: Family Safety Content Filtering
url: https://textslashplain.com/2025/06/12/family-safety-content-filtering/
source: text/plain
date: 2025-06-13
fetch_date: 2025-10-06T22:53:30.215800
---

# Family Safety Content Filtering

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Family Safety Content Filtering

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2025-06-122025-06-25](https://textslashplain.com/2025/06/12/family-safety-content-filtering/)Posted in[browsers](https://textslashplain.com/category/browsers/), [web](https://textslashplain.com/category/tech/web/)Tags:[browsers](https://textslashplain.com/tag/browsers/), [bugs](https://textslashplain.com/tag/bugs/), [Chrome](https://textslashplain.com/tag/chrome/), [Edge](https://textslashplain.com/tag/edge/), [Windows](https://textslashplain.com/tag/windows/)

Microsoft Family Safety is a feature of Windows that allows parents to control their children’s access to apps and content in Windows. The feature is tied to the user accounts of the parent(s) and child(ren).

When I visit `https://family.microsoft.com` and log in with my personal Microsoft Account, I’m presented with the following view:

[![](https://textslashplain.com/wp-content/uploads/2025/06/image-2.png?w=1024)](https://textslashplain.com/wp-content/uploads/2025/06/image-2.png)

The “Nate” account is my 9yo’s account. Clicking it reviews a set of tabs which contain options about what parental controls to enable.

[![](https://textslashplain.com/wp-content/uploads/2025/06/image-17.png?w=844)](https://textslashplain.com/wp-content/uploads/2025/06/image-17.png)

Within the **Settings** link, there’s a simple dialog of options:

[![](https://textslashplain.com/wp-content/uploads/2025/06/image-16.png?w=750)](https://textslashplain.com/wp-content/uploads/2025/06/image-16.png)

Within the tabs of the main page, parents can set an overall screen time limit:

[![](https://textslashplain.com/wp-content/uploads/2025/06/image-11.png?w=955)](https://textslashplain.com/wp-content/uploads/2025/06/image-11.png)

Parents can configure which apps the child may use, how long they may use them:

[![](https://textslashplain.com/wp-content/uploads/2025/06/image-10.png?w=864)](https://textslashplain.com/wp-content/uploads/2025/06/image-10.png)

…and so on. Parents can also lock out a device for the remainder of the day:

[![](https://textslashplain.com/wp-content/uploads/2025/06/image-9.png?w=676)](https://textslashplain.com/wp-content/uploads/2025/06/image-9.png)

On the Edge tab, parents can enable `Filter inappropriate websites` to apply parental filtering inside the Edge browser.

[![](https://textslashplain.com/wp-content/uploads/2025/06/image-4.png?w=910)](https://textslashplain.com/wp-content/uploads/2025/06/image-4.png)

(Unlike Microsoft Defender for Endpoint’s [Web Content Filtering](https://textslashplain.com/2025/05/27/web-category-filtering/), there are no individual categories to choose from– it’s all-or-nothing).

As with [SmartScreen protection](https://textslashplain.com/2025/04/07/understanding-smartscreen-and-network-protection/), Family Safety filtering is integrated directly into the Microsoft Edge browser. If the user visits a prohibited site, the navigation is blocked and a permission screen is shown instead:

[![](https://textslashplain.com/wp-content/uploads/2025/06/image-12.png?w=607)](https://textslashplain.com/wp-content/uploads/2025/06/image-12.png)

If the parent responds to the request by allowing the site:

[![](https://textslashplain.com/wp-content/uploads/2025/06/image-13.png?w=813)](https://textslashplain.com/wp-content/uploads/2025/06/image-13.png)

…the child may revisit that site in the future.

### Blocking Third-Party Browsers

Importantly, Family Safety offers no filtering in third-party browsers (mostly because doing so is [very difficult](https://textslashplain.com/2023/10/04/security-tradeoffs-privacy/)), so **enabling Web Filtering will block third party browsers by default**.

The blocking of third-party browsers is done in a somewhat unusual way. The `Parental Controls` Windows service watches as new browser windows appear:

[![](https://textslashplain.com/wp-content/uploads/2025/06/image-6.png?w=712)](https://textslashplain.com/wp-content/uploads/2025/06/image-6.png)

…and if the process backing a window is that of a known browser (e.g. `chrome.exe`) the process is killed within a few hundred milliseconds (causing its windows to vanish).

After blocking, the child is then (intended to be) presented with the following dialog:

[![](https://textslashplain.com/wp-content/uploads/2025/06/image-7.png?w=650)](https://textslashplain.com/wp-content/uploads/2025/06/image-7.png)

If the child presses “Ask to use”, a request is sent to the Family Safety portal, and the child is shown the same dialog they would see if they tried to use an application longer than a time limit set by the parent:

[![](https://textslashplain.com/wp-content/uploads/2025/06/image-8.png?w=650)](https://textslashplain.com/wp-content/uploads/2025/06/image-8.png)

The parent(s) will receive an email:

[![](https://textslashplain.com/wp-content/uploads/2025/06/image-15.png?w=796)](https://textslashplain.com/wp-content/uploads/2025/06/image-15.png)

…and the portal gives the parent simple options to allow access:

[![](https://textslashplain.com/wp-content/uploads/2025/06/image-14.png?w=454)](https://textslashplain.com/wp-content/uploads/2025/06/image-14.png)

### Some Bugs

For a rather long time, there was a bug where Family Safety failed to correctly enforce the block on third party browsers. That bug was fixed in early June and blocking of third party browsers was restored. This led to some panicked posts in forums like Microsoft Support and Reddit complaining that something weird had happened.

In many cases, the problem was relatively mild (“*Hey, I didn’t change anything, but now I’m seeing this new permission prompt. What??”*) and could be easily fixed by the parent by either turning off Web Filtering or by allowing Chrome to run:

How Parents Can Adjust Settings:

Go to <https://familysafety.microsoft.com> or open the Family Safety mobile app.

1.      Select the child.

2.      To allow other browsers:

·         Disable **“Filter inappropriate websites”** under the **Edge** tab, or

·         Go to **Windows** tab → **Apps & Games** → unblock Chrome.

***Note that settings changes will take a minute or so to propagate to the client.***

*Pretty straightforward.*

What’s less straightforward, however, is that there currently exists a second bug: If **Activity reporting** is disabled on the Windows tab for the child account:

[![](https://textslashplain.com/wp-content/uploads/2025/06/image-5.png?w=647)](https://textslashplain.com/wp-content/uploads/2025/06/image-5.png)

…then **the browser window is blown away *without* showing the permission request prompt**:

This is obviously not good, especially in situations where users had been successfully using Chrome for months without any problem.

This issue has been [acknowledged by the Family Safety team](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fwindows%2Frelease-health%2Fstatus-windows-11-24h2%23350msgdesc&data=05%7C02%7CEric.Lawrence%40microsoft.com%7Cdaf5d9945d0f452f032108ddb3b4a40b%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C638864310714594519%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=WygZpSBnfgSKsvrm%2B9am0kaGXTVL5fj7yYplPkzGu0I%3D&reserved=0) who will build the fix. For now, parents can workaround the issue by either opting out of web filtering or helping their children use the supported browser instead.

-Eric

### Share this:

* [Click to share on X (Opens in new window)
  X](https://textslashplain.com/2025/06/12/family-safety-content-filtering/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://textslashplain.com/2025/06/12/family-safety-content-filtering/?share=facebook)

Like Loading...

Posted by[ericlaw](https://texts...