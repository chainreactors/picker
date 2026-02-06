---
title: Deploying software update declarations for automatic minor OS updates using Blueprints in Jamf Pro
url: https://derflounder.wordpress.com/2026/02/05/deploying-software-update-declarations-for-automatic-minor-os-updates-using-blueprints-in-jamf-pro/
source: Der Flounder
date: 2026-02-05
fetch_date: 2026-02-06T04:08:12.402917
---

# Deploying software update declarations for automatic minor OS updates using Blueprints in Jamf Pro

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro Blueprints](https://derflounder.wordpress.com/category/jamf-pro-blueprints/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Deploying software update declarations for automatic minor OS updates using Blueprints in Jamf Pro

## Deploying software update declarations for automatic minor OS updates using Blueprints in Jamf Pro

February 5, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

Back in November 2025, Jamf released options for [automatically upgrading the OS version of a Mac to the latest version of macOS that a particular Mac can support](https://derflounder.wordpress.com/2025/11/06/deploying-software-update-declarations-for-automatic-os-upgrades-using-blueprints-in-jamf-pro/). However, this upgrade option meant that the Mac could potentially be upgraded to a new major version of macOS as part of the upgrade process.

For example, applying this software update declaration to a Mac running macOS Sequoia 15.7.1 would not upgrade it to the latest version of Sequoia, which is 15.7.3 as of February 5, 2026. Instead the Mac would be upgraded to the latest version of macOS available, which is macOS Tahoe 26.2 as of February 5, 2026.

To address this, now there is an option for updating the OS version to the latest minor version of the OS that the Mac is currently running. Using the example above, now a software update declaration can be applied to update a Mac running macOS Sequoia to the very latest version of macOS Sequoia, but not upgrade the Mac to now run macOS Tahoe.

For those familiar with Jamf Pro’s [managed software update functionality](https://derflounder.wordpress.com/2025/06/02/using-jamf-pros-managed-software-updates-for-macos/), the new software update declaration functionality provides the following update options:

* **Download and schedule to install**
* **Latest minor version**

**![](https://derflounder.wordpress.com/wp-content/uploads/2026/02/screenshot-2026-02-05-at-5.27.png?w=600&h=201 "Screenshot 2026-02-05 at 5.27.png")**

The **Latest minor version** functionality in the managed software update functionality tells the managed Mac to download and install the latest update available to the current version of macOS that a particular Mac is running. The Blueprints software update declaration option provides that same experience, where you can do the following:

* Set that you want the managed Macs to update their OS version using the latest update for the current version of macOS that the Mac is running.
* Set a deadline that you want to have your Macs updated by.

For more details, please see below the jump.

For this example, I have the goal of updating managed Macs to the latest available update for the current version of macOS that the individual Macs are running.

I want to have them all updated within one day of the release of new updates for the current macOS running on the individual Macs, with the install time set as being 6:00 PM (18:00)

I can set up a Blueprint in Jamf Pro to deploy a software update declaration to enforce this using the following procedure:

1. Log into Jamf Pro.

2. Select Blueprints

3. Click on **Update software to latest version**.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/02/screenshot-2026-02-05-at-5.37.png?w=599&h=391 "Screenshot 2026-02-05 at 5.37.png")

4. Give it a name when prompted. For this example, I’m using **Update macOS version**.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/02/screenshot-2026-02-05-at-5.37-1.png?w=599&h=391 "Screenshot 2026-02-05 at 5.37.png")

5. Select a Jamf Pro smart or static group. For this example, I’m selecting a static group named **Managed Software Update Deployment Group**.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/02/screenshot-2026-02-05-at-5.37-2.png?w=600&h=392 "Screenshot 2026-02-05 at 5.37.png")

6. In the **Software Updates** section, I’m choosing the following settings:

* **Enforcement type:**

+ **Latest OS version**

* Check the **Ignore major versions** checkbox (this setting is what restricts your Mac to updating to the latest update available for the current version of macOS that a particular Mac is running.)
* **Days after release to enforce update**:

+ **1**

* **Install at (local device time)**:

+ 18:00

7. Once all the information has been entered and verified to be correct, click the **Save** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/02/screenshot-2026-02-05-at-5.38.png?w=599&h=391 "Screenshot 2026-02-05 at 5.38.png")

8. Click the **Deploy** button to deploy the changes to the Macs you want to manage.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/02/screenshot-2026-02-05-at-5.39.png?w=600&h=396 "Screenshot 2026-02-05 at 5.39.png")

Once deployed, the Blueprints screen in Jamf Pro should show the newly-created **Update macOS version** Blueprint as being deployed.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/02/screenshot-2026-02-05-at-6.36.png?w=599&h=391 "Screenshot 2026-02-05 at 6.36.png")

**Note:** The options available via Blueprints for software declarations are the ones Apple has specified for software update declarations. For more information about this topic, please see the following link:

<https://support.apple.com/guide/deployment/software-update-declarative-configuration-depca14ecd4d/web>

For this example, I’m deploying this Blueprint to a Mac which is running macOS Tahoe 26.0.1. As mentioned previously, as of February 5, 2026, the latest version of macOS Tahoe is macOS 26.2.

On your managed devices that are not yet up to date with all updates for the current version of macOS being run by the Mac, you can verify that the new software update declaration has been deployed by clicking on the enrollment profile, then scrolling to the bottom. In the case of this example, you should see a **Device Declarations** section with a listing for **Software Update**.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/02/screenshot-2026-02-05-at-6.08.51pm.png?w=599&h=518 "Screenshot 2026-02-05 at 6.08.51 PM.png")

Because 26.0.1 has 26.1 and 26.2 as subsequent updates, **Required Software Update** listings for both 26.1 and 26.2 appear. However the Mac will only install 26.2 since that is the latest update for macOS Tahoe.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/02/screenshot-2026-02-05-at-6.09.27pm.png?w=599&h=518 "Screenshot 2026-02-05 at 6.09.27 PM.png")

The user logged into the macOS 26.0.1 Mac should also be prompted to install macOS 26.2 right away, since the declaration is enforcing installing the update at one day after the macOS update’s release date and macOS Tahoe 26.2 was released on December 12, 2025.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/02/screenshot-2026-02-05-at-6.08.43pm.png?w=357&h=98 "Screenshot 2026-02-05 at 6.08.43 PM.png")

On your managed Macs that are fully up to date, you will not see the **Software Update** declaration appearing on the enrollment profile. This is because the Mac is already fully updated and there is nothing for the Mac to do in response to the deployed software update declaration.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/02/screenshot-2026-02-05-at-6.18.53pm.png?w=599&h=518 "Screenshot 2026-02-05...