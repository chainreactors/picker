---
title: Deploying Apple software update deferrals using Blueprints in Jamf Pro
url: https://derflounder.wordpress.com/2026/01/26/deploying-apple-software-update-deferrals-using-blueprints-in-jamf-pro/
source: Der Flounder
date: 2026-01-26
fetch_date: 2026-01-27T03:36:49.926175
---

# Deploying Apple software update deferrals using Blueprints in Jamf Pro

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro Blueprints](https://derflounder.wordpress.com/category/jamf-pro-blueprints/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Deploying Apple software update deferrals using Blueprints in Jamf Pro

## Deploying Apple software update deferrals using Blueprints in Jamf Pro

January 26, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As part of the software testing cycle, Mac admins may choose to delay making Apple’s macOS updates generally available to their fleet while they’re testing to make sure all the software used on their organization’s Macs works correctly on new versions of macOS. To assist with this, [Apple has made available deferral settings for Apple’s Software Update](https://support.apple.com/guide/deployment/software-update-settings-declarative-dep0578d8b8a/web) on macOS, where you can choose to defer the following for up to 90 days:

* Major OS upgrades: An upgrade is a major macOS release with a new name (for example, macOS Sequoia 15 to macOS Tahoe 26).
* Minor OS updates: An update is a minor release within the same macOS version, such as Tahoe 26.0 to 26.2.
* Non-OS updates: These are software updates provided by Apple that are not covered by the prior two categories.

For those who need to know when deferral periods end, Apple has them available for the current shipping OS via the link below:

<https://support.apple.com/guide/deployment/about-software-updates-depc4c80847a/web> (see the **Software release dates** section.)

One example of a deferral choice is delaying the release of a new major version of macOS. In this scenario, a Mac admin may want to delay release because mandatory security software for their environment has not yet been certified by the software vendor as being compatible with the new version of macOS. You can use [Blueprints in Jamf Pro](https://learn.jamf.com/en-US/bundle/jamf-pro-blueprints-configuration-guide/page/Jamf_Pro_Blueprints_Configuration_Guide.html) to distribute these tokens, using the **Software Update Settings** component in Blueprints.

Let’s take a look on how to deploy deferral settings using using the following software update configuration as an example:

* What’s deferred: Major OS upgrades
* How long: 90 days

For more details, please see below the jump.

As of Jamf Pro 11.24.0, there is not a Blueprints template available for creating blueprints which manage software update settings so the blueprint will need to be configured manually. To do this, use the following procedure:

1. Log into Jamf Pro.

2. Select Blueprints

3. Click the **Create blueprint** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-26-at-11.17.23-am.png?w=595 "Screenshot 2026-01-26 at 11.17.23 AM.png")

4. You should see an unconfigured Blueprint. Click where it says Untitled blueprint and provide a name.

For this example, I’m using **Apple 90 Day Deferral**.

5. Scroll down in the list on the left-hand side of the browser window to locate the **Software Update Settings** component.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-26-at-11.18.png?w=595 "Screenshot 2026-01-26 at 11.18.png")

6. Click on the Software Update Settings component and drag the **Software Update Settings** component to the **Declaration group** section.

![Drag software update settings component.](https://derflounder.wordpress.com/wp-content/uploads/2026/01/drag_software_update_settings_component-1.gif?w=595 "drag_software_update_settings_component.gif")

7. Once added to the Declaration group section, click anywhere on the Software Update Settings component to open it for editing.

8. At this point, you will see all available Software Update settings which are available for all Apple platforms. To apply the desired deferral settings, select the following option:

**Deferrals**

Click the associated **Configure** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-26-at-11.26.png?w=595 "Screenshot 2026-01-26 at 11.26.png")

Check the checkbox for **Number of days to defer a major macOS software update**.
Enter the following value in the entry blank:

**90**

This will configure major OS upgrades to be deferred for the maximum amount of time, which is 90 days following the release of the major OS upgrade.

Once all choices have been made and verified, click the **Update** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-26-at-11.27.png?w=595 "Screenshot 2026-01-26 at 11.27.png")

9. Once all the settings choices have been made and verified, click the **Save** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-26-at-11.27-1.png?w=595 "Screenshot 2026-01-26 at 11.27.png")

10. At this point, you should have a blueprint which has all settings configured but where no target scope has been set. To scope this blueprint, go to the **Scope** section and click the arrow button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-26-at-11.28.png?w=595 "Screenshot 2026-01-26 at 11.28.png")

For this example, I’m selecting a static group named **macOS 90 Day Deferral Group**. Once the desired smart and/or static groups have been set and verified for the scope, click the **Save** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-26-at-11.29.png?w=595 "Screenshot 2026-01-26 at 11.29.png")

11. Once everything has been configured, click the **Deploy** button to deploy the changes to the Macs you want to manage.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-26-at-11.29-1.png?w=595 "Screenshot 2026-01-26 at 11.29.png")

12. Once deployed, the Blueprints screen in Jamf Pro should show the newly-created **Apple 90 Day Deferral** Blueprint as being deployed.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-26-at-11.30.png?w=595 "Screenshot 2026-01-26 at 11.30.png")

You can also check on the managed device’s end by opening **System Settings**: **General**: **Device Management**, locating the MDM enrollment profile in the list of profiles and double-clicking on it. When you scroll to the bottom of the enrollment profile’s window, you should see a **Device Declarations** section.

If you’re deploying a software update configuration via Blueprints, you should see a **Software Update Settings** listing for **Software Update** in the **Device Declarations** section.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-26-at-11.32.03am.png?w=595 "Screenshot 2026-01-26 at 11.32.03 AM.png")

If you click on the **Software Update Settings** listing, it should report the following:

* **Major period: 90**

**![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-26-at-11.32.20am.png?w=595 "Screenshot 2026-01-26 at 11.32.20 AM.png")**

### Share this:

* [Print (Opens in new window)
  Print](https://derflounder.wordpress.com/2026/01/26/deploying-apple-software-update-deferrals-using-blueprints-in-jamf-pro/#print?share=print)
* Email a link to a friend (Opens in new window)
  Email
* More

* [Share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2026/01/26/deploying-apple-software-update-deferrals-using-blueprints-in-jamf-pro/?share=facebook)
* [...