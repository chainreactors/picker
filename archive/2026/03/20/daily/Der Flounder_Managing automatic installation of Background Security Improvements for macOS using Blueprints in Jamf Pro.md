---
title: Managing automatic installation of Background Security Improvements for macOS using Blueprints in Jamf Pro
url: https://derflounder.wordpress.com/2026/03/20/managing-automatic-installation-of-background-security-improvements-for-macos-using-blueprints-in-jamf-pro/
source: Der Flounder
date: 2026-03-20
fetch_date: 2026-03-21T04:06:22.289242
---

# Managing automatic installation of Background Security Improvements for macOS using Blueprints in Jamf Pro

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro Blueprints](https://derflounder.wordpress.com/category/jamf-pro-blueprints/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Managing automatic installation of Background Security Improvements for macOS using Blueprints in Jamf Pro

## Managing automatic installation of Background Security Improvements for macOS using Blueprints in Jamf Pro

March 20, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

As a follow-up to my [previous post for managing Background Security Improvements (BSIs) using Jamf Pro’s Blueprints](https://derflounder.wordpress.com/2026/03/18/managing-background-security-improvements-for-macos-using-blueprints-in-jamf-pro/), it looks like I misunderstood what one of the management options was actually doing. As part of my prior post, I had said that in order to set this:

* **Background Security Improvements will be automatically installed**

You needed to do the following in the Blueprint’s **Software Update Settings** component:

1. Go to the **Background Security Improvements** section
2. Select the following options to apply the desired settings:

* **Background Security Improvements updates will be installed**:
  + Select **Allow** for Background Security Improvements installation

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-18-at-8.51-2.png?w=599&h=444 "Screenshot 2026-03-18 at 8.51.png")

That enables ***an*** installation option, but not the ***automatic*** installation option. For more details, please see below the jump.

What installation option is being enabled? As it turns out, what’s enabled is the logged-in user’s ability to manually select installing the BSI update. You can see this by setting the **Background Security Improvements installation** setting to **Allow**.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-18-at-8.51-3.png?w=599&h=444 "Screenshot 2026-03-18 at 8.51.png")

Once that’s been set and deployed to devices, look at **System Settings**: **Privacy & Security**: **Background Security Improvements** on a device that the setting has been deployed to. If there’s a BSI available to install, you’ll see it listed there along with an **Install** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-20-at-12.16.25pm.png?w=599&h=518 "Screenshot 2026-03-20 at 12.16.25 PM.png")

Next, let’s set **Background Security Improvements installation** to **Restrict** and deploy the settings to devices.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-20-at-3.02.png?w=599&h=452 "Screenshot 2026-03-20 at 3.02.png")

Now when we look at **System Settings**: **Privacy & Security**: **Background Security Improvements** on a managed device, that section and its **Install** button have disappeared.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-20-at-12.15.34pm.png?w=599&h=518 "Screenshot 2026-03-20 at 12.15.34 PM.png")

That means that the only install option available now is the automatic install option. Where’s that managed from? That is also managed in the **Software Update Settings** component, but in a different section. To set management for automatic installation of BSI updates:

1. Go to the **Install Actions** section
2. Select the following options to apply the desired settings:

* **Automatic installs of available security updates**:
  + Select **Always**

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-20-at-3.05.png?w=600&h=583 "Screenshot 2026-03-20 at 3.05.png")

When those settings are deployed to devices, you can go to **System Settings**: **Privacy & Security**: **Background Security Improvements** on a managed device and see that the **Automatically Install** setting is enabled and grayed out. There should also be a message that the setting is managed by your organization.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-20-at-12.30.51pm.png?w=599&h=518 "Screenshot 2026-03-20 at 12.30.51 PM.png")

You can also disable automatic installation of BSIs, but a very important thing to be aware of is that the **Automatic installs of available security updates** setting is managing [all background security updates for macOS](https://support.apple.com/101591), not only BSIs. This includes updates for Gatekeeper, XProtect and verifying the firmware that your Mac uses. Please keep that in mind if you want to disable automatic installs of BSIs.

If you’ve considered this information and still want to disable automatic installs of BSI updates, you can do so by using the following process:

1. Go to the **Install Actions** section
2. Select the following options to apply the desired settings:

* **Automatic installs of available security updates**:
  + Select **Never**

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-20-at-2.48.212-pm.png?w=600&h=585 "Screenshot 2026-03-20 at 2.48.212 PM.png")

When those settings are deployed to devices, you can go to **System Settings: Privacy & Security: Background Security Improvements** on a managed device and see that the **Automatically Install** setting is disabled and grayed out. There should also be a message that the setting is managed by your organization.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-20-at-2.47.28pm.png?w=599&h=518 "Screenshot 2026-03-20 at 2.47.28 PM.png")

### Share this:

* [Print (Opens in new window)
  Print](https://derflounder.wordpress.com/2026/03/20/managing-automatic-installation-of-background-security-improvements-for-macos-using-blueprints-in-jamf-pro/#print?share=print)
* Email a link to a friend (Opens in new window)
  Email
* More

* [Share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2026/03/20/managing-automatic-installation-of-background-security-improvements-for-macos-using-blueprints-in-jamf-pro/?share=facebook)
* [Share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2026/03/20/managing-automatic-installation-of-background-security-improvements-for-macos-using-blueprints-in-jamf-pro/?share=linkedin)
* [Share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2026/03/20/managing-automatic-installation-of-background-security-improvements-for-macos-using-blueprints-in-jamf-pro/?share=reddit)
* [Share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2026/03/20/managing-automatic-installation-of-background-security-improvements-for-macos-using-blueprints-in-jamf-pro/?share=twitter)
* [Share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2026/03/20/managing-automatic-installation-of-background-security-improvements-for-macos-using-blueprints-in-jamf-pro/?share=pinterest)
* [Share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2026/03/20/managing-automatic-installation-of-background-security-improvements-for-macos-using-blueprints-in-jamf-pro/?share=tumblr)

Like Loading...

### *Related*

Categories: [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jam...