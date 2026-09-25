---
title: App Settings declarative management may block unsigned apps on macOS Golden Gate
url: https://derflounder.wordpress.com/2026/09/24/app-settings-declarative-management-may-block-unsigned-apps-on-macos-golden-gate/
source: Der Flounder
date: 2026-09-24
fetch_date: 2026-09-25T06:51:54.161983
---

# App Settings declarative management may block unsigned apps on macOS Golden Gate

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [macOS](https://derflounder.wordpress.com/category/macos/) > App Settings declarative management may block unsigned apps on macOS Golden Gate

## App Settings declarative management may block unsigned apps on macOS Golden Gate

September 24, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

One of the new management options available for Apple devices running OS 27 is the [App Settings declaration](https://support.apple.com/en-lb/guide/deployment/depd65c456fa/web). This new declaration provides the ability to control the following:

* Allowing only specified apps and binaries to run.
* Preventing specified apps and binaries from running.
* Setting default privacy permissions for specified apps.

When creating an App Settings configuration to allow or deny specified apps or binaries, there is something to keep in mind. The current way App Settings works is the following:

* No allow or deny policy: All apps and binaries (signed and unsigned) are allowed to run.
* Any allow or deny policy: All unsigned apps and binaries are blocked, even if the configuration isn’t specifying any apps or binaries to allow or deny.

For more details, please see below the jump.

[Apple has this behavior documented](https://support.apple.com/en-lb/guide/deployment/dep001044b08/web) with the following description of the workflow:

1. ***If the device has no policy applied, the Endpoint Security client isn’t running and doesn’t restrict binaries from running. Otherwise, the Endpoint Security client reads the binary’s identifying attributes.***
2. ***The Endpoint Security client denies unsigned, ad hoc-signed, and development-signed binaries even if the configuration only provides an empty allow or deny list.***
3. ***The Endpoint Security client applies the core policy. Protected binaries and protected locations decide the outcome, unless the core policy marks the binary as deferred. In that case the configured policy overrides the decision.***
4. ***The Endpoint Security client consults the rule set provided by the configuration. A match against the deny list results in a deny decision. A match against the allow list results in an allow decision.***
5. ***If no rule matches, the Endpoint Security client applies the default behavior for the configured mode. In allow mode, the Endpoint Security client denies the binary. In deny mode, the Endpoint Security client allows the binary.***

***![](https://derflounder.wordpress.com/wp-content/uploads/2026/09/screenshot-2026-09-24-at-10.38.png?w=595 "Screenshot 2026-09-24 at 10.38.png")***

The workflow looks like this:

![Policy flowchart.](https://derflounder.wordpress.com/wp-content/uploads/2026/09/policy_flowchart.png?w=595 "policy_flowchart.png")

What this means is that when you set any policy for allowing or denying apps and binaries, any apps or binaries which are not signed by either a [Developer ID (Application) code signing certificate](https://developer.apple.com/help/account/certificates/create-developer-id-certificates/) or a code signing certificate owned by Apple get blocked automatically as part of Step #2 of the workflow.

Where this behavior may show up are with apps and binaries provided by solutions like [Homebrew](https://brew.sh/) or [MacPorts](https://www.macports.org/), where apps and binaries may be compiled from source code and not code signed.

In a situation like this, where there is an App Settings declaration applied to the Mac which has a configured allow or deny list (even when the allow and/or deny list is empty), apps and binaries which don’t have Developer ID or Apple code signing will be automatically blocked and not allowed to run.

As of this time, it appears the only way to allow apps or binaries in that situation would be to code sign the apps or binaries using a **Developer ID (Application)** or Apple-owned code signing certificate.

### Share this:

* [Print (Opens in new window)
  Print](https://derflounder.wordpress.com/2026/09/24/app-settings-declarative-management-may-block-unsigned-apps-on-macos-golden-gate/#print?share=print)
* Email a link to a friend (Opens in new window)
  Email
* More

* [Share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2026/09/24/app-settings-declarative-management-may-block-unsigned-apps-on-macos-golden-gate/?share=facebook)
* [Share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2026/09/24/app-settings-declarative-management-may-block-unsigned-apps-on-macos-golden-gate/?share=linkedin)
* [Share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2026/09/24/app-settings-declarative-management-may-block-unsigned-apps-on-macos-golden-gate/?share=reddit)
* [Share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2026/09/24/app-settings-declarative-management-may-block-unsigned-apps-on-macos-golden-gate/?share=twitter)
* [Share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2026/09/24/app-settings-declarative-management-may-block-unsigned-apps-on-macos-golden-gate/?share=pinterest)
* [Share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2026/09/24/app-settings-declarative-management-may-block-unsigned-apps-on-macos-golden-gate/?share=tumblr)

Like Loading...

### *Related*

Categories: [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [macOS](https://derflounder.wordpress.com/category/macos/)

Comments (0)
[Leave a comment](#respond)

1. No comments yet.

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2026/09/24/app-settings-declarative-management-may-block-unsigned-apps-on-macos-golden-gate/#respond)

Δ

[Enrolling macOS Golden Gate 27.0.0 virtual machines with MDM servers does not work correctly](https://derflounder.wordpress.com/2026/09/15/enrolling-macos-golden-gate-27-0-0-virtual-machines-with-mdm-servers-does-not-work-correctly/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.wordpress.com/feed/ "Subscribe with Google")
* [Youdao](http://reader.youdao.com/#url=https://derflounder.wordpress.com/feed/ "Subscribe with Youdao")
* [Xian Guo](http://www.xianguo.com/subscribe.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Xian Guo")
* [Zhua Xia](http://www.zhuaxia.com/add_channel.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Zhua Xia")
* [My Yahoo!](http://add.my.yahoo.com/rss?url=https://derflounder.wordpress.com/feed/ "Subscribe with My Yahoo!")
* [newsgator](http://www.newsgator.com/ngs/subscriber/subfext.aspx?url=https://derflounder.wordpress.com/feed/ "Subscribe with newsgator")
* [Bloglines](http://www.bloglines.com/sub/https%3A//derflounder.wordpress.com/feed/ "Subscribe with Bloglines")
* [iNezha](http://inezha.com/add?url=https://derflounder.wordpress.com/feed/ "Subscribe with iNezha")

September 2026

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | 1 | 2 | 3 | 4 | 5 | 6 |
| 7 | [8](https://derflounder.wordpress.com/2026/09/08/) | 9 | 10 | 11 | 12 | 13 |
| [14](https://derflounder.wordpress.com/2026/09/14/) | [15](https://derflounder.wordpress.com/2026/09/15/) | 16 | 17 | 18 | 19 | 20 |
| 21 | 22 | 23 | [24](https://derflounder.wordpress.com/2026/09/24/) | 25 | 26 | 27 |
| 28 | 29 | 30 |  | | | |

[« Aug](https://derflounder.wordpress.com/2026/08/)

### Rece...