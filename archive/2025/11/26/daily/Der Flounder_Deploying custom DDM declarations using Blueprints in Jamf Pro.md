---
title: Deploying custom DDM declarations using Blueprints in Jamf Pro
url: https://derflounder.wordpress.com/2025/11/26/deploying-custom-ddm-declarations-using-blueprints-in-jamf-pro/
source: Der Flounder
date: 2025-11-26
fetch_date: 2025-11-27T03:09:32.604166
---

# Deploying custom DDM declarations using Blueprints in Jamf Pro

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [Jamf Pro Blueprints](https://derflounder.wordpress.com/category/jamf-pro-blueprints/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Deploying custom DDM declarations using Blueprints in Jamf Pro

## Deploying custom DDM declarations using Blueprints in Jamf Pro

November 26, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

One of the management options Jamf Pro provides with Blueprints is the ability to [create and deploy custom declarative declarations](https://learn.jamf.com/en-US/bundle/jamf-pro-blueprints-configuration-guide/page/Blueprint_Builder.html#task-6845) to managed Macs. What this means that if you can manually build the JSON payload for a DDM declaration, you should now be able to deploy it using Blueprints even if Jamf does not yet have a Blueprint template available yet for that declaration. This is conceptually similar to Jamf Pro’s ability to deploy [custom configurations in management profiles to macOS](https://learn.jamf.com/en-US/bundle/technical-articles/page/Deploying_Custom_Computer_Configuration_Profiles_Using_the_Application_and_Custom_Settings_Payload.html) using the **Application & Custom Settings** management profile payload

For more details, please see below the jump.

For this example, I am using the following custom declaration to set disk management settings. Blueprints also has a [declaration template for disk management](https://derflounder.wordpress.com/2025/06/11/deploying-disk-management-using-blueprints-in-jamf-pro/), but using a custom declaration to deploy disk management settings allows the use of an example where that declaration is all in one JSON payload and doesn’t need to refer to other components (an example of a declaration which needs to refer to other components is a [service configuration declaration deploying a sudo configuration](https://derflounder.wordpress.com/2025/05/27/deploying-sudo-configurations-using-blueprints-in-jamf-pro/), where files need to be downloaded from an external source.)

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | { |
|  | "Restrictions": { |
|  | "ExternalStorage": "Disallowed", |
|  | "NetworkStorage": "Disallowed" |
|  | } |
|  | } |

[view raw](https://gist.github.com/rtrouton/d2f52e1a4647bc6f1811494af2f0ee69/raw/19e843a02c94092918cd4b271ffc74ead4462a12/com.apple.configuration.diskmanagement.settings.json)
 [com.apple.configuration.diskmanagement.settings.json](https://gist.github.com/rtrouton/d2f52e1a4647bc6f1811494af2f0ee69#file-com-apple-configuration-diskmanagement-settings-json)
hosted with ❤ by [GitHub](https://github.com)

In this case, the declaration is setting the following [disk management settings](https://developer.apple.com/documentation/devicemanagement/diskmanagementsettings):

* External storage devices are disallowed: the system can’t mount any external storage.
* Network storage is disallowed: the system can’t mount any storage from a network server.

As of Jamf Pro 11.22.1, there is not a Blueprints template available for creating blueprints which deploy custom declarations so the blueprint will need to be configured manually. To do this, use the following procedure:

1. Log into Jamf Pro.

2. Select Blueprints

3. Click the **Create blueprint** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-26-at-1.19.png?w=595 "Screenshot 2025-11-26 at 1.19.png")

4. You should see an unconfigured Blueprint. Click where it says **Untitled blueprint** and provide a name.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-26-at-1.49.png?w=595 "Screenshot 2025-11-26 at 1.49.png")

For this example, I’m using **Disk Management Settings**.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-26-at-1.50.png?w=595 "Screenshot 2025-11-26 at 1.50.png")

5. Scroll down in the list on the left-hand side of the browser window to locate the **Custom Declarations** component.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-26-at-1.51.png?w=595 "Screenshot 2025-11-26 at 1.51.png")

6. Click on the **Custom Declarations** component and drag the **Custom Declarations** component to the **Declaration group** section.

![Drag custom declarations component.](https://derflounder.wordpress.com/wp-content/uploads/2025/11/drag_custom_declarations_component.gif?w=595 "drag_custom_declarations_component.gif")

7. Once added to the **Declaration group** section, click anywhere on the **Custom Declarations** component to open it for editing.

When the Custom Declarations component opens for editing, there is an explanation about custom configurations and a warning that using custom configurations can come with risks and to carefully test all configurations built using the Custom Declarations component before deploying them in a production environment.

8. Once you’ve read through the warnings and understand the potential risks, click the **Get Started** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-26-at-1.56.png?w=595 "Screenshot 2025-11-26 at 1.56.png")

9. Click the **Add item** button. The custom declarations settings will open and show a set of placeholder settings.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-26-at-2.01.png?w=595 "Screenshot 2025-11-26 at 2.01.png")

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-26-at-2.15.png?w=595 "Screenshot 2025-11-26 at 2.15.png")

Before continuing further, if you have not already, I strongly recommend reading the [Creating a Custom Declaration Blueprint documentation](https://learn.jamf.com/en-US/bundle/jamf-pro-blueprints-configuration-guide/page/Blueprint_Builder.html#task-6845) to understand all the parts involved in creating a custom declaration using the Custom Declarations Blueprints component.

In the **Kind** field of the Custom Declarations component, there are two choices:

* **Configuration**
* **Asset**

**Configuration**: Settings and policies that define how devices should be configured, functioning similarly to profile payloads.
**Asset**: Data used by configurations such as certificates, configuration files, scripts or other data supported for use in a DDM declaration.

For our example, we’re choosing **Configuration**.

In the **Channel** field of the Custom Declarations component, there are two choices:

* **System**
* **User**

**System**: applies management settings to the device.
**User**: [applies management settings to the MDM-managed user or users](https://derflounder.wordpress.com/2025/09/09/declarative-device-management-user-channel-and-device-channel/).

For our example, we’re choosing **System**.

In the **Type** field, enter the declaration type.

For our example, we’re using the declaration type for disk management: **com.apple.configuration.diskmanagement.settings**

In the **Payload** field, enter the configuration of the declaration in JSON format. For our example, here’s the configuration we’re u...