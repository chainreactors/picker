---
title: Deploying device restrictions management using Blueprints in Jamf Pro
url: https://derflounder.wordpress.com/2025/06/25/deploying-device-restrictions-management-using-blueprints-in-jamf-pro/
source: Der Flounder
date: 2025-06-26
fetch_date: 2025-10-06T22:52:10.316726
---

# Deploying device restrictions management using Blueprints in Jamf Pro

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro Blueprints](https://derflounder.wordpress.com/category/jamf-pro-blueprints/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/) > Deploying device restrictions management using Blueprints in Jamf Pro

## Deploying device restrictions management using Blueprints in Jamf Pro

June 25, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As part of Apple’s unveiling of Declarative Device Management (DDM) at WWDC 2023, Apple announced that DDM management included the ability to deploy MDM configuration profiles using DDM as the delivery mechanism in place of using MDM to deliver the profiles. [Jamf Pro’s Blueprints](https://learn.jamf.com/en-US/bundle/jamf-pro-blueprints-configuration-guide/page/Jamf_Pro_Blueprints_Configuration_Guide.html) leverages this capability to support device restrictions.

Let’s see how this works using a device restriction configuration, using the example of setting the following Apple Intelligence management functions to **false** in order to block the corresponding Apple Intelligence functions on macOS:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  | Restriction | Setting available in version | Description | Key | Key value | Default setting in macOS |
| --- | --- | --- | --- | --- | --- | --- |
|  | Allow Image Playground | macOS 15.0.0 | If key value is set to FALSE, prohibits the use of image generation. | allowImagePlayground | Boolean | TRUE |
|  | Allow Writing Tools | macOS 15.0.0 | If key value is set to FALSE, allows only anonymous access to external services | allowWritingTools | Boolean | TRUE |
|  | Allow Genmoji | macOS 15.0.0 | If key value is set to FALSE, disables Genmoji | allowGenmoji | Boolean | TRUE |
|  | Allow Mail Summary | macOS 15.1.0 | If key value is set to FALSE, prohibits the ability to create email summaries | allowMailSummary | Boolean | TRUE |
|  | Allow Mail Smart Replies | macOS 15.4.0 | If key value is set to FALSE, disables smart replies in Mail. | allowMailSmartReplies | Boolean | TRUE |

[view raw](https://gist.github.com/rtrouton/4680de4d27df5688d6c388ca8dced3a7/raw/d9608fc05ccd2dc59a91cd958f01b2df75c505ea/Apple%20Intelligence%20device%20restrictions.csv)
 [Apple Intelligence device restrictions.csv](https://gist.github.com/rtrouton/4680de4d27df5688d6c388ca8dced3a7#file-apple-intelligence-device-restrictions-csv)
hosted with ❤ by [GitHub](https://github.com)

For more details, please see below the jump.

As of Jamf Pro 11.18.0, there is not a Blueprints template available for creating blueprints which manage device restrictions so the blueprint will need to be configured manually. To do this, use the following procedure:

1. Log into Jamf Pro.

2. Select **Blueprints**

3. Click the **Create blueprint** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-24-at-5.30.png?w=595 "Screenshot 2025-06-24 at 5.30.png")

4. Give it a name when prompted and click the **Create** button. For this example, I’m using **Restrictions Settings for macOS**.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-24-at-5.31.png?w=595 "Screenshot 2025-06-24 at 5.31.png")

5. You should see an unconfigured Blueprint. Scroll down in the list on the right-hand side of the browser window to locate the **Restrictions** component.

**Note**: The **Restrictions** component is listed as being the **Legacy Payload** type. In Blueprints, a **Legacy Payload** type indicates that this is an MDM configuration profile being delivered via DDM.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-24-at-5.31-1.png?w=595 "Screenshot 2025-06-24 at 5.31.png")

6. Click on the **Restrictions** component and drag the **Restrictions** component to the **Declaration group** section.

![Drag restrictions component.](https://derflounder.wordpress.com/wp-content/uploads/2025/06/drag_restrictions_component.gif?w=595 "drag_restrictions_component.gif")

7. Mouse over the **Restrictions** component and you will see a **Configure** button appear. Click the **Configure** button.

![Configure restrictions component.](https://derflounder.wordpress.com/wp-content/uploads/2025/06/configure_restrictions_component.gif?w=595 "configure_restrictions_component.gif")

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-24-at-5.36.png?w=595 "Screenshot 2025-06-24 at 5.36.png")

8. At this point, you will see all available **Restrictions** settings which are available for all Apple platforms. To limit to only those options available for both macOS and Apple Intelligence, you can click the filter button and then select **macOS** in **OS Type** and **Apple Intelligence** in **Category**.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-25-at-10.34.png?w=595 "Screenshot 2025-06-25 at 10.34.png")

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-25-at-10.35.png?w=595 "Screenshot 2025-06-25 at 10.35.png")

9. To apply the desired settings, select the following options and set them to **false**:

* **Allow Genmoji**
* **Allow Image Playground**
* **Allow Mail Smart Replies**
* **Allow manual mail summaries**
* **Allow writing tools**

10. Once all the settings choices have been made and verified, click the **Save** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-25-at-10.36.png?w=595 "Screenshot 2025-06-25 at 10.36.png")

11. At this point, you should have a blueprint which has all settings configured but where no target scope has been set. To scope this blueprint, go to the **Scope** section and click the **Open** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-25-at-10.47.png?w=595 "Screenshot 2025-06-25 at 10.47.png")

For this example, I’m selecting a static group named **Restrictions Deployment Group**.

Once the desired smart and/or static groups have been set and verified for the scope, click the **Save** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-25-at-10.47-1.png?w=595 "Screenshot 2025-06-25 at 10.47.png")

12. Once everything has been configured, Jamf Pro should inform you that you have undeployed changes. Click the **Deploy** button to deploy the new restrictions settings to the Macs you want to manage.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-25-at-10.47-2.png?w=595 "Screenshot 2025-06-25 at 10.47.png")

13. Once deployed, the Blueprints screen in Jamf Pro should show the newly-created **Restrictions Settings for macOS** blueprint as being deployed.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-25-at-10.50.png?w=595 "Screenshot 2025-06-25 at 10.50.png")

You can also check on the managed device’s end by opening **System Settings**: **General**: **Device ...