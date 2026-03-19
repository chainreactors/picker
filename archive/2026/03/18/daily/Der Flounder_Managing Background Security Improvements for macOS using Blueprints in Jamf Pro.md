---
title: Managing Background Security Improvements for macOS using Blueprints in Jamf Pro
url: https://derflounder.wordpress.com/2026/03/18/managing-background-security-improvements-for-macos-using-blueprints-in-jamf-pro/
source: Der Flounder
date: 2026-03-18
fetch_date: 2026-03-19T04:19:14.575311
---

# Managing Background Security Improvements for macOS using Blueprints in Jamf Pro

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro Blueprints](https://derflounder.wordpress.com/category/jamf-pro-blueprints/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Managing Background Security Improvements for macOS using Blueprints in Jamf Pro

## Managing Background Security Improvements for macOS using Blueprints in Jamf Pro

March 18, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As part of Apple’s unveiling of Declarative Device Management (DDM) at WWDC 2023, Apple announced that DDM management included the ability to manage software updates. [Jamf Pro’s Blueprints](https://learn.jamf.com/en-US/bundle/jamf-pro-blueprints-configuration-guide/page/Jamf_Pro_Blueprints_Configuration_Guide.html) leverages this capability to support to support managing software updates, including [Background Security Improvements](https://support.apple.com/102657). Let’s see how this works using the following software update configuration as an example:

* Background Security Improvements will be automatically installed
* Background Security Improvements can be removed

For more details, please see below the jump.

As of Jamf Pro 11.25.2, there is not a Blueprints template available for creating blueprints which manage software update settings so the blueprint will need to be configured manually. To do this, use the following procedure:

1. Log into Jamf Pro.

2. Select Blueprints

3. Click the **Create blueprint** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-18-at-8.45.png?w=598&h=349 "Screenshot 2026-03-18 at 8.45.png")

4. You should see an unconfigured Blueprint. Click where it says **Untitled blueprint** and provide a name.

For this example, I’m using **Background Security Improvements Management Settings**.

5. Scroll down in the list on the left-hand side of the browser window to locate the **Software Update Settings** component.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-18-at-8.50.png?w=600&h=347 "Screenshot 2026-03-18 at 8.50.png")

6. Click on the **Software Update Settings** component and drag the **Software Update Settings** component to the **Components in this blueprint** section.

![Software update settings component click and drag.](https://derflounder.wordpress.com/wp-content/uploads/2026/03/software_update_settings_component_click_and_drag.gif?w=600&h=375 "software_update_settings_component_click_and_drag.gif")

7. Once added to the **Components in this blueprint** section, click anywhere on the **Software Update Settings** component to open it for editing.

8. At this point, you will see the software update management settings. From there, scroll down to the **Background Security Improvements** section and click the **Configure** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-18-at-8.51.png?w=599&h=398 "Screenshot 2026-03-18 at 8.51.png")

In the **Background Security Improvements** section, select the following options to apply the following desired settings:

* Background Security Improvements updates will be installed:

+ Select **Allow** for **Background Security Improvements installation**

* Background Security Improvements updates can be removed:

+ Select **Allow** for **Background Security Improvements removal**

Once all choices have been made and verified, click the **Update** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-18-at-8.51-1.png?w=600&h=398 "Screenshot 2026-03-18 at 8.51.png")

You should now see the following items set to **Enabled**:

* **Background Security Improvements installation**
* **Background Security Improvements removal**

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-18-at-8.54-1.png?w=600&h=398 "Screenshot 2026-03-18 at 8.54.png")

9. Once all the settings choices have been made and verified, click the **Save** changes button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-18-at-8.54.png?w=600&h=398 "Screenshot 2026-03-18 at 8.54.png")

10. At this point, you should have a blueprint which has all settings configured but where no target scope has been set. To scope this blueprint, go to the **Scope** section and click the arrow button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-18-at-8.56.png?w=599&h=345 "Screenshot 2026-03-18 at 8.56.png")

11. Select a Jamf Pro smart or static group. For this example, I’m selecting a static group named **Background Security Improvements Settings Deployment Group**.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-18-at-8.56-1.png?w=600&h=398 "Screenshot 2026-03-18 at 8.56.png")

12. Once everything has been configured, click the **Deploy** button to deploy the changes to the Macs you want to manage.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-18-at-8.57.png?w=600&h=348 "Screenshot 2026-03-18 at 8.57.png")

18. Once deployed, the Blueprints screen in Jamf Pro should show the newly-created **Background Security Improvements Management Settings** Blueprint as being deployed.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-18-at-8.58.png?w=599&h=345 "Screenshot 2026-03-18 at 8.58.png")

You can also check on the managed device’s end by opening **System Setting**s: **General**: **Device Management**, locating the MDM enrollment profile in the list of profiles and double-clicking on it.

When you scroll to the bottom of the enrollment profile’s window, you should see a **Device Declarations** section. If you’re deploying a software update configuration via Blueprints, you should see a **Software Update** listing for **Software Update Settings** in the **Device Declarations** section.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-18-at-9.00.18am.png?w=599&h=518 "Screenshot 2026-03-18 at 9.00.18 AM.png")

If you click on the **Software Update Settings** listing, you should see the details of what is being managed. In the case of our example where we are setting Background Security Improvements to be automatically installed and allowing the removal option, you should see the the following entries set to **On**:

* **Enable**
* **Enable Removal**

**![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-18-at-9.00.29am.png?w=599&h=518 "Screenshot 2026-03-18 at 9.00.29 AM.png")**

### Share this:

* [Print (Opens in new window)
  Print](https://derflounder.wordpress.com/2026/03/18/managing-background-security-improvements-for-macos-using-blueprints-in-jamf-pro/#print?share=print)
* Email a link to a friend (Opens in new window)
  Email
* More

* [Share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2026/03/18/managing-background-security-improvements-for-macos-using-blueprints-in-jamf-pro/?share=facebook)
* [Share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2026/03/18/managing-background-security-improvements-for-macos-using-blueprints-in-jamf-pro/?share=linkedin)
* [Share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2026/03/18/managing-background-security-improve...