---
title: Deploying Apple beta program tokens using Blueprints in Jamf Pro
url: https://derflounder.wordpress.com/2026/01/07/deploying-apple-beta-program-tokens-using-blueprints-in-jamf-pro/
source: Der Flounder
date: 2026-01-07
fetch_date: 2026-01-08T03:29:12.725170
---

# Deploying Apple beta program tokens using Blueprints in Jamf Pro

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Apple Beta Programs](https://derflounder.wordpress.com/category/apple-beta-programs/), [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro Blueprints](https://derflounder.wordpress.com/category/jamf-pro-blueprints/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Deploying Apple beta program tokens using Blueprints in Jamf Pro

## Deploying Apple beta program tokens using Blueprints in Jamf Pro

January 7, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As discussed in [a previous post,](https://derflounder.wordpress.com/2026/01/06/obtaining-apple-beta-program-tokens/) Apple provides tokens which allow devices to be enrolled in Apple’s beta programs without the need for the user to sign in with an Apple Account on the device.

You can use [Blueprints in Jamf Pro](https://learn.jamf.com/en-US/bundle/jamf-pro-blueprints-configuration-guide/page/Jamf_Pro_Blueprints_Configuration_Guide.html) to distribute these tokens, using the **Software Update Settings** component in Blueprints. Let’s see how this works using the following software update configuration as an example:

* Macs are enrolled in the macOS Tahoe beta program.
* Macs cannot opt out of participating in the macOS Tahoe beta program.

For more details, please see below the jump.

**Pre-requisites:**

* [Token for the Apple macOS Tahoe beta program](https://derflounder.wordpress.com/2026/01/06/obtaining-apple-beta-program-tokens/)

As of Jamf Pro 11.23.1, there is not a Blueprints template available for creating blueprints which manage software updates so the blueprint will need to be configured manually. To do this, use the following procedure:

1. Log into Jamf Pro.

2. Select Blueprints

3. Click the **Create blueprint** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-07-at-9.26.png?w=595 "Screenshot 2026-01-07 at 9.26.png")

4. You should see an unconfigured Blueprint. Click where it says **Untitled blueprint** and provide a name.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-07-at-9.26-1.png?w=595 "Screenshot 2026-01-07 at 9.26.png")

For this example, I’m using **Apple Beta Tokens**.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-07-at-9.27.png?w=595 "Screenshot 2026-01-07 at 9.27.png")

5. Scroll down in the list on the left-hand side of the browser window to locate the **Software Update Settings** component.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-07-at-9.28.png?w=595 "Screenshot 2026-01-07 at 9.28.png")

6. Click on the **Software Update Settings** component and drag the **Software Update Settings** component to the **Declaration group** section.

![Drag software update settings component.](https://derflounder.wordpress.com/wp-content/uploads/2026/01/drag_software_update_settings_component.gif?w=595 "drag_software_update_settings_component.gif")

7. Once added to the **Declaration group** section, click anywhere on the **Software Update Settings** component to open it for editing.

8. At this point, you will see all available Software Update settings which are available for all Apple platforms. To apply the desired beta program settings, select the following option:

**Beta Updates**

Click the associated **Configure** button.

In the **Program enrollment** section, select the following:

* Check the checkbox for **Program enrollment**
* Select the **Always** option

Once the **Always** option is selected, two additional options should appear:

* **Require program**
* **Offer programs**

Select the **Require program** option.

Once the **Require program** option has been selected, a new set of entry blanks should appear:

* **Apple Business Manager or Apple School Manager beta enrollment token**
* **Description**

For the **Apple Business Manager or Apple School Manager beta enrollment token** entry, enter the token for the macOS Tahoe beta program.

For the **Description** entry, enter whatever you want in plain text. For this example, I’m entering the following text:

**macOS Tahoe beta program**

Once all choices have been made and verified, click the **Update** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-07-at-9.46.png?w=595 "Screenshot 2026-01-07 at 9.46.png")

9. Once all the settings choices have been made and verified, click the **Save** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-07-at-9.49.png?w=595 "Screenshot 2026-01-07 at 9.49.png")

10. At this point, you should have a blueprint which has all settings configured but where no target scope has been set. To scope this blueprint, go to the **Scope** section and click the arrow button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-07-at-9.51.png?w=595 "Screenshot 2026-01-07 at 9.51.png")

For this example, I’m selecting a static group named **Beta Software Deployment Group**. Once the desired smart and/or static groups have been set and verified for the scope, click the **Save** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-07-at-9.51-1.png?w=595 "Screenshot 2026-01-07 at 9.51.png")

11. Once everything has been configured, click the **Deploy** button to deploy the changes to the Macs you want to manage.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-07-at-9.53.png?w=595 "Screenshot 2026-01-07 at 9.53.png")

12. Once deployed, the Blueprints screen in Jamf Pro should show the newly-created **Apple Beta Tokens** Blueprint as being deployed.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-07-at-9.54.png?w=595 "Screenshot 2026-01-07 at 9.54.png")

You can also check on the managed device’s end by opening System Settings: General: Device Management, locating the MDM enrollment profile in the list of profiles and double-clicking on it. When you scroll to the bottom of the enrollment profile’s window, you should see a **Device Declarations** section.

If you’re deploying a software update settings configuration via Blueprints, you should see a **Software Update Settings** listing for **Software Update** in the **Device Declarations** section.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-07-at-9.57.39am.png?w=595 "Screenshot 2026-01-07 at 9.57.39 AM.png")

If you click on the **Software Update Settings** listing, it should report the following for the beta program settings:

* Beta program enrollment: **AlwaysOn**
* Require Specific Beta Program: **macOS Tahoe beta program**

**![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-07-at-9.57.45am.png?w=595 "Screenshot 2026-01-07 at 9.57.45 AM.png")**

You can also see the details of what’s configured in **System Settings**: **General**: **Software Update**. In this case, it’s showing the latest macOS Tahoe beta version available for installation.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-07-at-9.58.05am.png?w=595 "Screenshot 2026-01-07 at 9.58.05 AM.png")

You can also click on the **( i )** button next to the **Beta Updates** section and see the settings which have been applied, as well as a notification that the settings are managed.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-07...