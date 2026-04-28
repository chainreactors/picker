---
title: Managing Apple Intelligence settings for macOS using Blueprints in Jamf Pro
url: https://derflounder.wordpress.com/2026/04/27/managing-apple-intelligence-settings-for-macos-using-blueprints-in-jamf-pro/
source: Der Flounder
date: 2026-04-27
fetch_date: 2026-04-28T05:27:05.559365
---

# Managing Apple Intelligence settings for macOS using Blueprints in Jamf Pro

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Apple Intelligence](https://derflounder.wordpress.com/category/apple-intelligence/), [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro Blueprints](https://derflounder.wordpress.com/category/jamf-pro-blueprints/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Managing Apple Intelligence settings for macOS using Blueprints in Jamf Pro

## Managing Apple Intelligence settings for macOS using Blueprints in Jamf Pro

April 27, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

Jamf Pro’s [Blueprints](https://learn.jamf.com/en-US/bundle/jamf-pro-blueprints-configuration-guide/page/Jamf_Pro_Blueprints_Configuration_Guide.html) can be used to manage [Apple Intelligence](https://developer.apple.com/apple-intelligence/) settings, in place of [managing these settings using a configuration profile](https://derflounder.wordpress.com/2025/03/31/managing-apple-intelligence-features-on-macos-sequoia-15-4/). Let’s see how this works using the following configuration as an example:

* Genmoji is disabled
* Image Playground is disabled
* Writing Tools are disabled
* Summarizing emails is disabled
* Disable third party cloud-based intelligence service integrations
* Disable non-anonymous login to third party cloud-based intelligence services
* Notes transcription summaries are disabled
* Apple Intelligence reports are disabled
* Mail smart replies are disabled
* Summarizing Safari content is disabled
* Force on-device only dictation

For more details, please see below the jump.

As of Jamf Pro 11.27.0, there is not a Blueprints template available for creating blueprints which manage Apple Intelligence settings so the blueprint will need to be configured manually. To do this, use the following procedure:

1. Log into Jamf Pro.

2. Select Blueprints

3. Click the **Create blueprint** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/04/screenshot-2026-04-27-at-8.57.png?w=595 "Screenshot 2026-04-27 at 8.57.png")

4. You should see an unconfigured Blueprint. Click where it says **Untitled blueprint** and provide a name.

For this example, I’m using **Apple Intelligence Management Settings**.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/04/screenshot-2026-04-27-at-8.57-1.png?w=595 "Screenshot 2026-04-27 at 8.57.png")

5. To manage all of the settings mentioned above, two components will be needed:

* **External Intelligence Settings**
* **Intelligence Settings**

**![](https://derflounder.wordpress.com/wp-content/uploads/2026/04/screenshot-2026-04-27-at-8.58.png?w=595 "Screenshot 2026-04-27 at 8.58.png")**

Scroll down in the list on the left-hand side of the browser window to locate the **External Intelligence Settings** component.

6. Click on the **External Intelligence Settings** component and drag the **External Intelligence Settings** component to the **Components in this blueprint** section.

7. Scroll down in the list on the left-hand side of the browser window to locate the **Intelligence Settings** component.

8. Click on the **Intelligence Settings** component and drag the **Intelligence Settings** component to the **Components in this blueprint** section.

![External intelligence and intelligence settings components click and drag.](https://derflounder.wordpress.com/wp-content/uploads/2026/04/external_intelligence_and_intelligence_settings_components_click_and_drag.gif?w=595 "external_intelligence_and_intelligence_settings_components_click_and_drag.gif")

9. Once added to the **Components in this blueprint** section, click anywhere on the **External Intelligence Settings** component to open it for editing.

10. At this point, you will see the Apple Intelligence management settings. Select the following options to apply the following desired settings:

* **Allow External Intelligence Integrations**:
  + Select **False**
* **Allow External Intelligence Integrations Sign In**:
  + Select **False**

Once all choices have been made and verified, click the **Save** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/04/screenshot-2026-04-27-at-9.05.42-am.png?w=595 "Screenshot 2026-04-27 at 9.05.42 AM.png")

11. Click anywhere on the **Intelligence Settings** component to open it for editing.

At this point, you will see all available Intelligence settings which are available for all Apple platforms. To limit to only those options available for macOS, you can click the filter button and then select macOS in OS Type.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/04/screenshot-2026-04-27-at-9.09.png?w=595 "Screenshot 2026-04-27 at 9.09.png")

![](https://derflounder.wordpress.com/wp-content/uploads/2026/04/screenshot-2026-04-27-at-9.09-1.png?w=595 "Screenshot 2026-04-27 at 9.09.png")

12. At this point, you will see the Apple Intelligence management settings for macOS. Select the following options to apply the following desired settings:

* **Allow Apple Intelligence Report**:
  + Select **False**
* **Allow Genmoji**:
  + Select **False**
* **Allow Image Playground**:
  + Select **False**
* **Allow Writing Tools**
  + Select **False**

![](https://derflounder.wordpress.com/wp-content/uploads/2026/04/screenshot-2026-04-27-at-9.10.png?w=595 "Screenshot 2026-04-27 at 9.10.png")

In the **Apps** section, select the following options to apply the following desired settings:

**Mail**:

* **Allow Smart Replies**:
  + Select **False**
* **Allow Summary**:
  + Select **False**

**Notes**:

* **Allow Transcription**:
  + Select **False**
* **Allow Transcription Summary**:
  + Select **False**

**Safari**:

* **Allow Summary**:
  + Select **False**

![](https://derflounder.wordpress.com/wp-content/uploads/2026/04/screenshot-2026-04-27-at-9.11.png?w=595 "Screenshot 2026-04-27 at 9.11.png")

![](https://derflounder.wordpress.com/wp-content/uploads/2026/04/screenshot-2026-04-27-at-9.13.png?w=595 "Screenshot 2026-04-27 at 9.13.png")

In the section under **Apps**, select the following option to apply the following desired setting:

* **Force On-Device Only Dictation**:
  + Select **True**

![](https://derflounder.wordpress.com/wp-content/uploads/2026/04/screenshot-2026-04-27-at-9.16-1.png?w=595 "Screenshot 2026-04-27 at 9.16.png")

Once all choices have been made and verified, click the **Save** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/04/screenshot-2026-04-27-at-9.16.png?w=595 "Screenshot 2026-04-27 at 9.16.png")

13. At this point, you should have a blueprint which has all settings configured but where no target scope has been set. To scope this blueprint, go to the **Scope** section and click the arrow button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/04/screenshot-2026-04-27-at-9.18.png?w=595 "Screenshot 2026-04-27 at 9.18.png")

14. Select a Jamf Pro smart or static group. For this example, I’m selecting a static group named **Apple Intelligence Settings Deployment Group**.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/04/screenshot-2026-04-27-at-9.20.png?w=595 "Screenshot 2026-04-27 at 9.20.png")

15. Once everything has been configured, click the **Deploy** button to deploy the changes to the Macs you want to manage.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/04/screenshot-2026-04-27-at-9.27.png?w=595 "Screenshot 2026-04-27 at 9.27.png")

16. Once deployed, the Blueprints screen in Jamf Pro should ...