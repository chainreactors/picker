---
title: Deploying AirPrint printers using Blueprints in Jamf Pro
url: https://derflounder.wordpress.com/2025/06/28/deploying-airprint-printers-using-blueprints-in-jamf-pro/
source: Der Flounder
date: 2025-06-29
fetch_date: 2025-10-06T22:53:21.004274
---

# Deploying AirPrint printers using Blueprints in Jamf Pro

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro Blueprints](https://derflounder.wordpress.com/category/jamf-pro-blueprints/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/) > Deploying AirPrint printers using Blueprints in Jamf Pro

## Deploying AirPrint printers using Blueprints in Jamf Pro

June 28, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As part of Apple’s unveiling of Declarative Device Management (DDM) at WWDC 2023, Apple announced that DDM management included the ability to deploy MDM configuration profiles using DDM as the delivery mechanism in place of using MDM to deliver the profiles.  [Jamf Pro’s Blueprints](https://learn.jamf.com/en-US/bundle/jamf-pro-blueprints-configuration-guide/page/Jamf_Pro_Blueprints_Configuration_Guide.html) leverages this capability to support deploying printers which can use AirPrint. Let’s see how this works with an AirPrint configuration, using an AirPrint-compatible printer which is set to use the following static IP address:

**10.0.1.10**

For more details, please see below the jump.

The first thing we need to do is use the [ippfind](https://macosbin.com/bin/ippfind) command line tool to discover information about the printer we want to set up and print to. This process is described as part of Apple’s documentation for AirPrint payload settings for Apple devices, available via the link below:

<https://support.apple.com/guide/deployment/airprint-payload-settings-dep3b4cf515/web> (see the **Set up an AirPrint printer in Apple Configurator for Mac** section.)

Use the procedure below to discover the information needed:

1. Open Terminal.

2. Run the following command without root privileges:

**ippfind**

In this example, we’re getting back the following information about the printer:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@ZWCM2JG74W ~ % ippfind |
|  | ipp://BRN466371FFF599.local:631/ipp/print |
|  | username@ZWCM2JG74W ~ % |

[view raw](https://gist.github.com/rtrouton/e1f6df6200fce19abc4b6a1cde1452be/raw/3e1c4624a9edd5061705050702b809b228ca9fda/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/e1f6df6200fce19abc4b6a1cde1452be#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-28-at-1.01.01pm.png?w=595 "Screenshot 2025-06-28 at 1.01.01 PM.png")

From this, we can see the following information about the printer:

* Bonjour hostname: **BRN466371FFF599.local**
* Port number: **631**
* Resource path: **/ipp/print**

We can use the **BRN466371FFF599.local** hostname to look up what the IP address of the responding printer is, which in this example is going to be the following IP address:

**10.0.1.10**

The port number is **631**, or the default for the IPP protocol.

The resource path is **/ipp/print**, which we will need for setting up the AirPrint configuration in Blueprints.

Once we have this information, we’re ready to set up the AirPrint printer settings for deployment using Blueprints.

As of Jamf Pro 11.18.0, there is not a Blueprints template available for creating blueprints which manage AirPrint settings so the blueprint will need to be configured manually. To do this, use the following procedure:

1. Log into Jamf Pro.

2. Select Blueprints

3. Click the **Create blueprint** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-28-at-1.08.png?w=595 "Screenshot 2025-06-28 at 1.08.png")

4. Give it a name when prompted and click the **Create** button. For this example, I’m using **Reception Desk Printer Settings**.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-28-at-1.08-1.png?w=595 "Screenshot 2025-06-28 at 1.08.png")

5. You should see an unconfigured Blueprint. Scroll down in the list on the right-hand side of the browser window to locate the AirPrint component.

**Note:** AirPrint is listed as **Legacy Payload**. In Blueprints, a **Legacy Payload** type indicates that this is an MDM configuration profile being delivered via DDM.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-28-at-1.09.png?w=595 "Screenshot 2025-06-28 at 1.09.png")

6. Click on the **AirPrint** component and drag the **AirPrint** component to the **Declaration group** section.

![Drag airprint component.](https://derflounder.wordpress.com/wp-content/uploads/2025/06/drag_airprint_component.gif?w=595 "drag_airprint_component.gif")

7. Mouse over the **AirPrint** component and you will see a **Configure** button appear. Click the **Configure** button.

![Configure airprint component.](https://derflounder.wordpress.com/wp-content/uploads/2025/06/configure_airprint_component.gif?w=595 "configure_airprint_component.gif")

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-28-at-1.10.png?w=595 "Screenshot 2025-06-28 at 1.10.png")

8. At this point, you will see an **Air print** section without any listed printers. Click the **Add New Item** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-28-at-1.10-1.png?w=595 "Screenshot 2025-06-28 at 1.10.png")

9. To add the settings for the printer in this example, set the following entries as follows:

* IP Address:
  + **10.0.1.10**
* Resource path:
  + **/ipp/print**
* Port Number:
  + Make no changes
* Force TLS:
  + Make no changes

**Note:** Because we verified earlier that this printer is using port 631, which is the default port for the IPP protocol, it is not necessary to set the port number in the example AirPrint configuration we’re creating. In the event a printer does not use port 631, it would be necessary to set the port number here in the AirPrint configuration.

Likewise, if the printer was using TLS to secure the printer connection, it may be necessary to use the **Force TLS** setting. In this example, TLS is not being used so it is not necessary to configure the **Force TLS** setting.

10. Once all the settings choices have been made and verified, click the **Save** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-28-at-1.11.png?w=595 "Screenshot 2025-06-28 at 1.11.png")

11. At this point, you should have a blueprint which has all settings configured but where no target scope has been set. To scope this blueprint, go to the **Scope** section and click the **Open** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-28-at-1.11-1.png?w=595 "Screenshot 2025-06-28 at 1.11.png")

For this example, I’m selecting a static group named **Printer Deployment Group**.

Once the desired smart and/or static groups have been set and verified for the scope, click the **Save** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-28-at-1.11.30-pm.png?w=595 "Screenshot 2025-06-28 at 1.11.30 PM.p...