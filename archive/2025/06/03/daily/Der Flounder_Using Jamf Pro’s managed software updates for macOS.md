---
title: Using Jamf Pro’s managed software updates for macOS
url: https://derflounder.wordpress.com/2025/06/02/using-jamf-pros-managed-software-updates-for-macos/
source: Der Flounder
date: 2025-06-03
fetch_date: 2025-10-06T22:51:28.236343
---

# Using Jamf Pro’s managed software updates for macOS

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Using Jamf Pro’s managed software updates for macOS

## Using Jamf Pro’s managed software updates for macOS

June 2, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

One of the management options Jamf Pro provides is sending MDM commands or DDM declarations to managed Macs run macOS software updates automatically. For Macs, Jamf Pro includes this functionality in the **Software Updates** section under **Computers**. If you have not previously used the **Software Updates** functionality, by default it is turned off and needs to be enabled.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-01-at-12.49.png?w=599&h=341 "Screenshot 2025-06-01 at 12.49.png")

Once enabled, you should see a list of the smart and static computer groups set up on your Jamf Pro server. To set up a software update plan for one of those groups, click the desired group and then click **Update 1 Selected**.

**Note**: It’s possible to select multiple groups at once and set the same software plan for all selected groups.

![MacOS 15 5 DDM Software Update Select Group Jamf Pro.](https://derflounder.wordpress.com/wp-content/uploads/2025/06/macos_15_5_ddm_software_update_select_group_jamf_pro.png?w=599&h=434 "macOS_15_5_DDM_Software_Update_Select_Group_Jamf_Pro.png")

Once the groups have been selected for update, you’ll be provided with the various options available. Four of these options use MDM commands and one will use a DDM declaration:

**MDM commands**:

* **Download only**
* **Download and install**
* **Download, install and allow deferral**
* **Download, install, and restart**

**DDM declaration**:

* **Download and schedule to install**

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-02-at-9.20.png?w=599&h=340 "Screenshot 2025-06-02 at 9.20.png")

One reason it is important to know which use MDM commands and which use DDM declarations is that the [MDM command method is supported on the following versions of macOS](https://developer.apple.com/documentation/devicemanagement/schedule-os-update-command):

* macOS 10.11 and later

The [DDM declaration method is supported on the following versions of macOS](https://support.apple.com/guide/deployment/software-update-declarative-configuration-depca14ecd4d/web):

* macOS 14 and later

**Note**: The DDM declaration method works for Jamf Pro instances hosted in Jamf Cloud and does not work for on-premise Jamf Pro installations. If you are using an on-premise Jamf Pro installation, the **Download and schedule to install** option is grayed out and there is a note explaining that this method is only supported for Jamf Cloud-hosted environments.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-01-at-12.54.png?w=598&h=340 "Screenshot 2025-06-01 at 12.54.png")

You will also get various update options:

* **Latest version based on device eligibility** – This will download and install the latest version of macOS that the managed device can run.
* **Latest major version** – This will download and install the latest major version of macOS, like macOS 14.0 or macOS 15.0, if the managed device is running an earlier major version of macOS.
* **Latest minor version** – This will download and install the latest update to the major version macOS that the managed device is using, like updating a macOS 15.14.1 device to macOS 15.5
* **Specific version** – This will download and install the update for a specific macOS version, like macOS 15.4.1.

**Note**: The **Specific version** setting assumes that the version in question is still available from Apple’s software update feed. If it is not, then that version will not be downloaded or installed.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-01-at-12.54.09-pm.png?w=340&h=216 "Screenshot 2025-06-01 at 12.54.09 PM.png")

**Managed software update plan behavior**:

Something important to know about managed software update plans is that they were built to act like Jamf Pro’s functionality for sending out [MDM commands](https://learn.jamf.com/en-US/bundle/jamf-pro-documentation-current/page/Remote_Commands_for_Computers.html#ID-0002305d) via [a mass action](https://learn.jamf.com/en-US/bundle/jamf-pro-documentation-current/page/Mass_Actions_for_Computers.html). You select the devices you wanted to apply the mass action to (or in this case, the software update plan) and Jamf Pro would send the commands out. When choosing a smart or static group and setting up a software update plan, the commands for that software update plan will be sent to only the devices in that group at that point in time.

If a device subsequently enters the smart group or static group in question, it will not receive the commands which had been previously sent out. Please note that this also means that leaving the smart or static group will not remove a previously applied software update plan.

For more details, please see below the jump.

**Setting up managed software update plans**:

For how this works, let’s run through an example workflow. For this example workflow, the following assumptions are being made:

1. The Jamf Pro instance sending the software update plan is hosted in Jamf Cloud.
2. The DDM declaration method is being used.
3. One Mac is being updated.
4. The Mac receiving the software update plan is running macOS Sequoia 15.4.1 and updating to the latest OS version the device can support (which in this case should be 15.5.0.)
5. The software update plan is being run at a time prior to May 24, 2025.

With these assumptions, my first step is selecting a group to apply the software update plan to. For this example, I’ve set up a static group named Managed Software Update Deployment Group and assigned one device to it.

1. From the list of groups in the **Software Updates** window, select the **Managed Software Update Deployment Group** static group.

![MacOS 15 5 DDM Software Update Select Group Jamf Pro.](https://derflounder.wordpress.com/wp-content/uploads/2025/06/macos_15_5_ddm_software_update_select_group_jamf_pro.png?w=599&h=434 "macOS_15_5_DDM_Software_Update_Select_Group_Jamf_Pro.png")

2. Click the **Update 1 Selected** button.

![MacOS 15 5 DDM Software Update Select Group Jamf Pro 1.](https://derflounder.wordpress.com/wp-content/uploads/2025/06/macos_15_5_ddm_software_update_select_group_jamf_pro_1.png?w=599&h=434 "macOS_15_5_DDM_Software_Update_Select_Group_Jamf_Pro_1.png")

3. Select the following option to choose the available DDM declaration method:

* **Download and schedule to install**

4. Choose a date by which the software update should apply.

5. Choose the OS version update option.

In this example, I am choosing the **Latest version based on device eligibility** option.

**![MacOS 15 5 DDM Software Update Select Software Update Options Jamf Pro.](https://derflounder.wordpress.com/wp-content/uploads/2025/06/macos_15_5_ddm_software_update_select_software_update_options_jamf_pro.png?w=600&h=435 "macOS_15_5_DDM_Software_Update_Select_Software_Update_Options_Jamf_Pro.png")**

6. Once all choices have been made, verify that they are what is desired. Once verified, click the **Apply** button.

![MacOS 15 5 DDM Software Update Apply Software Update Options Jamf Pro.](https://derflounder.wordpress.com/wp-content/uploads/2025/06/macos_15_5_ddm_softwa...