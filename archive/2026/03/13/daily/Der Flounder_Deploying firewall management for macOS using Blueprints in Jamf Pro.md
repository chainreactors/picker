---
title: Deploying firewall management for macOS using Blueprints in Jamf Pro
url: https://derflounder.wordpress.com/2026/03/13/deploying-firewall-management-for-macos-using-blueprints-in-jamf-pro/
source: Der Flounder
date: 2026-03-13
fetch_date: 2026-03-14T04:02:56.891344
---

# Deploying firewall management for macOS using Blueprints in Jamf Pro

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro Blueprints](https://derflounder.wordpress.com/category/jamf-pro-blueprints/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/) > Deploying firewall management for macOS using Blueprints in Jamf Pro

## Deploying firewall management for macOS using Blueprints in Jamf Pro

March 13, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As part of Apple’s unveiling of Declarative Device Management (DDM) at WWDC 2023, Apple announced that DDM management included the ability to deploy MDM configuration profiles using DDM as the delivery mechanism in place of using MDM to deliver the profiles. Jamf Pro’s [Blueprints](https://learn.jamf.com/en-US/bundle/jamf-pro-blueprints-configuration-guide/page/Jamf_Pro_Blueprints_Configuration_Guide.html) leverages this capability to support managing the settings for the [built-in application firewall](https://support.apple.com/en-eg/guide/mac-help/mh34041/mac) on macOS. Let’s see how this works with the following settings for the firewall:

* Firewall enabled
* [Stealth mode](https://support.apple.com/en-eg/guide/mac-help/mh17133/mac) enabled
* User changes to the firewall disabled

For more details, please see below the jump.

As of Jamf Pro 11.25.2, there is not a Blueprints template available for creating blueprints which manage firewall settings so the blueprint will need to be configured manually. To do this, use the following procedure:

1. Log into Jamf Pro.

2. Select **Blueprints**.

3. Click the **Create blueprint** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-13-at-8.36.png?w=595 "Screenshot 2026-03-13 at 8.36.png")

4. You should see an unconfigured Blueprint. Click where it says **Untitled blueprint** and provide a name.

For this example, I’m using **Firewall Management Settings**.

5. Scroll down in the list on the left-hand side of the browser window to locate the **Firewall** component.

**Note:** The **Firewall** component is listed as being the **Legacy Payload** type. In Blueprints, a **Legacy Payload** type indicates that this is an MDM configuration profile being delivered via DDM.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-13-at-8.37.png?w=595 "Screenshot 2026-03-13 at 8.37.png")

6. Click on the **Firewall** component and drag the **Firewall** component to the **Components in this blueprint** section.

![Firewall component click and drag.](https://derflounder.wordpress.com/wp-content/uploads/2026/03/firewall_component_click_and_drag.gif?w=595 "firewall_component_click_and_drag.gif")

7. Once added to the **Components in this blueprint** section, click anywhere on the **Firewall** component to open it for editing.

8. At this point, you will see the firewall management settings (with one exception which will be covered in following steps.) To apply the desired settings, select the following options and set them to **T****rue**:

* **EnableFirewall**
* **EnableStealthMode**

9. Once all the settings choices have been made and verified, click the **Save changes** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-13-at-9.04.png?w=595 "Screenshot 2026-03-13 at 9.04.png")

10. The remaining setting (disabling the ability for the user to make changes to the firewall) is in the separate **Security Preferences** component.

Scroll down in the list on the left-hand side of the browser window to locate the **Security Preferences** component.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-13-at-9.07.png?w=595 "Screenshot 2026-03-13 at 9.07.png")

11. Click on the **Security Preferences** component and drag the **Security Preferences** component to the **Components in this blueprint** section.

![Security preferences component click and drag.](https://derflounder.wordpress.com/wp-content/uploads/2026/03/security_preferences_component_click_and_drag.gif?w=595 "security_preferences_component_click_and_drag.gif")

12. Once added to the **Components in this blueprint** section, click anywhere on the **Security Preferences** component to open it for editing.

13. At this point, you will see the **Security Preferences** management settings. To apply the desired setting, select the following option and set it to **T****rue**:

* **Do not allow firewall**

14. Once all the settings choices have been made and verified, click the **Save changes** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-13-at-9.11.png?w=595 "Screenshot 2026-03-13 at 9.11.png")

15. At this point, you should have a blueprint which has all settings configured but where no target scope has been set. To scope this blueprint, go to the **Scope** section and click the arrow button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-13-at-9.12.png?w=595 "Screenshot 2026-03-13 at 9.12.png")

16. Select a Jamf Pro smart or static group. For this example, I’m selecting a static group named **Firewall Settings Deployment Group**.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-13-at-9.17.png?w=595 "Screenshot 2026-03-13 at 9.17.png")

17. Once everything has been configured, click the **Deploy** button to deploy the changes to the Macs you want to manage.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-13-at-9.17-1.png?w=595 "Screenshot 2026-03-13 at 9.17.png")

18. Once deployed, the Blueprints screen in Jamf Pro should show the newly-created **Firewall Management Settings** Blueprint as being deployed.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-13-at-9.18.png?w=595 "Screenshot 2026-03-13 at 9.18.png")

You can also check on the managed device’s end by opening **System Settings**: **General**: **Device Management**, locating the MDM enrollment profile in the list of profiles and double-clicking on it. When you scroll to the bottom of the enrollment profile’s window, you should see a **Device Declarations** section.

If you’re deploying a legacy profile via Blueprints, you should see a **Profiles** section in **Device Declarations**. In the **Profiles** section, there is a listing with a name that matches the name of the blueprint which was deployed. In the case of our example, the listing shows **Firewall Management Settings**.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-13-at-9.19.43am.png?w=595 "Screenshot 2026-03-13 at 9.19.43 AM.png")

If you click on the **Firewall Management Settings** listing, you should see the details of what is being managed.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-13-at-9.20.16am.png?w=595 "Screenshot 2026-03-13 at 9.20.16 AM.png")

**Note:** The MDM profiles delivered via Blueprints are not signed. This is mentioned in the documentation available via the link below:

<https://learn.jamf.com/en-US/bundle/jamf-pro-blueprints-configuration-guide/page/Blueprint_Builder.html>

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-13-at-9.21.png?w=595 "Screenshot 2026-03-13 at 9.21.png")

You can also verify that the firewall is turned on and not editable by the user by going to **System Settings**...