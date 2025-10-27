---
title: Deploying software update declarations using Blueprints in Jamf Pro
url: https://derflounder.wordpress.com/2025/08/03/deploying-software-update-declarations-using-blueprints-in-jamf-pro/
source: Der Flounder
date: 2025-08-04
fetch_date: 2025-10-07T00:12:51.684086
---

# Deploying software update declarations using Blueprints in Jamf Pro

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro Blueprints](https://derflounder.wordpress.com/category/jamf-pro-blueprints/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Deploying software update declarations using Blueprints in Jamf Pro

## Deploying software update declarations using Blueprints in Jamf Pro

August 3, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

One of the management options Jamf Pro now provides with Blueprints is sending DDM declarations to managed Macs run macOS software updates automatically. This is comparable to Jamf Pro’s [managed software update functionality](https://derflounder.wordpress.com/2025/06/02/using-jamf-pros-managed-software-updates-for-macos/), which also provides the ability to send a DDM declaration to run software updates.

For those familiar with Jamf Pro’s managed software update functionality, the Blueprints software update declaration provides the following update options:

* **Download and schedule to install**
* **Specific version**

The **Specific version** functionality in the managed software update functionality tells the managed Mac to download and install the update for a specific macOS version, like macOS 15.6.0.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/08/screenshot-2025-08-01-at-2.43.png?w=595 "Screenshot 2025-08-01 at 2.43.png")

The Blueprints software update declaration option provides that same experience, where you can do the following:

* Set a date that you want to have your Macs updated by.
* Set the OS version you want to update to.

For more details, please see below the jump.

For this example, I have the goal of updating managed Macs to the following version of macOS:

* macOS 15.6.0

I want to have them all updated by Friday, August 1 2025 at 6:00 PM (18:00)

I can set up a Blueprint in Jamf Pro to deploy a software update declaration to enforce this using the following procedure:

1. Log into Jamf Pro.

2. Select Blueprints

3. Click on **Update software to latest version**.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/08/screenshot-2025-08-01-at-4.43.png?w=595 "Screenshot 2025-08-01 at 4.43.png")

4. Give it a name when prompted. For this example, I’m using **Update to macOS 15.6**.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/08/screenshot-2025-08-01-at-4.45.png?w=595 "Screenshot 2025-08-01 at 4.45.png")

5. Select a Jamf Pro smart or static group. For this example, I’m selecting a static group named **Managed Software Update Deployment Group**.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/08/screenshot-2025-08-01-at-4.46.png?w=595 "Screenshot 2025-08-01 at 4.46.png")

6. In the **Software Updates** section, I’m choosing the following settings:

* **Date and time of the update**:

+ **08/01/2025, 18:00**

* **Target OS version**:

+ **15.6**

**![](https://derflounder.wordpress.com/wp-content/uploads/2025/08/screenshot-2025-08-01-at-4.47.png?w=595 "Screenshot 2025-08-01 at 4.47.png")**

**Note**: The options available via Blueprints for software declarations are the ones Apple has specified for software update declarations. For more information about this topic, please see the following link:

<https://support.apple.com/guide/deployment/software-update-declarative-configuration-depca14ecd4d/web>

7. Once all the information has been entered and verified to be correct, click the **Save** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/08/screenshot-2025-08-01-at-4.47-1.png?w=595 "Screenshot 2025-08-01 at 4.47.png")

Once everything has been configured, Jamf Pro should inform you that you have undeployed changes. Click the **Deploy** button to deploy the changes to the Macs you want to manage.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/08/screenshot-2025-08-01-at-4.49.png?w=595 "Screenshot 2025-08-01 at 4.49.png")

Once deployed, the Blueprints screen in Jamf Pro should show the newly-created **Update to macOS 15.6** Blueprint as being deployed.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/08/screenshot-2025-08-01-at-4.51.png?w=595 "Screenshot 2025-08-01 at 4.51.png")

On your managed devices, you can verify that the new service background task configuration has been deployed by clicking on the enrollment profile, then scrolling to the bottom. In the case of this example, you should see a **Device Declarations** section with a listing for **Software Update**.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/08/screenshot-2025-08-01-at-4.58.32pm.png?w=595 "Screenshot 2025-08-01 at 4.58.32 PM.png")

If you click on that listing, you should see the details of the software update declaration.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/08/screenshot-2025-08-01-at-4.58.44pm.png?w=595 "Screenshot 2025-08-01 at 4.58.44 PM.png")

From the user’s perspective, they should see a Notifications center notification appear with two available options:

* **Details**
* **Update**

When you click the **Details** button, you should see behavior similar to what’s shown below:

When you click the **Update** button, you should see behavior similar to what’s shown below:

**Note:** *The video above has been edited to artificially reduce the amount of time the OS update took to run. Run time of the pre-edited video was 14 minutes 42 seconds.*

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2025/08/03/deploying-software-update-declarations-using-blueprints-in-jamf-pro/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2025/08/03/deploying-software-update-declarations-using-blueprints-in-jamf-pro/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2025/08/03/deploying-software-update-declarations-using-blueprints-in-jamf-pro/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2025/08/03/deploying-software-update-declarations-using-blueprints-in-jamf-pro/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2025/08/03/deploying-software-update-declarations-using-blueprints-in-jamf-pro/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2025/08/03/deploying-software-update-declarations-using-blueprints-in-jamf-pro/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2025/08/03/deploying-software-update-declarations-using-blueprints-in-jamf-pro/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2025/08/03/deploying-software-update-declarations-using-blueprints-in-jamf-pro/?share=pocket)

Like Loading...

### *Related*

Categories: [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro Blueprints](https://derflounder.wordpress.com/category/jamf-pro-blueprints/), [Mac administration](https://derflounder.wordpress.com/category/mac-adminis...