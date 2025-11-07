---
title: Deploying software update declarations for automatic OS upgrades using Blueprints in Jamf Pro
url: https://derflounder.wordpress.com/2025/11/06/deploying-software-update-declarations-for-automatic-os-upgrades-using-blueprints-in-jamf-pro/
source: Der Flounder
date: 2025-11-06
fetch_date: 2025-11-07T03:09:06.175117
---

# Deploying software update declarations for automatic OS upgrades using Blueprints in Jamf Pro

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [Jamf Pro Blueprints](https://derflounder.wordpress.com/category/jamf-pro-blueprints/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Deploying software update declarations for automatic OS upgrades using Blueprints in Jamf Pro

## Deploying software update declarations for automatic OS upgrades using Blueprints in Jamf Pro

November 6, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

One of the management options Jamf Pro provides with Blueprints is sending DDM declarations to managed Macs run macOS software updates automatically. This is comparable to Jamf Pro’s [managed software update functionality](https://derflounder.wordpress.com/2025/06/02/using-jamf-pros-managed-software-updates-for-macos/), which also provides the ability to send a DDM declaration to run software updates.

Previously, the only option for deploying software update declarations via Blueprints was to [specify an individual OS version](https://derflounder.wordpress.com/2025/08/03/deploying-software-update-declarations-using-blueprints-in-jamf-pro/). Now there is a new option for upgrading the OS version to the latest version a particular Mac can support.

For those familiar with Jamf Pro’s managed software update functionality, the new software update declaration functionality provides the following update options:

* **Download and schedule to install**
* **Latest version based on device eligibility**

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-08-01-at-2.43.12pm.png?w=595 "Screenshot 2025-08-01 at 2.43.12 PM.png")

The **Latest version based on device eligibility** functionality in the managed software update functionality tells the managed Mac to download and install the latest version of macOS that a particular Mac can support. The Blueprints software update declaration functionality provides that same experience, where you can do the following:

* Set that you want the managed Macs to update their OS version to the latest version of macOS a particular Mac can support.
* Set a deadline that you want to have your Macs updated by.

For more details, please see below the jump.

For this example, I have the goal of updating managed Macs to the latest available version of macOS. As of November 6 2025, that is the following version of macOS:

* macOS 26.1

I want to have them all updated within one day of the release of new OS versions, with the install time set as being 6:00 PM (18:00)

I can set up a Blueprint in Jamf Pro to deploy a software update declaration to enforce this using the following procedure:

1. Log into Jamf Pro.

2. Select Blueprints

3. Click on **Update software to latest version**.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-06-at-10.29.png?w=595 "Screenshot 2025-11-06 at 10.29.png")

4. Give it a name when prompted. For this example, I’m using **Update to latest macOS version**.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-06-at-10.29-1.png?w=595 "Screenshot 2025-11-06 at 10.29.png")

5. Select a Jamf Pro smart or static group. For this example, I’m selecting a static group named **Managed Software Update Deployment Group**.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-06-at-10.29-2.png?w=595 "Screenshot 2025-11-06 at 10.29.png")

6. In the **Software Updates** section, I’m choosing the following settings:

* **Enforcement type:**
  + **Latest OS version**
* **Days after release to enforce update:**
  + **1**
* **Install at (local device time):**
  + **18:00**

7. Once all the information has been entered and verified to be correct, click the **Save** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-06-at-10.32.png?w=595 "Screenshot 2025-11-06 at 10.32.png")

8. Click the **Deploy** button to deploy the changes to the Macs you want to manage.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-06-at-10.33.png?w=595 "Screenshot 2025-11-06 at 10.33.png")

**Note:** The days after release refers to the date that the latest version was released. In the case of macOS 26.1, that was on the following date:

* November 3, 2025

By setting the **Days after release to enforce update** setting to 1 day, that means that Macs receiving this software update declarations will have this deadline to install macOS 26.1:

* November 4, 2025 at 18:00 (6:00 PM in the Mac’s local time zone)

Devices receiving the Blueprint will detect that they are past the deadline set by the software update declaration if the Blueprint is being deployed on the following date:

* November 6, 2025

In this case, the Mac will try to update as soon as possible and provide notifications that it is past the deadline for updating.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-06-at-10.35.00am.png?w=595 "Screenshot 2025-11-06 at 10.35.00 AM.png")

Once deployed, the Blueprints screen in Jamf Pro should show the newly-created **Update to latest macOS version** Blueprint as being deployed.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-06-at-10.33-1.png?w=595 "Screenshot 2025-11-06 at 10.33.png")

**Note:** The options available via Blueprints for software declarations are the ones Apple has specified for software update declarations. For more information about this topic, please see the following link:

<https://support.apple.com/guide/deployment/software-update-declarative-configuration-depca14ecd4d/web>

On your managed devices, you can verify that the new service background task configuration has been deployed by clicking on the enrollment profile, then scrolling to the bottom. In the case of this example, you should see a **Device Declarations** section with a listing for **Required** **Software Update**. The **Required Software Update** listing will include the OS version number for the required update.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-06-at-10.35.22am.png?w=595 "Screenshot 2025-11-06 at 10.35.22 AM.png")

If you click on that listing, you should see the details of the software update declaration. In this case, since the latest available version of macOS is 26.1, that’s what is listed as part of the software update declaration.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-06-at-10.35.32am.png?w=595 "Screenshot 2025-11-06 at 10.35.32 AM.png")

From the user’s perspective, they should see a Notifications center notification appear with two available options:

* **Details**
* **Update**

When you click the **Details** button, you should see behavior similar to what’s shown below:

When you click the **Update** button, you should see behavior similar to what’s shown below:

**Note:** *The video above has been edited to artificially reduce the amount of time the OS update took to run. Run time of the pre-edited video was 12 minutes 33 seconds.*

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2025/11/06/deploying-software-update-declarations-for-automatic-os-upgrades-using-blueprints-in-jamf-pro/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window...