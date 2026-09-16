---
title: Intel apps and macOS Golden Gate
url: https://derflounder.wordpress.com/2026/09/15/intel-apps-and-macos-golden-gate/
source: Der Flounder
date: 2026-09-15
fetch_date: 2026-09-16T06:58:15.370702
---

# Intel apps and macOS Golden Gate

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Rosetta 2](https://derflounder.wordpress.com/category/rosetta-2/) > Intel apps and macOS Golden Gate

## Intel apps and macOS Golden Gate

September 15, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

As part of Apple’s ongoing transition from Intel processor support, [Apple announced a transition timeline for macOS’s Rosetta 2 translation environment in 2026](https://developer.apple.com/documentation/apple-silicon/about-the-rosetta-translation-environment). At that time, Apple said that Rosetta 2 would continue in its current form for both macOS 26 and macOS 27. That means that macOS Golden Gate 27 is the last version of macOS which will offer Intel app support in its current form.

As part of that change, Apple has introduced new warnings for Intel apps in macOS Golden Gate. which specifically say they will not open in macOS 28. This is a change from previous warnings in macOS Tahoe which stated that they would not open in a future release of macOS.

![Rosetta awareness window.](https://derflounder.wordpress.com/wp-content/uploads/2026/09/rosetta_awareness_window.png?w=364&h=118 "rosetta_awareness_window.png")

For example, an earlier version of an Automator app I wrote named [Show or Hide Desktop Icons.app](https://github.com/rtrouton/Show-or-Hide-Desktop-Icons) is an Intel-based app. On macOS Golden Gate 27.0.0, launching this earlier version of the **Show or Hide Desktop Icons** app will periodically result in the following message being displayed by the OS.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/09/screenshot-2026-09-15-at-7.56.00am.png?w=362&h=124 "Screenshot 2026-09-15 at 7.56.00 AM.png")

These warnings also now appear in the **Get Info** window for Intel applications.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/09/screenshot-2026-09-15-at-7.45.07am.png?w=265&h=591 "Screenshot 2026-09-15 at 7.45.07 AM.png")

If installing Rosetta on macOS Golden Gate, this warning about Intel apps not opening on macOS 28 is likewise displayed as part of the Rosetta install prompt.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/09/screenshot-2026-09-15-at-7.44.22am.png?w=260&h=314 "Screenshot 2026-09-15 at 7.44.22 AM.png")

### Share this:

* [Print (Opens in new window)
  Print](https://derflounder.wordpress.com/2026/09/15/intel-apps-and-macos-golden-gate/#print?share=print)
* Email a link to a friend (Opens in new window)
  Email
* More

* [Share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2026/09/15/intel-apps-and-macos-golden-gate/?share=facebook)
* [Share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2026/09/15/intel-apps-and-macos-golden-gate/?share=linkedin)
* [Share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2026/09/15/intel-apps-and-macos-golden-gate/?share=reddit)
* [Share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2026/09/15/intel-apps-and-macos-golden-gate/?share=twitter)
* [Share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2026/09/15/intel-apps-and-macos-golden-gate/?share=pinterest)
* [Share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2026/09/15/intel-apps-and-macos-golden-gate/?share=tumblr)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Rosetta 2](https://derflounder.wordpress.com/category/rosetta-2/)

Comments (4)
[Leave a comment](#respond)

1. ![isotopp's avatar](https://2.gravatar.com/avatar/280d95c4350c4a5e7c4f2b0524a049f13728799be8a96511fe31b684c6b00308?s=32&d=identicon&r=G)

   isotopp

   September 15, 2026 at 3:24 pm

   [Reply](https://derflounder.wordpress.com/2026/09/15/intel-apps-and-macos-golden-gate/?replytocom=72940#respond)

   Why do you have to reinstall Rosetta2 with MacOS2?

   <https://developer.apple.com/documentation/apple-silicon/about-the-rosetta-translation-environment> says:

   macOS 27 directly integrates support for Intel binary translation, without needing to install Rosetta. This enables support for Intel Linux binaries running in ARM virtual machines (VMs) as well as Intel Linux containers. For more on information on Intel machine code translation and Linux VMs, see [Running Intel Binaries in Linux VMs](https://developer.apple.com/documentation/virtualization/running-intel-binaries-in-linux-vms).

   So Rosetta is not going away, quite the contrary – Apple absolutely requires it to run Docker images for Intel based Linux.
2. ![isotopp's avatar](https://2.gravatar.com/avatar/280d95c4350c4a5e7c4f2b0524a049f13728799be8a96511fe31b684c6b00308?s=32&d=identicon&r=G)

   isotopp

   September 15, 2026 at 3:24 pm

   [Reply](https://derflounder.wordpress.com/2026/09/15/intel-apps-and-macos-golden-gate/?replytocom=72941#respond)

   Why do you have to reinstall Rosetta2 with MacOS2?

   <https://developer.apple.com/documentation/apple-silicon/about-the-rosetta-translation-environment> says:

   macOS 27 directly integrates support for Intel binary translation, without needing to install Rosetta. This enables support for Intel Linux binaries running in ARM virtual machines (VMs) as well as Intel Linux containers. For more on information on Intel machine code translation and Linux VMs, see [Running Intel Binaries in Linux VMs](https://developer.apple.com/documentation/virtualization/running-intel-binaries-in-linux-vms).

   So Rosetta is not going away, quite the contrary – Apple absolutely requires it to run Docker images for Intel based Linux.
3. ![isotopp's avatar](https://2.gravatar.com/avatar/280d95c4350c4a5e7c4f2b0524a049f13728799be8a96511fe31b684c6b00308?s=32&d=identicon&r=G)

   isotopp

   September 15, 2026 at 3:24 pm

   [Reply](https://derflounder.wordpress.com/2026/09/15/intel-apps-and-macos-golden-gate/?replytocom=72943#respond)

   Why do you have to reinstall Rosetta2 with MacOS2?

   <https://developer.apple.com/documentation/apple-silicon/about-the-rosetta-translation-environment> says:

   macOS 27 directly integrates support for Intel binary translation, without needing to install Rosetta. This enables support for Intel Linux binaries running in ARM virtual machines (VMs) as well as Intel Linux containers. For more on information on Intel machine code translation and Linux VMs, see [Running Intel Binaries in Linux VMs](https://developer.apple.com/documentation/virtualization/running-intel-binaries-in-linux-vms).

   So Rosetta is not going away, quite the contrary – Apple absolutely requires it to run Docker images for Intel based Linux.
4. ![isotopp's avatar](https://2.gravatar.com/avatar/280d95c4350c4a5e7c4f2b0524a049f13728799be8a96511fe31b684c6b00308?s=32&d=identicon&r=G)

   isotopp

   September 15, 2026 at 3:24 pm

   [Reply](https://derflounder.wordpress.com/2026/09/15/intel-apps-and-macos-golden-gate/?replytocom=72946#respond)

   Why do you have to reinstall Rosetta2 with MacOS2?

   <https://developer.apple.com/documentation/apple-silicon/about-the-rosetta-translation-environment> says:

   macOS 27 directly integrates support for Intel binary translation, without needing to install Rosetta. This enables support for Intel Linux binaries running in ARM virtual machines (VMs) as well as Intel Linux containers. For more on information on Intel machine code translatio...